# Actual Fourier polarization gives a nonzero geometric normal block

Research theorem, 27 October 2026. Fourier-transforming the SECOND
physical cut, while retaining the original first-cut rank-one row,
gives an exact new partial family for the original root state. Its
specified proper finite-array lift has a nonzero geometric formal
Gaussian block. The two external coordinates are the first physical
position and the second Fourier label. They correspond to (A,p_e),
which is birational on the complete discrete-faithful framing torsor.

The displayed source is the ACTUAL finite sum over both external
labels. A subsequent root Ward reduction fixes the first input
and retains only the Fourier-label sum, as described below. Neither
source is the residue eta=0 of the old band variable. No
selected global geometric contribution or volume conjecture follows
from the existence of this local block.

## 1. Exact finite polarization and the unchanged selected source

Use the literal four-port tensor T_(c,d;a,b) from
[the two physical cuts](actual_two_cut_framing_port_reconstruction.md).
All original pivots, caps, Cartan/framing lines, meridian marks and
the full peripheral factor stay in T or its recorded external line.
The second cut is an identity wire, with no new pivot. At level N
put Q_N=exp(2pi*i/N) and

    V_(j,b)=Q_N^(jb), (V^-1)_(b,j)=Q_N^(-jb)/N,
    T^V=(I tensor V)T(I tensor V^-1).

Keep the original first-cut row: define the RAW partial array

    Jtilde_(a,j)=sum_c T^V_(c,j;a,j).             (1)

Then finite basis invariance of the identity closure proves EXACTLY

    P_N(M)=(1/N)sum_(a,j=0)^(N-1) Jtilde_(a,j). (2)

The first factor 1/N is the original cut average. The inverse
Fourier matrix contributes another 1/N INSIDE Jtilde. Neither is
silently removed or treated as a second physical pivotal trace.
Here P_N denotes the originally selected scalar with its chosen
reduced/full external line; the original pointing at completeness
and every external d_N factor are unchanged on the two sides.
For a conserving tangle c+d=a+b, put q=d-b. Formula (1) becomes

    Jtilde_(a,j)=(1/N)sum_(b,q) Q_N^(jq)
                              T_(a-q,b+q;a,b).    (3)

All four original head bounds are retained by zero extension.
Crucially c is summed in (1), not set to a. A double diagonal at
BOTH cuts would impose q=0 and lose the new Fourier label.

The [whole Vandermonde construction](actual_two_cut_fourier_polarization_and_cap.md)
retains the actual generic inverse, source, normal connection and
endpoint carries. For the stationary construction here specify also
the proper ROOT LIFT obtained from (3) by using Q^(jq)/N off root.
It equals (1) at every original root. Off root this kernel is
generally DIFFERENT from V(Q)^-1, and its total external sum need
not equal the original whole q-germ. This distinction is retained;
no equality of their higher q-normal source jets is inferred.

## 2. The open phase is made from the original finite coefficients

Let the braid have m crossings. The old two-position array has
external labels (a,b) and r=m-1 remaining cycle flows u. Opening
the two ports with balanced offset (-q,+q) adds one boundary-flow
parameter. A spanning tree in the connected remaining graph gives
an integral particular flow linear in q; the same internal cycle
coordinates u remain. No lattice index or hidden determinant occurs.

Every original position/transfer is consequently an integral affine
function of (a,b,q,u). Substitute these functions into the original
finite factorial/Cartan coefficients. Their compact formal expansion
therefore defines a genuine open phase germ

    S_open(a_log,b_log,t,u_log), t=Hq,
    a_log=Ha, b_log=Hb, H=Log Q,

and the actual nonzero amplitude with all half-step and source lines.
The variable compact arguments must stay in the established regular
shape chart. At t=0 this is exactly the old closed coefficient model.
This construction uses its WHOLE finite-product expressions, not an
unjustified summation of fixed-offset asymptotic formulas.

The actual boundary proper-ratio calculation in the two-cut theorem
gives on the closed geometric critical surface

    partial_t S_open=Log p_e.                     (4)

The balanced exchange lowers the first output and raises the second;
the first-cut wave momentum is one in its original constant boundary
frame. Hence (4) has the stated sign and contains the original
factorial-boundary adapter. Flattened logarithms and peripheral signs
are those of the original marked critical correspondence.

Put v=Hj. The proper lift (3) has the exact additional monomial

    Q^(jq)=exp(vt/H),
    Phi=S_open+vt.                                (5)

The new external variables are (a_log,v). Its internal variables
are x=(b_log,u_log), together with t, of dimension m+1=r+2.

## 3. A complete discrete-faithful framing torsor has birational (A,p_e)

The following proof supplies a nonempty regular polarization chart
for EVERY complete discrete-faithful knot representation in the
actual geometric model. It does not assert this for arbitrary
reducible or nondiscrete representation components.

