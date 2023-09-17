from django.db import models

#create Your Model Here!
class Contact(models.Model):
        name=models.CharField(max_length=122)
        email=models.CharField(max_length=122)
        phone=models.CharField(max_length=122)

        def __str__(self):
            return self.name
        
        