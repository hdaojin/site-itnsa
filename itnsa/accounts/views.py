from django.shortcuts import render, redirect

# Create your views here.

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'heading': '用户注册'})
