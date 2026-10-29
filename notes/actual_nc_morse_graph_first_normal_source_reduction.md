# An exact first-normal reduction for arbitrary original NC Morse graphs

29 October 2026. Every fixed graph in the actual noncrossing Morse class
has a source-exact reduction to an ordinary magnetic spin network with
ONE retained generic-q normal. This includes a distinct boundary term
when the sole marked white vertex has an unsaturated root source.
The original unrestricted mark remains on the physical V_N strand.
No Euclidean norm, semisimple root quotient, scalar Frobenius vertex,
or vanishing source normal is substituted for it.

This is an exact finite source theorem at arbitrary fixed width. It
does not establish a norm bound, noncancellation, a stationary cycle,
or a geometric volume for a general graph.

## 1. The graph is an original ordered Morse diagram

Use precisely the class in section5 of the
[literal trivalent vertex theorem](actual_trivalent_complete_circle_vertex_kernel.md).
There are b black and b white vertices and E=3b ordered edge slots.
Each color class partitions {0,...,E-1} into sorted triples; each
partition is noncrossing. At a triple (a,b,c) the actual matching is

    (2a+1,2c+2), (2a+2,2b+1), (2b+2,2c+1).

Removing innermost adjacent arcs gives an original nested cup/cap
Morse word. There is no free incidence permutation or unrecorded
braid. Choose a white vertex v* whose outer cap is EXPOSED: it is
not contained in any other top cap. Mark that arc; all other caps
are ordinary. Its row is the original UNRESTRICTED m. Equivalently,
all ordinary top caps can be removed by innermost removals without
passing over the marked arc. Every noncrossing partition has such
a top-level block, so this leaves the arbitrary graph class intact
while restricting its bare pointing.

Replacing a NESTED cap by the same bare m is not covered. A genuine
cut at that location requires pivotal transport through the enclosing
caps, which is not a local unmodified m replacement.

Fix labels 0<=j_e<=M=floor((N-1)/2) and signed integer exponents e_e.
The edge coupon is the actual full-normal sector

    R^(e_e)L_(j_e)=omega_(j_e)^(e_e) h0_(j_e) W_(j_e) pi_(j_e),
    pi_j=G_j^(-1)W_j^dagger P,
    G_(j,r)=s_(2j)/(s_r s_(2j-r)),
    h0_j=k_j N s_(2j)/s_j^2,
    k_j=2 if 2j<d, k_j=1 if 2j=d,
    omega_j=kappa(-1)^j q^[j(j+1)].                 (1)

Here d=N-1, q=exp(pi i/N), Q=q^2, kappa=q^(d^2/2),
F_u=(Q;Q)_u, s_u=|F_u|. The paired coupon is nilpotent;
pi_j W_j=0 there. Formula(1) includes its first normal BEFORE
passing to an ordinary object. All external original line/framing
factors remain outside the raw scalar Z_Gamma defined here.

## 2. Explicit local regular lifts and canonical ordinary tensors

Set zeta=q exp(t). Every prime below means d/dt at t=0. Let V_N(t)
be the generic highest-weight d module in the same balanced basis.
Its physical cup has highest coefficient N zeta^(-d^2):

    pV_(u,d-u)(t)=N zeta^(-d^2)(-1)^u
       zeta^[u(d-u-1)] F_u(t)F_(d-u)(t)/F_d(t),
    ellV(t)=pV(t)^(-1).                             (2)

It specializes exactly to p_(u,v)=N x^(-v)delta_(u+v,d) and
ell_(u,v)=x^u/N delta_(u+v,d). On the ordinary object Q_j of
highest weight 2j choose pQ_j with highest coefficient ONE, using
the same formula with d replaced by 2j and the leading scale omitted.

The physical Clebsch map W_j(t) starts at degree l=d-j with

    h_u(t)=(-1)^u zeta^(-du)
       Q^[u(l-1)-u(u-1)/2](Q^(j+1);Q)_u F_(d-u)/F_d,
    W_(j,r)(t)=F_pair(t)^r h(t)/F_r(t), 0<=r<=2j.   (3)

