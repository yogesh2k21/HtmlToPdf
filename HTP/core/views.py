from multiprocessing import context
from django.shortcuts import render
from .render import Render
from qrcode import make

data=None
# Create your views here.
#when i click on downlaod than run this function
def home(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        # file_name=
        img.save(f"media/{data}.png")
    else:
        data=""
    return render(request,"home.html",{'data':data})

def gen(request):
    context={
        'Name':'Yogesh',
        'Age':'21',
        'Branch':'CSE'
    }
    return Render.render('gen.html',context)