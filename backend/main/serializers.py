from rest_framework import serializers
from .models import Projects, Tasks, Statuses

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ['name']

class TasksSerializer(serializers.ModelSerializer):
    status = StatusSerializer(source='status_id')

    class Meta:
        model = Tasks
        fields = '__all__'

class SpesificTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'