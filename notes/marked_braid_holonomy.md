# The actual cut period, its flag torsor, and its classical holonomy

Research note, 26 October 2026. This continues the
[relative octahedral calculation](relative_octahedral_period.md).
It identifies the global *classical critical correspondence* of
the actual cut state with a framed knot representation variety,
retaining the boundary vector that gives the original invariant.
It also identifies a split Borel framing torsor and proves a
boundary-wedge/complete-regulator rigidity statement for the
crossing Bloch sum. No assertion about which critical component
contributes to the finite period is made.

The holonomy braid map and existence of representation-associated
diagrammatic critical points have existing coverage. Section 9
records it. The proofs here are direct calculations from our fixed
actual R coefficients, not imports of those papers' proofs.

## 1. An exact change of boundary vector, at every level and color

Put q=exp(pi*i/N), Q=q^2, rho=q-q^(-1), x=q^alpha,
M=-qx as in [the ADO note](kashaev_ado_pointing.md). Let

    F_a=(Q;Q)_a, 0<=a<N,
    psi_a=1/F_a, phi_a=F_a/N.                       (1.1)

These coefficients are units, F_(N-1)=N, and

    sum_a phi_a psi_a=1.

Let C_N(x) be the actual zero-framed cut operator of a knot.
The previously proved intertwining and irreducibility calculation
gives C_N(x)=F_N(M) I at generic color; Laurent continuation
extends the matrix identity to exceptional colors. Therefore

    phi^t C_N(x) psi=F_N(M)                         (1.2)

for every color, including the Kashaev color M=1. This is a
bilinear algebraic pairing, with no complex conjugation.

Now use the basis w_a=v_a/F_a. A matrix transforms by D^(-1)CD,
where D=diag(1/F_a). In this basis psi is the constant vector 1
and phi is the normalized averaging functional (1/N)sum_a.
Equation (1.2) becomes

    F_N(M)=(1/N) sum_(a,b) (C_N^new(x))_(a,b).       (1.3)

This is an exact presentation of the existing invariant. It is
useful because its boundary vector has a simple geometric flag,
without fixing a state coordinate to its endpoint a=0.

## 2. The actual relative meridian module in that basis

Let A be multiplication by Q^a on functions of a modulo N, and
let sigma f(A)=f(QA). Let e_partial be the idempotent supported
at a=N-1. The actual conjugated quantum-group matrices are

    K=x A^(-1),
    F=(1-A)sigma^(-1),
    rho^2 E=q^(-1)(x^(-1)-x A^(-1))sigma
               -c(x)e_partial sigma,
    c(x)=q^(-1)(x^(-1)-Qx)
         =q^(-1)x^(-1)(1-M^2).                     (2.1)

For F the coefficient at a=0 vanishes, so the cyclic formula
already has the actual nilpotent endpoint. For E, cancellation
of the adjacent factorials gives

    rho^2 E_(a,a+1)=q^(-1)(x^(-1)-xQ^(-a)), a<N-1.

The cyclic formula would add the entry from 0 to N-1 with
coefficient c(x). Subtracting it gives precisely the actual
truncated E. This proves (2.1), including its exceptional row.

Write E_cyc for the operator in (2.1) before subtracting this
rank-one term. Multiplication around its orbit gives

    (rho^2 E_cyc)^N=(x^N-x^(-N))I, (rho^2 E)^N=0.   (2.2)

Indeed the product for the first operator is
q^(-N)x^(-N)(1-x^(2N))=x^N-x^(-N). At M=1 the wall
coefficient c and the central defect both vanish, and the cyclic
and actual E operators agree. Away from that point E_cyc is a
comparison module; replacing E by E_cyc in the knot contraction
has not been justified and is not done here.

The full modified dimension now has another exact interpretation:

    d_N(M)=q^(N(1-N)/2) c(x)/(x^N-x^(-N))
           =i^(N+3) M^(N-1)/(1+M^2+...+M^(2N-2)).   (2.3)

To prove it, use qx-(qx)^(-1)=-c(x) in the defining
modified-dimension formula. Thus the full meridian factor is a
specified phase times the ratio of a local boundary defect to
the cyclic central defect. At M=1 evaluate their whole ratio,
giving d_N(1)=i^(N+3)/N. The two zeros must not be evaluated
separately. This agrees with the missing-transition calculation
in the preceding note; it retains its full peripheral function.

This is the local color representation, with its internal
state-index wall. Turning that wall into a specified global
inhomogeneous meridian A-equation requires elimination with
the source retained. That identification is not assumed here.

## 3. Crossing Bloch sums change by a boundary coboundary

