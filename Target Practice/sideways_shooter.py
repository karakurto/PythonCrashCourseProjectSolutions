import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target
from won_button import WonButton
from lost_button import LostButton

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initilaize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(" --Target Practice-- ")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

     
        # Make the Play Button.
        self.play_button = Button(self, "Press <P> to Play")

        # Make the Won Button.
        self.won_button = WonButton(self, "Congratulations! Press <P> to Play Again")

        # Make the Lost Button.
        self.lost_button = LostButton(self, "Sorry, No more bullets left! Press <P> to Play Again")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._bullets_update()
                self._update_target()

            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _bullets_update(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self._check_bullets()
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_target(self):
        """
        Check if the target is at the edge,
        Then update the position of the target
        """
        self._check_target_edges()
        self.target.update()

        # Look for bullet-target collisions.
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            self._target_hit()

    def _target_hit(self):
        """Respond when the target is hit."""
        # Set the flags accordingly to display the right button.
        self.stats.game_won = True
        self.stats.game_active = False

        # Get rid of any remaining bullets
        self.bullets.empty()

        # Re-place the ship for the next game.
        self.ship.center_ship()

        # Re-place the target for the next game.
        self.target.shift_topright()

        #self.stats.game_active = False
        pygame.mouse.set_visible(True)

        # Pause.
        sleep(0.5) 

    def _no_bullets_left(self):
        """Respond to the case when there are no bullets left."""
        # Set the flags accordingly to display the right button.
        self.stats.game_won = False
        self.stats.game_active = False

        # Re-place the ship for the next game.
        self.ship.center_ship()
 
        # Re-place the target for the next game.
        self.target.shift_topright()

        #self.stats.game_active = False
        pygame.mouse.set_visible(True)

        # Pause.
        sleep(0.5)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
            
    def _start_game(self):
        """"""
        if not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.stats.game_won = None

            # Get rid of any remaining bullets.
            self.bullets.empty()

            # Place the ship in the left-center of the screen.
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)           
      
    def _check_keyup_events(self, event):
        """Respond to keyreleases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if self.stats.bullets_allowed > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.bullets_allowed -= 1

    def _check_bullets(self):
        """
        Check if there are still bullets to shoot and
        whether the shot bullets has already left the screen
        """
        if self.stats.bullets_allowed == 0 and len(self.bullets) == 0:
            self._no_bullets_left()

    def _check_target_edges(self):
        """Respond appropriately if the target has reached an edge."""
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        """Change the target`s direction when it reaches the edges of the screen."""
        #target.rect.x -= self.settings.fleet_drop_speed
        self.settings.target_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        
        # Draw the play button when the game is started.
        if not self.stats.game_active and self.stats.game_won == None:
            self.play_button.draw_button()
        # Draw the button when the game is won.
        elif not self.stats.game_active and self.stats.game_won:
            self.won_button.draw_button()
        # Draw the button when the game is lost.
        elif not self.stats.game_active and not self.stats.game_won:
            self.lost_button.draw_button()

if __name__ == '__main__':
    """ Make a game instance, and run the game."""
    sShooter = SidewaysShooter()
    sShooter.run_game()
