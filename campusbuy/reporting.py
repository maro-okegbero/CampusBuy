from openpyxl import Workbook
from .models import *


def report():
    filename = "users.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Users and Phone_numbers"
    sheet["A1"] = "Names"
    sheet["B1"] = "Phone_Numbers"

    adverts = Advert.objects.all()
    for i in range(1, Advert.objects.count()):
        for advert in adverts:
            i = i+1
            sheet[f"A{i}"] = advert.Seller_Name
            sheet[f"B{i}"] = advert.Phone_Number

    workbook.save(filename=filename)




