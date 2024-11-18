from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass 
# Create your models here.
class BaseMode(models.Model):
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add= True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True
        ordering = ["id"]


class   Category(BaseMode):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name


class Course(BaseMode):
    subject = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/%Y/%m/")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    class Meta:
        unique_together = ['subject', 'category']

class Lesson(BaseMode):
    subject = models.CharField(max_length=50,null=False)
    content = RichTextField() #nhung bo cong cu chinh sua
    image=models.ImageField(upload_to="lessons/%Y/%m/")
    course = models.ForeignKey(Course,on_delete=models.RESTRICT)
    def __str__(self):
        return self.subject
    