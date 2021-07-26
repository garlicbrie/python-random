# WIP

from abc import ABCMeta, abstractmethod
from enum import Enum
import sys

class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3

class Card(metaclass=ABCMeta):
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def val(self):
        pass

    