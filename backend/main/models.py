from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    estimated_time = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Statuses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Tasks(models.Model):
    name = models.CharField(max_length=255)
    time = models.PositiveIntegerField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)  
    status_id = models.ForeignKey(Statuses, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Tasks)
def update_project_estimated_time(sender, instance, **kwargs):
    project = instance.project_id
    tasks_time = Tasks.objects.filter(project_id=project).aggregate(total_time=models.Sum('time'))['total_time'] or 0
    project.estimated_time = tasks_time
    project.save()