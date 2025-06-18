from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.models import Teacher, Student, Assignment, Material
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'
    paginate_by = 5

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['full_name', 'email', 'department', 'phone_no', 'join_date', 'user']
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/teacher_form.html'
    fields = ['full_name', 'department', 'phone_no', 'join_date']
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(DeleteView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_delete_confirm.html'
    success_url = reverse_lazy('teacher.index')
