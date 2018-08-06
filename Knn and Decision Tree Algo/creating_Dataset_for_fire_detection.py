import xlwt
from random import randint
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "CO")
sheet1.write(0, 1, "CO2")
sheet1.write(0, 2, "Temperature")
sheet1.write(0,3,"Smog")
sheet1.write(0,4,"class_label")


for i in range(1,20000):
    co=randint(3,35) #below 10 normal above 35 very danger
    co2=randint(350,3000) #below 1000 normal above 1500 danger
    temperature=randint(1,500) #abve 400 danger fire is there
    smog=randint(0,500) #above 200 unhealthy and danger range 100 to 200 unhealthy below 100 moderate
    sheet1.write(i,0,co)
    sheet1.write(i,1,co2)
    sheet1.write(i,2,temperature)
    sheet1.write(i,3,smog)
    if co>=30:
        if co2>=1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
        elif 1000<=co2<1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
        else:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
    elif 10<=co<30:
        if co2>=1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
        elif 1000<=co2<1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
        else:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
    else:
        if co2>=1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                elif 100<=smog<200:   
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                if smog>=200:
                    sheet1.write(i,4,"No Fire")
                else:
                    sheet1.write(i,4,"No Fire")
        elif 1000<=co2<1500:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                sheet1.write(i,4,"No Fire")
            else:
                sheet1.write(i,4,"No Fire")
        else:
            if temperature>=350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"May Be Fire")
            elif 100<=temperature<350:
                if smog>=200:
                    sheet1.write(i,4,"May Be Fire")
                else:
                    sheet1.write(i,4,"No Fire")
            else:
                sheet1.write(i,4,"No Fire")
book.save("random_data.xls")