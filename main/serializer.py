from rest_framework import serializers
from .models import File
from datetime import datetime
class FileSer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id',
            'created_date',
            'name',
            'url',
            'time',
            'column')

    def get_time(self, obj):
        date = obj.created_date
        d = date.strftime("%Y-%m-%d %H:%M:%S")
        d = datetime.strptime(d, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        return d