All displayed factorial denominators have index <N and are units.
The direct highest recurrence and E,F commutator prove covariance;
the last F endpoint follows because E_pair is injective above degree d.
These facts were proved explicitly in the
[all-channel marked calculation](actual_trivalent_all_channel_marked_contraction.md),
section3. No generic decomposition theorem is required.

Keep the ROOT constants h0_j, omega_j and

    gamma_j=q^(2-j^2)/N^2

fixed as t varies. Define the chosen regular lift

    pi_j(t)=gamma_j^(-1)D_t(W_j(t)),
    D_t(W_j)=pQ_j(t)^T W_j(t)^T
                        [ellV(t)^T tensor ellV(t)^T]P. (4)

At t=0 this is precisely the actual pi_j in(1). Direct cup matrices
and K covariance give D_t^2(W_j)=W_j. This is a lift of the fixed-root
coupon, not an assertion about the full moving-q germ of the original
circle, pivot, or framed R. Constant omega_j^(e_e) in the lift is
legitimate because(1) is an exact all-normal root equality.

At any triangle triple (a,b,c), let Theta_abc(t) be the genuine ordinary
invariant in Q_a(t) tensor Q_b(t) tensor Q_c(t), normalized by

    Theta_abc(2a,b+c-a,0)=1.                         (5)

It is an explicit regular finite tensor. Put J=a+b+c, r=b+c-a,
r1=a+b-c. Its third-color-zero slice is

    Theta_abc(2a-k,r+k,0)
       =(-1)^k zeta^[k(2a+1-k)]
                         F_(r+k)F_(2a-k)/(F_r F_(2a)),
    0<=k<=r1.                                      (6)

All other slices are forced by

    v_u=-K_c(u-1)/E_c(u-1,u) E_ab v_(u-1).          (7)

Every denominator in(6),(7) is a unit at the root. The corresponding
integer-H invariant space is one-dimensional. Outside the ordinary
triangle range it is zero, by the rectangular lowest F equation.

Define the LOCAL source coefficient by the finite original index sum

    s_abc(t)=<2a,b+c-a,0|
        [pi_a(t) tensor pi_b(t) tensor pi_c(t)]J_source(t),
    J_source(t)=pV_16(t)pV_23(t)pV_45(t).            (8)

Then the whole black tensor is U_abc(t)=s_abc(t)Theta_abc(t).
At the root its value is explicitly

    s_abc(0)=N^3 A_N(a,b,c)/G_(b,b+c-a),             (9)

where the [proved positive source formula](actual_trivalent_all_channel_positive_scalar_and_regular_cubes.md)
includes its original phase. Thus s_abc(0)!=0 exactly when J>=d
within the triangle range; it is zero for J<d. The derivative in(8)
is a retained local source current, not determined merely by(9).

## 3. The exact ordinary spin network and all root constants

Keep each vertex's actual increasing edge order. At a black vertex
v with incident labels (a,b,c), place Theta_abc(t), and put

    s_v(t)=s_abc(t).

At a white vertex with the SAME displayed incident order place
D_t(Theta_cba(t)), and put s_v(t)=s_cba(t). The dual reverses the
abstract object order, so its resulting row is again indexed in
(a,b,c) order. No same-order adjoint may be substituted.

Contract equal magnetic edge indices, with their dimensions 2j_e+1,
to obtain the explicitly specified finite spin network Xi_Gamma(t).
It contains the genuine ordinary 3j tensors and cups; it is not
defined by the original unknown closed scalar. All its factors and
their first derivatives are given by(2),(6),(7).

Define the EXACT fixed root factor

    C_Gamma=product_edges [h0_j gamma_j omega_j^(e_e)],
    S_Gamma(t)=product_vertices s_v(t).             (10)

