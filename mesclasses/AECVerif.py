from mesclasses.algoLuhn import algoLuhn
from mesclasses.IVerificateur import IVerificateur


class AECVerif(IVerificateur):
        def VerifCarte(self, cardNumber):
            if (len(cardNumber) == 17 & (cardNumber.startwith(39) | cardNumber.startwith(30))):algoLuhn(cardNumber)
            print("C'est une carte American Express")
            print("Carte invalide")