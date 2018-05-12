class Encapsulada:

    atributo_visible = 'soy visible'
    _atributo_protegido = 'soy protegido'
    __atributo_privado = 'soy un atributo privado'

    def get_atributo_privado(self):
        return self.__atributo_privado

    def set_atributo_privado(self, cambio):
        self.__atributo_privado = cambio
