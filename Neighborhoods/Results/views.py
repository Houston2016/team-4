from django.shortcuts import render

def results(request):
    return render(request, 'Results/visualization.html')

