# Generated by Django 4.2.3 on 2024-05-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bugapp", "0009_alter_bug_report_bug_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug_report",
            name="bug_image",
            field=models.ImageField(upload_to="static/uploads"),
        ),
    ]