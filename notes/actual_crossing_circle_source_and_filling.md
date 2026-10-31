# Original crossing-circle sources and the complete twist-filling packet

29 October 2026. A crossing-circle source can be calculated from the
original mixed universal crossings and pivotal trace. Its complete-color
operator is generally noninvertible and is nilpotent at even levels.
Therefore a fixed N-colored augmented-link scalar is not, by itself,
an all-port filling state for the original knot.

The constructive replacement is the COMPLETE auxiliary-color packet.
Its N loop operators form a polynomial basis including all confluent
Casimir jets. The explicit Fourier--Hermite kernel then reconstructs
each original full-twist block at polynomial coefficient cost. This
gives an exact arbitrary-width source formula over mixed-color
augmented diagrams, with the original marked cut unchanged.

It does not prove a nonzero geometric coefficient at a fully augmented
base, or transport such a coefficient through long fillings. Those
require the selected mixed-color base period, not just its operator
basis or a positive geometric reference chain.

## 1. The literal encircling operator

Put N>=2, d=N-1, q=exp(pi*i/N), Q=q^2, rho=q-q^-1. The two physical
targets are the original complete V_d heads. Their Casimir is

    Omega=F12 Ecal12+q K12+q^-1 K12^-1,
    Ecal=rho^2 E.

For 1<=j<=N let A_j be the ordinary j-dimensional highest-weight
auxiliary module, with H weights j-1-2a, 0<=a<j. Use the literal
mixed universal R, including q^(H tensor H/2), and close the
auxiliary strand with

    g_j=K_j^(1-N).

There is NO new 1/j or 1/N in this auxiliary trace. The main
modified/marked source stays where it was. Define L_j on the two
physical targets by the actual block-braiding monodromy. With the
auxiliary strand initially in position3 this is the typed braid

    [2,1,1,2],

followed by the original pivotal trace of strand3. Intermediate
crossings use their actual changing strand dimensions.

Write T_n(z)=2cos(n theta) and U_n(z/2)=sin((n+1)theta)/sin(theta)
when z=2cos(theta). These are polynomial conventions:

    T_0=2,T_1=z,T_(n+1)=zT_n-T_(n-1),
    U_0=1,U_1=z,U_(n+1)=zU_n-U_(n-1).

Then the exact all-input circle identity is

    L_j=(-1)^(j-1) U_(j-1)(Omega/2).                      (1)

The notation U_n(Omega/2) means the displayed recurrence U_1=Omega.
In particular L_1=I and L_2=-Omega.

### Independent proof, including the root specialization

First work at generic q with ordinary finite highest-weight modules
and the standard pivotal trace K_j. Block braiding is obtained by
the actual coproduct identities of the finite universal R, proved
coefficientwise in the
[ordinary-color audit](actual_ordinary_color_comparison_audit.md).
The resulting closed loop is a Hopf intertwiner: its cups/caps use
the standard pivot and every mixed crossing is the actual intertwiner.
No division by a quantum dimension enters this statement.

On a target highest vector of H weight n, choose the block-braiding
order in which the first nilpotent factor acts by target E. It
annihilates that vector. In the return crossing any positive target
F power cannot contribute to its highest coefficient. Thus only
the two full Cartan factors contribute to that coefficient, giving

    Tr_(A_j)(K_j q^(n H_j))
       =sum_(a=0)^(j-1) q^[(n+1)(j-1-2a)]
       =U_(j-1)((q^(n+1)+q^(-n-1))/2).                  (2)

For a generic pair V_d tensor V_d the explicit highest vectors have
weights n=2d,2d-2,...,0. Their descendants have total dimension N^2
and distinct Casimir values. Therefore (2) proves the FULL matrix
identity U_(j-1)(Omega/2), not merely its eigenvalues at a root.
All mixed R denominators are [h]!, h<=j-1<=N-1, and target factorial
frame denominators have indices at most d. They are nonzero at q_N.
The matrix identity consequently specializes regularly, including
the actual nilpotent/Jordan coefficients at colliding Casimirs.

