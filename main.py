import pygame

from functoins import load_level, load_image, generate_level, move
from settings import *
from start import start_screen

# Инициализируем игру
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()

# Создаем спрайты
tile_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')
level_map = load_level("map.map")

# создаем  player
# открываем стартовый экран который воспроизводит игровой цикл пока не нажмем кнопку

player = generate_level(level_map, tile_group, hero_group, tile_images, player_image)

start_screen(screen, clock)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            move(player, level_map, event.key)
            # обработка нажатий стрелок

    tile_group.draw(screen)
    hero_group.draw(screen)


    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
