from road import Road
from car import Car
import random
import math
import pygame

num_cars = 250

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
            nextNum = random.randint(0, 1)
            turns.append(nextNum)
            turns.append(0)
            if nextNum:
                turns.append(random.randint(0, 1))
            else:
                turns.append(1)

            turns.append(random.randint(0, 32))

        unique = turns not in spotsTaken

    spotsTaken.append(turns)
    cars.append(Car(entryPoints[turns[0]], turns[-1], turns[1:-1], i))

pygame.init()
screen = pygame.display.set_mode((2059, 906))
pygame.key.set_repeat(100, 100)

background_image = pygame.image.load("background.png").convert()

running = True

circles = []

font = pygame.font.Font('freesansbold.ttf', 12)
texts = []

tick_num = 0
num_cars_remaining = num_cars
while running:

    screen.blit(background_image, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            circles = []
            tick_num += 1
            num_cars_remaining = 0
            for car in cars:
                car.tick()
                num_cars_remaining += 1 if car.done and car.taskTicks == 0 else 0
                if car.currentSpot is not None:
                    print(car.getPoint())
                    circles.append([car.getPoint(), car])

    for circle, car in circles, cars:
        pygame.draw.circle(screen, (255 if car.done and car.taskTicks == 0 else 0, 0, 0), circle, 7)
        text = font.render(f'Car {car.number} State: {"Parking" if car.done and car.taskTicks == 0 else "Parked"}', True, (255, 0, 0), (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (circle[0], circle[1] + (-15 if hash(car) >> 5 & 0x1 else 15))
        screen.blit(text, text_rect)

    pygame.display.set_caption(f'cars remaining: {num_cars - num_cars_remaining} out of {num_cars}. Tick {tick_num}')

    pygame.display.flip()
