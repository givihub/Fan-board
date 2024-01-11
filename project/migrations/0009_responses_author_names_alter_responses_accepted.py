from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_responses_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='author_names',
            field=models.ManyToManyField(to='project.author'),
        ),
        migrations.AlterField(
            model_name='responses',
            name='accepted',
            field=models.BooleanField(default=None, verbose_name='Принято/Отклонено'),
        ),
    ]
