from rest_framework import generics
from rest_framework.response import Response
from exam.serializers import AnswerListSerializer, AnswerSerializer, QuestionSerializer, QuestionTestVistaSerializer, SubjectSerializer, TestSerializer, QuestionTestSerializer
from exam.models import Subject, Test, Question, Answer, QuestionTest
from rest_framework.permissions import IsAuthenticated

class SubjectView(generics.ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class TestListCreateView(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]


class TestRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs["pk"])
        return obj

class QuestionListCreate(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]


class QuestionTestCreate(generics.CreateAPIView):
    serializer_class = QuestionTestSerializer
    queryset = QuestionTest.objects.all()
    permission_classes = [IsAuthenticated]


class QuestionTestList(generics.ListAPIView):
    serializer_class = QuestionTestVistaSerializer
    queryset = QuestionTest.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return self.queryset.filter(test=test_id)

class AnswerCreate(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        question_test = QuestionTest.objects.get(id=request.data.get('question_test'))
        if question_test.test.student.user != request._user:
            return Response('La pregunta no pertenece al estudiante, por lo cual no puede responder')
        return super().post(request, *args, **kwargs)


class TestAnswerList(generics.ListAPIView):
    serializer_class = AnswerListSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return self.queryset.filter(question_test__test=test_id)
