# Generated by Django 4.1.6 on 2023-04-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('researcher_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Protocol Code')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.CharField(max_length=100, verbose_name='Researcher Email')),
                ('password', models.CharField(max_length=100, verbose_name='Researcher Password')),
                ('school', models.CharField(max_length=100, verbose_name='Researcher School')),
                ('level', models.CharField(max_length=100, verbose_name='Researcher Level')),
                ('protocol_title', models.CharField(max_length=100, verbose_name='Research Title')),
                ('principal_investigator', models.TextField(max_length=1000, verbose_name='Principal Investigator/s')),
                ('minutes_of_proposal', models.FileField(upload_to='', verbose_name='Minutes of Proposal Defense')),
                ('revised_copy', models.FileField(upload_to='media/', verbose_name='Revised Copy')),
                ('routing_form', models.FileField(upload_to='media/', verbose_name='Routing Form')),
                ('adviser_edorsement', models.FileField(upload_to='media/', verbose_name="Adviser's Endorsement for Ethics Review")),
                ('curriculum_vitae', models.FileField(upload_to='media/', verbose_name='Updated Curriculum Vitae (CV) of the Adviser(s) and Researcher(s)')),
                ('research_agenda', models.FileField(upload_to='media/', verbose_name='Updated Research Agenda of the Program')),
                ('grades', models.FileField(upload_to='media/', verbose_name='Grades')),
                ('REC_FO_OO23', models.FileField(upload_to='media/', verbose_name='REC_FO_OO23')),
                ('REC_FO_OO24', models.FileField(upload_to='media/', verbose_name='REC_FO_OO24')),
                ('REC_FO_OO25', models.FileField(upload_to='media/', verbose_name='REC_FO_OO25')),
                ('REC_FO_OO26', models.FileField(upload_to='media/', verbose_name='REC_FO_OO26')),
                ('REC_FO_OO27', models.FileField(upload_to='media/', verbose_name='REC_FO_OO27')),
                ('REC_FO_OO57', models.FileField(upload_to='media/', verbose_name='REC_FO_OO57')),
                ('REC_FO_OO57B', models.FileField(upload_to='media/', verbose_name='REC_FO_OO57B')),
                ('REC_FO_OO58', models.FileField(upload_to='media/', verbose_name='REC_FO_OO58')),
                ('payment', models.FileField(upload_to='media/', verbose_name='Payment')),
                ('revised_manuscript', models.FileField(upload_to='media/', verbose_name='Revised Manuscript')),
            ],
        ),
    ]
