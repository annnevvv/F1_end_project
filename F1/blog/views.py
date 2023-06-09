from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout

from .models import Post
from .forms import CommentForm, PostCreatedForm

# Create your views here.

all_posts = Post.objects.all().order_by('-date')


class BlogMainPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


class SinglePostView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_post')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(
                reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }

        return render(request, 'blog/post-detail.html', context)


class PostsStorageView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/storage-for-post.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        post_id = int(request.POST['post_id'])

        if stored_posts is None:
            stored_posts = []

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect("/blog")


@login_required(login_url='/login')
@permission_required("blog.add_post", login_url='/dashboard',
                     raise_exception=True)
def createPost(request):
    if request.method == 'POST':
        form = PostCreatedForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('create_post_confirmation')
    else:
        form = PostCreatedForm()

    return render(request, 'blog/create-post.html', {'form': form})


def postCreatedConfirmation(request):
    return render(request, 'blog/post-create-confirmation.html')
