from django.contrib import admin

# Register your models here.
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'content', 'create_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)