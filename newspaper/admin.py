from django.contrib import admin

from newspaper.models import Newspaper, EmailSubscribe

admin.site.register(Newspaper)
admin.site.register(EmailSubscribe)
