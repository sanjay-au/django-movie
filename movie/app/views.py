from django.shortcuts import render,redirect
from app.forms import bookform
from app.models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'b':k})


class MovieList(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "b"


# def add(request):
#     if (request.method=="POST"):
#         form=bookform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=bookform()
#     return render(request,'addmovie.html',{'form':form})


class MovieAdd(CreateView):
    model = Movie
    template_name = "addmovie.html"
    fields = '__all__'
    success_url = reverse_lazy('movie:home')


# def detail(request,p):
#     k=Movie.objects.get(id=p)
#     return render(request,'detail.html',{'b':k})


class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail.html'
    context_object_name = 'b'


# def update(request,p):
#     m=Movie.objects.get(id=p)
#     if(request.method=="POST"):
#         form=bookform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=bookform(instance=m)
#     return render(request,'update.html',{'form':form})


class MovieUpdate(UpdateView):
    model = Movie
    template_name = 'update.html'
    fields = "__all__"
    success_url = reverse_lazy('movie:home')


# def delete(request,p):
#     m=Movie.objects.get(id=p)
#     m.delete()
#     return redirect('movie:home')


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:home')
    template_name = 'delete.html'