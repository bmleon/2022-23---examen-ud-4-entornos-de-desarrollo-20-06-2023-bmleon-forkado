"""
Clase Gato.
:author: Jaime Rabasco Ronda.
:author: Belen Maria Leon Fernandez
"""
class Gato:

    def maullar(self):
        """
        Metodo maullar
        :author: Belen Leon
        :return:
        """
        print(self.maulla());

    def maulla(self):
        """
        Metodo maulla
        :author: Belen Leon
        :return:
        """
        return 'Miau'


g = Gato();
g.maullar();
