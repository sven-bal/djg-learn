from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader

def index(request):
	laste_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls\\index.html')
	c = Context({
			'laste_poll_list':laste_poll_list,
		})
	#output = ','.join([p.question for p in laste_poll_list])
	return HttpResponse(t.render(c))

def detail(request,poll_id):
	return HttpResponse("You're looking at poll %s" % poll_id)

def results(request,poll_id):
	return HttpResponse("You're looking at the results of poll %s" % poll_id)

def vote(request,poll_id):
	return HttpResponse("you're voting on poll %s" % poll_id)
# Create your views here.
