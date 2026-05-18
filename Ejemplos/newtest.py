import pymongo
from pymongo import MongoClient
import os
import json
conexion=MongoClient("mongodb://localhost:27017")
db=conexion["ejemplos"]
col=db["alumnos"]
col2=db["ramos"]
def insertar():
    nombre=input("Ingrese el nombre del alumno/a: ")
    edad=int(input("Ingrese la edad del alumno/a: "))
    carrera=input("Ingrese la carrera del alumno/a: ")
    correo=input("Ingrese el correo del alumno/a: ")
    os.system("cls")
    documento={"nombre":nombre, "edad":edad, "carrera":carrera, "correo":correo}
    col.insert_one(documento)
    print(f"""Datos ingresados! 
    Alumno/a: {nombre}
    Edad: {edad}
    Carrera: {carrera}
    Correo: {correo}""")


def mostrar():
    os.system("cls")
    salida=col.find({})
    for linea in salida:
        print(linea["nombre"])

while True:
    os.system("cls")
    print("-- BIENVENIDO AL SISTEMA --")
    print("")
    print("0. Salir")
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("")
    op=int(input("Ingrese una opcion: "))
    if op==1:
        insertar()
        input("Presione enter para continuar...")
    elif op==2:
        mostrar()
        input("Presione enter para continuar...")
    elif op==0:
        os.system("cls")
        break
    else:
        print("Opcion invalida.")
        input("Presione enter para continuar...")