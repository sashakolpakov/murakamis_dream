# External circle reflection and its primitive cusp normalization

30 October 2026. The original color
N-h circle splits exactly into a cosine-weighted COMPLETE circle and
a literal small-color circle. This gives a precise interface to the
positive face coefficient without discarding any root Casimir normal.
The rectangle calculation independently identifies the primitive cusp
shape associated with the folded Gaussian. Neither calculation proves
the missing general complex external-color packet or its global gap.
The exact cosine core was already identified in the
[entire core-color compiler](actual_augmented_plat_entire_core_color_packet.md).
The new interface here is its positive face-coefficient realization,
its retained small-color and normal terms, and the independent primitive
rectangle normalization.

## 1. The actual full-matrix polynomial identity

Put N>=2, d=N-1, q=exp(pi i/N). To distinguish the two Chebyshev
normalizations, write

    C_m(z)=2T_m(z/2), P_m(z)=U_m(z/2),
    C_0=2, C_1=z; P_0=1, P_1=z.

The [literal mixed-circle theorem](actual_crossing_circle_source_and_filling.md)
proves, on the two original complete physical targets,

    L_n=(-1)^(n-1)P_(n-1)(Omega), 1<=n<=N,
    C_N(Omega)=-2I.                                    (1)

The auxiliary module has dimension n and its actual pivot K_n^(1-N).
There is no additional 1/n trace factor. Equation (1) includes every
double-node Jordan coefficient and the odd simple Steinberg node.
Define L_0=0.

For 1<=h<N the elementary sine subtraction formula proves the
POLYNOMIAL identity

    P_(N-h-1)(z)=T_h(z/2)P_(N-1)(z)
                                  -T_N(z/2)P_(h-1)(z).

Substitution of (1), with its signs, gives

    L_(N-h)=(-1)^h T_h(Omega/2)L_N+(-1)^N L_h.          (2)

The same equation holds at h=0 using T_0=1 and L_0=0. The value
T_N(Omega/2)=-I is supplied by the actual full pair relation, not
by checking only its repeated eigenvalues.

For the INTERNAL complete-circle label 0<=a<=floor(d/2), put

    s_a=d-2a, c_a=q^(2a+1)+q^(-2a-1),
    L_(N,a)=h0_a W_a pi_a.

These are the actual complete sectors, including the nilpotent ones.
At a double node L_N(c_a)=0, so multiplying by T_h retains exactly
T_h(c_a/2)L_N'(c_a); its apparent T_h' term is multiplied by zero.
At the odd simple node the ordinary value is retained. Therefore

    (-1)^h T_h(Omega/2)L_N
         =sum_a cos(pi h s_a/N) L_(N,a).               (3)

Here (-1)^h cos(pi h(2a+1)/N)=cos(pi h s_a/N) follows from
2a+1=N-s_a and the INTEGER external deficit h. In particular no
auxiliary color is being identified with an internal channel.

## 2. An exact subset expansion of the original mixed source

At R specified original circle ports substitute (2), tensor with
all spectators, and keep each R_i^epsilon_i, physical cup/cap,
unrestricted original mark and exterior framing line. Multilinearity
gives a sum over subsets J of the ports. At i in J retain the literal
small-color operator L_(h_i); at i outside J retain the weighted
complete sum (3). The subset scalar is (-1)^(N|J|). A port with
h_i=0 cannot occur in a nonzero such subset term.

The term J=empty is EXACTLY

    F_N(h)=chi_(D,N) N^R sum_a
       product_i[k_ai beta_ai^2 omega_ai^epsilon_i
                           cos(pi h_i s_ai/N)] C_(N,a), (4)

where C_(N,a) is the [original positive face coefficient](actual_original_marked_face_coefficient.md),
beta_a=S_(2a)/S_a^2, k_a=1 at s_a=0 and2 otherwise, and
omega_a=q^(d^2/2)(-1)^a q^[a(a+1)]. The physical-source notation
and finite scalar of that theorem are unchanged. Equation (4) applies
to its connected original plat scope, independently of the additional
geometric certificate used for asymptotics.

Consequently F_N(Nx) is an entire, separately even finite cosine
polynomial in the EXTERNAL variables x_i. Its frequencies are the
INTERNAL integer deficits s_ai. This is a specified exact finite
function, not an interpolation inferred from sampled asymptotics.

The nonempty-J terms are not known errors. They contain ordinary
simple channels killed by L_N and the full value/normal blocks of the
[mixed compiler](actual_mixed_augmented_plat_compiler.md), equations(7),(8).
They must remain until a bound on their ACTUAL contractions is proved.

