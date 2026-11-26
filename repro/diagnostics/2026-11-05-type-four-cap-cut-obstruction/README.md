# A fixed obstruction to an E-only first-cap cutoff

This is a rigorous fixed scalar comparison, not a full cap theorem or
an obstruction to the volume conjecture. There is no optimizer or new
root search. The checker revalidates the saved original-log Newton disk
for the actual one-vertex type-four critical point and binds its author,
independent replay, and source proofs.

Write J for the normalized strip primitive, g(e)=J(e)+i*pi*e*(1-e)/2,
and S(e) for the original complete-end critical action. The literal
type-four cap is the degree-less-than-N polynomial

    U1(w,X) = sum_i D_N(i/N)^(-1) C_N(i/N,w) p_i(X)/P_i.

After the inner endpoint packet, its original outer-row phase is

    Psi1(e,z) = S(e)+J(e+z)-J(z)-i*pi*e*z-g(e).

Let z be the actual symmetric one-vertex type-four critical leg. Its
existing original-log disk gives approximately

    z = .3463583260874289 - .04849274958830588 i.

The outward 320-bit calculation proves

    Re Psi1(.33,z) - Re Psi1(z,z) > 13/1000.

Thus discarding the real outer rows to the left of the endpoint-source
rectangle E, whose left edge is .33, cannot yield an absolute gap below
this selected cap saddle. For N divisible by 100, the row i=33N/100 is
literal. Its endpoint packet is nonzero, and its marked factorial
ratio and reciprocal factorial are regular; its rate is exactly the
first term in this comparison, up to polynomial factors. If the cut row
itself is assigned to the retained interval, the preceding physical row
has the same limiting rate by the uniform endpoint packet and continuity.

The full cap sum can still cancel those rows coherently. The conclusion
only rejects this particular cutoff. A wider endpoint-source strip,
or an additional coherently deformed outer piece, is needed. The exact
wrapped Fourier factor remains part of any final cap contraction.

Run from the repository root:

```sh
python3 repro/diagnostics/2026-11-05-type-four-cap-cut-obstruction/check.py
```
