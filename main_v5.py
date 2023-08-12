from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import math
import random



#Midpoint Line Drawing Algorithms
def midpointcircle(x, y, r, color):
    glColor3f(*color) # Set the color
    glBegin(GL_POINT)
    glPointSize(1) #pixel size. by default 1 thake
    
    #N, S, E, W from center
    d = 1.25-r
    x1 = x 
    y1 = y
    x = 0 
    y = r 
    if x1 != 0 or y1!=0:
        glVertex2f(x+x1, y+y1)
        glVertex2f(y+y1, x+x1)
        glVertex2f(y+y1, -x+x1)
        glVertex2f(x+x1, -y+y1)
        glVertex2f(-x+x1, -y+y1)
        glVertex2f(-y+y1, -x+x1)
        glVertex2f(-y+y1, x+x1)
        glVertex2f(-x+x1, y+y1)
    else: 
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)
    while x <= y:
        if d<0:
            #E
            d = d+2*x+3 
            x += 1  
        else:
            d = d + 2*x - 2*y + 5
            x = x + 1 
            y = y - 1 
        if x1 != 0 or y1!=0:
            glVertex2f(x+x1, y+y1)
            glVertex2f(y+y1, x+x1)
            glVertex2f(y+y1, -x+x1)
            glVertex2f(x+x1, -y+y1)
            glVertex2f(-x+x1, -y+y1)
            glVertex2f(-y+y1, -x+x1)
            glVertex2f(-y+y1, x+x1)
            glVertex2f(-x+x1, y+y1)
        else: 
            glVertex2f(x, y)
            glVertex2f(y, x)
            glVertex2f(y, -x)
            glVertex2f(x, -y)
            glVertex2f(-x, -y)
            glVertex2f(-y, -x)
            glVertex2f(-y, x)
            glVertex2f(-x, y)
    glEnd()
            
def draw_circle(x_center, y_center, radius, color):
    glColor3f(*color) # Set the color
    glBegin(GL_POLYGON)
    num_segments = 100 # Number of segments for smooth circle
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        dx = radius * cos(theta)
        dy = radius * sin(theta)
        glVertex2f(dx + x_center, dy + y_center)
    glEnd()


rain_animation = False
rain_timer = 0
rain_duration = 300  # 5 seconds at 20 FPS
raindrops = [(random.uniform(0, 800), random.uniform(0, 800)) for _ in range(2000)]


def draw_raindrop(x, y):
    glColor3f(0.5, 0.5, 1.0)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y + 3)
    glEnd()

# Function to draw sky (gradient background)
is_day = True
'''
def draw_sky():
    
    glBegin(GL_QUADS)

    if rain_animation:
        glColor3f(0.1, 0.1, 0.3)  # Darker blue sky color during rain
    else:
        glColor3f(0.4, 0.7, 1.0)  # Regular sky color
   
    if is_day:
        glColor3f(0.4, 0.7, 1.0)  # Day sky color (top)
        glVertex2f(-1, 1)
        glVertex2f(1, 1)
        glColor3f(0.7, 0.9, 1.0)  # Day sky color (bottom)

    else:
        glColor3f(0.03, 0.03, 0.2)  # Darker night sky color (top)
        glVertex2f(-1, 1)
        glVertex2f(1, 1)
        glColor3f(0.1, 0.1, 0.3)  # Darker night sky color (bottom)

    

    
    glVertex2f(1, -0.5)
    glVertex2f(-1, -0.5)
    glEnd()
'''


def draw_sky():
    glBegin(GL_QUADS)
    if is_day and not rain_animation:  # Day without rain
        glColor3f(0.4, 0.7, 1.0)  # Day sky color (top)
        glVertex2f(0, 600)
        glVertex2f(800, 600)
        glColor3f(0.7, 0.9, 1.0)  # Day sky color (bottom)
    elif not is_day and not rain_animation:  # Night without rain
        glColor3f(0.03, 0.03, 0.2)  # Darker night sky color (top)
        glVertex2f(0, 600)
        glVertex2f(800, 600)
        glColor3f(0.1, 0.1, 0.3)  # Darker night sky color (bottom)
    elif rain_animation:  # Rain (either day or night)
        glColor3f(0.2, 0.2, 0.5)  # Rainy sky color (top)
        glVertex2f(0, 600)
        glVertex2f(800, 600)
        glColor3f(0.3, 0.3, 0.7)  # Rainy sky color (bottom)
    glVertex2f(800, 300)
    glVertex2f(0, 300)
    
    glEnd()