There is a necessary far-end cancellation even for one port. Since
s_a=d modulo2, the polynomial in (4) satisfies

    F_N(N-h)=(-1)^(N-1)F_N(h).                         (5)

Thus the complete cosine term alone has an opposite-end alias with
the full complete rate. It cannot provide the entire external-color
gap. Outside the physical high-color range, F_N is the displayed
algebraic subset term, not a redefinition of the older compiler's
physical low-color core, which was set to zero. Extending the
algebraic convention to h=N, the two terms in
(2) cancel exactly to L_0=0. This does not wrap a physical auxiliary
color; it records the endpoint cancellation that an estimate of the
combined original source must respect.

## 3. The genuine first normal has explicit additional terms

Keep d fixed and let zeta=q exp(epsilon). Define the signed
STANDARD-pivot polynomial family

    Ltilde_j(epsilon)=(-1)^(j-1)P_(j-1)(Omega(epsilon)),
    Delta_N(epsilon)=C_N(Omega(epsilon))+2I.

The polynomial identity before specialization is

    Ltilde_(N-h)=(-1)^h T_h Ltilde_N+(-1)^N Ltilde_h
                          +(-1)^(N+1)Delta_N Ltilde_h/2. (6)

All T_h here have the actual moving Casimir argument. Delta_N(0)=0
but Delta_N'(0) is generally nonzero. Its first-normal contribution
cannot be deleted by differentiating the root relation (1).

In fact that defect itself has an exact complete-sector resolution:

    Delta_N'(0)=sum_a (-1)^N N s_a
               [q^(2a+1)-q^(-2a-1)] L_(N,a).          (7)

To prove this without a differentiated root identity, use the actual
generic eigenvalues from the mixed compiler. At a double pair a,d-a,
put w=q^(2a+1), A=2N-1-2a, B=2a+1. The eigenvalues are
zeta^A+zeta^-A and zeta^B+zeta^-B. Their difference is
-2N(w-w^-1)epsilon+O(epsilon^2). The corresponding Delta values are
-N^2 A^2 epsilon^2+O(epsilon^4) and
-N^2 B^2 epsilon^2+O(epsilon^4). Their divided difference is therefore

    [2N^2 s_a/(w-w^-1)] epsilon+O(epsilon^2).

The exact linear interpolation on this generic two-dimensional
spectral block now gives Delta_N'(0) as that coefficient times its
root Casimir nilpotent. Dividing by the original
L_N'(c_a)=(-1)^d 2N/(4-c_a^2) proves (7). Unpaired simple blocks
have zero first derivative; the odd self-node has s_a=0 and also
contributes zero. This proves (7) on every physical degree block.

There is a SECOND distinction: the original moving auxiliary pivot is
K_j^(1-N), not its fixed-root replacement (-1)^(j-1)K_j. Let H_j
have weights j-1-2r and let M_j(epsilon) be the literal typed
monodromy [2,1,1,2]. Exactly,

    K_j^(1-N)=(-1)^(j-1)K_j exp(-N epsilon H_j).

Thus, with the actual standard trace identity kept before the limit,

    (Llit_j)'(0)=(Ltilde_j)'(0)-N B_j,
    B_j=(-1)^(j-1)Tr_aux[K_j(q)H_j M_j(q)].             (8)

Set B_0=0 along with the algebraic convention L_0=0.

Combining (6),(8) gives the literal first-normal reflection: retain
the derivatives of (-1)^h T_h L_N and (-1)^N L_h, then add

    (-1)^(N+1)Delta_N'(0)L_h/2
       +N[(-1)^h T_h B_N+(-1)^N B_h-B_(N-h)].          (9)

The derivative of T_h(Omega(epsilon)/2) is included. Every spectator,
source cup, mark and exposed trace normalization still has its own
derivative when the identity is contracted. No whole-source generic
normal is replaced by a root value. Equations(2),(3) already retain
the spectral normals f'(c); these are distinct from epsilon derivatives.

## 4. The actual tangent-circle rectangle fixes the factor two

At one original crossing disk let x,y be the outer white-circle
curvatures and b,c its two middle curvatures. They are the SAME shared
face variables (circle curvatures) used by the coefficient theorem, with
zero for either of the two marked white lines. Put

    A=x+y, T_b=sqrt(bA+xy), T_c=sqrt(cA+xy),
    C=pi(T_b+T_c)/A.                                  (10)

The certified rectangle is nondegenerate, so A>0 and T_b+T_c>0.
For positive x,y,b,c put the outer tangency at z=0 and their centers
at1/x and -1/y. Under the conformal inversion w=1/z their circles
become the white lines Re w=x/2 and Re w=-y/2.

