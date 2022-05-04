# Generated by Django 3.2 on 2022-05-03 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220429_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authboard',
            name='ab_img_fir',
        ),
        migrations.RemoveField(
            model_name='authboard',
            name='ab_img_se',
        ),
        migrations.RemoveField(
            model_name='authboard',
            name='ab_img_thi',
        ),
        migrations.CreateModel(
            name='Authpicture',
            fields=[
                ('authpicture_id', models.AutoField(db_column='Authpicture_id', primary_key=True, serialize=False)),
                ('authpicture_img', models.ImageField(blank=True, db_column='Authpicture_img', null=True, upload_to='ab_images/')),
                ('ab_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.authboard')),
            ],
            options={
                'db_table': 'authpicture',
                'managed': True,
            },
        ),
    ]