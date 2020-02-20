from django.db import models
from django.contrib.auth.models import User

#class List(models.Model):
#    name = models.CharField(max_length=100)
#    occasion = models.CharField(max_length=100)
#    owner = models.ForeignKey(User,max_length=100, on_delete=models.CASCADE )

class Wish(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    image = models.ImageField(null = True , blank = True )
    owner = models.ForeignKey(User,max_length=100, on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name
