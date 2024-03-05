from utils.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model


class GenderChoice(models.TextChoices):
    MALE = ("Male",)
    FEMALE = ("Female",)
    NOT_TO_SAY = ("Prefer not to say",)


class Profile(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GenderChoice.choices)
    suggestion = models.BooleanField(default=False)
    website = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to="media/", blank=True, null=True)
    avatar = models.ImageField(upload_to="media/", blank=True, null=True)

    followers = models.ManyToManyField("self", related_name="following", symmetrical=False)

    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)


class RemindOfMe(BaseModel):
    text = models.TextField()

    def __str__(self):
        return self.text


class AdditionalSetting(BaseModel):
    is_hide_views_likes = models.BooleanField(default=False)
    is_comments = models.BooleanField(default=False)
    is_share_facebook = models.BooleanField(default=False)

    additional_text = models.TextField()


class Post(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="post_user")

    image = models.ImageField(upload_to="media/")
    description = models.TextField(blank=True, null=True)

    add_remainder = models.ForeignKey(
        RemindOfMe, on_delete=models.CASCADE, blank=True, null=True, related_name="post_remainder"
    )
    additional_settings = models.ForeignKey(AdditionalSetting, on_delete=models.CASCADE, related_name="post_settings")

    location = models.CharField(max_length=255, blank=True, null=True)

    likes = models.IntegerField(default=0)

    is_facebook = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)


class NotesInDM(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="noted_user")

    note = models.TextField()


class DirectMessage(BaseModel):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="received_messages")
    note = models.ForeignKey(NotesInDM, on_delete=models.CASCADE, blank=True, null=True, related_name="notes")
    message = models.TextField()


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commented_post")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="author")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies")

    text = models.TextField()


class Like(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")
    user = models.ManyToManyField(get_user_model())


class Story(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="stories")
    image = models.ImageField(upload_to="story_image/")
