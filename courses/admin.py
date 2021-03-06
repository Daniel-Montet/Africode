from django.contrib import admin
from datetime import date
from . import models
# Register your models here.

class QuizInline(admin.StackedInline):
    model = models.Quiz

class TextInline(admin.StackedInline):
    model = models.Text

class MultipleChoiceQuestionInline(admin.StackedInline):
    model = models.MultipleChoiceQuestion

class AnswerInline(admin.StackedInline):
    model = models.Answer


class YearListFilter(admin.SimpleListFilter):
    title = 'year created'

    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            ('2015', '2015'),
            ('2016', '2016'),
        )

    def queryset(self, request, queryset):
        if self.value() == '2015':
            return queryset.filter(created_at__gte=date(2015,1,1),
                                    created_at__lte=date(2015,12,31)
        )
        if self.value() == '2016':
            return queryset.filter(created_at__gte=date(2016,1,1),
                                    created_at__lte=date(2016,12,31)
        )



class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline,]

    search_fields = ['title', 'description']
    list_filter = ['created_at', YearListFilter]
    list_display = ['title', 'created_at']
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceQuestionInline,]

    search_fields = ['prompt',]
    list_display = ['prompt', 'quiz', 'order']
    list_editable = ['quiz', 'order']


class MultipleQuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]

    search_fields = ['prompt',]

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Quiz)
admin.site.register(models.Text)
admin.site.register(models.Answer)
admin.site.register(models.Question)
admin.site.register(models.MultipleChoiceQuestion, MultipleQuestionAdmin)

