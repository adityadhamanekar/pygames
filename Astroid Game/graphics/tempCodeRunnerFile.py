    if snake_head.colliderect(food):
        food_x = randint(50, 1000)
        food_y = randint(50, 600)
        food = pygame.Rect(food_x, food_y, snake_size, snake_size)
        snake_length += 5