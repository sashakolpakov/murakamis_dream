# Cyclic modules, the Kashaev color, and a recoupling lattice at degeneration

Research note, 25 October 2026. This supplies an integral extension of
the local algebra used in the torsor construction. The results are
uniform in every level N>=2. They are explicit representation and lattice
calculations, not an appeal to a theorem about quantum knot invariants.
No novelty is claimed for cyclic quantum-group representations.

The distinguished Kashaev state remains the one fixed in
[kashaev_crossing_and_period_lattice.md](kashaev_crossing_and_period_lattice.md)
and [kashaev_ado_pointing.md](kashaev_ado_pointing.md).

## 1. A regular quantum-group family through the nilpotent fiber

Put q=exp(pi*i/N), omega=q^2, rho=q-q^(-1), and

    R=C[t,t^(-1)], E_t=R[x]/(x^N-t),
    X f(x)=x f(x), sigma f(x)=f(omega*x).

The following endomorphisms are regular over R, including t=1:

    F=(1-X)sigma^(-1),
    E=(1-omega*X)/(omega*X*rho^2) sigma,
    K=-q^(-1)X^(-1).                                  (1.1)

All inverses in (1.1) exist over R. Direct multiplication gives

    K E=q^2 E K, K F=q^(-2)F K,
    E F-F E=(K-K^(-1))/rho.                            (1.2)

For a short verification let

    f(X)=(X+X^(-1)-2)/rho^2.

Then FE=f(X), EF=f(omega*X), and
f(omega*X)-f(X)=(q X-q^(-1)X^(-1))/rho.
The last numerator equals K-K^(-1). The normalized Casimir is

    rho^2 FE+qK+q^(-1)K^(-1)=-2.                     (1.3)

The central powers follow by multiplying around the cyclic orbit:

    F^N=1-t,
    E^N=(-1)^(N-1)(1-t)/(t*rho^(2N)),
    K^N=(-1)^(N-1)/t.                                (1.4)

Thus the inverses of F used in the generic quantum-torus chart are
unnecessary in this quantum-group lattice. At t=1 both E and F are
nilpotent, while the module stays simple.

To see the fiber explicitly, evaluate functions at omega^j, and write
e_j for the corresponding delta vectors. Put

    p_j=product_(a=1)^j(1-omega^a), v_j=p_j e_j.

Then

    F v_j=v_(j+1), E v_j=[j]_q^2 v_(j-1),
    K v_j=q^(N-1-2j)v_j,                             (1.5)

with the endpoint vectors zero. These are exactly the Kashaev color
matrices in the crossing proof. The K eigenvalues are distinct and
all adjacent E,F coefficients are nonzero. Matrix units are obtained
from the K spectral projectors and these adjacent maps. For t!=1,
X,F already generate the full matrix algebra because 1-X is invertible.
Hence the image of this family in End_R(E_t) is the full matrix bundle:
fiberwise surjectivity implies surjectivity over R by Nakayama.
This concerns the image of the given family, not an assertion that
every central quotient of the unrestricted quantum group is Azumaya.

## 2. The pointing also extends

The cyclic vacuum equation is

    (X+F-1)v=0.

Its kernel over R is R*1. Away from t=1 this follows from
(X+F-1)=(1-X)(sigma^(-1)-1). At t=1 its rows in the evaluation basis
are the N-1 independent differences v_(j-1)-v_j. Thus its rank remains
N-1 and its kernel line remains primitive. In the basis (1.5), its
specialized vector is

    v_vac=sum_(j=0)^(N-1) p_j^(-1) v_j.              (2.1)

It is a quantum Whittaker vector rather than the highest-weight vector.
The functional eps(f)=Tr_(E_t/R)(f)/N is regular and eps(1)=1.
On a knot's cut operator, which is scalar at t=1, pairing with this
vector and functional gives the same Kashaev period as pairing with
the highest-weight vector. No possibly large change-of-basis norm
is discarded; scalarity cancels that change exactly.

### A tensor convention that must be retained

The algebra extension above is not by itself a Hopf-algebra comparison.
The Borel coproduct used in the pointed recoupling notes is

    Delta_B X=X tensor X,
    Delta_B F=F tensor 1+X tensor F.

For the standard quantum-group coproduct and X=-q^(-1)K^(-1),

    Delta_q X=-q X tensor X,
    Delta_q F=F tensor 1-q X tensor F.                (2.2)

These formulas give the exact scalar mark that any tensor comparison
must carry. It has the following explicit endpoint transport; an
algebra isomorphism alone would not provide it.

### A matched endpoint chain for the actual coproduct

Write kappa=-q. In an ordered tensor product of b factors, put

    U_j=K_j^(-1)=kappa*X_j, c_j=kappa^(1-j),
    F_j^new=c_j*F_j, E_j^new=c_j^(-1)*E_j.

