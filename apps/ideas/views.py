# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def ideas(request):
    return redirect('/admin/ideas/idea/')

