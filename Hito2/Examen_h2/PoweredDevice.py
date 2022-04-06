class PoweredDevice:
    modelo = None
    marca = None
    wifi = None
    lan = None
    usb = None

    def __init__(self, modelo, marca, wf, lan, usb):
        self.modelo = modelo
        self.marca = marca
        self.wifi = wf
        self.lan = lan
        self.usb = usb

    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Modelo: {self.modelo}  \nMarca: {self.marca} \nWifi: {self.wifi} \nLan: {self.lan} \nUsb: {self.usb} \n'

    def encender(self):
        print("Se ha encendido")

    def apagar(self):
        print("Se ha apagado")

PoweredDevice1 = PoweredDevice('L3150','EPSON','EpsonSeries','UTP','2')
print(PoweredDevice1)
PoweredDevice1.encender()

class Scanner(PoweredDevice):
        tipoVidrio = None
        Botones = None

        def __init__(self, modelo, marca, wf, lan, usb, tipo, btn):
            PoweredDevice.__init__(self, modelo, marca, wf, lan, usb)
            self.tipoVidrio = tipo
            self.Botones = btn

        def __str__(self):  ## \n salto de linea --> alt+92 = \
            return f'TipoVidro: {self.tipoVidrio}  \nBotones: {self.Botones} \n'

        def Scanear(self):
            print("Ha iniciado el scaneo")

Scanner1 = Scanner('Scan1','SacnnerpRo','NO','SI','SI','VidrioTipo1','Cuatro')
print(Scanner1)
Scanner1.Scanear()


class Printer(PoweredDevice):
    tipoHojas = None
    Funciones = None

    def __init__(self, modelo, marca, wf, lan, usb, tipo, fun):
        PoweredDevice.__init__(self, modelo, marca, wf, lan, usb)
        self.tipoHojas = tipo
        self.Funciones = fun

    def __str__(self):  ## \n salto de linea --> alt+92 = \
        return f'TipoHojas: {self.tipoHojas}  \nFunciones: {self.Funciones} \n'

    def Imprimir(self):
        print("Ha iniciado las impresiones")


Printer1 = Printer('Printeer1', 'PrintpRo', 'SI', 'SI', 'SI', 'Carta-Oficio', 'B/N-Color')
print(Printer1)
Printer1.Imprimir()


class Copier(PoweredDevice):
    cantiMax = None
    tipoCopia = None

    def __init__(self, modelo, marca, wf, lan, usb, canti, tipoC):
        PoweredDevice.__init__(self, modelo, marca, wf, lan, usb)
        self.cantiMax = canti
        self.tipoCopia = tipoC

    def __str__(self):  ## \n salto de linea --> alt+92 = \
        return f'Cantidad Maxima: {self.cantiMax}  \nTipoCopia: {self.tipoCopia} \n'

    def CopierBN(self):
        print("Ha iniciado la copia BN")
    def CopierColor(self):
        print("Ha iniciado la copia color")


Copier1 = Copier('Scan1', 'SacnnerpRo', 'NO', 'NO', 'NO', 'Max:1000Hojas', 'B/N-Color')
print(Copier1)
Copier1.CopierBN()
Copier1.CopierColor()

PoweredDevice1.apagar()
