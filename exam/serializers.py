from rest_framework import serializers
from exam.models import Answer, Question, Subject, Test, QuestionTest


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'year']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'subject', 'course', 'student', 'note', 'date_init', 'date_finish' ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text_question']

class QuestionTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTest
        fields = ['id', 'test', 'question']

class QuestionTestVistaSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    test = TestSerializer()
    class Meta:
        model = QuestionTest
        fields = ['id', 'test', 'question']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','question_test', 'text_answer']


class QuestionTestAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    test = TestSerializer()
    class Meta:
        model = QuestionTest
        fields = ['id', 'test', 'question']

class AnswerListSerializer(serializers.ModelSerializer):
    question_test = QuestionTestAnswerSerializer()
    class Meta:
        model = Answer
        fields = ['id','question_test', 'text_answer']