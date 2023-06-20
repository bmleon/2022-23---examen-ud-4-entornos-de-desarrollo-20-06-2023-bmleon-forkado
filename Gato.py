"""
Clase Gato.
:author: Jaime Rabasco Ronda.
:author: Belen Maria Leon Fernandez
"""
class Gato:

    def maullar(self):
        print(self.maulla());

    def maulla(self):
        return 'Miau'


g = Gato();
g.maullar();
