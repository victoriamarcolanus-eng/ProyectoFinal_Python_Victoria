from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post

def inicio(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")

def listar_posts(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        posts = Post.objects.filter(titulo__icontains=busqueda)
    else:
        posts = Post.objects.all()
    return render(request, "blog/pages.html", {"posts": posts})

def detalle_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

# Vista para crear un post (Usa LoginRequiredMixin para que solo logueados entren)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor']
    success_url = reverse_lazy('pages')

# Vista para borrar un post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('pages')
