# Función de Utilidad en Estrategias Climáticas

**Autor:** Edgar Tobon Sosa  
**Fecha:** 18.01.2026  

Este repositorio contiene una implementación en Python para calcular la **función de utilidad** de ciudades en el contexto de estrategias de cooperación climática. El objetivo es evaluar los beneficios y costos para cada ciudad al decidir cooperar en la reducción de emisiones y la adopción de soluciones tecnológicas.  

---

## Resumen

En este modelo, cada ciudad tiene tres características principales:

1. **Potencial de reducción de emisiones (`ei`)** – Cuánto puede reducir la ciudad sus emisiones.  
2. **Factor de riesgo (`ri`)** – Qué tan vulnerable es la ciudad frente a riesgos climáticos.  
3. **Capacidad tecnológica (`ti`)** – Qué tan preparada está la ciudad para adoptar nuevas tecnologías de acción climática.  

La **función de utilidad** combina estos factores para proporcionar un valor escalar que representa el beneficio neto de la cooperación y el esfuerzo de la ciudad en estrategias climáticas.

---

## Constantes

El modelo utiliza valores predefinidos para las ciudades:

```python
EMISION_CITIES_VALUES = [0.9, 0.7, 0.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
RISK_CITIES_VALUES = [0.6, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
TECHNOLOGICAL_CITIES_VALUES = [0.4, 0.8, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
