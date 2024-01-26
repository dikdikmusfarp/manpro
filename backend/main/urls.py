from django.urls import path
from .views import ProjectsListCreateView, ProjectsDetailView, TasksListCreateView, TasksDetailView, ProjectTasksView, StatusListView, TasksUpdateView

urlpatterns = [
    path('projects/', ProjectsListCreateView.as_view(), name='projects-list-api'),
    path('projects/', ProjectsListCreateView.as_view(), name='projects-list-create'),
    path('projects/<int:pk>/', ProjectsDetailView.as_view(), name='projects-detail'),
    path('projects/<int:pk>/update/', ProjectsDetailView.as_view(), name='projects-update'),
    path('projects/<int:pk>/delete/', ProjectsDetailView.as_view(), name='projects-delete'),
    path('tasks/', TasksListCreateView.as_view(), name='tasks-create'),
    path('tasks/', TasksDetailView.as_view(), name='tasks-list-api'),
    path('tasks/<int:pk>/', TasksDetailView.as_view(), name='tasks-detail'),
    path('tasks/<int:pk>/update/', TasksUpdateView.as_view(), name='tasks-update'),
    path('tasks/<int:pk>/delete/', TasksDetailView.as_view(), name='tasks-delete'),
    path('projects/<int:project_id>/tasks/', ProjectTasksView.as_view(), name='project-tasks'),
    path('statuses/', StatusListView.as_view(), name='status-list-api'),

]