For a crossing with input indices a,b and output indices c,d,
the basis change gives exactly

    r_new=F_c F_d r_old/(F_a F_b).                  (3.1)

For the positive crossing c=b+k,d=a-k, put A=Q^a,
B=Q^b,C=Q^k,X=x^2. Its non-Gaussian finite product is now

    F_(b+k)/(F_b F_k) * (QX/A;Q)_k.

Its five-dilogarithm symbol is

    beta_+=[B]+[C]+[X/A]-[BC]-[XC/A].               (3.2)

The Gaussian and sign in the preceding note are unchanged.
For the inverse crossing c=b-k,d=a+k the product and symbol are

    F_(a+k)/(F_a F_k) * (QX/B;Q)_k,
    beta_-=[A]+[C]+[X/B]-[AC]-[XC/B].               (3.3)

The difference between either new symbol and the old one is

    [A]+[B]-[U]-[V], U=Q^c,V=Q^d.                 (3.4)

It cancels on each shared strand of a finite contraction. The
cut vector and covector transform at the remaining endpoints
as in Section 1. Thus this basis change does not lose a global
period or insert an unspecified normalization.

Both (3.2) and (3.3) have the form

    [u]+[v]+[w]-[uv]-[vw].                         (3.5)

They have the five ordered tetrahedron shapes

    v, u, 1/(uv), w, 1/(vw),

with ideal vertices infinity,0,1,v,uv,
v(1-w)/(1-vw), by the previous cross-ratio proof. The positive
case uses (u,v,w)=(B,C,X/A); the negative uses (A,C,X/B).
The inverse orientation is consistent: substituting
(A,B,C)->(B/C,AC,1/C) in beta_+ gives -beta_- by
[1/C]=-[C]. No additional negative sign is inserted in the
negative coefficient's already computed symbol.

## 4. Deriving the rational crossing map from the actual symbols

For clarity, derive it first in the old basis. Its physical
coordinates do not change with (3.1). Let p,r denote the
classical eigenvalues of the input Q-shifts and put

    P(A)=(1-A)(1-x^2/A)/x,
    K_1=x/A, e_1=P(A)p, f_1=p^(-1),
    K_2=x/B, e_2=P(B)r, f_2=r^(-1).                (4.1)

These are the commuting symbols of K,rho^2 E,F. They obey

    K_i+K_i^(-1)+e_i f_i=x+x^(-1).                 (4.2)

In the new basis, the same coordinates are

    K=x/A, e=(1-x^2/A)p_new/x, f=(1-A)/p_new,
    p_new=(1-A)p.                                  (4.3)

Let S be the positive generating expression G_++Phi already
derived from the actual R coefficient. Its output coordinates
are U=BC,V=A/C. The canonical relation on the constraint UV=AB is

    exp(S_a)=p_out,2/p,
    exp(S_b)=p_out,1/r,
    exp(S_c)=p_out,1/p_out,2.                       (4.4)

Here derivatives are in log A,log B,log C. Substitution of the
exact contiguity symbols gives

    p_out,1=Ar/(Cx),
    p_out,2=(BC/x)*(1-A)(1-x^2/A)
                      /((1-A/C)(1-x^2C/A))*p,
    C=1/(1-e_1 f_2).                               (4.5)

The last equality follows on cancelling the common factors
in the third equation of (4.4); equivalently
r(C-1)=C P(A)p. It is not a guessed holonomy map.

Write d=1-e_1 f_2. In physical coordinates the resulting map R is

    K'_1=K_2 d,       K'_2=K_1/d,
    f'_1=K_1 f_2/d,   e'_2=e_1/(K_2 d),
    e'_1=(d e_2+e_1(dK_2-K_2^(-1)))/K_1,
    f'_2=K_2(d f_1+f_2(d/K_1-K_1)).                 (4.6)

The inverse is also derived from the negative crossing symbol.
Writing c=1-(K_1/K_2)e_2 f_1, it is

    K'_1=K_2 c,       K'_2=K_1/c,
    e'_1=K_1 e_2,     f'_2=f_1/K_2,
    f'_1=f_1+f_2/K_1-f_1/(K_2^2 c),
    e'_2=K_2 e_1+e_2-K_1^2 e_2/c.                 (4.7)

All equations are rational identities on their specified open
charts. The symbolic audit derives both (4.6) and (4.7) from
their respective generating relations and checks that they
compose to the identity.

## 5. A matrix proof that this is meridian holonomy

Define two triangular matrices and a determinant-one matrix by

    b_+(K,e)=[ K e ],  b_-(K,f)=[ 1  0 ],
             [ 0 1 ]              [-Kf K ]
    G=b_-^(-1)b_+=[ K       e       ].
                    [ Kf  K^(-1)+ef ]