Normalize the cut meridian J=[[1,1],[0,1]] and retain
F(r,s)=[[r,1-r],[s,-s]], s nonzero, A=1/(1+s). For the chosen
actual physical second edge retain its developed PREFIX words U,V.
The actual inverse clock is

    k=ell_U/ell_V,
    ell_W=d_W+(a_W-d_W)r+b_Ws+c_W r(1-r)/s.        (6)

An independent second physical position exists by the actual
two-position theorem, so k depends nontrivially on r. Here U,V
are group words, UV^-1 is a nontrivial parabolic meridian, and
det U=det V=1. Let t_W=Tr W, h_W=a_W-d_W and sigma=(-1)^ell
for its actual prefix strand position ell; the Fourier sample label
is still j. The exact prefix/momentum identities
give, with u_p=p+p^-1 and v_p=p^-1-p,

    A_0=c_U+s t_U, A_1=c_V+s t_V,
    u_p=sigma(A_0-kA_1)/[s(k-1)],
    D=-sigma s(k-1)v_p,
    D=c_C+s h_C-2c_Cr, C=U-kV.                  (7)

First, every UPPER TRIANGULAR word W of this discrete torsion-free
projective group has diagonal entries a,a^-1 with a^2=1, hence h_W=0.
Indeed if |a| differs from one, suitable conjugates W^n J W^-n
are nontrivial translations converging to the identity. If |a|=1
and a^2 has infinite order, choose a^(2n) tending to one; then
W^n J W^-n J^-1 is a nontrivial translation tending to the identity.
Both contradict discreteness. If a^2 has finite nontrivial order,
the upper triangular W is diagonalizable with projectively finite
order, contradicting torsion-freeness. This proves the assertion
without a stabilizer classification theorem.

Suppose p were independent of r. Since k_r is nonzero, differentiating
the Mobius expression in (7) forces A_0=A_1 as functions of s.
Thus c_U=c_V and t_U=t_V. Now C_0=U-V has c=0, trace zero and
determinant zero, so C_0=b E_12. It is nonzero because UV^-1 is
a nontrivial meridian. Equality of the two determinants forces
b c_V=0, hence c_U=c_V=0. Both U,V are upper triangular; the
previous paragraph gives h_U=h_V=0. Equation (6) then makes k
independent of r, a contradiction. Therefore (A,p) is etale on
a nonempty open of the complete geometric framing torsor.

The same upper-word argument shows c_U,c_V are not both zero.
On the open set with the displayed denominators units, (7) has
the explicit rational inverse

    s=(1-A)/A,
    k=(s u_p+sigma A_0)/(s u_p+sigma A_1),
    C=U-kV, D=-sigma s(k-1)v_p,
    r=(c_C+s h_C-D)/(2c_C).                       (8)

Thus the function field of the framing torsor equals its field in
(A,p): no new framing cover is introduced by this polarization.
Any existing marked representation, SL2-sign or half-density cover
is still retained. This is a birational assertion on the indicated
open sets, not a global compactification or cycle identification.

At a generic old position-projection caustic p=+1 or -1, k_p=0
but differentiating (8) gives

    r_p=-sigma s(k-1)/c_C !=0.                    (9)

Thus the new chart resolves those old two-position caustics when
the other displayed units and original shape chart remain regular.
The exact geometric two-form is

    Omega_cut=-ell_V(k-1)/(A_1-A_0)
                              dlog A wedge dlog p. (10)

This is the prefix density in its new rational coordinates, not a
claim about the old finite band cap variable. It is regular at the
generic caustics in (9).

## 4. The ACTUAL new stationary block is nondegenerate

At t=0 let x=(b_log,u_log). Fixing the first physical position
in the old geometric Morse--Bott model leaves one framing tangent
xi. Hence H_0=partial_x^2 S_open has rank r and radical span(xi).
Let c=partial_x partial_t S_open and gamma=partial_t^2 S_open.
Differentiating (4) along the critical framing gives

    mu=c dot xi=dlog p_e(xi),

which is nonzero precisely on the new etale polarization chart.
The internal Hessian of (5) is the actual bordered matrix

    H_new=[[H_0,c],[c^t,gamma]].                   (11)

It is invertible. If H_new(delta_x,delta_t)=0, pairing its first
row with xi gives mu delta_t=0, hence delta_t=0. Then delta_x
lies in the old radical, and the last equation gives delta_x=0.
No invertibility of an old two-position transverse minor is used.
Thus this proof also applies where that old minor is singular.

For each new external pair with

    eta=exp(v), eta p_e=1,

the old closed geometric point at t=0 solves all new internal
critical equations. The formal implicit-function theorem for (11)
makes it the UNIQUE critical germ there. In particular all the old
closed equations still hold, and

    Phi_critical=S_geo,                            (12)

with exactly the same marked regulator action and retained base
characters: the new term vt vanishes at t=0. The comparison is
now an actual Fourier partial-family critical construction, not
substitution into the old band-generating cap.

