# Generated by Django 4.1.2 on 2022-11-18 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeBook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='IngredientClassID',
        ),
        migrations.DeleteModel(
            name='Ingredient_Class',
        ),
    ]