The crossing map satisfies three exact factorizations:

    b'_(+,2)b'_(+,1)=b_(+,2)b_(+,1),
    b'_(-,2)b'_(-,1)=b_(-,2)b_(-,1),
    b'_(+,2)b'_(-,1)=b_(-,2)b_(+,1).                (5.1)

The last follows immediately from the four simple entries of
(4.6); the other two are the preserved coproducts. Direct
substitution proves all three. The map also swaps the two
Casimirs K+K^(-1)+ef.

For two strands define

    H_1=G_1, H_2=b_(-,1)^(-1)G_2 b_(-,1).

Equations (5.1) imply

    H'_2=H_1, H'_1=H_1^(-1)H_2 H_1.                (5.2)

For example
H'_2=(b'_(-,2)b'_(-,1))^(-1)b'_(+,2)b'_(-,1)
=b_(-,1)^(-1)b_(+,1)=H_1. The total product H_2H_1
is preserved, which gives the other equality. This proves the
Hurwitz/Wirtinger conjugation rule by matrix multiplication.

For b strands, set B_(-,j)=b_(-,j)...b_(-,1) and

    H_j=B_(-,j-1)^(-1)G_j B_(-,j-1).               (5.3)

The same calculation applies to adjacent strands; later prefix
products do not change because their two factors have the same
product in (5.1). Hence (5.3) intertwines every mixed braid word
with the ordinary conjugation action on meridians.
Composition uses the order in which the actual operator acts:
rightmost factor first when a braid is written as a matrix
product. The conjugation action uses that same convention.

This map is birational, with an explicit inverse. Given H_j,
let P_j=H_j...H_1. When its upper-left entries are nonzero put

    B_-(P)=[  1     0  ], B_+(P)=[ P_11 P_12 ],
            [-P_21 P_11]          [   0    1  ]

so P=B_-(P)^(-1)B_+(P). Recover
b_(+,j)=B_+(P_j)B_+(P_(j-1))^(-1), and the analogous
b_(-,j). In particular K_j=(P_j)_11/(P_(j-1))_11.
This proves the inverse, rather than only counting dimensions.

The braid relations now follow from (5.2). On any common regular
chart these are identities of schemes, including Artin test rings;
the rational identities clear to polynomial identities with unit
denominators. No reducedness or isolated-critical-point assertion
is needed.

The actual meridians in this convention are mu_j=-H_j. Their
traces are M+M^(-1), since x=-M at the classical symbol.
The central minus sign preserves (5.2). The cut's unit vector
p_new=1 gives f=1-A,e=(1-x^2/A)/x, and directly

    G (1,1)^t=x^(-1)(1,1)^t.                       (5.4)

Thus it selects the peripheral eigenflag 1, with meridian
eigenvalue M^(-1). The inverse is explicit; this flag must
not be silently called the M-eigenflag when marking holonomies.

## 6. The actual cut's critical locus and a nonempty geometric chart

Close strands 2,...,b by the actual pivotal trace and use the
constant vector and normalized average on the first strand.
For internal variables the exponentiated stationary equations
are precisely equality of the closed position and momentum
coordinates. At the two cut endpoints the constant boundary
vectors give p_new,in=p_new,out=1.

The pivotal factor on a closed strand is

    x^(1-N)Q^(a(N-1)).

With h=Log Q, N=2pi*i/h, its leading logarithmic expression is
2pi*i(log A-log x). Its internal momentum multiplier is one.
The residual writhe factor x^(w(N-1)) depends only on x.
Thus these factors do not change the exponentiated internal
stationary equations. Their logarithmic branches and peripheral
derivatives remain part of the period.

Preservation of the product of K's forces the two cut positions
to agree once all the other strands have closed. Equation (4.3)
then makes their physical e,f agree as well. Consequently the
critical equations are exactly

    R_beta(z)=z, with the first meridian eigenflag equal to 1.   (6.1)

Conversely every point of this open fixed locus satisfies the
critical equations and the cut boundary conditions.

Under (5.3), (6.1) is the familiar presentation

    <mu_1,...,mu_b | beta(mu_j)=mu_j>

of the braid-closure knot group, with the fixed eigenflag.
This presentation follows by applying van Kampen to the braid
strands and identifying their endpoints: at each crossing (5.2)
is exactly the understrand meridian relation. Thus we have an
identification of open critical schemes with framed, augmented
representation schemes. This is not yet a claim about the
classical symbol of a minimal *summed* meridian operator.

