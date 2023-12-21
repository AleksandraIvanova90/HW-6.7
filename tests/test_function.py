import pytest

from function import cheking_brackets

@pytest.mark.parametrize(
    'bracket_str, expected',(
        ['(((([{}]))))', 'Cбалансированно'],
        ['[([])((([[[]]])))]{()}', 'Cбалансированно'],
        ['{{[()]}}', 'Cбалансированно'],
        ['}{}', 'Несбалансированно' ],
        ['{{[(])]}}', 'Несбалансированно'],
        ['[[{())}]', 'Несбалансированно']
    )
)
def test_cheking_brackets(bracket_str, expected):
    result = cheking_brackets(bracket_str)
    assert result == expected