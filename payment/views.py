import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from .tasks import payment_completed
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView

from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


# Create your views here.

# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)



#gateway = braintree.BraintreeGateway(
#    braintree.Configuration(
#        braintree.Environment.Sandbox,
#        merchant_id="5z7rt48fbyxzvx7t",
#        public_key="ryqn2zn23nrhb2g9",
#        private_key="74e35f96cada0ebf9a9ddb303ec90aff"
#    )
#)


def payment_process(request):
    
    order_id = request.session.get('order_id')
    #cou = request.session.get('own')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce':nonce,
            'options':{
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order has paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            #launch asynchronous task




            #orders = Order.objects.get(id=order_id)
            # create invoice e-mail
            subject = f'Publisher - EE invoice no. {order.id}'
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject,
                         message,
                         'settings.EMAIL_EMAIL_USER',
                         [order.email])
                         
        
            #generate PDF
            html = render_to_string('orders/order/pdf.html', {'order':order})
            out = BytesIO()
            d = "css/pdf.css"
            stylesheets = [weasyprint.CSS(settings.STATIC_ROOTSS + "css/pdf.css")]
            weasyprint.HTML(string=html).write_pdf(out,
                                                stylesheets=stylesheets)
            #attach PDF file
            email.attach(f'order_{order.id}.pdf',
                        out.getvalue(),
                        'application/pdf')
            #send email
            email.send()





            payment_completed.delay(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        #generate token
        client_token = gateway.client_token.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token,
                       })


def payment_done(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'payment/done.html', {'order':order})
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

