from django.shortcuts import render
from bitcoin import *
import qrcode
from PIL import Image
from PIL import ImageDraw
from eth_account import Account
import secrets

def BTCDonation(request):
    # generate a btc wallet address for the user
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)

    # generate a payment request with qrcode
    payment_request = "bitcoin:" + address + "?amount=0.01"
    qrmake = qrcode.make(payment_request)
    qrmake.save('donation/static/donation/btcs.png')
    qrpath = f'static/donation/btcs.png'  

    
    context = {
        'qrcode': qrpath,
        'address': address,
    }

    return render(request, 'donation/test.html', context)

def ETHDonation(request):
    # Generate a eth wallet address for the user
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    address = acct.address
    
    # Generate a payment request with qrcode
    payment_request = "ethereum:" + address + "?amount=0.01"
    qrmake = qrcode.make(payment_request)
    qrmake.save('donation/static/donation/eths.png')
    qrpath = f'static/donation/eths.png'

    context = {
        'qrcode': qrpath,
        'address': address,
    }

    return render(request, 'donation/test.html', context)