from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    def validate(self, data):
        request = self.context.get('request')
        if not request.user.is_authenticated:
            raise PermissionDenied('Требуется аутентификация.')

        if self.instance and self.instance.author != request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        return data

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    post = serializers.SlugRelatedField(read_only=True, slug_field='id')
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if not request.user.is_authenticated:
            raise PermissionDenied('Требуется аутентификация.')

        if self.instance and self.instance.author != request.user:
            raise PermissionDenied('Изменение чужого комментария запрещено!')
        return data

    def create(self, validated_data):
        post_id = validated_data.pop('post')
        validated_data['post'] = get_object_or_404(Post, pk=post_id.id)
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate(self, data):
        request = self.context.get('request')
        if request.user == data['following']:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follow.objects.filter(
            user=request.user,
            following=data['following']
        ).exists():
            raise serializers.ValidationError(
                "You are already following this user."
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
