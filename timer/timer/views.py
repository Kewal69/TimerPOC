import uuid

from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from app.models import Timer


def index(request):
    return render(request, 'timer/index.html', {})


def start_timer(request):
    msg = "timer called for {} minutes".format(request.POST.get('duration', 10))
    duration = request.POST.get('duration', 10)
    if Timer.objects.count() == 0:
        timer = Timer.objects.create(duration=duration)
    else:
        timer = Timer.objects.first()
    context = {'duration': duration, 'timer': timer}

    return render(request, 'timer/timer_view.html', context)

