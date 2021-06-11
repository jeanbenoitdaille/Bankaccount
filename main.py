class Compte_bancaire:
    def __init__(self,nom="Dupond", solde=1000):
        self.nom=nom
        self.solde=solde

    def depot(self,somme) :
        self.solde +=somme
        return self.solde

    def retrait(self,somme):
        self.solde -=somme
        return self.solde

    def afficher(self):
        print ("le compte bancaire du",self.nom,"a pour solde :",self.solde)

compte1 = Compte_bancaire("Christopher",1500)
compte1.afficher()

compte1.depot(5000)
compte1.afficher()

compte1.retrait(2000)
compte1.afficher()


        