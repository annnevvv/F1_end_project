from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from quiz.views import QuizListView, QuizDetailView, QuizSubmitView

urlpatterns = [
                  path('', QuizListView.as_view(), name='quiz_list'),
                  path('<int:quiz_id>/', QuizDetailView.as_view(),
                       name='quiz_detail'),
                  path('<int:quiz_id>/submit/', QuizSubmitView.as_view(),
                       name='submit_quiz'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
