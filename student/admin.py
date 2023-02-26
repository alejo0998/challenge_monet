from django.contrib import admin

from exam.models import Answer, Question, QuestionTest, Test
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from student.models import Student
# Register your models here.

class AdminStudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'students'


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request._user.is_superuser():
            return qs
        try:
            return qs.filter(student__user=request._user)
        except Exception as e:
            return qs.none()


class CustomUserAdmin(UserAdmin):
    inlines = [AdminStudentInline, AnswerInline]
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return [inline(self.model, self.admin_site) for inline in self.inlines]

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(QuestionTest)
admin.site.register(Student)
admin.site.register(Answer)