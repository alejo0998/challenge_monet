# Generated by Django 3.0.8 on 2023-02-26 21:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='date',
            new_name='date_finish',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.AddField(
            model_name='test',
            name='date_init',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='note',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0, 0), django.core.validators.MaxValueValidator(10, 0)]),
        ),
        migrations.AlterField(
            model_name='test',
            name='note',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0, 0), django.core.validators.MaxValueValidator(10, 0)]),
        ),
        migrations.CreateModel(
            name='QuestionTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Test')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.QuestionTest'),
            preserve_default=False,
        ),
    ]
