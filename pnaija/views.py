from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from .models import UserProfile, Feedback
from .ratecal import dailyRate, rate

from .task import send_email

user = get_user_model()


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def report(request):
  return render(request, 'report.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            meterid = form.cleaned_data.get('meterid')
            location = form.cleaned_data.get('location')
            office = form.cleaned_data.get('office')

            new_user = User.objects.create_user(username, email, password)
            new_user.save()

            new_profile = UserProfile.objects.create(user=new_user, meterid=meterid, location=location, office=office)
            new_profile.save()

            user = authenticate(request, username=username, password=password)

            login(request, user)
            # send_email(user.id)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                "form": RegistrationForm,
                "errors": form.errors
            }
            return render(request, 'signup.html', context)
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})
    # return render(request, "success.html", context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context['error'] = "Provide valid credentuals"
            return render(request, "login.html")
    else:
        return render(request, "login.html", context)


def feedback(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    title = request.POST['title']
    content = request.POST['content']

    feedback = Feedback.objects.create(name=name, email=email, title=title, content=content)

    return render(request, "report.html")
  else:
    return render(request, "report.html")


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                "user": "Welcome quest",
                "error": "Invalid username or password",
            }
            return render(request, "login.html", context)
    else:

        context = {
            "user": "Welcome quest",
            "error": "",
        }
        return render(request, "login.html", context)

@login_required
def profile(request):

  profile = UserProfile.objects.get(user=request.user)
    
  context = {
      "profile": profile,
      "rate": rate(),
      "dailyUsage": dailyRate()
    }
  return render(request, "profile.html", context)


def list_reports(request):
  qs = Feedback.objects.all()
  context = {
    'reports': qs
  }
  return render(request, 'list_reports.html', context)

