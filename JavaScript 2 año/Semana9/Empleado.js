class Empleado extends Persona{

    static conntarEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad)
        this._idEmpleado = ++Empleado.conntarEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get sueldo(){
        return this._sueldo;
    }

    set sueldo(sueldo){
        this._sueldo =sueldo;
    }
    
    toString(){
        return super.toString()+' '+this.idEmpleado+' '+this._sueldo;  
    }
    
}