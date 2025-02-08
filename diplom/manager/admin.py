from django.contrib import admin

from .models import Role, Position, Status, Executors, Subdivision, Bank


admin.site.register(Role)
admin.site.register(Position)
admin.site.register(Status)
admin.site.register(Executors)
admin.site.register(Subdivision)
admin.site.register(Bank)