"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import (
    IndexViewQuestion,
    QuestionView,
    QuestionCreate,
    QuestionUpdateView,
    QuestionDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexViewQuestion.as_view(), name='index_question'),
    path('question/<int:id>/', QuestionView.as_view(), name='poll'),
    path('question/create/', QuestionCreate.as_view(), name='question_create'),
    path('question/<int:id>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:id>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
]
