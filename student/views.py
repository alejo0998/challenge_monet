from rest_framework import generics
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

class StudentView(generics.ListCreateAPIView, generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request._user)
    
    def get_object(self):
        user = self.request._user
        return Student.objects.get(user=user)

    def perform_update(self, serializer):
        serializer.save()