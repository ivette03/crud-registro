from django.db import models
#libreria datetime
from datetime import date
class estudiantes(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    Last_name=models.CharField(max_length=50,null=False,blank=False)
    document=models.CharField(max_length=10,null=False,blank=False)
    email=models.EmailField(max_length=50,blank=True,null=True)
    date=models.DateField(default=date.today)
    

    def __str__(self):
        return self.name