The regular marked representation/gluing branch has the meridian
as a local coordinate. Nonzero mu and det H_new persist in that
meridian deformation germ. Thus the same construction supplies
the geometric formal normal line and action S_geo(M) there. The
birational function-field statement of Section 3 was specifically
at completeness; it is not promoted to a global statement over
every peripheral point.

On an old regular (A,B) chart, choose xi with xi_b=1 and first
contract u. If H_perp is the old r-by-r transverse Hessian, its
remaining Schur block in (b,t) is

    [[0,mu],[mu,gamma_eff]],
    det H_new=-mu^2 det H_perp.                  (13)

The formula is independent of gamma_eff. At an old projection
caustic xi_b may vanish, so that normalization and old minor are
not used; the direct kernel proof of (11) remains valid.

## 5. Fourier normalization and the remaining actual source

The amplitude at the new critical point is the SAME original
nonzero coefficient amplitude at q=0. The Fourier character is
one there. Equations (11)--(13) therefore give a nonzero formal
normal block, with algebraic coefficients on the new chart and
the original square-root/phase mark retained in its Gaussian line.

The two extra discrete sums b,q contribute their logarithmic
measure H^-2, while the inverse Fourier matrix contributes 1/N.
On the physical sequence H_N=2pi*i/N their product is EXACTLY

    (1/N)H_N^-2=1/(2pi*i H_N).                  (14)

This is the normalized two-variable formal Fourier pairing. With
the explicit convention that its cross Gaussian exp(zt/H) has
pairing one, composition after the old transverse contraction
gives numerical leading coefficient a_perp/mu for that declared
ordered cross pairing. The oriented
external two-form has an additional minus sign: v=-Log p implies
db/dv=-1/mu, consistently with (10). This is a FIXED ordered-
Fourier phase, not a variable source correction. Another ordered
Gaussian square-root mark carries its corresponding fixed phase
in the recorded base line. Neither the original physical 1/N in
(2) nor any peripheral character is absorbed into an unspecified
variable unit.

The resulting amplitude has the same exponential action (12);
no new exponential factor is generated by the Fourier pair. This
is a formal, coefficientwise statement from the original proper
finite-array model. It asserts neither analytic stationary-phase
asymptotics for its growing sums nor survival of this block in
the final selected contraction.

In particular the CORRECT new final source is still the finite
sum in (2). Its Fourier label j takes all original N head values.
It has not become eta=0, a choice of one momentum boundary, or
an unmarked sum over the old quadratic framing sheets. A global
comparison must transport that finite source, its endpoint carries
and the actual whole-V versus proper-root-lift distinction above.

[Exact bordered-Hessian and rational-polarization checks](../experiments/audit_actual_fourier_polarized_normal_block.py)
and [saved results](../experiments/actual_fourier_polarized_normal_block_results.json).
They pass four exact bordered-Hessian identities, 548 rational
forward/inverse and density-Jacobian cases, and 120 old-caustic
cases with nonzero new momentum derivative, including both prefix
parities. Finite-field cases check the rational identities; the
discrete-faithful argument in Section 3 is a separate direct proof.

The [Fourier partial support theorem](partial_geometric_support_theorem.md),
Section 7, applies the global finite-array certificate to the
specified proper root lift and this SAME formal block. It retains
the full first-cut sum, the two exterior labels, the original and
Fourier factors 1/N, and the distinction from whole-V normal jets.
Its geometric A-factor assertion concerns that actual all-level
ROOT partial family, rather than an asserted off-root q-normal
equivalence or the final sourced scalar sum.

The [subsequent one-index source theorem](actual_one_index_fourier_source_and_ward_reduction.md)
and [its independent audit](one_index_fourier_source_independent_audit.md)
use actual ROOT scalarity of the fully reclosed cut to fix ANY
first input a while retaining the original sum over its outputs.
Thus the selected scalar is sum_j Jtilde_(a,j), with no remaining
outside 1/N and with its internal Fourier 1/N unchanged. A fixed
good root-of-unity phase sequence retains a nonzero geometric
normal block. Section 8 of the partial support theorem gives
the corresponding nonzero operator on each finite residue class.
The unresolved global pushforward can therefore be formulated
as ONE exterior Fourier-label sum. Whole q-normal source defects
remain explicit; root scalarity is not extended off root.

The [rank-one prefix calculation](mobius_fourier_framing_and_intrinsic_norm_pole.md)
now simplifies the fixed-A rational inverse to an explicit Möbius
map of projective lines and computes its single intrinsic density
pole. The [actual cancellation theorem](actual_fourier_source_cancellation.md)
provides an important scope test: an actual port current with zero
final source still has a nonzero block of the same geometric action
on this chart. Consequently this local block and its partial
A-factor do not, by themselves, prove selected survival.
