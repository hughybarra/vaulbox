from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render
from polls.models import Poll
from django.http import Http404



def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
        context = {"poll":poll}
    except Poll.DoesNotExist:
#         return HttpResponse("failed")
        raise Http404
    return render(request, 'polls/detail.html', context)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)