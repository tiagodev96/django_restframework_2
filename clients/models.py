from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        blank=False,
        max_length=30,
    )
    document = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=14)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
