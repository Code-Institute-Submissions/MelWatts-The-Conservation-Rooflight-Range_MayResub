from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
      
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Stories(models.Model):

    class Meta:
        verbose_name_plural = 'Stories'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    size = models.TextField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
