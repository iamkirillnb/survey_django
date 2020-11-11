from django.shortcuts import render
from django.views.generic import TemplateView

from .models import MySurvey, Quest, Users
from .forms import UserForm
from  django.views.generic.edit import CreateView
from django.forms import ModelForm

def index(request):
    surveys = MySurvey.objects.all()
    return render(request, 'index.html', {'surveys': surveys})


def by_survey(request, survey_id):
    form = UserForm

    all_survey = MySurvey.objects.all()
    current_survey = MySurvey.objects.get(pk=survey_id)
    questions = Quest.objects.filter(survey=survey_id)
    context = {'questions': questions, 'all_survey': all_survey, 'current_survey': current_survey, 'form': form}
    return render(request, 'by_survey.html', context)


class UserAnswer(CreateView):
    template_name = by_survey
    form_class = UserForm
    success_url = 'http://127.0.0.1:8000/'

    def get_answers(self, *args, **kwargs):
        answers = super().get_context_data(**kwargs)
        answers['answer'] = Users.objects.all()
        return answers
