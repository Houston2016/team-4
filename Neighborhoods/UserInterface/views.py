from django.shortcuts import render

def mat_view(request):
    return render(request, 'UserInterface/mats_render.html')

def preferences(request,id):
    return render(id, request, 'UserInterface/drag_and_drop.html')

