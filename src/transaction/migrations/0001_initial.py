# Generated by Django 2.2.3 on 2019-07-29 14:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0002_auto_20190726_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stellar_account', models.TextField(validators=[django.core.validators.MinLengthValidator(1)])),
                ('kind', models.CharField(choices=[('deposit', 'deposit'), ('withdrawal', 'withdrawal')], default='deposit', max_length=20)),
                ('status', models.CharField(choices=[('completed', 'completed'), ('pending_external', 'pending_external'), ('pending_anchor', 'pending_anchor'), ('pending_stellar', 'pending_stellar'), ('pending_trust', 'pending_trust'), ('pending_user', 'pending_user'), ('pending_user_transfer_start', 'pending_user_transfer_start'), ('incomplete', 'incomplete'), ('no_market', 'no_market'), ('too_small', 'too_small'), ('too_large', 'too_large'), ('error', 'error')], default='pending_external', max_length=30)),
                ('status_eta', models.IntegerField(blank=True, null=True)),
                ('stellar_transaction_id', models.TextField(blank=True, null=True)),
                ('external_transaction_id', models.TextField(blank=True, null=True)),
                ('amount_in', models.FloatField(blank=True, null=True)),
                ('amount_out', models.FloatField(blank=True, null=True)),
                ('amount_fee', models.FloatField(blank=True, null=True)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Asset')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]