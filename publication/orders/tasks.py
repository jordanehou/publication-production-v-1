from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
        task to sends and email notifications
        when an order is successfully created
    """

    order = Order.objects.get(id=order_id)
    #course = order.items.all
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          #'admin@publication.com',
                          #'publication788@gmail.com',
                          'settings.EMAIL_EMAIL_USER',
                          [order.email],
                          fail_silently=False)
    return mail_sent
