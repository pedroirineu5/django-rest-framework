from django.db import models

PLATFORMS_CHOICES = (
    ("PC_STEAM", "PC (Steam)"),
    ("XBOX_360", "Xbox 360"),
    ("XBOX_ONE", "Xbox One"),
    ("XBOX_SERIES", "Xbox Series X/S"),
    ("PS4", "PlayStation 4"),
    ("PS5", "PlayStation 5"),
    ("NINT_SWITCH", "Nintendo Switch"),
)

class Platforms(models.Model):
    name = models.CharField(choices=PLATFORMS_CHOICES, max_length=50)

    def __str__(self):
        return self.name
    