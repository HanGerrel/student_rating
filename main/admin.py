from django.contrib import admin
import main.models as models


admin.site.register(models.Faculty)
admin.site.register(models.Rating)
admin.site.register(models.ExtraPoint)
admin.site.register(models.Sertificate)
admin.site.register(models.InviteKey)