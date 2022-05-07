from __future__ import absolute_import
import os
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
app = Celery('proj')

# 문자열로 등록은 Celery Worker가 자식 프로세스에게 피클링하지 하지 않아도 되다고 알림
# namespace = 'CELERY'는 Celery관련 세팅 파일에서 변수 Prefix가 CELERY_ 라고 알림
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
   print('Request: {0!r}'.format(self.request))