There is a useful uniform nonemptiness result. Fix any such
representation whose meridians are noncentral, and its selected
meridian eigenvector w. This includes the complete hyperbolic
representation. Choose a covector alpha with alpha(w)=1,
then a vector v with alpha(v)=1. In the basis (v,w-v), the
chosen flag is 1. For every partial product P in every stage
of the finite braid word, its upper-left entry is alpha(Pv).

For one strand in such a stage, e_j=0 exactly when alpha is a
left eigenline of H_j. Avoid these finitely many covector
lines. Also f_j=0 exactly when v is an eigenline of
P_(j-1)^(-1)P_j. These matrices are conjugate to a noncentral
meridian, so again there are only finitely many forbidden lines.
The conditions alpha(Pv)=0 and v=w exclude finitely many
additional points of the affine line alpha(v)=1. None of
alpha(Pv)=0 vanishes identically there: P is invertible.
One can therefore avoid all of them simultaneously.

This proves that all K_j,e_j,f_j can be made nonzero at every
stage, in a frame respecting the actual cut flag. The positive
and negative crossing denominators then remain nonzero. Moreover
all five shapes in (3.5) avoid 0 and 1: the input conditions
exclude A,B in {1,x^2}, the output conditions exclude the
corresponding U,V, and e_1 f_2!=0 (respectively e_2 f_1!=0)
excludes C=1. This asserts nondegenerate tetrahedron shapes;
it does not assert positivity or distinctness of every pair of
nonadjacent developed octahedron vertices.

Thus every hyperbolic knot's complete representation lies in
the actual cut state's complex, exponentiated critical locus
on a chart with nondegenerate tetrahedra. A chosen such frame
works on a Zariski open neighborhood of the point in the
augmented representation scheme. No alternatingness is needed.

## 7. The framing torsor is explicitly split

Over the irreducible augmented character locus, fixing the
selected flag to 1 leaves the group

    B_1=Stab_(PGL_2)(1),

a two-dimensional split Borel group. It acts freely on framed
representations because their projective centralizer is trivial.
Its orbits are precisely the framed realizations of one augmented
character. The full framed locus is a B_1 torsor; the regular
critical chart is an open subset of that torsor. The open chart
is not asserted to be preserved by every B_1 element.

It can be split algebraically. For a non-elementary representation
choose fixed group words g,h such that

    p, rho(g)p, rho(h)p

are distinct. Send this ordered triple to (1,0,infinity). The
unique fractional transformation is rational in its three
points and gives a section on their nondegenerate locus.
If necessary choose the two words so this frame is also regular
in Section 6: the infinite projective orbit is Zariski dense in
P^1, its square is dense in the space of pairs, and the good
frames form a nonempty open subset. The words can then be held
fixed near the complete character.

Equivalently, over the augmented function field H^1(k,B_1)=0.
After sending the flag to infinity, B_1 is G_a semidirect G_m.
For a Galois cocycle, Hilbert 90 kills its multiplicative part.
Its remaining additive cocycle b_gamma is killed by averaging:
a=(1/|G|)sum_gamma b_gamma satisfies b_gamma=a-gamma(a).
This is a proof of the splitting, not an assumed rigidity claim
for the quantum period. It removes an ordinary framing torsor;
it does not kill a horizontal difference-extension class or
the central Bloch regulator.

## 8. A global boundary wedge and complete-frame regulator rigidity

Let beta_beta be the sum of (3.2)--(3.3) over the braid, with
their actual input/output variables. Work rationally in
F^* tensor Q and use delta[z]=z wedge (1-z). Let S be the
total classical generating expression, including the retained
Gaussian factors. Write x for the common meridian coordinate,
and put

    L_intr=exp((1/2)[partial_(Log x) S]_critical).    (8.1)

This is the intrinsic conjugate coordinate from the actual
meridian q-shift: h=Log Q is twice its step. Initially this
is on the logarithmic/root cover specified by the coefficients.
The derivative in (8.1) holds internal coordinates fixed before
restricting to the exponentiated critical equations; a global
flattening for a critical primitive is not being assumed.
No topological longitude identification is built into its name.

The subsequent [exact longitude proof](quantum_longitude_and_regulator_action.md)
now supplies that identification. Its finite meridian insertion
fixes the square-root sign by an integer-position coboundary.
The knot's eigenvector transport then proves that (M,L_intr),
with M=-x classically, is the preferred peripheral pair on the
M-eigenflag. The actual cut uses the opposite M^(-1)-flag,
whose longitude eigenvalue is L_intr^(-1).

There is an exact rational wedge identity on the critical locus:

    delta beta_beta=-2 x wedge L_intr.              (8.2)

