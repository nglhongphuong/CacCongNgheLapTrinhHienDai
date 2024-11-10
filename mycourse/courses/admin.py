from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse

from courses.models import Category, Course, Lesson
from django.utils.html import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.urls import path
class MyCourseAdmin(admin.AdminSite):
    site_header = 'Ou e course'
    def get_urls(self):
        return [path('course-stats/', self.stats)] + super().get_urls()

    def stats(self, request):
        stats = Category.objects.annotate(count=Count('course__id')).values('id', 'name', 'count')
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': stats
        })

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
admin_site = MyCourseAdmin(name='eCourse')

admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Lesson, LessonAdmin)