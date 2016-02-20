from django.shortcuts import render

def results(request):
    return render(request, 'Results/visualization.html')

def gather_mat():
    return MattModel.object.filter(submissions)

