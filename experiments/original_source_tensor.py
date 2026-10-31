"""Shared original-source tensor contraction used by portable audits.

The ordered adjacent axes, reshape convention and modular reduction are the
original apply_pair implementation. This module imports no audit fixtures.
"""
import numpy as np


def apply_pair(A,state,slot,N,p):
    s=np.moveaxis(state,(slot,slot+1),(0,1));shape=s.shape
    out=(A@s.reshape(N*N,-1))%p
    return np.moveaxis(out.reshape(shape),(0,1),(slot,slot+1))
