#!/usr/bin/env python

TRINARY_0 = [1,0,0,0,1,0,0,0]
TRINARY_1 = [1,1,1,0,1,1,1,0]
TRINARY_X = [1,0,0,0,1,1,1,0]

SYNC      = [1] + [0] * 32

BIT_CODE = [TRINARY_0 + TRINARY_X + TRINARY_X + TRINARY_X,
            TRINARY_X + TRINARY_0 + TRINARY_X + TRINARY_X,
            TRINARY_X + TRINARY_X + TRINARY_0 + TRINARY_X,
            TRINARY_X + TRINARY_X + TRINARY_X + TRINARY_0]

UNKNOWN_CODE = TRINARY_0 + TRINARY_X + TRINARY_X

ON_CODE  = TRINARY_X
OFF_CODE = TRINARY_0

DEFAULT_PULSE_WIDTH = 350 * 1e-6