At the root the ACTUAL auxiliary pivot satisfies

    K_j^(1-N)=(-1)^(j-1)K_j,

since every H_j weight has parity j-1. This proves (1) with the
literal original pivot and full Cartan normalization. This root
specialization is not a claim about generic-q derivatives of the
ADO pivotal source, for which K^(1-N) must remain literal.

## 2. The full pair relation and the complete-color circle

On the two original complete targets,

    P_N(Omega)=0, P_N(z)=T_N(z)+2.                        (3)

To check (3) without semisimplification, multiply the N quantum-shifted
factors of FEcal=Omega-qK-q^-1K^-1. Their product is F^N Ecal^N=0.
The elementary root product evaluates it as
T_N(Omega)+K^N+K^-N. For two complete heads K12^N=1, giving (3).
The degree-d physical block is the actual irreducible tridiagonal
Jacobi matrix with nonzero adjacent entries. Its first coordinate
is cyclic, so its minimal polynomial has degree N and is exactly P_N.

Equation (1) at j=N is equivalently

    L_N=(-1)^d T_N'(Omega)/N.                            (4)

It annihilates the highest pair vector |0,0>, and the ACTUAL cup p:

    L_N|0,0>=0, L_N p=0.                                (5)

For the first identity use its Casimir c_0=q+q^-1 and U_d(c_0/2)=0.
The same value holds on p. Alternatively its literal highest trace
is q^(d^2)sum_(a=0)^d Q^a=0, retaining the Cartan and pivot.

For even N, T_N+2=T_(N/2)^2. Hence (3)--(4) give

    L_N^2=0.                                            (6)

The operator is nonzero on the degree-d block: P_N there has actual
double Jordan nodes and (4) has a nonzero first derivative at each.
For odd N there is a single simple node -2; all other nodes are
double. There is an exact projector P_St onto that simple total
Steinberg channel, with

    L_N^2=N^2 P_St, L_N^3=N L_N^2.                       (7)

The nilpotent part on the double channels is retained in (7).
These are full matrix statements, not an odd-level semisimple
replacement for the source.

The original tame Hermite source plane makes the missing normal
information especially concrete. In
[its actual normalization](actual_tame_c0_hermite_source_frame.md),

    (Omega-c_0)t=theta p, theta=(-1)^N rho^2,
    mp=1, mt=0, ell p=0, ell t=1.

At c_0 the derivative in (4) is
(-1)^d N/[2sin^2(pi/N)]. Therefore

    L_N t=2N p.                                         (8)

Its coefficient is polynomial, but (8) is a nonzero NORMAL source.
An ordinary positive scalar replacing L_N would lose this datum.

In particular no all-input local operator S_p can satisfy

    R12^(2p)=S_p L_N,

because the left side is invertible on |0,0> and the right side
vanishes there. A scalar at fixed complete crossing-circle color
therefore cannot be inverted into every original filling port.
This does not say that a complete augmented-link scalar is zero,
or that its geometric saddle cannot survive; the original modified
source can detect nilpotent channels after the surrounding tangle.

## 3. The complete crossing-circle filling packet

The N polynomials L_1,...,L_N have successive degrees0,...,d and
nonzero leading coefficients. They are a basis of C[z]/(P_N).
The original complete crossing has the already proved ALL-INPUT form

    R12=kappa r_N(Omega),
    r_N(c_k)=nu_k=(-1)^k q^[k(k+1)],
    c_k=q^(2k+1)+q^(-2k-1),
    r_N'(c_k)/nu_k=-(d-2k)/[2(q^(2k+1)-q^(-2k-1))]       (9)

at each double node. At the odd simple node only its value is
required. The paired node k'=d-k has the same nu, so (9) is
well-defined as a Hermite specification. All original first-normal
coefficients are part of this formula.

