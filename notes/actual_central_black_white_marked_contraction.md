# Exact central black, ordinary-white and marked contractions

29 October 2026. At the ODD simple Steinberg triple the actual ordinary
white covector is a genuine pivotal dual of the black tensor, with an
explicit scalar. It is nonzero, yet its closed magnetic pairing with
black is ZERO. The original marked closure instead gives an explicit
positive scalar after all magnetic indices are contracted. This is a
coherent source calculation, not a norm-square replacement of the
vertex. It explains why the
[full-black CD norm obstruction](actual_trivalent_full_cd_normalization_and_magnetic_growth.md)
does not determine the growth of a sewn scalar.

Only this odd central sector and the specified actual two-vertex
contraction are evaluated. No paired/even analogue, arbitrary graph
recoupling estimate or global volume statement is inferred.

## 1. Original duality fixes the ordinary white tensor

Use N=2m+1, d=2m and the exact central W,pi,Theta,A_N of
[the actual odd source](actual_trivalent_steinberg_central_anchor.md).
Thus pi=W^dagger P, pi W=I, and the unscaled black tensor is

    U=pi^tensor3 J_source=s Theta,
    s=N^2 q^(-m^2) A_N,
    Theta=(W tensor I)p.                              (1)

The ORIGINAL physical cup/cap matrices are

    p_(a,b)=N x^(-b)delta_(a+b,d),
    ell_(a,b)=x^a/N delta_(a+b,d), p ell=ell p=I.

For a map T:V->V tensor V its genuine right dual, after identifying
the dual objects by these SAME maps, is

    D(T)=p^T T^T(ell^T tensor ell^T)P_ord.             (2)

P_ord reverses abstract dual tensor order; it is not an inserted R.
For an invariant column v in V^tensor3 the right-dual covector is

    D(v)=v^T(ell^T)^tensor3 Rev_3.                    (3)

These are bilinear pivotal duals. Complex conjugation is not part of
D. Both formulas follow by the ordinary evaluation index sums, with
every N factor retained.

The actual simple-channel Hom space is one-dimensional, so D(W) is
a scalar multiple of pi. Evaluate row0,column(m,0) in(2), using
W_d(d,m)=q^(m^2). It gives EXACTLY

    D(W)=gamma pi, gamma=q^(3m^2)/N.                  (4)

In particular gamma is nonzero. Dualizing pi W=I and using the same
one-dimensional Hom space gives D(pi)=gamma^(-1)W.
The nested matching (16),(23),(45) is preserved by reversal, and its
right dual is precisely the ORIGINAL three ordinary caps ell^S.
Therefore, with Lambda=ell^S W^tensor3,

    D(U)=gamma^(-3)Lambda,
    Lambda=gamma^3 s D(Theta).                        (5)

Both U and Lambda are nonzero at every odd N, since A_N is the
proved nonzero quartic scalar. The original ordinary white packet V
in the unscaled W coordinates satisfies conjugate(V)=N^6 Lambda.
This proves its precise dual relation; it does not assume V=U or V=Vm.

## 2. The ordinary closed pairing is zero, despite nonzero vertices

Write Theta_c and lambda_c for the third magnetic slices of Theta
and D(Theta). Let

    T_(s,t)=sum_(a,b) Theta_(a,b,s)D(Theta)_(a,b,t).

Integer H=0 support makes T diagonal. The ordinary E equations for
the invariant column and covector imply, for 1<=r<=d,

    k_r lambda_r E_12=-e_r lambda_(r-1),
    k_(r-1) E_12 Theta_(r-1)=-e_r Theta_r.

Here k_r=xQ^(-r) and every e_r is nonzero. Pairing these identities
gives T_rr/T_(r-1,r-1)=k_(r-1)/k_r whenever interpreted as the
cleared equality. Hence K T is scalar, with NO division by T_rr.

Its scalar can also be computed finitely. The top-edge Clebsch
identity is

    W_(d-a)(d,m-a)=q^(m^2)h_a, 0<=a<=m.              (6)

To prove it, start at W_d(d,m)=q^(m^2), apply the actual E relation
at first physical color d, and use factorial reflection. The resulting
factor is
Q^(ma)F_m F_(d-a)/(F_(m-a)F_d); its root phase converts it exactly
to h_a. There is no new scalar connection constant.

Equations(2),(4),(6) give

    T_dd=gamma x^(-d)q^(-m^2) sum_a x^a beta(m,a)^2
         =gamma x.

