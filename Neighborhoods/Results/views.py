from django.shortcuts import render
from Ranking.models import MatteModel


def results(request):
    return render(request, 'Results/visualization.html')
#
# def gather_mat():
#     return MatteModel.object.filter(submissions)

