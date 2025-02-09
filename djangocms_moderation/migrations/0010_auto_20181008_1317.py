# Generated by Django 1.11.13 on 2018-10-08 12:17
from django.db import migrations


def get_model_classes(apps):
    confirmation_form_submission = apps.get_model(
        "djangocms_moderation", "ConfirmationFormSubmission"
    )
    moderation_request_action = apps.get_model(
        "djangocms_moderation", "ModerationRequestAction"
    )

    return confirmation_form_submission, moderation_request_action


def forward_copy_moderation_requests(apps, schema_editor):
    for model_class in get_model_classes(apps):
        for obj in model_class.objects.all():
            obj.moderation_request = obj.request
            obj.save()


def reverse_copy_moderation_requests(apps, schema_editor):
    for model_class in get_model_classes(apps):
        for obj in model_class.objects.all():
            obj.request = obj.moderation_request
            obj.save()


class Migration(migrations.Migration):

    dependencies = [("djangocms_moderation", "0009_auto_20181005_1534")]

    operations = [
        migrations.RunPython(
            forward_copy_moderation_requests, reverse_copy_moderation_requests
        )
    ]
