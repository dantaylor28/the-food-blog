# Generated by Django 3.2.16 on 2022-10-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221028_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='food', max_length=75),
        ),
        migrations.AlterField(
            model_name='post',
            name='extract',
            field=models.CharField(max_length=300),
        ),
    ]
