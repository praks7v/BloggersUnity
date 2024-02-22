from django.apps import AppConfig


class TechConfig(AppConfig):
    """ Configuration for the 'Tech' app. """

    # The default_auto_field defines the default primary key field for models.
    # In this configuration, it's set to 'django.db.models.BigAutoField'.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the app, which should match the name of the app's directory.
    name = 'Tech'
