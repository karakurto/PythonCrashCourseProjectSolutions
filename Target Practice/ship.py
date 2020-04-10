import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, sShooter):
		"""Initialize the ship and set its stating position."""
		self.screen = sShooter.screen
		self.settings = sShooter.settings
		self.screen_rect = sShooter.screen.get_rect()

		# Load the ship image and fet its rect
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the midleft of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the ship`s horizontal position.
		self.x = float(self.rect.x)

		# Store a decimal value for the ship`s vertical position
		self.y = float(self.rect.y)

		# Movement Flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship`s position based on the movement flags."""
		# Update the ship`s x vlaue, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left:
			self.x -= self.settings.ship_speed

		# Update the ship`s y vlaue, not the rect.
		if self.moving_up and self.rect.top:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update rect object from self.x.
		self.rect.x = self.x

		# Update rect object from self.y.
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)
