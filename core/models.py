from django.db import models
from django.conf import settings
from django.utils import timezone


class Game(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor')
    name_game = models.CharField('Nome do jogo', max_length=50)
    release_year = models.DecimalField('Ano de Lançamento', max_digits=4, decimal_places=0)
    text = models.TextField('Resumo do jogo',())
    date_publish = models.DateField('Data de publicação', default=timezone.now)
    game_img = models.ImageField('Foto do Game', upload_to='media', blank=False)

    def publish_game(self):
        self.publish_game = timezone.now()
        self.save()

    def __str__(self):
        return self.name_game

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
