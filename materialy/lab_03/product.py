# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price < 0:
            raise ValueError("Cena nie może być ujemna.")
        if quantity < 0:
            raise ValueError("Ilość nie może być ujemna.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu.

        Raises:
            ValueError: jesli amount jest ujemne
        """
        # TODO: Zaimplementuj dodawanie do magazynu
        if amount < 0:
            raise ValueError("Nie można dodać ujemnej ilości do magazynu.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu.

        Raises:
            ValueError: jesli amount jest ujemne lub wieksze niz dostepna ilosc
        """
        # TODO: Zaimplementuj usuwanie z magazynu
        if amount < 0:
            raise ValueError("Nie można usunąć ujemnej ilości z magazynu.")
        if amount > self.quantity:
            raise ValueError("Brak wystarczającej ilości produktów w magazynie.")
        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        # TODO: Zaimplementuj sprawdzanie dostepnosci
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        # TODO: Zaimplementuj obliczanie wartosci
        return self.price * self.quantity
