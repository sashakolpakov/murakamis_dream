# The actual matching source as shared cycle Fourier periods

30 October 2026. Fixing the matching
magnetic labels reduces every physical component of the original
complete-circle source to a one-variable cycle or marked path.
The matching magnetic labels are bounded integral Kirchhoff flows.
The exact unused-node zeros permit a full N-node Fourier sum, with
literal affine lifts and no wrapping of the physical indices.
The actual cups and caps cancel the half-character parity at BOTH
level parities. The original mark selects a specified Fourier charge.

This supplies a joint positive comparison energy of coherent cycle
periods. It does not identify that energy's maximum with hyperbolic
volume or prove survival of the original summed contribution.

## 1. Freeze the actual matching labels, not the physical wires

Use the original complete-circle source of
[the full matching-graph theorem](general_matching_graph_full_normal_source.md).
Put q=exp(pi i/N), Q=q^2, d=N-1, M=floor(d/2). At circle i retain
its folded label a_i and its ordinary matching magnetic index r_i:

    0<=a_i<=M, 0<=r_i<=2a_i,
    W_(a_i) pi_(a_i)=sum_(r_i) W_(a_i)[r_i] pi_(a_i)[r_i].

All original white maps, including their reversal and positive
ordinary channel metric, are the actual pi maps. No paired norm
pi_a W_a is inverted. The original circle multiplier is still
h0_a omega_a^epsilon, as in the full source theorem.

After these indices are fixed, every W or pi vertex has two physical
ports. Its only support condition is the EXACT integer equation

    u+v=T_i=d-a_i+r_i.                               (1)

Every physical cup or ordinary cap has support u+v=d. Straight
segments identify their endpoint indices. Thus the physical graph
is a disjoint union of cycles. The one original unrestricted mark
cuts its cycle into a path with a dense endpoint functional. The
matching labels are still shared by their two incident vertices;
they have not been maximized or summed independently.

At the root the original physical cup, cap, and mark are

    pV(u,d-u)=N q^(-d^2) q^(du),
    ellV(u,d-u)=N^-1 q^(du),
    mark(u,v)=N^-2 q^(dv).                           (2)

These are the given source tensors, in their recorded order. The
last row is unrestricted; it is not an invariant cap substituted
for the physical mark. Any exterior framing line remains the one
already recorded for the original invariant.

Let F_c(a,r) denote the coherent physical contraction of component
c, with every actual local scalar in it. The source is EXACTLY

    A_(D,N)=sum_(a,r) product_i[h0_(a_i)omega_(a_i)^epsilon_i]
                                      product_c F_c(a,r). (3)

This is the root source identity itself. Its circle normals are
already retained in h0_a pi_a, and its physical mark remains (2).
It is not obtained by differentiating a truncated root formula.

## 2. Every fixed physical vertex has the same finite continuation

For a vertex with (a,r), define

    T=d-a+r, t=min(T,2d-T), b=max(0,T-d).

Then d-a<=t<=d. In its actual first physical coordinate u its
nonzero entries have the form

    V(u,T-u)=c_V f_(t,a)(u-b),                       (4)

where c_V is the ACTUAL endpoint entry V(b,T-b), and f_(t,a)(0)=1.
For W, this follows by normalizing its physical column and using
the original root partner identity. The high-degree block is the
actual translated low block, not a freely changed framing.
For pi, the exact relation

    pi_a(r;u,v)=G_(a,r)^-1 conjugate(W_a(v,u;r))

and the root column reflection
f_(t,a)(t-y)=f_(t,a)(t) conjugate(f_(t,a)(y)) give (4),
with its own actual endpoint c_V. The endpoint has modulus one
before the W/metric scalar. Both local maps therefore use the same
normalized finite f; their different constants are retained.

The [literal magnetic polynomial](actual_q_hahn_magnetic_complex_corridor.md)
gives a degree-a polynomial G_(t,a) satisfying

    f_(t,a)(y)=q^[(d-2a)y] G_(t,a)(Q^y),
    G_(t,a)(q^t z)=c_(t,a) P_(t,a)(z),
    P_(t,a)(z)=sum_(k=0)^a p_(t,a,k) z^k,
    p_(t,a,k)>0,
    c_(t,a)=q^[a(t+a-d)]/(Q;Q)_a.                    (5)

For a=0 the polynomial is one. Every power in (5) has its literal
specified exponent. In particular this is a finite continuation
at ALL integer y, including values outside the physical range.
Its unused-node zeros are

    G_(t,a)(Q^y)=0, t+1<=y<=d.                       (6)

The positivity and zeros in (5),(6) were proved from the original
coproduct. They are not inferred from a Fourier fit to samples.

