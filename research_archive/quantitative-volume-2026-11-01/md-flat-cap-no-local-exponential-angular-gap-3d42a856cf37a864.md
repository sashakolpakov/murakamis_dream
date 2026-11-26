# A flat cap has no uniform local exponential angular mismatch bound

Private exact source observation, 31 October 2026. This is a limitation of
one local phase estimate, not a lower bound for the original shared source
or its filling period.

At the residual cap x=b=0, sigma=2, the literal raw coefficient is

    [c^(d-j)y^j] H_V=(-1)^j A_j,
    A_j=csc²(theta/2) prod_(r=1)^j
                     sin²(r theta)/sin²((r+1/2)theta),
    theta=pi/N, d=N-1.                                (1)

All original unused factors and the raw sign are retained. For
0<=j<=M=floor(N/2)-1, the sequence A_j is positive and decreasing,
because sin(j theta)<=sin((j+1/2)theta) on this range. Also

    A_j<=A_0=csc²(theta/2)<=N².                        (2)

The monotonicity of sine gives the telescoping lower bound

    prod_(r=1)^j sin(r theta)/sin((r+1/2)theta)
        >=prod_(r=1)^j sin(r theta)/sin((r+1)theta)
        =sin theta/sin((j+1)theta).

Consequently, for N>=3,

    A_j>=4cos²(theta/2)/sin²((j+1)theta)
        >=4cos²(theta/2)>=3.                          (3)

Fix 0<a<b<1/2 and choose integer endpoints L_N~aN, U_N~bN with
U_N-L_N even. They lie in the original LEFT range for large N. At the
ordinary positive radius and common phase c=y=1, its sharp stop-window
polynomial and actual absolute envelope are

    W_N=sum_(j=L_N)^(U_N)(-1)^j A_j,
    E_N=sum_(j=L_N)^(U_N)A_j.

Pairing consecutive terms of the decreasing sequence and keeping the
last term gives

    |W_N|>=A_(U_N)>=3,    E_N<=N³,
    |W_N|/E_N>=3/N³.                                 (4)

The actual cap character is aligned only when the c and y phases differ
by pi. At the phases used in (4), they are equal, so their distance to
that supported alignment is pi/2. Nevertheless no fixed constants
C,kappa>0 can satisfy |W_N|<=C exp(-kappa N) E_N on all these levels.
The retained alternating terms leave endpoint currents of at least
polynomial size; there is no strict local stop-action gap at the cap.

Therefore the regular-window angular theorem cannot be extended to a
flat cap merely by assigning it the same opposite-sign incidence labels.
An odd MAIN cycle involving such a cap does not by itself supply the
product-envelope exponential loss used by the regular cycle-packing
argument. This does not exclude cancellation after ORIGINAL shared
coefficient extraction, a combined analytic block estimate with other
ports, or a different source-preserving treatment of the cap boundaries.
It makes no assertion that W_N occurs uncoupled in the full invariant.

The proof is exact at every N>=3 for the stated endpoints and uses no
asymptotic coefficient formula or numerical experiment. Full review pending.
