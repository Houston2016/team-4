from django.shortcuts import render
from Ranking.models import MatteModel

def results(request):
    requested_model = MatteModel.objects.filter(title="Maker Space")
    context = {'workspace': requested_model}
    return render(request, 'Results/visualization.html', context)

def gather_mat():
    return MatteModel.objects.all()

