from django.shortcuts import render

def upload_view(request):
    return render(request, 'AdminUpload/upload_view.html')
