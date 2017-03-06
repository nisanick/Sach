from dama import Dama
from event import PohniEvent, VysledokEvent
from jazdec import Jazdec
from kral import Kral
from pesiak import Pesiak
from strelec import Strelec
from veza import Veza

__author__ = 'hudec29'

CONST_BIELA = 1
CONST_CIERNA = 2


class Sachovnica:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.figurky = []
        self.posledna = None
        self.resetni_sachovnicu()

    def notify(self, event):
        if isinstance(event, PohniEvent):
            vysledok = self.posun_figurku(event.odkial, event.kam)
            self.event_manager.post(VysledokEvent(vysledok))

    def resetni_sachovnicu(self):
        for i in range(1,9):
            self.pridaj_figurku(Pesiak(i, CONST_BIELA))
            self.pridaj_figurku(Pesiak(i, CONST_CIERNA))

        self.pridaj_figurku(Veza(1, CONST_BIELA))
        self.pridaj_figurku(Veza(8, CONST_BIELA))

        self.pridaj_figurku(Veza(1, CONST_CIERNA))
        self.pridaj_figurku(Veza(8, CONST_CIERNA))

        self.pridaj_figurku(Jazdec(2, CONST_BIELA))
        self.pridaj_figurku(Jazdec(7, CONST_BIELA))

        self.pridaj_figurku(Jazdec(2, CONST_CIERNA))
        self.pridaj_figurku(Jazdec(7, CONST_CIERNA))

        self.pridaj_figurku(Strelec(3, CONST_BIELA))
        self.pridaj_figurku(Strelec(6, CONST_BIELA))

        self.pridaj_figurku(Strelec(3, CONST_CIERNA))
        self.pridaj_figurku(Strelec(6, CONST_CIERNA))

        self.pridaj_figurku(Kral(CONST_BIELA))

        self.pridaj_figurku(Kral(CONST_CIERNA))

        self.pridaj_figurku(Dama(CONST_BIELA))

        self.pridaj_figurku(Dama(CONST_CIERNA))

    def pridaj_figurku(self, figurka):
        "pridava figurku na sachovnicu"
        self.figurky.append(figurka)

    def posun_figurku(self, z, na):
        """posunie figurku zo zadanej suradnice na zadanu suradnicu
        ak sa posunutie z nejakeho dovodu nepodari, vracia false"""
        x_z, y_z = self.prepocitaj_hodnotu(z)
        x_na, y_na = self.prepocitaj_hodnotu(na)
        for figurka in self.figurky:
            if figurka.x == x_z and figurka.y == y_z:

                #ak je to pre figurku platny tah
                if figurka.je_tah_povoleny(x_na, y_na):

                    #ak figurke nic nestoji v ceste
                    if self.volna_cesta(x_z, y_z, x_na, y_na):

                        #ak je cielove policko prazdne
                        if self.je_volne(x_na, y_na):
                            figurka.posun_sa(x_na, y_na)
                            self.posledna = figurka

                            #ak je figurka pesiak
                            if figurka.__class__ is Pesiak:
                                self.zmen_pesiaka()
                            return True
                        else:

                            #ak je figurka pesiak
                            if figurka.__class__ is Pesiak:
                                return False

                            #ak mozem vyhodit figurku stojacu na cielovej suradnici
                            elif self.mozem_vyhodit(x_na, y_na, figurka.farba):
                                figurka.posun_sa(x_na, y_na)
                                self.posledna = figurka
                                return True
                            return False
                    return False

                #specialne pripady pre pohyb pesiaka
                elif figurka.__class__ is Pesiak:

                    #ak je zadany tah pre vyhodenie
                    if figurka.mozem_vyhodit(x_na, y_na):

                        #ak je policko obsadene
                        if not self.je_volne(x_na, y_na):

                            #ak je na obsadenom policku superova figurka
                            if self.mozem_vyhodit(x_na, y_na, figurka.farba):
                                figurka.posun_sa(x_na, y_na)
                                self.posledna = figurka
                                self.zmen_pesiaka()
                                return True

                        #ak mozem brat mimochodom
                        elif self.mozem_brat_mimochodom(x_na, y_z):
                            figurka.posun_sa(x_na, y_na)
                            self.posledna = figurka
                            return True
                        return False
                    return False

                #specialne pripady pre pohyb krala
                elif figurka.__class__ is Kral:

                    #ak mozem vykonat rosadu
                    if self.mozem_vykonat_rosadu(x_na, y_na, figurka):
                        self.posledna = figurka
                        return True
                    else:
                        return False
                return False
        else:
            return False

    def volna_cesta(self, x_z, y_z, x_na, y_na):
        "vracia true ak medzi polickom kde stojim a cielovym polickom nestoji ziadna figurka"

        #urcenia rozsahov pre cyklus
        if x_z - x_na < 0:
            rangex = range(x_z+1, x_na)
        elif x_z - x_na > 0:
            rangex = range(x_z-1, x_na, -1)

        if y_z - y_na < 0:
            rangey = range(y_z+1, y_na)
        elif y_z - y_na > 0:
            rangey = range(y_z-1, y_na, -1)

        for figurka in self.figurky:

            #kontrola pre pohyb vo vertikalnom smere
            if x_z == x_na:
                for i in rangey:
                    if figurka.y == i and figurka.x == x_z:
                        return False

            #kontrola pre pohyb v horizontalnom smere
            elif y_z == y_na:
                for i in rangex:
                    if figurka.x == i and figurka.y == y_z:
                        return False

            #kontrola pre pohyb po diagonale
            elif abs(x_z - x_na) == abs(y_z - y_na):

                #urcenie smeru diagonaly
                if x_z - x_na < 0:
                    incx = +1
                else:
                    incx = -1
                if y_z - y_na < 0:
                    incy = +1
                else:
                    incy = -1
                x = x_z
                y = y_z

                #kontrola diagonaly
                for i in range(1,abs(y_z - y_na)):
                    x += incx
                    y += incy
                    if figurka.x == x and figurka.y == y:
                        return False
            else:
                return True
        else:
            return True

    def prepocitaj_hodnotu(self, suradnica):
        """zmeni slovnu reprezentaciu suradnice na ciselnu"""
        return ord(suradnica[0]) - 64, int(suradnica[1])

    def je_volne(self, x, y):
        "vracia true ak je cielove policko prazdne"
        for figurka in self.figurky:
            if figurka.x == x and figurka.y == y:
                return False
        return True

    def mozem_vyhodit(self, x, y, farba):
        "vracia true ak na cielovom policku stoji superova figurka"
        for figurka in self.figurky:
            if figurka.x == x and figurka.y == y and figurka.farba != farba:
                self.figurky.remove(figurka)
                return True
        return False

    #en passant
    def mozem_brat_mimochodom(self, x, y):
        """vracia true ak sa su splnene vsetky podmienky pre en passant
        x - je x-ova suradnica na ktoru chceme ist
        y - je y-nova suradnica na ktorej stojime"""


        #ak posledna tahana figurka bol pesiak
        if self.posledna.__class__ is Pesiak:

            #superov pesiak sa pohol o dve policka zo zakladnej pozicie
            if self.posledna.x == x and self.posledna.y == y:

                #superov pesiak sa pohol len raz
                if self.posledna.pohyby == 1:
                    self.figurky.remove(self.posledna)
                    return True
        return False

    def zmen_pesiaka(self):
        "zmeni pesiaka na damu, ak sa dostal na opacnu stranu hracej plochy"
        if self.posledna.y == 8 or self.posledna.y == 1:

            #nastavenie spravnych udajov pre damu
            if self.posledna.farba == 1:
                nova = Dama(1)
            else:
                nova = Dama(2)
            nova.x = self.posledna.x
            nova.y = self.posledna.y

            #odstranenie pesiaka z hry a pridanie damy na jeho poziciu
            self.figurky.remove(self.posledna)
            self.figurky.append(nova)
            self.posledna = nova

    def mozem_vykonat_rosadu(self, x_na, y_na, kral):
        "vracia true ak su splnene vsetky podmienky na vykonanie rosady"

        #kral do teraz nevykonal ziaden pohyb
        if kral.pohyby != 0:
            return False

        #musim sa pohnut po riadku na ktorom stojim
        if y_na != kral.y:
            return False

        #musim sa pohnut o dve miesta vlavo alebo vpravo
        if x_na != 3 and x_na != 7:
            return False

        #nic nemoze stat v smere cesty
        if not self.volna_cesta(kral.x, kral.y, x_na, y_na):
            return False

        #urcenie pozicie veze podla smeru rosady
        if x_na == 3:
            x = 1
        else:
            x = 8

        veza = None
        #hladanie veze v jej zakladnej pozicii. ak sa tam nenachadza skoncime
        for figurka in self.figurky:
            if figurka.x == x and figurka.y == kral.y:
                veza = figurka

        if veza == None:
            return False

        #s vezou sa zatial nemohlo hybat
        if veza.pohyby != 0:
            return False

        #nastavenie suradnice pre pohyb veze
        if x == 1:
            x = 4
        else:
            x = 6

        #cesta pre vezu musi byt volna
        if not self.volna_cesta(veza.x, veza.y, x, veza.y):
            return False

        #kral nesmie byt ohrozeny v sucastnej ani novej pozicii
        for figurka in self.figurky:
            if figurka.je_tah_povoleny(kral.x, kral.y):

                #kontrola pre ohrozenie v sucastnej pozicii
                if self.volna_cesta(figurka.x, figurka.y, kral.x, kral.y) and figurka.farba != kral.farba:
                    return False

            if figurka.je_tah_povoleny(x_na, y_na):

                #kontrola pre ohrozenie v novej pozicii
                if self.volna_cesta(figurka.x, figurka.y, x_na, y_na) and figurka.farba != kral.farba:
                    return False

        #presun krala a veze na nove pozicie
        kral.posun_sa(x_na, y_na)
        veza.posun_sa(x, y_na)
        return True