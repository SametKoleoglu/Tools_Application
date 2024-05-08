from django.urls import path
from . import views

urlpatterns = [
    path('paypalPaymentLinkGenerator', views.PayPalPaymentLinkGenerator, name='paypal_payment_link_generator'),
    path('signatureCreator', views.SignatureCreator, name='signature_creator'),
]
