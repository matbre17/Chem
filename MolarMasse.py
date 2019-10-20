import csv

while True:
    with open ("Periodic Table.csv",mode = "r" ) as ps:
        ps_reader = csv.reader(ps)
        value = False
        variabel = str(input("Skriv inn grunnstoff: "))
        for line in ps_reader:
               if variabel.upper() == str(line[2]).upper() or variabel.upper() == str(line[1]).upper() \
                       or str(variabel.upper()) == str(line[0]):  #If og elif-statements nedenfor fikser feil data i csv fil.
                  if variabel.upper() == "SILICON" or variabel.upper() == "SI" or str(variabel.upper()) == str(14):
                      print("\n" + "Silicon" +"\nMolar Masse: 28.086 g/mol" + "\nAtomnummer: 14 \n")
                      value = True
                  elif variabel.upper() == "VANADIUM" or variabel.upper() == "V" or str(variabel.upper()) == str(23):
                      print("\n" + "Vanadium" +"\nMolar Masse: 50.942 g/mol" + "\nAtomnummer: 23 \n")
                      value = True
                  elif variabel.upper() == "MOLYBDENUM" or variabel.upper() == "MO" or str(variabel.upper()) == str(23):
                      print("\n" + "Molybdenum" +"\nMolar Masse: 95.95 g/mol" + "\nAtomnummer: 42 \n")
                      value = True

                  elif variabel.upper() == "POLONIUM" or variabel.upper() == "PO" or str(variabel.upper()) == str(84):
                      print("\n" + "Polonium" +"\nMolar Masse: 209 g/mol" + "\nAtomnummer: 84 \n")
                      value = True

                  elif variabel.upper() == str(line[2]).upper() or variabel.upper() == str(line[1]).upper() \
                       or str(variabel.upper()) == str(line[0]):
                       print("\n" + line[1]  +  "\nMolar Masse: " + str(round(float(line[3]),3)) +" g/mol"+ \
              "\nAtomnummer: " + line[0] +"\n")
                       value = True

        if value == False:
            print("\nUgyldig grunnstoff\n")







