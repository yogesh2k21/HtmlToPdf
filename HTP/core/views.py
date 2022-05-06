from multiprocessing import context
from django.shortcuts import render
from .render import Render


# Create your views here.
def home(request):
    return render(request,'home.html')

def gen(request):
    context={
        'Name':'Yogesh',
        'Age':'21',
        'Branch':'CSE'
    }
    return Render.render('gen.html',context)