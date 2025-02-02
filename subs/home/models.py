import datetime
import random
import os
from PIL import Image
from django.db import models
from accounts.models import User, Subscriber, Employee

def pay_picture_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.or_no}{extension}"

    return f"payments/references/{new_filename}"

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='provinces')

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=100, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='municipalities')

    def __str__(self):
        return self.name

class Barangay(models.Model):
    name = models.CharField(max_length=100, unique=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='barangays')

    def __str__(self):
        return self.name

class Plan(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_description = models.CharField(max_length=200, blank=True, null=True)
    plan_up = models.IntegerField(default=0)
    plan_down = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.plan_name}"

class Modem(models.Model):
    modem_brand = models.CharField(max_length=100)
    modem_description = models.CharField(max_length=200, blank=True, null=True)
    is_gigabit = models.BooleanField(default=False, blank=True)
    modem_supplier = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['modem_brand']

    def __str__(self):
        return f"{self.modem_brand}"

class Subscription(models.Model):
    no = models.CharField(max_length=50, unique=True, editable=False)
    subscriber = models.ForeignKey(Subscriber, related_name='subs', on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(User, related_name="emps", on_delete=models.CASCADE, blank=True, null=True)
    alias = models.CharField(max_length=150, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    referred_by = models.CharField(max_length=150, blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.SET_NULL, null=True, blank=True)
    municipality = models.ForeignKey('Municipality', on_delete=models.SET_NULL, null=True, blank=True,)
    barangay = models.ForeignKey('Barangay', on_delete=models.SET_NULL, null=True, blank=True)
    purok = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    landmark = models.TextField(blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, blank=True, null=True)
    pon_no = models.CharField(max_length=10, blank=True, null=True)
    nap_no = models.CharField(max_length=10, blank=True, null=True)
    bill_schedule = models.CharField(max_length=10, choices=[("start","Start"), ("end","End"), ("others","Others")], default="start", blank=True, null=True)
    is_paid = models.BooleanField(default=False, blank=True, null=True)
    is_partial = models.BooleanField(default=False, blank=True, null=True)
    modem_serial = models.CharField(max_length=100, blank=True, null=True)
    modem = models.ForeignKey(Modem, on_delete=models.SET_NULL, blank=True, null=True)
    sub_status = models.CharField(max_length=50, choices=[("pending", "Pending"),("active", "Active"), ("warning", "Warning"), ("suspended","Suspended"),("terminated", "Terminated")], default="active" )
    sub_type = models.CharField(max_length=50, choices=[("government", "Government"), ("vendo", "Vendo"), ("residential","Residential"), ("business","Business"), ("vip","VIP"), ("test","Testing"), ("employee", "Employee"),("station","Station")], default="residential" )
    date_activated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    date_terminated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    date_suspended = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    modem_username = models.CharField(max_length=50, blank=True, null=True)
    modem_password = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.no:
            self.no = self.generate_subscription_number()
        super().save(*args, **kwargs)

    def generate_subscription_number(self):
        # Corrected code: using parentheses to generate a list
        no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        # Ensure id_no is unique
        while Subscription.objects.filter(no=no).exists():
            no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        return no


    def __str__(self):
        return self.alias

class Billing(models.Model):
    billed_by = models.ForeignKey(User, related_name="billed_by", on_delete=models.SET_NULL, blank=True, null=True)
    collector = models.ForeignKey(User, related_name="collector", on_delete=models.SET_NULL, blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    amount_due = models.FloatField(default=0.00)
    billing_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_partial = models.BooleanField(default=False)
    bill_schedule = models.CharField(max_length=10, choices=[("start","Start"), ("end","End"), ("others","Others")], default="start", blank=True, null=True)
    bill_type = models.CharField(max_length=10, choices=[("net","Internet"), ("foc","FOC"), ("labor","Labor"),("others","Others")], default="net", blank=True, null=True)
    notice = models.CharField(max_length=50, choices=[("disconnection", "Disconnection"), ("updated", "Updated"),("disconnected","Disconnected"),("warning","Warning")], default="updated")
    remarks = models.CharField(max_length=200, blank=True, null=True)
    billing_no = models.CharField(max_length=15, unique=True, editable=False)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-billing_date',]

    def __str__(self):
        return f"Billing {self.billing_no}"

    def save(self, *args, **kwargs):
        if not self.billing_no:
            self.billing_no = self.generate_billing_number()
        super().save(*args, **kwargs)

    def generate_billing_number(self):
        # Corrected code: using parentheses to generate a list
        billing_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        # Ensure id_no is unique
        while Billing.objects.filter(billing_no=billing_no).exists():
            billing_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        return billing_no
    
class Payment(models.Model):
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    bill_no = models.ForeignKey(Billing, related_name='payments', on_delete=models.SET_NULL, blank=True, null=True)
    amount_paid = models.FloatField(default=0.00)
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_partial = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    or_no = models.CharField(max_length=15, unique=True, editable=True)
    or_ref_no = models.CharField(max_length=10, blank=True, null=True)
    payment_type = models.CharField(max_length=10, choices=[("cash","Cash"),("cheque","Cheque"),("gcash","GCash"),("maya","Maya"),("bank","Bank")], default="cash")
    cheque_no = models.CharField(max_length=50, blank=True, null=True)
    reference_no = models.CharField(max_length=50, blank=True, null=True)
    reference_picture = models.ImageField(upload_to=pay_picture_path, default="default.jpg", blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.or_no}"

    def save(self, *args, **kwargs):
        if not self.or_no:
            self.or_no = self.generate_or_number()
        super().save(*args, **kwargs)

        # if self.reference_picture:
        #     picture_path = self.reference_picture.path
        #     img = Image.open(picture_path)

        #     img = img.convert("RGB")
        #     img = img.resize((200, 200), Image.Resampling.LANCZOS)

        #     img.save(picture_path, format='JPEG', quality=90)

        # Update related Billing and Subscription statuses
        self.update_billing_and_subscription_status()

    def generate_or_number(self):
        # Corrected code: using parentheses to generate a list
        or_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        # Ensure id_no is unique
        while Payment.objects.filter(or_no=or_no).exists():
            or_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        return or_no

    def update_billing_and_subscription_status(self):
        # Update Billing Status
        if self.bill_no:
            billing = self.bill_no
            payments = Payment.objects.filter(bill_no=billing, is_cancelled=False)  # Exclude canceled payments

            total_paid = sum(payment.amount_paid for payment in payments)
            billing.is_paid = total_paid >= billing.amount_due
            billing.is_partial = 0 < total_paid < billing.amount_due
            billing.save()

        # Update Subscription Status
        if self.subscription:
            subscription = self.subscription
            all_bills = Billing.objects.filter(subscription=subscription)

            # is_fully_paid = all(all_bills.filter(is_paid=True).exclude(is_cancelled=True).values_list('is_paid', flat=True))
            # has_partial_payment = any(all_bills.filter(is_partial=True).exclude(is_cancelled=True).values_list('is_partial', flat=True))

            # Check payment status of the bills (considering non-canceled payments)
            is_fully_paid = all(bill.is_paid for bill in all_bills)
            has_partial_payment = any(bill.is_partial for bill in all_bills)

            subscription.is_paid = is_fully_paid
            subscription.is_partial = not is_fully_paid and has_partial_payment
            subscription.save()
    

class Issue(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

class Ticket(models.Model):
    prepared_by = models.ForeignKey(User, related_name="prepared_by", on_delete=models.SET_NULL, blank=True, null=True)
    assigned_to = models.ForeignKey(User, related_name="assigned_to", on_delete=models.SET_NULL, blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    issue = models.ForeignKey(Issue, on_delete=models.SET_NULL, blank=True, null=True)
    ticket_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    ticket_no = models.CharField(max_length=10, unique=True, editable=False)
    priority = models.CharField(max_length=20, choices=[("low","Low"),("medium","Medium"),("high","High")], default="high")
    status = models.CharField(max_length=20, choices=[("pending","Pending"),("inprogress","In progress"),("resolved","Resolved")], default="inprogress")
    remarks = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket_no}" 
    
    def save(self, *args, **kwargs):
        if not self.ticket_no:
            self.ticket_no = self.generate_or_number()
        super().save(*args, **kwargs)

    def generate_or_number(self):
        # Corrected code: using parentheses to generate a list
        ticket_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        # Ensure id_no is unique
        while Ticket.objects.filter(ticket_no=ticket_no).exists():
            ticket_no = ''.join(str(random.randint(0, 9)) for _ in range(10))

        return ticket_no

