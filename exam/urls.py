from django.urls import path

from exam.views import SubjectView, QuestionListCreate, QuestionTestCreate, QuestionTestList, AnswerCreate, TestAnswerList, TestListCreateView


urlpatterns = [
    path('subject/', SubjectView.as_view(), name='subject-list-create'), #Endpoint para crear y listar materias.
    path('test/', TestListCreateView.as_view(), name='test-list-create'), #Enpoint para crear y listar examenes
    path('question/', QuestionListCreate.as_view(), name='question-list-create'), #Endpoint para crear y listar preguntas.
    path('test/question/', QuestionTestCreate.as_view(), name='question-test-create'), #Endpoint para asociar una pregunta a un examen.
    path('test/<int:test_id>/question/', QuestionTestList.as_view() ,name='question-test-list'), #Endpoint para listar todas las preguntas de un examen.
    path('answer/', AnswerCreate.as_view(), name='answer-create'), #Endpoint para crear una respuesta.
    path('test/<int:test_id>/answer/', TestAnswerList.as_view() ,name='question-test-list'), #Endpoint para obtener todas las respuestas a un examen.

]
