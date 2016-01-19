import numpy as np
import math as m

ab = (raw_input('Give line AB :'))
bc = int(raw_input('Give length of line BC :'))

## length of hypotenuse of right triangle
ac = m.hypot(ab,bc)

## solve for phi, angle made from MC, BC ##
phi = m.radians(m.acos((bc/ac)))

## midpoint to C
mc = 0.5 * ac

