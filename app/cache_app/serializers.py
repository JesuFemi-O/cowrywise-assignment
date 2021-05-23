from rest_framework import fields, serializers


class TimeStampSerializer(serializers.Serializer):
    timestamp = serializers.CharField(max_length=36)

    class Meta:
        fields = '__all__'
