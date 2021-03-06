# Generated by Django 3.0.5 on 2020-04-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interactions_over_Processes', models.CharField(max_length=120, verbose_name='Individuals and Interactions Over Processes and Tools')),
                ('comprehensive_documentation', models.CharField(max_length=120, verbose_name='Working Software Over Comprehensive Documentation')),
                ('customer_collaboration', models.CharField(max_length=120, verbose_name='Customer Collaboration Over Contract Negotiation')),
                ('change_over_plan', models.CharField(max_length=120, verbose_name='Responding to Change Over Following a Plan')),
                ('customer_satisfaction', models.CharField(max_length=120, verbose_name='Customer satisfaction through early and continuous software delivery')),
                ('accommodate_changing_in_requirements', models.CharField(max_length=120, verbose_name='Accommodate changing requirements throughout the development process')),
                ('frequent_delivery', models.CharField(max_length=120, verbose_name='Frequent delivery of working software')),
                ('collaboration_dev_client', models.CharField(max_length=120, verbose_name='Collaboration between the business stakeholders and developers throughout the project')),
                ('support_trust_motivate', models.CharField(max_length=120, verbose_name='Support, trust, and motivate the people involved')),
                ('face_interaction', models.CharField(max_length=120, verbose_name='Enable face-to-face interactions')),
                ('primary_measure', models.CharField(max_length=120, verbose_name='Working software is the primary measure of progress')),
                ('consistent_development', models.CharField(max_length=120, verbose_name='Agile processes to support a consistent development pace')),
                ('attention_to_technical_details', models.CharField(max_length=120, verbose_name='Attention to technical detail and design enhances agility')),
                ('simplicity', models.CharField(max_length=120, verbose_name='Simplicity')),
                ('encourage_organizing', models.CharField(max_length=120, verbose_name='Self-organizing teams encourage great architectures, requirements, and designs')),
                ('regular_reflections', models.CharField(max_length=120, verbose_name='Regular reflections on how to become more effective')),
            ],
        ),
    ]
