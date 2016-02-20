from django.shortcuts import render

def mat_view(request):
    return render(request, 'UserInterface/mats_view.html')

def preferences(request):
    return render(request, 'UserInterface/drag_and_drop.html')

