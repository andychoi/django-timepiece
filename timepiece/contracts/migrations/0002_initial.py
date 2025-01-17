# Generated by Django 4.1.5 on 2023-01-14 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entries', '0001_initial'),
        ('crm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcontract',
            name='projects',
            field=models.ManyToManyField(related_name='contracts', to='crm.project'),
        ),
        migrations.AddField(
            model_name='hourgroup',
            name='activities',
            field=models.ManyToManyField(related_name='activity_bundle', to='entries.activity'),
        ),
        migrations.AddField(
            model_name='entrygroup',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entry_group', to='crm.project'),
        ),
        migrations.AddField(
            model_name='entrygroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entry_group', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contracthour',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contract_hours', to='contracts.projectcontract'),
        ),
        migrations.AddField(
            model_name='contractassignment',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='contracts.projectcontract'),
        ),
        migrations.AddField(
            model_name='contractassignment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='contractassignment',
            unique_together={('contract', 'user')},
        ),
    ]
