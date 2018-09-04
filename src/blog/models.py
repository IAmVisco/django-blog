from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=64)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={'id': self.id})
