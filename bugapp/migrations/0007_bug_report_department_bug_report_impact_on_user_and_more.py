# Generated by Django 4.2.3 on 2024-04-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugapp", "0006_bug_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="bug_report",
            name="department",
            field=models.CharField(
                choices=[("1", "Backend"), ("2", "Frontend"), ("3", "other")],
                default="1",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="bug_report",
            name="impact_on_user",
            field=models.CharField(
                choices=[
                    ("1", "major"),
                    ("2", "minor"),
                    ("3", "moderate"),
                    ("4", "no_impact"),
                ],
                default="1",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="bug_report",
            name="urgency_level",
            field=models.CharField(
                choices=[("1", "low"), ("2", "medium"), ("3", "high")],
                default="1",
                max_length=1,
            ),
        ),
    ]
