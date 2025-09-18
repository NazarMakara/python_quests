from models import Antibiotic, Vitamin, Vaccine

meds = [
    Antibiotic("Амоксицилін", 10, 2.5),
    Vitamin("Вітамін C", 20, 0.8),
    Antibiotic("Азитроміцин", 15, 3.0),
    Vaccine("Грипова вакцина", 5, 12.0),
    Vitamin("Вітамін D", 30, 1.2),
]

for i in meds:
    print(i.info())