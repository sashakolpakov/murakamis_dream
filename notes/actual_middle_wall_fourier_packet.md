# An actual dressed middle wall is a Fourier-mode projector

28 October 2026. A literal aggregate of the ORIGINAL middle-wall
operators has an exact Fourier/Plancherel reduction. Its two Euler
factors can separately have exponential norm, and its wall has both
zero and positive integer carry. Their COMPLETE packet is nevertheless
a known unitary clock times N times a rank-N cyclic Fourier projector.
The full wrap parameter, Cartan line and marked source are retained.

This is a boundary/current-kernel simplification, not a substitution
for the original knot invariant. Its precise placement is essential.
It does not bound an arbitrary F_H-conjugated wall or the complete
unmodified knot scalar, and gives no volume lower bound.

## 1. The actual literal factors and the failed separate damping

Use the conventions of
[the literal middle certificate](literal_middle_full_phi_certificate.md):

    Q=exp(2pi*i/N), d=N-1, x=-exp(-pi*i/N),
    k=x^N=(-1)^(N-1), lambda=x^(-1)=Qx,
    S_1^N=mu, S_2^N=k mu,
    X=x S_2 S_1^(-1), Z=Z_1,
    n=e_1 S_2, n_-=-e_1 Z_2 S_2,
    P(A)=sum_(h=0)^d (-1)^h Q^(h(h-1)/2) A^h/F_h,
    F_h=(Q;Q)_h,
    W=E_d(Z)X=x mu^(-1)|d><0| tensor S_2.      (1)

The full original checked positive crossing is

    B_plus=kappa Flip D P(n_-)P(n),
    D|a,b>=x^(-a-b)Q^(ab)|a,b>.                (2)

All displayed factors in (1)--(2) are actual finite operators. The
original kappa has not been normalized away; it is external only
to simplify writing the following packet.

The split W=W_0+W_+ has

    W_0=x k |d,0><0,d|,
    W_+=x mu^(-1)|d><0| tensor sum_(b<d)|b+1><b|. (3)

Their integer degrees are 0 and +N. Between whole original crossings
the positive part is source-null. INSIDE (2), however, the adjacent
Euler factors have negative carries. In fact

    pi_0(n W_+)=k(1-Q)|d-1,0><0,d-1| !=0.     (4)

Conjugation by r^D scales W_+ by r^N and the negative part of n by
r^(-N); (4) is unchanged. The
[positive-carry damping theorem](actual_exponentially_tame_carry_completion.md)
therefore cannot be applied separately to these internal factors.
The following identity controls the actual aggregate instead.

## 2. The complete aggregate is exactly a Fourier projector

Define the specified checked wall packet

    L=Flip D P(n_-) W P(n).                    (5)

Then, for EVERY N>=2, parity and nonzero typed wrap mu,

    L=x^2 Z_1^(-1) sum_(j=0)^d X^j
      =N x^(N+1) g_1 E_0(X),
    g_1=x^(1-N) Z_1^(-1),
    E_0(X)=N^(-1)sum_(j=0)^d X^j.              (6)

The full original Cartan scalar gives kappa L, with the same
original framing/peripheral source lines as (2). No unknown scalar
or numerical norm factor is used in (6).

Here is an entry proof including the cyclic wrap. Let (a,b) be
the input and (c,e) the output BEFORE the final Flip. Put
r=[a+b]=[c+e], and epsilon_in=(a+b-r)/N,
epsilon_out=(c+e-r)/N. The entry is zero unless these residues
agree. The right P(n) must lower the first input a to zero, hence
only its power a contributes. Since

    e_1|a>=lambda(1-Q^(-a))|a-1>,
    (Q^(-1);Q^(-1))_a
        =(-1)^a Q^(-a(a+1)/2)F_a,

its coefficient simplifies EXACTLY to x^a times S_2^a. The wall
then raises that first index to d. The left P(n_-) must have
power s=d-c. Root reflection

    (Q^(-1);Q^(-1))_c F_(d-c)=N

