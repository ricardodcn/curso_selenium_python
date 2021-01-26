from selenium.webdriver import Firefox
from time import sleep

b = Firefox()

url = 'http://selenium.dunossauro.live/exercicio_05.html'

b.get(url)

def preenche_form (browser, form, nome, senha):
    sleep(2)
    context = browser.find_element_by_css_selector(f'.form-{form}') # a cada iteração do for la embaixo será um form l0c0, l1c0, l0c1, l1c1
    inputs = {

        'nome':context.find_element_by_css_selector ('[name="nome"]'),
        'senha':context.find_element_by_css_selector('[name="senha"]'),
        'enviar':context.find_element_by_css_selector('[type="submit"]'),
   }

    inputs['nome'].send_keys(nome)
    inputs['senha'].send_keys(senha)
    inputs['enviar'].click()

forms = ['l0c0', 'l0c1', 'l1c0', 'l1c1']
for form in forms:
    preenche_form(b, form, 'Ricardo', 'Ric123')
