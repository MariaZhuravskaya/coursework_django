# Generated by Django 4.2.5 on 2023-10-02 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id_блога')),
                ('header', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Cодержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='изображение')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='дата публикации')),
                ('number_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('is_publication', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
