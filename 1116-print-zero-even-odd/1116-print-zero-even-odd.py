from threading import Condition
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cur = 1
        self.non_zero = False
        self.c = Condition()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.c:
                printNumber(0)
                self.non_zero = True
                self.c.notify_all()
                self.c.wait_for(lambda: not self.non_zero)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n // 2):
            with self.c:
                self.c.wait_for(lambda: self.non_zero and self.cur % 2 == 0)
                printNumber(self.cur)
                self.cur += 1
                self.non_zero = False
                self.c.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n + 1) // 2):
            with self.c:
                self.c.wait_for(lambda: self.non_zero and self.cur % 2 != 0)
                printNumber(self.cur)
                self.cur += 1
                self.non_zero = False
                self.c.notify_all()