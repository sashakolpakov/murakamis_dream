# The simultaneous many-head Ward gap is a separate problem

28 October 2026. The proved polynomial inverse for an actual
[two-head lowering current](actual_two_head_ward_polynomial_contraction.md)
does not yet give an inverse for arbitrary many-head constraints.
This note records a reproducible test and an exact identity identifying
the full system worth studying. It proves no new asymptotic spectral
bound and reports no counterexample to such a bound.

## 1. The actual physical operators

At the canonical complete color, put

    Q=exp(2pi i/N), x=-exp(-pi i/N),
    F_one e_a=(1-Q^(a+1))e_(a+1),
    Ecal_one e_a=-(1-Q^(-a))e_(a-1),
    K_one e_a=x Q^-a e_a.

Here Ecal=rho^2 E in the original balanced physical frame. This
polynomial scalar rescaling retains the actual Ward equation.
For b heads use the ACTUAL coproducts

    F_b=sum_j K_1^-1...K_(j-1)^-1 F_j,
    Ecal_b=sum_j Ecal_j K_(j+1)...K_b.

Let P reverse the physical heads. Since K is unitary and
Ecal_one=-F_one^*, directly

    Ecal_b=-P F_b^* P.                                  (1)

In total-degree blocks this is

    Ecal_s=-P_(s-1) F_(s-1)^* P_s.

Thus the simultaneous Ward normal operator is exactly

    F_s^*F_s+P_s F_(s-1)F_(s-1)^*P_s.                   (2)

This identity uses the original physical metric, not a nonunitary
fusion similarity. It holds in every head number at this complete
color. No claim that (2) has a uniform spectral gap follows from
the identity alone.

There is also an exact Hermitian formulation. On the full physical
tensor space put D=F_b+Ecal_b. Equation (1) gives

    (P D)^*=-P D.

Thus iP D is Hermitian. For a vector in a single total degree,
the F and Ecal outputs are orthogonal, so ||Dv||^2 is precisely
the simultaneous Ward energy (2). This is a folded Hermitian
Dirac formulation in the original metric. Its spectral estimate
remains to be proved; Hermiticity alone does not bound a gap.

There is a further exact kernel issue: the full Dirac kernel need
not be graded. Already at one complete physical head, N=5, write
c_r=1-Q^r and

    v=e_0+[c_1/conjugate(c_2)]e_2+e_4.

Then (F+Ecal)v=0 by the two odd-row recurrences, whereas neither
F e_2 nor Ecal e_2 vanishes. The degree-2 component is nonzero and
obeys K=1, since x=Q^2. Thus even on the required K=1 slice,
projection of the FULL Dirac kernel is not the joint Ward kernel.
A gap for the global Hermitian Dirac would require an additional
kernel-angle estimate before yielding the fixed-degree stacked
inverse. This is why the target remains the actual Gram (2).

## 2. The exact Gram matrix has nontrivial magnetic triangle flux

Write H_s=F_s^*F_s+Ecal_s^*Ecal_s, and let a be a physical head
state of total degree s. Its diagonal is exactly

    H_s[a,a]=4 sum_i [sin^2(pi(a_i+1)/N)+sin^2(pi a_i/N)].

