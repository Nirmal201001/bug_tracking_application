# Generated by Django 5.0.4 on 2024-05-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugapp", "0019_alter_bug_report_bug_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug_report",
            name="bug_image",
            field=models.ImageField(
                default="./static/media/default_bug_img.jpg", upload_to="uploads"
            ),
        ),
    ]
