# Generated by Django 5.0.4 on 2024-05-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugapp", "0017_alter_bug_status_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug_report",
            name="bug_image",
            field=models.ImageField(
                default="static/media/default_bug_img.jpg", upload_to="uploads"
            ),
        ),
    ]
