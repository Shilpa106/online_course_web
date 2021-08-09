from django.shortcuts import render, redirect
from courses.models import Course, Payment,UserCourse,CouponCode
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from online_courses.settings import *
# from datetime import datetime
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url='/login')
def checkout(request,slug):
    course = Course.objects.get(slug = slug)
    
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    coupon_code_message = None
    coupon = None
    order = None
    payment = None
    error = None

    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        error = "You are already Enrolled in this Course"

    except:
        pass
    
    amount = None
    if error is None:
        amount = int((course.price - (course.price * course.discount * 0.01))*100)



    if couponcode:
        # print("fdfdsfsdf",couponcode)
        try:
            coupon = CouponCode.objects.get(course=course, code=couponcode)
            amount = course.price - (course.price * coupon.discount*0.01)
            amount = int(amount) * 100
            # print("amount",amount)
            # if coupon.discount == 100:
            #     amount = 0;
        except:
            coupon_code_message = 'Invalid Coupon Code'
            print('coupon code invalid')

# if amount zero dont create payment only save enrollment object


    if amount == 0:
        userCourse = UserCourse(user = user, course = course)
        userCourse.save()
        return redirect('my-courses')
      
    if action == 'create_payment':
        
        
               
            
            currency = "INR"
            notes={
                "email" : user.email,
                "name" : f'{user.first_name}{user.last_name}'

            }
            reciept = f"Online_courses-{int(time())}"
            order = client.order.create(
                {'receipt':reciept, 
                'notes':notes,
                'amount' : amount,
                'currency':currency
                }
                )

            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()
        # print("Creating Order Object")
        # order = "Order Created"

    
    
    context = {
    "course" : course,
    "order" : order,
    "payment" : payment,
    "user" : user,
    "error" : error,
    "coupon_code_message":coupon_code_message,
    "coupon" : coupon
   
    }
    return render(request, template_name="courses/check_out.html", context=context)
        

@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        # print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True;

            userCourse = UserCourse(user=payment.user,course=payment.course)

            userCourse.save()

            payment.user_course = userCourse
            payment.save()

            return redirect('my-courses')

        except:
            return HttpResponse("Invalid payment details")

# a = time()
# print("number",a)