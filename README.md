# swagger-app
# API con Swagger

Esta es una API simple que utiliza Flask y Swagger para generar documentación automática.

## Cómo ejecutar la aplicación

### Localmente
1. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2. Ejecutar la aplicación:
    ```bash
    python app.py
    ```
3. Acceder a la API en [http://localhost:5000](http://localhost:5000).
4. La documentación Swagger estará en [http://localhost:5000/swagger](http://localhost:5000/swagger).

### Usando Docker
1. Construir la imagen:
    ```bash
    docker build -t swagger-app .
    ```
2. Ejecutar el contenedor:
    ```bash
    docker run -p 5000:5000 swagger-app
    ```
3. Acceder a la API en [http://localhost:5000](http://localhost:5000).
4. La documentación Swagger estará en [http://localhost:5000/swagger](http://localhost:5000/swagger).
