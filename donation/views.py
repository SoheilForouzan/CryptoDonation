from django.shortcuts import render
from bitcoinlib.wallets import Wallet
import qrcode
from PIL import Image
from PIL import ImageDraw
from eth_account import Account
import secrets

# BTC


def BTCDonation(request):
    # generate a btc wallet with bitcoinlib
    wallet = Wallet.create(f'{secrets.token_hex(32)}')
    key1 = wallet.get_key()
    address = key1.address

    # Generate a payment request with qrcode
    payment_request = "bitcoin:" + address + "?amount=0.01"
    qrmake = qrcode.make(payment_request)
    qrmake.save('donation/static/donation/btcs.png')
    qrpath = f'static/donation/btcs.png'

    # Generate a transaction

    # destination = "bc1qklqkjy8d79gdnkeagwtykeh2ejdadrar3pr46x"
    # tx = wallet.send_to(destination, 0.01)

    context = {
        'address': address,
        'qrcode': qrpath,
    }

    return render(request, 'donation/test.html', context)


# ETH
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

    # Generate a transaction

    # destination = "0x00bf6C66241897CB5E3d3819f3B87240453e86D3"
    # tx = Transaction(
    #     nonce=0,
    #     gas_price=10000000000,
    #     gas=21000,
    #     to=destination,
    #     value=10000000000,
    #     data=b'',
    #     chain_id=1
    # )
    # tx.sign(private_key)
    # tx_signed = tx.raw

    context = {
        'qrcode': qrpath,
        'address': address,
    }

    return render(request, 'donation/test.html', context)


# USDT
def USDTDonation(request):
    # Generate a usdt wallet address for the user
    wallet = Wallet.create(f'{secrets.token_hex(32)}')
    key1 = wallet.get_key()
    address = key1.address

    # Generate a payment request with qrcode
    payment_request = "ethereum:" + address + "?amount=0.01"
    qrmake = qrcode.make(payment_request)
    qrmake.save('donation/static/donation/usdts.png')
    qrpath = f'static/donation/usdts.png'

    # Generate a transaction

    # destination = "0x00bf6C66241897CB5E3d3819f3B87240453e86D3"
    # tx = Transaction(
    #     nonce=0,
    #     gas_price=10000000000,
    #     gas=21000,
    #     to=destination,
    #     value=10000000000,
    #     data=b'',
    #     chain_id=1
    # )
    # tx.sign(private_key)
    # tx_signed = tx.raw

    context = {
        'qrcode': qrpath,
        'address': address,
    }

    return render(request, 'donation/test.html', context)
