# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')

#@login_required
def modules(request):
    return redirect('/admin/dev/devmodule/')

#@login_required
def submodules(request):
    return redirect('/admin/dev/submodule/')

