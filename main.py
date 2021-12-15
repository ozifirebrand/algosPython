import unittest

from personalAlgoProblems.unitesting.person import Person
from personalAlgoProblems.unitesting.testing import Testing

if __name__ == '__main__':
    person = Person()
    print('User Nonye has been added with id ', person.set_name('Nonye'))
    print('User Esse has been added with id ', person.set_name('Esse'))
    print('Users with ids 0 and 1 are ', person.get_name(0), 'and ', person.get_name(1), 'respectively')

    unittest.main()