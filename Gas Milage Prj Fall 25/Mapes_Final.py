#Imports
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""Citations
@Article{         harris2020array,
 title         = {Array programming with {NumPy}},
 author        = {Charles R. Harris and K. Jarrod Millman and St{\'{e}}fan J.
                 van der Walt and Ralf Gommers and Pauli Virtanen and David
                 Cournapeau and Eric Wieser and Julian Taylor and Sebastian
                 Berg and Nathaniel J. Smith and Robert Kern and Matti Picus
                 and Stephan Hoyer and Marten H. van Kerkwijk and Matthew
                 Brett and Allan Haldane and Jaime Fern{\'{a}}ndez del
                 R{\'{i}}o and Mark Wiebe and Pearu Peterson and Pierre
                 G{\'{e}}rard-Marchant and Kevin Sheppard and Tyler Reddy and
                 Warren Weckesser and Hameer Abbasi and Christoph Gohlke and
                 Travis E. Oliphant},
 year          = {2020},
 month         = sep,
 journal       = {Nature},
 volume        = {585},
 number        = {7825},
 pages         = {357--362},
 doi           = {10.1038/s41586-020-2649-2},
 publisher     = {Springer Science and Business Media {LLC}},
 url           = {https://doi.org/10.1038/s41586-020-2649-2}
}
@Article{Hunter:2007,
  Author    = {Hunter, J. D.},
  Title     = {Matplotlib: A 2D graphics environment},
  Journal   = {Computing in Science \& Engineering},
  Volume    = {9},
  Number    = {3},
  Pages     = {90--95},
  abstract  = {Matplotlib is a 2D graphics package used for Python for
  application development, interactive scripting, and publication-quality
  image generation across user interfaces and operating systems.},
  publisher = {IEEE COMPUTER SOC},
  doi       = {10.1109/MCSE.2007.55},
  year      = 2007
}
Geeks for Geeks
Dining Hall Cookies
"""

#Code
def open_list(IO):     #Making a function to open 
    L = []
    Q = []
    with open(IO, "r") as heck:
        M = heck.read().split('\n')     #opens file, reads it as a string, splits it by line to a [list of strings]
        M.pop(0)                        #pops header
        dt = []
        mlg = []
        dis = []
        pr = []
        gal = []
        
        for x in M:                     #splits strings in list into [[list],[of],[strings]]
            h = x.split(',')
            L.append(h)
        
        
        for x in L:                     #strips out unessisary characters and puts into a new list
            P = []
            for y in x:
                O = y.strip("$ ")
                P.append(O)
            Q.append(P)
        Q.pop(-1)

        for x in Q:                     #splits data into its own lists
            dt.append(x[0])
            mlg.append(x[1])
            dis.append(x[2])
            pr.append(x[3])
            gal.append(x[4])

        ate = []
        for x in dt:                                        #Makes each entry a numpy array
            y = datetime.datetime.strptime(x, '%m/%d/%Y')
            z = np.datetime64(y)
            ate.append(z)
                                                                #ate is a list of matplot date objects
        mlg = np.array(mlg).astype(float)                       #the rest are floats
        dis = np.array(dis).astype(float)
        pr = np.array(pr).astype(float)
        gal = np.array(gal).astype(float)

    return(ate, mlg, dis, pr, gal)                

def Money_gallon(A):                                            #Calculates the Price per gallon of gas
    a,b,c,d,e = open_list(A)
    price = []
    index = 0

    for x, y, z in zip(c,d,e):
        mon = ((x*z)+y)/z
        price.append(round(mon, 2))

    
    fig, ax = plt.subplots(layout='constrained')                #Shows the change of price of gas over time
    ax.plot(a, price)
    ax.set_title("Price of gas over the years")
    ax.set_ylabel("$")
    plt.show()


    return()

def milage(A):                                                  #Calculates the miles per gallon
    a,b,c,d,e = open_list(A)

    car = []
    i1 = 0
    i2 = 1
    while i2 < len(b):                                          #Uses the difference of the current element and the next element for the miles traveled.
            mi = (b[i2] - b[i1]) / e[i2]
            i1 = i1+1
            i2 = i2+1
            car.append(mi)
    num = float()

    num = np.average(car)

    num = round(num, 3)

    return(num)


#Initializing the files so they're easily replacable
A = str(r"C:\Users\Tessa\OneDrive\Desktop\CSCI 3603\Mapes_Final_Project\Gas - F150.csv")
B = str(r"C:\Users\Tessa\OneDrive\Desktop\CSCI 3603\Mapes_Final_Project\Gas - GMC Terrain.csv")

print("The average milage of my 2008 Ford F-150 is: ", milage(A))
print("The average milage of my 2018 GMC Terrain is: ", milage(B))

print(Money_gallon(A))
print(Money_gallon(B))

