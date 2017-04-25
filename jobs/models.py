from django.db import models

class Jobs(models.Model):
    name = models.CharField(max_length = 50)
    addr = models.TextField()
    modelNo = models.CharField(max_length = 50)
    registration = models.CharField(max_length = 50)
    attendee = models.CharField(max_length = 50)
    serviceCategory = models.CharField(max_length = 50)
    spares = models.CharField(default = "none", max_length = 50)
    lubes = models.CharField(default= "none", max_length = 50)
    date = models.DateTimeField(auto_now_add=True, blank=True)