For a middle circle of curvature b above that tangency, its original
center is

    (x-y)/(bA)+i 2T_b/(bA), radius1/b.

This follows by squaring its two external tangency equations. Its
center norm squared minus radius squared is4/(bA); inversion
therefore gives center (x-y)/4-i T_b/2 and radius A/4. The middle
c circle on the other side gives center (x-y)/4+i T_c/2.
The orthogonal shaded planes are the horizontal lines through these
centers. Hence the actual crossing-circle rectangle has

    white-line width W=A/2,
    shaded-line height H=(T_b+T_c)/2.                 (11)

The zero-curvature cases follow by the same formulas and continuous
line limits. No auxiliary color or finite off-critical frame has
been substituted for this complete circle packing.

The [original two-rectangle cusp marking](general_augmented_plat_matching_geometry.md),
section6, has even meridian spanning height H and disk longitude
spanning TWO widths. In its positive orientation,

    tau_geom,0=2i W/H=2i A/(T_b+T_c)=2pi i/C.          (12)

The area of this primitive basis is2WH, the area of the two actual
rectangles. This accounts for the factor2; one rectangle width alone
would give the wrong longitude.

For the SOURCE half twist R^epsilon, the already typed collar
calibration in the [channel Hessian theorem](actual_augmented_plat_channel_hessian.md),
section3, gives

    tau_geom,epsilon=tau_geom,0/(1-epsilon tau_geom,0/2)
                    =2pi i/(C-pi i epsilon).           (13)

Source epsilon=-1 is the geometric '+' collar. This is the marked
diagonal meridian in the half-twisted cusp lattice, not a claim that
half of the longitude is an integral loop in the original lattice.

## 5. The exact empty-subset term has a mesoscopic complex Gaussian law

Assume the fixed connected labeled right-angled certificate of the
[signed complete-source theorem](general_signed_augmented_source_volume.md).
Let A_N^epsilon=F_N(0) be the original complete signed source. Let l_N
be its all-maximal positive coefficient radius, and retain
Z_i,N=C_i(l_N)-pi i epsilon_i with Re Z_i,N>=c>0. For every fixed
compact complex polydisc K,

    F_N(sqrt(N) z)/A_N^epsilon
       =exp[-pi^2 sum_i z_i^2/Z_i,N] [1+o(1)]          (14)

uniformly for z in K. All fixed z derivatives converge uniformly on
smaller compact polydiscs to the derivatives of the displayed Gaussian.
This is an absolute derivative statement, not a relative estimate
at zeros of a differentiated Gaussian.

Here is a direct proof retaining both finite lattices. Write
a_i=M-t_i, M=floor(d/2), s0=d-2M in {0,1}. The signed theorem
gives the actual relative sector weights uniformly for
max t_i<=N^(1/2+delta), 0<delta<1/6, as

    exp[-sum_i Z_i,N t_i(t_i+s0)/N] [1+o(1)].

The extra factor is cos(pi z_i(2t_i+s0)/sqrt(N)). At odd levels
k_M=1 and all other multiplicities are2; at even levels all are2.
Thus u=t+s0/2 gives the full integer or half-integer Gaussian,
with the retained factor exp(Z_i,N s0^2/(4N)). Uniform Riemann
summation on either lattice gives

    sqrt(N) integral_R exp(-Z x^2)cos(2pi z x) dx
       =sqrt(pi N) Z^(-1/2) exp(-pi^2 z^2/Z).

The square root has positive real part. The integral follows first
for real positive Z and then by holomorphy on Re Z>0. Its convergence
is uniform on the stated compact sets of Z and complex z.

The original source tails remain controlled. The cosine product costs
at most C exp(C sum_i t_i/sqrt(N)), so the central absolute majorant
is exp(-c|t|^2/N+C|t|/sqrt(N)). The uniform relative sector error
therefore contributes o(N^(R/2)). Beyond the mesoscopic window and
below the fixed macroscopic cutoff, the proved common-radius bound
is a fixed polynomial times that same Gaussian majorant, and its
tail tends to zero. Beyond the macroscopic cutoff the original rate
gap exp(-cN+o(N)) loses at most exp(C sqrt(N)), and remains a gap.
Thus these sums concern the full finite F_N, not just a chosen window.
Divide by the nonzero signed complete asymptotic. Its common exterior
phase and omega_M factors cancel literally. The Gaussian is bounded
away from zero on K. Finally Cauchy's formula on a slightly larger
compact polydisc proves the derivative assertion.

