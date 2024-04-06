from django.db import models
from uuid import uuid4

# Create your models here.
class Games(models.Model):
    id_game = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=1024)
    release_year = models.DateField()
    developer = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Game'
