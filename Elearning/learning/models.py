from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)


class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=70, blank=True)
    enrollment = models.ManyToManyField('Student')
    Teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, blank=True, null=True)
    categories = models.ManyToManyField(Category,blank=True,null=True)

    def __str__(self):
        return self.name
