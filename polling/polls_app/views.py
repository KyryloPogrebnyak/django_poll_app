from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls_app/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    #output = "/ ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, "polls_app/index.html", context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    """try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls_app/detail.html", {"question": question})

def results(request, question_id):
    responce = "You're lookig at the result of question %s." 
    return HttpResponse(responce % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)