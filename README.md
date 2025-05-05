# ERP CRM - Implementación Personalizada de Odoo

[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)

## Descripción del Proyecto
Este proyecto es una implementación personalizada de Odoo, un sistema ERP (Enterprise Resource Planning) de código abierto. El sistema está diseñado para gestionar todos los aspectos de un negocio, desde CRM hasta gestión de inventario y contabilidad.

## Características Principales
- CRM (Customer Relationship Management)
- Gestión de Inventario
- Contabilidad y Facturación
- Gestión de Proyectos
- Comercio Electrónico
- Punto de Venta
- Recursos Humanos
- Marketing
- Manufactura

## Requisitos del Sistema
- Python 3.8+
- PostgreSQL
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/miguelmartmart/erpcrm.git
cd erpcrm
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
.\venv\Scripts\activate  # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos PostgreSQL

5. Iniciar el servidor:
```bash
./odoo-bin
```

## Estructura del Proyecto
```
erpcrm/
├── addons/           # Módulos personalizados
├── odoo/            # Core de Odoo
├── setup/           # Scripts de configuración
├── venv/            # Entorno virtual
├── requirements.txt # Dependencias del proyecto
└── odoo-bin        # Script de inicio
```

## Configuración
El archivo de configuración principal se encuentra en `setup/odoo.conf`. Asegúrate de configurar:
- Conexión a la base de datos
- Puerto del servidor
- Modo de desarrollo/producción

## Desarrollo
Para desarrollo, se recomienda:
1. Activar el modo desarrollador en la interfaz web
2. Usar el entorno virtual
3. Seguir las guías de desarrollo de Odoo

## Contribución
Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Crear un Pull Request

## Licencia
Este proyecto está bajo la licencia LGPL-3.0. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Soporte
Para soporte y ayuda:
- Revisar la [documentación oficial de Odoo](https://www.odoo.com/documentation/master)
- Consultar el [foro de ayuda de Odoo](https://www.odoo.com/forum/help-1)
- Abrir un issue en este repositorio

## Seguridad
Para reportar problemas de seguridad, por favor revisa nuestra [política de seguridad](SECURITY.md).

## Acceso a la Base de Datos en Contenedor Docker

Si bien puede haber problemas de autenticación al intentar acceder a la base de datos directamente desde el host, se puede interactuar con la base de datos ejecutando comandos `psql` dentro del contenedor Docker `erpcrm-db-1`.

Para ejecutar comandos `psql` dentro del contenedor, utilice el siguiente formato:

```bash
docker exec erpcrm-db-1 psql -U odoo -d odoodb -c 'TU_SENTENCIA_SQL_O_COMANDO_PSQL'
```

Donde `TU_SENTENCIA_SQL_O_COMANDO_PSQL` es el comando SQL o el meta-comando de psql que desea ejecutar.

Ejemplos:

- Para ver el esquema de una tabla (por ejemplo, `account_move`):
```bash
docker exec erpcrm-db-1 psql -U odoo -d odoodb -c '\d account_move'
```

- Para seleccionar datos de una tabla (por ejemplo, los nombres de los empleados):
```bash
docker exec erpcrm-db-1 psql -U odoo -d odoodb -c 'SELECT name FROM hr_employee;'
```

- Para seleccionar datos con uniones y límites:
```bash
docker exec erpcrm-db-1 psql -U odoo -d odoodb -c 'SELECT aml.date, aa.name AS account_name, rp.name AS partner_name, aml.debit, aml.credit FROM account_move_line aml JOIN account_account aa ON aml.account_id = aa.id LEFT JOIN res_partner rp ON aml.partner_id = rp.id LIMIT 10;'
```

Utilice este método para explorar la estructura y los datos de la base de datos directamente desde el contenedor.
