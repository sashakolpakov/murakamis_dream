# Adaptive Fermat sampling preserves the entire original crossing source

28 October 2026. The internal root-orbit source may be placed on its
exact Fourier resonance without changing the original finite crossing
operator. Its sampling point is allowed to depend on the input/output
heads. The old degree-zero restriction is replaced by two explicit
physical source walls. This is not an unsupported central base change
or a modification of one homogeneous summand.

The resulting source-flat family has a first-normal-jet reconstruction
at resonance, with jet order independent of N. It fixes the whole
finite state, including its currents. It does not prove a global
geometric coefficient is nonzero.

## 1. Complete Laurent kernel and its only alias

Put Q=exp(2*pi*i/N), d=N-1, retain the actual color x and scalar
kappa, and use the COMPLETE positive crossing polynomial

    K(t)=B_N(t/z_1,x^(-1)t/z_0)
         R_N(z_6/z_0,x^(-1)z_6/t)
         B_N(x^(-1)z_7/z_6,x^(-2)z_7/t).              (1)

The physical crossing is its original finite input/output block,
with kappa retained. This is the proved Gaussian-absorbed complete
kernel; no original Gaussian was deleted from a separated sector.

Expand the three factors with indices (i,j),(r,k),(h,l), respectively,
each nonnegative pair having sum<N. One term has

    input demands a=j+r, b=i,
    output degrees c=r+k-h, e=h+l,
    t exponent p=i+j-k-l,
    c+e-a-b=-p.                                      (2)

In particular input powers are nonpositive, second-output degree is
at most d, both output degrees are at most d, and -2d<=p<=d.
For any nonzero sampling root t_0,

    (1/N)sum_(j=0)^d K(t_0 Q^j)
               =CT_t K+t_0^(-N)[t^(-N)]K.             (3)

There is exactly one possible alias. This identity is an equality
of the COMPLETE finite Laurent kernel before any source split.

## 2. A source-flat adaptive family, including exact resonance

Let A be an independent scalar source parameter. Choose the algebraic
sampling root by

    t_0^(-N)=z_1^(-N)-A z_7^(-N).                    (4)

The normalized symmetric root average is independent of which Nth
root is chosen. Equations (3)--(4) show its two errors explicitly:

    z_1^(-N)[t^(-N)]K-A z_7^(-N)[t^(-N)]K.            (5)

The FIRST term demands incoming second index at least N, since K
has no positive powers of z_1. The original finite INPUT space kills
it. The SECOND term has negative second-output degree, since K
has z_7 degree at most d. The original finite OUTPUT block kills
it. Therefore the adaptive average has EXACTLY the original finite
crossing operator, for EVERY A, not merely its closed trace.

This is stronger than the earlier total-degree alias argument. The
root t_0 has overall head degree one, so that argument alone would
not apply. The two physical index walls in (5) are the replacement.
No alias deletion is asserted for a separately continued full-Psi
homogeneous/current sector.

The symmetric average is linear in t_0^(-N). It consequently extends
regularly across z_1^(-N)-A z_7^(-N)=0, even though the individual
sample points then go to infinity. One first takes the COMPLETE
symmetric average and the original finite block, not a value of a
single divergent sample.

In the all-homogeneous one-Psi field, the full-turn multiplier is

    (z_7/z_1)^N[1-(z_1/t_0)^N]=A.                    (6)

Thus A=1 is precisely its exact Fourier resonance. It is reached
inside an actual source-flat family, rather than by imposing A=1
inside the old co-source. The normalized finite-orbit/Fourier formula
then has zero FINAL closure current and its explicitly known nonzero
resonant coefficient. The pre-existing B/R currents must still be
kept unless a further proved source map removes them.

The stronger independent external-frame construction in
[the balanced crossing theorem](actual_balanced_fourier_crossing_kernel.md)
also balances all three B/R sources. That theorem is compatible with
the present head-adaptive source map; it is not assumed in its proof.

## 3. Both signs and whole original words

At complete color x=-q^(-1), the exact balanced relation is
R_-=P overline(R_+)P, with the common scalar conjugated to kappa^(-1).
Apply this relation to the COMPLETE polynomial source, with opposite
root Q^(-1) and the formal two heads exchanged. Its adaptive negative
sampling is

    t_(0,-)^(-N)=z_0^(-N)-A z_6^(-N).                (7)

The errors now demand first INPUT index at least N or have negative
first OUTPUT degree. Both are removed by the SAME original physical
finite blocks. This is an exact negative source representation, not
a fixed-value balance of the old negative continuous Gaussian.

