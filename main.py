# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    lives = 5
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable,drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if not player.invincible and player.collision(asteroid):
                print("Collision detected! Respawning...")
                lives -= 1
                if lives == 0:
                    print("Game over!")
                    return
                Player.respawn()
                print(f"Lives left: {lives}")

                
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 5
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (1180, 10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
