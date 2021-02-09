from django.contrib import admin
from .models import Question, UserChoice, UserName 
from import_export.admin import ImportExportModelAdmin
from.resources import QuestionResource
# Register your models here.

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

admin.site.register(Question,QuestionAdmin)               ## Can also use the decorator above the class as @admin.register(Question)
 


# admin.site.register(TestRecord)
admin.site.register(UserChoice)
admin.site.register(UserName)

