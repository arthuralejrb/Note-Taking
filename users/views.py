from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def logout_view(request):
    """Log out user"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Register user"""
    if request.method != 'POST':
        # Shows blank register form
        form = UserCreationForm()
        
    else:
        # process form
        form = UserCreationForm(a=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            
            # Log in user and redirect to home page 
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, '/home/balmaceda/appWebPython/users/templates/registration/register.html', context)



