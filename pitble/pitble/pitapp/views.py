from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render_to_response('pitapp/index.html',
                              {},
                              context_instance=RequestContext(request))
