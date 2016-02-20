from django.shortcuts import render

def results(request):
    return render(request, 'Results/visualization.html')

def gather_mats(event_id):
    return MattModel.object.filter(id=event_id)

