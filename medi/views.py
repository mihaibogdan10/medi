from django.http import HttpResponse
from django.template import RequestContext, loader
from django.conf import settings

def home(request):
    return_dict = {}
    t = loader.get_template('home.html')
    c = RequestContext(request, return_dict)
    return HttpResponse(t.render(c))
