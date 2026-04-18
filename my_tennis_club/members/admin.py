from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  
  def full_name(self, obj):
    return f"{obj.firstname} {obj.lastname}"

  list_display = ('full_name', 'joined_date', 'phone')
  list_display_links = ('full_name',)


admin.site.register(Member, MemberAdmin)

