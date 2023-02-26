from django.contrib import admin

from exam.models import Answer, Question, QuestionTest, Test

from student.models import Student


class AnswerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(student__user=request.user)
        except Exception as e:
            return qs.none()


admin.site.register(Test)
admin.site.register(Question)
admin.site.register(QuestionTest)
admin.site.register(Student)
admin.site.register(Answer, AnswerAdmin)