# The quantum matrix torsor and the transport of its base

Research proof, 27 October 2026. On the dense full-cyclic chart, the
actual cyclotomic-normal algebra has an explicit whole quantum-torus
matrix cover. An actual crossing algebra map then splits, constructively,
into a matrix intertwiner and an automorphism of the quantized leaf.
The matrix part has no local lifting obstruction. The base transport
and the selected source are separate data, and the latter has an exact
comparison residual below.

This extends the root-level [regular holonomy line](regular_holonomy_braiding.md)
and [closed-braid period line](closed_braid_period_line.md). Those notes
already construct the root Hom line and its cut. The new issue here is
the noncommutative base of the actual
[full-cyclic Rees module](irregular_rees_full_cyclic_module.md), before
setting its normal parameter to zero. No selected-period or volume
identity is inferred from smoothness.

## 1. A commutative base cannot support the full cyclic normal family

Let R be a commutative ring, and let K,E be invertible N by N matrices
with KE=Q EK. Taking determinants gives

    Q^N=1 in R.                                             (1.1)

In particular a full-cyclic E, for which E^N is a unit, cannot deform
as an N-dimensional matrix representation over a flat commutative
q-normal base with Q^N!=1. This remains true at a nonsingular point
of the classical center. A commutative quantum implicit-function
argument for such finite matrices would start with an impossible
ambient family.

The actual Rees construction avoids (1.1): its entries are operators
on the Fock variable. The base itself is quantized. The construction
below identifies the corresponding matrix cover without a formal
order-by-order choice of matrix entries.

## 2. An exact whole quantum-torus matrix cover

Work over a characteristic-zero field containing a marked primitive
N-th root zeta. Keep Q variable and put c=Q/zeta. On the open set
K Ecal!=0, fix the quantum Casimir Omega. The relation

    F Ecal=Omega-qK-q^(-1)K^(-1)

eliminates F. Thus the actual localized algebra is the quantum torus

    A_Q=<K^(+/-1),Ecal^(+/-1): K Ecal=Q Ecal K>.              (2.1)

Its Laurent monomials are independent: one may either use their
normal-order multiplication directly, or represent K by multiplication
and Ecal by the Q-shift. This also proves flatness in Q on this chart.

Choose nonzero root coordinates k_*,e_* and marked roots k_*^(1/N),
e_*^(1/N). Let

    B_c=<u^(+/-1),v^(+/-1): u v=c v u>.                      (2.2)

Let D,S be constant clock and shift matrices with

    D h_j=zeta^j h_j, S h_j=h_(j+1 mod N),
    D S=zeta S D, D^N=S^N=I.

There is an exact map, for the whole variable Q,

    K=k_*^(1/N) D u,
    Ecal=e_*^(1/N) S v,                                    (2.3)

from A_Q to Mat_N(B_c). Indeed the two commutation factors multiply
to zeta*c=Q. Distinct K^a Ecal^b have distinct scalar Laurent powers
u^a v^b, so the map is injective. Its central powers at the root are

    K^N=k_* u^N, Ecal^N=e_* v^N.                            (2.4)

Adjoining these marked quantum N-th roots gives the full matrix
cover: D and S are recovered from (2.3), and their finite Fourier
projectors and arrows give every matrix unit. Explicitly,

    p_0=(1/N)sum_(r=0)^(N-1)D^r,
    E_ij=S^i p_0 S^(-j).                                   (2.5)

Conversely (2.3), the quantum roots u,v, and (2.5) generate exactly
Mat_N(B_c). This is a noncommutative cover before the root is taken.
The marked cross relations include u Ecal=c Ecal u and
K v=c v K; choosing arbitrary N-th roots without these cross
relations would not specify this cover.
It is not an etale cover of a nonexistent commutative generic center.
At Q=zeta, B_c becomes the commutative root-coordinate cover of the
regular fixed-Casimir leaf, and (2.3) is its ordinary matrix splitting.

This construction is compatible with the dense full-cyclic color
chart already obtained from the actual Verma source. It covers its
Ecal^N!=0 open set. Another chart is needed at an Ecal^N zero; the
identity singularity of the fixed-Casimir leaf has not been removed
by declaring this open set dense.