For i<j, a_i<d and a_j>0, set a'=a+e_i-e_j and
M=sum_(i<h<j)a_h. Direct multiplication of the two actual coproducts
gives the off-diagonal entry

    H_s[a',a]=8 q^-1 sin(pi(a_i+1)/N)sin(pi a_j/N)
       *cos((j-i)phi-pi(a_i+a_j+2M)/N),                 (3)

where q=exp(pi i/N) and phi=Arg x=pi-pi/N. All other
off-diagonal entries vanish except the Hermitian reverse edges.
Equivalently the real cosine factor in (3) is

    (-1)^(j-i) cos[pi(a_i+a_j+2M+j-i)/N].

For clarity, the F^*F contribution before combining phases is

    x^(j-i)Q^(-a_i-M-1)
                         (1-Q^(a_i+1))(1-Q^-a_j),

and the Ecal^*Ecal contribution is

    x^(i-j)Q^(a_j+M-1)
                         (1-Q^(a_i+1))(1-Q^-a_j).

Their sum is exactly (3). No asymptotic symbol or K=1 approximation
is used in this calculation.

Consequently a diagonal unitary vertex gauge CANNOT in general make
this Gram matrix an ordinary real weighted graph Laplacian. There is
an explicit countertest inside the actual K_total=1 sector: take
b=4, N=5, s=8, and the triangle

    a=(1,1,2,4), b=(2,0,2,4), c=(2,1,1,4).

Put k=(5-sqrt(5))/2. Equation (3) and the elementary golden-angle
sine identities give exactly

    H[b,a]=k q^-1, H[c,b]=k q^-1, H[a,c]=-sqrt(5)q,
    H[b,a]H[c,b]H[a,c]=-sqrt(5)k^2 q^-1.               (4)

The triangle product is nonreal. It is invariant under every
diagonal unitary gauge, while any matrix with real off-diagonal
entries has real products around all such triangles. All three
states obey K_total=1 since x^4Q^-8=1. Thus this obstruction is
present on the required actual invariant-weight fiber, not only
on another degree or a hypothetical kernel.

This does not refute a polynomial simultaneous Ward bound, a
magnetic/Hodge comparison, or a nonlocal unitary decomposition.
It rules out the direct real-path argument obtained by simply
gauging away all global phases. The two-head path proof has no
triangles and does not encounter this obstruction.

There is nevertheless an EXACT norm-preserving realification at all
head numbers. The entry formula and reversal of the interval i,...,j
give

    P_s H_s P_s=conjugate(H_s).

Define P_+=(I+P_s)/2, P_-=(I-P_s)/2, and

    U=P_++iP_-=[(1+i)/2]I+[(1-i)/2]P_s.

Then U is unitary, mixes only a state and its physical reversal, and

    U^* H_s U=Re H_s-P_s Im H_s                            (5)

is REAL SYMMETRIC. Indeed the real part commutes with P_s and
the imaginary part anticommutes with it. This proves (5) directly.
It is a sparse two-state mixing with condition number one, not
an exponentially conditioned fusion transformation.

The resulting real matrix has signed interactions and no automatic
diagonal-dominance or Laplacian comparison. Thus the triangle test
rules out a diagonal phase gauge, while (5) supplies a valid more
general unitary reduction. Any use on the original source must
transform the currents and source by this same specified U.

## 3. Four-head diagnostic at the actual two-cup degree

For b=4 choose s=2(N-1), exactly the total integer degree of two
original cups. The regular Borel decomposition has full length-N
strings, so the exact rank of F_s is

    rank F_s=h_4(s)-h_3(s-(N-1)),

where h_b(s) is the coefficient of t^s in (1+...+t^(N-1))^b.
This fixes which singular values are nonzero without numerical
thresholding. The original physical matrices give the following
resolved nonzero F gaps:

    N= 4: 1.08239220
       6: 0.43260052
       8: 0.18973845
      10: 0.08478187
      12: 0.03780617
      14: 0.01676550
      16: 0.00740054
      20: 0.00142953.

The exact zero cluster remains below 9e-15 in these diagnostics.
This rapid decay warns against carrying the two-head estimate over
to F_b by an unproved iteration. These finite values alone DO NOT
prove exponential decay or disprove every polynomial estimate.

Crucially, keeping BOTH actual Ward currents changes the picture.
For [F_s; Ecal_s] the computed smallest nonzero values are

    N= 4: 1.20597689
       6: 0.62788204
       8: 0.39963573
      10: 0.28269084
      12: 0.21347310
      14: 0.16854041.

The observed joint kernel dimension is N at these levels. The
joint gap is consistent with a polynomial bound, which is not
proved here. In particular the F-only diagnostic is not an
obstruction to a polynomial simultaneous Ward contraction.

## 4. The remaining constructive target

A useful many-head theorem must solve the compatible simultaneous
current system with its joint kernel and cokernel retained. Its
exact Gram is (2)--(3), (4) rules out a diagonal phase removal,
and (5) gives a condition-one sparse realification. It
must not impose a separate invariant-pair equation at an intermediate
slice where interbridge crossings have mixed the pair channels.
Equations (1)--(2) provide an actual fixed-metric formulation of
that target. The local two-head bounds and the
[cyclic Ward-wall contraction](ward_cyclic_wall_contraction_and_marked_augmentation.md)
are valid inputs; compatibility and a simultaneous spectral estimate
are further work.

Even a proved polynomial simultaneous inverse would transport exact
currents, not identify a positive geometric kernel or prove the
selected scalar's volume rate by itself.

[Reproduce the diagnostic](../experiments/audit_global_four_head_ward_gap.py).
The default levels stop at N=12; `--larger` adds N=14,16. Larger
resolved F-only values above were separately computed in the same
physical basis; a contemplated N=24 dense SVD was interrupted.
