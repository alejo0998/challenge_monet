from django.urls import reverse
from django.test import RequestFactory
from rest_framework.test import APITestCase
from model_bakery import baker
from student.models import Student
from student.views import StudentView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import force_authenticate



class ApiStudent(APITestCase):
    def test_post_forbidden(self):
        response = self.client.post(reverse("student-list-create"))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_student(self):
        view = StudentView.as_view()
        default_user = baker.make(User)
        factory = RequestFactory()
        dict = {
            'user': default_user.id,
            'name': 'Pepe',
            'last_name': 'Pepe',
            'date_of_birth': '1998-10-09',
            'phone': '112354234',
            'gender': 'MALE'
        }
        request = factory.post(reverse("student-list-create"), data=dict)
        force_authenticate(request, user=default_user)
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.all().count(), 1)
        self.assertEqual(response.data.get('name'), 'Pepe')

    def test_create_student_sin_name(self):
        view = StudentView.as_view()
        default_user = baker.make(User)
        factory = RequestFactory()
        dict = {
            'user': default_user.id,
            'last_name': 'Pepe',
            'date_of_birth': '1998-10-09',
            'phone': '112354234',
            'gender': 'MALE'
        }
        request = factory.post(reverse("student-list-create"), data=dict)
        force_authenticate(request, user=default_user)
        response = view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Student.objects.all().count(), 0)
