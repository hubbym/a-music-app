from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import AlbumForm,UserForm
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    
        
    return render(request,"music/index.html" , context)
@unauthenticated_user
def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account was created for ' + user)
            return redirect('/music/login')
    context = {'form' : form}   
    return render(request,"music/register.html" , context) 

    
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/music')
        else:
            messages.info(request,"username password combination is wrong")

    context = {}   
    return render(request,"music/login.html" , context)   

def logoutUser(request):
    logout(request,)
    return redirect('/music/login')

def detail(request,album_id):
    '''try:
        album = Album.objects.get(pk = album_id)
        context = {'album': album }
    except:
        raise Http404("Album does not exist")'''
    album = get_object_or_404(Album, pk = album_id) 
    context = {'album': album }        
    return render(request,"music/detail.html",context )


def favorite (request,album_id):
    album = get_object_or_404(Album, pk = album_id)
    try :
        selected_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
            'album' : album,
            'error_message' : 'you did not select a valid song' ,
        })    
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,"music/detail.html",{'album' : album} )

def addAlbum(request):
    form = AlbumForm()
    if request.method == "POST":
        #print('printing post : ', request.POST)
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/music')
    context = {'form' : form}
    return render(request,'music/createAlbum.html' , context)

def updateAlbum(request,album_id):
    album = Album.objects.get(id = album_id)
    form = AlbumForm(instance= album)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect('/music')
    context = {'form' : form}
    return render(request,'music/createAlbum.html' , context)

def deleteAlbum(request,album_id):
    album = Album.objects.get(id = album_id)
    album.delete()
    return redirect('/music')
