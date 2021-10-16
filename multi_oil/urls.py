"""main_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "multi_oil"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('faq', views.FaqPageView.as_view(), name='faq-page'),
    path('stocks', views.GetStocksPageView.as_view(), name='stocks'),

    # path('stocks', views.StocksView.as_view(), name='stocks'),
    path('business', views.BuisinnessPageView.as_view(), name='business'),
    path('multioil-for-azs', views.ForAzsPageView.as_view(), name='multioil-for-azs'),
    path('multioil-business', views.MultiBuisinnessPageView.as_view(), name='multioil-business'),

    path('stock/just_install', views.stocksJustInstallView.as_view(), name='stock-install'),
    path('stock/test_for_benifit', views.stocksTestForBenefitView.as_view(), name='stock-test'),
    path('policy', views.PolicyPageView.as_view(), name='policy-page'),
    path('terms', views.TermsPageView.as_view(), name='terms-page'),
    path('set_form', views.set_message),
    path('set_phone_form', views.set_phone_form),
    path('set_return_form', views.set_return_form),

    path('news', views.GetNewsPageView.as_view(), name="get-news-page"),
    # path("news/<int:pk>", views.GetNewsView.as_view(), name="get-news"),
    path('api/news', views.GetNewsListView.as_view(), name="get-news-list"),
    # path('stocks_test', views.GetStocksPageView.as_view(), name="get-stocks-page"),

]
