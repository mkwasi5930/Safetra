from django.shortcuts import render,redirect,HttpResponse

from safiri.models import PostCar
from .forms import LetCarForm, SelfDriveForm, TaxCabForm

# Create your views here.

def Home(request):
    context={

    }
    return render(request,'index.html',context)

def SelfDrive(request):
    postcar = PostCar.objects.all()
    context = {
        'postcars':postcar
    }
    if request.method == 'POST':
        form = SelfDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')
    else:
      form = SelfDriveForm()
    return render(request, 'udrive.html', {'form': form})

def LetCar(request):
    if request.method == 'POST':
        form = LetCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')
    else:
      form = LetCarForm()
    return render(request, 'sublet.html', {'form': form})

def TaxCab(request):
    if request.method == 'POST':
        form = TaxCabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks')
    else:
      form = TaxCabForm()
    return render(request, 'taxcab.html', {'form': form})
def About(request):
    context={}
    return render(request,'about.html',context)



def thanksPage(request):
    return HttpResponse("Thanks received. We will reach you shortly.")