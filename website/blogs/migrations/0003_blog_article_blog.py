# Generated by Django 4.0.4 on 2022-05-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_article_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blogs.blog'),
            preserve_default=False,
        ),
    ]