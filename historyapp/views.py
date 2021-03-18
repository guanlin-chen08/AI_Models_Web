from django.shortcuts import render, redirect
from historyapp.models import History
from historyapp.models import HistoryImage
from .forms import Insertform
from .forms import UploadModelFrom
from django.http import HttpResponseRedirect
# Create your views here.

def historylist(request):
    # form = Insertform
    #
    # context = {
    #     'form': form
    # }
    # return render(request, 'test.html', context)
    try:
        Historys = History.objects.all().order_by('id')
        form = Insertform()
        if request.method == 'POST':
            form = Insertform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request)
        else:
            form = Insertform()
    except:
        errormessage = "ERROR"
    return render(request, 'historyapi.html', {'form': form})

def index(request):
    photos = HistoryImage.objects.all()

    form = UploadModelFrom()
    if request.method == 'POST':
        form = UploadModelFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'photos': photos,
        'form': form
    }

    return render(request, 'image/index.html', context)

# def insert(request):
#     unit = History.objects.create(bs1='10', bs2='1', bs3='1', bs4='1', bs5='1', bs6='1')
#     unit.save()
#     Historys = History.objects.all().order_by('id')
#     return render(request, 'historyapi.html', locals())
#
#
# def delete(request):
#     unit = History.objects.get(id='10')
#     unit.delete()
#     Historys = History.objects.all().order_by('id')
#     return render(request, 'historyapi.html', locals())
