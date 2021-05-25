from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . models import Song
# Create your views here.
# def index(request):
    # return render(request,"index.html")

def index(request):
    # user = User.objects.create_user(username='rawat', email='lennon@thebeatles.com', password='johnpassword')
    sng=Song.objects.all()
    
    return render(request,"index.html",{"sng":sng})

def add(request):
    if request.method=="POST":
        
        name=request.POST.get("name")
        language=request.POST.get("language")
        singer=request.POST.get("singer")
        sng=Song(name=name,language=language,singer=singer).save()
        return redirect("/")
        
        
    return render(request,"add.html")

def delete(request,id):
    if request.method=="POST":   
        sng=Song.objects.filter(id=id)
        sng.delete()
        return redirect("/")
    else:
         for_id=Song.objects.filter(id=id)
         sng=Song.objects.all()
         for i in for_id:
             del_id=i.id
             del_song=i.name
         
         return render(request,"index.html",{"value":"okay","sng":sng,"del_id":del_id,"del_song":del_song})

def edit(request,id):
    sng=Song.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        language=request.POST.get("language")
        singer=request.POST.get("singer")
        sng=Song(name=name,language=language,singer=singer,id=id).save()
        return redirect("/")
    else:    
        return render(request,"edit.html",{"sng":sng})
    
       
def del_selected(request):   
    if request.method=="POST":
            checked_values = request.POST.getlist('checks')
            for i in checked_values:
              sng=Song.objects.filter(id=i).delete()
              print(checked_values)
    return redirect("/")

def search(request):
    query=request.GET.get("search")
    song_search=Song.objects.filter(name__icontains=query)
    for i in song_search:
        print(i.name)
    return render(request,"index.html",{"sng":song_search})