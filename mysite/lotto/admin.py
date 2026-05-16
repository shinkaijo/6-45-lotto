from django.contrib import admin
from .models import Ticket, Draw  # 정의한 모델들을 불러옵니다.

# 관리자 페이지에서 Ticket과 Draw 모델을 조작할 수 있도록 등록합니다.
admin.site.register(Ticket)
admin.site.register(Draw)
# Register your models here.
