from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

from .forms import RegistrationForm
from blog.models import Post
from events.models import Event


def goToMemberRegister(request):
    return render(request, 'members/main/members.html')


def memberRegisterConfirmation(request):
    return render(request, 'members/main/confirm-member-account-created.html')


@login_required(login_url='/login')
@permission_required('blog.delete_post', login_url='/login',
                     raise_exception=True)
def memberDashboard(request):
    posts = Post.objects.all().order_by("-date")
    events = Event.objects.all().order_by("-date")

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.get(id=post_id)
        if post and (post.user == request.user or request.user.has_perm(
                'blog.delete_post')):
            post.delete()

    return render(request, 'members/main/dashboard.html',
                  {'posts': posts, 'events': events})


def signUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)

            default_group = Group.objects.get(name='default')
            user.groups.add(default_group)

            return redirect('confirm-member-account-created')

    else:
        form = RegistrationForm()

    return render(request, 'registration/sign-up.html', {'form': form})


@login_required(login_url='/login')
def deleteMemberAccount(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('homepage')
    else:
        return render(request, 'members/main/delete-member-account.html')
