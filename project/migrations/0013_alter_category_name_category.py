from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_alter_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(choices=[('tanks', 'Танки'), ('Hill', 'Хилы'), ('DD', 'ДД'), ('Merchants', 'Торговцы'), ('Guildmasters', 'Гилдмастеры'), ('Questgivers', 'Квестгиверы'), ('Blacksmiths', 'Кузнецы'), ('Leatherworkers', 'Кожевники'), ('Potions', 'Зельевары'), ('Spell Masters', 'Мастера закленаний')], max_length=20, verbose_name='Тип'),
        ),
    ]
