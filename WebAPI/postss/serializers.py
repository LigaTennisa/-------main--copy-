from rest_framework import serializers
from postss.models import Post
from django.forms import SelectDateWidget
from django.utils import timezone
from rest_framework import serializers


class TimePickerWidget(serializers.CharField):
    input_type = 'time'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    training_date = serializers.DateField(
        label='Дата', widget=SelectDateWidget(), initial=timezone.now().date())
    training_time = serializers.TimeField(
        label='Время', widget=TimePickerWidget(), initial=timezone.now().time())

    class Meta:
        model = Post
        fields = ['title', 'court', 'training_date',
                  'training_time', 'preferences']
        
