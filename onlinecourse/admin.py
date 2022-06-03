from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInline(admin.StackedInline):
    model = Question
    fields = ('question_text', 'grade')
    extra = 1


class ChoiceInline(admin.StackedInline):
    model = Choice
    fields = ('choice_text', 'is_correct')
    extra = 1

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('question_text', 'grade')
    list_filter = ['question_text']
    search_fields = ['question_text', 'grade']

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('choice_text', 'is_correct')
    list_filter = ['choice_text']
    search_fields = ['choice_text', 'is_correct']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

