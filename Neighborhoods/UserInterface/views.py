from django.shortcuts import render
from Ranking.models import Themes, MatteModel
def mat_view(request):
    return render(request, 'UserInterface/mats_render.html')

def preferences(request):
    matte_object = MatteModel.objects.filter(title="Maker Space").get()
    card_list = list(matte_object.themes.all())
    min_id_num = 0
    context = {
        'min_id_num':min_id_num,
        'card_list':card_list
    }
    print card_list
    return render(request, 'UserInterface/glidekim.html', context)

