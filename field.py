from copy import copy


class Field:
    def __init__(self, domain, chosen=None):
        self.d = domain

        self.c = chosen

        self.bd = None

    def set(self, num):
        self.c = num

    def is_set(self):
        return self.c is not None

    def set_bd(self):
        self.bd = copy(self.d)

    def restore_domain(self):
        self.d = copy(self.bd)

    def remove_min_domain(self):
        self.d.remove(min(self.d))

    def remove_max_domain(self):
        self.d.remove(max(self.d))

    def remove_lower_then(self, cond):
        self.d[:] = [x for x in self.d if x > cond]

    def remove_greater_then(self, cond):
        self.d[:] = [x for x in self.d if x < cond]

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.c is None:
            return 'x'
        return str(self.c)
