import pygame

class Target:
    """A class to manage the target."""

    def __init__(self, sShooter):
        """Create a target object at the screen`s topright."""
        super().__init__()
        self.screen = sShooter.screen
        self.settings = sShooter.settings
        self.color = self.settings.target_color

        # Create a target rect at (0, 0) and then set its correct position.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
            self.settings.target_height)
        self.rect.topright = sShooter.screen.get_rect().topright

        # Store the target`s position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the target up/down the screen."""
        # Update the decimal position of the target.
        self.y += self.settings.target_speed * self.settings.target_direction
        # Update the rect position.
        self.rect.y = self.y

    def check_edges(self):
        """Return True if the target is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top < 0:
            return True

    def draw_target(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def shift_topright(self):
        """Target starts at the topright of the screen."""
        screen_rect = self.screen.get_rect()
        self.rect.topright = screen_rect.topright
        self.y = float(self.rect.y)