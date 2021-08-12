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
