from django.db import models


class Post(models.Model):
    name= models.CharField(max_length=100)
    emailid= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    movie= models.CharField(max_length=100)
    dessert= models.CharField(max_length=100)

    def __str__(self):
        return  self.name;

class Blogs(models.Model):
    title= models.CharField(max_length=100, unique=True)
    content= models.TextField()
    emailid= models.CharField(max_length=100)

