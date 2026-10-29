# The balanced common-Verma source at the two walls

Research construction, 27 October 2026. A single genuine infinite
balanced module realizes the finite root color as a submodule and
the complete integral color as a quotient. Its boundary has two
opposite rank-one edges, giving an explicit matrix factorization
of the compressed Hopf defect. At the root its block completion
has an exact Weyl pair, coherent source kernel and a literal action
of the regular-meridian centralizer.

These are actual source modules and matrix maps. They do not identify
their coherent parameter with the internal geometric framing of a
knot, or prove its selected Bloch-regulator period or volume norm.

## 1. One genuine module before either specialization

Fix N>=2 and the marked point q=q_N=exp(pi*i/N), M=1. Put
Q=q^2, rho=q-q^(-1), x=-M/q. Work over the local characteristic-
zero coefficient ring R at this point, retaining the prescribed
Cartan half-character. The following are regular parameters:

    delta=1-Q^N,
    w=M Q^(-N)-M^(-1)=(Y-Z)/(MZ),
    Y=M^2, Z=Q^N.                                  (1.1)

Their Jacobian in log Q,log M has nonzero determinant -2N.
On the free direct-sum module with basis v_a, a>=0, define

    K v_a=x Q^(-a)v_a,
    Ecal v_a=(M Q^(-a)-M^(-1))v_(a-1), a>=1,
    Ecal v_0=0,
    F v_a=(1-Q^(a+1))v_(a+1).                    (1.2)

Every matrix column is finite. Direct adjacent-entry multiplication
gives, for all generic q,M,

    K Ecal K^(-1)=Q Ecal, K F K^(-1)=Q^(-1)F,
    [Ecal,F]=rho(K-K^(-1)).                      (1.3)

Thus E=Ecal/rho^2 gives a genuine unrestricted quantum-sl2 module.
There is no generic-M finite-dimensional Hopf premise here.

## 2. The literal rank-one boundary and its two-wall factorization

Let H=span(v_0,...,v_(N-1)) be the finite head and T the remaining
tail. Use the literal inclusion i and projection p. Set

    U(v_(N-1))=v_N, L(v_N)=v_(N-1),

zero on all other basis vectors. In head/tail block notation,

    F=[F_H 0;delta U F_T],
    Ecal=[E_H wL;0 E_T], K=[K_H 0;0 K_T].        (2.1)

The head projector P=i p has exact Ward boundary currents

    [F,P]=delta U, [Ecal,P]=-wL, [K,P]=0.       (2.2)

Compression of (1.3) therefore gives precisely

    [E_H,F_H]-rho(K_H-K_H^(-1))
                         =-delta w P_(N-1).     (2.3)

This is the actual generic finite auxiliary Hopf defect.
On the two corner lines v_(N-1),v_N the odd boundary matrix is

    D_boundary=[0 w;delta 0],
    D_boundary^2=delta w I.                      (2.4)

It is an explicit matrix factorization of the two-wall product,
with its two arrows fixed by the original generator entries.
On R/(delta w) it is a two-periodic complex. No arbitrary choice
of a normal identification is used to construct it.

On delta=0, H is an actual invariant submodule, giving

    0 -> H_root -> V_root -> T_root -> 0.         (2.5)

On w=0, T is invariant and the same finite head is the quotient:

    0 -> T_Weyl -> V_Weyl -> H_Weyl -> 0.        (2.6)

Near the marked point the latter wall is x=q^(N-1), M=-q^N,
the genuine complete integral color. At the intersection both
boundary arrows vanish, and the two marked subquotients agree.
The opposite orientations of (2.5)--(2.6) explain why their
normal derivatives must not be silently identified.

The source and co-source are equally explicit. For the prescribed
balanced head cut e=psi phi, psi=1, phi=(1/N)sum_a, extend it to
the finite-rank ambient coupon Gamma=i e p. Then

    [Ecal,Gamma]=i[E_H,e]p-w i e L,
    [F,Gamma]=i[F_H,e]p+delta U e p.              (2.7)

