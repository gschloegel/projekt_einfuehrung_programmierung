#!/usr/bin/env python
"""
Mirrors the ascii images of 2 cats
"""


def mirror_string(s: str, len_longest_line: int):
    """Mirrors string. Replaces characters that have counterparts,
     keeps the rest."""
    assert '\n' not in s
    # adds spaces to make sure all lines have the same length
    s = s + ' ' * (20 - len(s))
    # replace symbol by mirrored counterpart and invert string
    tab = str.maketrans('\\/()', '/\\)(')
    return s.translate(tab)[::-1]


def mirror(s):
    """Mirrors multi-line string. Breaks it up into strings, mirrors them,
    puts them back together.

    What about padding/alignment?
    """
    output = []
    # determine longest line in string
    len_longest_line = len(max(s.split("\n"), key=len))
    # mirror string
    for i in s.splitlines():
        output.append(mirror_string(i, len_longest_line))
    return '\n'.join(output)


cat1 = r"""
                  _ 
                 / )
                ( ( 
  A.-.A  .-""-.  ) )
 / , , \/      \/ / 
=\  t  ;=    /   /  
  '--,'  .""|   /   
      || |  \\ \    
     ((,_|  ((,_\   
"""

cat2 = r"""
                  _ 
                 / )
                ( (
  A.-.A  .-""-.  ) )
 / , , \/      \/ /
=\  t  ;=    /   /
  '--,'  .""|   /
      || |  \\ \
     ((,_|  ((,_\
"""

print("Cat 1:", cat1)
print("Mirrored cat 1:", mirror(cat1))

print("Cat 2:", cat2)
print("Mirrored cat 2:", mirror(cat2))
