from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'AMERICAN'),
    ('BRAZIL', 'BRAZILLIAN'),
    ('JAPAN', 'JAPANESE')
    )


class Developers(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.named