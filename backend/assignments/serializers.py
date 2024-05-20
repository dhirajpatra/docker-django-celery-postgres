from rest_framework import serializers
from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    # Serializer to validate input
    class Meta:
        model = Assignment
        fields = ('id', 'first_term', 'second_term', 'sum')
        read_only_fields = ['id', 'sum']

        # validate the sum of the two terms
        def validate(self, data):
            if data['first_term'] + data['second_term'] != data['sum']:
                raise serializers.ValidationError('Sum of the two terms does not match the sum field')
            return data
