def e_t(func):
    def inner():
        print("Maison... Téléphone... Maison...")
        return func()
    return inner

@e_t
def gertie():
    print("Je lui ai appris à parler ! Ecoute !")


@e_t
def elliott():
    print("Il veut rentrer chez lui !")


elliott()
gertie()


class MyIterator:
    def __init__(self, data):
        self.data = 0
        print("Je m'initialise à 40")
        self.i = 40

    def __iter__(self):
        print("On a appelé __iter__")
        return self

    def __next__(self):
        print("On a appelé __next__")
        self.i += 2
        if self.i > 56 :
            raise StopIteration()
        return self.i


for i in MyIterator(5):
  print(i)


def my_generator():
      i = 40
      while i <= 56:
          i += 2
          yield i

my_generator()