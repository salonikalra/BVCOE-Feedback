from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField(blank=False, null=False)
    department = models.CharField(blank=False, max_length=15)

    def save(self, *args, **kwargs):
        if self.user.username[-2] + self.user.username[-1] == '18':
            self.semester = 1
        elif self.user.username[-2] + self.user.username[-1] == '17':
            self.semester = 3
        elif self.user.username[-2] + self.user.username[-1] == '16':
            self.semester = 5
        elif self.user.username[-2] + self.user.username[-1] == '15':
            self.semester = 7

        if self.user.username[-5]+self.user.username[-4]+self.user.username[-3] == '027':
            self.department = 'CSE'
        elif self.user.username[-5]+self.user.username[-4]+self.user.username[-3] == '028':
            self.department = 'ECE'
        elif self.user.username[-5]+self.user.username[-4]+self.user.username[-3] == '030':
            self.department = 'ICE'
        elif self.user.username[-5]+self.user.username[-4]+self.user.username[-3] == '031':
            self.department = 'IT'
        elif self.user.username[-5]+self.user.username[-4]+self.user.username[-3] == '049':
            self.department = 'EEE'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student(sender, instance, **kwargs):
    instance.student.save()