These are still the regular quantum-group representations (1.1),
with a constant scaling automorphism of E,F. Their Borel coordinates
are now U_j,F_j^new, with the actual coproduct

    Delta U=U tensor U,
    Delta F=F tensor 1+U tensor F.

The unit vector of factor j solves

    (F_j^new+a_j U_j-b_j)1=0,
    a_j=kappa^(-j), b_j=kappa^(1-j), a_j=b_(j+1).    (2.3)

Thus these are exactly matched endpoint modules in the
[endpoint formulation](pointed_period_descent.md), at all levels.
The iterated coproduct acts on the unit tensor by the telescoping sum

    F_tot 1=sum_(j=1)^b
           kappa^(j-1)*c_j*x_1...x_(j-1)*(1-x_j)
           =1-x_1...x_b,
    U_tot=kappa^b*x_1...x_b.                         (2.4)

Consequently its pointing is
(F_tot+kappa^(-b)U_tot-1)1=0. More generally the substitution

    m:E_(t_1...t_b) -> E_(t_1) tensor ... tensor E_(t_b),
    f(x) -> f(x_1...x_b),                            (2.5)

intertwines F with F_tot, and multiplication by kappa^b*x with
U_tot. Each summand shifts the product coordinate by omega^(-1),
so the same telescoping calculation proves (2.5) on every f, not
just on the vacuum.

The central marks are retained:

    U_j^N=kappa^N*t_j, (F_j^new)^N=c_j^N*(1-t_j),
    U_tot^N=kappa^(bN)*product t_j,
    F_tot^N=1-product t_j.                           (2.6)

At the nilpotent fiber, the individual automorphism is the explicit
basis conjugation v_h -> c_j^h v_h. It is a unit at every level,
even when kappa^N=-1. Moreover c_j=(-q)^(1-j) is one fixed monomial
in the generic quantum parameter; it is not an unrelated scalar
chosen separately at each level. At the specified complex roots its
basis-conjugation entries all have absolute value one. Thus the
scalar in (2.2) is accounted for at
the Borel pointing and tensor-embedding level without changing the
nilpotent color. At this stage (2.5) has only been checked on the
Borel action. The subsequent
[Casimir comparison](casimir_braiding_and_recoupling_lattice.md)
proves its full E-action, identifies both actual crossings on the
transported recoupling lattice, and derives the pivotal closing trace.
The selected global geometric period and its norm remain additional
comparison requirements.

## 3. Pointed Borel factorization at all levels

For nondegenerate s,t, the existing relative operators are

    Z=Y_1 Y_2^(-1), D=X_1+Z, C=ZX_2,
    X_tot=X_1X_2, Y_tot=X_1Y_2+Y_1,
    tau=(1-st)/(1-t).

The generic commutation and vacuum-ideal certificates in the preceding
notes do not use parity. For the central powers one must retain

    (ZX_2)^N=(-1)^(N-1) Z^N X_2^N.

Consequently

    X_tot^N=st, Y_tot^N=1-st,
    D^N=tau, (-C)^N=1-tau                           (3.1)

for every N>=2. The quantum-binomial argument requires primitivity,
not primality or oddness. Simplicity and the common vacuum then give
the pointed factorization at every level, with the same kernel

    C_(s,t)(u^a v^b)
       =w^a product_(j=1)^b(1-omega^j w)/(1-omega^j z),
    w=x_1x_2, z=x_2.                                 (3.2)

In the monomial bases used in the earlier note, its determinant is

    det C_(s,t)=sigma_N f(s,t)^(N(N-1)/2),
    f(s,t)=t(1-st)/(1-t)^2,
    sigma_N=(-1)^(N(N-1)^2/2).                       (3.3)

The earlier formula without sigma_N applies to odd N. For completeness,
the change from x_1^a x_2^b to w^a z^b contributes
sigma_N*t^(N(N-1)/2): translation of the z exponent by a has sign
(-1)^(a(N-1)). The numerator-column norms contribute
(1-st)^(N(N-1)/2). The remaining z-column determinant has sign
(-1)^(N-1), phase omega^(N(N^2-1)/3), and denominator (1-t)^(N-1).
Its N-th power has no sign or phase. Multiplying these factors proves
(3.3), including the even-level sign.

## 4. Blow up the simultaneous nilpotent point

Use the discrete valuation ring A=C(a,b)[[eps]], with a,b,a+b nonzero,
and substitute

    s=1-eps*a, t=1-eps*b.

This records a direction above (s,t)=(1,1). Its relative parameter is

    tau=(a+b)/b-eps*a,
    f(s,t)=eps^(-1) (a+b)/b^2 * (1+O(eps)).          (4.1)

