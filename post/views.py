from post.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, redirect,render
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .forms import UserForm
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

def index(request):
    return render_to_response('post/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('post/view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('post/view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })





class UserFormView(View):
    form_class = UserForm
    template_name = 'post/registrations.html'

    def get(self,request):

        form = self.form_class(None)
        return render(request,self.template_name, {'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if self.form_class(request.POST).is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user.is_active:
                    login(request, user)


            return redirect('view_posts')

