from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.models import Teacher, Student, Assignment, Material
from django.urls import reverse_lazy
from core.forms import TeacherForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_index.html'
    context_object_name = 'teachers'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = context['page_obj']  # Now 'teachers' is the Page object
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher.index')

class TeacherDeleteView(DeleteView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'teachers/teacher_delete_confirm.html'
    success_url = reverse_lazy('teacher.index')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_index.html'
    context_object_name = 'students'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student.index')

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['full_name', 'email', 'semester', 'phone_no', 'user']
    success_url = reverse_lazy('student.index')

class StudentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_delete_confirm.html'
    success_url = reverse_lazy('student.index')