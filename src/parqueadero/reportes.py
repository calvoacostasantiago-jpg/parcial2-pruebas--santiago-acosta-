import math
import os


def resumen(registros):
    r = {"carro": 0, "moto": 0, "total_recaudado": 0}
    temporal = 0
    for reg in registros:
        t = reg[0]
        m = reg[1]
        if t == "carro":
            r["carro"] += 1
            if m > 15:
                v = math.ceil(m / 60) * 3000
                if v > 25000:
                    v = 25000
                r["total_recaudado"] += v
        elif t == "moto":
            r["moto"] += 1
            if m > 15:
                v = math.ceil(m / 60) * 1500
                if v > 12000:
                    v = 12000
                r["total_recaudado"] += v
    return r