'''
def draw_cloud(x, y):
    glBegin(GL_POLYGON)
    if rain_animation:
        glColor3f(0.3, 0.3, 0.3)  # Dark grey clouds during rain
    else:
        glColor3f(1, 1, 1)  # White clouds otherwise
    for i in range(10):
        theta = 2 * math.pi * i / 10
        x_pos = 0.1 * math.cos(theta)
        y_pos = 0.05 * math.sin(theta)
        glVertex2f(x + x_pos, y + y_pos)
    glEnd()
'''




def draw_cloud(x, y):
    if rain_animation:
        glColor3f(0.5, 0.5, 0.5)  # Dark grey clouds during rain
    else:
        glColor3f(1, 1, 1)  # White clouds (color will be overridden during rain)
    draw_circle(x, y, 50, (1, 1, 1))
    draw_circle(x + 50, y, 40, (1, 1, 1))
    draw_circle(x - 50, y, 40, (1, 1, 1))
    

def draw_star(x, y):
    # Drawing a simple star using a point
    glColor3f(1, 1, 1)  # White color for stars
    glPointSize(2.0)  # Adjusting the size of the point
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
star_positions = [(random.uniform(0, 600), random.uniform(800, 300)) for _ in range(50)]


# Function to draw ground (flat surface)
def draw_ground():
    glColor3f(0.0, 0.6, 0.0)  # Green color for the ground
    glBegin(GL_QUADS)
    glVertex2f(0, 300)
    glVertex2f(800, 300)
    glVertex2f(800, 0)
    glVertex2f(0, 0)
    glEnd()

# Function to draw a simple house
def draw_house(situation):
    # Draw main body of the house
    glColor4f(1.0, 1.0, 0.0, 0.0)# Brown color for the house
    glBegin(GL_POLYGON)
    glVertex2d(200, 200)
    glVertex2d(300, 200)
    glVertex2d(300, 250)
    glVertex2d(250, 300)
    glVertex2d(200, 250)
    glVertex2d(200, 200)


    glVertex2d(300, 200)
    glVertex2d(350, 200)
    glVertex2d(350, 250)
    glVertex2d(300, 250)

    glEnd()

    # Draw roof
    glColor3f(0.5, 0.0, 0.0)  # Dark red color for the roof
    glBegin(GL_POLYGON)
    glVertex2d(200, 250)
    glVertex2d(180, 270)
    glVertex2d(250, 340)
    glVertex2d(250, 300)
    glVertex2d(200, 250)

    #glVertex2d(310, 270)
    #glVertex2d(300, 250)
    #glVertex2d(250, 300)
    #glVertex2d(200, 250)
    glEnd()


    
    
    glColor3f(0.5, 0.0, 0.0)  # Black color for windows
    glBegin(GL_QUADS)
    glVertex2d(300, 250)
    glVertex2d(310, 270)
    glVertex2d(250, 340)
    glVertex2d(250, 300)
    glVertex2d(300, 250)

    glEnd()

    
    glColor3f(0.5, 0.0, 0.0)  # Black color for windows
   
    glBegin(GL_POLYGON)
    glVertex2d(310, 270)
    glVertex2d(350, 270)
    glVertex2d(370, 250)
    glVertex2d(300, 250)
    glVertex2d(310, 270)

    glEnd()


    # Draw windows
    

    # Window 1
    if situation == "day":
        glColor3f(0.0, 0.0, 0.0)  # Black color for windows
    else:
        glColor3f(1.0, 1.0, 1.0) 
    glBegin(GL_QUADS)
    glVertex2d(310, 220)
    glVertex2d(330, 220)
    glVertex2d(330, 240)
    glVertex2d(310, 240)
    glEnd()
    # Door

    # glColor3f(0.0, 0.0, 0.0)  # Black color for windows
    # glBegin(GL_QUADS)
    # glVertex2d(310, 220)
    # glVertex2d(330, 220)
    # glVertex2d(330, 240)
    # glVertex2d(310, 240)
    # glEnd()
 
    

# Function to draw a simple tree
def draw_tree(x, y):
    # Draw trunk
    glColor3f(0.5, 0.25, 0.0)  # Brown color for the trunk
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 0.05, y)
    glVertex2f(x + 0.05, y + 0.15)
    glVertex2f(x, y + 0.15)
    glEnd()

    # Draw leaves
    glColor3f(0.0, 0.8, 0.0)  # Green color for the leaves
    for i in range(3):  # Three layers of leaves
        glBegin(GL_TRIANGLES)
        glVertex2f(x - 0.05, y + 0.15 + i * 0.05)
        glVertex2f(x + 0.1, y + 0.15 + i * 0.05)
        glVertex2f(x + 0.025, y + 0.25 + i * 0.05)
        glEnd()

def draw_bird(x, y):
    glColor3f(0, 0, 0)  # Black color for the bird
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x - 10, y + 10)
    glVertex2f(x, y)
    glVertex2f(x + 10, y + 10)
    glEnd()



