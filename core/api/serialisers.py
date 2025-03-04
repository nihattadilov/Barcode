
from core.models import Blog
from rest_framework import serializers


class BlogSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title','description','description2','image')
        
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = instance.image.url
        data['created_at'] = instance.created_at.strftime('%Y-%m-%d')
        return data
 # onemli metodlar   
      
    # def create(self,validated_data):
    #     return super().create(validated_data)
    
    # def update(self,instance, validated_data):
    #     return super().update(instance,validated_data)
    
    # def to_internal_value(self, data):
    #     return super().to_internal_value(data)
    
    # def validate_title(self, value):
    #     if len(value) < 10:
    #         raise serializers.ValidationError('Title is too short')
    #     return value
    
    # def validate(self, attrs):
    #     print(attrs)
    #     return super().validate(attrs)
    
    