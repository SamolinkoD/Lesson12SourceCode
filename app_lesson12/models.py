from django.db import models

class MovieType (models.Model):
    name = models.CharField(max_length=63, unique=True, null=False, blank=False)
    def __str__(self) -> str:
        return f"{self.name}"

class Movie(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    dicription = models.TextField()
    episodes = models.PositiveIntegerField(null=True, blank=True)
    movie_type = models.ForeignKey(
        MovieType, on_delete=models.CASCADE, null=False, blank=False
    )
    my_episodes = models.PositiveIntegerField(null=True, blank=True)
    my_rating = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.name} {self.episodes} | {self.movie_type}"
    price = models.PositiveIntegerField(null=True, blank=True)