### 2.1 The exact local logarithmic algebra

For comparison with the actual normal parameter, put

    d=N(Q^N-1), H=N Log(Q^N)=N Log(1+d/N).

Thus H=d+O(d^2), and Q=zeta exp(H/N^2) on the marked branch. Set

    X=N Log u, P=N Log v.

In the completed local algebra, (2.2) is exactly

    [X,P]=H,                                                (2.6)

and

    K=k_*^(1/N)D exp(X/N),
    Ecal=e_*^(1/N)S exp(P/N).                               (2.7)

One can check (2.6) directly inside the original completed quantum
torus. Its logarithms X=Log(K^N/k_*), P=Log(Ecal^N/e_*) satisfy
exp(ad X)P=P+H. The operator ad X raises the complete local
filtration, so taking its formal logarithm gives [X,P]=H. The
operators

    D=k_*^(-1/N)K exp(-X/N),
    S=e_*^(-1/N)Ecal exp(-P/N)

commute with X,P, have N-th powers one, and obey DS=zeta SD.
This recovers (2.7), including its matrix units, from the actual
algebra itself. Completion may be taken with weights X=P=1,H=2;
all normal-order products then have finite coefficients at each weight.

In particular the divided commutator has {X,P}=1. Its symplectic
form is -dX wedge dP, exactly the fixed-leaf Gauss form
-dLog k wedge dLog e in the Rees calculation. On a connected
formal chart the center of this quantum base is the constant ring
k[[H]]: commuting a normal-ordered series with X and P forces its
P and X derivatives, respectively, to vanish. Additional fixed
peripheral parameters belong to that constant ring.

## 3. Constructive matrix Hensel splitting of an actual map

Here is the algebra statement needed for crossing transport. It
works over a noncommutative base.

**Matrix/base splitting.** Let B_s,B_t be complete rings, with a
central ideal of definition containing d, and let

    alpha:Mat_m(B_s) -> Mat_m(B_t)

be a continuous algebra isomorphism. Suppose a specified root frame
G_0 identifies the two systems of matrix units modulo d. Then there
is an invertible G and a base isomorphism theta:B_s->B_t such that

    alpha(a)=G theta_entry(a) G^(-1).                       (3.1)

This requires the given actual alpha. Classical nonsingularity by
itself does not choose theta.

Proof and exact formula: lift G_0 to any invertible G_* and replace
alpha by alpha'=Ad_(G_*^-1)alpha. Now alpha'(E_ij)=E_ij modulo d.
Define the finite sum

    G'=sum_(i=1)^m alpha'(E_i1) E_1i.                       (3.2)

It is I modulo d and therefore invertible. Matrix-unit multiplication
gives, for every a,b,

    alpha'(E_ab)G'=G'E_ab.