Hence any number of crossings in ANY original signed braid or plat
may be replaced simultaneously. Their finite matrices agree entrywise,
and the original cups/caps, pivot, marked row, Cartan and zero-framing
lines are unchanged. Arbitrary bridge count is allowed.

There is also a raw no-healing formulation: the two complete modified
kernels still have only nonnegative input demands and output upper
bound d. A negative output cannot be healed at the next touching
kernel, since that input has no such coefficient; an input demand
at least N cannot be supplied by any preceding output. The original
finite end sources kill surviving untouched invalid heads. This
does not authorize arbitrary Laurent coupons that change that support.

## 4. The unsplit cyclic inhomogeneous equation

The COMPLETE state has a concrete cyclic connection, not only the
one-function homogeneous equation. Put

    u_0=t/z_1, v_0=x^(-1)t/z_0,
    a=x^(-1)z_7/z_6, c=z_6/z_0, w=x^(-1)z_6/t,
    B_0(t)=B_N(u_0,v_0), F(t)=B_N(a,a w)R_N(c,w),
    Y(t)=B_0(t)F(t)=K(t),
    D_0=1-u_0^N+v_0^N,
    H_pair=D_B R_N(c,w)+a D_R B_N(a,Qa w).

The exact finite Newton/Rogers Ward equations imply POINTWISE

    Y(t)-b(t)Y(t/Q)=eta(t),
    b(t)=(z_7/z_1)(1-Q z_1/t),
    eta=B_0(t)H_pair(t)+(Qac/v_0)D_0 F(t/Q).           (8)

Indeed F(t)-ac F(t/Q)=H_pair(t), and
v_0 B_0(t)=(u_0-Q)B_0(t/Q)+Q D_0. Multiplying these two
identities proves (8) with every endpoint and source norm present.
In particular the source eta is not declared zero on resonance.

At t_j=t_0 Q^j, let Y_j=Y(t_j), eta_j=eta(t_j), and define

    (T_A v)_j=b(t_j)v_(j-1), j modulo N.

Then T_A^N=A I by (6), and the actual state satisfies

    (I-T_A)Y=eta.                                    (9)

All these are finite algebraic functions on the specified sampling
cover; no formal WKB expansion or choice of a new period is involved.

## 5. Resonant first-normal-source reconstruction

On a regular local chart of the cover (4), let

    G_A=I+T_A+...+T_A^(N-1).

The exact geometric-series identity gives

    G_A eta=(1-A)Y.                                  (10)

At A=1 the left side vanishes. Since the whole original state is
regular on this chart, differentiating the ACTUAL source family gives

    Y|_(A=1)=-d_A(G_A eta)|_(A=1).                   (11)

Thus the entire resonant finite state is fixed by the first normal
jet of its explicit unsplit source, with jet order ONE independent
of N. This is a source identity, not an instruction to divide by
1-A and separately evaluate a vanishing numerator.

For an explicit homogeneous coefficient choose a holomorphic branch
omega=A^(1/N) near one and the periodic cyclic gauge g_j(A), g_0=1,

    b(t_j)g_(j-1)=omega g_j.

All b(t_j) are nonzero at resonance. Write tildeY_j=Y_j/g_j and
tildeeta_j=eta_j/g_j. Averaging their equation yields

    mean(tildeeta)=(1-omega)mean(tildeY).

Consequently its zero-clock homogeneous projection coefficient is

    mean(tildeY)|_(A=1)
                 =-N*d_A mean(tildeeta)|_(A=1).        (12)

The normalized homogeneous vector g_j at resonance is the actual
Fermat/cyclic full-Psi vector with the independently fixed Fourier
normalizer. Equation (12) constructs its comparison coefficient
from the original source, rather than assuming that coefficient
exists or is nonzero. Its possible vanishing and its geometric
overlap after exterior contraction still have to be checked.

For a fixed word with m internal orbit variables, apply (10) to
each complete tensor factor before the original finite contraction.
The whole original period is thereby a mixed FIRST normal derivative
in each of m independent source parameters at their Fermat values.
The required jet order depends on the fixed word, not on N. These
derivatives include the moving root and all source terms; differentiating
only a homogeneous block would not be the same operation.

## 6. Scope

The adaptive sampling and normal-source formulas are exact, source
preserving and valid for all original signed finite words. They close
an actual internal circle on its resonant algebraic multisection and
give a prescribed normal-jet pointing there. Neither the one-dimensional
homogeneous space nor its nonzero local Fourier vector by itself
proves survival of the final geometric period. That remaining claim
cannot be obtained by invoking divisor rigidity without the actual
global source coefficient supplied by (12) and the exterior pairing.
