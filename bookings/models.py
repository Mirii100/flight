from django.db import models

# Create your models here.
class registerClient(models.Model):
    checkbox=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    home=models.CharField(max_length=20)
    depart=models.TextField
    returning=models.TextField
    role=models.CharField(max_length=30)
    stateClass=models.CharField(max_length=20)



    def __str__(self):
        return f"role : {self.role} \n home is : ({self.home} and class you are :{self.stateClass})"


