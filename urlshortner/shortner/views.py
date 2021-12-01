from django.shortcuts import render, redirect

from .models import Url
from .forms import SubmitUrl

# Create your views here.
def home(req):
    if req.method == 'POST':
        url = SubmitUrl(req.POST)
        if url.is_valid():
            url.short_url = Url.make_url_small()
            data = url.save()            
            return redirect('shortner-home', data)
    else:
        form = SubmitUrl()
    data = {'form': form}     
    return render(req, 'shortner/home.html', data)

def show(req, short_url):
    return 'Hello'