The original pivot, defect D_cut and modified-dimension line remain
the ones recorded in the actual finite Ward/cut construction.
Equation (2.7) supplies their boundary arrows before normal
specialization; it is not a replacement cut functional.

## 3. Regular infinite R entries and an exact braid excursion adapter

Use the balanced infinite crossing coefficients with no upper
cutoff on a,b. After separating only the original common Cartan
unit, the positive transfer has k=0,...,a and coefficient

    (-1)^k x^(-a-b-k)
       Q^[ab+(a-b)k-k(k+1)/2]
       {b+k choose k}_Q (M^2 Q^(-a);Q)_k.        (3.1)

The negative transfer has k=0,...,b and coefficient

    x^(a+b-k)Q^(-ab)
       {a+k choose k}_Q (M^2 Q^(-b);Q)_k.        (3.2)

Both are Laurent polynomials in the displayed nonzero variables,
since the Gaussian coefficient is polynomial. They are the exact
generic balanced basis changes of the existing Verma R entries;
their apparent divided-factorial poles have already canceled.
Every total-index shell is finite and invariant. These formulas
and their original Cartan line therefore specialize regularly at
the root, including terms k>=N when the input is in the tail.

Let P_b project to H^(tensor b). For a local crossing R_i,

    (1-P_b)R_i P_b is divisible by delta,
    P_b R_i(1-P_b) is divisible by w.             (3.3)

For the first assertion all entering indices are <N and k<N.
An exit through F has a Gaussian numerator 1-Q^N with no zero
denominator. For the second assertion an entering tail index
which returns into the head must cross the E edge at N. Its
Pochhammer product contains 1-M^2Q^(-N)=-M w. The other
possible entering tail index only increases and cannot return.
The same reasoning applies to the inverse crossing, with the
two transfer directions exchanged. Spectator indices do not alter
these assertions.

For a word beta=R_m...R_1, let R_beta^amb be its product on the
common module, and R_beta^H the product of its individually
compressed finite-head matrices. On head inputs the total index
is at most b(N-1). Restrict all ambient calculations to the finite
span of tuples of nonnegative indices with that total bound.
No infinite summation is needed. Expanding each intermediate
head/tail projector gives the exact regular identity

    P_b R_beta^amb i_b-R_beta^H
                         =delta w H_beta.        (3.4)

Every excursion has a first exit containing delta and a return
containing w. This proves divisibility even for words with many
excursions and for both crossing signs. The quotient H_beta is
canonical in the local domain; the path expansion computes it
by finite matrix multiplication. It keeps all phases, Cartan,
twist and boundary factors rather than discarding a multiplier.

At the intersection its value is the sum of paths with exactly
one excursion. This is a concrete mixed-normal connecting matrix.
For a pair of generators F followed by Ecal it reduces to the
rank-one product L U=P_(N-1) in (2.3). For a braid word its
rank need not remain one.

Thus the root submodule and Weyl quotient have an actual common
R realization and a specified off-intersection curvature adapter.
Equality of their ordinary values at the node does not make the
two transverse source jets equal.

## 4. A nonzero root meridian extension Bockstein

Now fix Q=Q_N and vary M. Coefficients in (1.2) are N-periodic.
Put gamma=(-1)^(N+1), kappa_N=M^N-M^(-N). Directly multiplying
N adjacent E edges gives

    Ecal^N v_a=0, a<N,
    Ecal^N v_a=gamma kappa_N v_(a-N), a>=N,
    F^N=0.                                        (4.1)

In particular the first two blocks span an actual 2N-dimensional
root submodule, an extension of the finite head by an identical
head quotient. At M=1 it splits. Nevertheless its first meridian
normal is nonzero:

    [d/dM Ecal^N]_(M=1)
       =gamma 2N [0 I_N;0 0].                   (4.2)

