from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# quiz_api/models.py

from django.db import models

class Lessons(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Question(models.Model):
    lessons = models.ForeignKey(Lessons, related_name='questions', on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=225, unique=True)

    def __str__(self):
        return str(self.text)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return str(self.answer)


class MultiQuestion(models.Model):
    lessons = models.ForeignKey(Lessons, related_name='questionsWM', on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=225, unique=True)

    def __str__(self):
        return str(self.text)
    



class MultiAnswer(models.Model):
    question = models.ForeignKey(MultiQuestion, related_name='multianswer', on_delete=models.CASCADE,null=True)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return str(self.answer)
    
class Score(models.Model):
    user = models.OneToOneField(User, related_name='score', on_delete=models.CASCADE,null=True)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)