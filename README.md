# ISO810ISO815-Contabilidad

Ian Fernandez - A00100600
Raymer Segura - A00104796

# Requerimientos de la asignación

Desarrolle un Sistema de Contabilidad que cumpla con las siguientes características y que se integre con el Sistema de Nóminas y con el de WS Púublicos (a ser desarrollado por otro de los equipos) mediante Servicio Web:

1. Gestión de Catálogo de Cuentas Contables
2. Gestión de Tipos de Cuentas (1- Activo, 2-Pasivo, 3-Capital, etc.)
3. Gestión de Tipos de Moneda (ej: Peso, Dollar, etc.)
4. Gestion de Auxiliares (Otros Sistemas Contables)
5. Registro de Entrada contable  
6. Interfaz con el Sistema de: (Servicios Web Públicos (Tasa Cambiaria) y expone WS para registro automático de entrada contable de los auxiliaries, vía WS)
7. Una consulta por criterios (ej: Entradas Contables x Cuenta, fecha, etc.)
8. Desarrrollado en el lenguaje Propietario de su preferencia

# Set up del Web Service

En cada carpeta se encuentra un .txt con cada instrucción para cada componente.

# Set up del programa local general

1. Instalar Python de 64 bits (si usas Mac con ARM, correr la terminal con Rossetta 2)
2. Installar requests, PyQt5, cx_Oracle usando pip
3. Hacer set up de la DB de Oracle en la nube y configurar el InstantClient correctamente y usando conexión vía Wallet, recordar configurar el TNS correctamente de forma local en la carpeta /network/admin dentro de la carpeta de InstantClient.