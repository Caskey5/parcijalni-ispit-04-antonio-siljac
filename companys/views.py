from django.shortcuts import get_object_or_404, redirect, render

from companys.forms import CompanysForm

from .models import Companys

# Create your views here.


def companys_list(request):
    companys = Companys.objects.all()
    return render(request, 'companys/companys_list.html', {'companys': companys})


def companys_create(request):
    form = CompanysForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('companys_list')
    return render(request, 'companys/companys_form.html', {'form': form})


def companys_update(request, pk):
    customer = get_object_or_404(Companys, pk=pk)
    form = CompanysForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('companys_list')
    return render(request, 'companys/companys_form.html', {'form': form})