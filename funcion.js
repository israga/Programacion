//Fecha: 2025-08-05
//Autor: Ismael Racines
//Tema: Funciones

function Saludos()
{
    const edad=30
    nombre="Ismael Racines"
    console.log(`Hola ${nombre}, tu edad es ${edad}`)
}

function MensajeDeBienvenida(nombre, msj, edad)
{
    if(edad >=18)
    return`Bienvenidos ${nombre} a nuestra discoteca. ${msj}!`
else
    return `Hola ${nombre}, no puedes entrar en este sitio. ${msj}!`
}

const Cuadrado = function(num)
{
    return num*num;
}

const Espar=(num)=>{
    if(num%2==0)
        return true
    else
        return false
}



//Llamando a la funcion
Saludos()
const x = MensajeDeBienvenida("Ismael", "Disfruta tu dia", 22)
console.log(x)

const y = MensajeDeBienvenida("Jeremy", "Quedate en casa", 17)
console.log(y)

console.log("El cuadrado es ", Cuadrado(9))
const res = Cuadrado(Cuadrado(6)) * 1000
console.log("El resultado es ", res)


let n=10
if(Espar(n))
    console.log(`${n} es par`)
else
    console.log(`${n} es impar`)