from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post, City, Profile
from .forms import PostForm, ProfileForm
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def profile(request):
  posts = Post.objects.all()
  profile = Profile.objects.get(user=request.user)
  profile_form = ProfileForm(instance=profile)
  return render(request, 'posts/index.html', { 
    'posts': posts, 
    'profile_form': profile_form
    })

def post_show(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/show.html', { 'post': post })

def post_new(request):
  post_form = PostForm(request.POST or None)
  if request.POST and post_form.is_valid():
    new_post = post_form.save(commit=False)
    new_post.user = request.user
    new_post.city_id = request.POST['cityId']
    new_post.save()
    return redirect('profile')
  else:
    return render(request, 'posts/new.html', { 'post_form': post_form })

def cities_index(request):
  return render(request, 'cities/index.html')

def city_show(request, city_id):
  post_form = PostForm(request.POST or None)
  city = City.objects.get(id=city_id)
  return render(request, 'cities/show.html', { 
    'city': city,
    'post_form': post_form
    })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      profile = Profile(first_name = request.POST['first_name'], last_name = request.POST['last_name'], current_city = request.POST['current_city'], user = request.user )
      profile.save()
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def profile_edit(request):
  profile = Profile.objects.get(user=request.user)
  profile_form = ProfileForm(request.POST or None, instance=profile)
  if request.POST and profile_form.is_valid():
    profile_form.save()
    return redirect('profile')
  else:
    return HttpResponse('invalid edit')
    