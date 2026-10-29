# The actual four-line Fermat crossing and its unavoidable exponential action

28 October 2026. The compactified cap sources form an explicit full
head frame with an exact inverse and the ORIGINAL basis as its
normalized cap value. This gives a four-Fermat-line formula for the
actual crossing. The full frame and EACH selected corner have a
sharp positive exponential norm on fixed-log root charts, although
the separate quad-line coefficients are polynomial. That action
must be retained in a geometric comparison.

The cyclic conjugation and existence of dilogarithmic gauge action
are already established in the
[actual Hilbert-90 gauge](actual_hilbert90_gauge_dilogarithm_action.md)
and [controlled cyclic source](controlled_cyclic_euler_source.md).
They are not counted as new here. The new content is the full dual
frame, its cap-compatible four-leg actual kernel, the selected sharp
norm scale, and an all-N support obstruction for independent frames.
No positive geometric crossing identity or volume limit is claimed.

## 1. The full coherent frame has an explicit dual

Use N>=2, d=N-1, q,Q,Z,S,P,L from
[the cap-residue theorem](cap_wall_fermat_quad_residue_transport.md).
Thus u^N+v^N=w^N, uvw!=0, and

    P_n=v^n/product_(r=1)^n(w-uQ^r),
    L_n=v^-n product_(r=0)^(n-1)(w-uQ^r).

The N-column coherent frame is

    M_(n,j)=P_n(uQ^j,v,w), 0<=n,j<N.                     (1)

It has the EXACT inverse

    (M^-1)_(j,n)
      =v^N Q^n L_n(uQ^j,v,w)
                  /[N(uQ^j)^(N-1)(w-uQ^j)].             (2)

Indeed the columns are eigenvectors of A=Z^-1(wI-vS), with
distinct eigenvalues uQ^j. The corresponding left eigenvectors
are L(uQ^j,v,w)Z. Different eigenvalues are orthogonal, while
their diagonal pairing is

    L(uQ^j,v,w)Z P(uQ^j,v,w)
       =N(uQ^j)^(N-1)(w-uQ^j)/v^N.                     (3)

To compute it, sum (w-uQ^j)Q^n/(w-uQ^(j+n)) and use the
logarithmic derivative of w^N-u^N. Every factor in (3) is a
unit on the chart. This proves (2), including its output clock.

## 2. A cap-normalized circulant, with exact inverse

Set w=1 and take u=(1-v^N)^(1/N), u(0)=1. Order the columns
by k=-j modulo N. Multiply column k>=1 by
v^(N-k)/F_(N-k), and leave column k=0 unchanged. Call the
result K(v). The all-cusp residue formulas prove

    K(0)=I.                                              (4)

Extend p_n=P_n(u,v,1) periodically. Put

    H_(n,k)=p_(n-k), r_0=1,
    r_k=(uQ;Q)_(N-k)/F_(N-k), 1<=k<N.

Then exactly

    K=H diag(r_k).                                      (5)

For P_n(uQ^-k)=p_(n-k)/p_(-k) and
p_(-k)=v^(N-k)/(uQ;Q)_(N-k), proving (5). All r_k tend
to one, with r_k-1=O(v^N). Thus the FULL head frame, not only
one vector, extends invertibly through the actual cap wall.

The circulant has an especially simple inverse. For general
homogeneous u,v,w, define

    kappa=v^N/[N u^(N-1)(w-u)],
    h_n=kappa (v/Q)^n/product_(r=1)^n(w-uQ^-r).

Then

    H^-1_(n,k)=h_(n-k).                                 (6)

For a proof, (2) at j=0 gives the zeroth row of the inverse
circulant; finite-product reflection gives exactly h_n. Thus
(6) is a finite cyclic beta-convolution identity with its WHOLE
rational scalar. At the cap branch kappa→1 and H→I. The
apparent 0/0 has this prescribed regular extension.

The associated known cyclic Weyl shear is exactly

    H^-1 S H=S,
    H^-1 Z H=u^-1(wI-vS)Z.                              (7)

It follows from u H(QS)=(w-vS)H(S) and ZH(S)=H(QS)Z.
The new clock's Nth power is one precisely because
w^N-v^N=u^N. Its compensating root u must not be dropped.

## 3. The original crossing in four Fermat lines

