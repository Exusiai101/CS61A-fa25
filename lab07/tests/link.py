test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1000)
          >>> link.first
          1000
          >>> link.rest is Link.empty
          True
          >>> link = Link(1000, 2000)
          Error
          >>> link = Link(1000, Link())
          Error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          1
          >>> link.rest.first
          2
          >>> link.rest.rest.rest is Link.empty
          True
          >>> link.first = 9001
          >>> link.first
          9001
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          3
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest is Link.empty
          1a1d55c577c8de00da2b32e78f9335d1
          # locked
          >>> link.rest.rest.rest.rest.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> link2.rest.first
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          a353eddb3d8856d2db7bf086df685a3d
          # locked
          >>> print(link)           # Look at the __str__ method of Link
          25c7ce903757e4d9be73a6ae9cf74023
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
