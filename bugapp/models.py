from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1', 'Admin'),
        ('2', 'Staff'),
        ('3', 'User')
    )
    
    user_type = models.CharField(choices=USER, max_length=1, default='1')
    profile_pic = models.ImageField(upload_to='static/uploads', null=True, default='static/media/avatar1.png')
    
class customer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    

class staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class bug_report(models.Model):
    URGENCY_LEVEL = (
        ('1', 'low'),
        ('2', 'medium'),
        ('3', 'high')
    )
    
    IMPACT_ON_USER = (
        ('1', 'major'),
        ('2', 'moderate'),
        ('3', 'minor'),
    )
    
    DEPARTMENT = (
        ('1', 'Backend'),
        ('2', 'Frontend'),
        ('3', 'Other'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bug_image = models.ImageField(upload_to='uploads')
    urgency_level = models.CharField(choices=URGENCY_LEVEL, max_length=10, default='1')
    impact_on_user = models.CharField(choices=IMPACT_ON_USER, max_length=10, default='1') 
    department = models.CharField(choices=DEPARTMENT, max_length=10, default='1')
    priority = models.CharField(max_length=10 , default='medium', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


# model for bug status
class bug_status(models.Model):
    STATUS = (
        ('1', 'Open'),
        ('2', 'In Progress'),
        ('3', 'Resolved'),
    )
    
    bug = models.ForeignKey(bug_report, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20, default='1')
    assigned_to = models.ForeignKey(staff, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.bug.title
