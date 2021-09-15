from django.shortcuts import render
from .models import Profile, Work, Skill


def index(request):
    profile = Profile.objects.all().last()
    skills = Skill.objects.all()
    works = Work.objects.all().order_by('-published')
    context = {
        'profile': profile,
        'skills': skills,
        'works': works,
    }
    return render(request, 'portfolio.html', context)


def airbnb1index(request):
    return render(request, 'airbnb1.html')


def airbnb2index(request):
    return render(request, 'airbnb2.html')
