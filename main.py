import sys
import pygame
from labirentler import Maze
from random import randint

"""@author: MUSTAFA YALINIZ"""

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 540))
        pygame.display.set_caption('Labirent Oyunu')

        self.labirent_baslangic = 0
        self.labirent = Maze.maze(self.labirent_baslangic)
        if self.labirent is None:
            print("Labirent yüklenemedi")
            sys.exit()

        self.block_size = 60
        self.player_pos = [1, 1]
        self.banana_pos = self.random_yer()

        self.player_image = pygame.image.load('images/monkey.bmp')
        self.banana_image = pygame.image.load('images/banana.bmp')
        self.moving_right = False
        self.moving_left = False

    def random_yer(self):
        while True:
            x = randint(0, len(self.labirent[0]) - 1)
            y = randint(0, len(self.labirent) - 1)
            if self.labirent[y][x] == 0:
                return [x, y]

    def draw_maze(self):
        for row in range(len(self.labirent)):
            for col in range(len(self.labirent[row])):
                color = (255, 255, 255) if self.labirent[row][col] == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color,
                                 (col * self.block_size, row * self.block_size, self.block_size, self.block_size))

    def draw_monkey(self):
        self.screen.blit(self.player_image,
                         (self.player_pos[0] * self.block_size, self.player_pos[1] * self.block_size))

    def draw_banana(self):
        self.screen.blit(self.banana_image,
                         (self.banana_pos[0] * self.block_size, self.banana_pos[1] * self.block_size))

    def move_player(self, dx, dy):
        new_pos = [self.player_pos[0] + dx, self.player_pos[1] + dy]
        if self.labirent[new_pos[1]][new_pos[0]] == 0:
            self.player_pos = new_pos
            if self.player_pos == self.banana_pos:
                self.labirent_baslangic = (self.labirent_baslangic + 1) % len(Maze.mazes)
                self.labirent = Maze.maze(self.labirent_baslangic)
                self.player_pos = [1, 1]
                self.banana_pos = self.random_yer()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player(1, 0)

            self.screen.fill((0, 0, 0))
            self.draw_maze()
            self.draw_monkey()
            self.draw_banana()
            pygame.display.flip()


if __name__ == '__main__':
    Main().run()