Equivalently, each physical vertex in (4) has the finite expansion

    V(u,T-u)=c_V c_(t,a)
         sum_(k=0)^a p_(t,a,k)
                     q^[(d-2a+2k)(u-b)-tk].         (7)

The scalar and the t-dependent phase in (7) must both be retained.
Only the p coefficients are declared positive.

## 3. The first-failure zero lemma permits a full grid

Choose a starting physical leg with value x in {0,...,d}. Along
an ordinary vertex the other leg is T-x; at a cup or cap it is
d-x. Straight intervals preserve the value. Hence all succeeding
leg indices are literal affine functions

    u_e=epsilon_e x+b_e, epsilon_e in {1,-1}, b_e integer. (8)

No modulo-N reduction is made in (8). The admissible x originally
form an integer interval, with the final cycle closure imposed.
Nevertheless the product of the continued factors (7) is zero
at every x outside that interval.

To prove this, take the FIRST vertex where a legal incoming index
u in [0,d] would produce an illegal outgoing index. Cups and caps
cannot cause that failure. If T=t<=d, it means u>t. If the incoming
port is the first port, the polynomial argument is u in the unused
range of (6). If it is the second port, the argument is t-u<0;
its residue modulo N lies in {t+1,...,d}, again a zero of G.

If T=2d-t>d, failure means u<T-d. On the first port the normalized
argument is u-(T-d)<0, whose residue modulo N is in {t+1,...,d}.
On the second port it is d-u, directly in that unused range.
The same zeros hold for the actual white dual by (4), or directly
by conjugating its reversed column. Thus that first illegal vertex
has zero continued coefficient. Later affine indices need not be
repaired; all later finite exponential polynomials remain defined.

Therefore the cycle or path variable may be summed over ALL
x=0,...,d. This lemma does not make f periodic: at even levels it
is antiperiodic under y->y+N. Literal exponents in (7),(8) avoid
losing precisely those signs.

For an unmarked cycle the final value is epsilon x+B. Its exact
closure may be replaced by

    delta_N((epsilon-1)x+B).                         (9)

Indeed, whenever the product is nonzero all propagated leg values
are in [0,d], so congruence of the final and initial values implies
their equality. There is no surviving false winding state. At the
marked component the final and initial values are instead inserted
in the original dense row in (2); no closure delta is imposed.

## 4. Integral Kirchhoff flow and the actual mark

Restore the ordinary cap only for the purpose of recording the
physical graph. Its nodes have a canonical bipartition: W and cup
nodes have two outgoing ports; pi and cap nodes have two incoming
ports. Every original straight physical interval joins opposite
types. Each physical cycle therefore has an EVEN number of nodes,
including its cups and caps. Contracting these bivalent cup/cap
nodes prematurely would hide this parity statement.

Collapse every physical cycle to a vertex of a graph Gamma, and
orient matching edge i from its pi cycle to its W cycle. Set

    w_i=r_i-a_i,       -a_i<=w_i<=a_i.               (10)

