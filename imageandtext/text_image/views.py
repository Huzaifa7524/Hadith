from django.shortcuts import render, redirect
from .forms import hadithsForm, tatorialForm
from .models import hadithsModel, tatorial


# Create your views here.
def home(request):
    tatorial_data = tatorial.objects.all()
    print(tatorial_data)
    return render(request, 'base.html', {'data': tatorial_data})

# upload the data to the database
def tatorial_video(request):
    if request.method == 'POST':
        form = tatorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = tatorialForm()
    return render(request, 'tatorial.html', {'form': form})

def hadiths(request):
    if request.method == 'POST':
        form = hadithsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('haidth')
    else:
        form = hadithsForm()
    return render(request, 'hadiths.html', {'form': form})

# get all the data from the database
def Mishkat(request):
    hadiths_data = hadithsModel.objects.all()
    print(hadiths_data)
    return render(request, 'mishkat-ul.html', {'data': hadiths_data})