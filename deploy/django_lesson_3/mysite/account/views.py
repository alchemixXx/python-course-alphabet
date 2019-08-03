from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from .models import Profile
from .forms import UpdateProfileForm


class ProfilesList(ListView):
    model = Profile
    template_name = 'account/all_profiles.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfilesList, self).get_context_data()
        context['page_title'] = 'All profiles list'

        # testing user auth
        if self.request.user.is_authenticated:
            self.nickname = self.request.user.username
            self.id = self.request.user.id
            a = User.objects.get(id=self.id)
            self.profile_id = a.profile.id
        return context


class ProfileDetailView(DetailView):
    template_name = 'account/profile.html'
    model = Profile
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            self.nickname = self.request.user.username
            current_user = User.objects.get(id=self.request.user.id)
            self.profile_id = current_user.profile.id
            context['nickname'] = self.nickname
            context['current_profile_id'] = self.profile_id
        return context


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Create user
        created_user = form.save()
        # Create profile
        profile = Profile.objects.create(user=created_user)
        # Authenticate User
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('profile', profile.id)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'account/update_form.html'
    pk_url_kwarg = 'profile_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            self.nickname = self.request.user.username
            context['nickname'] = self.nickname
        return context

    def get_success_url(self):
        return reverse('profile', args=(self.object.id,))
