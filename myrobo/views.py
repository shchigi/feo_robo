from robokassa.signals import result_received
# from myrobo.models import Order
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from robokassa.forms import RobokassaForm


def pay_with_robokassa(request, id):
    # order = get_object_or_404(Order, pk=order_id)

    form = RobokassaForm(initial={
               'OutSum': 10,
               'InvId':id,
               'Desc': 'Temp_description',
               'Email': 'denis.shchigelsky@gmail.com',
               'IncCurrLabel': '',
               'Culture': 'ru'
           })

    return render(request, 'pay_with_robokassa.html', {'form': form})


# def payment_received(sender, **kwargs):
#     order = Order.objects.get(id=kwargs['InvId'])
#     order.status = 'paid'
#     order.paid_sum = kwargs['OutSum']
#     order.extra_param = kwargs['extra']['my_param']
#     order.save()
#
# result_received.connect(payment_received)