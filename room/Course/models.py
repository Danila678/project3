from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Module(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Material(models.Model):
    title = models.CharField(max_length=255)

class UserProgress(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
