from django.http import HttpResponse


def hellow(request):
    return HttpResponse('hellow world')