from django_tables2 import tables, LinkColumn, A, BooleanColumn, TemplateColumn

from shareholder.models import ShareHolder, Share


class ShareHoldersTable(tables.Table):
    id = LinkColumn('shareholder_detail', args={A("id")})

    class Meta:
        model = ShareHolder
        fields = ('id', 'name', 'mobile', 'email')


class ShareTable(tables.Table):
    class Meta:
        model = Share
        fields = (
            'duration', 'total_amount', 'installment_type', 'start_date', 'no_of_installments', 'installment_amount')


class InstallmentTable(tables.Table):
    paid = BooleanColumn()
    action = TemplateColumn(verbose_name='Action',
                            template_name='shareholder/installment_action.html',
                            orderable=False)  # orderable not sortable

    class Meta:
        model = Share
        fields = ('date', 'amount', 'paid', 'action')
