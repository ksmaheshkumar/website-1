# Generated by Django 1.11.16 on 2018-10-24 09:29

import uuid

import django.db.models.deletion
import vies.models
import vies.validators
from django.db import migrations, models

import payments.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vat",
                    vies.models.VATINField(
                        blank=True,
                        max_length=14,
                        null=True,
                        validators=[
                            vies.validators.VATINValidator(validate=True, verify=True)
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(max_length=200, null=True)),
                ("country", models.CharField(max_length=200, null=True)),
                (
                    "email",
                    models.EmailField(
                        max_length=190, validators=[payments.utils.validate_email],
                    ),
                ),
                ("origin", models.URLField(max_length=300)),
                ("user_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.IntegerField()),
                ("description", models.TextField()),
                (
                    "recurring",
                    models.CharField(
                        choices=[("y", "Yearly"), ("m", "Monthly"), ("", "None")],
                        default="",
                        max_length=10,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("paid", models.BooleanField(default=False)),
                ("handled", models.BooleanField(default=False)),
                ("processor", models.CharField(default="", max_length=100)),
                ("details", payments.utils.JSONField(editable=False)),
                ("extra", payments.utils.JSONField(editable=False)),
                ("repeat", payments.utils.JSONField(editable=False)),
                ("invoice", models.CharField(blank=True, default="", max_length=20)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.Customer",
                    ),
                ),
            ],
        ),
    ]
