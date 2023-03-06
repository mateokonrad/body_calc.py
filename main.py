import datetime


now = datetime.date.today()

weight = float(input("Podaj swoją wagę w kilogramach: "))
waist = float(input("Podaj obwód swojego pasa w centymetrach: "))

height = 1.93  # your height (m)
bmi = round(weight / height ** 2, 2)

with open("dane.txt", "a") as file:

    if file.tell() == 0:
        file.write("Data".ljust(12) + "Waga(kg)".ljust(12) + "Obwód pasa(cm)".ljust(17) + "BMI".ljust(12) + "\n")


    file.write(f"{now}".ljust(12) + f"{weight}".ljust(12) + f"{waist}".ljust(17) + f"{bmi}".ljust(12) + "\n")

file.close()