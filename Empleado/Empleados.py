class Empleado:
    #aqui va el codigo de empleado
    """"------------------------------------------------
    #Atributos
    ------------------------------------------------"""
    nombre= ""
    apellido=""
    """-----------------------------------------
    # 1 = masculino y 2 femenino
    ------------------------------------------"""
    sexo= 0
    salario= 0
    
    """-----------------------------------------
    #metodos
    -----------------------------------------"""
    
    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo del metodo 
        return 0
        
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va el codigo del nuevo empleado 
        return None
    
    def ConsultarSalario(self):
        # Aqui va el codigo de metodo 
        return self.salario 
    
    def ConsultarNombre(self):
        return self.nombre
    
    def ConsultarApellido(self): 
        return self.apellido
    
    def ColsultarNombreCompleto(self):
        return self.nombre +" "+ self.apellido
    