# Expresos de la Costa 🚌

Proyecto web desarrollado con Django para visualizar los horarios y tarifas de la línea de buses "Expresos de la Costa" que opera en la región de la costa de Valdivia, Chile. El objetivo es ofrecer una interfaz limpia, rápida y fácil de usar para que los pasajeros puedan consultar la información de sus viajes.

## Características Principales

* **Visualización de Horarios:** Horarios agrupados de forma clara por cada ruta (Origen → Destino).
* **Tabla de Tarifas:** Precios detallados por tipo de pasajero (Adulto, Adulto Mayor, Escolar).
* **Filtro Dinámico:** Permite buscar y mostrar únicamente las rutas que parten de un origen seleccionado.
* **Diseño Responsivo:** Interfaz adaptable a dispositivos móviles y de escritorio gracias a Bootstrap 5.
* **Panel de Administración:** Interfaz segura y personalizada para que el cliente pueda autogestionar los horarios y tarifas.

## Tecnologías Utilizadas

* **Backend:** `Python`, `Django`
* **Frontend:** `HTML`, `CSS`, `Bootstrap 5`
* **Base de Datos (Desarrollo):** `MySQL` (con XAMPP)
* **Herramientas para Producción:** `Gunicorn`, `WhiteNoise`, `PostgreSQL`

## Instalación y Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

**1. Clonar el repositorio:**
```bash
git clone [https://github.com/RiFTIL/Proyecto-prueba.git](https://github.com/RiFTIL/Proyecto-prueba.git)
cd Proyecto-prueba
```

**2. Crear y activar un entorno virtual para Mac:**

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar dependencias:**
El archivo `requirements.txt` contiene todas las librerías necesarias.
```bash
pip install -r requirements.txt
```

**4. Configurar la base de datos local:**
* Asegúrate de tener XAMPP (o un servidor MySQL) en ejecución.
* Crea una base de datos llamada `expresos`.
* El archivo `settings.py` está preconfigurado para conectarse a esta base de datos localmente.

**5. Aplicar las migraciones:**
Este comando creará las tablas vacías en tu base de datos.
```bash
python manage.py migrate
```

**6. Cargar los datos iniciales:**
Este comando llenará las tablas con todos los horarios y tarifas del proyecto usando el archivo de `fixtures`.
```bash
python manage.py loaddata initial_data.json
```

**7. Ejecutar el servidor de desarrollo:**
```bash
python manage.py runserver
```

**8. Acceder a la aplicación:**
Abre tu navegador y ve a `http://127.0.0.1:8000`.
