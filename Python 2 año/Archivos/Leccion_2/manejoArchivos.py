class manejoArchivos:
    def init(self, nombre):
        self.nombre = nombre

    def enter(self):
        print('Obtenemos el recurso'.center(50, '_'))
        self.nombre = open(self.nombre, 'r', encoding='utf8') # Encapsulamos el codigo dentro del metodo
        return self.nombre

    def exit(self, tipo_exception, valor_exception, trazaerror):
        print('Cerramo el recurso'.center(50, ''))
        if self.nombre:
            self.nombre.close() # cerramos el archivo