The last sum is the finite Vandermonde sum N/F_m^2. Since k_d=x^-1,

    K T=gamma I,
    D(Theta)Theta=Tr T=gamma Tr(K^-1)=0.              (7)

Consequently Lambda U=0 exactly. This is the ordinary q-dimension
zero in its actual magnetic contraction, not a claim that either
vertex vanishes. Replacing it by a positive Euclidean contraction
would destroy this cancellation.

The open tangle obtained by cutting that third edge is K T in these
left/right duality conventions. The K factor is the recorded pivotal
clock from the same snakes; (7) also verifies directly that the open
map is a Hopf endomorphism. Its normalized marked closure is gamma,
since the original marked unknot has value one.

## 3. Transfer the physical mark through the actual simple projector

Let E_St=W pi be the FULL isolated -2 Casimir projector. The actual
central circle is L_St=N E_St. Its appropriately oriented ordinary
partial traces are

    sum_b K_b (E_St)_(a b;c b)=delta_(a,c),
    sum_a K_a^(-1)(E_St)_(a b;a e)=delta_(b,e).         (8)

Here is a root-safe proof, rather than a guessed positive resolution.
Lift only this projector to the ordinary generic highest-weight-d
pair. Its central summand is again the highest-weight-d module.
The Casimir projector is regular at the odd root: its eigenvalue -2
collides with no other pair eigenvalue, so every projector denominator
is a unit there. Its typed partial trace is a Hopf endomorphism of
V_N, hence scalar. Taking the generic full pivotal trace gives

    scalar [N]_q=[N]_q,

so the scalar is one away from the root and remains one by regular
specialization. This proves(8) with the original root duality. The
same argument shows equality of the root scalar obtained by cutting
a physical V_N component or its embedded central V_N edge: the
generic quantum dimensions are IDENTICAL, and all relevant coupons
have a regular lift. No arbitrary modified-trace axiom is assumed.

At odd root the usual generic pivotal maps specialize to the recorded
ones, since K^N=I on V_N and K^(1-N)=K. Root marked closure of an
open scalar t I is exactly t, by the direct identity m p=1 with
m_(a,b)=x^b/N^2. This is the actual unrestricted marked source,
not a replacement by an ordinary cap.

This generic lift proves a FIXED-ROOT identity only. It does not
identify the original moving-q normal germ of the complete circle
with a value-only projector or authorize differentiation of it.
Other Casimir channels and their original normals remain separate.

## 4. Exact marked two-vertex central scalar

Use the actual two-vertex, three-edge source of the branching note,
with one original marked cap and all three edge circles projected
to their odd simple Steinberg summand. Contract EVERY magnetic
index before estimating. The open effective scalar of U and Lambda
is, from(1),(5),(7),

    gamma^4 s^2=q^(10m^2)A_N^2=|A_N|^2.              (9)

Indeed A_N=q^[m(2-m)]S_N with S_N positive, and the remaining
phase is q^[8m^2+4m]=q^(4mN)=1. Each of the three actual central
circles contributes N, while(8) transports the original marked cut
without an extra dimension. Thus the ORIGINAL raw marked central
contribution is EXACTLY

    Z_St=N^3 |A_N|^2
         =(1/16)exp(2Nj0)[1+O(1/N)].                (10)

For edge twists R^(e_i)L_St multiply(10) by the literal full-Cartan
unit phase omega_m^(e_1+e_2+e_3). Any recorded external line chi_N
stays outside. Equation(10) is not the full graph source with the
other joint channels removed by fiat: it is the explicitly specified
central sector of an original source decomposition.

This is a concrete coherent contraction that removes the extra
magnetic growth of the black CD norm. It does not make the original
marked WHITE tensor equal to the black tensor, or furnish a sharp
norm bound for arbitrary six-port sewing. The paired/even analogue
still needs its own normal-current calculation. A complete graph
also retains all other channels, phases and possible cancellations.

The [focused exact audit](../experiments/audit_actual_central_black_white_marked_contraction.py)
passes seven odd levels N=3,...,15: literal right-dual Clebsch maps,
nonzero ordinary white rows and zero closed pairing, both typed
physical partial traces, the complete magnetic cut operator, and
the unrestricted original marked contraction. Nine direct physical
signed full-Cartan matrix contractions independently reproduce(10).
Four labeled high-precision checks calibrate its scalar prefactor.
The duality and regular-projector arguments above prove the general
identities; the finite range is supplementary.
