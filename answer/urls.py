from django.urls import path, include

from . import views
from .views import index, by_survey, UserAnswer


urlpatterns = [
    path('', index),
    path('<int:survey_id>/', by_survey, name='by_survey'),
    path('<int:survey_id>/', UserAnswer.as_view()),
]
