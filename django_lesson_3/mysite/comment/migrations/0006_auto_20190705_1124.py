# Generated by Django 2.2.2 on 2019-07-05 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_merge_20190627_1334'),
        ('comment', '0005_auto_20190705_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecomment',
            name='article',
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='article_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
            preserve_default=False,
        ),
    ]
