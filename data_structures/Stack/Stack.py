from __future__ import annotations
from msilib.schema import Property

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):

    def __init__(self, limit: int = 10) -> None:
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> None:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        """ Appends data to the top of the stack. """
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self) -> T:
        """ Removes the last element of the stack. """
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        """ Return the top element of the stack. """
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def size(self) -> int:
        """ Returns the length of the stack. """
        return len(self.stack)

    def is_empty(self) -> bool:
        """ Check if a stack is empty. """
        return not bool(self.stack)

    def is_full(self) -> bool:
        """ Check if the stack reached the limit. """
        return self.size() == self.limit

    def __contains__(self, item: T) -> bool:
        """Check if item is in stack"""
        return item in self.stack
