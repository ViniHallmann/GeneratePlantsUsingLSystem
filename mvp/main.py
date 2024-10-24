from lsystem import LSystem
from renderer import Renderer
import pygame
import time
import globals

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("L-System Growth")
    clock = pygame.time.Clock()
    running = True
    return screen, clock, running

def main():
    screen, clock, running = init_pygame()

    l_system = LSystem()
    renderer = Renderer(screen)
    drawing = False
    iteration_count = 0
    string = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                iteration_count = 0
                
                string = ""
                renderer.set_values(position=(400, 600), angle=-90)
                l_system.set_values(current_string=True)
                screen.fill(globals.BACKGROUND_COLOR)

        if drawing:
            if iteration_count < globals.DISPLAY_STEPS:
                string = l_system.generate_next()
                renderer.draw_l_system(string, (400, 600), -90)
                
                pygame.time.wait(100)
                iteration_count += 1
            else:
                drawing = False
        
        pygame.display.flip()  
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
