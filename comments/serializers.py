from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')

    def get_is_owner(self, obj):
        request_user = self.context['request'].user
        return obj.owner == request_user

    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'owner',
         'is_owner', 'profile_id', 'profile_image']

class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'post', 'owner',
         'is_owner', 'profile_id', 'profile_image']
