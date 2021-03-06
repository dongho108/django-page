# Generated by Django 2.1.7 on 2020-01-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20200101_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_type',
            field=models.CharField(choices=[(None, '일반 페이지'), ('root', '루트 페이지'), ('main', '메인 페이지'), ('home', '루트 + 메인')], default=None, help_text='\n    랜딩 페이지: 처음 사이트에 진입하면 표시되는 사이트 입니다. 페이지 코드와 무관하게 루트 주소 "/"를 갖습니다.<br/>\n    메인 페이지: 페이지 내에서 첫 페이지로 돌아갈 때에 목적지가 되는 페이지 입니다. 로고나 \'처음으로\' 버튼 등에 링크됩니다.<br/>\n    랜딩 + 메인: 루트이자 첫 페이지로 대부분의 사이트에서 홈페이지에 해당 됩니다.\n    ', max_length=10, null=True, verbose_name='특별한 페이지'),
        ),
    ]
