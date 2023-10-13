from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializer import QuestionsSerializer , AnswerSerializer,ScoreSerializer,LessonSerializer,QuestionsMASerializer,MultiAnswerSerializer
from app.models import Question,Answer,Score,Lessons,MultiQuestion,MultiAnswer,MultiQuestion
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class LessonsView(APIView):
    def get(self,request):
        lessons = Lessons.objects.all()
        lessons_serilaizer = LessonSerializer(lessons,many=True,context={'request': request})
        return Response(lessons_serilaizer.data)
    
    def post(self, request):
        lesson_serializer = LessonSerializer(data=request.data)
        if lesson_serializer.is_valid():
            lesson_serializer.save()
            return Response(lesson_serializer.data,status=201)
        else:
            return Response(lesson_serializer.errors,status=400)



class QuestionsView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        questions_serializer = QuestionsSerializer(questions, many=True, context={'request': request}) 
        return Response(questions_serializer.data)
    
    def post(self, request):
        question_serializer = QuestionsSerializer(data=request.data,context={'request':request}) 

        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=201)  
        else:
            return Response(question_serializer.errors, status=400) 


class AnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        answer_serializer = AnswerSerializer(answers, many=True)
        return Response(answer_serializer.data)
    def post(self,request):
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data, status=202)
        else:
            return Response(answer_serializer.errors, status=400)


class QuestionDetail(APIView):
    def get(self, request,pk):
        question = Question.objects.get(pk=pk)
        question_serializer = QuestionsSerializer(question,context={'request': request})
        return Response(question_serializer.data)

class AnswerDetail(APIView):
    def get(self, request,pk):
        answer = Answer.objects.get(pk=pk)
        answer_serializer = AnswerSerializer(answer,context={'request': request})
        return Response(answer_serializer.data)
    def post(self,request):
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data, status=202)
        else:
            return Response(answer_serializer.errors, status=400)
        
        
class TestView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        questions = Question.objects.all()
        questions_serializer = QuestionsSerializer(questions,many=True,context={'request': request})
        return Response(questions_serializer.data)
    
    def post(self, request):
        question_id = request.data.get('id')
        user_answer = request.data.get('answers')

        # Get the correct answer as a string
        correct_answer = Answer.objects.filter(question=question_id, is_correct=True).values_list('answer', flat=True).first()

        if correct_answer is not None:
            # Check if the user's answer matches the correct answer as a string
            if user_answer == correct_answer:
                try:
                    score = Score.objects.get(user=request.user)
                    score.score += 1
                    score.save()
                except Score.DoesNotExist:
                    score = Score.objects.create(user=request.user, score=1)

                score_serializer = ScoreSerializer(score)
                return Response({'message': 'your answer was correct', 'score': score_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'your answer was incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'correct answer not found for this question'}, status=status.HTTP_404_NOT_FOUND)


class TestMultiAnswer(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        questions = MultiQuestion.objects.all()
        questions_serializer = QuestionsMASerializer(questions,many=True,context={'request': request})
        return Response(questions_serializer.data)
    
    def post(self, request):
        question_id = request.data.get('id')
        user_answer = request.data.get('multianswer')

        correct_answers = MultiAnswer.objects.filter(question=question_id, is_correct=True).values_list('answer', flat=True)

        is_correct = all(answer in correct_answers for answer in user_answer)

        if is_correct:
            try:
                score = Score.objects.get(user=request.user)
                score.score += 1
                score.save()
            except Score.DoesNotExist:
                score = Score.objects.create(user=request.user, score=1)
            score_serializer = ScoreSerializer(score)

            return Response({'message': 'your answer was correct','score':score_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'your answer was incorrect'}, status=status.HTTP_400_BAD_REQUEST)




class QuestionsMAView(APIView):
    def get(self, request):
        questions_m_a = MultiQuestion.objects.all()
        questions_serializer = QuestionsMASerializer(questions_m_a, many=True, context={'request': request}) 
        return Response(questions_serializer.data)
    
    def post(self, request):
        question_serializer = QuestionsMASerializer(data=request.data,context={'request':request}) 

        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=201)  
        else:
            return Response(question_serializer.errors, status=400) 
        



class MultiAnswerView(APIView):
    def get(self, request):
        answers = MultiAnswer.objects.all()
        answer_serializer = MultiAnswerSerializer(answers, many=True)
        return Response(answer_serializer.data)
    def post(self,request):
        answer_serializer = MultiAnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data, status=202)
        else:
            return Response(answer_serializer.errors, status=400)


       
        