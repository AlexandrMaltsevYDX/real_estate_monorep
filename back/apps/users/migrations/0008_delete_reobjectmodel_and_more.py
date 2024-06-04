# Generated by Django 4.2.9 on 2024-02-06 17:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0007_alter_employeeprofileavatarmodel_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ReObjectModel",
        ),
        migrations.AlterModelOptions(
            name="employeeprofilemodel",
            options={"verbose_name": "Сотрудник", "verbose_name_plural": "Сотрудники"},
        ),
        migrations.AlterField(
            model_name="employeeprofileavatarmodel",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