The central operator Ecal^N is zero on both diagonal complete
blocks. A regular first-normal change of splitting changes its
first coefficient by a commutator with that zero operator, hence
cannot remove (4.2). A direct sum of the two finite head families
has Ecal^N identically zero. Therefore this actual first-normal
self-extension does not split. This is a genuine nonzero boundary
extension class, rather than just a nonzero entry of a current
which might later be projected away.

It is still a central root-source extension. It is not the
irreducible hyperbolic representation, and does not by itself
give a nonzero geometric coefficient in the knot period.

## 5. Exact block Weyl pair and the coherent source kernel

Write a=rN+j, 0<=j<N. In the product completion of the root
module let B be backward block shift, killing the first block.
Then (4.1) says Ecal^N=gamma kappa_N B. This identity defines B
integrally even at kappa_N=0; one does not divide two zero values.
The operators are explicitly

    Ecal=E_H tensor I+kappa W tensor B,
    F=F_H tensor I, K=K_H tensor I,
    kappa=M-M^(-1), W=E_(N-1,0).                 (5.1)

The second block operator is the regular divided matrix

    T=[F(q)^N/(Q;Q)_N]_(q=q_N).

On the infinite balanced lattice its generic coefficient is the
polynomial Gaussian {a+N choose N}_Q. At the root,

    T v_(rN+j)=(r+1)v_((r+1)N+j).               (5.2)

This root Gaussian value follows from the finite product formula:
one zero numerator and denominator cancel, giving r+1; the
remaining root factors cancel as a full cycle. No parity sign
remains. Thus

    [B,T]=I.                                    (5.3)

Identify v_(rN+j) with h_j tensor t^r/r!. Then B=partial_t,
T=t. The source kernel

    theta_s(h_j)=sum_(r>=0)s^r v_(rN+j)
                =h_j exp(st)                   (5.4)

obeys B theta_s=s theta_s, T theta_s=partial_s theta_s and
pi_0 theta_s=I. It is a coherent kernel; sending B to s and T
to partial_s is not an algebra homomorphism with the same Weyl
orientation. The t-model fixes that convention explicitly.

The finite rank-N family induced on these kernels is

    E_s=E_H+kappa s W, F_s=F_H, K_s=K_H,
    E_s^N=gamma kappa_N s I.                    (5.5)

It is a genuine unrestricted root quantum-group family:
[W,F_H]=0 and K_H W K_H^(-1)=Q_N W preserve the generator
relations. Its Casimir is unchanged since F_H W=0. The actual
nilpotent head is s=0; its prescribed cyclic completion is s=1.
These are fibers of the same actual source family in a common
completed module, rather than unrelated matching determinants.
The infinite R need not preserve a fixed s fiber; terms k>=N
must remain in its action.

## 6. A literal regular-centralizer torsor representation

Use kappa_N as parameter and the regular-meridian group at M^N:

    J_(M^N)={b:1+kappa_N b invertible},
    b*c=b+c+kappa_N b c.

On the Fock completion put N_block=T B and define

    U_b=exp(bT)(1+kappa_N b)^(N_block).           (6.1)

The second factor means diagonal multiplication by
(1+kappa_N b)^r on block r; no logarithm choice is required.
In the t model it is f(t) -> exp(bt) f((1+kappa_N b)t).
Hence, exactly,

    U_b U_c=U_(b+c+kappa_N b c),
    U_b theta_s=theta_((1+kappa_N b)s+b).         (6.2)

The coherent locus 1+kappa_N s invertible is therefore a genuine
J_(M^N) torsor with anchor theta_0, not only an equality of norm
characters. Its infinitesimal operator is T(1+kappa_N B); on
the kernel it is (1+kappa_N s)partial_s, in that order.
At completeness it becomes the additive translation exp(bT).
This action moves the source central character E_s^N; it is not
asserted to be a fixed-color quantum-group intertwiner or the
centralizer action on a knot's geometric framing coordinates.

