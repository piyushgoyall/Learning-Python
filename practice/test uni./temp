n = input("if you want to convert a unit enter 'u' and if you want to convert a currency enter anything - ")
if n == 'u':
    l=[['km','m',1000],['m','km',0.001],['m','cm',100],['cm','m',0.01],['m','mm',1000],['mm','m',0.001],['um','m',0.000001],['m','um',100000],['km','cm',100000],['km','mm',10000000],['km','um',1000000000],['cm','km',0.00001]]
    Quantity=input("\033[31m\033[40mEnter  Quantity:  ")
    if Quantity=='Length':
        old_unit=input("\033[33m\033[40mEnter old unit: ")
        new_unit=input("\033[34m\033[40mEnter new unit: ")
        Number=float(input("\033[32m\033[40mEnter the number: "))
        for i in l:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    m=[['kg','g',1000],['g','kg',0.001],['kg','lbs',0.45],['lbs','kg',2.22],['kg','mg',1000000],['mg','kg',0.000001],['g','mg',1000],['mg','g',0.001],['q','kg',100],['kg','q',0.01],['ton','kg',1000],['kg','ton',0.001],['q','g',100000],['g','q',0.00001],['ton','g',1000000],['g','ton',0.000001],['q','mg',100000000],['mg','q',0.0000001]]
    if Quantity=='mass':
        old_unit=input("\033[34m\033[36mEnter old unit: ")
        new_unit=input("\033[35m\033[35mEnter new unit: ")
        Number=float(input("\033[32m\033[46mEnter the number: "))
        for i in m:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    t=[['mins','sec',60],['sec','mins',0.016],['hour','min',60],['min','hour',0.016],['hour','sec',3600],['sec','hour',0.00027],['day','hour',24],['hour','day',0.041],['day','min',1440],['min','day',0.00069],['day','sec',86400],['sec','day',0.000015]]
    if Quantity=='Time':
        old_unit=input("Enter old unit: ")
        new_unit=input("Enter new unit: ")
        Number=float(input("Enter the number: "))
        for i in t:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    A=[['m2','cm2',10000],['cm2','m2',0.0001],['km2','m2',1000000],['m2','km2',0.000001],['cm2','km2',0.000000001],['km2','cm2',10000000000],['hectare','km2',0.01],['km2','hectare',100],['hectare','m2',10000],['m2','hectare',0.00001]]
    if Quantity=='Area':
        old_unit=input("Enter old unit: ")
        new_unit=input("Enter new unit: ")
        Number=float(input("Enter the number: "))
        for i in A:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    V=[['hl','l',100],['l','hl',0.01],['hl','ml',100000],['ml','hl',0.00001],['hl','cl',10000],['cl','hl',0.0001],['hl','dl',1000],['dl','hl',0.001],['hl','m3',0.1],['m3','hl',10],['hl','cm3',100000],['cm3','hl',0.00001],['m3','cm3',1000000],['cm3','m3',0.000001],['m3','l',1000],['l','m3',0.001]]
    if Quantity=='Volume':
        old_unit=input("Enter old unit: ")
        new_unit=input("Enter new unit: ")
        Number=float(input("Enter the number: "))
        for i in V:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    S=[['km/h','m/s',0.277],['m/s','km/h',3.6],['km/h','km/s',0.00027],['km/s','km/h',3600],['km/h','in/s',10.93],['in/s','km/h',0.091],['km/h','mph',0.621],['mph','km/h',1.6],['m/s','mph',2.23],['mph','m/s',0.44],['km/s','mph',2236],['mph','km/s',0.00044],['m/s','in/s',39.37],['in/s','m/s',0.025]]
    if Quantity=='Speed':
        old_unit=input("Enter old unit: ")
        new_unit=input("Enter new unit: ")
        Number=float(input("Enter the number: "))
        for i in S:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
    T=[['°C','°F',33.8],['°F','°C',-17.22],['°C','k',274.15],['k','°C',-272.15],['°F','k',255.92],['k','°F',-457.8]]
    if Quantity=='Temperature':
        old_unit=input("Enter old unit: ")
        new_unit=input("Enter new unit: ")
        Number=float(input("Enter the number: "))
        for i in T:
            if old_unit==i[0]:
                if new_unit==i[1]:
                    o=Number*i[2]
                    print(o)
else:
    from forex_python.converter import CurrencyRates

    currency = CurrencyRates()

    amount = int(input("Enter the Amount: "))

    from_curr = input("From Currency:").upper()
    to_curr = input("To Currency:").upper()

    print(from_curr, "To", to_curr, amount)

    result = currency.convert(from_curr, to_curr, amount)

    print("Conversion Amount:", result)
    
   
   
   
  currency and unit converter
