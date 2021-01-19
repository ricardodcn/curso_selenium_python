from selenium.webdriver import Firefox

def find_by_text(navegador, tag,  text):
    """
    Encontrar o elemento com o 'text.'

    Argumentos:
        -navegador = Instancia do Navegador [firefox]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """
    elementos = navegador.find_elements_by_tag_name(tag) #lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href (navegador, link):

    elementos = navegador.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

navegador = Firefox()

navegador.get ('http://selenium.dunossauro.live/aula_04_a.html')

#elemento_ddg = find_by_text(navegador, 'a', 'DuckDuckGo')

elemento_ddg = find_by_href(navegador, 'ddg')
