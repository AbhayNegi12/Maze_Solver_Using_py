import pygame
import random
from maze import generate_maze
from graphics import draw_maze
from constants import CELL_SIZE, DIFFICULTY
from solver import dijkstra, calculate_path_cost, print_path_with_cost
from ui import difficulty_selection

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Maze Solver")
    font = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()

    waiting = True
    while waiting:
        screen.fill((30, 30, 30))
        title_font = pygame.font.Font(None, 36)
        text = title_font.render("Press ENTER to Start", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

    difficulty = difficulty_selection(screen)
    size, wall_prob = DIFFICULTY[difficulty]
    screen = pygame.display.set_mode((size * CELL_SIZE, size * CELL_SIZE), pygame.RESIZABLE)

    maze = generate_maze(size, size, wall_prob)
    cell_numbers = {(r, c): random.randint(1, 10) for r in range(size) for c in range(size)}

    player_pos, end = [0, 0], (size - 1, size - 1)
    visited = {(0, 0)}
    player_path = [(0, 0)]
    reached_goal = False
    dijkstra_path = dijkstra(maze, cell_numbers, (0, 0), end)

    blink_state = True
    blink_timer = 0

    while True:
        blink_timer += clock.get_time()
        if blink_timer > 400:  # Blink every 400ms
            blink_state = not blink_state
            blink_timer = 0

        draw_maze(screen, maze, player_path, visited, cell_numbers, font, clock, blink_state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                new_pos = player_pos[:]
                if event.key == pygame.K_UP: new_pos[0] -= 1
                elif event.key == pygame.K_DOWN: new_pos[0] += 1
                elif event.key == pygame.K_LEFT: new_pos[1] -= 1
                elif event.key == pygame.K_RIGHT: new_pos[1] += 1

                if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size and not maze[new_pos[0]][new_pos[1]]:
                    if tuple(new_pos) in player_path:
                        while player_path and player_path[-1] != tuple(new_pos):
                            player_path.pop()
                    else:
                        player_path.append(tuple(new_pos))
                        visited.add(tuple(new_pos))
                    player_pos = new_pos

                if tuple(player_pos) == end and not reached_goal:
                    reached_goal = True
                    print("You reached the goal!")
                    print_path_with_cost(dijkstra_path, cell_numbers, "Dijkstra's")
                    print_path_with_cost(player_path, cell_numbers, "Your")
                    pygame.quit()
                    exit()

        clock.tick(60)  

if __name__ == "__main__":
    main()
