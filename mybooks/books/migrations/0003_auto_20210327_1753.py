# Generated by Django 3.1.7 on 2021-03-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210327_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(max_length=255)),
                ('author_last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='books.Author'),
        ),
    ]
