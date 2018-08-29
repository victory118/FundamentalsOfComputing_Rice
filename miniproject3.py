# Mini-project #3 - "Stopwatch: The Game"

# Project template: http://www.codeskulptor.org/#examples-guess_the_number_template.py

# CodeSkulptor submission link: http://www.codeskulptor.org/#user45_1j7UydRQV28Tdkd_69.py

# template for testing format function: http://www.codeskulptor.org/#examples-gtn_testing_template.py

# helpful examples
# http://www.codeskulptor.org/#examples-timers.py

# import modules
import simplegui

# define global variables
timeElapsed = 0
interval = 100 # 100 msec = 0.1 sec
score = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D_tenthSec = t % 10
    C_sec = (t/10) % 10
    B_tenSec = (t/100) % 6
    A_min = t/600
    
    return str(A_min) + ":" + str(B_tenSec) + str(C_sec) + "." + str(D_tenthSec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()

def Stop():
    global score, attempts
    if timer.is_running():
        if (timeElapsed % 10) == 0:
            score += 1
        attempts += 1
    timer.stop()

def Reset():
    global timeElapsed, score, attempts
    timer.stop()
    timeElapsed = 0
    score = 0
    attempts = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global timeElapsed
    timeElapsed += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(timeElapsed), [25, 100], 36, "Red")
    canvas.draw_text('Time Elapsed:', [25, 50], 24, 'White')
    canvas.draw_text('Score (whole second stops/total stops):', [200, 50], 24, 'White')
    canvas.draw_text(str(score) + '/' + str(attempts), [200, 100], 36, 'Red')

# create frame
frame = simplegui.create_frame("Stopwatch: The Game!", 600, 200)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", Start)
frame.add_button("Stop", Stop)
frame.add_button("Reset", Reset)

# start frame
frame.start()

# Please remember to review the grading rubric
