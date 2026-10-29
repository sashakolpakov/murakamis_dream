# The Fourier framing fiber is a projective line with one intrinsic pole

Research proof, 27 October 2026. The new momentum coordinate has a
simpler description than the quadratic position projection: on every
regular fixed-cut fiber it is a Möbius coordinate. Its only pole in
the framing density is fixed by the developed prefixes, independently
of the cut position. This is an identity of rational functions before
any quantum expansion. It also computes the exact cyclic norm of the
principal density, with its exceptional factors retained.

This calculation concerns the geometric framing density. Its finite
root sampling is not asserted to be the Gaussian pushforward of the
original finite source. The actual zero-source current in
[the Fourier source audit](actual_fourier_source_cancellation.md)
explains why a nonzero local geometric block alone cannot establish
that assertion.

## 1. The rank-one difference removes the quadratic shell

Use the signed developed prefixes U,V of
[the actual Fourier polarization](actual_fourier_polarized_geometric_normal_block.md),
with det U=det V=1 and UV inverse the nontrivial TRACE-TWO
meridian in that convention. Thus U-V has rank one. Choose a
factorization

    U-V=u v,   v=(a,b),   w=v V inverse=(c,d).

Here u is a column, v and w are rows, and w u=0. Rescaling u
and v inversely has no effect on the formulas below. Keep the
actual prefix sign sigma, equal to either +1 or -1.

For F(r,s)=[[r,1-r],[s,-s]], s nonzero, write

    V'=F inverse V F,   ell_V=V'_11,
    k=ell_U/ell_V,   C=U-kV,
    p=sigma (F inverse C F)_12/(k-1).

The last equation is the ACTUAL balanced second-edge momentum,
not a definition of the independent finite Fourier-band variable.
The principal stationary incidence is eta_F=p inverse, with the
same scope as the actual Fourier theorem.

On the regular open where these expressions are defined,

    p=sigma [c(1-r)-ds]/[ar+bs],                         (1)
    r=[sigma(c-ds)-bsp]/[ap+sigma c].                    (2)

Here is a direct proof. The first row of F inverse(U-V)F is a
scalar multiple of vF. Hence, denoting its first two entries by
ell_D,beta_D,

    beta_D/ell_D=(vF)_2/(vF)_1.

