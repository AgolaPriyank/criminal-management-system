from django.shortcuts import render, get_object_or_404, redirect
from .models import Criminal
from .forms import CriminalForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
def criminal_list(request):
    query = request.GET.get('q')
    if query:
        criminals = Criminal.objects.filter(Q(id__icontains=query))
    else:
        criminals = Criminal.objects.all()
    return render(request, 'criminals/criminal_list.html', {'criminals': criminals})

# @login_required
# def criminal_list(request):
#     query = request.GET.get('q')
#     if query:
#         # Enhanced search for ID, name, or Aadhaar number
#         criminals = Criminal.objects.filter(
#             Q(id__icontains=query) |
#             Q(name__icontains=query) |
#             Q(aadhaarNumber__icontains=query)
#         )
#     else:
#         criminals = Criminal.objects.all()
#     return render(request, 'criminals/criminal_list.html', {'criminals': criminals})

def criminal_detail(request, pk):
    criminal = get_object_or_404(Criminal, pk=pk)
    return render(request, 'criminals/criminal_detail.html', {'criminal': criminal})

@login_required
def criminal_create(request):
    if request.method == "POST":
        form = CriminalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('criminal_list')
    else:
        form = CriminalForm()
    return render(request, 'criminals/criminal_form.html', {'form': form})

@login_required
def criminal_update(request, pk):
    criminal = get_object_or_404(Criminal, pk=pk)
    if request.method == "POST":
        form = CriminalForm(request.POST, request.FILES, instance=criminal)
        if form.is_valid():
            form.save()
            return redirect('criminal_list')
    else:
        form = CriminalForm(instance=criminal)
    return render(request, 'criminals/criminal_form.html', {'form': form})



@login_required
def criminal_delete(request, pk):
    criminal = get_object_or_404(Criminal, pk=pk)
    if request.method == "POST":
        criminal.delete()
        return redirect('criminal_list')
    return render(request, 'criminals/criminal_confirm_delete.html', {'criminal': criminal})
