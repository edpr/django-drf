from django.db import models

# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length=225)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(selfs):
        return selfs.title

    def __repr__(self):
        return self.title

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/featured_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True )
    tags = models.TextField(default='')

    def __str__(self):
        return  self.title

    def __repr__(self):
        return self.title
