from django.shortcuts import render, redirect

# Create your views here.
def home(req):
    if req.method == 'POST':
        form = SubmitUrl(req.POST)
        context = {
            "title": "Submit URL",
            "form": form
        }
        if form.is_valid():
            current_url = form.cleaned_data.get('url')
            shortened = Url.shortened(url=current_url)
            redirect = Url.redirect(url=current_url)
            context = {
                'title': 'URL Shortened!',
                'redirect': redirect,
                'shortened': shortened
            }

            return render(req, 'home.html', context)
    else:
        form = SubmitUrl()
        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(req, 'shorten/home.html', context)

# def show(req, short_url):
