from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_alter_notice_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='accepted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя автора'),
        ),
    ]
