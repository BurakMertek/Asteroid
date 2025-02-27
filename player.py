import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.invincible = False
        self.invincible_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def draw (self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    
    def update(self, dt):
        self.shoot_timer -= dt
        if self.invincible:
            self.invincible_timer -=dt
            print(f"Invincibility Timer: {self.invincible_timer}")
            if self.invincible_timer <= 0:
                self.invincible = False
                print("Player is no longer invincible!")


        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt, position):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def respawn():
        print("Respawning player...")
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.invincible = True
        self.invincible_timer = 2
        print("Player is now invincible!")
        