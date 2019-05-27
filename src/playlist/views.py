import pytube

from django.shortcuts import render

# Create your views here.

from .forms import getlink,downlink
from .models import videolink

def download(request):
    context = {}

    template = "playlist/home.html"
    form = getlink(request.POST or None)
    if form.is_valid():

        print(form.cleaned_data)
        link = form.cleaned_data.get('link')
        yt =  pytube.YouTube(link)
        videos = yt.streams.all()

        template = "playlist/success.html"
        context = {
            "link":link,
            "videos":videos,
        }
        #message = ""

    return render(request,template,context)

def success(request):
    form = downlink(request.POST or None)
    context = {}
    message = "An error occured!!"
    template = "playlist/down.html"

    if form.is_valid():
        print(form.cleaned_data)
        yt = pytube.YouTube(form.cleaned_data.get('link'))
        v = yt.streams.all()
        vid = form.cleaned_data.get('quality')
        print(vid)
        # i = 0
        # while(1):
        #     if(str(v[i])==vid):
        #         break
        #     i +=1
        message = "Your Video is successfully downloading!!"
        v[vid-1].download()
    context = {
        "message": message,
    }
    return render(request,template,context)


