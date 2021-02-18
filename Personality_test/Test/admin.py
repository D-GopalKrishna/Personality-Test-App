from django.contrib import admin
from .models import Question, UserData, userSelection 
from import_export.admin import ImportExportModelAdmin
from import_export import resources


## For Import export facility in the admin panel
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

admin.site.register(Question,QuestionAdmin)               ## Can also use the decorator above the class as @admin.register(Question)
 


# admin.site.register(TestRecord)
# admin.site.register(UserChoice)
admin.site.register(UserData)
admin.site.register(userSelection)

