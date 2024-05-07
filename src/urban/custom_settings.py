import os

from urban.settings import *

INSTALLED_APPS += (
    'django_media_fixtures',
)

USE_X_FORWARDED_HOST = True

SENTRY_DSN = os.getenv("SENTRY_DSN", None)
if SENTRY_DSN:
    import logging
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration
    from sentry_sdk.integrations.celery import CeleryIntegration

    SENTRY_LOG_LEVEL = int(os.getenv("DJANGO_SENTRY_LOG_LEVEL", logging.INFO))

    sentry_logging = LoggingIntegration(
        level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR,  # Send errors as events
    )

    integrations = [sentry_logging, DjangoIntegration(), CeleryIntegration()]

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=integrations,
        environment=os.getenv("SENTRY_ENVIRONMENT", "production"),
        traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", 1.0)),
    )

    LOGGING["loggers"]["sentry_sdk"] = {"level": "ERROR", "handlers": ["console"], "propagate": False}
