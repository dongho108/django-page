# Generated by Django 2.1.7 on 2020-01-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_auto_20190722_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='special',
            field=models.CharField(choices=[(None, '일반 페이지'), ('root', '루트 페이지'), ('main', '메인 페이지'), ('home', '루트 + 메인')], default=None, help_text='\n    랜딩 페이지: 처음 사이트에 진입하면 푀시되는 사이트 입니다. 페이지 코드와 무관하게 루트 주소 "/"를 갖습니다.\n    메인 페이지: 페이지 내에서 첫페이지로 돌아갈 때에 목적지가 되는 페이지 입니다. 로고나 \'처음으로\' 버튼등에 링크됩니다.\n    랜딩 + 메인: 대부분의 사이트에서 홈페이지에 해당 됩니다.\n    ', max_length=10, null=True, verbose_name='특별한 페이지'),
        ),
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.SlugField(help_text='페이지 url로 사용됩니다. 단, "home"의 경우 예외적으로 루트가 됩니다.', unique=True, verbose_name='페이지 코드'),
        ),
        migrations.AlterField(
            model_name='page',
            name='mobile_style',
            field=models.TextField(blank=True, default='', help_text='스타일 시트에 추가할 내용(테그 없이 작성)', null=True, verbose_name='CSS'),
        ),
        migrations.AlterField(
            model_name='page',
            name='script',
            field=models.TextField(blank=True, default='', help_text='페이지에 추가할 스크립트 내용(테그 없이 작성)', null=True, verbose_name='Script'),
        ),
        migrations.AlterField(
            model_name='page',
            name='style',
            field=models.TextField(blank=True, default='', help_text='스타일 시트에 추가할 내용(테그 없이 작성)', null=True, verbose_name='CSS'),
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(blank=True, default='', help_text='사이트 기본 템플릿(page.html)을 사용하지 않고 별도 템플릿을 사용하려는 경우 지정', max_length=256, null=True, verbose_name='커스텀 템플릿'),
        ),
    ]