Here is the proof. For one crossing, write its five shapes as
monomials z_j in A,B,C,x with signs eps_j. If X_i denotes
one of these four multiplicative generators, then

    delta beta=-sum_i X_i wedge exp(partial_i Phi).

The Gaussian G has symmetric quadratic coefficient matrix in
their logarithms, so sum_i X_i wedge exp(partial_i G)=0.
Its constant signs are torsion and disappear rationally. Hence
Phi may be replaced by S=G+Phi in this identity. The generating
relations (4.4) then give exactly

    delta beta=A wedge p_in,1+B wedge p_in,2
         -U wedge p_out,1-V wedge p_out,2
         -x wedge exp(partial_(Log x) S).

For the inverse crossing use U=B/C,V=AC and
S_c=Log p_out,2-Log p_out,1; the same formula results.
Internal leg terms cancel. Closed legs have equal positions
and momenta, and the two cut momenta are 1. The last term is
-2x wedge L_intr by (8.1). This proves (8.2).
It is the previous boundary coefficient -1/2 in m=x^2,l=L_intr^2.
The wedge alone does not fix the marked longitude. The subsequent
vector-transport proof linked above fixes its flag, sign and framing.

At the complete color x=-1, (8.2) is zero in the rational
wedge. Thus beta_beta is a Bloch class on this critical
component. Applying the directly proved Bloch--Wigner
differential shows

    d D(beta_beta)=0

along its framing torsor. The good complex frame locus is a
nonempty Zariski open subset of the connected rational group
B_1, hence connected. Its regulator value is independent of
the regular frame. This is an explicit classical rigidity
argument for the *actual crossing* sum.

The [crossing fundamental-cycle proof](crossing_fundamental_cycle.md)
now identifies this complete rational Bloch class with the marked
idealized fundamental class, and hence the constant with Vol(M).
It gives a three-five-term certificate, a four-tetrahedron
diagram face table, and the degree-one peripheral check. This
supplies the classical datum that the wedge alone did not fix.
The quantum source and selected period must additionally be
transported, and its exponential norm established. Existence
of the critical component does not show that its period coefficient
is nonzero or that other components do not cancel it.

## 9. Coverage, verification, and the remaining target

Coverage checked after deriving these formulas:

* [Kashaev--Reshetikhin, braiding for quantum gl_2](https://arxiv.org/abs/math/0410182)
  covers holonomy braiding at roots of unity. We reconstruct
  the rational map from the actual crossing symbols and prove
  its conjugation rule by (5.1).
* [McPhail-Snyder--Reshetikhin, cyclic modules and flat connections](https://arxiv.org/abs/2509.02354)
  states a four-holonomy-dilogarithm factorization. It is coverage
  of a comparison framework, not a theorem identifying its
  geometric-character invariant with the original cut period.
* [Cho, existence of an optimistic-limit solution](https://arxiv.org/abs/1410.0525)
  covers critical equations associated with representations.
  The existence statement here therefore carries no novelty
  claim. Its boundary and meridian conventions are instead
  derived from (1.1)--(2.3) of the actual literature state.

The [audit](../experiments/audit_marked_braid_holonomy.py) and
[results](../experiments/marked_braid_holonomy_results.json)
check both symbolic generating maps, their inverse, all three
matrix factorizations, the exact Hurwitz rule, and the cut flag.
They check 300 mixed braid words, each of length twelve, in
three finite fields, together with braid relations and Gauss
reconstruction. At ten levels, including even and composite
ones, they check the boundary vectors, rank-one E correction,
cyclic defect and nilpotency, and dimension ratio. Thirty
actual cut contractions at levels 2 through 6 give the same
period under the boundary/basis change. A three-field algebraic
figure-eight calibration checks a nondegenerate geometric
critical chart. A high-precision complex calibration checks the
regulator's sign and frame independence against its two-regular-
tetrahedron value in three frames. These are validations, not
the general mechanism.

The original volume conjecture remains the target. This note
supplies an actual-state geometric critical locus, its framing
torsor, and a global rational Bloch boundary formula; the next
note identifies its complete fundamental-class lift. A global
quantum source comparison, the minimal meridian operator's
geometric classical factor, and the selected volume limit
remain unproved.

The subsequent [regular holonomy-braiding note](regular_holonomy_braiding.md)
derives a quantum counterpart of this classical transport. It gives
rational generator formulas, the full unrestricted root-center map,
and a regular module/intertwiner line through the actual color.
Their checked center map is the inverse map (4.7), as required by
pullback. Its pointed determinant normalization preserves the
original zero-framed knot period after the explicit twist
compensation. A global relative gluing source and its selected
regulator period remain unproved.
