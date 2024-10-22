from django.contrib import admin
from courses.models import Category,Course,Lesson
from django.utils.html import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
#form cho phép nhúng để upload
    content = forms.CharField(widget=CKEditorUploadingWidget)
    #đè lên Lesson
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    search_fields = ['subject','content']
    list_display = ['id','subject','active','create_date']
    list_filter = ['id','subject','create_date']
    readonly_fields = ['avatar']
    form = LessonForm #LessonForm đè lên

    def avatar(self,lesson):
            return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")
    
    class Media:
             css = {
               'all': ('/static/css/style.css', )
             }


# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)