In particular the exceptional relative parameter remains nondegenerate.
The direction unit (a+b)/b^2 is part of the normalization torsor.

**Integral recoupling theorem.** The invariant factors of C_(s,t)
over A are

    eps^(-1), multiplicity N(N-1)/2,
    1,        multiplicity N(N+1)/2.                 (4.2)

Thus C^(-1) is regular. The image lattice C A^(N^2) contains the basic
target lattice A^(N^2), and their quotient is killed by eps and has
dimension N(N-1)/2 over the residue field. This is the precise lattice
change across the pole, with the vacuum retained.

### Uniform proof

Pass to the w,z evaluation bases with

    w_i=omega^i (st)^(1/N), z_j=omega^j t^(1/N),

using formal roots with constant term one. Their Vandermonde changes
are units in A, so invariant factors are unchanged. Formula (3.2)
becomes N blocks, whose entries are

    B_i(j,d)=product_(k=1)^d(1-omega^k w_i)
                            /(1-omega^k z_j), 0<=d<N. (4.3)

Define r_i=[-i]_N if i!=0, and r_0=N. The numerator has one simple
zero exactly when d>=r_i; the denominator has one exactly when
d>=r_j. Therefore every entry has pole order at most one. The
residue eps*B_i has nonzero columns only for 1<=d<r_i, and rows
r_j<=d. The square submatrix r_j,d in {1,...,r_i-1} is triangular
with nonzero diagonal. Its rank is r_i-1.

The denominator-column matrix, before multiplying by the numerator
factors, has determinant valuation -(N-1): multiply its columns
d=1,...,N-1 by eps and evaluate at eps=0. The row j=0 is supported
only on column zero; the other rows are the same nonzero triangular
residue matrix. Numerator factors add valuation N-r_i. Hence

    val(det B_i)=1-r_i.

Since all poles are simple and the residue has rank r_i-1, exactly
r_i-1 invariant factors have valuation -1. The remaining valuations
are nonnegative, and their sum is zero, so all are zero. Summing
over r_i=1,...,N proves (4.2).

There is also an explicit integral frame for each block: multiply its
source columns d=1,...,r_i-1 by eps. The resulting matrix has a unit
determinant. This gives the lattice modification without a numerical
limit or an unspecified regularization.

## 5. The determinant root retains the exceptional unit

For odd N, h=(N-1)/2 and the preceding normalized frame can use

    gamma^N=f^(-h).

For even N an explicit determinant-one cover is

    gamma^(2N)=-f^(-(N-1)).                          (5.1)

Indeed sigma_N=(-1)^(N/2) in this case, so raising (5.1) to N/2
cancels the sign in (3.3). This is a genuine even-level phase.

On the ramified cover eps=delta^(2N), gamma has valuation N-1.
Its remaining unit retains (a+b)/b^2 through the displayed root
equations. The determinant-normalized C still needs the source and
target lattices of (4.2); determinant one alone does not make its
entries regular in the original lattices.

Generic pointed recouplings obey the categorical pentagon at all
levels. Extension of their specified scalar normalizations through
a whole degeneration requires compatible transported lattices and
the phases above. No global path-independence is inferred merely
from the determinant formula.

The subsequent [common carry-lattice theorem](carry_recoupling_lattice.md)
now proves the required path independence for arbitrary finite
pointed recoupling trees. Its explicit image in leaf evaluation
coordinates is epsilon^(-floor(sum i_j/N)) on each tuple. A
nodewise carry inequality and determinant count prove this equality
uniformly. Both the basic sources and the actual sublattices are
preserved by every recoupling. The original cut meridian family
is recovered with all wrap sources, pivot and framing retained.
This extends the two-factor lattice theorem; it does not infer
a global geometric gluing or regulator norm from the determinant.

## 6. Relevance and remaining comparison

The cyclic vacuum now has a regular realization in the actual nilpotent
Kashaev color. The simultaneous recoupling pole has an explicit two-step
integral lattice, and its direction-dependent normalization unit is
known. These results remove a local degeneracy restriction of the
earlier generic cyclic-module arguments.

They do not identify the geometric fundamental-class period with the
Kashaev cut period. Equations (2.3)--(2.6) account for the tensor mark
at the Borel level. The subsequent
[Casimir calculation](casimir_braiding_and_recoupling_lattice.md)
extends the E-action and identifies actual crossings and local
pivotal traces on these lattices. The global geometric period pairing
and its regulator norm must still be matched. Choosing an unpointed
isomorphism of matrix algebras cannot replace that theorem.

The independent checks in `experiments/audit_cyclic_steinberg_lattice.py`
verify the regular quantum-group relations, nilpotent fiber, all-level
pointed factorization, determinant sign, and the block lattice frames.
They are diagnostics for the uniform arguments above.
