# Generated by Django 4.2.4 on 2023-09-23 14:39

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
            name='ShowcaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='images/projects')),
                ('creators_review', models.CharField(max_length=100)),
                ('project_showcase_image', models.ImageField(upload_to='images/projects/showcase')),
                ('single_project_page_image', models.ImageField(upload_to='images/projects/single_project')),
                ('category_type', models.CharField(max_length=200)),
                ('project_tittle_showcase', models.CharField(max_length=15)),
                ('project_tittle_single_project_page', models.CharField(max_length=250)),
                ('project_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showcase', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Showcase',
                'verbose_name_plural': 'Showcases',
            },
        ),
    ]
