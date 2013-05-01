import os

DEBUG = False

SITE_NAME = "TraceView Status"
SITE_AUTHOR = "TraceView Ops"
SITE_URL = "http://status.tv.appneta.com"
REPORT_URL = "mailto:traceviewsupport@appneta.com"

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
