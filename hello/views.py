from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.utils.timezone import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage, Question


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def polls_index(request):
    """Renders the polls page."""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("hello/polls_index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def polls_detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def polls_results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def polls_vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )


@csrf_exempt
def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})
