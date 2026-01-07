from .celery import app as celery_app

# its a config for celery
__all__ = ("celery_app",)
