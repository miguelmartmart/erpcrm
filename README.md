# ERP CRM - Implementación Personalizada de Odoo actualizado

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

## Integración con Xata Agent

Este proyecto integra Xata Agent como un copiloto de base de datos para facilitar consultas SQL generadas por IA y análisis de la base de datos. La arquitectura de contenedores es la siguiente:

-   **Contenedor Odoo:** Ejecuta la aplicación principal de Odoo (ERP).
-   **Contenedor de Base de Datos (PostgreSQL):** Almacena todos los datos de Odoo. Este servicio se llama `db` dentro de la red de Docker.
-   **Contenedor Xata Agent:** Ejecuta la aplicación de Xata Agent. Este contenedor se conecta a la base de datos de Odoo (`db`) para realizar análisis y generar consultas.

Todos estos servicios se ejecutan en la misma red de Docker definida en el archivo `docker-compose.yml` para permitir la comunicación entre ellos.

### Funcionamiento

-   Odoo proporciona la interfaz de usuario y la lógica de negocio del ERP.
-   La base de datos PostgreSQL almacena de forma persistente todos los datos del ERP.
-   Xata Agent se conecta a la base de datos de Odoo y utiliza un modelo de lenguaje grande (LLM) para entender preguntas en lenguaje natural sobre la base de datos y generar respuestas o consultas SQL relevantes. La interacción con Xata Agent se realiza a través de su propia interfaz web.

### Configuración del LLM

La clave de API para el modelo de lenguaje (LLM) utilizado por Xata Agent se define en el archivo `.env.production` ubicado en el directorio donde clonaste el repositorio de Xata Agent (`/home/miguel/dev/agents/xata-agent/`). Asegúrate de configurar la variable correspondiente a tu proveedor de LLM (por ejemplo, `GOOGLE_GENERATIVE_AI_API_KEY` para Gemini).

El modelo gratuito de Gemini es **Gemini 2.0 Flash**. Puedes configurarlo usando la variable `GEMINI_MODEL` en el archivo `.env.production` con el valor `models/gemini-2.0-flash`.

### Gestión de Contenedores con Docker Compose (desde `/home/miguel/erpcrm`)

Para gestionar los servicios definidos en el archivo `docker-compose.yml` (Odoo, BD y Xata Agent) desde el directorio raíz de este proyecto (`/home/miguel/erpcrm`), puedes usar los siguientes comandos:

**Levantar todos los servicios (Odoo, BD, Xata Agent):**

Para construir las imágenes (si hay cambios) e iniciar todos los servicios:

```bash
docker compose up --build -d
```

-   `up`: Inicia los servicios definidos en `docker-compose.yml`.
-   `--build`: Reconstruye las imágenes de los servicios que tienen una directiva `build` (como Odoo y Xata Agent) antes de iniciarlos. Esto es útil si has realizado cambios en el código fuente de Odoo o Xata Agent.
-   `-d`: Ejecuta los contenedores en modo "detached" (en segundo plano).

**Detener todos los servicios:**

```bash
docker compose down
```

**Reiniciar un servicio específico (por ejemplo, Xata Agent):**

Si solo has modificado la configuración o el código de Xata Agent y quieres reiniciarlo sin afectar a los otros servicios:

```bash
docker compose restart xata-agent
```

**Reconstruir la imagen de un servicio específico (por ejemplo, Xata Agent):**

Si has realizado cambios en el código fuente de Xata Agent (`/home/miguel/dev/agents/xata-agent/`), necesitarás reconstruir su imagen antes de reiniciarlo para que los cambios se apliquen:

```bash
docker compose build --no-cache xata-agent
```

-   `build`: Reconstruye la imagen de un servicio específico.
-   `--no-cache`: Deshabilita el caché de construcción, asegurando que se utilicen los archivos más recientes del código fuente.
-   `xata-agent`: Especifica que solo se reconstruya la imagen del servicio `xata-agent`.

Después de reconstruir la imagen, recuerda reiniciar el servicio (`docker compose restart xata-agent`) para usar la nueva imagen.

### Acceso a la Interfaz Web

-   **Odoo:** Accede a la interfaz web de Odoo en [http://localhost:8069](http://localhost:8069).
-   **Xata Agent:** Accede a la interfaz web de Xata Agent en [http://localhost:8080](http://localhost:8080).

### Verificación de Modelos de LLM en Xata Agent

La lista de modelos de LLM disponibles en el combobox de la interfaz de Xata Agent se define en el código fuente del agente, específicamente en el archivo `apps/dbagent/src/lib/ai/providers/builtin.ts`. Si has configurado una clave de API en `.env.production` para un proveedor soportado, los modelos definidos para ese proveedor en `builtin.ts` deberían aparecer en la interfaz.

Si has configurado un modelo de Gemini en `.env.production` pero no aparece en la interfaz o no funciona, verifica que esté correctamente definido en `builtin.ts` y que no haya otros problemas de configuración o compatibilidad.


