# Generated by Django 3.1.3 on 2020-11-11 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quest',
            options={'ordering': ['survey'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='mysurvey',
            name='end',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='mysurvey',
            name='published',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='mysurvey',
            name='title',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='text',
            field=models.TextField(max_length=100, verbose_name='Вопрос'),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Ответ')),
                ('qwes', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='answer.quest', verbose_name='Вопрос')),
                ('sur', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='answer.mysurvey', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]