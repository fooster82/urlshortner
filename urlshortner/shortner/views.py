from django.shortcuts import render, redirect

from .models import Url
from .forms import SubmitUrl

# Create your views here.
def home(req):
    if req.method == 'POST':
        url = SubmitUrl(req.POST)
        if url.is_valid():
            original_url = url.cleaned_data.get('original_url')
            new_url = Url()            
            new_url.original_url = original_url
            new_url.short_url = Url.make_url_small()
            new_url.save()      
            data = {
                'form': url,
                'url': new_url
            }                 
            return render(req, 'shortner/home.html', data)
        else:
            print(url.errors)
    form = SubmitUrl()
    data = {'form': form}     
    return render(req, 'shortner/home.html', data)

def show(req, short_url):
    try:
        actual_url = Url.objects.filter(short_url=short_url)[0]
        return redirect(actual_url.original_url)
    except:
        form = SubmitUrl()
        data = {'form': form}     
        return render(req, 'shortner/home.html', data)

def handle_500(req):
    return render(req, 'shortner/home.html')