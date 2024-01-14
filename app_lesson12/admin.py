from django.contrib import admin

from app_lesson12.models import Movie, MovieType

class X (admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    
class MovieAdmin (admin.ModelAdmin):
    list_display = ('name', 'episodes', 'movie_type', 'my_episodes', 'my_rating', )
    search_fields = ('name', 'episodes')
    list_filter = ('movie_type',  )

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieType, X)


# Register your models here.
