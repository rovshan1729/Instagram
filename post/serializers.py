from rest_framework import serializers
from . import models

class PronounSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pronouns
        fields = (
            'id',
            'pronoun',
            'show_followers_only',
            'created_at',
            'updated_at',
        )

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Links
        fields = (
            'id',
            'url',
            'title',
            'created_at',
            'updated_at',
        )

class ProfileSerializer(serializers.ModelSerializer):
    pronoun = serializers.StringRelatedField(source='pronoun')
    link = LinkSerializer()

    class Meta:
        model = models.Profile
        fields = (
            'id',
            'user_username',
            'link',
            'caption',
            'gender',
            'suggestion',
            'image',
            'avatar',
            'followers',
            'date_of_birth',
            'email',
            'phone_number',
            'created_at',
            'updated_at',
        )

class ReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reel
        fields = (
            'id',
            'user_username',
            'tag',
            'reel_video',
            'location',
            'is_let_template',
            'is_hide_count_likes',
            'is_show_captions',
            'is_high_quality',
            'caption',
            'number_of_likes',
            'number_of_comments',
            'number_of_sends',
            'created_at',
            'updated_at',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'id',
            'user_username',
            'description',
            'add_remainder',
            'additional_text',
            'location',
            'likes',
            'image',
            'is_facebook',
            'is_saved',
            'is_hide_views_likes',
            'is_comments',
            'created_at',
            'updated_at',
        )

class NoteInDMSerializer(serializers.Model):
    class Meta:
        model = models.NotesInDM
        fields = (
            'id',
            'user_username',
            'note',
            'likes',
            'created_at',
            'updated_at',
        )

class DirectChat(serializers.ModelSerializer):
    class Meta:
        model = models.DirectChat
        fields = (
            'id',
            'first_user_username',
            'second_user_username',
            'created_at',
            'updated_at',
        )

class DirectMessage(serializers.ModelSerializer):
    chat = DirectChat()

    class Meta:
        model = models.DirectMessage
        fields = (
            'id',
            'chat'
            'sender',
            'note',
            'message',
            'file',
            'created_at',
            'updated_at',
        )

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentPost
        fields = (
            'id',
            'user_username',
            'parent',
            'likes',
            'text',
            'created_at',
            'updated_at',
        )

class CommentReelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentReel
        fields = (
            'id',
            'user_username',
            'parent',
            'likes',
            'text',
            'created_at',
            'updated_at',
        )

class CommentPostUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentPostUserLike
        fields = (
            'id',
            'user_username',
            'comment',
            'created_at',
            'updated_at',
        )


class CommentReelUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentReelUserLike
        fields = (
            'id',
            'user_username',
            'comment',
            'created_at',
            'updated_at',
        )


class LikesPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = models.LikesPost
        fields = (
            'id',
            'user_username',
            'post',
            'created_at',
            'updated_at',
        )

class LikesReelSerializer(serializers.ModelSerializer):
    reel = ReelSerializer()

    class Meta:
        model = models.LikesPost
        fields = (
            'id',
            'user_username',
            'reel',
            'created_at',
            'updated_at',
        )

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Story
        fields = (
            'id',
            'user_username',
            'image',
            'created_at',
            'updated_at',
        )



