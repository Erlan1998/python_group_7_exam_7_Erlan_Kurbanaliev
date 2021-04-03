# Generated by Django 3.1.7 on 2021-04-03 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210403_0645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопрос'},
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answers', to='webapp.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answers', to='webapp.poll')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'db_table': 'Answers',
            },
        ),
    ]