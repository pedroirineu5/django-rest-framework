from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from games.models import Games


class Review(models.Model):
    game = models.ForeignKey(
        Games, 
        on_delete=models.PROTECT, 
        related_name='reviews'
    )

    grade = models.IntegerField(
        validators=[
            MinValueValidator(0,'Valor não pode ser menor que 0.'),
            MaxValueValidator(5, 'Valor não pode ser maior que 5.')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.game