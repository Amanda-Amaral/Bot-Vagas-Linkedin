
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
import time


driver.get('https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0')


# Exibir_mais = driver.find_element_by_css_selector('body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.description > div > div > section > button.show-more-less-html__button.show-more-less-html__button--more')                                                  
# Exibir_mais.send_keys(Keys.ENTER)
# descricao = driver.find_element_by_css_selector('body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.description > div > div > section > div')
# print(descricao.text)


resultados = driver.find_elements_by_class_name('base-card__full-link')
len(resultados)


lista_descri=[]


for vaga in resultados:
    try:
        vaga.click()
        time.sleep(2)
        #Exibir_mais.clear()
        Exibir_mais = driver.find_element_by_css_selector('body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.description > div > div > section > button.show-more-less-html__button.show-more-less-html__button--more')    
        Exibir_mais.send_keys(Keys.ENTER)
        #descricao.clear()
        descricao = driver.find_element_by_css_selector('body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.description > div > div > section > div')
        time.sleep(2)
        lista_descri.append(descricao.text)
    except:
        print('Nao foi possivel abrir vaga, seguindo para proxima')


def listToString(a): 
    str1 = "\n\n/// Vaga\n\n" 
    return ('/// Vaga\n' + str1.join(a))


import csv
with open('vagas dados.csv', "w", encoding="utf-8") as f:
    f.write(listToString(lista_descri))