Let R be either ORIGINAL mixed crossing, with its original
Cartan scalar inside R or in the specified external line.
Choose Fermat triples f_i on its two incoming and two outgoing
heads. Define R_F=(M_3^-1 tensor M_4^-1)R(M_1 tensor M_2).
Equations (1)--(3) give its explicit four-line kernel:

    (R_F)_(j3,j4;j1,j2)
      =v3^N v4^N /
        [N^2 (u3Q^j3)^(N-1)(w3-u3Q^j3)
             (u4Q^j4)^(N-1)(w4-u4Q^j4)]
       *sum_(n1,n2,n3,n4) Q^(n3+n4)
          L_n3(u3Q^j3,v3,w3)L_n4(u4Q^j4,v4,w4)
          R_(n3,n4;n1,n2)
          P_n1(u1Q^j1,v1,w1)P_n2(u2Q^j2,v2,w2).          (8)

The original crossing support reduces this to three independent
finite indices. There is no asymptotic substitution or new cap.
One can instead use the cap-normalized K frames, or H with the
explicit r factors in (5). The four external kernels are then
p and the reflected cyclic sources h in (6). At all four cap
walls this identity specializes back to the original crossing
MATRIX by (4). In a whole plat every interior inverse frame
cancels; actual rows, columns, coupons and scalar lines all move.

There are two distinct applications. For the original PHYSICAL
head R in (8), cups and caps remain their original balanced
arrays, transported by these frames; they are not replaced by
corner vectors. The literal cup is C_x|d,0>, so the physical
transformed cup keeps (K_1^-1 tensor K_2^-1)C_x|d,0>.
Alternatively first use the proved pair-fused corner presentation,
then apply these head frames to its RELATIVE heads. Its within-pair
crossing has four such lines, while its between-pair kernel acts
on four relative heads and has eight external lines. The formulas
apply to both presentations, but they must not be conflated.

The transported Hopf currents are also explicit. On a balanced
head of color x, K_head=xZ^-1 and F_head=S(1-QZ); their H
images follow by (7). At completeness the original scaled E is
the exact cyclic expression S^-1(Z^-1-1). At other colors its
original bottom projector must also move. No bare current is
left in the old relative frame.

Equation (8) is an exact four-line ACTUAL identity. Arbitrary
independent f_i are not thereby geometric shared-face data.

## 4. Sharp exponential norms include every selected corner

Take canonical unit roots and compatible fixed logarithms

    u=exp(a/N), v=exp(b/N), w=1,
    exp(a)+exp(b)=1.

Assume the central values stay away from zero and the logarithms
in a fixed compact set. Define

    gamma_*=-integral_0^(1/6)log(2sin(pi t))dt >0.

Then

    lim (1/N)log||H||_2=lim (1/N)log||H^-1||_2=gamma_*,
    lim (1/N)log cond_2(H)=2gamma_*.                     (9)

The same holds for the cap-normalized frame K. For EVERY corner
j=j(N), uniformly in that choice,

    lim (1/N)log||K e_j||_2=gamma_*,
    lim (1/N)log||e_j^t K^-1||_2=gamma_*.                (10)

In the existing figure-eight normalization,
gamma_*=Vol(4_1)/(4pi); the integral definition alone suffices.
These are the standard Euclidean norms of the explicitly chosen
head basis. When used on the actual relative corner presentation,
they concern its original corner sources. A further nonunitary
physical fusion change needs its own comparison and may not be
ignored in a whole physical norm estimate.

Here is a complete proof. The elementary marked root-product
comparison gives, uniformly in n,k,

    N^-C/|F_n| <= |p_n|, |h_n| <= N^C/|F_n|,
    N^-C <= |r_k| <= N^C.                               (11)

For each product the relative logarithmic errors are
O(1/min(j,N-j)); their sum is O(log N). The finitely many
endpoint ratios have nonzero limits, because the marked central
value of u differs from one. For h use (6), the identical
inverse-Q factorial magnitude, and the nonzero bounded kappa.
The r assertion is the same comparison in (5).

The elementary uniform factorial estimate proved in
[the full-Euler estimate](full_euler_atom_dilog_and_endpoint_regions.md)
is

    log|F_n|=N J(n/N)+O(log N),
    J(s)=integral_0^s log(2sin(pi t))dt.

Its minimum is J(1/6)=-gamma_* and its maximum is
J(5/6)=gamma_*. Consequently max_n 1/|F_n| has rate gamma_*.
The norm of an N by N matrix is between its maximum entry
magnitude and N times that magnitude. Applied to H and H^-1,
this proves (9). Every circulant column is a permutation of p,
and every inverse row a permutation of h, so their Euclidean
norms have the same rate. The polynomial r factors in (5)
prove both claims for K and (10).

