from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from student.forms import (
    StudentProfileForm,
    StudentSkillForm,
    ProjectForm,
    CertificateForm
)
from student.models import (
    Student,
    StudentSkill,
    Project,
    Certificate
)
from .forms import RegisterForm


def home(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Student.objects.create(
                user=user,
                full_name=user.username,
                email=user.email
            )

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):

    student = Student.objects.get(
        user=request.user
    )

    skill_count = StudentSkill.objects.filter(
        student=student
    ).count()

    project_count = Project.objects.filter(
        student=student
    ).count()

    certificate_count = Certificate.objects.filter(
        student=student
    ).count()

    total_profile_fields = 5

    completed_fields = 0

    if student.full_name:
        completed_fields += 1

    if student.email:
        completed_fields += 1

    if student.phone:
        completed_fields += 1

    if student.college:
        completed_fields += 1

    if student.course:
        completed_fields += 1

    profile_completion = int(
        (completed_fields / total_profile_fields) * 100
    )

    return render(
        request,
        'accounts/dashboard.html',
        {
            'student': student,
            'skill_count': skill_count,
            'project_count': project_count,
            'certificate_count': certificate_count,
            'profile_completion': profile_completion,
        }
    )
@login_required
def profile(request):

    student = Student.objects.get(user=request.user)

    if request.method == 'POST':

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect('profile')

    else:

        form = StudentProfileForm(
            instance=student
        )

    return render(
        request,
        'accounts/profile.html',
        {'form': form, 'student': student}
    )
@login_required
def my_skills(request):

    student = Student.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = StudentSkillForm(request.POST)

        if form.is_valid():

            student_skill = form.save(commit=False)

            student_skill.student = student

            student_skill.save()

            messages.success(
                request,
                "Skill added successfully."
            )

            return redirect('my_skills')

    else:

        form = StudentSkillForm()

    skills = StudentSkill.objects.filter(
        student=student
    )

    return render(
        request,
        'accounts/my_skills.html',
        {
            'form': form,
            'skills': skills
        }
    )
@login_required
def projects(request):

    student = Student.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            project = form.save(commit=False)

            project.student = student

            project.save()

            messages.success(
                request,
                "Project added successfully."
            )

            return redirect('projects')

    else:

        form = ProjectForm()

    project_list = Project.objects.filter(
        student=student
    ).order_by('-created_at')

    return render(
        request,
        'accounts/projects.html',
        {
            'form': form,
            'projects': project_list
        }
    )
@login_required
def certificates(request):

    student = Student.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = CertificateForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            certificate = form.save(commit=False)

            certificate.student = student

            certificate.save()

            messages.success(
                request,
                "Certificate added successfully."
            )

            return redirect('certificates')

    else:

        form = CertificateForm()

    certificate_list = Certificate.objects.filter(
        student=student
    )

    return render(
        request,
        'accounts/certificates.html',
        {
            'form': form,
            'certificates': certificate_list
        }
    )
def logout_view(request):

    logout(request)

    return redirect('home')
@login_required
def delete_account(request):

    if request.method == "POST":
        user = request.user

        logout(request)
        user.delete()

        return redirect("home")

    return render(
        request,
        "accounts/delete_account.html"
    )