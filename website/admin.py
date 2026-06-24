from django.contrib import admin
from website.models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_display = ('name', 'created_date', 'email')
    list_filter = ('email',)
    search_fields = ['name', 'message']

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)