Since k-1=ell_D/ell_V,

    p/sigma=(beta_D/ell_D)ell_V-(V')_12.

For a determinant-one matrix V', its inverse gives

    (vF)_2 ell_V-(vF)_1(V')_12=(v V inverse F)_2.

This is exactly (1), and solving (1) gives (2). The calculation
uses the full prefix matrices and the original sign. It does not
pass through a choice of square root of the position discriminant.

Put

    Delta(s)=sigma [s(ad-bc)-ac].

Then

    partial_p r=Delta(s)/(ap+sigma c)^2.                  (3)

If Delta(s) is nonzero, (1)-(2) extend to mutually inverse maps
of projective lines over the marked prefix field. The excluded
values of s are explicit. The previously proved discrete-faithful
argument ensures Delta(s) is not identically zero for an actual
independent second position. No additional framing cover is needed.

## 2. The pole is intrinsic and does not move with the cut

Suppose a is nonzero. Define

    lambda=-sigma c/a,   D(s)=Delta(s)/a^2.

Then r=infinity corresponds to p=lambda, and

    dr=D(s) dp/(p-lambda)^2                            (4)

on a fixed-s fiber. In particular the pole lambda is independent
of s. If a=0, nondegeneracy forces c nonzero and r is affine in p;
the corresponding pole is p=infinity. If c=0 and a nonzero, it is
p=0. These cases are retained, rather than divided away.

There is also a coordinate-free prefix expression on a regular
chart. Put K=UV inverse. If c_U-c_V is nonzero, then

    lambda=-sigma c_K/(c_U-c_V),                         (5)

where c_W is the lower-left entry of W in the marked cut frame.
Indeed c_U-c_V=u_2 a and c_K=u_2 c. The same ratio is a marked
trace-word function, since for J=[[1,1],[0,1]],

    c_W=Tr(JW)-Tr(W).

Consequently this pole belongs to the fixed marked character field;
it is not a free additional framing parameter. Formula (5) is not
used on its vanishing-denominator chart; (1)-(4) remain the defining
expressions there.

## 3. The actual geometric density has an explicit cyclic norm

Retain the established geometric two-form and cut clock

    Omega_cut=-dr wedge ds/[s(1+s)],   A=1/(1+s).

Using (3) without discarding its orientation gives

    Omega_cut= -Delta(s) p/[s(ap+sigma c)^2]
                                      dlog A wedge dlog p. (6)

Thus in the finite-pole case its coefficient is

    T_s(p)=G(s) p/(p-lambda)^2,
    G(s)=-Delta(s)/(s a^2).                              (7)

Let Q be a primitive N-th root, lambda^N different from one.
The EXACT finite functional on this rational coefficient is

    (1/N) sum_(j=0)^(N-1) T_s(Q^j)
          =G(s) N lambda^(N-1)/(1-lambda^N)^2.             (8)

The original Fourier incidence samples p=Q^(-j), which has the
same finite set of values and hence the same functional. Equation
(8) is the logarithmic second derivative of

    product_(j=0)^(N-1)(1-lambda Q^(-j))=1-lambda^N.

It is the SAME elementary cyclic-norm identity already proved in
[the two-position density calculation](cyclic_framing_density_source.md),
now on the birational Fourier fiber, with no quadratic field trace.
The underlying differential (4) is exact, and its ordinary
logarithmic residue vanishes. That does not make (8) zero.

If lambda=0, (8) vanishes for N>1. In the pole-at-infinity case
the coefficient in (6) is a scalar multiple of p, whose average
also vanishes for N>1. For nonzero lambda off the unit circle,
the limit of (1/N) log of the modulus in (8) is
-abs(log abs(lambda)), provided G(s) is fixed and nonzero.
Thus rationality and birationality
alone do not provide a subexponential source estimate.

Before root specialization the retained product is

    P_N(Q,lambda)=product_(j=0)^(N-1)(1-lambda Q^(-j)).

Its logarithmic Q-normal derivative D_Q log P_N is the weighted sum
sum_j j lambda Q^(-j)/(1-lambda Q^(-j)). One cannot replace
P_N by 1-lambda^N before taking that derivative. The whole normal,
the norm-zero fiber and any cancellation with another source
factor must be kept. This is consistent with the explicit moving
norm pole of [the original factorial atom](actual_negative_band_boundary_moment_and_ward_atom.md).

## 4. An actual figure-eight prefix and the scope of the theorem

For the actual third prefix used in the polarization audit,
u^2+u+1=0 and

    V=[[1,1],[-u,1-u]],
    U=[[u+1,2u+1],[1-u,3-u]],   sigma=-1.

One can take u_column=(u,1), v=(1,2), w=(1+u,1).
Equations (1)-(3) become

    p=[s-(1+u)(1-r)]/[r+2s],
    r=[s-(1+u)-2sp]/[p-(1+u)],
    partial_p r=[(1+u)+(1+2u)s]/[p-(1+u)]^2.              (9)

The intrinsic pole is lambda=1+u=-u^2, of order six at either
geometric embedding. It is independent of the good cut phase.
For N divisible by six, principal-density sampling in (8) is
undefined. The original finite tensor and its source are regular.
Therefore simply sampling this principal density cannot be their
whole source formula. A genuine comparison must explain this
pole using the actual finite coefficients, walls and co-source.

The projective-line description (1)-(4), the intrinsic pole (5),
and the finite norm (8) are general prefix identities. They
simplify the geometric fiber and locate its escaping boundary.
They do not construct its quantum completion, show that the
original last cyclic sum has a nonzero geometric coefficient,
or prove the volume conjecture.

[The exact audit](../experiments/audit_mobius_fourier_framing.py)
checks these formulas against raw conjugated matrices, including
both prefix signs, finite and infinite poles, the figure-eight
number field and independent companion-matrix cyclic traces.
The [independent proof audit](mobius_and_flat_source_frame_independent_audit.md)
also verifies the orientation, intrinsic pole, exceptional-fiber
agreement and the distinction between the two normal divisors.

The subsequent [universal actual-cut theorem](universal_resonant_cut_and_actual_source.md)
shows that the prefix-dependent pole can be normalized to p=1
by a genuine braid/inverse insertion and a first-slot physical
cut, while preserving the original period and a regular geometric
chart. This does not make principal sampling legitimate: the new
density is resonant at every level. The full quantum source must
be transported, including that escaping boundary layer.
