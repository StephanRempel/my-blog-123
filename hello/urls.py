from django.urls import path

from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[
        :5
    ],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    # path("polls/", views.polls_index, name="polls_index"),
    path("polls/", views.IndexView.as_view(), name="polls_index"),
    # path("polls/<int:question_id>/", views.polls_detail, name="polls_detail"),
    path("polls/<int:pk>/", views.DetailView.as_view(), name="polls_detail"),
    # path("polls/<int:question_id>/results/", views.polls_results, name="polls_results"),
    path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="polls_results"),
    path("polls/<int:question_id>/vote/", views.polls_vote, name="polls_vote"),
]
