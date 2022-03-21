from django.contrib import admin
from .models import LogUploadModel, TlogEvaluate
from accounts.models import User

# Register your models here.

class TlogEvaluateAdmin(admin.ModelAdmin):
    list_display = ['evaluate_score', 'evaluate_content', 'evaluate_time', 'evaluate_coach']

class TlogEvaluateInline(admin.TabularInline):
    model = TlogEvaluate
    extra = 1




class tlogAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'author_role', 'log_date', 'class_type', 'module_list', 'log_file', 'uploaded_date']
    list_filter = ['author_name', 'author_role', 'log_date', 'class_type', 'module_list', 'log_file']
    search_fields = ['author_name', 'author_role', 'log_date', 'class_type', 'module_list', 'log_file']
    inlines = [TlogEvaluateInline]



admin.site.register(LogUploadModel, tlogAdmin)
# admin.site.register(TlogEvaluate, TlogEvaluateAdmin)