In particular e_j^t K^-1 K e_j is EXACTLY one, while the
product of its selected row and column norms has rate 2gamma_*.
This is selected source cancellation, not merely poor conditioning
of an unrelated auxiliary module. The polynomial quad-LINE
coefficients do not make the FULL frame subexponential. This
dilogarithmic action has to enter the geometric phase calculation.
There is no contradiction with the cap theorem's fixed-log line
bounds: a full raw frame includes uQ^j with bulk j, whose marked
logarithms need not stay bounded. Even for fixed-log selected
lines, a polynomial transition COEFFICIENT compares two vectors
which can both have exponential norm.

For comparison, the UNNORMALIZED coherent frame M in (1) is
even worse:

    lim (1/N)log||M||_2
      =lim (1/N)log||M^-1||_2=2gamma_*,
    lim (1/N)log cond_2(M)=4gamma_*.

Its largest entry is exactly max|p_n|/min|p_n|, since
M_(n,j)=p_(n+j)/p_j. In (2), the inverse entries equal
p_j/p_(n+j) times a uniformly polynomial factor, using
L_n P_n=(w-u)/(w-uQ^n). The factorial profile proves the
displayed limits. The cap column factors in (5) therefore
remove part, but not all, of the exponential condition number.
Both normalizations must remain explicit in a four-face comparison.

## 5. What tetrahedral variable the principal shear needs

For fixed-log roots u,v→1, let the input clock be A, output
clock U, and let p be their common wavefunction momentum. S
has symbol p^-1. Equation (7) has the principal graph

    t=U/A=1-p^-1.                                      (12)

Its generating action is Li_2(t)-Li_2(1), with the branches
inherited from the cyclic product. Differentiation gives
p_out=p_in=(1-t)^-1. If p is in the upper half-plane, t is
its positive quad rotation. The variable needing a geometric
mark is the BULK ratio U/A, not the central Fermat value u^N.

The actual momentum has a holonomy meaning. In the existing
Gauss coordinates

    K=x/U, e=(1-x^2/U)p/x, f=(1-U)/p,
    G=[[K,e],[Kf,fe+K^-1]],

direct multiplication gives

    G(1,p^-1)^t=x^-1(1,p^-1)^t.                         (13)

Thus p^-1 is the selected meridian eigenflag in that frame.
The other three reference flags must still be identified with
the actual shared developing flags to make (12) a geometric
tetrahedron. A single eigenflag/source ratio does not establish
that four-face comparison. The action's existence is already
known; its exact four-leg source and scale (9)--(10) are the
new comparison information here.

## 6. Independent line frames cannot be one basic tetrahedron

There is an all-N support obstruction to a naive reading of (8).
Take four INDEPENDENT cap parameters z_i with
u_i=(1-z_i^N)^(1/N), v_i=z_i, w_i=1 and H frames. Every
entry of (H_3^-1 tensor H_4^-1)R(H_1 tensor H_2) is a
NONZERO algebraic germ.

For input (a,b) and output (c,e), let r=-a mod N and s=-b
mod N in the head range. The coefficient of
z_1^r z_2^s z_3^c z_4^e is uniquely the original route with
both intermediate R indices (0,0). It equals

    R_(00,00) (-1)^(c+e)Q^[c(c-1)/2+e(e-1)/2]
                           /[F_r F_s F_c F_e],          (14)

which is nonzero with the original Cartan line retained. Each
degree is less than N, so no central correction to u_i enters.
The four cyclic shifts fix both intermediate indices uniquely,
which proves (14) with no possible cancellation.

The basic matrix tetrahedron kernel instead has strict support
delta i+j=l modulo N, hence only N^3 potential nonzero entries.
Independent diagonal face gauges and Weyl index permutations
preserve that support count. Therefore this generic four-line
actual kernel cannot be a SINGLE such tetrahedron under those
changes. Coupled shared-face parameters, additional shears, or
several tetrahedra are necessary.

This does not exclude a genuine four-face geometric identity.
It states precisely what (8) alone lacks. Proving actual shared
developing-flag relations, with their full source and phase,
remains the next comparison; no broad volume claim follows here.

## 7. Reproducible checks

The [audit](../experiments/audit_actual_four_line_fermat_crossing.py)
and [saved output](../experiments/actual_four_line_fermat_crossing_results.json)
pass 56 full coherent/circulant frames at N=2,...,8, including
the dual inverse, exact nonlinear clock transport and all column
normalizations. They check 56 mixed positive/negative ORIGINAL
crossing entries by an independent sum using the literal E and
Cartan coefficients, with the full four-line kernel retained.
The 8,771 support witness coefficients are nonzero at every
matrix position in these levels. Five norm-scale diagnostics
through N=256 approach the limits in (9)--(10); the limits are
proved by the uniform product estimates, not those samples.
Independent proof review and rerun checked the exact dual,
reflected inverse, all conditioning rates, actual kernel order,
full-support witness, and physical-versus-relative source scope.
