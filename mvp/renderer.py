import pygame
import math
import random
from globals import LENGTH, ANGLES, PLANT_COLOR, FRUIT_A_COLOR, FRUIT_B_COLOR

class Renderer:
    def __init__(self, screen):
        self.screen = screen

        self.current_position = None
        self.current_angle = None
        self.growth_percent = 0.0

    def set_values(self, position: tuple = None, angle: float = None) -> None:

        if position is not None:
            self.current_position = position
        if angle is not None:
            self.current_angle = angle

    def draw_l_system(self, commands, initial_position, initial_angle):
        if self.current_position is None: self.current_position = initial_position
        if self.current_angle    is None: self.current_angle = initial_angle

        stack = []
        position = self.current_position
        angle = self.current_angle

        for command in commands:
            if command == "F":
                length = LENGTH + random.uniform(-2, 2) 
                angle_variation = random.uniform(-5, 5)
                new_position = (
                    position[0] + length * math.cos(math.radians(angle + angle_variation)),
                    position[1] + length * math.sin(math.radians(angle + angle_variation))
                )
                self.draw_line(position, new_position)  # Pass `t` for interpolation
                position = new_position
            elif command == "A":
                pygame.draw.circle(self.screen, FRUIT_A_COLOR, position, random.randint(3,5))
            elif command == "B":
                pygame.draw.circle(self.screen, FRUIT_B_COLOR, position, random.randint(4,5)) 
            elif command == "+":
                angle += ANGLES
            elif command == "-":
                angle -= ANGLES 
            elif command == "[":
                stack.append((position, angle))
            elif command == "]":
                position, angle = stack.pop()

        self.current_position = position
        self.current_angle = angle

    
    def draw_line(self, start, end):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx**2 + dy**2)
        if length == 0:
            return
        perp_dx = -dy / length
        perp_dy = dx / length
        
        for i in range(-2 // 2, 2 // 2 + 1):
            offset_x = perp_dx * i
            offset_y = perp_dy * i
            pygame.draw.aaline(self.screen, PLANT_COLOR, (start[0] + offset_x, start[1] + offset_y), (end[0] + offset_x, end[1] + offset_y), 1)
    

