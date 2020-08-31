from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, CVEntry
from .forms import PostForm, CVForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv_page(request):
    entries = CVEntry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/cv_page.html', {'entries': entries})

def cv_detail(request, pk):
    entry = get_object_or_404(CVEntry, pk=pk)
    return render(request, 'blog/cv_detail.html', {'entry': entry})

def cv_edit(request, pk):
    entry = get_object_or_404(CVEntry, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect('cv_page')
    else:
        form = CVForm(instance=entry)
    return render(request, 'blog/cv_edit.html', {'form': form})

def cv_new(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect('cv_detail', pk=entry.pk)
    else:
        form = CVForm()
    return render(request, 'blog/cv_edit.html', {'form': form})