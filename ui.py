import pygame

def difficulty_selection(screen):
    font = pygame.font.Font(None, 36)
    options = ['Easy', 'Medium', 'Hard']
    selected = 0

    while True:
        screen.fill((30, 30, 30))
        title = font.render("Select Difficulty", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, 100)))

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (150, 150, 150)
            text = font.render(option, True, color)
            screen.blit(text, text.get_rect(center=(screen.get_width() // 2, 180 + i * 50)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    selected = (selected + (-1 if event.key == pygame.K_UP else 1)) % 3
                elif event.key == pygame.K_RETURN:
                    return options[selected].lower()
