from psychopy import visual, core, event, gui, data
import random, csv, time, os

# Participant info dialog
info = gui.Dlg(title="Digit Span Task")
info.addField("pOrder")
info.show()

if not info.OK:  # User clicked cancel
    core.quit()
    
pOrder = info.data[0]  # Get participant ID

# Initialize window (now uses full screen dimensions)
win = visual.Window(fullscr = True, color='black', units='pix')
win_width, win_height = win.size  # Get actual display dimensions

# Shortcut to quit in fullscreen
event.clearEvents()

def emergency_quit():
    print("Experiment terminated by user")
    win.close()
    core.quit()

event.globalKeys.add(
    key='escape',
    func=emergency_quit,
    name='forced_quit'
)

# Experiment parameters
params = {
    'nTrials': 14,
    'minSetSize': 3,
    'stimuli_duration': 1.0,
    'recall_duration': None,
    'practiceTrials': 3,
    'maxSetSize': 17,
    'feedbackDuration': 1.0,
    'possibleNumbers': ["1","2","3","4","5","6","7","8","9","0"]
}

# Data structure
data_dict = {
    "pOrder": pOrder,
    "instruction": {"rt_1": None, "rt_2": None},
    "practice": {"trials": []},
    "task": {"trials": []},
    "summary": {},
}

# Tracking variables
selection = []
selection_id = -1
trial_nb_ds = 0
isPract_ds = True
nError = 0
highest_span_score = 0
consec_error_score = 0
recalledGrid = []

# Calculate sizes based on window dimensions
base_size = min(win_width, win_height)  # Use smallest dimension for scaling

# Keypad parameters
button_size = base_size * 0.08  # 8% of screen height
button_spacing = button_size * 1.3  # Space between buttons
vertical_offset = -win_height * 0.15  # Position from bottom

