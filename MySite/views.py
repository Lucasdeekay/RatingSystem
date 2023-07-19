from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from MySite.models import Course, Rating, Student, Ranking


# Create your views here.
class LoginView(View):
    template_name = "mysite/ratelog.html"

    # Create get function
    def get(self, request):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('MySite:dashboard'))
        # Otherwise
        else:
            # load the page with the form
            return render(request, self.template_name)

    # Create post function to process the form on submission
    def post(self, request):
        #  Check if the form is valid
        if request.method == 'POST':
            # Process the input
            username = request.POST['username'].strip()
            password = request.POST['password'].strip()
            # Authenticate the user login details
            user = authenticate(request, username=username, password=password)
            # Check if user exists
            if user is not None:
                # Log in the user
                login(request, user)
                # Redirect to dashboard page
                return HttpResponseRedirect(reverse('MySite:dashboard'))
            # If user does not exist
            else:
                # Create an error message
                messages.error(request, "Invalid login details")
                # Redirect back to the login page
                return HttpResponseRedirect(reverse('MySite:login'))


class ForgotPasswordView(View):
    template_name = "mysite/forgot_password.html"

    # Create get function
    def get(self, request):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('MySite:dashboard'))
        # Otherwise
        else:
            # load the page with the form
            return render(request, self.template_name)

    # Create post function to process the form on submission
    def post(self, request):
        #  Check if the form is valid
        if request.method == 'POST':
            # Process the input
            email = request.POST['email'].strip()

            if not Student.objects.filter(email=email).exists():
                student = Student.objects.get(email=email)
                # Redirect to dashboard page
                return HttpResponseRedirect(reverse('MySite:change_password', arg=(student.user.username,)))
            # If user does not exist
            else:
                # Create an error message
                messages.error(request, "Account does not exist")
                # Redirect back to the login page
                return HttpResponseRedirect(reverse('MySite:forgot_password'))


class ChangePasswordView(View):
    template_name = "mysite/change_password.html"

    def get(self, request, username):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('MySite:dashboard'))
        # Otherwise
        else:
            # load the page with the form
            return render(request, self.template_name)

    def post(self, request, username):
        user = User.objects.get(username=username)
        student = Student.objects.get(user=user)

        # Collect inputs
        password = request.POST.get("password").strip()
        confirm_password = request.POST.get("confirm_password").strip()

        if password == confirm_password:
            student.user.set_password(password)
            student.user.save()
            messages.success(request, "Password update successful")
            return HttpResponseRedirect(reverse("Assignment:login"))
        else:
            messages.error(request, "Password does not match")
            return HttpResponseRedirect(reverse("Assignment:change_password", args=(user.username,)))


class RegisterView(View):

    def post(self, request):
        # Check if form is submitting
        if request.method == "POST":
            # Collect inputs
            last_name = request.POST.get("last_name").strip().upper()
            first_name = request.POST.get("first_name").strip().upper()
            matric_no = request.POST.get("matric_no").strip()
            email = request.POST.get("email").strip()
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            # Check if user with username already exists
            if not User.objects.filter(username=matric_no).exists():
                if password == confirm_password:
                    # Create user and person
                    user = User.objects.create_user(username=matric_no, password=password)
                    Student.objects.create(user=user, last_name=last_name, first_name=first_name, matric_no=matric_no,
                                           email=email)
                    # Send success message
                    messages.success(request, "Registration successful. Please login")
                    # Redirect to login page
                    return HttpResponseRedirect(reverse("MySite:login"))
                else:
                    # Send error message
                    messages.error(request, "Password does not match")
                    # Redirect back to register page
                    return HttpResponseRedirect(reverse("MySite:login"))
            else:
                # Send error message
                messages.error(request, "Username already exists")
                # Redirect back to register page
                return HttpResponseRedirect(reverse("MySite:login"))


class RankingView(View):
    template_name = "mysite/ratingscalc.html"

    def get(self, request):
        rankings = Ranking.objects.all().order_by("-points")
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return render(request, self.template_name, {"current_user": request.user, "rankings": rankings})
        # Otherwise
        else:
            # load the page with the form
            return render(request, self.template_name, {"rankings": rankings})


class DashboardView(View):
    template_name = "mysite/ratemain.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        student = Student.objects.get(user=request.user)
        # Check if form is submitting
        if request.method == "POST":
            # Collect inputs
            course_code = request.POST.get("course_code").strip()
            mode_of_teaching = request.POST.get("mode_of_teaching")
            communication = request.POST.get("communication")
            relationship = request.POST.get("relationship")
            comment = request.POST.get("comment")

            if Course.objects.filter(code__icontains=course_code).exists():
                course = Course.objects.get(code__icontains=course_code)
                Rating.objects.create(course=course, student=student, mode_of_teaching=mode_of_teaching,
                                      communication=communication, relationship=relationship, comment=comment)
                messages.success(request, "Rating successfully completed")
                return HttpResponseRedirect(reverse('MySite:dashboard'))
            else:
                messages.success(request, "Course does not exist")
                return HttpResponseRedirect(reverse('MySite:dashboard'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('MySite:dashboard'))
