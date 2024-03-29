import ckeditor.fields
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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('MR', 'Торговцы'), ('GL', 'Гилдмастеры'), ('QE', 'Квестгиверы'), ('BL', 'Кузнецы'), ('LT', 'Кожевники'), ('PM', 'Зельевары'), ('SP', 'Мастера закленаний')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_notice', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время поста')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField()),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.author', verbose_name='Имя автора')),
                ('category_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_responses', models.TextField(max_length=255, verbose_name='Текст комментария')),
                ('datetime_responses', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время комментария')),
                ('responses_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.notice')),
                ('user_responses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
        ),
    ]
