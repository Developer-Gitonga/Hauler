from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# app imports
from .forms import *
from .models import Posts, UserProfile
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'haul/home.html')
        # return HttpResponse('Hello World!')


# user register view
class RegisterView(View):
    """This class view is used to render the register page and execute user registrations."""
    form = CreateUserForm()
    ctx = {
        'title': 'Register',
        'form': form,
    }

    def get(self, request):
        return render(request, 'haul/register.html', self.ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateUserForm()  # reset form
            messages.success(request, 'Registered successfully.')
            return redirect(reverse('login'))
        messages.error(request, 'Registration failed.')
        context = {
            form: form,
        }
        return render(request, 'haul/register.html', context)


# user login view
class LoginView(View):
    context = {
        'title': 'Login'
    }

    def get(self, request):
        return render(request, 'haul/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Invalid username or password.')

        return render(request, 'haul/login.html', self.context)


# logout view
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect("home")


# profile design
@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    # prepolate the form with the user's data
    user_form = UserForm(instance=user)

    ProfileInlineFormSet = inlineformset_factory(
        User, UserProfile, fields=('bio', 'phone', 'picture'), extra=0)
    formset = ProfileInlineFormSet(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == 'POST':
            user_form = UserForm(
                request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormSet(
                request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormSet(
                    request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/profile/')

        return render(request, 'haul/edit_profile.html', {
            "pk": pk,
            "user_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    """this class view is used to render the profile page and execute user profile updates."""

    def get(self, request):
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)
        context = {
            'title': 'Profile',
            'user_data': user,
            'profile_data': profile,

        }
        return render(request, 'haul/profile.html', context)


# creating of posts and viewing posts
@login_required(login_url='/create_posts/')
def create_post(request):

    if request.method == 'POST':
        current_user = request.user
        title = request.POST['title']
        description = request.POST['description']

        post = Posts(
            user=current_user,
            title=title,
            description=description
        )
        post.create_post()

        return redirect('posts')


def Posted(request):

    posts = Posts.objects.all()

    ctx = posts

    return render(request, 'haul/posts.html', {"posts": posts})