# Global variable to hold bird positions
bird_positions = [
    (600, 400), (700, 450), (550, 550), 
    (700, 300), (750, 400), (750, 550),
    (800, 450), (900, 500),
    (600, 300), (500, 500)
] 
# Global variable to control bird animation
bird_animation = False

def animate_birds():
    global bird_positions
    # Move the birds to the left
    bird_positions = [(x - 0.01, y) for x, y in bird_positions]

'''
# Function to draw the sun using the midpoint circle drawing algorithm
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
'''
def draw_river():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.5, 1.0)  # Blue color for water
    glVertex2f(500, 0)
    glVertex2f(800, 0)
    glVertex2f(800, 300)
    glVertex2f(500, 300)
    glEnd()

def draw_boat(x_position):
    # Draw the base of the boat
    glColor3f(0.5, 0.25, 0.0)  # Brown color
    glBegin(GL_POLYGON)
    #glVertex2f(x_position - 0.2, -0.2)
    #glVertex2f(x_position + 0.2, -0.2)
    #glVertex2f(x_position + 0.2, -0.15)
    #glVertex2f(x_position - 0.2, -0.15)
    glVertex2f(x_position, 270)
    glVertex2f(x_position+45, 220)
    glVertex2f(x_position+110, 220)
    glVertex2f(x_position+150, 270)
    glVertex2f(x_position, 270)
    
    glEnd()

    # Draw the upper part of the boat
    glColor3f(0.0, 0.9, 0.0)  # Slightly darker shade for the upper part
    glBegin(GL_POLYGON)
    glVertex2f(x_position+75, 290)
    glVertex2f(x_position+75, 330)
    glVertex2f(x_position+150, 330)
    glVertex2f(x_position+150, 290)
    glVertex2f(x_position+75, 290)
    glEnd()

    glColor3f(0.0, 0.0, 0.9)  # Green color for the ground
    glBegin(GL_QUADS)
    glVertex2f(x_position+ 75, 270)
    glVertex2f(x_position+ 75, 330)
    glVertex2f(x_position+ 72, 330)
    glVertex2f(x_position+ 72, 270)
    glEnd()

    # Green color for the ground
    
    draw_circle(x_position+113, 307, 13, (1, 0, 0))

boat_position = 550

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    iterate()
    global is_day, rain_animation, rain_timer, boat_position

     # Draw sky and ground
    draw_sky()
    draw_ground()

    # Draw houses
    draw_house("day")
    global bird_animation
    # Draw trees
    draw_tree(-0.9, -0.1)
    draw_tree(-0.8, -0.2)
    draw_river()
    draw_boat(boat_position)
    if bird_animation:
        global bird_positions
        bird_positions = [(x - 0.5, y) for x, y in bird_positions]  # Move birds to the left
        for x, y in bird_positions:
            draw_bird(x, y)
        
        
  
    global rain_timer, rain_animation

    # Rain Scene
    if rain_animation:
        #glColor3f(0.9, 0.9, 0.9)  # Grey clouds during rain
        draw_cloud(500, 450)
        draw_cloud(300, 420)
        draw_cloud(200, 500)
        draw_house("night")
        # Raindrop animation
        global raindrops
        raindrops = [(x, y - 2) for x, y in raindrops]  # Move raindrops downward
        for x, y in raindrops:
            draw_raindrop(x, y)
        rain_timer += 1
        if rain_timer > rain_duration:
            rain_animation = False
            rain_timer = 0
            raindrops = [(random.uniform(0, 800), random.uniform(0, 800)) for _ in range(2000)]


    # Day Scene
    elif is_day:
        draw_circle(700, 500, 40, (1.0, 0.843, 0.0))  # Sun
        #midpointcircle(700, 500, 40, (1.0, 0.843, 0.0))
        draw_cloud(500, 450)
        draw_cloud(300, 420)
        draw_cloud(200, 500)
        draw_house("day")
    # Night Scene
    else:
        draw_circle(700, 500, 40, (1, 1, 1))  # Moon
        for x, y in star_positions:
            draw_star(x, y)
        draw_house("night")
    glutSwapBuffers()

def keyboard(key, x, y):
    global is_day, bird_animation
    global is_day, rain_animation, rain_timer, boat_position

    if key == b'd':
        is_day = not is_day
    if key == b'b':
        bird_animation = not bird_animation
        
    if key == b'r' and not rain_animation:
        rain_animation = True
        rain_timer = 0

    if key == b'm':
        boat_position += 5
    if key == b'n':
        if boat_position < 500:
            boat_position -=0
        else:
            boat_position -= 5
        

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Village Scenario") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keep drawing the scene
glutKeyboardFunc(keyboard)
glutMainLoop()