The h0_j and G_j can have factorial exponential growth. They have
not been declared polynomial or suppressed. A single gamma_j occurs
per edge, because that edge meets exactly one white vertex.

Let F_Gamma(t) be the ordinary closed ORIGINAL physical graph with
the regular lifted coupons (1),(4), and with an ordinary cap also at
the eventually marked arc. Genuine local duality gives

    Lambda_abc(t)=gamma_a gamma_b gamma_c D_t(U_cba(t)).

Substitution at every vertex is therefore the all-width index identity

    F_Gamma(t)=C_Gamma S_Gamma(t) Xi_Gamma(t).        (11)

This does not require a factorization of Xi_Gamma into vertex norms
or source-independent inverse frames. The magnetic contraction is
retained in full, on the actual graph wiring.

## 4. The original marked scalar is exactly the first normal

Remove all other caps in their actual innermost Morse order. Exposure
ensures that this leaves the two marked legs as a genuine generic
invariant physical column. Bend with the SAME pV(t). Every remaining
map is then a generic Hopf map; hence the resulting open
map on V_N(t) is a scalar z_Gamma(t)I. To prove scalarity directly,
its generic K eigenvalues are distinct and all its interior F arrows
are nonzero, so commuting with K,F forces a scalar matrix. Every
entry is regular at t=0, by(2)--(4); thus z_Gamma is holomorphic.

The physical closing trace, including the cup's sign, is exactly

    ellV pV^T=(-1)^d K_V,
    F_Gamma(t)=D_N(t) z_Gamma(t),
    D_N(t)=(-1)^d[N]_(q exp(t)),
    D_N(0)=0,
    nu_N:=D_N'(0)=2N(-1)^N/(q-q^(-1))!=0.           (12)

