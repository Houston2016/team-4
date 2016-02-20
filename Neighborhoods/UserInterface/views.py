from django.shortcuts import render

def mat_view(request):
    return render(request, 'UserInterface/mats_render.html')

def preferences(request):
    card_list = []
    min_id_num = 0
    context = {
        'min_id_num':min_id_num,
        'card_list':card_list
    }
    return render(request, 'UserInterface/glidekim.html', context)

