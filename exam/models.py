from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=20)
    class Year(models.TextChoices):
        FIRST = 'FIRST', 'First year'
        SECOND = 'SECOND', 'Second year'
        THIRD = 'THIRD', 'Third year'
        FOURTH = 'FOURTH', 'Fourth year'
        FIFHT = "FIFTH", 'Fifth year'
    year = models.CharField(max_length=25, choices=Year.choices)

class Test(models.Model):
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    course = models.CharField(max_length=20)
    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    note = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)], null=True)
    date_init = models.DateTimeField(null=True)
    date_finish = models.DateTimeField(null=True)

class Question(models.Model):
    text_question = models.CharField(max_length=500)

class QuestionTest(models.Model):
    test = models.ForeignKey(Test, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)

class Answer(models.Model):
    question_test = models.OneToOneField(QuestionTest, null=False, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=500)
    note = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)], null=True)
