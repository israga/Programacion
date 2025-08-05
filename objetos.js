/*
Fecha: 2025-08-05
Autor: Ismael Racines
Tema: Objetos
*/


const persona = {
    identificacion: "0805212677",
    apellidos: "Racines Garcia",
    nombre: "Josue Ismael",
    edad: 21,
    sexo: "Masculino"
}
const estudiante = {
    matricula:"1234",
    nombre_completo:"Ismael Racines",
    edad:21,
    pasatiempos: ["Jugar", "correr"],
    cursos:[
        { nombre: "Base de datos", horas:3, notafinal:45 },
        { nombre: "Programacion", horas:2, notafinal:40 },
        { nombre: "Matematicas", horas:9, notafinal:33 },
        { nombre: "Fisica", horas:5, notafinal:38 }
    ]  
}
console.log("Objeto persona ", persona)
console.log("Nombre del estudiamte ", estudiante.nombre_completo)
console.log("Mensaje del estudiante", estudiante.pasatiempos)
console.log("Curso matriculados", estudiante.cursos)
console.log("Mi primer curso", estudiante.cursos[0])
console.log("Nombre de la asignatura del primer curso", estudiante.cursos[0].nombre)