



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_comments_foodname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_comments',
        ),
    ]
