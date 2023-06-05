from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.utils.timezone import datetime
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import Choice, LogMessage, Question


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


# def polls_index(request):
#     """Renders the polls page."""
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("hello/polls_index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, "hello/polls_index.html", context)  # shortcut


class IndexView(generic.ListView):
    template_name = "hello/polls_index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


# def polls_detail(request, question_id):
#     try:
#         question = get_object_or_404(Question, pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "hello/polls_detail.html", {"question": question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "hello/polls_detail.html"


# def polls_results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "hello/polls_results.html", {"question": question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = "hello/polls_results.html"


def polls_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "hello/polls_detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls_results", args=(question.id,)))

    # return HttpResponse("You're voting on question %s." % question_id)


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
