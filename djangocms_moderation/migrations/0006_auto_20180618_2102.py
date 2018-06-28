# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-18 20:02
from __future__ import unicode_literals

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from djangocms_moderation import conf


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangocms_moderation', '0005_pagemoderationrequestaction_is_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationFormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(blank=True, editable=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='by user')),
            ],
            options={
                'verbose_name': 'Confirmation Form Submission',
                'verbose_name_plural': 'Confirmation Form Submissions',
            },
        ),
        migrations.CreateModel(
            name='ConfirmationPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('content_type', models.CharField(choices=[('plain', 'Plain'), ('form', 'Form')], default='form', max_length=50, verbose_name='Content Type')),
                ('template', models.CharField(choices=conf.CONFIRMATION_PAGE_TEMPLATES, default=conf.DEFAULT_CONFIRMATION_PAGE_TEMPLATE, max_length=100, verbose_name='Template')),
                ('content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='confirmation_content', to='cms.Placeholder')),
            ],
            options={
                'verbose_name': 'Confirmation Page',
                'verbose_name_plural': 'Confirmation Pages',
            },
        ),
        migrations.AddField(
            model_name='confirmationformsubmission',
            name='confirmation_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='djangocms_moderation.ConfirmationPage', verbose_name='confirmation page'),
        ),
        migrations.AddField(
            model_name='confirmationformsubmission',
            name='for_step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='djangocms_moderation.WorkflowStep', verbose_name='for step'),
        ),
        migrations.AddField(
            model_name='confirmationformsubmission',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_submissions', to='djangocms_moderation.PageModerationRequest', verbose_name='request'),
        ),
        migrations.AddField(
            model_name='role',
            name='confirmation_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='djangocms_moderation.ConfirmationPage', verbose_name='confirmation page'),
        ),
        migrations.AlterUniqueTogether(
            name='confirmationformsubmission',
            unique_together=set([('request', 'for_step')]),
        ),
    ]