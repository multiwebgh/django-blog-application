from urllib import request
from django.shortcuts import render,redirect
from authentication.forms import RegisterForm,UserProfileForm,UpdateProfile
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from authentication.models import UserProfile


# Register Function.
def RegisterFunc(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_link")
            
    else:

        form = RegisterForm()
    context={
            "form":form
        }        

    return render(request, "auth/register.html",context)    



def LoginFunc(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_link")
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "auth/login.html", context)



def LogoutFunc(request):
    logout(request)
    return redirect("home_link")



def ProfileFunc(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    
    context = {
        "profile": profile
    }
    
    return render(request, "auth/profile.html",context)


def UpdateImageFunc(request):

      if request.method == "POST":
          form = UserProfileForm(request.POST , request.FILES, instance=request.user.userprofile)
          if form.is_valid():
             form.save()
             return redirect("profile_link")

      else:
            form = UserProfileForm(instance=request.user.userprofile)

      context = {
        "form": form
    }
      return render(request, "auth/update_image.html", context)


def AddProfileFunc(request):
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST , request.FILES)
        if form.is_valid():
           profileInfo =  form.save(commit=False)
           profileInfo.user = request.user 
           profileInfo.save()
           return redirect("profile_link")
    context={
        "form":form
    }        
    
    return render(request, "auth/add_profile.html",context)


def UpdateProfileFunc(request):
    if request.method == "POST":
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile_link")
    else:
        form = UpdateProfile(instance=request.user)
    return render(request, "auth/update_profile.html", {"form": form})