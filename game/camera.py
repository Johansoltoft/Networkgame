import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Limit scrolling to the map size
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.width - self.width), x)  # Right
        y = max(-(self.height - self.height), y)  # Bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply_offset(self):
        return pygame.math.Vector2(self.camera.topleft)
