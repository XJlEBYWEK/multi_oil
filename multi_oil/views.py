import telebot
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import News, Stocks
from .serializers import NewsSerializer, StocksSerializer
import json
import requests

TOKEN = "1676155536:AAFRozMpefP9nHWAhKhLHrrzNHd1afc07Xk"
CHANNEL_NAME_1 = -1001405418274
CHANNEL_NAME_2 = -1001439028729

bot = telebot.TeleBot(TOKEN)


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = json.loads(requests.get("https://app.multioil.in.ua/gas/api/v1/pricelist/stels").text)
        for azs in response:
            name = azs['fuelName']
            azs.pop('fuelName')
            name = name.replace(" ", "_")
            name = name.replace("-", "_")

            context[name] = azs
        return context


class TermsPageView(TemplateView):
    template_name = "terms.html"


class BuisinnessPageView(TemplateView):
    template_name = "business.html"


class ForAzsPageView(TemplateView):
    template_name = "multioilForAzs.html"


class stocksTestForBenefitView(TemplateView):
    template_name = "stocksTestForBenefit.html"


class StocksView(TemplateView):
    template_name = "stocks.html"


class stocksJustInstallView(TemplateView):
    template_name = "stocksJustInstall.html"


class PolicyPageView(TemplateView):
    template_name = "privacy-policy.html"


class MultiBuisinnessPageView(TemplateView):
    template_name = "multioilBusiness.html"


class FaqPageView(TemplateView):
    template_name = "faq.html"


def set_message(request):
    """Отправка собщения из формы стать партнером"""

    inputCompany = request.POST.get('inputCompany', False)
    inputIpn = request.POST.get('inputIpn', False)
    inputName = request.POST.get('inputName', False)
    inputPhone = request.POST.get('inputPhone', False)
    inputEmail = request.POST.get('inputEmail', False)
    textarea = request.POST.get('textarea', False)

    text = f"Стать партнёром\n" \
           "--------------------------------------\n" \
           f"Название компании: {inputCompany}\n" \
           f"ИПН: {inputIpn}\n" \
           f"Контактное лицо: {inputName} \n" \
           f"Номер телефона: {inputPhone} \n" \
           f"Email: {inputEmail} \n" \
           f"Текстовое сообщение: {textarea} \n"

    # bot.send_message(CHANNEL_NAME_1, text)
    return redirect('/')


def set_phone_form(request):
    """Отправка номера телефона из формы получить ссылку"""

    inputPhone = request.POST.get('inputPhone', False)
    text = f"Получить ссылку\n" \
           "--------------------------------------\n" \
           f"Номер телефона: {inputPhone}\n"

    # bot.send_message(CHANNEL_NAME_2, text)
    return redirect('/')


def set_return_form(request):
    """Отправка собщения из формы оформления возврата"""

    inputCompany = request.POSTNewsSerializer.get('inputCompany', False)
    inputSeries = request.POST.get('inputSeries', False)
    dataD = request.POST.get('dataD', False)
    inputName = request.POST.get('issuedBy', False)
    idTranz = request.POST.get('idTranz', False)
    BeforeTurning = request.POST.get('BeforeTurning', False)
    inputPhone = request.POST.get('inputPhone', False)
    inputEmail = request.POST.get('inputEmail', False)
    textarea = request.POST.get('inputEmail', False)

    text = f"Оформить возврат\n" \
           "--------------------------------------\n" \
           f"Название компании: {inputCompany}\n" \
           f"Серия и/или номер: {inputSeries}\n" \
           f"Дата выдачи: {dataD} \n" \
           f"Кем выдано: {inputName} \n" \
           f"ID транзакции: {idTranz} \n" \
           f"Сума к возврату: {BeforeTurning} \n" \
           f"Контактный телефон: {inputPhone} \n" \
           f"Почта: {inputEmail} \n" \
           f"Текстовое сообщение: {textarea} \n"

    # bot.send_message(CHANNEL_NAME_1, text)
    return redirect('/')


# ----------- NEWS ------------

class GetNewsListView(ListAPIView):
    """Список всех новостей"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class GetNewsPageView(TemplateView):
    """Страница со всеми новостями"""

    template_name = "news.html"

    def get_context_data(self, **kwargs):
        new = News.objects.all()[:2]
        context = super().get_context_data(**kwargs)
        context["news"] = NewsSerializer(new, many=True).data
        return context


class GetNewsView(TemplateView):
    """Страница новости"""

    # template_name = "news.html"

    def get_context_data(self, **kwargs):
        new = News.objects.get(pk=self.kwargs['pk'])
        data = NewsSerializer(new).data
        context = super().get_context_data(**kwargs)

        for value in data:
            context[value] = data[value]
        return context

# ----------- STOKS -------------

class GetStocksPageView(TemplateView):
    """Страница со всеми акциями"""

    template_name = "stocks.html"

    def get_context_data(self, **kwargs):
        new = Stocks.objects.all()
        context = super().get_context_data(**kwargs)
        context["stocks"] = StocksSerializer(new, many=True).data
        return context


class GetStocksView(TemplateView):
    """Страница акции"""

    template_name = "example_head.html"

    def get_context_data(self, **kwargs):
        new = Stocks.objects.get(name_url=self.kwargs['name_url'])
        data = StocksSerializer(new).data
        context = super().get_context_data(**kwargs)

        for value in data:
            context[value] = data[value]
        print(context)
        return context