The original unrestricted root marked row has m pV(0)=1. Thus the
original marked source is z_Gamma(0), with no extra component factor:

    Z_Gamma=C_Gamma/nu_N
             *[S_Gamma'(0)Xi_Gamma(0)
                                  +S_Gamma(0)Xi_Gamma'(0)]. (13)

Only the chosen physical trace quotient is differentiated. The mark
has never been transported through a paired image or replaced by an
ordinary cap. In particular (13) retains the current that would be
lost by first specializing the generic ordinary graph to its root zero.
The factor 1/nu_N has magnitude sin(pi/N)/N; this alone gives no
bound for the differentiated tensors or their source coefficients.

The answer is independent of the chosen regular Hopf lift. Two such
lifts with the same original root coupons give the same root open
map, hence the same z_Gamma(0). Their ordinary closures differ by
D_N(t) times a holomorphic scalar vanishing at t=0, so their first
normals agree. Individual local source and spin-network derivatives
may change with the lift; their complete combination in(13) does not.

### 4a. Why an inner bare mark is not a movable pivotal cut

The exposure hypothesis is necessary for the bare row used here. On
the ordered cube at N=3, give all twelve edges label j=1 and zero
twist. Reduce q to 375 in the prime field of order 1009; this has
exact order six and every denominator is a unit. The actual physical
contraction with bare m on the exposed white block (0,10,11) is 155.
Putting the same bare m on the NESTED block (1,8,9), leaving all other
coupons unchanged, gives 620. The ordinary trace and its first normal
are unchanged, so these two bare insertions cannot both be its
normalized pivotal cut. Their difference is an exact cyclotomic
counterexample, not a floating-point discrepancy.

The original proof's phrase allowing an arbitrary white vertex was
therefore too broad. It has been corrected to the exposed hypothesis
in section1, and the audit retains this negative test. Moving a
genuine cut through an enclosing cap requires its actual pivotal
transport. It cannot justify deleting the marked-white current in
(15) while leaving that enclosing ordinary cap row unchanged.

## 5. Exact source support and the marked-white boundary term

The following alternatives are valid for every graph above.

* A nontriangle triple at ANY vertex makes Z_Gamma=0. If black, its
  generic invariant column is zero. If white, genuine ordered duality
  makes its generic ordinary row zero. In either case F_Gamma is
  identically zero. By generic scalarity and D_N(t)!=0 off its isolated
  root, the physical open scalar is identically zero and its marked
  specialization is zero as well. This includes a nontriangle MARKED
  white vertex; no local invariance of m is presumed.

* A triangle with J<d at a black or an UNMARKED white vertex makes
  Z_Gamma=0 directly at the root: respectively the actual black column
  or the ordinary cap row is zero before estimating or summing. The
  marked white row is not included in this local deletion rule.

* If every vertex has J>=d, all s_v(0) are nonzero, and (11),(12)
  force Xi_Gamma(0)=0. The complete formula is then

      Z_Gamma=C_Gamma [product_v s_v(0)]
                                      Xi_Gamma'(0)/nu_N.    (14)

* Suppose every black and unmarked white vertex has J>=d but the
  marked white triangle has J<d. There is exactly one zero source
  factor, s_v*(0)=0. Its full contribution is

      Z_Gamma=C_Gamma [product_(v!=v*) s_v(0)]
                               s_v*'(0) Xi_Gamma(0)/nu_N.   (15)

  It is not legitimate to set this term to zero merely because its
  ordinary root coefficient vanishes. The derivative may vanish, but
  that requires its actual finite local source current(8).

If at least two s_v(0) vanish, holomorphy of every factor in(11)
gives a double zero and hence Z_Gamma=0. If there is a sole black or
unmarked-white zero, (13) and the direct deletion above give the exact
compatibility identity s_v'(0)Xi_Gamma(0)=0. This is a consequence of
the whole original source, not a license to discard an arbitrary normal.

## 6. The retained normal is explicitly local and finite

These formulas can be evaluated using first jets only. For example,
put

    L_u=-sum_(k=1)^u 2k Q^k/(1-Q^k), L_0=0.

The logarithmic derivative of the nonzero highest coefficient in(3) is

    h_u'/h_u=u(2l-d-u-1)+L_(j+u)-L_j+L_(d-u)-L_d.  (16)

All terms are physical units. With f_r=1-Q^r, its actual descendants
and derivatives satisfy

    W_(r+1)=F_pair W_r/f_(r+1),
    W_(r+1)'=(F_pair' W_r+F_pair W_r')/f_(r+1)
                  +2(r+1)Q^(r+1)W_(r+1)/f_(r+1).  (17)

For a canonical cup of highest weight L and scale p0(t),

    p_(u,L-u)'/p_(u,L-u)
      =p0'/p0+u(L-u-1)+L_u+L_(L-u)-L_L,
    ell'=-ell p' ell.                              (18)

Here p0'/p0=-d^2 on V_N and zero on Q_j. Differentiating (4) gives
pi_j'; differentiating the four factors in(8) gives s_abc' by a finite
sum with one differentiated factor. Equations(6),(7),(18) similarly
give Xi_Gamma' by a sum of ordinary magnetic contractions with ONE
first-jet tensor or cup. This construction retains the full original
source normal at any fixed width, without inverses of paired frames.

The [exact first-jet audit](../experiments/audit_actual_nc_morse_graph_first_normal_source_reduction.py)
checks these local jet identities and original marked graph contractions.
Its sole-unsaturated-marked cube fixture has a nonzero LOCAL source
normal but zero exterior spin value; it therefore asserts no nonzero
boundary contribution merely from that local current. Both factors
in(15) are retained.
General norm/nonzero/volume control for the ordinary network normal
in(14), and for the marked-white current in(15), remains open.

Internal review history: the initial review and positive tests missed
the exposed-versus-nested bare-mark distinction. The additional test
in section4a found it. The pointing hypothesis and the dipole fixture
have been corrected explicitly; all local source/jet formulas remain
unchanged. The corrected audit passes five local jet families, sixteen
exposed original source cases and the inner-mark rejection. These are
internal checks, not an external peer review or a geometric
identification of the network.
