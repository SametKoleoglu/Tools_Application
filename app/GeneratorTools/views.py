from django.shortcuts import render


#Paypay Payment Link Generator
def PayPalPaymentLinkGenerator(request):
    pass


#Signature Creator
def SignatureCreator(request):
    return render(request, 'GeneratorTools/SignatureCreator.html')