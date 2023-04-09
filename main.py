from pygame import *

window = display.set_mode((700,500))

class Game_sprie(sprite.Sprite):
    def __init__ (self, sprite_image, sprite_x, sprite_y, sprite_speed, sprite_w, sprite_h):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_w, sprite_h))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_sprie):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - 150 - 15:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 150 - 15:
            self.rect.y += self.speed

player1 = Player('racket.jpg', 20, 200, 10, 20, 150)
player2 = Player('racket.jpg', 650, 200, 10, 20, 150)

clock = time.Clock()
game = True

while game:
    window.fill((0, 255, 255))

    player1.reset()
    player2.reset()

    player1.update_l()
    player2.update_r()

    for e in event.get():
        if e.type == QUIT:
            game = 0

    display.update()
    clock.tick(100)
