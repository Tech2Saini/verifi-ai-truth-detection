# Generated by Django 5.1.1 on 2024-10-17 19:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='fid',
            field=models.UUIDField(default=uuid.UUID('b8441828-b68c-4a0f-a314-0c04410a2287'), editable=False, unique=True),
        ),
    ]
