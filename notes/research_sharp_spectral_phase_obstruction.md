# A sharp spectral maximum does not by itself define the original torsor

Workspace research draft, 31 October 2026. Exact local result. This concerns the actual LEFT
coefficient, including its omitted-half scalar and unused rows. It exhibits
a strict real spectral maximum of its absolute leading rate for which the
usual positive-clock physical adapter cannot transport the original ordered
meridian pair. A missing sign character is identified explicitly. This is
NOT a global shared-source growth counterexample, nor an obstruction to a
properly constructed signed-clock/phase adapter.

## 1. A literal coefficient with one protected outer face

Use the original even-level notation

    N=2m, d=N-1,
    alpha_r(delta)=4cos²(pi(r+1/2)/N)-4sin²(pi delta),
    s_r=2sin(pi r/N).

Set y=0. Then every dimer vanishes, so the actual tail is the single
monomer product

    K_(i,j)=x^(j-i) product_(r=i+1)^j s_r².

Consequently the coefficient of x^(j-i)b^i c^(d-j) in the original LEFT
factor, up to its recorded overall sign, is EXACTLY

    a_N(delta)=A_rest(delta)
               product_(r<i) alpha_r(delta)
               product_(j<r<m) alpha_r(delta)
               product_(r=i+1)^j s_r².                          (1)

This follows from actual_global_left_weighted_spectral_envelope.md (1);
no absolute recurrence or endpoint replacement has been introduced.

Take N divisible by12, i=N/6, j=N/3 and delta=1/4. The omitted-half
Chebyshev scalar has modulus2, since m is divisible by6 and sigma=0.
No alpha_r vanishes: its zero would require r+1/2=N/4, with an integer
right side. Thus (1) is nonzero at every one of these levels.

More generally, write mu=i/N, nu=j/N and assume

    0<mu<t_c=1/2-delta<nu<1/2.

The unused intervals avoid the moving zero. Their absolute Riemann rate,
with the same monomer interval and zero-rate omitted half, is

    h_delta(mu,nu)
      = integral_0^mu log|alpha(t,delta)|dt
        +integral_nu^(1/2) log|alpha(t,delta)|dt
        +integral_mu^nu log(4sin²(pi t))dt,                     (2)

    alpha(t,delta)=4[cos²(pi delta)-sin²(pi t)].

At the specified point (2) is the ACTUAL coefficient limit
N^(-1)log|a_N(1/4)| along N divisible12. The smoothly varying rate
functional (2) is not asserted to approximate through every dense zero
of A_rest on a fixed spectral interval.

## 2. A strict free-spectral maximum and all row equations

Hold mu=1/6 and nu=1/3 fixed. At delta=1/4,

    alpha(t)=2cos(2pi t), alpha_delta=-4pi,
    alpha_(delta delta)=0.

Reflection t ->1/2-t interchanges the two unused intervals and negates
alpha. Hence direct differentiation of (2) gives

    partial_delta h=0,
    partial_delta² h
       =-4pi² [integral_0^(1/6) sec²(2pi t)dt
                +integral_(1/3)^(1/2) sec²(2pi t)dt]
       =-4pi sqrt(3)<0.                                        (3)

This is a strict interior maximum in the FREE real spectral coordinate.
No branch-contour assertion is involved.

At shared positive face multipliers x=b=1,c=3, add the original degree
terms mu log b+(1-nu)log c to (2). The x term is zero because x=1.
Both row equations hold as well. Indeed, with y=0,

    L_delta(t)=sin²(pi t)/|cos²(pi delta)-sin²(pi t)|,
    L_(1/4)(1/6)=1=b, L_(1/4)(1/3)=3=c.                      (4)

Thus partial_mu=log b-log L(mu)=0 and
partial_nu=log L(nu)-log c=0. The outer-degree constraint is literal:
xi=nu-mu=1/6, since all outer degree lies at x and y is protected.

These are exactly the local real equations one would encounter when
using (2) as an absolute-rate functional with common face multipliers.
The local datum need not extend to a globally maximizing shared flow;
no such extension is claimed.

## 3. The original physical Casimir fails on one leg

For the original physical adapter H/(bc)^(d/2), the endpoint derivatives
of the absolute stationary action give

    p_in=exp(-2pi i mu), p_out=exp(-2pi i nu).                  (5)

