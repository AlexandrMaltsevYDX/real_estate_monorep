# Generated by Django 4.2.9 on 2024-02-06 10:45

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apps_blog", "0004_alter_post_uuid_alter_postimagemodel_uuid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostProxy",
            fields=[],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps_blog.post",),
        ),
    ]
