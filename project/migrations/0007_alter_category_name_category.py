from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('MR', 'Торговцы'), ('GL', 'Гилдмастеры'), ('QE', 'Квестгиверы'), ('BL', 'Кузнецы'), ('LT', 'Кожевники'), ('PM', 'Зельевары'), ('SP', 'Мастера закленаний')], max_length=2, verbose_name='Тип'),
        ),
    ]
