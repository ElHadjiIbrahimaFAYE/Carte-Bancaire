from mesclasses.algoLuhn import algoLuhn
from mesclasses.IVerificateur import IVerificateur


class VisaVerif(IVerificateur):
    def VerifCarte(self, cardNumber):
        if(len(cardNumber)==15 & (cardNumber.startwith(14) | cardNumber.startwith(14))):
            algoLuhn(cardNumber)
        print("C'est une carte Visa")
        print("Carte invalide")