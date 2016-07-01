from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from forms import AuthenticateForm, UserCreateForm, thoughtform
#from .forms import PostForm
#from models import thought, UserProfile

def search_form(request):
    return render(request, 'post_form.html')

def search(request):
    if 'q' in request.POST:
        message = 'You posted %r' %str(request.POST['q'])
    else:
        message = 'You posted nothing'
    return HttpResponse(message)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
              'form': form,
    })

    #else:
        # User is not logged in
        # auth_form = auth_form or AuthenticateForm()
        #user_form = user_form or UserCreateForm()
        
        #return render(request,
                #'ThoughtScape.html',
                            #{'auth_form': auth_form, 'user_form': user_form, })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

def clean_username(self):
    # Since User.username is unique, this check is redundant,
    # but it sets a nicer error message than the ORM. See #13147.
    username = self.cleaned_data["username"]
    try:
        User._default_manager.get(username=username)
    except User.DoesNotExist:
        return username
    raise forms.ValidationError(
                                self.error_messages['duplicate_username'],
                                code='duplicate_username',
                                )

def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError(
                                    self.error_messages['password_mismatch'],
                                    code='password_mismatch',
                                    )
    return password2

def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
        user.save()
        
        userProfile = DoctorSeeker(user=user, name=name, email=email)
        userProfile.save()
    
    return user


def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')


# Create your views here.
def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        thought_form = thoughtform()
        user = request.user
        thoughts_self = thought.objects.filter(user=user.id)
        thoughts_buddies = thought.objects.filter(user__userprofile__in=User.profile.follows.all)
        thoughts = thoughts_self | thoughts_buddies
        thoughts = thoughts_self
        
        return render(request,
                      'ThoughtScape.html',
                      {'thought_form': thought_form, 'user': user,
                      'thoughts': thoughts,
                      'next_url': '/', })

#def new_post(request):
    form = PostForm()
    return render(request, 'frontpage.html', {'form':form})