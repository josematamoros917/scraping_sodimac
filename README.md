# scraping_sodimac

Este proyecto realiza un scraping en la página oficial de Sodimac para extraer datos de productos.

## Descripción

El código extrae información de productos disponibles en la página de Sodimac, incluyendo:
- **Nombre del producto**
- **Descripción**
- **Precio actual**
- **Precio original** (si el producto está en oferta)
- **Porcentaje de descuento** (si el producto está en oferta)

La información extraída se guarda en un archivo CSV con las siguientes columnas:
- `id`: Identificador del producto
- `name`: Nombre del producto
- `description`: Descripción del producto
- `price`: Precio actual del producto
- `original_price`: Precio original del producto (si está en oferta)
- `discount`: Porcentaje de descuento (si está en oferta)
- `offer`: Indica si el producto está en oferta (True/False)

En una etapa más avanzada, este proyecto pretende:
- Comparar precios con otras tiendas.
- Identificar alteraciones en los productos.
- Encontrar semejanzas y patrones.
- Realizar visualizaciones de datos para análisis más detallado.

## Requisitos

Para ejecutar el código, necesitarás las siguientes librerías:

- `selenium` - Para realizar el scraping web.
- `pandas` - Para manipulación y análisis de datos (si decides usarlo para trabajar con el archivo CSV en el futuro).

## Instalación

Recomendamos usar `pipenv` para gestionar las dependencias del proyecto. Sigue estos pasos para configurar el entorno:

1. **Instala `pipenv`** si aún no lo tienes:

    ```bash
    pip install pipenv
    ```

2. **Instala las dependencias del proyecto** usando `pipenv`:

    ```bash
    pipenv install selenium
    pipenv install pandas
    ```

3. **Activa el entorno virtual** creado por `pipenv`:

    ```bash
    pipenv shell
    ```

4. **Ejecuta el script** dentro del entorno virtual:

    ```bash
    python scrap_selen.py
    ```

## Notas

- Asegúrate de tener un controlador web como ChromeDriver instalado en tu sistema y configurado correctamente.
- Revisa las políticas de uso de datos de los sitios web que estás scrapeando para cumplir con sus términos y condiciones.
- El scraping puede estar sujeto a cambios en la estructura del sitio web, por lo que es posible que necesites actualizar los selectores CSS si el sitio cambia.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias para mejorar el código, por favor, abre un problema o una solicitud de extracción.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE.txt para obtener más detalles.

