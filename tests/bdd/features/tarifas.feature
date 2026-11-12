# language: es
Característica: Cobrar las estadías en EstacionaYa
  Como dueño del parqueadero
  Quiero cobrar según el vehículo y el tiempo de permanencia
  Para respetar la gracia, el tope diario y los beneficios de mis clientes

  Esquema del escenario: Cobrar la estadía según las reglas del parqueadero
    Dado que un vehículo de tipo "<tipo_vehiculo>" permaneció <minutos> minutos
    Cuando se calcula el cobro de su estadía
    Entonces debe pagar <valor> pesos

    Ejemplos: Estadías dentro de los minutos de gracia
      | tipo_vehiculo | minutos | valor |
      | carro         | 0       | 0     |
      | carro         | 14      | 0     |
      | carro         | 15      | 0     |
      | moto          | 0       | 0     |
      | moto          | 14      | 0     |
      | moto          | 15      | 0     |

    Ejemplos: Cobro por cada hora o fracción después de la gracia
      | tipo_vehiculo | minutos | valor |
      | carro         | 16      | 3000  |
      | carro         | 60      | 3000  |
      | carro         | 61      | 6000  |
      | moto          | 16      | 1500  |
      | moto          | 60      | 1500  |
      | moto          | 61      | 3000  |

    Ejemplos: El cobro llega al tope diario y no lo supera
      | tipo_vehiculo | minutos | valor |
      | carro         | 480     | 24000 |
      | carro         | 481     | 25000 |
      | carro         | 1440    | 25000 |
      | moto          | 420     | 10500 |
      | moto          | 421     | 12000 |
      | moto          | 480     | 12000 |
      | moto          | 481     | 12000 |
      | moto          | 1440    | 12000 |

  Escenario: Un cliente frecuente recibe descuento sobre su estadía
    Dado que un vehículo de tipo "carro" permaneció 61 minutos
    Y que el cliente es "frecuente"
    Cuando se calcula el cobro de su estadía
    Y se aplica el descuento del cliente
    Entonces debe pagar 5400 pesos

  Escenario: Un cliente con convenio recibe descuento sobre el tope diario
    Dado que un vehículo de tipo "carro" permaneció 1440 minutos
    Y que el cliente es "convenio"
    Cuando se calcula el cobro de su estadía
    Y se aplica el descuento del cliente
    Entonces debe pagar 20000 pesos

  Escenario: Una estadía gratuita sigue siendo gratuita al aplicar un beneficio
    Dado que un vehículo de tipo "moto" permaneció 15 minutos
    Y que el cliente es "frecuente"
    Cuando se calcula el cobro de su estadía
    Y se aplica el descuento del cliente
    Entonces debe pagar 0 pesos

  Escenario: El cobro con descuento se redondea hacia abajo al peso entero
    Dado que el cobro antes del descuento es 1999 pesos
    Y que el cliente es "frecuente"
    Cuando se aplica el descuento del cliente
    Entonces debe pagar 1799 pesos
