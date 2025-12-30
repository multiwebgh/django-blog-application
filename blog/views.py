from django.shortcuts import render, get_object_or_404 , redirect
from django.views.generic import ListView,CreateView,DetailView,DeleteView,TemplateView
from .models import Blog
from blog.forms import CreateBlogForm,CommentForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def BlogListFunc(request):
    blog_list = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blog_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'blog_list': page_obj.object_list,
    }
    return render(request, 'blog/index.html', context)


def BlogDetailsFunc(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    comments = blog.comments.all()


# Handle comment form submission
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('details_link', slug=blog.slug)

  
    context={
        'blog': blog,
        'form': form,
        'comments': comments,
    }


    return render(request, "blog/blog_detail.html",context)

def CreatePostFunc(request):

       if request.method == "POST":
           form = CreateBlogForm(request.POST, request.FILES)
           if form.is_valid():
              blog =  form.save(commit=False)
              blog.author = request.user 
               # Generate slug from title
              base_slug = slugify(blog.title)
              slug = base_slug
              count = 1

            # Ensure slug is unique
              while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

              blog.slug = slug
              blog.save()
              return redirect('details_link', slug=blog.slug)

       else:

            form = CreateBlogForm()     
            context={
            "form":form,
       }
       return render(request, "blog/create_post.html",context)



@login_required
def MyPostsFunc(request):
    my_posts = Blog.objects.filter(author=request.user).order_by('-created_at')
    paginator = Paginator(my_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "blogs": page_obj.object_list,
    }
    return render(request, "blog/my_posts.html", context)

def like_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    user = request.user
    if user in blog.like.all():
        blog.like.remove(user)
    
    else:
        blog.like.add(user)
    return redirect('details_link', slug=blog.slug)