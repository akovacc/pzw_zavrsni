# Generated by Django 4.1.3 on 2024-03-04 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="Ime")),
                ("surname", models.CharField(max_length=64, verbose_name="Prezime")),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Broj telefona",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(max_length=128, verbose_name="Naziv kategorije"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=25, verbose_name="Naslov")),
                (
                    "content",
                    models.TextField(
                        blank=True, null=True, verbose_name="Tekst članka"
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Datum objave"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.author",
                        verbose_name="Author",
                    ),
                ),
                (
                    "category_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.category",
                        verbose_name="Category",
                    ),
                ),
            ],
        ),
    ]
