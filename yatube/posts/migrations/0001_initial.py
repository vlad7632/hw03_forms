import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(
                    max_length=100,
                    verbose_name='Имя')),
                ('slug', models.SlugField(
                    max_length=100,
                    unique=True,
                    verbose_name='URL')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(
                    max_length=100,
                    unique=True,
                    verbose_name='URL')),
                ('author', models.ForeignKey(
                 on_delete=django.db.models.deletion.CASCADE,
                 related_name='posts',
                 to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(
                 blank=True,
                 null=True,
                 on_delete=django.db.models.deletion.CASCADE,
                 related_name='groups',
                 to='posts.Group')),
            ],
        ),
    ]
