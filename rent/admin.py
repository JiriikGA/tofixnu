from django.contrib import admin

from .models import Item
from .models import Loan
admin.site.register(Item)
admin.site.register(Loan)
