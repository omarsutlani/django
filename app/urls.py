from django.urls import path
from app.views import QuestionsView,AnswerView,QuestionDetail,AnswerDetail,TestView,LessonsView,QuestionsMAView,MultiAnswerView,TestMultiAnswer
urlpatterns = [
    path('lessons/',LessonsView.as_view(),name='lessons' ),
    path('questions/',QuestionsView.as_view(),name='questions' ),
    path('question/<int:pk>',QuestionDetail.as_view(),name='question-detail' ),
    path('multi-answer-questions/',QuestionsMAView.as_view(),name='multi-answer-questions' ),

    path('answers/',AnswerView.as_view(),name='answers' ),
    path('answer/<int:pk>',AnswerDetail.as_view(),name='answer-detail' ),
    path('test/',TestView.as_view(),name='test' ),
    path('multianswer/<int:pk>',AnswerDetail.as_view(),name='multianswer-detail' ),
    path('multianswer/',MultiAnswerView.as_view(),name='multianswer' ),
    path('multi-answer-test/',TestMultiAnswer.as_view(),name='multi-answer-test' ),


]
