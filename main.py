from road import Road
from car import Car
import random
import math
import pygame

num_cars = 300

rows = 5
spots_per_row = 33

road1 = Road(15, [Road(5, [Road(33, None, True, ((600, 47), (1915, 47)))], False, ((322, 162), (600, 47))),
                  Road(5, [Road(33, None, True, ((591, 208), (1913, 208)))], False, ((322, 162), (591, 208)))], False,
             ((208, 162), (322, 162)))
road2 = Road(15,
             [Road(10,
                   [Road(33, None, True, ((600, 366), (1915, 366)))], False, ((330, 550), (600, 366))),
              Road(5,
                   [Road(3, [Road(33, None, True, ((591, 525), (1915, 525)))], False, ((489, 596), (591, 525))),
                    Road(3, [Road(33, None, True, ((592, 685), (1915, 685)))], False, ((489, 596), (592, 685)))
                    ], False, ((326, 553), (488, 596)))], False, ((204, 554), (320, 554)))

entryPoints = [road1, road2]

spotsTaken = []
cars = []
for i in range(num_cars):
    unique = False
    turns = []
    while not unique:
        turns = []
        randomNum = math.floor(random.random() + .6)
        if randomNum:
            turns.append(randomNum)
            randomNum = random.randint(0, 1)
            turns.append(randomNum)
            if randomNum:
                turns.append(random.randint(0, 1))

                turns.append(0)
                turns.append(random.randint(0, 1))
                turns.append(random.randint(0, 32))
            else:
                turns.append(0)
                turns.append(random.randint(0, 1))
                turns.append(random.randint(0, 32))
        else:
            turns.append(randomNum)
            turns.append(random.randint(0, 1))
            turns.append(0)
            turns.append(random.randint(0, 1))
            turns.append(random.randint(0, 32))

        unique = turns not in spotsTaken

    spotsTaken.append(turns)
    cars.append(Car(entryPoints[turns[0]], turns[-1], turns[1:-1], i))

pygame.init()
screen = pygame.display.set_mode((2059, 906))
pygame.key.set_repeat(100, 150)

background_image = pygame.image.load("background.png").convert()

running = True

circles = []

tick_num = 0
while running:
    screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            circles = []
            tick_num += 1
            for car in cars:
                car.tick()
                if car.currentSpot is not None:
                    print(car.getPoint())
                    circles.append(car.getPoint())

    for circle in circles:
        pygame.draw.circle(screen, (0, 0, 255), circle, 7)



    pygame.display.flip()
