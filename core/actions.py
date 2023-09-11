import requests
from core import models


class PopulateAction:
    @staticmethod
    def request_api():
        response = requests.get('https://www.abibliadigital.com.br/api/books')
        if response.ok:
            data = response.json()

            # livros
            for idx, book in enumerate(data):

                book['name'] = book['name'].replace('1ª', '1').strip()
                book['name'] = book['name'].replace('1º', '1').strip()
                book['name'] = book['name'].replace('2ª', '2').strip()
                book['name'] = book['name'].replace('2º', '2').strip()
                book['name'] = book['name'].replace('3ª', '3').strip()
                book['name'] = book['name'].replace('3ª', '3').strip()


                print(f"{book['name']} - {book['testament']} - {book['chapters']} - {book['abbrev']['pt']}")

                obj = models.Book.objects.create(
                    name=book['name'],
                    order=(idx+1),
                    testament=models.Book.Testament.OLD if book['testament'] == 'VT' else models.Book.Testament.NEW
                )
                obj.save()

                # capitulos
                for i in range(book['chapters']):
                    chapter = models.Chapter.objects.create(
                        number=(i+1),
                        chronology=0,
                        book=obj
                    )
                    chapter.save()

    @staticmethod
    def update_chronology_order():
        with open('core/fixtures/capitulos_ordem_crono.txt') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                tx_book, nb_chapter = line.split()

                tx_book = tx_book.replace('1', '1 ')
                tx_book = tx_book.replace('2', '2 ')
                tx_book = tx_book.replace('3', '3 ')

                queryset = models.Chapter.objects.filter(number=nb_chapter, book__name__icontains=tx_book)
                if queryset.exists():
                    chapter = queryset.first()

                    print(f"book {tx_book} - capitulo {chapter.number} de {chapter.chronology} para {idx+1}")

                    chapter.chronology = (idx + 1)
                    chapter.save()

    @staticmethod
    def view():
        list = models.Chapter.objects.values('book__name', 'number', 'chronology').order_by('chronology')
        for cha in list:
            print(f"{cha['book__name']} - {cha['number']} - {cha['chronology']}")
