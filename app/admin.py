from django.contrib import admin
from .models import Question,Lessons,Answer,Score,MultiAnswer,MultiQuestion
# Register your models here.
admin.site.register(Question)
admin.site.register(Lessons)
admin.site.register(Answer)
admin.site.register(Score)
admin.site.register(MultiAnswer)
admin.site.register(MultiQuestion)