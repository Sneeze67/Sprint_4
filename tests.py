import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
@pytest.fixture(scope = 'function')
def collector():
    collector = BooksCollector()
    return collector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
    def test_add_new_book_empty_string_dont_add_book(self,collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0
    def test_add_new_book_more_than_41_symbols_dont_add_book(self,collector):
        collector.add_new_book('Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных, браноносных и мирных гениев России с последованием дидактических, эротических и других разного рода в стихах и прозе опытов Семена Боброва')
        assert len(collector.get_books_genre()) == 0
    def test_add_new_book_add_same_book_dont_add_book(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
    books_with_different_genres = [['Гордость и предубеждение и зомби','Фантастика'],['Сияние','Ужасы'],['Шерлок Холмс','Детективы'],['Смешарики','Мультфильмы'],['Собачье сердце','Комедии']]
    @pytest.mark.parametrize('name,genre',books_with_different_genres)
    def test_set_book_genre_book_in_collection_genre_in_genre_array_genre_set_successfully(self,collector,name,genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre
    def test_set_book_genre_genre_not_in_genre_array_genre_not_set(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Очень крутой жанр')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''
    def test_set_book_genre_set_genre_nonexistent_book_genre_not_set(self,collector):
        collector.set_book_genre('Преступление и наказание', 'Фантастика')
        assert collector.books_genre == {}
    @pytest.mark.parametrize('name,genre',books_with_different_genres)
    def test_get_book_genre_book_in_dict_get_book_genre(self,collector,name,genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_book_genre(name)
        assert result == genre
    def test_get_book_genre_dont_add_book_genre_return_empty_string(self,collector):
        collector.add_new_book('Преступление и наказание')
        result = collector.get_book_genre('Преступление и наказание')
        assert result == ''
    def test_get_books_genre_returned_dict(self,collector):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Фантастика')
        result = collector.get_books_genre()
        assert result == collector.books_genre
    def test_get_books_with_specific_genre_add_two_books_show_book_with_specific_genre(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        collector.add_new_book('Смешарики')
        collector.set_book_genre('Смешарики','Мультфильмы')
        result = collector.get_books_with_specific_genre('Мультфильмы')
        assert result == ['Смешарики']
    @pytest.mark.parametrize('name,genre', [['Гордость и предубеждение и зомби','Фантастика'], ['Смешарики','Мультфильмы'],['Собачье сердце','Комедии']] )
    def test_get_book_for_children_add_books_suited_for_children_book_added(self,collector,name,genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert result == [name]
    @pytest.mark.parametrize('name,genre', [['Сияние','Ужасы'],['Шерлок Холмс','Детективы']])
    def test_get_book_for_children_add_books_not_suited_for_children_book_not_added(self,collector,name,genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert result == []
    def test_get_book_for_children_book_without_genre_book_not_added(self,collector):
        collector.add_new_book('Хорошая книга')
        result = collector.get_books_for_children()
        assert result == []
    def test_add_book_in_favorites_add_two_books_two_books_added(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Гордость и предубеждение и зомби' in collector.favorites and 'Что делать, если ваш кот хочет вас убить' in collector.favorites
    def test_add_book_in_favorites_add_same_book_twice_book_added_once(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1
    def test_add_book_in_favorites_add_nonexistent_book_book_not_added(self,collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 0
    def test_delete_book_from_favorites_book_deleted(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == []
    def test_get_list_of_favorites_books_shown_favorite_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = collector.get_list_of_favorites_books()
        assert result == collector.favorites
