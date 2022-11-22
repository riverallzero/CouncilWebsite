# from django.contrib import admin
# from .models import Qna
#
# # Register your models here.
# admin.site.register(Qna)
from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)