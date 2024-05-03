from django.db import models

# Create your models here.
class TypesGift(models.Model):
    typegift=models.CharField(max_length=100)
    picture=models.ImageField()
    
    def __str__(self):
        return self.typegift

class Gifts(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    picture=models.ImageField()
    tarif=models.TextField()
    turi=models.ForeignKey(TypesGift,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

