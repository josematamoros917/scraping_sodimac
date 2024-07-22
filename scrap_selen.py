import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define la URL donde se realizará el scraping
url = "https://www.sodimac.cl/sodimac-cl/buscar?Ntt=herramientas&f.product.L0_category_paths=CATG10005%7C%7CFerreter%C3%ADa+y+construcci%C3%B3n"

# La variable que contiene a Chrome
driver = webdriver.Chrome()
driver.get(url)  # Solicitar la URL a Chrome

# Archivo CSV donde se guardarán los datos
csv_filename = "data_herramientas_sodimac.csv"

# Crear el archivo CSV y escribir el encabezado con codificación UTF-8
with open(csv_filename, 'w', encoding='utf-8') as file:
    file.write("id,name,description,price,original_price,discount,offer\n")

# Función para limpiar las comas de la descripción
def clean_text(text):
    return text.replace(',', '.')

# Inicializar el contador de ID de producto
product_id = 1

# Bucle principal
while True:
    # Listas que contendrán nuestros datos scrapeados
    product_ids = []
    product_names = []
    descriptions = []
    prices = []
    original_prices = []
    discounts = []
    ofertas = []

    # Selectores de tipo CSS para identificar los elementos de la página
    product_name_elements = driver.find_elements(By.CSS_SELECTOR, ".pod-title.title-rebrand.jsx-1045750598")
    description_elements = driver.find_elements(By.CSS_SELECTOR, ".pod-subTitle.subTitle-rebrand.jsx-1045750598")
    price_containers = driver.find_elements(By.CSS_SELECTOR, ".pod-prices")

    # Bucle for para agregar cada dato capturado a las listas en forma de texto
    for i in range(len(product_name_elements)):
        try:
            product_name = product_name_elements[i].text
            description = clean_text(description_elements[i].text) if i < len(description_elements) else ""
            price = ""
            original_price = ""
            discount = ""
            oferta = False

            price_container = price_containers[i]
            price_element = price_container.find_element(By.CSS_SELECTOR, ".prices-0 .jsx-3451706699:not(.crossed)")
            price = price_element.text.strip()

            try:
                original_price_element = price_container.find_element(By.CSS_SELECTOR, ".prices-1 .jsx-3451706699.crossed")
                original_price = original_price_element.text.strip()
                discount_element = price_container.find_element(By.CSS_SELECTOR, ".discount-badge-item")
                discount = discount_element.text.strip()
                oferta = True
            except:
                # Si no encuentra elementos de precio original o descuento, no pasa nada
                pass

            # Agregar los datos a las listas
            product_ids.append(product_id)
            product_names.append(product_name)
            descriptions.append(description)
            prices.append(price)
            original_prices.append(original_price)
            discounts.append(discount)
            ofertas.append(oferta)

            # Incrementar el ID de producto para el siguiente
            product_id += 1

        except IndexError:
            print(f"Error procesando producto en el índice {i}.")
            continue

    # Guardar los datos en el CSV con codificación UTF-8
    with open(csv_filename, 'a', encoding='utf-8') as file:
        for pid, name, description, price, original_price, discount, oferta in zip(product_ids, product_names, descriptions, prices, original_prices, discounts, ofertas):
            file.write(f"{pid},{name},{description},{price},{original_price},{discount},{oferta}\n")

     # Intentar pasar a la siguiente página
    try:
        # Verificar si el botón "Siguiente" está habilitado
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "i.jsx-1389196899.arrow_right-mkp"))
        )

        if "disabled" in next_button.get_attribute("class"):
            # Si el botón está deshabilitado, terminar el bucle
            print("No hay más páginas para procesar.")
            break

        # Si el botón está habilitado, hacer clic en él
        next_button.click()
        time.sleep(5)  # Esperar a que la siguiente página cargue

    except Exception as e:
        print(f"Error al intentar pasar a la siguiente página: {e}")
        break

# Al finalizar el bucle se cierra el programa y muestra un mensaje de "proceso completado"
driver.quit()
print("Datos guardados en data_herramientas_sodimac.csv.")
