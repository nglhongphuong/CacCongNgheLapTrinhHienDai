# Các công nghệ lập trình hiện đại
## Models
### 1. In a Project
- Creating a project
```
django-admin startproject name_project
```
- Run project 
```
py manage.py runserver
```
- Adding an app in project

Creating an app
```
django-admin startapp name_app
```
Adding app in settings
```
# settings.py
INSTALLED_APPS = [
    'name_app',
    # các ứng dụng khác
]
```
- Adding database in project
```
#settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myCoursedb',#DB name is defined
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '' # mặc định localhost
    }
}
```
- After adding AstractUser in an app, we need to add User's app in project
```
#settings.py
AUTH_USER_MODE = 'name_app.User'
```
### 2. In an app
### In models.py
- Add an abstractUser of app
```
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass 
```
- Add an entity of class on model
**Example**: Adding a table named 'Category'
```
class   Category(models.Model):
    name_cols = models.CharField(max_length=50,unique=True)
```
- toString representation of an object in an Entity of class
```
def __str__(self):
      return self.name
```
- Imagefied
-- When executed, the `ImageField` in Django will combine with `MEDIA_ROOT` in `settings.py` to determine the location for uploading images.
-- `pip install pillow` to import library to work with `Image`
-- Remember creating `static` file after `migration` file in app to restore `Imanges`
```
#models.py in app
 image = models.ImageField(upload_to="name_app/%Y/%m/")#"Absolute path."
 
#settings.py in project
BASE_DIR = Path(__file__).resolve().parent.parent # it will lead to project
MEDIA_ROOT = '%s/name_app/static/' % BASE_DIR
```
- Add Foreign Key 
```
object_1 = models.ForeignKey(Entity_class, on_delete=models.CASCADE)
# on_delete=models.CASCADE: Composition
# on_delete=models.RESTRICT: Aggregation
```
### 3. Models -> migration
**Migration**:
Transitioning from code-first source to a script to prepare for database changes. (Chuyển từ mã nguồn của code first thành scripts để chuẩn bị tác động đến DB)
- Import pymysql to driver with client of project
```
#settings.py
import pymysql
pymysql.install_as_MySQLdb()
```
- Make migration to check what code will be create
```
#cmd
py manage.py makemigrations
# It will appear in file migration of app
```
- Defined name of migration to checked =)))
```
py manage.py sqlmigrate name_app named_define_migration
```
- Attack to database what things will create
```
py manage.py migrate
```
- Adding admin to manage what_model after creating superuser in project
```
#admins.py in app
admin.site.register(what_model?)
```
### 3.Inserting data to table in database (model)
1. In powershell
``` 
python manage.py shell
```
2. import any table you want to insert/delete/....
- Example: from app_name.models import *
```
#insert any things you want in named_Entity
name_Enity.objects.create(name = "Abc")
```
### 4. SUPERUSER IN DJANGO
- Link admin user in django
```
#urls.py - project
urlpatterns = [
      path('admin/',admin.site.urls),
      ]
```
- Create superuser
```
py manage.py createsuperuser
#User:.....
#email
#password
```
### 5. Meta Class
- 'Meta Class':
Lớp Meta được sử dụng để định nghĩa các thuộc tính bổ sung cho mô hình mà bạn không muốn đưa vào như là các trường (fields) trong mô hình chính.

**Attribute: Abstract Class in model cannot create Object**
```
      class Meta:
          abstract = True
          ordering = ["What?"] - Increasing list with what?
                     ["-What?"] - decreasing list with what?
```
**Attribute:  unique_together**
xác định một ràng buộc duy nhất cho một tập hợp các trường
```
  class Meta:
        unique_together = ['subject','category']
#vd: Không thể tồn tại cặp
         1 - Data mining - Computer Science
         2 - Data mining - Computer Science   => throw IntegrityError
      Có thể tồn tại cặp 
         1 - Data mining - Computer Science
         2 - Data mining - IT
         3 - Algorithm - Computer Science  
```
### 6 Model.Admin
***Insert Image***
```
from django.contrib import admin
from courses.models import Category,Course,Lesson
from django.utils.html import mark_safe

class LessonAdmin(admin.ModelAdmin):
    search_fields = ['subject','content']
    list_display = ['id','subject','active','create_date']
    list_filter = ['id','subject','create_date']
    readonly_fields = ['avatar']

    def avatar(self,lesson):
    return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)
```

***CSS***
```
#meta class
class name_what?
       class Media:
          css = {
                'all': ('/static/css/style.css', )
          }
```
### 7. libraries after coding
```
py pip freeze > requirement.txt
```
## Lỗi hay gặp
- 'remote-permission-to-repository-denied-url-returned-error-403'
"https://stackoverflow.com/questions/47465644/github-remote-permission-denied"











