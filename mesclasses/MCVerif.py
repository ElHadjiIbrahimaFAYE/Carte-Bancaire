from mesclasses.algoLuhn import algoLuhn
from mesclasses.IVerificateur import IVerificateur


class MCVerif(IVerificateur):
    def VerifCarte(self,cardNumber):
        if (len(cardNumber) == 16 & (cardNumber.startwith(41) | cardNumber.startwith(40))):
            algoLuhn(cardNumber)
        print("C'est une carte Mastercard")
        print("Carte invalide")
