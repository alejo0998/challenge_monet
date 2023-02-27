import datetime
from django.urls import reverse
from django.test import RequestFactory
from rest_framework.test import APITestCase
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import force_authenticate
from exam.models import Question, QuestionTest, Subject, Test
import jwt
from exam.views import AnswerCreate, QuestionListCreate, SubjectView, TestListCreateView
from student.models import Student



class ApiExamSubject(APITestCase):
    def test_post_forbidden(self):
        response = self.client.post(reverse("subject-list-create"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_subject(self):
        view = SubjectView.as_view()
        default_user = baker.make(User)
        factory = RequestFactory()
        dict = {
            'name': 'Pepe',
            'year': 'FIRST',
        }
        request = factory.post(reverse("subject-list-create"), data=dict)
        force_authenticate(request, user=default_user)
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subject.objects.all().count(), 1)
        self.assertEqual(response.data.get('name'), 'Pepe')

class ApiExamTest(APITestCase):
    def test_post_forbidden(self):
        response = self.client.post(reverse("test-list-create"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_test(self):
        view = TestListCreateView.as_view()
        student = baker.make(Student)
        subject = baker.make(Subject)
        factory = RequestFactory()
        dict = {
            'subject': subject.id,
            'course': 'K115',
            'student': student.id,
        }
        request = factory.post(reverse("test-list-create"), data=dict)
        force_authenticate(request, user=student.user)
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Test.objects.all().count(), 1)
        self.assertEqual(response.data.get('student'), student.id)


    def test_create_error_test(self):
        view = TestListCreateView.as_view()
        student = baker.make(Student)
        factory = RequestFactory()
        dict = {
            'subject': 123123,
            'course': 'K115',
            'student': 1231231,
        }
        request = factory.post(reverse("test-list-create"), data=dict)
        force_authenticate(request, user=student.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_test(self):
        view = TestListCreateView.as_view()
        student = baker.make(Student)
        baker.make(Test, 4)
        factory = RequestFactory()
        request = factory.get(reverse("test-list-create"))
        force_authenticate(request, user=student.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Test.objects.all().count(), 4)


class ApiQuestion(APITestCase):

    def test_post_forbidden(self):
        response = self.client.post(reverse("question-list-create"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_question(self):
        view = QuestionListCreate.as_view()
        user = baker.make(User)
        factory = RequestFactory()
        dict = {
            'text_question': "Esta es una pregunta",
        }
        request = factory.post(reverse("question-list-create"), data=dict)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.all().count(), 1)
    
    def test_list_question(self):
        view = QuestionListCreate.as_view()
        user = baker.make(User)
        baker.make(Question, 4)
        factory = RequestFactory()
        request = factory.get(reverse("question-list-create"))
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
    


class ApiQuestionAnswer(APITestCase):
    def test_post_forbidden(self):
        response = self.client.post(reverse("answer-create"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_answer(self):
        user = baker.make(User)
        payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        view = AnswerCreate.as_view()
        student = baker.make(Student, user=user)
        test = baker.make(Test, student=student)
        baker.make(QuestionTest, test=test)
        factory = RequestFactory()
        dict = {
        }
        request = factory.post(reverse("answer-create"), data=dict, HTTP_AUTHORIZATION='Bearer ' + token)
        response = view(request)
        self.assertEqual(response.status_code, 401)