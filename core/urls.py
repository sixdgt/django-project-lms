from django.urls import path
from core.views import (
   HomePageView, 
   TeacherCreateView, 
   TeacherListView,
   TeacherDetailView, 
   TeacherDeleteView,
   TeacherUpdateView,
   StudentCreateView,
   StudentListView,
   StudentDetailView,
   StudentDeleteView,
   StudentUpdateView,
   AssignmentListView,
   AssignmentCreateView,
   AssignmentDetailView,
   AssignmentUpdateView,
   AssignmentDeleteView
)

urlpatterns = [
   # path('', views.home, name='home') - function base views loading
   path('', HomePageView.as_view(), name='home'),
   
   # Teacher URLs
   path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
   path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create'),
   path('teacher/<int:pk>/detail/', TeacherDetailView.as_view(), name='teacher.detail'),
   path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher.edit'),
   path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher.delete'),
   
   # Student URLs
   path('student/list/', StudentListView.as_view(), name='student.index'),
   path('student/create/', StudentCreateView.as_view(), name='student.create'),
   path('student/<int:pk>/detail/', StudentDetailView.as_view(), name='student.detail'),
   path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student.edit'),
   path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student.delete'),
   
   # Assignment URLs
   path('assignment/list/', AssignmentListView.as_view(), name='assignment.index'),
   path('assignment/create/', AssignmentCreateView.as_view(), name='assignment.create'),
   path('assignment/<int:pk>/detail/', AssignmentDetailView.as_view(), name='assignment.detail'),
   path('assignment/<int:pk>/edit/', AssignmentUpdateView.as_view(), name='assignment.edit'),
   path('assignment/<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment.delete'),
]