An ordinary physical cycle closes if and only if its signed
alternating sum of total degrees is zero. With the bipartition just
specified, that defect is

    B_c=sum_(W on c)(d-a_i+r_i)-sum_(pi on c)(d-a_i+r_i)
                            +d(#cups on c-#caps on c)
       =sum_(W on c) w_i-sum_(pi on c) w_i
       =(div_Gamma w)_c.                            (11)

All d terms cancel because the two bipartite classes on a cycle
have equal size. Each matching edge contributes with opposite signs
to its two ends, so sum_c B_c=0 identically. Nonzero unmarked cycle
contractions force their EXACT defects B_c=0, not just congruence
modulo N. The omitted equation on the marked cycle then follows
from the others. Thus (3) can be restricted EXACTLY to the bounded
integral flow space

    w in ker(div_Gamma:Z^R->Z^C), |w_i|<=a_i.        (12)

There may be further quantum cancellations inside this support.
The assertion is not that every flow gives a nonzero source term.

On such a flow the marked endpoints are complementary. Let x be
the SECOND coordinate of the original mark, so its first coordinate
is d-x. Only now compare it with the ordinary cap in (2):

    mark(d-x,x)/ellV(d-x,x)
                  =N^-1 q^(-d^2) Q^(dx).            (13)

This is the original specified mark, not a redefinition of it.
Since d=-1 modulo N, it supplies a one-unit Fourier character.
If instead the first marked coordinate were called x, its charge
and constant phase would have the opposite displayed convention.

## 5. The exact shared-cycle Fourier compiler

Insert (7) at every W or pi vertex of a physical component, and
insert the monomials (2) at its cups/caps or marked endpoint.
By (8), the dependence on x in each term is a SINGLE character

    q^[m_c(k)x],

where m_c(k) is an explicitly determined integer affine function
of the LOCAL Fourier indices k_v. All remaining factors consist
of the positive product product_v p_(t_v,a_v,k_v), the original
scalar endpoint/cup factors, and explicit q phases depending on
the SAME matching labels and Fourier indices.

For an arbitrary formal cycle one could expand its closure as

    delta_N((epsilon-1)x+B)
      =N^-1 sum_(h=0)^d q^[2hB+2h(epsilon-1)x].      (14)

Thus its x sum is evaluated exactly by

    S_N(m)=sum_(x=0)^d q^(mx)
      = N                         if m=0 mod 2N,
      = 0                         if m even but not 0 mod 2N,
      = 2/(1-q^m)                if m odd.            (15)

For the ACTUAL source the odd case in (15) disappears for a proved
reason. Every W/pi node has carrier parity d-2a=d modulo 2; every
cup/cap and the dense mark has carrier parity d as well. The sign
of the affine coordinate does not change that parity. Since the
restored component has an even number of nodes, its total frequency
m_c(k) is even for every Fourier tuple, at both level parities.
The marked path has one fewer ordinary node and the mark supplies
the last carrier. Thus the same conclusion holds before replacing
the mark by its charged cap. The terms 2k and the closure terms
in (14) do not alter the parity. Omitting a pivotal cup/cap carrier
would destroy this argument.

On a flow (12), let L_c(X) be the finite Laurent polynomial obtained
by multiplying the ACTUAL continued ordinary vertex and cup/cap
factors on c, with X=Q^x. It exists by this even-frequency result.
Use the second marked coordinate for the variable on the marked
cycle c_*. Let [X^b]_N denote cyclic coefficient extraction modulo
X^N-1, summing every Laurent coefficient of exponent b modulo N.
The full-grid lemma and (13)--(15) give

    A_(D,N)=q^(-d^2) N^(C-1)
      sum_(a,w:div w=0, |w_i|<=a_i)
        product_i[h0_(a_i)omega_(a_i)^epsilon_i]
        *[X_(c_*)^1]_N L_(c_*)(X_(c_*))
        *product_(c!=c_*) [X_c^0]_N L_c(X_c).         (16)

Here C is the number of restored physical cycles. Every constant
endpoint, cup, cap and source phase is included in L_c. For the
marked cycle the Fourier sum contributes N and the original ratio
(13) contributes 1/N; this explains the exact N^(C-1), including
its phase q^(-d^2). Formula (16) is valid at BOTH level parities.

It can be evaluated by cyclic convolution of coefficient arrays
of length N, without enumerating all Fourier tuples. In an expanded
form it is a finite sum with positive local p coefficients, the
original scalar factors, explicit t_v-dependent phases, integral
Kirchhoff constraints (12), and coupled Fourier congruences from
(16). Those phases are not removed by positivity of the p's.

## 6. A joint energy, with every shared state retained

Define the explicit positive comparison

    Z_cycle(N)=sum_(a,r) product_i h0_(a_i)^2
                                      product_c |F_c(a,r)|^2.     (17)

Each cycle period in (17) is evaluated coherently BEFORE its
absolute square. The matching labels and their magnetic indices
remain common to both incident vertices and to all components
they connect. If there are R original circles, the number of
matching states is at most N^(2R), so finite Cauchy gives

    |A_(D,N)|^2 <= N^(2R) Z_cycle(N).                (18)

The circle half-twist phases have modulus one, but are removed
only in this stated upper bound, not from the exact identity (3).
This is one joint comparison energy for arbitrary fixed bridge
width. It neither maximizes each vertex independently nor replaces
each F_c by a product of column norms.

To turn (17) into the desired geometric theorem, one must still
control the coherent cycle periods with their shared labels and
identify the resulting constrained action, including its phases,
with the actual marked gluing equations. The real Legendre action
of positive Fourier coefficients alone is not such an identification.
A lower bound or contributing-cycle argument for (3) is still
required; (18) allows complete cancellation in the original source.

Audit: [original fixed-label cycles and full Fourier kernels](../experiments/audit_actual_matching_graph_shared_cycle_fourier_compiler.py).

Independent review: the root agent and cluster/source agent checked
the complete proof, including the original white normalization,
both-port first-failure zeros, exact Kirchhoff support, both-parity
carrier cancellation, and the original marked charge. The cluster
agent freshly replayed the audit: 40 literal fixed-label plats,
440 physical vertex polynomials, 117 first-failure zeros, 80 even
carrier components, and 17 exact charged coefficients passed.
This review does not assert a global energy asymptotic or
noncancellation of the original source.
