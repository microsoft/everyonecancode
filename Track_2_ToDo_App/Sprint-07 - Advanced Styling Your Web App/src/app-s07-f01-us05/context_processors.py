# context_processors.py

from datetime import datetime

def inject_current_date():
    return {'current_date': datetime.now().strftime('%Y-%m-%d')}