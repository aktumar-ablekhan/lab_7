import pygame
import time 
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("MICKEY CLOCK")

left_arm = pygame.image.load("leftarm.png")
right_arm = pygame.image.load("rightarm.png")
mickey_clock = pygame.transform.scale(pygame.image.load("clock.png"), (800, 600))


stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = minute * 6 + (second / 60) * 6
    second_angle = second * 6

    screen.blit(mickey_clock, (0,0))

    rotated_right_arm = pygame.transform.rotate(pygame.transform.scale(right_arm, (800,600)), -minute_angle)
    right_arm_rect = rotated_right_arm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_right_arm, right_arm_rect)

    rotated_left_arm = pygame.transform.rotate(pygame.transform.scale(left_arm, (40.95, 682.5)), -second_angle)
    left_arm_rect = rotated_left_arm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_left_arm, left_arm_rect)

    pygame.display.flip() #окноны жаңартады
    clock.tick(60) #fps

pygame.quit()
