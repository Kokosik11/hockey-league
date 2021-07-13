from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField("Название", max_length=200)
  slug = models.SlugField("Ссылка", max_length=130, unique=True, help_text="Ссылка на пост")
  updated_on = models.DateTimeField(auto_now=True)
  content = RichTextField() # Need to connect tinymice
  created_on = models.DateTimeField(auto_now_add=True)
  date = models.DateTimeField("Дата", default=timezone.now)
  status = models.IntegerField(choices=STATUS, default=0)
  image = models.ImageField("Фото", upload_to='post_images', blank=True, default="default.png")
  views = models.IntegerField("Просмотры", default=0)

  def get_absolute_url(self):
    return reverse('post-detail', args=[self.slug])

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_on']
    verbose_name = "Пост"
    verbose_name_plural = "Посты"