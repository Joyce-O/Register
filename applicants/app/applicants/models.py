from django.db import models

# Create your models here.


class Users(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=225)
    lastname = models.TextField()
    age = models.IntegerField(null=True)
    job_position = models.TextField(max_length=225, null=True)

    def __str__(self):
        return self.firstname
