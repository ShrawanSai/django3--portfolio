from django.shortcuts import render, get_object_or_404
from .models import Project, Skill


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    x = len(skills)
    skills1 = skills[:x//2]
    skills2 = skills[x//2:]
    return render(request, 'homepage/home.html',{'projects':projects, 'skills1':skills1, 'skills2':skills2})

def project_detail(request,proj_id):
    proj = get_object_or_404(Project,pk = proj_id)
    return render(request, 'homepage/projects_detail.html',{'proj':proj})
