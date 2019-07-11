from django.contrib import admin
#新加入的包
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.


from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(Cadmin)
class CadminAdmin(admin.ModelAdmin):
    list_display = ('clubid', 'name','pwd', 'state',)
    list_filter = ('clubid', 'name','state',)
    search_fields = ('clubid', 'name','state')
    list_display_links = ('clubid', 'name','state')
    # list_editable = ('top', 'category')
    list_per_page = 20
# class Cadmin(models.Model):
#     name = models.CharField(max_length=30)
#     pwd = models.CharField(max_length=30)
#     state = models.PositiveIntegerField()
#     clubid = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'cadmin'
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'uname','phone', 'clubid', 'gender', 'birthday','clubid', 'astate','state','upwd')
    list_filter = ('gender', 'uname','phone',)
    search_fields = ('gender', 'uname','birthday')
    list_display_links = ('uid', 'uname','clubid')
    # list_editable = ('top', 'category')
    list_per_page = 20
# class User(models.Model):
#     upwd = models.CharField(max_length=30)
#     uname = models.CharField(max_length=30)
#     uid = models.AutoField(primary_key=True)
#     state = models.IntegerField()
#     gender = models.IntegerField()
#     birthday = models.DateField()
#     phone = models.CharField(max_length=30)
#     clubid = models.IntegerField()
#     mstate = models.IntegerField()
#     astate = models.IntegerField()


