from django.shortcuts import render
from django.http import HttpResponse
from .models import Content
from .models import Member
from .models import Service
from .models import Work

def index(request):
    context ={
        'content': Content.objects.last(),
        'members': Member.objects.order_by('name'),
        'services': Service.objects.order_by('name'),
        'works': Work.objects.order_by('name'),
    }
    return render(request, 'home/index.html', context)
