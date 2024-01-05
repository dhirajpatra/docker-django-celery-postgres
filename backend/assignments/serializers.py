from rest_framework import serializers
from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('id', 'first_term', 'second_term', 'sum')
        read_only_fields = ['id', 'sum']

