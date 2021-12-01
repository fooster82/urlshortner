from django.shortcuts import render, redirect

from .models import Url
from .forms import SubmitUrl

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = SubmitUrl(req.POST)
        if form.is_valid():
            short_url = form.save()
            return redirect('url-show', short_url=short_url)
    else:
        form = SubmitUrl()
    data = {'form': form}     
    return render(req, 'shortner/home.html', data)

def show(req, short_url):
    return 'Hello'
