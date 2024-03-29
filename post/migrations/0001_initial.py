# Generated by Django 4.2.7 on 2024-03-07 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("likes", models.IntegerField(default=0)),
                ("text", models.TextField()),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies_post",
                        to="post.commentpost",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DirectChat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "first_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="first_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "second_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="second_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Links",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("url", models.URLField()),
                ("title", models.CharField(max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("caption", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female"), ("Prefer not to say", "Not To Say")],
                        max_length=255,
                    ),
                ),
                ("suggestion", models.BooleanField(default=False)),
                ("image", models.ImageField(blank=True, null=True, upload_to="media/")),
                ("avatar", models.ImageField(blank=True, null=True, upload_to="media/")),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                ("followers", models.ManyToManyField(related_name="following", to="post.profile")),
                (
                    "links",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="post.links"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pronouns",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("pronoun", models.CharField(max_length=16)),
                ("show_followers_only", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Story",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="story_image/")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Reel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("tag", models.CharField(max_length=32)),
                ("reel_video", models.FileField(upload_to="media/reel/")),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("is_let_template", models.BooleanField(default=False)),
                ("is_hide_count_likes", models.BooleanField(default=False)),
                ("is_show_captions", models.BooleanField(default=True)),
                ("is_high_quality", models.BooleanField(default=False)),
                ("caption", models.TextField()),
                ("number_of_likes", models.PositiveIntegerField(default=0)),
                ("number_of_comments", models.PositiveIntegerField(default=0)),
                ("number_of_sends", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="reel", to="post.profile"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("add_remainder", models.TextField(blank=True, null=True)),
                ("additional_text", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("likes", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="media/")),
                ("is_facebook", models.BooleanField(blank=True, default=False, null=True)),
                ("is_saved", models.BooleanField(blank=True, default=False, null=True)),
                ("is_hide_views_likes", models.BooleanField(blank=True, default=False, null=True)),
                ("is_comments", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="post_user", to="post.profile"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NotesInDM",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("note", models.TextField()),
                ("likes", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="noted_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LikesReel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="reel_likes", to="post.reel"
                    ),
                ),
                ("user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LikesPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="post_likes", to="post.post"
                    ),
                ),
                ("user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DirectMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("message", models.TextField()),
                ("file", models.FileField(blank=True, null=True, upload_to="media/")),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="dm_message", to="post.directchat"
                    ),
                ),
                (
                    "note",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="post.notesindm",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CommentReelUserLike",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_liked_reel",
                        to="post.commentpost",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_like_reel",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CommentReel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("likes", models.IntegerField(default=0)),
                ("text", models.TextField()),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies_reel",
                        to="post.commentreel",
                    ),
                ),
                (
                    "reel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="commented_reel", to="post.reel"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_comment_reel",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CommentPostUserLike",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_liked_post",
                        to="post.commentpost",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_like_post",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="commentpost",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="commented_post", to="post.post"
            ),
        ),
        migrations.AddField(
            model_name="commentpost",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_comment_post",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
