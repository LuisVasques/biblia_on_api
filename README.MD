# Bíblia On
Este projeto é uma versão digital do plano de estudo bíblico, criado como uma
forma de estudo das tecnologias Django e Angular, também feito com o intuíto de
resolver uma problemática real.

## Tecnologias
* Python 3.11
* Django 4.2.4
* Angular 14

## Como rodar (Pycharm)
1. Configurar a venv do ambiente
2. Instalar as dependências
    > pip install -r requirements
3. Migrar a base de dados
    > python manage.py migrate
4. Executar os métodos da action de população da base (Python Console)
    ```py
   from core import actions
   actions.PopulateAction.request_api()
   actions.PopulateAction.update_chronology_order()
   ```