from rest_framework import serializers
from main.models import BlogPost


class BlogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
