from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Samyuktha! Your Django app is live on Railway!")
