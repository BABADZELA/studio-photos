from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from django.db.models import Q
from .forms import PhotoForm, BlogForm, DeleteBlogForm, FollowUserForm
from .models import Photo, Blog

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo.uploader = request.user
        photo.save()
        return redirect('blog:home')


    return render(request, 'blog/photo_upload.html', context={'form': form})

@login_required
def photo_and_blog_upload(request):
    photo_form = PhotoForm()
    blog_form = BlogForm()

    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        blog_form = BlogForm(request.POST)

        if any([photo_form.is_valid(), blog_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            # champs ManyToMany
            blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
        
            return redirect('blog:home')
        
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
    }

    return render(request, 'blog/blog_post.html', context=context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    edit_form = BlogForm(instance=blog)
    delete_form = DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('blog:home')
            
        if 'delete_blog' in request.POST:
            delete_form = DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('blog:home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_blog.html', context=context)

@login_required
def home(request):
    # photos = Photo.objects.all()
    # blogs = Blog.objects.all()
    """ blogs = Blog.objects.filter(contributors__in=request.user.follows.all())
    photos = Photo.objects.filter(uploader__in=request.user.follows.all()).exclude(blog__in=blogs) """
    # on ne veut voir que les photos publié par les personnes que l'on suit
    blogs = Blog.objects.filter(
        Q(contributors__in=request.user.follows.all()) | Q(starred=True))
    photos = Photo.objects.filter(
        uploader__in=request.user.follows.all()).exclude(
            blog__in=blogs
    )


    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'photos': photos,
    }
    return render(request, 'blog/home.html', context=context)

def create_multiple_photos(request):
    PhotoFormset = formset_factory(PhotoForm, extra=5)
    formset = PhotoFormset()
    if request.method == 'POST':
        for form in formset:
            # permet de vérifier s'il y a des données dans le formulaire
            if form.cleaned_data:
                photo = form.save(commit=False)
                photo.uploader = request.user
                photo.save()
        return redirect('blog:home')
    return render(request, 'blog/create_multiple_photos.html', context={'formset': formset})


def follow_users(request):
    form = FollowUserForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})