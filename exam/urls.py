from django.urls import path

from exam.views import SubjectView, QuestionListCreate, QuestionTestCreate, QuestionTestList, AnswerCreate, TestAnswerList, TestListCreateView


urlpatterns = [
    path('subject/', SubjectView.as_view(), name='subject-list-create'),
    path('test/', TestListCreateView.as_view(), name='test-list-create'),
    path('question/', QuestionListCreate.as_view(), name='question-list-create'), #Para crear y obtener preguntas
    path('test/question/', QuestionTestCreate.as_view(), name='question-test-create'), #Para asociar una pregunta a un examen
    path('test/<int:test_id>/question/', QuestionTestList.as_view() ,name='question-test-list'), #Para obtener todas las preguntas de un examen
    path('answer/', AnswerCreate.as_view(), name='answer-create'), #Para registrar una respuesta de un test
    path('test/<int:test_id>/answer/', TestAnswerList.as_view() ,name='question-test-list'), #Para obtener todas las respuestas de un test

]
