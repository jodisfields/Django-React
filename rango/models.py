from django.db import models

class Rango(models.Model):
    Ship = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    IP_Address = models.TextField(max_length=30)
    Notes = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)