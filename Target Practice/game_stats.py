class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, sShooter):
        """Initialize statistics."""
        self.settings = sShooter.settings
        self.reset_stats()

        # Start "Target Practice" in non-active state.
        self.game_active = False

        # The game is either won or lost when the game is started.
        self.game_won = None
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.bullets_allowed = self.settings.bullets_allowed