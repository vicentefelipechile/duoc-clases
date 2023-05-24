from os import system;system("cls")
import json
import random

FILE_NOMBRES = open("first-names.json")
FILE_APELLIDOS = open("middle-names.json")
FILE_HEROES = open("superheroes.json")

TABLA = "villano"

NOMBRES = json.load(FILE_NOMBRES)
APELLIDOS = json.load(FILE_APELLIDOS)
HEROES = json.load(FILE_HEROES)
CIUDAD = open("list.txt").read().splitlines()


for i in range(100):
    i += 1
    query = f"""INSERT INTO {TABLA} VALUES ({i}, '{random.choice(HEROES)}');"""
    print(query)