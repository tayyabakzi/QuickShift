from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Id', models.IntegerField(verbose_name='employee ID')),
                ('Name', models.CharField(max_length=50, verbose_name='full name')),
                ('Scheduling', models.CharField(max_length=50, verbose_name='scheduling')),
                ('Department', models.CharField(max_length=100, verbose_name='department')),
                ('Team', models.CharField(max_length=50, verbose_name='team')),
                ('Manager_Name', models.CharField(max_length=50, verbose_name='manager name')),
                ('Manager_Id', models.IntegerField(verbose_name='manager ID')),
                ('Email', models.EmailField(max_length=254, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
    ]