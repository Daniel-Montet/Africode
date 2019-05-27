from django import forms

from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields =[
            'title',
            'description',
            'order',
            'total_questions',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control z-depth-1 title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control z-depth-1 description'})
        self.fields['order'].widget.attrs.update({'class': 'form-control z-depth-1 order'})
        self.fields['total_questions'].widget.attrs.update({'class': 'form-control z-depth-1 questions'})


class QuestionForm(forms.ModelForm):
    class Media:
        css = {'all': ('courses/css/order.css',)}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )

class TrueFalseQuestionForm(QuestionForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prompt'].widget.attrs.update({'class': 'form-control z-depth-1 prompt ','rows':'2'})
        self.fields['order'].widget.attrs.update({'class': 'form-control z-depth-1 order'})
        
class MultipleChoiceQuestionForm(QuestionForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'prompt',
            'shuffle_answers',
            'order'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].widget.attrs.update({'class': 'form-control z-depth-1 order'})
        self.fields['prompt'].widget.attrs.update({'class': 'form-control z-depth-1 prompt ','rows':'2'})
        self.fields['shuffle_answers'].widget.attrs.update({'class': 'form-control z-depth-1 shuffle_answers'})

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields= [
            'order',
            'text',
            'correct'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].widget.attrs.update({'class': 'form-control z-depth-1 order'})
        self.fields['text'].widget.attrs.update({'class': 'form-control z-depth-1 text'})
        self.fields['correct'].widget.attrs.update({'class': 'form-control z-depth-1 correct'})

AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm
)

AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,
    models.Answer,
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1
)