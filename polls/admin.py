from django.contrib import admin
from .models import Question, Choice


admin.site.register(Question)
admin.site.register(Choice)     # admin site에 등록한다. 새로운 메뉴를