The finite source norm is consistent with this action:

    det(I+z E_s)=1+kappa_N s z^N.                (6.3)

Thus it pulls back the regular-centralizer character with
b=s z^N, including its entire divisor. The original adapter
u_N=kappa_N/(M-M^(-1)) and the phase i^(N+3) of d_N remain
the ones already fixed in the actual state. Near M=1 the
normalized power map from J_M is explicitly

    b -> [(1+(M-M^(-1))b)^N-1]/kappa_N.

Its numerator has the same meridian zero; the resulting map is
regular there. It sends the meridian section b=M to b'=M^N.
This supplies an actual algebraic centralizer source action and
its power adapter. It does not identify it with a knot's internal
framing period or determine its regulator integration constant.

There is also a specified source matrix coefficient for its marked
relative period. Since pi_0 U_b theta_0=I_H, the actual normalized
cut of this matrix coefficient is one. The invariant differential
is db/(1+kappa_N b), and the recorded meridian section is b=M^N.
On the marked local logarithmic branch, therefore,

    Phi_cut pi_0 integral_(0)^(M^N)
          U_b theta_0 db/(1+kappa_N b)
          =Log(M^(2N))/kappa_N.                  (6.4)

It has complete value one. With kappa=M-M^(-1) and
u_N=kappa_N/kappa the exact adapter is

    Log(M^(2N))/kappa_N
            =(N/u_N) Log(M^2)/kappa.             (6.5)

Thus obtaining the physical meridian period from the upstairs one
uses u_N/N; the reverse power pullback uses N/u_N. The logarithm
sheet and the whole u_N divisor remain marked. Formula (6.4) is
an actual coherent-source matrix coefficient and its invariant
group differential, not an arbitrary division by a group volume.
It is a universal centralizer normalization period, not the
knot-dependent marked Bloch regulator or its volume constant.

## 7. Comparison with the earlier source constructions

The repository already has an unbalanced Verma period in
[the Frobenius Verma note](frobenius_verma_period.md), with the
exact Alexander denominator, and genuine F-cyclic holonomy sources
in [the carry-braiding note](semicyclic_carry_braiding.md).
[The tetrahedral transport note](verma_tetrahedral_transport.md)
already supplies pointed compact-factor rewrites. No new Burau
invariant or previously unavailable Verma construction is claimed.

The present root lattice is different. The generic basis change
v_a^unbalanced/(Q;Q)_a is a unit only for a<N at the root;
it is singular on later blocks. Consequently the balanced root
lattice has F^N=0 and nontrivial Ecal^N block lowering, whereas
the unbalanced lattice has the opposite Frobenius behavior.
One cannot substitute one root lattice for the other without
its factorial carry and normal data. The new statements here are
the explicit two-wall submodule/quotient comparison, nonzero
extension Bockstein, dual E-cyclic coherent kernel, and literal
Weyl/regular-centralizer source action.

The complete-color q-normal and the fixed-root meridian normal
also retain their distinct pivot/twist adapters from
[the complete divided-Ward note](complete_color_divided_ward_and_fusion.md),
Section 7. Those moments must accompany any closed period map.

## 8. Remaining geometric source map

This constructs the common source, both branch maps, their mixed
normal curvature and a genuine centralizer torsor action from actual
matrices. The marked finite cut is still the head source with its
original coupon and normal row. The infinite R acts on coherent
parameters, so its high-transfer terms cannot be discarded when
comparing a nonzero s fiber with that head.

No identification of this torsor with the selected geometric
framing of a hyperbolic A-curve has yet been proved. Nor has a
nonzero global coefficient of the regulator period been obtained.
The exact adapters above specify what such a source map must
carry, rather than infer it from equal normal values or a norm
character alone.

[Exact matrix audit](../experiments/audit_common_verma_two_wall_source.py).
[Results](../experiments/common_verma_two_wall_source_results.json).
[Independent proof audit](common_verma_two_wall_independent_audit.md).
