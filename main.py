import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange',
          'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')


def create_turtle(colors):
    turtles = []


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    # Screen Title
    screen.title('Turtle Racing!')


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
