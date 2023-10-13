from rest_framework import serializers
from .models import Question,Answer,Lessons,Score,MultiAnswer,MultiQuestion

class LessonSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='question-detail')
    class Meta:
        model = Lessons
        fields = ['title','questions']



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'



class MultiAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiAnswer
        fields = '__all__'




class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id','text']

class QuestionsSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    questions = LessonsSerializer(many=True,read_only=True)
    question_url = serializers.HyperlinkedIdentityField(read_only=True, view_name='question-detail')


    class Meta:
        model = Question
        fields = ['id','text', 'answers','questions','question_url','lessons']

    def get_answers(self, obj):
        return [multi_answer.answer for multi_answer in obj.answers.all()]
    



class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ['score',]



class QuestionsMASerializer(serializers.ModelSerializer):
    multianswer = serializers.SerializerMethodField()
    questions = LessonsSerializer(many=True,read_only=True)


    class Meta:
        model = MultiQuestion
        fields = ['id','text', 'multianswer','questions','lessons']
    def get_multianswer(self, obj):
        return [multi_answer.answer for multi_answer in obj.multianswer.all()]