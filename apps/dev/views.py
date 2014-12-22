# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('index.html')


def modules(request):
    return redirect('/admin/dev/devmodule/')


def submodules(request):
    return redirect('/admin/dev/submodule/')