# Create dynamic positions for 3x4 grid
button_positions = [
    ((i%3-1)*button_spacing,  # x position (centered)
     (1-i//3)*button_spacing + vertical_offset)  # y position
    for i in range(12)
]

# Keypad setup
digits = ["1","2","3","4","5","6","7","8","9","⌫","0","✓"]
keypad = []
for i, (digit, pos) in enumerate(zip(digits, button_positions)):
    keypad.append({
        'rect': visual.Rect(
            win=win,
            width=button_size,
            height=button_size,
            pos=pos,
            fillColor="#333333",
            lineColor="white",
            opacity=0.8
        ),
        'text': visual.TextStim(
            win=win,
            text=digit,
            pos=pos,
            height=button_size*0.4,  # Text scales with button
            color="white"
        )
    })

# Dynamic text elements
text_height = base_size * 0.04  # Base text size
digit_stim = visual.TextStim(win, text='', height=text_height*2, color='white')
instructions = visual.TextStim(win, text='', height=text_height, wrapWidth=win_width*0.8)
feedback_text = visual.TextStim(win, text='', height=text_height*1.3)

# Position recall elements dynamically
recall_ypos = win_height * 0.18  # 18% from top
prompt_ypos = win_height * 0.25  # 25% from top

recall_display = visual.TextStim(
    win=win,
    text='',
    pos=(0, recall_ypos),
    height=text_height*1.3,
    wrapWidth=win_width*0.9
)

prompt_text = visual.TextStim(
    win=win,
    text='CLICK the numbers in order:',
    pos=(0, prompt_ypos),
    height=text_height
)

def draw_keypad():
    """Draw all keypad elements with hover effects"""
    mouse = event.Mouse()
    for btn in keypad:
        if btn['rect'].contains(mouse.getPos()):
            btn['rect'].fillColor = "#555555" if not mouse.getPressed()[0] else "#777777"
        else:
            btn['rect'].fillColor = "#333333"
        btn['rect'].draw()
        btn['text'].draw()

def recall_phase(correct_sequence):
    """Handles recall with onscreen keypad"""
    global recalledGrid
    recalledGrid = []
    display_text = ""
    mouse = event.Mouse()
    recall_start = time.time()
    
    while True:
        # Draw all elements
        recall_display.text = display_text
        prompt_text.draw()
        recall_display.draw()
        draw_keypad()
        win.flip()
        
        # Check mouse clicks
        if mouse.getPressed()[0]:  # Left click
            click_pos = mouse.getPos()
            for i, btn in enumerate(keypad):
                if btn['rect'].contains(click_pos):
                    core.wait(0.1)  # Debounce
                    if digits[i] == "⌫":  # Backspace
                        if recalledGrid:
                            recalledGrid.pop()
                            display_text = display_text[:-2]
                    elif digits[i] == "✓":  # Submit
                        if recalledGrid:
                            return (1 if recalledGrid == correct_sequence else 0, 
                                   time.time() - recall_start)
                    else:  # Digit
                        recalledGrid.append(digits[i])
                        display_text += digits[i] + " "
        
        # Timeout check
        if params['recall_duration'] and (time.time() - recall_start > params['recall_duration']):
            return (0, params['recall_duration'])

def show_instructions(text, record_rt_key=None):
    instructions.text = text
    instructions.draw()
    win.flip()
    start_time = time.time()
    
    event.clearEvents()
    keys = event.waitKeys(keyList=['space'])
    rt = time.time() - start_time
    
    if record_rt_key:
        data_dict["instruction"][record_rt_key] = rt
        if record_rt_key == 'rt_2':
            data_dict["start_time"] = time.time()

def generate_sequence(length):
    if length <= 8:
        return random.sample(params['possibleNumbers'], length)
    else:
        seq = random.sample(params['possibleNumbers'], 8)
        extra = length - 8
        possible_temp = [n for n in params['possibleNumbers'] if n != seq[7]]
        seq.extend(random.sample(possible_temp, extra))
        return seq

def show_digits(sequence):
    for digit in sequence:
        digit_stim.text = digit
        digit_stim.draw()
        win.flip()
        core.wait(params['stimuli_duration'])
        win.flip()
        core.wait(0.3)  # ISI

def run_trial():
    global selection, selection_id, trial_nb_ds, isPract_ds
    global nError, highest_span_score, consec_error_score
    
    # Generate new sequence if needed
    if selection_id == -1:
        selection = generate_sequence(params['minSetSize'])
    
    # Show digits
    show_digits(selection)
    
    # Recall phase
    recall_success, rt = recall_phase(selection)
    accuracy = 1 if (recall_success and recalledGrid == selection) else 0
    
    # Update scores
    if accuracy == 1:
        if highest_span_score < params['minSetSize']:
            highest_span_score = params['minSetSize']
        params['minSetSize'] += 1
        nError = 0
    elif nError < 1:
        nError += 1
    else:
        if not isPract_ds and consec_error_score < params['minSetSize']:
            consec_error_score = params['minSetSize'] - 1
        params['minSetSize'] = max(3, params['minSetSize'] - 1)
    
    # Save trial data
    trial_data = {
        "trial_number": trial_nb_ds + 1,
        "set_size": len(selection),
        "stimuli": selection,
        "response": recalledGrid,
        "accuracy": accuracy,
        "rt": rt
    }
    
    if isPract_ds:
        data_dict["practice"]["trials"].append(trial_data)
    else:
        data_dict["task"]["trials"].append(trial_data)
    
    # Show feedback
    feedback_text.text = "Correct" if accuracy else "Incorrect"
    feedback_text.color = 'green' if accuracy else 'red'
    feedback_text.draw()
    win.flip()
    core.wait(params['feedbackDuration'])
    
    # Prepare for next trial
    selection_id = -1
    trial_nb_ds += 1

# ===== RUN EXPERIMENT =====
# Instruction screens 
show_instructions(
    "INSTRUCTIONS\n\nThis is the digit span task.\n\n"
    "You will see a sequence of numbers presented one at a time.\n\n"
    "At the end of each trial, enter all the numbers into the onscreen number-pad in their correct order.\n\n"
    "Use ⌫ to delete last digit\n"
    "Click ✓ when finished\n\n"
    "Example: if you see '7 4 5 1', enter '7 4 5 1' in this exact order.\n\n"
    "Press SPACEBAR to begin practice trials.",
    'rt_1'
)

# Practice trials 
for _ in range(params['practiceTrials']):
    run_trial()

# Transition screen
show_instructions(
    "You have completed the practice trials.\n\n"
    "Press SPACEBAR to proceed to the main trials.",
    'rt_2'
)

# Main trials
isPract_ds = False
params['minSetSize'] = 3  # Reset to starting length
trial_nb_ds = 0  # Reset trial counter

for _ in range(params['nTrials']):
    run_trial()

# Conclusion screen
data_dict["end_time"] = time.time()
data_dict["total_time"] = data_dict["end_time"] - data_dict["start_time"]
data_dict["summary"] = {
    "max_digits_recalled": highest_span_score,
    "max_digits_before_errors": consec_error_score
}

# Save data 
data_folder = 'data'

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

filename = os.path.join(data_folder, f'{pOrder}_digit_span.csv')
fieldnames = ['pOrder', 'rt_1', 'rt_2', 'trial_type', 'trial_num', 'digits', 'response', 'accuracy', 'rt', 'digit_count', 'max_digit', 'max_before_error']

# Create a list to hold all flattened data rows
all_rows = []

# Add instruction times as first row with metadata
instruction_row = {
    'pOrder': pOrder,
    'rt_1': data_dict["instruction"]["rt_1"],
    'rt_2': data_dict["instruction"]["rt_2"],
    'trial_type': 'instruction',
    'trial_num': '',
    'digits': '',
    'response': '',
    'accuracy': '',
    'rt': '',
    'digit_count': '',
    'max_digit': highest_span_score,
    'max_before_error': consec_error_score
}
all_rows.append(instruction_row)

# Add practice trials
for trial in data_dict["practice"]["trials"]:
    trial_row = {
        'pOrder': pOrder,
        'rt_1': '',
        'rt_2': '',
        'trial_type': 'practice',
        'trial_num': trial["trial_number"],
        'digits': ' '.join(trial["stimuli"]),
        'response': ' '.join(trial["response"]),
        'accuracy': trial["accuracy"],
        'rt': trial["rt"],
        'digit_count': trial["set_size"],
        'max_digit': '',
        'max_before_error': ''
    }
    all_rows.append(trial_row)

# Add task trials
for trial in data_dict["task"]["trials"]:
    trial_row = {
        'pOrder': pOrder,
        'rt_1': '',
        'rt_2': '',
        'trial_type': 'task',
        'trial_num': trial["trial_number"],
        'digits': ' '.join(trial["stimuli"]),
        'response': ' '.join(trial["response"]),
        'accuracy': trial["accuracy"],
        'rt': trial["rt"],
        'digit_count': trial["set_size"],
        'max_digit': '',
        'max_before_error': ''
    }
    all_rows.append(trial_row)

# Write the flattened data to CSV
with open(filename, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_rows)

# Show summary 
summary_text = visual.TextStim(win, wrapWidth=700, height=30)
summary_text.text = (
    f"You have completed the task.\n"
    f"Thank you for your participation.\n\n"
    f"Maximum digits recalled correctly: {highest_span_score}\n"
    f"Maximum digits before 2 errors: {consec_error_score}\n\n"
    "The experiment will now end."
)

summary_text.draw()
win.flip()
core.wait(3.0)

win.close()
core.quit()