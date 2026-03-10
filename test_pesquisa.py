from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_pesquisa_google():
    # 1. Configura o driver
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)

    try:
        # 2. Abre o site
        driver.get("https://www.google.com")
        
        # 3. Encontra a barra de pesquisa (o nome dela no código do Google é "q")
        barra_busca = driver.find_element(By.NAME, "q")
        
        # 4. Digita o que você quer pesquisar
        barra_busca.send_keys("Automação com Python e Selenium")
        
        # 5. Simula o aperto da tecla ENTER
        barra_busca.send_keys(Keys.ENTER)
        
        # Pequena pausa para você conseguir ver o resultado na tela
        time.sleep(3)
        
        print("Teste de pesquisa concluído com sucesso!")

    finally:
        # 6. Fecha o navegador
        driver.quit()

if __name__ == "__main__":
    test_pesquisa_google()