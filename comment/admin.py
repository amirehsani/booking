from django.contrib import admin
from .models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_time', 'validated_by', 'parent_comment', 'status')
    list_filter = ('validated_by', 'status')
    search_fields = ('user',)
    # TODO add a function to add ability of search through comments' bodies

    # @admin.display(description='User')
    # def get_username(self, obj):
    #     return obj.user.username


admin.site.register(HotelComment, CommentAdmin)
admin.site.register(HotelRoomComment, CommentAdmin)
admin.site.register(ResidentialComment, CommentAdmin)
admin.site.register(AirlineComment, CommentAdmin)
admin.site.register(AirportComment, CommentAdmin)
