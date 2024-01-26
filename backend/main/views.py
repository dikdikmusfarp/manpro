from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Projects, Tasks, Statuses
from .serializers import ProjectsSerializer, TasksSerializer, StatusSerializer, SpesificTasksSerializer, AllStatusSerializer

class ProjectsListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class StatusListView(generics.ListAPIView):
    queryset = Statuses.objects.all()
    serializer_class = AllStatusSerializer

class TasksListCreateView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = SpesificTasksSerializer

class TasksUpdateView(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = SpesificTasksSerializer

class TasksDetailView(generics.RetrieveDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class ProjectTasksView(generics.ListAPIView):
    serializer_class = TasksSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Tasks.objects.filter(project_id=project_id).select_related('status_id')

class ProjectTasksView(generics.ListCreateAPIView):
    serializer_class = TasksSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Tasks.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        serializer.save(project_id=project_id)

    def perform_update(self, serializer):
        serializer.save()
        project_id = self.kwargs['project_id']
        update_project_estimated_time(project_id)