from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from itertools import chain


from . import models
from . import forms
from . import serializers
# Create your views here.

def course_list(request):
    courses = models.Course.objects.filter(published=True)
    email = 'questions@learning_site.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email':email})

def course_detail(request, pk):
    course = get_object_or_404(models.Course,pk=pk, published=True)
    try:
        course = models.Course.objects.prefetch_related(
            'quiz_set', 'text_set', 'quiz_set__question_set'
        ).get(pk=pk, published=True)
    except models.Course.DoesNotExist:
        raise Http404
    else:
        steps = sorted(chain(
            course.text_set.all(),
            course.quiz_set.all()
            ),key=lambda step: step.order)
    return render(request, 'courses/course_detail.html',{'course': course, 'steps': steps})

def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk, course__published=True)
    return render(request, 'courses/text_detail.html',{'step': step})

def quiz_detail(request, course_pk, step_pk):
    try:
        step = models.Quiz.objects.select_related('course').get(
            course_id=course_pk, pk=step_pk, course__published=True
        )
    except models.Quiz.DoesNotExist:
        raise Http404
    else:
        return render(request, 'courses/quiz_detail.html',{'step': step})

# @login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(models.Course, pk=course_pk, published=True)
    form = forms.QuizForm()

    if request.method == 'POST':
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.add_message(request, messages.SUCCESS, "Quiz Added")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {'form': form})

# @login_required
def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course_id=course_pk, course__published=True)
    form = forms.QuizForm(instance=quiz)
    if request.method == 'POST':
        form = forms.QuizForm(instance=quiz,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated {}'.format(form.cleaned_data['title']))
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {'form': form})

# @login_required
def create_question(request, quiz_pk, question_type):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course__published=True)
    if question_type == 'tf':
        form_class = forms.TrueFalseQuestionForm
    else:
        form_class = forms.MultipleChoiceQuestionForm
    
    form = form_class()
    answer_forms = forms.AnswerInlineFormSet(queryset=models.Answer.objects.none())

    if request.method == 'POST':
        form = form_class(request.POST)
        answer_forms = forms.AnswerInlineFormSet(request.POST,queryset=models.Answer.objects.none())

        if form.is_valid() and answer_forms.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question =question
                answer.save()
            messages.success(request, "Added question")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/question_form.html',{
            'quiz': quiz,
            'form': form,
            'formset': answer_forms,
            })

# @login_required
def edit_question(request, quiz_pk, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk, quiz_id=quiz_pk)
    if hasattr(question, 'truefalsequestion'):
        form_class = forms.TrueFalseQuestionForm
        question = question.truefalsequestion
    else:
        form_class = forms.MultipleChoiceQuestionForm
        question = question.multiplechoicequestion
    form = form_class(instance=question)
    answer_forms = forms.AnswerInlineFormSet(queryset=form.instance.answer_set.all())

    if request.method == 'POST':
        form = form_class(request.POST, instance=question)
        answer_forms = forms.AnswerInlineFormSet(request.POST,queryset=form.instance.answer_set.all())
        if form.is_valid() and answer_forms.is_valid():
            form.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()
            messages.success(request, "Updated question")
            return HttpResponseRedirect(question.quiz.get_absolute_url())
    return render(request, 'courses/question_form.html', {'form': form, 'quiz': question.quiz,'formset': answer_forms,})


# @login_required
def answer_form(request, question_pk):
    question = get_object_or_404(models.Question, pk=question_pk)
    formset = forms.AnswerFormSet(queryset=question.answer_set.all())

    if request.method == 'POST':
        formset = forms.AswerFormSet(request.POST, queryset=question.answer_set.all())

        if formset.is_valid():
            answers = formset.save(commit=False)
            for answer in answers:
                answer.question=question
                answer.save()
        messages.success(request, "Added answers")
        return HttpReponseRedirect(question.quiz.get_absolute_url())
    return render(request, 'courses/answer_form.html', {'question': question, 'formset': formset})


def courses_by_teacher(request, teacher):
    courses = models.Course.objects.filter(teacher__username=teacher, published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})

def search(request):
    term = request.GET.get('q')
    courses = models.Course.objects.filter(
            Q(title__icontains=term)|Q(description__icontains=term),
            published=True 
        )
    return render(request, 'courses/course_list.html', {'courses': courses})


#API views start here
class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer