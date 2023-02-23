class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            if self.canal <= 100:
                self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            if self.canal > 1:
                self.canal -= 1

# tv = TV()
# print("A TV está ligada? {}" .format(tv.ligada))
# tv.power()
# print("A TV está ligada? {}" .format(tv.ligada))
# tv.power()
# print("A TV está ligada? {}" .format(tv.ligada))
#
# print("Canal atual: {}" .format(tv.canal))
# tv.aumenta_canal()
# tv.aumenta_canal()
# print("Canal atual: {}" .format(tv.canal))
# tv.diminui_canal()
# tv.diminui_canal()
# print("Canal atual: {}" .format(tv.canal))
# tv.diminui_canal()
# print("Canal atual: {}" .format(tv.canal))