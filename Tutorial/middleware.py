import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

EXEMPT_URLS=[re.compile(settings.LOGIN_URL.lstrip('/'))] # removing the first forward slash in my url for better perfomance
if hasattr (settings,'LOGIN_EXEMPT_URLS'): # checking for the LOGIN_EXEMPT_URL attr in my settings.py
    EXEMPT_URLS+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS] # updating the EXEMPT_URLS

class LoginRequiredMiddleware:
    # this method is called once when the web server starts
    def __init__(self,get_response):# called once and this is when the web starts this is the response part of the middleware factory
        self.get_response=get_response
    # this method is called once in every request
    def __call__(self,request):# called once per every request this is the request part of the middleware factory
    # it makes the middleware callable
        response=self.get_response(request)
        return response


    def process_view(self,request,view_func,view_args,view_kwargs):
        """this method returns either a HttpResponse object or None If it returns None django will
        continue processing the process_view() middleware and then the appropriate view.If it returns
        HttpResponse object django wont bother calling the appropriate view it’ll apply response middleware
        to that HttpResponse and return the result."""

        assert hasattr(request,'user')
        # assert is a python statement which evaluates to True or raise an assertion error otherwise
        # it has  a simple syntax assert expression("args")
        # hasattr takes an object and a string The result is True if the string is an attribute of the object
        path=request.path_info.lstrip('/')

        url_is_exempt=any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('accounts:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated or url_is_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)

# a middleware factory is a callable that takes get_response callable and returns  a middleware which is
# also a callable that takes a request and returns a response just like a view.It can be written as a
# Function

# def simple_middleware(get_response):

      # def middleware(request):


           # response=get_response(request)

           # return response

     # return middleware
