# A positive Fourier partition with the original shared constraints

30 October 2026. The exact shared-cycle
compiler admits a fully positive coefficient comparison whose scalar
weight is explicit in the original source normalization. Every
matching label, integral Kirchhoff equation and physical-cycle Fourier
congruence is retained. This is an upper bound for the original
complete-circle source, not a volume equality or a noncancellation
theorem.

## 1. Original endpoint scalars, including the high-degree adapter

Use the notation and recorded physical-port orders of
[the exact shared-cycle compiler](actual_matching_graph_shared_cycle_fourier_compiler.md).
Thus q=exp(pi i/N), d=N-1, s_j=product_(h=1)^j 2sin(pi h/N),
0<=a<=floor(d/2), r=a+w, |w|<=a. The physical total and its low
adapter are

    T=d+w,             t=d-|w|.

Write c_W=W_a(b,T-b;r), b=max(0,T-d), for the actual first
endpoint of the original Clebsch column. Then

    |c_W|=s_a/(s_|w| s_(a-|w|)).                    (1)

Here is a proof retaining the normalization. If r<=a, the endpoint
has first physical index zero. In the original coproduct
Delta F=F tensor 1+K^-1 tensor F, only its second summand can reach
that endpoint from the highest column. Dividing by the original
ordinary-channel descendant factors gives, with F_j=(Q;Q)_j,

    c_W=q^(-dr) F_(d-a+r)/(F_(d-a)F_r).             (2)

The highest endpoint is one. Taking absolute values and using
s_(d-j)=N/s_j proves (1) when w<=0.

For the other half use the ACTUAL Chevalley maps

    J_L |u> = q^(-(L+1)u) |L-u>,
    S=P(J_d tensor J_d).

For the balanced source generators, J_L exchanges F and Ecal and
exchanges K and K^-1. The flip in S consequently gives
S Delta F=Delta Ecal S and S Delta Ecal=Delta F S. In the original
generic Clebsch image, uniqueness of its highest vector gives

    S W_a=kappa W_a J_(2a).

This is a rational generic identity, then specialized; it does not
assume semisimplicity at the root. Squaring it yields

    kappa^2=q^(-2Nd+2a(2a+1)).                     (3)

The original W column and its Chevalley image have nonzero finite
highest endpoints at the root, so the identity specializes there;
alternatively (3) already makes any scalar singularity removable.
All coefficients of the two J maps and kappa have modulus one
at the root. The low endpoint (0,t) maps to the HIGH endpoint
(d-t,d), exactly the endpoint used in the compiler. Thus its
modulus is unchanged under r->2a-r. This proves (1) for both halves
and both level parities.

The original white map is

    pi_a(r;u,v)=G_(a,r)^-1 conjugate(W_a(v,u;r)),
    G_(a,r)=s_(2a)/(s_r s_(2a-r))>0.

The normalized physical column has unit-modulus final endpoint,
so its first-endpoint scalar satisfies

    |c_pi|=|c_W|/G_(a,r).                           (4)

Both physical vertices have the same t and a. Their positive
Fourier polynomials are normalized by c_(t,a) from the compiler,
with |c_(t,a)|=1/s_a. Finally retain the actual complete-circle
weight

    h0_a=k_a N s_(2a)/s_a^2,
    k_a=1 if 2a=d, and k_a=2 otherwise.

Equations (1)--(4) give the exact positive scalar

    B_N(a,w)
      :=h0_a |c_W c_pi c_(t,a)^2|
       =k_a N s_(a+|w|)
                    /(s_a^2 s_|w|^2 s_(a-|w|)).     (5)

There is no omitted exponential row, face or ordinary-channel
metric in (5). The original physical cups have modulus N and
ordinary caps modulus 1/N. Their numbers agree in the closed
Morse diagram, so those moduli cancel globally. The original
marked cap is handled by the exact charged-cap ratio in the
compiler, rather than included in this cancellation.

## 2. The shared state space and all Fourier congruences

Let R be the number of original matching circles and C the number
of restored physical cycles. Collapse those cycles to the graph
Gamma, orienting each matching edge from its pi cycle to its W
cycle. A shared state consists of

    a_i in {0,...,floor(d/2)},
    w_i in {-a_i,...,a_i},          div_Gamma w=0,
    k_v in {0,...,a_i}             at EACH of the two ends v of i.

