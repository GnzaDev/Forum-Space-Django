# Generated by Django 5.1.1 on 2024-11-15 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_remove_customuser_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='tema',
        ),
        migrations.AddField(
            model_name='customuser',
            name='banear_hasta',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.categoria')),
                ('likes', models.ManyToManyField(blank=True, related_name='posts_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notificacion',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.post'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagina.post'),
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
    ]
