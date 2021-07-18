from django.contrib import admin


def register(model, model_admin=admin.ModelAdmin, _exclude=None, _fields=None, _exclude_from_table=None, form=None,
             _filter_fields=None, _actions=None, _search_fields=None):
    if not _exclude_from_table:
        _exclude_from_table = []
    if not _actions:
        _actions = []
    if not _search_fields:
        _search_fields = []
    if not _filter_fields:
        _filter_fields = []

    class Admin(model_admin):
        list_select_related = True
        fields = _fields
        exclude = _exclude
        actions = _actions
        search_fields = _search_fields
        list_filter = _filter_fields

        def get_queryset(self, request):
            try:
                return self.model.all_objects.all()
            except AttributeError:
                return self.model.objects.all()

        @property
        def form(self):
            if not form:
                return super(Admin, self).form
            else:
                return form

        @property
        def list_display(self):
            return (['__str__'] + [field.name for field in model._meta.get_fields() if
                                   field.get_internal_type() not in ['ForeignKey', 'ManyToManyField']
                                   and field.name not in _exclude_from_table])

    admin.site.register(model, Admin)


def register_many(*args):
    for model in args:
        register(model)
