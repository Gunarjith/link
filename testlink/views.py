from django.http import HttpResponse
import requests



def home(request):

    url = "https://test.cashfree.com/api/v1/order/create"

    payload = {
        "appid": "TEST3931154d6e90b54bfbc3b4946d511393",
        "secretKey": "TEST701a10a8d7389d719903c77dda9fa993fbc0db63",
        "orderId": "order_id_new_013113939",
        "orderAmount": "1",
        "orderCurrency": "INR",
        "oderNote": "pay",
        "customerName": "mohan",
        "customerEmail": "abcd@gmail.com",
        "customerPhone": "8494863493",
        # "returnUrl": "https://cashfree.com",

         "notifyUrl": "http://127.0.0.1:8000/payment_info/",
    }

    response = requests.request("POST", url, data=payload)
    print(response.text)

    return HttpResponse("link generated successfully")

def payment_info(request):
    print("mogan")
    print("gowda")
    if request.method == 'POST':
        payment_data = request.POST  # Retrieve the payment data sent by Cashfree
        print(payment_data)
    return HttpResponse("payment information has been successfully fetched")
