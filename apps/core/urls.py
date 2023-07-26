from django.urls import path
from apps.core.views import question_view

urlpatterns = [
    path('', question_view, name='question-view'),
]
