# submission link: http://www.codeskulptor.org/#user45_WEXgUNPnHk75THn_88.py
# template: http://www.codeskulptor.org/#examples-pong_template.py

# helpful examples
# http://www.codeskulptor.org/#examples-keyboard_echo.py
# http://www.codeskulptor.org/#examples-position_control.py
# http://www.codeskulptor.org/#examples-motion_explicit.py
# http://www.codeskulptor.org/#examples-motion_implicit.py
# http://www.codeskulptor.org/#examples-collisions_and_reflections.py
# http://www.codeskulptor.org/#examples-velocity_control.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [2, 2]
    ball_vel = [random.randrange(3,5), -random.randrange(2,4)]
    if direction == 'LEFT':
        ball_vel[0] = -ball_vel[0]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    # randomize new ball velocity direction
    direction = 'LEFT' if random.randrange(0,2) else 'RIGHT'
    spawn_ball(direction)
    
def Restart():
    new_game()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen

    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= PAD_HEIGHT/2:
        paddle1_pos = PAD_HEIGHT/2
    elif paddle1_pos >= HEIGHT - PAD_HEIGHT/2:
        paddle1_pos = HEIGHT - PAD_HEIGHT/2
        
    if paddle2_pos <= PAD_HEIGHT/2:
        paddle2_pos = PAD_HEIGHT/2
    elif paddle2_pos >= HEIGHT - PAD_HEIGHT/2:
        paddle2_pos = HEIGHT - PAD_HEIGHT/2
        
    # draw paddles
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos - PAD_HEIGHT/2], [PAD_WIDTH/2, paddle1_pos + PAD_HEIGHT/2], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos - PAD_HEIGHT/2], [WIDTH - PAD_WIDTH/2, paddle2_pos + PAD_HEIGHT/2], PAD_WIDTH, 'White')
    
    # determine whether paddle and ball collide
    # ball in left gutter
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos + PAD_HEIGHT/2 and ball_pos[1] >= paddle1_pos-PAD_HEIGHT/2:
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
        else:
            score2 += 1
            spawn_ball("RIGHT")
    
    # ball in right gutter
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] <= paddle2_pos + PAD_HEIGHT/2 and ball_pos[1] >= paddle2_pos-PAD_HEIGHT/2:
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
        else:
            score1 += 1
            spawn_ball("LEFT")
    
    # draw scores
    canvas.draw_text(str(score1), [150, 50], 36, "White")
    canvas.draw_text(str(score2), [450, 50], 36, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    vel = 10
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", Restart)

# start frame
new_game()
frame.start()
