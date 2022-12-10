from rest_framework import serializers
from .models import Todo


class TodoSerializador(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields = '__all__' #para todos los campos.
        read_only_fields = ('created_at', 'done_at', 'updated_at', 'deleted_at',)

class TestTodoSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title = serializers.CharField(max_length = 100)
    body=serializers.CharField(max_length = 300)
    status=serializers.IntegerField()


    def validate_title(self,value):
        if "$" in value:
            raise serializers.ValidationError("Error, $ encontrado")
        return value

    def validate_body(self,value):
        if "$" in value:
            raise serializers.ValidationError("Error, $ encontrado")
        return value

        
    def create(self, validated_data):
        print(validated_data)
        return Todo.objects.create(**validated_data)
