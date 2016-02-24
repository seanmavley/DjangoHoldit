from django.contrib import admin
from django import forms

from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        # this is not automatically inherited from FlatpageFormOld
        model = FlatPage
        fields = ['id', 'title', 'content']


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
