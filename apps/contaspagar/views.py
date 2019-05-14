import io

import xlwt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from xhtml2pdf import pisa

from apps.contaspagar.forms import ContasPagarForm
from apps.contaspagar.models import ContasPagar
from apps.pessoal.models import Familia


class CreateContasPagar(CreateView):
    model = ContasPagar
    form_class = ContasPagarForm

    def get_form_kwargs(self):
        kwargs = super(CreateContasPagar, self).get_form_kwargs()
        kwargs.update({'id': self.kwargs.get('familia_id')})
        return kwargs

    def form_valid(self, form):
        contas = form.save(commit=False)
        cooperativa_logada = self.request.user.funcionario.cooperativa
        contas.cooperativa = cooperativa_logada
        contas.save()

        return super(CreateContasPagar, self).form_valid(form)



class ListContasPagar(ListView):
    model = ContasPagar

    def get_queryset(self):
        qs = self.kwargs.get('familia_id')
        queryset = ContasPagar.objects.filter(familia_id=qs)
        return queryset

@login_required
def select(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'contaspagar/contaspagar_familia_list.html', data)


class DetailContaPagar(DetailView):
    queryset = ContasPagar.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

#Relatórios

class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio_contas_a_pagar.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Contas a Pagar')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['nome', 'descricao', 'parcela_atual', 'data_documento', 'data_pagar',
                      'valor', 'numero_parcela_total', 'status']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = ContasPagar.objects.filter(status=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.nome, font_style)
            ws.write(row_num, 1, registro.descricao,  font_style)
            ws.write(row_num, 2, registro.parcela_atual, font_style)
            ws.write(row_num, 3, registro.data_documento, font_style)
            ws.write(row_num, 5, registro.data_pagar, font_style)
            ws.write(row_num, 6, registro.valor, font_style)
            ws.write(row_num, 7, registro.numero_parcela_total, font_style)
            ws.write(row_num, 8, registro.status , font_style)
            row_num += 1

        wb.save(response)
        return response








