class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]):
                return iterable[i]
        return None

    def filter(self, iterable, callback):
        newList = []
        for i in range(len(iterable)):
            if callback(iterable[i]):
                newList.append(iterable[i])
        return newList

    def reject(self, iterable, callback):
        newList = []
        for i in range(len(iterable)):
            if not callback(iterable[i]):
                newList.append(iterable[i])
        return newList

_ = Underscore() 

# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# squared = _.map([1, 2, 3, 4, 5, 6], lambda x: x ** 2)
# exsited = _.find([1,2,3,4,5,6], lambda x: x > 3)
# rejected = _.reject([1,2,3,4,5,6], lambda x: x > 3)
# print(evens)
# print(squared)
# print(exsited)
# print(rejected)
