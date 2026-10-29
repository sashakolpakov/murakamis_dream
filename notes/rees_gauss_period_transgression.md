# The Rees source and holonomy charts have an exact dilogarithm period

Research proof, 27 October 2026. This follows the user's proposal to
work with a whole torsor before restricting it to quantum jets. It
strengthens the symplectic identity in
[the actual full-cyclic Rees construction](irregular_rees_full_cyclic_module.md):
the difference of the two marked Liouville forms has an explicit
dilogarithm primitive. Its connection is algebraic, its period is
specified on a logarithmic cover, and the complete-meridian source
chart is regular. Varying the meridian has an additional explicit
boundary term.

This is a local period comparison for actual module coordinates.
It neither identifies the full selected knot period nor proves its
large-level norm. In particular the local root-normal parameter is
not being substituted for the physical large-level parameter.

## 1. Whole functions on the actual symplectic chart

Fix a level N, put gamma=(-1)^(N+1), and use the phase-p family
already obtained from the genuine balanced Verma module. Its center is

    U=exp(up), a=gamma M^N, b=gamma M^(-N),
    k=a/U, e=p(k-b), f=(1-U)/p.                       (1.1)

Thus ab=1. Set r=b/a=M^(-2N). On a marked logarithmic cover of the
open set p U (1-rU)!=0 put

    x=Log U=up, z=Log p, ell=Log(1-rU).

All logarithms and the dilogarithm below are continued together from
one marked basepoint. The Gauss relation is the exact whole identity

    dLog e=dz+dLog a-dx+dell.                         (1.2)

At fixed M, the two symplectic forms agree:

    Omega=du wedge dp=dx wedge dz
                         =-dLog k wedge dLog e.

Use the corresponding primitives

    theta_source=x dz,
    theta_Gauss=-Log(k/a)dLog e=x dLog e.             (1.3)

Both have exterior derivative Omega on the fixed-meridian leaf.
The centering by a in (1.3) is part of the stated primitive convention.

**Exact period transgression.** Define

    W(U;M)=Li_2(rU)+x ell-x^2/2.                    (1.4)

Then, at fixed M,

    theta_Gauss-theta_source=dW.                     (1.5)

Proof: dLi_2(rU)=-ell dx, whereas d(x ell)=ell dx+x dell.
Consequently dW=x dell-x dx, which equals the difference in
(1.3) by (1.2). No series or limiting operation enters the identity.
The basepoint value of W, or equivalently its additive period mark,
is retained rather than determined from (1.5).

The useful strengthening over equality of symplectic forms is the
specified primitive in (1.4). A symplectic map alone would supply
only a closed difference locally. Here the actual coordinate map
gives a particular dilogarithm period, with its branch data.

## 2. Its algebraic period torsor

For fixed M the functions x, ell and

    R=Li_2(rU)+x ell

satisfy

    dx=dU/U, dell=-r dU/(1-rU), dR=x dell.           (2.1)

In particular their fundamental matrix

    Pi=[[1,x,R],[0,1,ell],[0,0,1]]

has the algebraic flat connection

    Pi^(-1)dPi=[[0,dU/U,0],
               [0,0,-r dU/(1-rU)],
               [0,0,0]].                          (2.2)

Flatness follows directly: both displayed one-forms are multiples
of dU. Given two solutions of (2.1), their differences have the form

    x'=x+c_1, ell'=ell+c_2, R'=R+c_1 ell+c_3,

with constant c_i. The central cross term is the Heisenberg law.
Specifying one value of all three coordinates fixes the horizontal
solution. The shear W=R-x^2/2 gives (1.4).

This is a torsor of periods of an algebraic connection. It is not
an assertion that Li_2(rU), Log U, or a horizontal frame is algebraic.
Already dU/U cannot have a rational primitive: a derivative of a
rational function has zero residue and dU/U has residue one.
Thus algebraic gluing data and a transcendental period are compatible
parts of the same object.

The form (2.2) is the same elementary Heisenberg connection as in
[the local finite/continuous torsor](rational_quantum_dilogarithm_torsor.md).
The new statement here is its derivation from the actual Rees-to-Gauss
source map, including its primitive and boundary correction.

### A fixed whole connection before the level restrictions

The apparent N-dependence of this period disappears if the peripheral
power is kept as a whole coordinate. Put B=M^N and work first over

    Spec Q[B^(+/-1),U^(+/-1),(1-U/B^2)^(-1)].

The finite sign gamma belongs to its separately marked phase cover.
Set t=U/B^2 and use period coordinates

    mu=Log B, xi=Log t, ell=Log(1-t),
    H=Li_2(t)+xi ell.

They satisfy the algebraic flat equations

    dmu=dB/B, dxi=dt/t, dell=-dt/(1-t), dH=xi dell. (2.3)

This is the direct product of the displayed Heisenberg connection
and one additive logarithm connection. Its group is two-step
unipotent and its presentation is independent of N. In these same
coordinates the whole generating period is

    W=H+2mu ell-(xi+2mu)^2/2.                     (2.4)

Restricting B=M^N recovers (1.4) exactly. No independent Taylor series
is used to define each level. The extra peripheral form in (4.1)
is simply (x-2ell)dmu before that restriction. This gives a concrete
whole algebraic period connection to which level restrictions belong.
It does not provide a whole selected knot source merely by extending
the coordinate B: the head projectors and the crossing transport
must also be carried into the same period object.

## 3. The complete-meridian source is regular after resolution

