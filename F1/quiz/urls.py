from django.contrib import admin
from django.urls import path
from quiz.views import QuizListView, QuizDetailView, QuizSubmitView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:quiz_id>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', QuizSubmitView.as_view(), name='submit_quiz'),
]