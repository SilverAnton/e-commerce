from abc import ABC, abstractmethod


class AnyProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass