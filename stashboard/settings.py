import os

DEBUG = False

SITE_NAME = "Tracelytics Status"
SITE_AUTHOR = "Tracelytics Ops"
SITE_URL = "http://status.tracelytics.com"
REPORT_URL = "mailto:support@tracelytics.com"

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