This is the LEFT sign convention of the calibrated endpoint Green
calculation, including its integer c character; inversion of either p
does not change the following scalar test. The original crossing
Casimir in the same clock chart is

    Sigma(z,p)=2+[(p-1)²/p] (z+x)(z+y)/z².                     (6)

It is the actual principal formula in
notes/actual_cross_cofactor_marked_action.md (12), not a freely chosen
trace convention. Equal whole ordered products necessarily have equal
traces, independently of the common scale or outer momentum.

At the exact datum (3)--(4),

    p_in=(1-i sqrt3)/2, p_out=(-1-i sqrt3)/2,
    Sigma(1,p_in)=0=sigma,
    Sigma(3,p_out)=-2 != sigma.                               (7)

Thus these positive-clock absolute equations cannot supply the original
pair-preserving centralizer. The discrepancy is not repaired by choosing
the reciprocal spectral eigenline. In contrast

    Sigma(-3,p_out)=0.                                       (8)

The output's row equation after the pole is the conic with c replaced
by -c. This is a genuine clock sign, not a zero spectral boundary or
a discarded protected-face singularity.

An all-positive companion exists: x=y=b=1,c=5, delta=1/4,
sin²(pi mu)=1/8, sin²(pi nu)=25/32, and xi=(nu-mu)/2.
Symmetry gives the unique outer tilt x/y=1. The absolute stationary
spectral derivative vanishes, with fixed-row second derivative
-2pi sqrt7. Its two positive-clock traces are0 and -5/2, and replacing
c by -5 gives0. The protected monomer example above is sufficient and
does not need a general coefficient Legendre theorem.

## 4. The exact character that the modulus discarded

In the strict straddling regime every unused prefix row r<i has
alpha_r>0, while every unused suffix row j<r<m has alpha_r<0.
Its EXACT sign is

    (-1)^(m-1-j)=(-1)^(d-j) (-1)^(m-1-d).                     (9)

The first factor depends on the physical c exponent. It is precisely
the change c -> -c in that summand; the second is a retained scalar.
The omitted-half scalar A_rest is still present and has its own two
oscillatory Chebyshev modes. Its zero exponential modulus does not
license deleting its phase or its derivatives.

At even levels these modes can be printed exactly:

    A_rest=2(-1)^m cos(N pi delta)
          =(-1)^m[exp(i pi N delta)+exp(-i pi N delta)].        (10)

For odd N=2m+1 the exact formula from the same source is

    A_rest=4(-1)^m sin(pi delta) sin(N pi delta).

On a fixed strict spectral interior its two exponential modes have
the same derivatives +/-i pi; the displayed sine prefactor has zero
principal derivative after division by N. No endpoint continuation
of that prefactor is assumed.

Within the strict straddling chamber the suffix sign in (9) is
independent of delta. Thus the principal spectral derivative of each
of these two RETAINED modes is

    partial_delta h + i pi,  or  partial_delta h - i pi.        (11)

At (3) it equals +i pi or -i pi, not zero. A consistent face-character
absorption changes only the recorded integer monomial phase and does
not remove (10). If a corresponding actual longitude-polarized
representation were constructed, its normalization U=partial_delta A
would therefore give U=+/-i pi, hence M²=-1, rather than a killed
meridian. This last sentence is a conditional interpretation using
the existing primitive-log convention, not a representation constructed
from the absolute datum.

Therefore partial_delta h=0 asserts stationarity of a REAL absolute
rate only. It does not imply that the full complex original phase has
zero primitive auxiliary meridian log, nor that a formally written
ratio H_c/E_b=1 is its actual primitive collar.

The endpoint identity/hybrid construction at delta=0 does not see this
post-pole character, because no pole lies inside a strict lower interval.
Extending that construction requires a consistent shared face-character
assignment and the original omitted-half/peripheral phases. It cannot
follow from the absolute row and spectral equations alone.

This identifies a precise missing adapter, not an impossibility theorem.
A signed-clock assignment could restore the two conics locally; whether
those signs sew at every original face, cup, cap and unrestricted mark
is a separate incidence and phase problem.

The historical diagnostic for this calculation is not included in the public reproduction suite.
