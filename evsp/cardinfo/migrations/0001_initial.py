# Generated by Django 4.1.4 on 2022-12-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=64, verbose_name='카드이름')),
                ('cardtag', models.CharField(max_length=64, verbose_name='카드테그')),
                ('cardstatus', models.CharField(max_length=64, verbose_name='배포상태')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='카드등록일시')),
                ('userid', models.CharField(max_length=64, verbose_name='회원아이디')),
            ],
            options={
                'verbose_name': '카드정보',
                'verbose_name_plural': '카드정보',
                'db_table': 'evsp_cardinfo',
            },
        ),
    ]
