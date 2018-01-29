from django.shortcuts import render


def task(request):
    return render(request, 'task/empty_page.html')
