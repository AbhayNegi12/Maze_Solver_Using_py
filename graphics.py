import pygame
from constants import CELL_SIZE

def fade_in_maze(screen, maze, cell_numbers, font):
    screen.fill((255, 255, 255))
    offset_x = (screen.get_width() - len(maze[0]) * CELL_SIZE) // 2
    offset_y = (screen.get_height() - len(maze) * CELL_SIZE) // 2

    for alpha in range(0, 256, 15):
        screen.fill((255, 255, 255))
        for r, row in enumerate(maze):
            for c, cell in enumerate(row):
                color = (0, 0, 0) if cell else (200, 200, 200)
                rect = (offset_x + c * CELL_SIZE, offset_y + r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                num_text = font.render(str(cell_numbers[(r, c)]), True, (0, 0, 0))
                text_rect = num_text.get_rect(center=(offset_x + c * CELL_SIZE + CELL_SIZE // 2,
                                                       offset_y + r * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(num_text, text_rect)

        pygame.display.update()
        pygame.time.delay(30)


def draw_maze(screen, maze, player_path, visited, cell_numbers, font, clock, blink_state):
    screen.fill((255, 255, 255))
    offset_x = (screen.get_width() - len(maze[0]) * CELL_SIZE) // 2
    offset_y = (screen.get_height() - len(maze) * CELL_SIZE) // 2

    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell:
                color = (0, 0, 0)  # Wall
            elif (r, c) == player_path[-1]:
                # Blinking current position
                color = (0, 0, 255) if blink_state else (100, 100, 255)
            elif (r, c) in player_path:
                color = (173, 216, 230)  # Trail
            else:
                color = (200, 200, 200)  # Unvisited

            rect = (offset_x + c * CELL_SIZE, offset_y + r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

            # Draw cell weight
            num_text = font.render(str(cell_numbers[(r, c)]), True, (0, 0, 0))
            text_rect = num_text.get_rect(center=(offset_x + c * CELL_SIZE + CELL_SIZE // 2,
                                                   offset_y + r * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(num_text, text_rect)

    # Goal cell (red)
    pygame.draw.rect(screen, (255, 0, 0),
        (offset_x + (len(maze[0])-1) * CELL_SIZE, offset_y + (len(maze)-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