Set t_i=d-|w_i|. On a fixed physical cycle, propagate its actual
indices as literal affine functions of one starting coordinate x.
Let epsilon_v in {+1,-1} be the slope of the recorded FIRST
physical coordinate at vertex v, and epsilon_b the same slope
at a physical cup or restored cap b. The total character is

    m_c(a,k)=sum_(v on c) epsilon_v(d-2a_i+2k_v)
                              +d sum_(b on c) epsilon_b.          (6)

The actual bipartite cycle proof shows m_c is always even. All
affine offsets, high-degree shifts and the terms -t_i k_v are
retained in the remaining coefficient phase. They do not affect
(6). Put b_c=0 except b_(c_*)=1 on the marked cycle, whose
variable is the SECOND marked coordinate. Retain EVERY equation

    m_c(a,k)=2b_c modulo 2N.                        (7)

Write S_N for this finite state space: the capacities, exact
Kirchhoff equations, and all congruences (7), jointly. There are
at most N^(4R) states: N choices for each a_i and each w_i, and
N choices for each of the 2R coefficient indices. Constraints
can only decrease this bound. No variables on separate vertices
or cycles have been optimized independently.

## 3. Exact phase-bearing sum and one Cauchy inequality

For a state in S_N, let Theta_N(a,w,k) be the phase left by the
EXACT compiler after removing the positive factors (5) and the
positive coefficients p_(t_i,a_i,k_v). Its modulus is one. This
definition is explicit: multiply the original endpoint phases,
c_(t_i,a_i), cup/cap monomials, recorded half-twist omega phases,
and the affine-offset terms in compiler equation (7), then divide
by their moduli. The global q^(-d^2) marked phase is written
separately below. All these factors are nonzero; no arbitrary
phase or framing normalization is introduced.

The original complete-circle source is therefore EXACTLY

    A_(D,N)=q^(-d^2) N^(C-1)
       sum_(S_N) Theta_N(a,w,k)
          product_i B_N(a_i,w_i)
          product_(v incident to i) p_(t_i,a_i,k_v). (8)

Define the fully positive shared coefficient partition

    Z_F(N)=sum_(S_N)
          product_i B_N(a_i,w_i)^2
          product_(v incident to i) p_(t_i,a_i,k_v)^2.             (9)

ONE finite Cauchy inequality applied to the full sum (8) gives

    |A_(D,N)|^2 <= N^(4R+2C-2) Z_F(N).              (10)

The sharper factor |S_N| N^(2C-2) is equally valid. If S_N is
empty, both sides of (8) vanish and (10) is immediate. The
half-twist phases disappear only in (9),(10); they remain in the
exact source (8). In particular, (9) retains the marked charge,
all other cycle charges and the same matching magnetic label at
both ends of every edge. Dropping these restrictions would give
a different, generally weaker comparison problem.

## 4. Its local variational interface and its limit

For a fixed diagram, the loss in (10) is polynomial in N. The
local positive coefficients in (9) are precisely those in
[the proved coefficient variational theorem](actual_q_hahn_fourier_coefficient_variational.md),
with complete-channel parameters tau=t_i/N and xi=a_i/N.
Its interior coefficient action may therefore be used in this
JOINT constrained partition, with the original scalar (5).
Its theorem does not supply uniform boundary asymptotics where
these parameters or k_v/N approach the boundary.

For clarity, the exact finite cycle charge also controls the
limiting local momentum. Set lambda_v=k_v/N, xi_i=a_i/N and

    Y_v^*=exp[2pi i(lambda_v+1/2-xi_i)].

This is the selected radial coefficient saddle momentum on the
interior parameter domain of that theorem. Since
q^(d-2a_i+2k_v)=q^-1 Y_v^*, equations (6),(7) give EXACTLY

    product_(v on c) (Y_v^*)^epsilon_v
           (-1)^(sum_(b on c) epsilon_b)
       =Q^(E_c/2+b_c),
    E_c=sum_(v on c)epsilon_v+sum_(b on c)epsilon_b in 2Z.        (11)

The finite pivotal correction and original marked charge have
not been dropped. Equation (11) is a phase constraint supplied
by the Fourier extraction; it is not yet a proof of all marked
complex gluing equations. In particular, the positive partition
can lose cancellation between its states, and a constrained
maximum alone need not supply a contributing original cycle.
Neither equality in exponential rate in (10) nor identification
of the constrained maximum with hyperbolic volume is asserted.

Audit: [original endpoint norms and shared coefficient partition](../experiments/audit_actual_matching_graph_positive_fourier_partition.py).

The exact constrained coefficient partition does not establish noncancellation or a volume statement.