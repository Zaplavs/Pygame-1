import pygame


class MainPlayer:
    player_x = 150
    player_y = 303
    walk_left = [
        pygame.transform.scale(pygame.image.load('img/player/left/left_1.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/left/left_2.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/left/left_3.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/left/left_4.png'), (60, 60)),
    ]
    walk_right = [
        pygame.transform.scale(pygame.image.load('img/player/right/right_1.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/right/right_2.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/right/right_3.png'), (60, 60)),
        pygame.transform.scale(pygame.image.load('img/player/right/right_4.png'), (60, 60)),
    ]
    is_jump = False
    jump_count = 8
    player_speed = 5
    player_anim_count = 0
    def square_player(self):
        return self.walk_left[0].get_rect(topleft=(self.player_x, self.player_y - 30))
