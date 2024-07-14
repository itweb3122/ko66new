# Generated by Django 5.0.7 on 2024-07-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_banner_lobbyitem_alter_brandinfo_favicon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancaLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='CasinoLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(verbose_name=8)),
                ('username', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DagaLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='EsportLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='GamebaiLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='HotGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameItem', models.CharField(max_length=40)),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='HotLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='NohuLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=20)),
                ('describe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TheThaoLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='TopGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameItem', models.CharField(max_length=40)),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.CreateModel(
            name='XosoLobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobbyId', models.IntegerField(verbose_name=3)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('nameItem', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(verbose_name=1)),
                ('isActive', models.IntegerField(verbose_name=1)),
                ('order', models.IntegerField(verbose_name=2)),
            ],
        ),
        migrations.RenameField(
            model_name='lobbyitem',
            old_name='lobby',
            new_name='lobbyName',
        ),
        migrations.RenameField(
            model_name='lobbyitem',
            old_name='name',
            new_name='nameItem',
        ),
        migrations.RenameField(
            model_name='mainlobby',
            old_name='mainlobby',
            new_name='lobbyName',
        ),
        migrations.RemoveField(
            model_name='lobbyitem',
            name='order',
        ),
        migrations.AddField(
            model_name='mainlobby',
            name='lobbyId',
            field=models.IntegerField(default=0, verbose_name=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='isDeleted',
            field=models.IntegerField(verbose_name=1),
        ),
        migrations.AlterField(
            model_name='lobbyitem',
            name='isActive',
            field=models.IntegerField(verbose_name=1),
        ),
        migrations.AlterField(
            model_name='lobbyitem',
            name='isDeleted',
            field=models.IntegerField(verbose_name=1),
        ),
    ]
