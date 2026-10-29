# An independent audit of the Li–Wang regulator line

Research audit, 26 October 2026. The source is Weiping Li and Qingxue
Wang, [On the Generalized Volume Conjecture and Regulator,
arXiv:math/0610745v1](https://arxiv.org/pdf/math/0610745v1), the nine-page
2006 version. Its [version-specific HTML](https://arxiv.org/html/math/0610745v1)
was checked against the PDF. The earlier math/0604057 is not needed here.
This is a correctness and terminology audit, not a claim about novelty or
a proof of colored-Jones asymptotics.

The core flat regulator line is valid with logarithms continued along
paths. The paper does not construct our root-of-unity quantum norm
torsor. There are two distinct branch qualifications: a literal use of
the printed discontinuous logarithm fails, while an endpoint-only scalar
reading of its later special Chern–Simons integral requires additional
trivialization data. Neither qualification disproves the continued-log
regulator.

## 1. What the source actually supplies

The terminology is a flat line bundle: Introduction, p. 1; §3.2,
equation (3.6), pp. 4–5; and Remark 2(iii), p. 7. The universal
Heisenberg bundle's explicit construction is referred to Bloch and
Ramakrishnan, rather than written out. The inspected text contains
neither “torsor” nor “principal.” Proposition 3.2, p. 5, supplies a
K2-torsion assertion; Theorem 3.3, p. 6, deduces exactness and rational
periods. Equation (3.9), p. 7, remains a conjecture.
[Primary text, §§3.2–3.3](https://arxiv.org/html/math/0610745v1#S3.SS2).

Removing the zero section of a complex line gives an analytic principal
C* bundle. Calling that associated object a torsor is mathematically
legitimate. It is a translation of the line-bundle construction, not a
separate scalar norm equation or an identification with a quantum object.
The calculations below independently check the relevant construction.

## 2. Rebuild the logarithmic quotient and its connection

Set t=2πi. On the logarithmic cover of (C*)² write f=exp(F), g=exp(G).
The following deck transformations define an analytic line:

    D_(a,b)(F,G,z)=(F+t a,G+t b,exp(aG) z),
    a,b in Z.                                           (2.1)

Indeed, applying D_(a,b) and then D_(c,d) gives the product multiplier
exp((a+c)G+t cb)=exp((a+c)G). Thus the action is an actual action.
Local branches F_j=F_i+t a_ij, G_j=G_i+t b_ij give local fiber-coordinate
transitions z_j=exp(a_ij G_i)z_i; the same calculation checks their
cocycle.

Declare

    A=F dG/t,        nabla=d-A.                          (2.2)

Then A changes by a dG, the logarithmic differential of exp(aG).
Consequently (2.2) descends. In this declared convention its curvature is

    F_nabla=-dA=-dF wedge dG/t.                          (2.3)

On a smooth complex curve with f,g invertible, dF and dG are locally
holomorphic multiples of the same local parameter differential. Their
wedge is zero. The pullback connection is therefore flat. No K2 torsion
is needed for this flatness.

Lift a based loop γ starting with logarithms F0,G0. Write its endpoint
as (F0+t a,G0+t b). Parallel transport in (2.2) multiplies z by
exp(∫γ F dG/t). Comparing the endpoint fiber to the initial fiber
requires exp(−aG0), by (2.1). The holonomy is exactly

    r(f,g)(γ)=exp((∫γ F dG−G0 ∫γ dF)/t).                 (2.4)

This reproduces the source's (3.6), with continued logarithms. Shifting
F by t r and G0 by t s changes the numerator by
t²(rb−sa), so the exponential is branch independent. Concatenation
adds an extra t²ab' to the numerator, also invisible after exponentiation.
Flatness proves homotopy invariance; rank-one holonomy also gives the
usual base-point independence under transport.

There is a normalization issue in the printed curvature statements,
Proposition 3.1(1), p. 4, and Remark 2(iii), p. 7. With (2.4) fixed as
holonomy, the actual connection curvature in convention (2.2) is (2.3),
not the unnormalized dF wedge dG. The discrepancy is invisible after
restriction to a curve, where both vanish. A nonzero universal curvature
or Chern class must retain the connection convention and its factors
of 2πi. We do not use the source's unnormalized formula as such a
universal Chern–Weil identity.

## 3. Verify that the holonomy descends through the K2 relations

Bilinearity follows directly from (2.4). For antisymmetry, the sum of
the two numerators is

    ∫γ d(FG)−G0 ∫γ dF−F0 ∫γ dG=t²ab,

whose exponential after division by t is one.

The local tame-symbol calculation can also be done without a cited
proof. At a puncture with parameter w, let

    f=w^a u(w),  g=w^b v(w),  u(0)v(0)!=0.

On a small positive circle, continuous logarithms give the limiting
numerator/t as bF0−aG0+tab/2. Its exponential is

    (−1)^(ab) u(0)^b/v(0)^a.                            (3.1)

The radius-dependent powers cancel. Flatness on the punctured disc
identifies this limit with the actual small-loop holonomy.

For the Steinberg relation, first use f=w,g=1−w on
P1 minus {0,1,infinity}. The small-loop values at both 0 and 1 are
one by (3.1). These loops generate its fundamental group, so the
character is trivial. Pulling back along f proves r(f,1−f)=1 on its
domain. Thus the homomorphism out of the symbol presentation of K2
is verified here, including its tame signs. One need not assume a
published dilogarithm argument for these particular checks.

## 4. Exactly what torsion gives

Suppose q{l,m}=0 in the function-field K2. Then (2.4) has q-th power
one. If the relation is initially realized after deleting extra points,
the inclusion of that smaller punctured curve surjects on the fundamental
group of the larger one; the already-defined character therefore has
q-th power one on the source's Y_h as well. Its image has order
**dividing** q. Equality with the K2 order is not required and is not
implied by applying a homomorphism.

The transfer arithmetic in Proposition 3.2 is correct: if restriction
to a degree-n field extension kills 2{l,m}, then transfer back gives
2n{l,m}=0. This audit has not independently rederived, from a knot
presentation, the existence of that finite extension or the cited
order-two statement in it. Those are the geometric K2 inputs to the
paper's knot-wide application. They are explicitly kept separate from
the directly verified regulator construction and its conditional
consequences.

For those consequences write F=log l=x+iu and G=log m=y+iv,
continuing u,v on the path. Integration by parts on a closed loop gives

    Im(∫ F dG−G0 ∫ dF)=∫(x dv−y du),
    Re(∫ F dG−G0 ∫ dF)=−∫(y dx+u dv)+v0∫du.           (4.1)

The boundary contribution in the first identity cancels the real part
of G0 ∫dF. At the paper's complete base point m0=1, choose G0=0.
Finite-order holonomy then gives

    ∫γ (x dv−y du)=0,
    (q/(4π²))∫γ(y dx+u dv) is an integer.              (4.2)

The first integrand is a globally defined closed real form; all its
periods vanish, so it is exact. The second is a continued-branch
integral. Changing the initial branch u by 2πk changes its normalized
value by an integer multiple of q. This verifies the substantive
quantization deduction under the K2-torsion hypothesis. It gives finite
monodromy and a trivial q-th tensor power of the flat line, not a
pointing of the original line and not a quantum asymptotic estimate.

## 5. A literal fixed-cut reading fails; the continued-log reading survives

Immediately after (3.6), p. 4, the source fixes 0≤arg z<2π and
describes the discontinuity on the positive real axis. A literal
pointwise insertion of this discontinuous log into the integral cannot
define the asserted regulator. Continuous path logs, or equivalent
transition contributions at cuts, are necessary.

An exact diagnostic uses the algebraic curve

    l=−z, m=z, z in C*, base point z=1.                 (5.1)

Its symbol {−z,z} is zero: the Steinberg relation applied to z and
z^(-1) gives {z,z}={z,−1}, hence {z,−z}=2{z,−1}=0.
Thus its K2 order is q=1. On z=exp(iθ), 0≤θ≤2π, continuous
logarithms give arg l=π+θ and log m0=0. Therefore

    ∫ log l dlog m=−∫_0^(2π)(π+θ)dθ=−4π²,
    r(l,m)=1.                                         (5.2)

With pointwise 0≤arg l<2π, arg l instead jumps at θ=π. The
same integral becomes

    −∫_0^π(π+θ)dθ−∫_π^(2π)(θ−π)dθ=−2π²,
    literal_fixed_cut_r(l,m)=−1.                       (5.3)

The corresponding normalized real period is 1/2 rather than an
integer. This is a counterexample to the **literal fixed-cut reading**
of the general construction and quantization inference. It is not a
knot A-curve counterexample and does not contradict (2.4) or (4.2).
Interpreting (3.6) using continued logs repairs this issue.

## 6. The later special invariant needs its path or endpoint frame

After Remark 2(iii), p. 7, the paper defines, for a path c from the
complete base point to (l,m), the quantity

    U_c=−q∫c(y dx+u dv).                               (6.1)

Remark 3, on the same page, describes U/(2π)² as well-defined in
R/Z. The path is indeed present in the preceding definition. On that
marked path domain (6.1) is a meaningful quantity. The assertion cannot
be inferred as a single-valued function of an **unmarked endpoint**
from the closed-loop statement (4.2) alone.

To see the obstruction, insert a based loop γ before c and let
a=wind_γ(l). The l logarithm on the following copy of c has changed
by 2πia. Consequently

    U_(γ*c)−U_c=U_γ−2πq a∫c darg m,
    (U_(γ*c)−U_c)/(4π²)
       =−q a Δ_c arg(m)/(2π) mod Z.                   (6.2)

The right side is generally not integral. For (5.1), let c_θ run
from angle 0 to θ with continuous arguments. Direct integration gives

    U_(c_θ)=−πθ−θ²/2,
    U_(c_(θ+2π))−U_(c_θ)=−4π²−2πθ.                    (6.3)

At θ=π/2 the difference divided by 4π² is −5/4. Thus even the
valid continued-log interpretation does not make this integral a
function of the unmarked endpoint on a general torsion-symbol curve.
The same obstruction (6.2) applies on any curve possessing the stated
winding loop and a path with the indicated nonintegral endpoint phase;
we do not assert a specific knot example from (5.1).

There is a precise section interpretation. Put

    rho=−y dx−u dv+i(x dv−y du)
       =F dG−d(yF).                                   (6.4)

Then d rho=dF wedge dG. Under u→u+2πa it changes by
−2πa dv. Thus rho is a local connection potential, not a single
global scalar form. The smooth gauge z_tilde=exp(−yF/t)z changes
(2.2) to rho/t and has deck multiplier exp(i a v). Its q-th tensor
power retains exp(iq a v), exactly the endpoint phase missing from
an endpoint-only reading of (6.1). A path-cover value or a local
coordinate of a bundle section is consistent. A chosen global endpoint
frame, or explicit cut corrections, is additional data. The vanishing
of the exterior derivative in Remark 2(iii) does not itself supply it.

## 7. Keep the categories and our normalization separate

The universal object in (2.1) is analytic. Its nonzero vectors form
an analytic principal C* bundle. Its restriction to a curve with (2.2)
is a flat bundle; the sheaf of horizontal vectors is a rank-one local
system. H1 with **constant** C* coefficients classifies these flat
objects, rather than just their underlying holomorphic lines.

The universal analytic bundle is not an algebraic G_m torsor on
(G_m)². Integrating (2.3)/(2πi) on the real two-torus gives −1
in our declared convention, so the underlying topological line is
nontrivial. In contrast C[f^(±1),g^(±1)] is a factorial regular ring,
and its algebraic Picard group is zero. The universal line therefore
cannot be the analytification of an algebraic line on that torus.
This obstruction concerns the universal torus bundle, not every
restriction of it. In particular a finite-monodromy restriction can
be studied with a finite-cover algebraic model, but that is further
category/comparison information, not the displayed analytic quotient.

The associated Heisenberg group can be written

    (F,G,H)*(F',G',H')
      =(F+F',G+G',H+H'+F G').                         (7.1)

Its center is additive and the quotient is the additive (F,G) plane.
Left multiplication by (ta,tb,t²c) sends H to H+taG+t²c.
Exponentiating H/t gives precisely (2.1); dH−F dG is invariant.
The noncommutative central extension, its integral lattice quotient,
and the resulting analytic C* bundle are related constructions, not
interchangeable names for one algebraic G_m torsor over the A-curve.

There is also a factor of two in a direct comparison with
[our boundary line](boundary_regulator_period.md). On a **common**
torus with U=log m,V=log l, the regulator potential is V dU/t.
The gauge z_sym=exp(−UV/(2t))z changes it to

    A_sym=(V dU−U dV)/(2t),
    z_sym'=(−1)^(ab)exp((bU−aV)/2)z_sym.               (7.2)

Squaring removes the sign and gives exactly our deck multiplier
exp(bU−aV) and potential (V dU−U dV)/t. Thus, on the same
torus and with these conventions, our boundary line is the **square**
of the symmetrized r(l,m) line. Matching the actual papers additionally
requires transporting squared eigenvalues and complete-point shifts;
the literal variable names are not that transport. Reversing (l,m)
dualizes the regulator. These constants should not be hidden inside
a generic statement that the two lines are the same.

[Our common period space](common_frobenius_regulator_period_space.md)
has an explicit algebraic unipotent connection and further exponential
periods. Nothing here identifies their selected periods with the knot
state. [Our quantum norm construction](intrinsic_quantum_a_norm_torsor.md)
instead begins with a specialized q-difference module, a finite etale
cyclic algebra S/k, and N_(S/k)(a)=v. That solution variety is a
torsor under the norm-one torus, while its scalar intertwiners form
a separate G_m torsor. Neither follows from (2.4) or from calling a
line's nonzero vectors a torsor.

## 8. Reproducible scope

[The exact audit script](../experiments/audit_li_wang_heisenberg.py)
checks the deck cocycle, connection transformation, curvature constant,
antisymmetry, branch shifts, Heisenberg horizontal form, local
secondary-potential transformation, factor-of-two comparison, and both
explicit branch diagnostics.
[Recorded results](../experiments/li_wang_heisenberg_results.json).

    python3 experiments/audit_li_wang_heisenberg.py

The verified result is the analytic regulator line, its continued-log
holonomy, and the quantization deduction conditional on K2 torsion.
The knot K2 input has not been independently reproved here. The
endpoint-only reading of the later special invariant needs correction
or additional marking. No quantum norm-torsor comparison or volume
conjecture is proved by this audit.
