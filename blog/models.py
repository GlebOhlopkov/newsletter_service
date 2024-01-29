from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='image')
    views_count = models.IntegerField(default=0, verbose_name='views_count')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='published_at')

    def __str__(self):
        return f'{self.title} (date:{self.published_at}, views: {self.views_count})'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'