Set M=1. On the branch near U=1 with Log U=0 at U=1, the elementary
dilogarithm identity gives

    W(U;1)-pi^2/6=-Li_2(1-U)-(Log U)^2/2.           (3.1)

For a proof of that identity differentiate
Li_2(U)+Li_2(1-U)+Log U Log(1-U); its derivative is zero.
On the real interval 0<U<1 its limit at U=1 is Li_2(1)=pi^2/6,
from the defining sum sum_(n>=1)1/n^2. Continuation with the same
branches proves the assertion near U=1. The numerical constant can
equally be kept as the marked Li_2(1); no value of it affects (1.5).

The right side of (3.1) is holomorphic at U=1. Hence the apparent
dilogarithm branch singularity in (1.4) cancels at this source point.
Its first terms, with t=U-1, are

    W(U;1)-pi^2/6=t-(3/4)t^2+(11/18)t^3+O(t^4).

Use the actual resolving chart from the module theorem, with v=1/p
and w=e/gamma:

    U=(1+wv)^(-1),
    k=gamma(1+wv), e=gamma w,
    f=w v^2/(1+wv), Omega=dw wedge dv/(1+wv).       (3.2)

The primitives themselves extend:

    theta_source=[Log(1+wv)/v]dv,
    theta_Gauss=-[Log(1+wv)/w]dw.                   (3.3)

Both quotients have removable singularities at v=0 and w=0 on the
Log(1+wv)=0 branch at wv=0. Direct differentiation gives Omega
for each. Their difference is d of the regular function

    W((1+wv)^(-1);1)-pi^2/6,

whose leading term is -wv. At v=0 the actual module is the
E-semicyclic source, and at w=0 its central point is the identity;
the period chart retains the exceptional direction as the module
chart does. The module's original transformed source exp(-pu/d)
and its ramified head flags are separate data and have not become
regular because the classical transgression has.

The primitives in (1.3) and (3.3) specify the chosen polarization:
theta_source=u dp has exterior derivative Omega. The alternative
-p du differs by d(up). Neither convention is being inferred from
an unmarked scalar quantum amplitude. Formula (1.5) is the exact
gauge between the stated primitive connections; proving that the
selected quantum source uses that gauge is a further assertion.

## 4. Meridian variation has a nonzero peripheral correction

Keeping M variable is not the same identity with a silent parameter.
With N fixed, dLog a=N dLog M and dLog r=-2N dLog M. Now

    dW=x dell-x dx-ell dLog r.

Using the whole formula (1.2) therefore gives exactly

    theta_Gauss-theta_source
         =dW+x dLog a+ell dLog r
         =dW+N[x-2ell]dLog M.                     (4.1)

This is the required boundary term of this change of primitives.
It has not been identified with the full knot's longitude insertion;
that would require composing the actual crossing and peripheral maps.
It cannot be omitted in a quantum-meridian comparison.

In particular fixed-leaf regularity at M=1 does not prove joint
meridian regularity near (M,U)=(1,1). Write A=Log r and t=rU.
The same branch identity rewrites the potential as

    W=pi^2/6-Li_2(1-t)-A Log(1-t)-x^2/2.           (4.2)

The term -A Log(1-t) vanishes on M=1 but its meridian derivative
still contains the logarithmic divisor. Formula (4.1) retains it.
This is why complete-point evaluation must follow the whole
peripheral marking and cancellation, rather than precede it.

## 5. Relation to Rivin rigidity and the volume question

[Positive geometric rigidity](geometric_rigidity_and_cyclic_source.md)
supplies an algebraic geometric place, etale over the marked meridian.
[Rivin concavity](rivin_flow_and_quantum_source.md) selects that place
on the positive shape locus. The actual Rees construction supplies
a quantum-normal model whose center has the same holonomy leaf form.
Equations (1.5), (2.2), (3.3), and (4.1) now show that its source
coordinate map lifts to a specified local period torsor.

These are function identities before quantum jets. The
[cyclotomic rigidity theorem](whole_period_cyclotomic_rigidity.md)
can test a proposed whole algebraic comparison after its presentation
and marked source have been supplied; it is not needed to derive
the identities here.

The complete source value Li_2(1) is real. It does not supply the
hyperbolic-volume action. That action belongs to the full composed
crossing/fundamental-class period, already computed in
[the actual regulator-action proof](quantum_longitude_and_regulator_action.md).
The remaining theorem must connect that composed period to the
actual selected quantum source with controlled normalization.

[The whole crossing factorization](rees_whole_crossing_source_factorization.md)
now also obtains the cyclic and resonant period factors from the
actual Verma crossing in this same Rees chart. Its center transport
is the characteristic holonomy braiding. That is a crossing/source
operator statement with all finite-head projectors retained; it
does not discard their irregular factors when composing a knot word.

The parameter d=N(Q^N-1) used to construct this chart is a normal
parameter at a fixed root and fixed N. The volume-conjecture step
is H_N=2pi*i/N. An identity for the chart or its polar root-normal
action does not equate these two directions or prove the N-growth.

[Symbolic and marked-path checks](../experiments/audit_rees_gauss_period_transgression.py)
verify the whole differential, both resolved primitives, 32 fixed-leaf
and 32 varying-meridian path integrals, and 24 near-boundary branch
cancellations. The [results](../experiments/rees_gauss_period_transgression_results.json)
use 85-digit arithmetic for the period checks; the arguments above
are the proofs. An independent derivation checked the primitive,
its signs, the parabolic extension and the peripheral correction.
The [independent audit, Section 5](flat_pointed_torsor_and_quantum_lifting.md)
also checks the whole two-variable connection before level restriction.

