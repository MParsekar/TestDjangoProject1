from django.contrib import admin
from .dto.models import Sprameterdata
@admin.register(Sprameterdata)
class SprameterAdmin(admin.ModelAdmin):
    list_display = ("z01","z02","l","f","r","lt","g","c","rodd","lodd","godd","codd","reven","leven","geven","ceven","s11","s12","s13","s14","s21","s22","s23","s24","s31","s32","s33","s34","s41","s42","s43","s44","sdd11","sdd12","sdd21","sdd22","sdc11","sdc12","sdc21","sdc22","scd11","scd12","scd21","scd22","scc11","scc12","scc21","scc22", "issingleended"
    )