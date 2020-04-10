class Settings:
    """A Class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game`s settings."""
        # Screen setiings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.0
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.target_direction = 1
        self.target_speed = 1.0
        self.target_width = 20
        self.target_height = 50
        self.target_color = (60, 60, 60)
