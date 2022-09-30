PasseOrdonneA = 0
while PasseOrdonneA == 0 :
    try:
        PointAa = int(input("Point A abscisse : ")) 
        if PointAa == int(PointAa):
            PasseOrdonneA = 1
    except ValueError:
        print('IL FAUT ENTRER UN NUMERO')

if PasseOrdonneA == 1:
    print("2")
