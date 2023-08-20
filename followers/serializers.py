from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name']

    def create(self, validated_data):
        owner = self.context['request'].user
        followed = validated_data['followed']

        # Check if the follower relationship already exists
        if Follower.objects.filter(owner=owner, followed=followed).exists():
            raise serializers.ValidationError("You are already following this user.")

        return Follower.objects.create(owner=owner, followed=followed)
