import pygame


class Game:
    def __init__(self, heart, bandit, player):
        self.heart = heart
        self.bandit = bandit
        self.player = player

    def incilizato(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode((760, 380))
        pygame.display.set_caption("Моя первая игра (Zaplavs)")
        self.icon = pygame.image.load('img/icon/icon.png').convert_alpha()
        pygame.display.set_icon(self.icon)
        self.bg = pygame.image.load('img/basic/background.png').convert()
        self.bg_sound = pygame.mixer.Sound('sound/music.mp3')
        self.bg_sound.play()
        self.ghost_list_in_game = []
        self.label = pygame.font.Font('font/Borel-Regular.ttf', 40)
        self.lose_label = self.label.render('You Lose!!!', False, (193, 196, 199))
        self.restart_label = self.label.render('Restart Game!!!', False, (115, 132, 148))
        self.restart_label_rect = self.restart_label.get_rect(topleft=(280, 200))
        self.bg_x = 0
        self.bullets_left = 5
        self.ghost_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ghost_timer, 2500)
        self.gameplay = True
        self.bullets = []
        self.running = True

    def play(self):
        while self.running:
            self.screen.blit(self.bg, (self.bg_x + 0, 0))
            self.screen.blit(self.bg, (self.bg_x + 760, 0))

            if self.gameplay:

                self.keys = pygame.key.get_pressed()

                self.player_rect = self.player.square_player()

                if self.ghost_list_in_game:
                    for (i, el) in enumerate(self.ghost_list_in_game):
                        self.screen.blit(self.bandit.img, el)
                        el.x -= 10

                        if el.x < -60:
                            self.ghost_list_in_game.pop(i)

                        if self.player_rect.colliderect(el):
                            self.gameplay = False

                if self.keys[pygame.K_LEFT]:
                    self.screen.blit(self.player.walk_left[self.player.player_anim_count],
                                     (self.player.player_x, self.player.player_y)
                                     )
                else:
                    self.screen.blit(self.player.walk_right[self.player.player_anim_count],
                                     (self.player.player_x, self.player.player_y)
                                     )

                if not self.player.is_jump:
                    if self.keys[pygame.K_SPACE]:
                        self.player.is_jump = True

                else:
                    if self.player.jump_count >= -8:
                        if self.player.jump_count > 0:
                            self.player.player_y -= (self.player.jump_count ** 2) / 2
                        else:
                            self.player.player_y += (self.player.jump_count ** 2) / 2
                        self.player.jump_count -= 1
                    else:
                        self.player.is_jump = False
                        self.player.jump_count = 8

                if self.keys[pygame.K_LEFT] and self.player.player_x > 50:
                    self.player.player_x -= self.player.player_speed
                elif self.keys[pygame.K_RIGHT] and self.player.player_x < 200:
                    self.player.player_x += self.player.player_speed
                self.player.player_anim_count += 1
                self.player.player_anim_count = self.player.player_anim_count % 4

                self.bg_x -= 5
                if self.bg_x == -760:
                    self.bg_x = 0

                if self.bullets:
                    for (i, el) in enumerate(self.bullets):
                        self.screen.blit(self.heart.img, (el.x, el.y))
                        el.x += 4

                        if el.x > 770:
                            self.bullets.pop(i)
                        if self.ghost_list_in_game:
                            for (index, bandit_el) in enumerate(self.ghost_list_in_game):
                                if el.colliderect(bandit_el):
                                    self.ghost_list_in_game.pop(index)
                                    self.bullets.pop(i)


            else:
                self.screen.fill((87, 88, 89))
                self.screen.blit(self.lose_label, (280, 100))
                self.screen.blit(self.restart_label, self.restart_label_rect)

                self.mouse = pygame.mouse.get_pos()
                if self.restart_label_rect.collidepoint(self.mouse) and pygame.mouse.get_pressed()[0]:
                    self.gameplay = True
                    self.player.player_x = 150
                    self.ghost_list_in_game.clear()
                    self.bullets.clear()
                    self.bullets_left = 5

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == self.ghost_timer:
                    self.ghost_list_in_game.append(self.bandit.img.get_rect(topleft=(760, 303)))
                if self.gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and self.bullets_left > 0:
                    self.bullets.append(self.heart.img.get_rect(topleft=
                                                                (self.player.player_x + 30, self.player.player_y + 10)))
                    self.bullets_left -= 1

            self.clock.tick(15)
