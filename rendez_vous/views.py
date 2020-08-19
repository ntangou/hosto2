from django.shortcuts import render, redirect
from .forms import RdvForm
from rendez_vous.models import Rdv, Heure
#from django.views.decorators.cache import cache_page

#from rendez_vous.models import Rdv, Siteweb

# Create your views here.

def qrcode(request, id):
    obj = Rdv.objects.get(id=id)
    context = {
        'obj' : obj,
    }
    return render(request, 'rendez_vous/qrcode.html', context)


#@cache_page(60 * 15)
def rdv(request):
    
    if request.method == "POST":
        form = RdvForm(request.POST)
        if form.is_valid():
            rdv = form.save() 
            return redirect('qrcodeindex', id=rdv.id)
    else:
        form = RdvForm()

    return render(request, 'rendez_vous/rdv.html', {'form': form})


