from django.contrib import admin
from .models import Game
from django.utils.html import format_html


class GameAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'name_game', 'release_year')

    def thumb(self, obj):
        return format_html(f'<img src="{obj.game_img.url}" alt="" width="32px">')


admin.site.register(Game, GameAdmin)