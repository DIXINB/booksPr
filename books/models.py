from django.db import models


class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    def __str__(self):
	    return u'%s %s' % (self.first_name, self.last_name)
	    #return self.first_name 
class Book(models.Model):
    authors=models.ManyToManyField(Author)
    title=models.CharField(max_length=70)
    content=models.CharField(max_length=150)
    publication=models.SmallIntegerField()
    num=models.SmallIntegerField()
    def __str__(self):
	    return self.title
class Hist(models.Model):
    ind=models.SmallIntegerField(default=0)
    title=models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title
class Artc(models.Model):
    ind=models.SmallIntegerField(default=0)
    title=models.CharField(max_length=70)
    content=models.TextField()
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title
class Dict(models.Model):
    lat=models.CharField(max_length=70)
    trans=models.CharField(max_length=70)
    rus=models.CharField(max_length=150)
    def __str__(self):
	    return self.lat
class Pros(models.Model):
    ind=models.SmallIntegerField(default=0)
    author=models.CharField(max_length=70)
    title=models.CharField(max_length=70)
    image=models.ImageField(upload_to="bks/list",
          verbose_name="Основное изображение",null=True,blank=True)
    def __str__(self):
	    return self.title		
		
# Create your models here.