cancels its entire factorial denominator. Its remaining coefficient
is lambda^s Q^[s(a+b+1)+s^2]. The total S_2 power is N+a-c,
so its wrap count is 1+epsilon_in-epsilon_out. Its first wrap
k mu cancels the mu^(-1) in W. Simplifying the remaining powers
gives the FULL entry

    (P(n_-)WP(n))_(c,e;a,b)
      =x^(a+c+2)Q^(-(c+1)e)
                    (k mu)^(epsilon_in-epsilon_out). (7)

This includes all positive, zero and negative total-degree paths;
none was discarded after taking absolute values. Multiplication
by D and then Flip, with output written (u,v), makes (7)

    L_(u,v;a,b)=x^(a+u+2)
                    (k mu)^(epsilon_in-epsilon_out). (8)

On the other hand, exactly one summand X^j, j=[a-u], connects
these states in the same total-degree residue class. Its coefficient
is x^(a-u)(k mu)^(epsilon_in-epsilon_out). Multiplying by the
output factor x^2 Q^(-u)=x^(2u+2) proves (6).

## 3. Plancherel, exact norm and reduction to one channel head

For |mu|=1 the literal X is unitary and X^N=1. It has N disjoint
cycles, labeled by total degree modulo N, and its eigenvalue-one
space has dimension N. Thus E_0(X) is an ORTHOGONAL projector.
Equation (6) gives

    rank L=N, ||L||=N,
    L^dagger L=N^2 E_0(X),
    LL^dagger=N^2 Z_1^(-1)E_0(X)Z_1.            (9)

This is an exact two-copy positive contraction. It is not inferred
from positivity of the original pivotal trace, which is false.

For explicit normalized channel vectors, set b=[r-a] and
epsilon=(a+b-r)/N, and put

    U|r>=N^(-1/2)sum_(a=0)^d
           x^(-a)(k mu)^(-epsilon)|a,[r-a]>.

Different r have disjoint support, and XU=U. Therefore

    U^dagger U=I_N, E_0(X)=UU^dagger,
    L=N x^2 Z_1^(-1) U U^dagger.                (10)

It follows that every occurrence of this actual two-head packet
can be replaced by two known isometries with ONE N-dimensional
internal channel. Its previous two-head cut had dimension N^2.
A normalized root Fourier transform on the r-channel is unitary;
Plancherel preserves both exterior channel norms exactly.

For example retain any specified exterior row Lambda, state psi
and original surrounding operators A,B. Equation (10) gives

    Lambda A(kappa L)B psi
      =kappa N x^2 <alpha,beta>,
    alpha=U^dagger Z_1 A^dagger Lambda^dagger,
    beta=U^dagger B psi.                        (11)

Original spectator indices can remain as tensor factors in (11).
Every original cap, pivot and normalization remains in Lambda,
psi,A,B; these are not chosen from the unknown knot value. Hence

    |Lambda A(kappa L)B psi|^2
                  <=N^2 ||alpha||^2 ||beta||^2. (12)

The same identity holds after a unitary DFT of both channel
vectors. Formula (11) is an actual local channel reduction, not
the tautological Fourier transform of an already evaluated scalar.
Its two exterior vectors need not agree or be conjugates; (12)
does not give a lower bound or geometric alignment.

For a fixed compact nonunit wrap, each X^j has norm at most
max(|mu|,|mu|^(-1)), because each head can wrap at most once.
Thus ||L||<=N max(|mu|,|mu|^(-1)); the unitary formulation is
used only for |mu|=1. No exponential source conditioning is hidden
by fixing a regular nonzero wrap.

## 4. Precise original-source placement and marked face normalizers

Let P=P(n), H=P^(-1)ZP and define the CORRECT transported wall

    W_H=P^(-1) W P.                            (13)

