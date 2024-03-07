from utils.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model


class GenderChoice(models.TextChoices):
    MALE = ("Male",)
    FEMALE = ("Female",)
    NOT_TO_SAY = ("Prefer not to say",)


class Pronouns(BaseModel):
    pronoun = models.CharField(max_length=16)
    show_followers_only = models.BooleanField(default=False)

    def __str__(self):
        return self.pronoun


class Links(BaseModel):
    url = models.URLField()
    title = models.CharField(max_length=32)


class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    links = models.ForeignKey(Links, on_delete=models.CASCADE, blank=True, null=True)

    caption = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GenderChoice.choices)
    suggestion = models.BooleanField(default=False)
    

    image = models.ImageField(upload_to="media/", blank=True, null=True)
    avatar = models.ImageField(upload_to="media/", blank=True, null=True)

    followers = models.ManyToManyField("self", related_name="following", symmetrical=False)

    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)


class Reels(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reels')
    tag = models.CharField(max_length=32)
    
    reel_video = models.FileField(upload_to='media/reels/')

    location = models.CharField(max_length=255, blank=True, null=True)

    is_let_template = models.BooleanField(default=False)
    is_hide_count_likes = models.BooleanField(default=False)
    is_show_captions = models.BooleanField(default=True)
    is_high_quality = models.BooleanField(default=False)

    caption = models.TextField()

    number_of_likes = models.PositiveIntegerField(default=0)
    number_of_comments = models.PositiveIntegerField(default=0)
    number_of_sends = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Reels'
        verbose_name_plural = 'Reels'


class Post(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post_user")

    description = models.TextField(blank=True, null=True)
    add_remainder = models.TextField(blank=True, null=True)
    additional_text = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=255, blank=True, null=True)

    likes = models.IntegerField(default=0)
    
    image = models.ImageField(upload_to="media/")

    is_facebook = models.BooleanField(default=False, blank=True, null=True)
    is_saved = models.BooleanField(default=False, blank=True, null=True)
    is_hide_views_likes = models.BooleanField(default=False, blank=True, null=True)
    is_comments = models.BooleanField(default=False, blank=True, null=True)


class NotesInDM(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="noted_user")
    note = models.TextField()
    likes = models.IntegerField(default=0)
    

class DirectChat(BaseModel):
    first_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='second_user')


class DirectMessage(BaseModel):
    chat = models.ForeignKey(DirectChat, on_delete=models.CASCADE, related_name='dm_message')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sent_messages")

    note = models.ForeignKey(NotesInDM, on_delete=models.CASCADE, blank=True, null=True, related_name="notes")

    message = models.TextField()
    file = models.FileField(upload_to='media/', blank=True, null=True)


class CommentPost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commented_post")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_comment_post")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies_post")

    likes = models.IntegerField(default=0)
    text = models.TextField()

class CommentReel(BaseModel):
    reel = models.ForeignKey(Reels, on_delete=models.CASCADE, related_name="commented_reel")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_comment_reel")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies_reel")

    likes = models.IntegerField(default=0)
    text = models.TextField()


class CommentPostUserLike(BaseModel):
    comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE, related_name='comment_liked_post')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_like_post')


class CommentReelUserLike(BaseModel):
    comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE, related_name='comment_liked_reel')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_like_reel')


class LikesPost(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ManyToManyField(get_user_model())

class LikesReel(BaseModel):
    reel = models.ForeignKey(Reels, on_delete=models.CASCADE, related_name="reel_likes")
    user = models.ManyToManyField(get_user_model())



class Story(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="stories")
    image = models.ImageField(upload_to="story_image/")
