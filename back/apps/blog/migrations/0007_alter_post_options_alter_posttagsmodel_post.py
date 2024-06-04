# Generated by Django 4.2.9 on 2024-02-23 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_blog", "0006_alter_post_uuid_alter_postimagemodel_uuid_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["author"],
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.AlterField(
            model_name="posttagsmodel",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts_posts",
                to="apps_blog.post",
            ),
        ),
    ]