For every integer p the
[explicit Fourier--Hermite filling kernel](actual_twist_circle_fourier_kernel.md)
constructs coefficients a_(p,j) such that

    R12^(2p)=kappa^(2p) sum_(j=1)^N a_(p,j) L_j,          (10)
    sum_j |a_(p,j)| <= 2N(1+|p|).                       (11)

The kernel interpolates the full Hermite data of r_N^(2p) modulo
P_N; it is not an interpolation of repeated eigenvalues without
their derivatives. Equation (1) identifies every term of that
polynomial kernel with a literal mixed-color crossing circle.
Consequently (10) is an original tensor/source identity, not an
assumed surgery formula or a semisimple Kirby-color substitution.

## 4. Arbitrary-width original-source filling identity

Take any original marked braid/plat diagram with a fixed collection
of disjoint, specified two-strand full-twist boxes. Write their powers
as R_i^(2p_i), keeping all other signed crossings, turns, pivots and
the original marked cut literally. An odd twist box may retain its
one original half twist and apply (10) only to the even remainder.
At a dual-oriented port transport the actual whole identity by its
given rigid duality; no independent auxiliary cut is introduced.

Remove the full twists and insert a crossing circle in each box.
For colors j_i, let A_N(j_1,...,j_s) be that mixed-color diagram's
literal contraction: physical heads still have complete color N,
each new circle uses its ordinary auxiliary module and pivot from
Section1, and the main modified/marked source is unchanged. Then

    K_N=chi_N product_i kappa^(2p_i)
           sum_(j_1,...,j_s) product_i a_(p_i,j_i)
                              A_N(j_1,...,j_s).         (12)

The displayed chi_N is the original filled-diagram peripheral and
framing line. It has not been replaced by a guessed normalization of
the augmented diagram. If a separately normalized augmented-link
invariant is used, its precise ratio to this literal A_N must first
be calculated. No new 1/N or 1/j average is attached to the circles.

Proof: tensor (10) with all spectators, substitute it at each box,
expand finitely, and apply the unchanged original functional. Each
auxiliary trace in (1) is exactly the local box operator. This proves
(12) at arbitrary braid width, for either sign of p_i and at every N,
with all Casimir normal coefficients retained.

For fixed s the coefficient l1 norm is at most

    product_i 2N(1+|p_i|).                              (13)

It is polynomial for fixed filling slopes, even if they are chosen
large; more generally it is exp(o(N)) when
sum_i log(1+|p_i|)=o(N). This is a quantified original-source filling
map. Taking absolute values in (12) only gives an augmented-family
envelope, not the smaller volume of the filled knot. The oscillatory
kernel and selected filling saddle still matter.

The auxiliary j<N terms in (12) are genuine ordinary modules with
their literal traces. One must NOT identify them with closed
N-dimensional ADO components at ordinary meridian points merely by
the one-component quotient lemma: that lemma does not apply to
separate closed crossing-circle components. The finite all-input
identity (1) is the comparison used here.

## 5. Consequence for a fully augmented geometric-survival strategy

The actual algebraic filling port and its normal data are now explicit.
It is possible to pose the survival problem for a fully augmented
diagram with arbitrarily many twist regions, using its full original
mixed-color packet and (12). This is broader input than a single
twist family and does not replace the knot invariant by an AK state.

What is NOT proved is that this mixed-color base has a positive
original relative cycle with nonzero geometric coefficient, uniformly
in the cusp-color corridor required by long filling. The positive
constrained-lens reference chart does not establish that source
identification. Nor does a fixed-color augmented scalar plus (11)
supply it, because (5)--(8) exhibit its lost normal information.

Even given such a base, its geometric coefficient must be transported
through the actual oscillatory filling kernel, including its boundary
and confluent channels. No Stokes constancy or noncancellation theorem
is inferred just from the polynomial coefficient cost (13).

[Audit](../experiments/audit_actual_crossing_circle_source_and_filling.py)
constructs mixed universal R matrices with their full half-Cartan,
the typed four-crossing loop, original pivotal traces, complete pair
Casimirs and actual positive/negative twist matrices. It compares
all input columns, nilpotent parities and original source normals.
