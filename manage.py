#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Unable to import Django. Is it installed and "
            "accessible on your PYTHONPATH env variable? Have you "
            "activated a virtual env ?"
        ) from exc
    execute_from_command_line(sys.argv)
