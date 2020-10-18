from django.db import migrations


def create_customtext(apps, schema_editor):
    CustomText = apps.get_model("home", "CustomText")
    customtext_title = "Tst-Mob-1121"

    CustomText.objects.create(title=customtext_title)


def create_homepage(apps, schema_editor):
    HomePage = apps.get_model("home", "HomePage")
    homepage_body = """
        <h1 class="display-4 text-center">Tst-Mob-1121</h1>
        <p class="lead">
            This is the sample application created and deployed from the Crowdbotics app.
            You can view list of packages selected for this application below.
        </p>"""

    HomePage.objects.create(body=homepage_body)


def create_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    custom_domain = "tst-mob-1121-dev-13514.botics.co"

    site_params = {
        "name": "Tst-Mob-1121",
    }
    if custom_domain:
        site_params["domain"] = custom_domain

    Site.objects.update_or_create(defaults=site_params, id=1)


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(create_customtext),
        migrations.RunPython(create_homepage),
        migrations.RunPython(create_site),
    ]
