from django.db import models
from django.conf import settings
from PIL import Image

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=200, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # cette clase permet de spécifier des permissions beaucoup plus fines
    class Meta:
        permissions = [
            ('change_blog_title', 'Peut changer le titre d\'un billet')
        ]

    def __str__(self) -> str:
        return self.caption

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
        
class Blog(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def _get_word_count(self):
        return len(self.content.split(' '))
    
    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)
        
class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        """
        Nous avons défini l'attribut   unique_together  dans la classe   Meta  pour garantir 
        qu'il n'y a qu'une seule instance de  BlogContributor  pour chaque paire   
        contributor  -   blog
        """
        unique_together = ('contributor', 'blog')