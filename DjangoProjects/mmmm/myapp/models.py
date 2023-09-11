from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    teaching_course = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.fullname

class Application(models.Model):
    client_name=models.CharField(max_length=200)
    client_last_name=models.CharField('Familiya',max_length=255,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    client_phone_number=models.CharField(max_length=50)


    def __str__(self):
        return f"Client name: {self.client_name}, Phone number:{self.client_phone_number}"