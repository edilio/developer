# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

#@login_required
def idea(request):
    return redirect('/admin/ideas/idea/')

