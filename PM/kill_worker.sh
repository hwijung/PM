ps auxww | grep 'celery -A PM worker' | awk '{print $2}' | xargs kill -9