from django.http import HttpResponse

def index(request):
    return HttpResponse("Is this thing on?")
