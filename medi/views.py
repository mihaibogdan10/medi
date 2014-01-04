from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from forms import SignUpForm
from random import choice
from string import letters

def home(request):
    return render_to_response('home.html', RequestContext(request))

def about(request):
    return render_to_response('about.html', RequestContext(request))

@csrf_protect
def login_view(request):
    """ User login form """
    def errorHandle(error):
        form = AuthenticationForm()
        return render_to_response('login.html', {
            'error' : error,
            'form' : form,
        }, RequestContext(request))

    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['username'], 
                            password=data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                return errorHandle('Disabled account')
        else:
            return errorHandle('Invalid login') 
    else:
        form = AuthenticationForm()
        return render_to_response('login.html', {'form':form},
                                  RequestContext(request))

@csrf_protect
def sign_up(request):
    """ User sign up form """
    def errorHandle(error):
        form = AuthenticationForm()
        return render_to_response('signup.html', {
            'error' : error,
        }, RequestContext(request))

    if request.method == 'POST':
        data = request.POST.copy() # so we can manipulate data

        # random username
        data['username'] = ''.join([choice(letters) for i in xrange(30)])
        form = SignUpForm(data)

        if form.is_valid():
            form.save()
            user = authenticate(username=data['email'], 
                                password=data['password1'])
            
            #The user just signed up, this is a sanity check:
            assert(user is not None)

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                return errorHandle('Please activate your account.\
                                    Check the instructions in your e-mail.')
    else:
        form = SignUpForm()

    return render_to_response('sign_up.html', {'form':form},
                              RequestContext(request))