Then the actual input insertion has exactly the packet (5):

    B_plus W_H=kappa L.                        (14)

This is valid inside every original signed word and with its
ENTIRE fixed co-source, simply by the literal matrix identity.
It is not the false relocation B_plus W -> W B_plus. Bare W
and the transported W_H are different coupons.

The marked full-Phi clocks are the original ones,

    F_Z=phi_N diag_j(1/F_j), F_H=P^(-1)F_ZP.

Since W has first input zero and first output d, F_d=N gives

    F_Z W F_Z^(-1)=W/N,
    F_H W_H F_H^(-1)=W_H/N,
    B_plus F_H^s W_H F_H^(-s)=kappa N^(-s)L.    (15)

The exact phi_N cancels only in this specified conjugation; it
has not been deleted from a one-sided face or source. Similarly
for the original factorial face frame Gamma_j,
Gamma_d=N^2 Q^(-1), Gamma_0=1, so

    Gamma W Gamma^(-1)=N^2 Q^(-1)W.             (16)

Transporting BOTH Gamma and W by P gives the same relation in
the H frame. Any bounded number of these MATCHED conjugations
therefore changes the packet by known polynomial powers of N
and recorded root phases, despite exponential standalone norms
of Gamma, P or F_H.

These identities do not bound arbitrary one-sided F_H factors
or an untransported wall in an unrelated slot. A full middle-move
comparison must exhibit (13)--(15), or another exact matching of
its actual interfaces, before invoking (9)--(12).

For a concrete source check, the ORIGINAL cup has Xp=Q^(-1)p.
Thus Lp=0, while the bare wall has the known nonzero mWp.
This distinction is compulsory: the packet cannot be substituted
for the bare wall in the old endpoint formula. If an explicitly
transported source has X-eigenvalue one, its E_0(X) channel instead
survives, with its actual transported dual still retained.

## 5. The original affine cap is a charged Fourier mode

There is an exact bridge from (6) to the FULL original nilpotent
source, before replacing a knot cut by its scalar value. Put

    T=Z_1 Z_2, P_d=E_d(T), P_cap=P_d E_0(X).

T commutes with X. Since the integer degree of two physical heads
lies in [0,2d], its eigenvalue Q^d has exactly the ONE lift D=d;
the putative second lift d+N exceeds 2d. Thus P_d is precisely
the original positive affine cap charge D+1=N, with no zero-winding
alias. At r=d the isometry vector in Section 3 is

    w=N^(-1/2)sum_a x^(-a)|a,d-a>,
    P_cap=|w><w|.                              (17)

It is independent of mu. Even for a nonunit mu, X restricted to
this degree-d sector is unitary: its two simultaneous endpoint
wraps cancel the mark. Hence P_cap is an orthogonal rank-one
projector for every nonzero typed mark at complete color.

Use the ORIGINAL cup and ordinary right cap

    p_(a,b)=N x^(-b) delta_(a+b,d),
    l_(a,b)=x^b g_a/N delta_(a+b,d),
    Pi_N=p l.

Direct substitution of (17) proves

    Pi_N=N g_1 P_cap,
    Pi_N^dagger Pi_N=N^2 P_cap,
    P_d(kappa L)=kappa x^(N+1)Pi_N.             (18)

The pivot is indispensable. It moves the ket's X-eigenvalue
from one to Q^(-1), the exact original cup mark; <w,g_1 w>=0,
so Pi_N^2=0. This positive two-copy identity therefore does not
contradict the failure of a positive one-copy pivotal trace.

Retain the actual partial closing

    Phi_g(A)=Tr_2[A(I tensor g)].

The same original turns give Phi_g(Pi_N)=I. Consequently for ANY
finite matrix C on the open cut, not merely a scalar intertwiner,

    C=(kappa x^(N+1))^(-1)
          Phi_g[(C tensor I)P_d(kappa L)].       (19)

