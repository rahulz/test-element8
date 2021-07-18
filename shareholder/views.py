# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django_tables2 import SingleTableView

from shareholder.forms import ShareHolderForm, ShareForm
from shareholder.models import ShareHolder, Share, Installment
from shareholder.tables import ShareHoldersTable, ShareTable, InstallmentTable


class ShareHoldersView(SingleTableView):
    template_name = 'shareholder/list.html'
    queryset = ShareHolder.objects.all()
    model = ShareHolder
    table_class = ShareHoldersTable


class AddShareHoldersView(CreateView):
    template_name = 'shareholder/add.html'
    form_class = ShareHolderForm
    success_url = '/'


class ShareHoldersDetailView(CreateView):
    template_name = 'shareholder/detail.html'
    form_class = ShareForm

    def get_success_url(self):
        return f"/detail/{self.kwargs['pk']}"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data()
        ctx['share'] = ShareTable(Share.objects.filter(shareholder_id=self.kwargs['pk']))
        ctx['installments'] = InstallmentTable(Installment.objects.filter(share__shareholder_id=self.kwargs['pk']))
        ctx['form'] = ShareForm
        return ctx

    def get_form_kwargs(self):
        kwargs = super(ShareHoldersDetailView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        if 'installment' in request.POST:
            Installment.objects.get(pk=request.POST.get('installment')).toggle_paid()
            return HttpResponseRedirect(request.path)
        else:
            return super().post(request, *args, **kwargs)
