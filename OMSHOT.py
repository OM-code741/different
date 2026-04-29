#  print("hello world")
#   print("om")
#  print(2+4)
# import pyjokes
#  joke = pyjokes.get_joke()
#  print (joke)
# this print a special 
 # jokes here is the bes
# t way to resolve jokres
 # si that anybo
 # dy can read
 # your program easily
# # ?print("Twinkle, twinkle, little star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.")
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.''')
# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("ORS them is one of the best team is the history of world")
# engine.runAndWait()
# Simple pygame program

# Import and initialize the pygame library
# a= 1
# b=("harry")
# print(b and a)
a=1
# aaa=122
# harry=123
# _harry=233
# @harry=5454
# a += 1
# print(a)
# a = 2.43
# t=(type(a))
# print (t)
a = 1 
b = 2

# print(a+b)
# a = 2
# b = 4
# print( "remainder when a divided by b", a % b )
# #a = 4
# input("enter the value of a: ")
# a= "harry"  
# nameshort = a[0:3]
# character1= a[1]
# print(character1)
# name= "omkumar" 
# print(name[0:3])
# print(len(name))
# a = input("enter your cute name: ")
# print (f"good afternoon {a} ")
# print(f"what can i help you cutie pie? {a} ")
# print(f"i am your personal coach,bhaiya, didi. babu {a} ")
# b = input("type Z for more information")
# print (f"our server is currently down today{a}")""""
#import pygame
#import random

# 1. Setup Game
"""pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gangster Street Fight - No Images")

# Rang (Colors)
ROAD_GRAY = (50, 50, 50)
PLAYER_BLUE = (0, 100, 255)
ENEMY_RED = (255, 50, 50)
BULLET_YELLOW = (255, 255, 0)
BUILDING_COLOR = (30, 30, 40)

# Player (Gangster) Settings
player_pos = [WIDTH // 2, HEIGHT - 100]
player_size = 40
player_speed = 5

# Bullets & Enemies
bullets = []
enemies = []
enemy_size = 40
enemy_speed = 3
score = 0

def draw_environment():
    screen.fill(ROAD_GRAY) # Sadak
    # Side mein buildings (rectangles se)
    pygame.draw.rect(screen, BUILDING_COLOR, (0, 0, 100, HEIGHT))
    pygame.draw.rect(screen, BUILDING_COLOR, (WIDTH - 100, 0, 100, HEIGHT))
    # Road lines
    for i in range(0, HEIGHT, 100):
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 5, i, 10, 50))

# Game Loop
clock = pygame.time.Clock()
running = True

while running:
    draw_environment()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Goli chalane ke liye Space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_pos[0] + 15, player_pos[1]])

    # 2. Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 100:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - 140:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - 40:
        player_pos[1] += player_speed

    # 3. Enemies Spawn (Dushman aayenge)
    if random.randint(1, 50) == 1:
        enemies.append([random.randint(110, WIDTH - 150), -40])

    # 4. Update Bullets & Enemies
    for b in bullets[:]:
        b[1] -= 10
        if b[1] < 0: bullets.remove(b)
        else: pygame.draw.rect(screen, BULLET_YELLOW, (b[0], b[1], 10, 20))

    for e in enemies[:]:
        e[1] += enemy_speed
        if e[1] > HEIGHT: enemies.remove(e)
        else:
            enemy_rect = pygame.draw.rect(screen, ENEMY_RED, (e[0], e[1], enemy_size, enemy_size))
            player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
            
            # Collision: Agar dushman se takraye
            if player_rect.colliderect(enemy_rect):
                print(f"Game Over! Score: {score}")
                running = False

            # Check if Bullet hits Enemy
            for b in bullets[:]:
                bullet_rect = pygame.Rect(b[0], b[1], 10, 20)
                if bullet_rect.colliderect(enemy_rect):
                    if e in enemies: enemies.remove(e)
                    if b in bullets: bullets.remove(b)
                    score += 10

    # 5. Draw Player (Gangster)
    # Body
    pygame.draw.rect(screen,
PLAYER_BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    # Head (thoda alag dikhne ke liye)
    pygame.draw.rect(screen, (200, 150, 100), (player_pos[0] + 10, player_pos[1] - 10, 20, 20))

    # Score Board
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(f"Izzat (Score): {score}", True, (255, 255, 255))
    screen.blit(text, (110, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit"""
"""from ursina import *
import random

# 1. Game Setup
app = Ursina()

# Window settings
window.fps_counter.enabled = False
window.exit_button.visible = False

# 2. Player (Car) - Built-in Cube se bani hai
player = Entity(
    model='cube', 
    color=color.green, 
    scale=(1, 0.5, 2), 
    position=(0, 0, 0), 
    collider='box'
)

# 3. Environment (Road)
ground = Entity(
    model='plane', 
    scale=(10, 1, 100), 
    texture='white_cube', # Built-in texture
    color=color.dark_gray, 
    texture_scale=(1, 10)
)

# Side ki Walls (Bahar ka area)
left_wall = Entity(model='cube', scale=(1, 5, 100), x=-5, color=color.black, collider='box')
right_wall = Entity(model='cube', scale=(1, 5, 100), x=5, color=color.black, collider='box')

# 4. Camera Setup (3D View ke liye)
camera.position = (0, 5, -10)
camera.rotation_x = 20

# 5. Enemies (Traffic)
enemies = []
def spawn_enemy():
    e = Entity(
        model='cube', 
        color=color.red, 
        scale=(1, 0.5, 2), 
        x=random.uniform(-4, 4), 
        z=50, 
        collider='box'
    )
    enemies.append(e)
    invoke(spawn_enemy, delay=1) # Har 1 second mein naya dushman

spawn_enemy()

# 6. Update Loop (Game Logic)
def update():
    # Car Movement
    player.x += held_keys['d'] * time.dt * 5
    player.x -= held_keys['a'] * time.dt * 5

    # Road move hote hue dikhe (Looping effect)
    ground.z -= time.dt * 10
    if ground.z < -10:
        ground.z = 0

    # Enemies movement aur collision
    for e in enemies:
        e.z -= time.dt * 15 # Dushman car ki taraf aayenge
        
        # Collision check
        if player.intersects(e).hit:
            print("CRASHED! Game Over.")
            player.color = color.yellow
            application.pause()

        # Purane enemies delete karna
        if e.z < -15:
            enemies.remove(e)
            destroy(e)

# Game Start
app.run()"""
"""from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# --- RANG SETUP (RGB Colors) ---
rang_asman = Vec4(0.5, 0.8, 1, 1) 
rang_player = Vec4(0, 0, 1, 1)    
rang_car = Vec4(1, 0.5, 0, 1) # Orange Car
rang_sadak = Vec4(0.1, 0.1, 0.1, 1)
window.color = rang_asman

# --- PLAYER SETUP ---
player = FirstPersonController(
    model='cube', color=rang_player, z=-10, scale=(1, 2, 1), collider='box'
)
player.cursor.visible = False

# Camera GTA Style
camera.parent = player
camera.position = (0, 30, -15)
camera.rotation_x = 70

# --- CAR SETUP ---
# Ek car entity banate hain
car = Entity(
    model='cube', color=rang_car, position=(10, 0.5, 10), 
    scale=(2, 1, 4), collider='box'
)
driving = False # Check karne ke liye ki hum car mein hain ya nahi

# --- ENVIRONMENT ---
ground = Entity(model='plane', scale=(200, 1, 200), color=rang_sadak, collider='box', texture='white_cube')

# Buildings
for i in range(30):
    bx, bz = random.randint(-80, 80), random.randint(-80, 80)
    if abs(bx) > 15 or abs(bz) > 15:
        h = random.randint(10, 30)
        Entity(model='cube', position=(bx, h/2, bz), scale=(10, h, 10), 
               color=Vec4(0.2, 0.2, 0.3, 1), collider='box', texture='white_cube')

# --- INSTRUCTIONS UI ---
instruction = Text(
    text="Car ke paas jaao aur 'E' dabao baithne ke liye\nBahar nikalne ke liye 'F' dabao",
    position=(0.5, 0.45), origin=(0.5, 0.5), scale=1.2, color=color.yellow
)

# --- GAME LOGIC ---
def input(key):
    global driving
    # Car mein baithna
    if key == 'e' and not driving:
        # Check distance between player and car
        if distance(player.position, car.position) < 5:
            driving = True
            player.visible = False
            player.collider = None # Collision band takki car ke andar na fanse
            
    # Car se utarna
    if key == 'f' and driving:
        driving = False
        player.position = car.position + Vec3(3, 1, 0) # Car ke thoda side mein utarna
        player.visible = True
        player.collider = 'box'

def update():
    global driving
    
    if driving:
        # Car Controls
        car.rotation_y += held_keys['d'] * time.dt * 100
        car.rotation_y -= held_keys['a'] * time.dt * 100
        
        # Forward/Backward
        move_direction = car.forward * (held_keys['w'] - held_keys['s'])
        car.position += move_direction * time.dt * 20
        
        # Player ko car ke saath chipka do
        player.position = car.position
        # Camera ko car ke hisab se thoda adjust karo
        camera.world_rotation_y = car.world_rotation_y
    else:
        # Normal Player Movement (Automatic handled by FirstPersonController)
        pass

app.run()



# z=2
# print(type(z))
# print(float(z))
# print(complex(z))
# print(float(z))
#String or literals

MY_PHOME_NUMBER=9123467946

print("MY_PHOME_NUMBER", MY_PHOME_NUMBER)
# a= "hello, world"
# print(a[11:12])
# print(a[::-1])



# HOMEWOR QUESTION 1
r=7
a=3.14159*r*r
print("area of circle", a)

# HOMEWORK QUESTION 2
n1 = 20
n2 = 40
n3 = 60
average_of_number=n1+n2+n3/3
print("average_of_number", average_of_number)

# HW 3
maths=85
science=90
english=75
TOTAL_MARKS =(maths + science + english)
PERCENTAGE =(TOTAL_MARKS/3)
print("TOTAL_MARKS", TOTAL_MARKS)
print("PERCENTAGE", PERCENTAGE)

# HW 5
a=10
b=20
b=a
print(b)
a=b=20
print (a)
# HW 4
s= 5
CUBE_OF_CIRCLE = 6*s**2
print("CUBE_OF_CIRCLE", CUBE_OF_CIRCLE)
# hw 
l= 10
w= 5
h=3
z= l*w*h
print(z)

s= 8
print("area of square", s*s)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"<h1>Hello {name}, welcome to my website!</h1>"

if __name__ == '__main__':
app.run(debug=True)"""

#sum of two nunber
"""a=2
b= " harry"  #string
print(a)
print(b)"""



# x=y=z="apple"
# print(x)
# print(y)
# print(z)

"""a = " 23"
b= ("you are" +a)
print(a)
 
a = 12
b = 12.2
c = 12+2j
print(type(a))       
print(type(b))
print(type(c))
a=1
print(float(a))
b=12.4
print(int(b))

a="whj"
print(len(a))

fruits =["apple", "banana", "cherry"]
is_apple_present ="apple" in fruits
print(f"Is 'apple' in the list? {is_apple_present}")"""
 


'''print(a[0])
print(a[2])
print(a[1])
for x in a:
   print(x)
if "satish" in a:
   print("yes, satish is in the list")
a = ["rahul", "ankur", "satish"]
# a.append("hamza")
print(a)
a.insert(0, "HAMZA")
print(a)
a.remove("HAMZA")
print(a)
a.pop()
print(a)'''