This is a source-normalized opening through the actual wall packet.
Its factor is a known original Cartan/root phase, not a scalar chosen
from the value of a knot period. The external modified dimension,
framing and peripheral line multiply both sides unchanged.

The vector w is maximally entangled: Tr_2(P_cap)=I/N. Equation
(18) therefore also proves, for EVERY C,

    ||(C tensor I)Pi_N||_HS^2=N||C||_HS^2.       (20)

For the actual knot cut C=K_N I this is N^2|K_N|^2. Unlike a Fourier
transform of an already scalar K_N delta, (17)--(20) specify the
original charged source and an explicit local Fourier projector
before that scalar reduction. They may be inserted into the full
uncontracted original tensor network. Plancherel then acts on
known head or channel variables with all normalization fixed.

There is a source-preserving positive averaging at this TERMINAL
opening. Set

    P_k=Z_1^k P_cap Z_1^(-k), Pi_k=N g_1 P_k,
    k=0,...,d.

The vectors Z_1^k w are an orthonormal Fourier basis of the
degree-d sector. Every P_k has marginal I/N. Thus exactly

    sum_k P_k=P_d, Phi_g(Pi_k)=I,
    ||(C tensor I)Pi_k||_HS^2=N||C||_HS^2,
    sum_k ||(C tensor I)g_1 P_k||_HS^2=||C||_HS^2. (21)

For the partial closing, the only nonzero traced entry has
b=d-a, and its two pivotal factors obey g_a g_(d-a)=1;
the Fourier phases cancel. This proves the middle identity for
an arbitrary nonscalar C, independently of an intertwining or
scalar-cut assumption. The other identities follow from the
orthogonal modes and their identical marginals.

Equivalently the positive terminal density N P_cap can be replaced
by its clock average P_d when testing ANY operator on its FIRST
leg alone. This is an exact positive mixed boundary source, with
the factor N retained. It does not average an internal paired
source on which the exterior acts on both legs. In particular it
does not justify replacing local doubled Euler coefficients
c_a conjugate(c_b) by their diagonal a=b terms. Such an internal
dephasing would require another source identity.

Equations (19)--(20) still contain the original exterior pivotal
contractions. Their norm is not determined by the nonzero local
projector. In particular they provide no lower bound for its
geometric overlap and no Rivin-volume estimate for the whole
doubled network.

## 6. Integer degree and the remaining geometric limitation

The degree-zero part of (7) has c+e=a+b, and its total-degree
blocks have rank one and unit-modulus entries. Its norm is N.
If all OTHER exterior factors preserve total integer degree, the
original pivotal first-cut and marked-plat sources kill the
packet's +/-N parts. This gives an exact source replacement by
that degree-zero packet, not a scalar relocation to an endpoint.

Retaining the full Fourier projector (10) is often the simpler
representation: integer-degree projection would split its N
modular blocks into 2N-1 ordinary blocks. Neither operation makes
the entire knot source positive or bounds its other crossings.

The projector in (6) is a position-ratio clock X, not a physical
head clock Z_1. Its correctly transported version can be a relative
H-wall. Therefore the finite physical-projector action-zero theorem
cannot simply be applied to (6). A regular geometric source can
meet an auxiliary face degeneration. The useful rigorous conclusion
is the polynomial norm and explicit one-head Plancherel reduction;
geometric support and source overlap of the remaining exterior are
still additional work.

## 7. Audit

    python3 experiments/audit_actual_middle_wall_fourier_packet.py

The audit compares (6)--(8) directly with the literal finite Euler
operators for both parities and nontrivial wrap marks. It retains
the actual Cartan, checked flip, original cup/marker, and complete
figure-eight pivotal source. It checks the transported-source
identity (14), marked normalization (15), and independent complex
isometries/double-layer Plancherel identities. It tests all terminal
Fourier modes, their positive average, and arbitrary nonscalar cut
matrices in (21). The entry calculation
above proves the all-level formula.