Equation (14) concerns the EXACT empty-subset term. It does not bound
any nonempty-J small-color diagram, identify it with the whole mixed
source, or give a fixed complex neighborhood of h/N.

## 6. The primitive Hessian matching and remaining external problem

The [signed complete-source theorem](general_signed_augmented_source_volume.md)
has folded weight exp[-Z t(t+s0)/N], where
Z=C-pi i epsilon, s0=d-2floor(d/2), and s=s0+2t. The cosine in
(3) is therefore in exactly the normalization whose Gaussian
transform has the candidate quadratic external action

    phi(x_ext)=Phi-pi^2 x_ext^2/Z+O(x_ext^4).          (15)

Equation (14) proves this Gaussian normalization on its mesoscopic
scale; it does NOT assert a general fixed-neighborhood external
asymptotic or an analytic action phi. If the required packet is
proved, its retained similarity coordinates U=-2pi i x_ext and
V=-2phi' give V/U=tau_geom,epsilon to first order by (13).

In particular phi''(0)=pi i tau_geom,epsilon. The transfer template
which writes phi''=2pi i tau_packet uses

    tau_packet=tau_geom,epsilon/2=pi i/Z.              (16)

This agrees with the existing marked channel elimination and keeps
the primitive cusp shape separate from the packet's Hessian convention.

A real sqrt(N) folded-window estimate does not imply a relative
packet on a fixed COMPLEX external neighborhood: the relevant complex
internal displacement is then of order N. The general nonempty-J small-color
contractions, the combined far-color and alias gap, and the actual
nonlinear marked regulator comparison remain necessary inputs to
[general long-filling transfer](general_original_source_long_filling_transfer.md),
equations(2)--(5). None is claimed here. The external h_i and the
internal s_i,a_i remain different variables throughout.

## 7. A strict bound for the all-small untwisted subset

One subset admits an immediate literal bound. Assume EVERY circle is
replaced by L_(h_i), h_i>=1, and every retained epsilon_i is zero.
Write B_N^small(h) for this original marked contraction. In the
original balanced complete physical basis,

    F|u>=(1-Q^(u+1))|u+1>,
    Ecal|u>=(Q^(-u)-1)|u-1>, K|u>=q^d Q^(-u)|u>.

Thus ||F||,||Ecal||<=2 and ||K||=||K^-1||=1. The original
coproducts F12=F tensor I+K^-1 tensor F and
Ecal12=Ecal tensor K+I tensor Ecal have norms at most4. Hence
||Omega||<=18. Its exact Chebyshev recurrence gives by induction
||L_h||<=19^(h-1), retaining its actual full matrix.

The k bottom cups have norms N^(3/2), the k-1 ordinary caps have
norms N^(-1/2), and the unrestricted marked cap has norm N^-1:
their respective supported entries have moduli N,1/N,1/N^2, with
N,N,N^2 entries. The exterior framing factor is a unit. The literal
matrix contraction therefore satisfies

    |B_N^small(h)|<=N^(k-1/2) 19^[sum_i(h_i-1)].       (17)

If any h_i=0 this algebraic subset term is zero. Equation(17) is
subexponential for h_i=O(sqrt(N)). For a fixed certified positive-volume
exterior, it also gives a strict gap below F0=Vol(Y_D)/(2pi) throughout
1<=h_i<=delta N whenever delta R log19<F0.

This covers only J=all ports and epsilon_i=0. A proper subset still
contains its actual complete coupons; a signed port still contains
R^epsilon. Neither may be deleted from the norm estimate. No general
proper-subset gap, signed small-color bound, or mixed packet follows
from (17), and no generic-q normal is inferred from this root estimate.

## 8. Verification and scope

The [focused audit](../experiments/audit_actual_external_circle_reflection_and_cusp.py),
with [recorded results](../experiments/actual_external_circle_reflection_and_cusp_results.json),
checks 78 formal polynomial identities, 54 full root matrix reflections,
204 actual complete-sector weights, 54 genuine polynomial first jets,
and nine full Casimir-relation normal defects. Fourteen independently
built original typed circle/pivot jets and fourteen literal first-normal
reflections check both terms of (9), including the moving pivot.
Six exact inversion identities and nine primitive/packet Hessian
identities check the geometric normalization. An additional 216 complex
Gaussian comparisons retain both finite fold lattices and their first
two derivatives; they are checks of the Gaussian step, not substitutes
for the source-tail proof of (14). The latter follows from the signed source theorem as shown above.

No fixed-neighborhood mixed-color packet, proper-subset gap or filled-knot limit follows from this local reflection theorem.