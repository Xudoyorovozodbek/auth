from django.db import models

class Talaba(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=18)
    contact_number=models.IntegerField(default=+998938066344)
    def __str__(self):
        return f"{self.name} , {self.age} , {self.contact_number}"
