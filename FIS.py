from SelfFunctions import *

YearOfRelease = NumberOfFunctions = Price = 0
A_RYisCur = A_RYisRec = A_RYisEar = RYisCur = RYisRec = RYisEar = Price_RYisCur = Price_RYisRec = Price_RYisEar = 0

def Fuzzification():
    global YearOfRelease
    global RYisCur, RYisRec, RYisEar

    RYisCur = mfRYisCur(YearOfRelease)
    RYisRec = mfRYisRec(YearOfRelease)
    RYisEar = mfRYisEar(YearOfRelease)

def FuzzyInference():
    global A_RYisCur, A_RYisRec, A_RYisEar, RYisCur, RYisRec, RYisEar

    A_RYisCur = RYisCur
    A_RYisRec = RYisRec
    A_RYisEar = RYisEar

def Composition():
    global Price_RYisCur, Price_RYisRec, Price_RYisEar
    global NumberOfFunctions

    Price_RYisCur = 10000 * NumberOfFunctions
    Price_RYisRec = 1000 * NumberOfFunctions
    Price_RYisEar = 100 * NumberOfFunctions

    def Defuzzyfication():
        global Price
        Price = (A_RYisCur * Price_RYisCur + A_RYisRec * Price_RYisRec + A_RYisEar * Price_RYisEar) / (A_RYisCur + A_RYisRec + A_RYisEar)

    def Run():
        Fuzzification()
        FuzzyInference()
        Composition()
        Defuzzyfication()

    def Init():
        global YearOfRelease, NumberOfFunctions
        YearOfRelease = float(input("Year Of Release = "))
        NumberOfFunctions = float(input("Number Of Functions = "))

    def Terminate():
        global Price
        print('Price = ', Price)

    def Main():
        Init()
        Run()
        Terminate()

    if __name__=='__main__':
        Main()
