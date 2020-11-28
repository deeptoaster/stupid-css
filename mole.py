#!/usr/bin/python
from heapq import *
from random import *

DELAY_MAX = 6.0
DELAY_MIN = 3.0
HOLE_COUNT = 5
HOLE_SCORE = 5
MOLE_COUNT = 5
MOLE_SCORE = 10
POSITIONS = [
  {"top": "2.5em", "left": "5em"},
  {"top": "1em", "left": "11em"},
  {"top": "2.5em", "left": "17em"},
  {"top": "1em", "left": "23em"},
  {"top": "2.5em", "left": "29em"}
]
REST_MAX = 1.2
REST_MIN = 0.6

for i in range(HOLE_COUNT + MOLE_COUNT + 1):
  for j in range(max(i - MOLE_COUNT, 0), min(i + 1, HOLE_COUNT + 1)):
    print(
      '.mole-hole-toggle:checked ~ ' * j + '.mole-mole-toggle:checked ~ ' *
          (i - j) + '.mole-score::after {\n  content: \'' +
          ('\\2210 ' if (i - j) * MOLE_SCORE < j * HOLE_SCORE else '+') +
          f'{abs((i - j) * MOLE_SCORE - j * HOLE_SCORE):02}' + '\';\n}'
    )

seed(0)
moles = [
  (uniform(DELAY_MIN, DELAY_MAX), mole, None) for mole in range(MOLE_COUNT)
]
holes = [None] * HOLE_COUNT
css = [''] * MOLE_COUNT
while True:
  (time, mole, hole) = heappop(moles)
  if time >= 100:
    break
  if hole is None:
    hole = randrange(HOLE_COUNT)
    while holes[hole] is not None:
      hole = (hole + 1) % HOLE_COUNT
    holes[hole] = mole
    rest = uniform(REST_MIN, REST_MAX)
    heappush(moles, (time + rest, mole, hole))
    css[mole] += (
      f'  {time / MOLE_COUNT + mole * 100 / MOLE_COUNT:.2f}% {{\n'
      f'    top: {POSITIONS[hole]["top"]};\n'
      f'    left: {POSITIONS[hole]["left"]};\n'
       '  }\n'
    )
  else:
    holes[hole] = None
    delay = uniform(DELAY_MIN, DELAY_MAX)
    heappush(moles, (time + delay, mole, None))
    css[mole] += (
      f'  {time / MOLE_COUNT + mole * 100 / MOLE_COUNT:.2f}% {{\n'
      f'    top: -8em;\n'
       '  }\n'
    )
for chunk in css:
  print(chunk, end='')
