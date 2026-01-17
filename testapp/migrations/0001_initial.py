from django.db import migrations, models
import cryptographic_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enc_char_field', cryptographic_fields.fields.EncryptedCharField(max_length=100)),
                ('enc_text_field', cryptographic_fields.fields.EncryptedTextField()),
                ('enc_date_field', cryptographic_fields.fields.EncryptedDateField(null=True)),
                ('enc_date_now_field', cryptographic_fields.fields.EncryptedDateField(auto_now=True, null=True)),
                ('enc_date_now_add_field', cryptographic_fields.fields.EncryptedDateField(auto_now_add=True, null=True)),
                ('enc_datetime_field', cryptographic_fields.fields.EncryptedDateTimeField(null=True)),
                ('enc_boolean_field', cryptographic_fields.fields.EncryptedBooleanField(default=True)),
                ('enc_null_boolean_field', cryptographic_fields.fields.EncryptedNullBooleanField()),
                ('enc_integer_field', cryptographic_fields.fields.EncryptedIntegerField(null=True)),
                ('enc_positive_integer_field', cryptographic_fields.fields.EncryptedPositiveIntegerField(null=True)),
                ('enc_small_integer_field', cryptographic_fields.fields.EncryptedSmallIntegerField(null=True)),
                ('enc_positive_small_integer_field', cryptographic_fields.fields.EncryptedPositiveSmallIntegerField(null=True)),
                ('enc_big_integer_field', cryptographic_fields.fields.EncryptedBigIntegerField(null=True)),
            ],
        ),
    ]
