from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название', max_length=256)
    data = models.DateTimeField('Дата', auto_now_add=True)
    text = models.TextField('Текст')
    photo = models.ImageField(upload_to='images', verbose_name='Картинка')
    tags = models.ManyToManyField('Tags')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('theme', kwargs={'theme_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['data', 'title']


class Tags(models.Model):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
