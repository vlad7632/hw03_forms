import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220208_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='posts',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True,
            null=True,
            on_delete=django.db.models.deletion.SET_NULL,
            related_name='posts', to='posts.Group',
            verbose_name='Группа'),
        ),
    ]
