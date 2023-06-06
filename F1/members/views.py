from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from blog.models import Post


# Create your views here.


def goToMemberRegister(request):
    return render(request, 'members/main/members.html')


def memberRegisterConfirmation(request):
    return render(request, 'members/main/confirm-memeber-account-created.html')


@login_required(login_url='/login')
def memberDashboard(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.get(id=post_id)
        if post and post.user == request.user:
            post.delete()

    return render(request, 'members/main/dashboard.html', {'posts': posts})


def signUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('confirm-memeber-account-created')

    else:
        form = RegistrationForm()

    return render(request, 'registration/sign-up.html', {'form': form})
