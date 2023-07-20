from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def register_user(request):
    action = "Sign Up"

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('welcome')
    else:
        form = CustomUserCreationForm()

    context = {
        'action': action,
        'form': form,
    }
    return render(request, 'users/login_register.html', context=context)