Consequently beta=Ad_(G'^-1)alpha' fixes all E_ij. The centralizer
of these matrix units is exactly the set of scalar matrices bI,
even when B_t is noncommutative. Therefore beta(bI)=theta(b)I
for an isomorphism theta; multiplying by E_ij proves (3.1) with
G=G_*G'. This proves existence and gives the intertwiner explicitly.
In particular the base map is also extracted by a finite formula:

    theta(b)=[G^(-1)alpha(bI)G]_(1,1).                      (3.3)

The calculation is not restricted to a Taylor truncation: whenever
alpha, the marked matrix units, and G_* belong to a specified whole
function algebra, (3.2) belongs to that algebra too. Inverting its
unit gives the same whole local formula. The formal theorem alone
does not prove that this inverse or the quantum-root branches extend
globally across their divisors.

At a chosen regular root place the marked quantum roots of Section 2
lift under an actual regular alpha by Hensel functional calculus.
For an element with scalar invertible root value, the derivative of
W^N-a in the unknown W is multiplication by N W_0^(N-1), a unit.
The unique branch obtained this way is the one reducing to the
marked scalar N-th root, not one of the non-scalar finite-order roots.
Uniqueness enforces the required quantum cross relations as well.
For example, writing a=K^N,b=Ecal^N gives ab=c^(N^2)ba. Conjugating
the marked root u by b and taking its N-th power shows
b u b^(-1)=c^(-N)u. Conjugating the marked root v by u and repeating
the argument gives u v u^(-1)=c v. The same proof gives
u Ecal=c Ecal u and K v=c v K. These equalities use the marked
branches with the same scalar root values modulo d.
Thus alpha locally lifts to the specified matrix cover, and (3.2)
then applies. This constructs a local function germ; it does not
replace the branch and localization data of a whole cover.

Apply this to the actual rational R-conjugation on the pair of
localized full-cyclic colors, with m=N^2. At an admissible point
where its denominators and the chosen input/output cyclic charts
are units, it yields an explicit semilinear crossing object (3.5)
below. Its classical base map is the actual root holonomy map. The
procedure constructs an intertwiner of the actual algebra transport;
it does not select the scalar normalization or the original R-source
kernel from that algebra transport alone.

### 3.1 Precisely which torsor is a line?

For fixed alpha and fixed theta, two G in (3.1) differ by a unit
of Z(B_t). Indeed their ratio commutes with all matrix units, so
is bI; commuting also with all scalar matrices forces b central.
If only the matrix-unit equations are fixed, the freedom is B_t^x,
not Z(B_t)^x. Changing G to G bI changes theta to

    theta' = Ad_(b^-1) theta.                               (3.4)

This distinction matters. At the root the whole base is commutative
and the Hom object is an ordinary line over the leaf. Before the
root, fixing the full quantum base transport usually reduces its
scalar freedom to functions of Q and the fixed peripheral parameters.
A nonconstant root rescaling can instead change the subleading base
transport through (3.4), while leaving its classical map unchanged.

There is a semilinear module map

    R_theta(v)=G theta_entry(v),                            (3.5)

which satisfies R_theta(av)=alpha(a)R_theta(v). This is a genuine
linear intertwiner over the constants, with the specified right-base
semilinearity. It need not be represented by a regular scalar
operator on the original Fock representation.

### 3.2 No matrix obstruction can hide a base obstruction

If a regular unit in Mat_m(B) implements an inner automorphism,
its induced action on the scalar commutative algebra B/dB is the
identity: the root scalar matrices are central. Hence a crossing
with a nonidentity classical leaf map cannot be implemented by
such a regular inner unit on a fixed fiber. It must be understood
semilinearly between the transported fibers, or implemented after
an irregular enlargement, as the actual quantum factorial does.

The infinitesimal form is equally explicit. An O-linear derivation
D of Mat_m(O) is inner, with

    H_D=sum_i D(E_i1)E_1i,
    D(E_ab)=[H_D,E_ab].                                    (3.6)

The proof differentiates the matrix-unit identities; the term
E_a1 D(E_11)E_1b vanishes by differentiating E_11^2=E_11.
A general derivation decomposes into its derivation on O and (3.6).
Thus a matrix correction can remove a lifting error precisely after
its base derivation has been accounted for.

Even a smooth symplectic base does not select the higher corrections.
For [P,X]=d, all maps X->X+d a,P->P have the same classical identity.
They are distinct exact automorphisms, implemented by exp(aP) on a
formal coordinate chart. Classical uniqueness of an algebraic gluing
point does not choose among them, or choose a central scalar factor
of its intertwiner.

## 4. Composition, scalar cocycles, and what Hilbert 90 removes

Suppose actual crossing maps alpha_g have been split as in (3.1).
For composable g,h write alpha_(gh)=alpha_g alpha_h. The two matrix
parts satisfy

    G_g theta_g(G_h)=G_(gh) b_(g,h), b_(g,h) in B^x,
    theta_(gh)=Ad_(b_(g,h)) theta_g theta_h.                 (4.1)

To prove that b is a scalar matrix, compare the two sides on each
matrix unit. This yields (4.1) without assuming a strict scalar
cocycle in advance. Associativity gives the exact coherence identity

    b_(gh,k) b_(g,h)
       =b_(g,hk) theta_g(b_(h,k)).                          (4.2)

If the base lifts have also been chosen coherently, so that
theta_(gh)=theta_g theta_h, the b_(g,h) lie in Z(B)^x. Only then
does this become the usual scalar cocycle. In particular equality
of classical center maps does not make the two quantum base maps
equal or make their relative transport scalar. An actual universal
R identity can trivialize the corresponding cocycle; smoothness of
the classical place alone cannot do so.

For completeness the generic finite-Galois descent of such a scalar
line has an elementary proof. Over a finite Galois field extension
L/K let gamma(G)=a_gamma G, with

    a_(gamma delta)=a_gamma gamma(a_delta).

Choose t in L such that b=sum_gamma a_gamma gamma(t) is nonzero.
Such t exists because distinct field automorphisms are linearly
independent: a minimal nontrivial relation, evaluated at tx and
subtracted from its value at t times one chosen automorphism of x,
would give a shorter relation. Reindexing gives

    gamma(b)=a_gamma^(-1)b.

Therefore bG is Galois invariant. This is the needed Hilbert-90
calculation, with its scalar marking explicit. It works over the
generic function field, or the constant Laurent-series field of the
quantized leaf. It does not prove that b is a unit on an entire
integral chart, trivialize a global line bundle, or normalize the
actual cut. Those assertions have divisors and source data of their
own.

## 5. The actual dilogarithm moves the quantum base

The separation above locates the resonant factor of the actual
crossing. For the uncheck nilpotent factor

    Theta=P_Q(q Ecal_1 F_2), P_Q(z)=(z;Q)_infinity,

put X=-e_1 f_2, with e_i=Ecal_i^N,f_i=F_i^N. The root-normal
logarithm has polar part Li_2(X)/d. This follows coefficientwise:
in -sum_(m>=1)z^m/[m(1-Q^m)] only m=N r have poles, and
their leading coefficient is z^(Nr)/(r^2 d). The precise regular
matrix factor and its marked source are retained in
[the explicit crossing regularization](rees_whole_crossing_source_factorization.md).

The actual divided brackets on the two leaves give

    {Li_2(X),k_1}=k_1 Log(1-X),
    {Li_2(X),k_2}=-k_2 Log(1-X),
    {Li_2(X),e_1}={Li_2(X),f_2}=0.                           (5.1)

Since X is constant along this Hamiltonian field, its time-one map
is exactly

    k_1 -> k_1(1+e_1 f_2), k_2 -> k_2/(1+e_1 f_2),
    e_1 -> e_1, f_2 -> f_2,
    e_2 -> e_2+e_1/k_2-e_1 k_2/(1+e_1 f_2),
    f_1 -> f_1+f_2 k_1-f_2/[k_1(1+e_1 f_2)].               (5.2)

For the last two equations, the vector field is

    e_2 dot=(k_2^(-1)-k_2)Log(1-X)/f_2,
    f_1 dot=(k_1-k_1^(-1))Log(1-X)/e_1.

Insert k_1(t)=k_1(1-X)^t,k_2(t)=k_2(1-X)^(-t) and integrate.
The formulas are rational and therefore extend from the log chart
to the indicated divisor open set.

These are the center formulas for Theta alone. Composing with the
actual Cartan automorphism changes the relevant X to
-e_1 f_2 k_2/k_1 and gives the full divisor

    D_c=1+e_1 f_2 k_2/k_1

of the root holonomy crossing. Thus the resonant function has a
specific base action; a finite regular inner matrix factor cannot
supply that action by itself. This is a statement about the actual
crossing, not an identification of its selected braid closure with
the geometric fundamental-class period.

The [Rees-to-Gauss transgression](rees_gauss_period_transgression.md)
is also exact, but has a different role. Its primitives
theta_source=u dp and theta_Gauss=-Log(k/a)dLog e are explicitly
chosen polarizations. Their dilogarithm difference gauges those
prequantum primitives. This does not assert that exp(W/d) is the
actual R, the actual source, or a selected horizontal section.
The joint-meridian correction there must remain part of any such
comparison.

## 6. The source obstruction is an explicit residual, not a matrix lift

First suppose psi,phi are a column and row over the transported base
algebras, so that their coupons are B-linear matrices. Their exact
transport under (3.5) is

    psi_t=G theta(psi_s),
    phi_t=theta(phi_s)G^(-1),                               (6.1)

and phi_t psi_t=theta(phi_s psi_s). For their coupons Gamma=psi phi,
the exact comparison with an independently specified target coupon is

    Delta_Gamma=G theta(Gamma_s)-Gamma_t G.                 (6.2)

Vanishing of (6.2) is equivalent to preservation of the rank-one
source projector. For these B-linear coupons it is unchanged, up to
an invertible scalar, by rescaling G through Z(B)^x. It is therefore
not removable by the remaining scalar freedom of the intertwiner
torsor. Matching the
actual source vector and co-source is stronger still: their common
rank-one coefficient must be the allowed central unit, with the
prescribed normalization.

For the actual finite cut, Gamma contains vacuum evaluation and is
not a regular matrix-valued function on the leaf. One must first
extend theta to its Fock/source module or construct the corresponding
kernel. The source (6.2) is otherwise not even defined in the regular
coefficient algebra. For such operator-valued coupons the scalar
invariance just proved requires the scalar to commute with the source
operator as well. The generic quantum center consists of the constant
parameters, which do commute with this actual vacuum coupon. At the
root the center enlarges to functions on the leaf, and those functions
need not commute with vacuum evaluation. Arbitrary root-leaf units
cannot be substituted for the allowed quantum scalars.

In the actual Rees construction its entries are

    eta^(i-j) exp(-u/d)/N times evaluation at u=0,
    eta^N=d.                                               (6.3)

Every internal finite-head projector also carries exp(-u/d). Their
finite normal jets have the recorded pole bounds and ramified flags;
replacing them by regular leaf functions would change the period.
The matrix splitting proves neither an extension across this
irregular source nor the vanishing of (6.2).

There is also a separate scalar evaluation obstruction. For an
intertwiner line L and a cut functional ell:L->R, a normalized
section ell(J)=1 exists locally if and only if ell of a local frame
is a unit. Smoothness and invertibility of the frame do not imply it.
An exact two-dimensional example, which can be tensored with any
smooth symplectic base, is

    J=[[0,1],[-1,0]], Gamma=(1/2)[[1,1],[1,1]].

Here J is invertible and defines a perfectly regular inner algebra
transport, but Tr(Gamma J)=0 and J Gamma-Gamma J!=0. This is not a
knot counterexample. It disproves the inference from a nonsingular
algebraic place and a lifted intertwiner to a nonzero selected source.

## 7. What is now constructive and what remains for the knot

At an admissible smooth full-cyclic place, the actual rational
crossing map and the marked quantum-root cover determine a local
semilinear crossing object by (2.3), (3.2), and (3.5). Its matrix
deformation is explicit. Its classical leaf transport is forced by
the actual algebra map; its actual resonant dilogarithm gives (5.2).
When base transport is made coherent the remaining ambiguity is an
ordinary central-unit torsor, with the generic descent proved above.

The missing pointed comparison has a precise target: extend that
base transport to the actual vacuum/source lattice, retain every
internal projector, and prove the corresponding residual (6.2)
vanishes with the required scalar evaluation. Nonsingularity of the
Rivin algebraic place supplies none of these source equations by
itself. Conversely this result does not exclude a whole cyclotomic
rigidity theorem after those actual equations and marks are supplied.

The normal direction d at a fixed N remains distinct from the
large-level direction H_N=2 pi i/N. The original finite auxiliary
state is regular at its fixed root. Irregular factors in (6.3) can
cancel polar phases in a whole contraction; regularity does not
determine the eventual N-growth or select a geometric saddle.

The [exact algebra audit](../experiments/audit_quantum_matrix_base_intertwiner_torsor.py)
checks the noncommutative cover, the finite matrix-unit construction
with a noncentral base gauge, the phase vector field, and the source
counterexample. These checks supplement the proofs above. The
[independent proof audit](quantum_matrix_torsor_independent_audit.md)
also verifies the matrix cover, quantum-root cross relations, local
logarithmic scale, matrix/base splitting, weak cocycle, and generic
Hilbert-90 descent.

[Independent matrix/base audit](quantum_matrix_torsor_independent_audit.md)
checks the whole cover, logarithmic scale, matrix-unit construction,
base/scalar freedom, weak cocycle order and Hilbert-90 convention.
