#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de cálculo de promedio
"""
def calcular_promedio(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)

if __name__ == "__main__":
    datos = [10, 15, 20, 25, 30]
    print(f"El promedio de {datos} es: {calcular_promedio(datos)}")
