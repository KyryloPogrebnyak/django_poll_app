from django.urls import path
from . import views

app_name = "polls_app"
urlpatterns = [
    # ex: /polls_app/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls_app/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls_app/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls_app/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
