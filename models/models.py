

class Model:

    count = int()

    def __init__(self, **kwargs):
        if kwargs:
            for i in kwargs:
                print(type(self))
                exec(f'self.{i}.data = kwargs[i]')

    def __setattr__(self, key, value):
        try:
            key.data = value
        except AttributeError:
            super(Model, self).__setattr__(key, value)
        finally:
            return

    def save(self):
        pass

    @classmethod
    def updatePK(cls, obj):
        cls.count += 1
        obj.id = cls.count


class RelationField:
    data = None

    def __init__(self, model=None):
        self.data = model


class TextField:

    data = str()

    def __str__(self):
        return f'{self.data}'

    def __setattr__(self, key, value):
        if type(value) == type(str):
            self.data = value
        else:
            raise ValueError('value must be a string')


class IntegerField:
    data = int()

    def __str__(self):
        return f'{self.data}'

    def __setattr__(self, key, value):
        if type(value) == type(int):
            self.data = value
        else:
            raise ValueError('value must be a integer')
