from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,JsonResponse
from .models import Doc
# Create your views here.

class MainView(TemplateView):
    template_name = 'posts/main.html'
    
def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')#burdaki sekil nameden gelir html deki
        Doc.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})
