# Generated by Django 4.2.3 on 2024-05-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugapp", "0011_alter_bug_report_bug_image_bug_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bug_status",
            name="status",
        ),
        migrations.AddField(
            model_name="bug_status",
            name="bug_status",
            field=models.CharField(
                choices=[("1", "Open"), ("2", "In Progress"), ("3", "Resolved")],
                default="1",
                max_length=10,
            ),
        ),
    ]
