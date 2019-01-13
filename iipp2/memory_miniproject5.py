# codeskulptor link: http://www.codeskulptor.org/#user45_6rIgmIQtCWcc69u_82.py

# http://www.codeskulptor.org/#examples-mouse_input.py
# http://www.codeskulptor.org/#examples-iteration.py
# http://www.codeskulptor.org/#examples-list_removal.py
# http://www.codeskulptor.org/#examples-list_selection.py
# http://www.codeskulptor.org/#examples-list_of_balls.py
# http://www.codeskulptor.org/#examples-list_methods.py

# http://www.codeskulptor.org/#examples-images.py
# http://www.codeskulptor.org/viz/#examples_iteration_lists.py
# http://www.codeskulptor.org/viz/#examples-dictionaries.py
# http://www.codeskulptor.org/#examples-memory_states.py
# http://www.codeskulptor.org/#examples-memory_template.py

# implementation of card game - Memory

import simplegui
import random

# define variables
num_list = range(8) + range(8)
#exposed = [False for i in range(16)]
#exposed = [random.randrange(2) for i in range(16)]
first_card = 0
second_card = 0
card_clicked = False

# helper function to initialize globals
def new_game():
    global state, turns, exposed, num_list
    random.shuffle(num_list)
    state = 0
    turns = 0
    exposed = [False for i in range(16)]
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, first_card, second_card, card_clicked
    
    if pos[0] > 0 and pos[0] < 800 and pos[1] > 0 and pos[1] < 100:
        card_clicked = True
        card_idx = pos[0] // 50
        
    #print("card_clicked = " + str(card_clicked))
    #print("state = " + str(state))
    
    if not exposed[card_idx]:
        if state == 0:
            exposed[card_idx] = True
            first_card = card_idx
            state = 1
        elif state == 1:
            exposed[card_idx] = True
            second_card = card_idx
            turns+=1
            label.set_text("Turns = " + str(turns))
            state = 2
            
        else:
            if num_list[first_card] != num_list[second_card]:
                exposed[first_card] = False
                exposed[second_card] = False
                
            exposed[card_idx] = True
            first_card = card_idx
            second_card = -1
            state = 1
        
        card_clicked = False
        #print("state = " + str(state))
                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    point = [10, 70]
    card_top = [25, 0]
    card_bottom = [25, 100]
    for idx, num in enumerate(num_list):
        if exposed[idx]:
            # canvas.draw_text(text, point, font_size, font_color)
            num_color = "White"
            if idx == first_card or idx == second_card:
                num_color = "Red"
            canvas.draw_text(str(num), point, 48, num_color)
        else:
            card_points = [(0 + 50*idx, 0), (50 + 50*idx, 0), (50 + 50*idx, 100), (0 + 50*idx, 100)]
            canvas.draw_polygon(card_points, 4, "Gray", "Green")
        point[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric