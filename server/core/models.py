from django.db import models


class Tree(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True, verbose_name='Родитель')
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Ветвь'
        verbose_name_plural = 'Ветви'

    def __str__(self):
        return self.name
