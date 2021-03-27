import os


def GA_context(req):
    return {
        'GA_CODE':os.getenv('GA','--=--')
    }