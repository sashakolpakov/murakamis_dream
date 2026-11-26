# The left-minus-local remainder on a fixed complex neighborhood

Private finite-source deduction, 9 November 2026. The exact remainder
\(E_N^-=\mathcal T_N-I_N-\mathcal R_N^+\) is exponentially smaller
than the original local action on a fixed complex neighborhood of
\((-2,z_*)\). The selected-left and half-grid estimates already hold
on real intervals of both outside variables. Their exact polynomial
degrees supply the missing complex continuation. The other required
terms already have fixed complex-neighborhood bounds.

This conclusion uses the complete contour reduction before its
physical-half-band and small-outgoing-index partitions. Neither
partition needs to be continued. The full right contribution
\(\mathcal R_N^+\) remains separate, particularly when the incoming
ordinary color varies. No numerical evaluation, saved-value arithmetic,
import, compilation, or alteration of a frozen source is used.

## 1. Exact quantities and fixed reference

Fix an eligible actual complete word beginning \(343\), in the original
powers three and four, of length at least five. All its coupled reference
coordinates, private heights and original primitive constants remain
fixed. Use
\[
 c=\Im y_*,\qquad h_z=\Im z_*,\qquad H=1/100,\qquad
 Z=e^{-2\pi iz},\qquad P(w,z)=\mathcal P_0^+(w,z).
 \tag{1}
\]
The actual reference satisfies
\[
 3/10<\Re z_*<39/100,\qquad |e^{-2\pi iz_*}|<8/7,\qquad
 \Lambda_*:=\Re P(-2,z_*)=\Lambda_{123}(z_*)>419/200.
 \tag{2}
\]
Here \(\Lambda_{123}\) is the original fixed-reference affine plane,
not an action reassigned to displaced references.

Retain
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad P_b=(r;r)_b,\quad
 M=\lceil N/2\rceil,\quad B=\lceil11N/12\rceil,\quad
 L=(M-\tfrac12)/N.
 \tag{3}
\]
Write \(F_N=F_{34,N}\), and retain the complete own-three kernel
\[
 C_N(Y,Z)=\sum_{k=0}^{D}
       \frac{Y^{-k}(rY;r)_k(rZ;r)_k}{P_k^2}
 \tag{4}
\]
and the full forced polynomial \(d_N(r^b)=P_b^{-1}\),
\(\deg d_N\le D\). The original exact transfer and its full right
physical part are
\[
 \begin{split}
 \mathcal T_N(w,Z)
 &=N[Y^0](F_Nd_NC_N)+N[Y^N](F_Nd_NC_N)
   =\sum_{b=0}^{D}\frac{F_N(w,r^b)}{P_b}C_N(r^b,Z),\\
 \mathcal R_N^+(w,Z)
 &=\sum_{b=M}^{D}\frac{F_N(w,r^b)}{P_b}C_N(r^b,Z).
 \end{split}
 \tag{5}
\]
Both original Fourier sectors and their \(+N\) factors occur in (5).

Choose the unchanged fixed local segment \(J_*\) used by the
lower-central and lower-half assemblies. It can be, and is, the
segment in the local-source theorem (15). Define
\[
 I_N(w,z)=N\int_{J_*}
  F_N(w,e^{-2\pi iy})d_N(e^{-2\pi iy})
            C_N(e^{-2\pi iy},e^{-2\pi iz})\,dy.
 \tag{6}
\]
The local theorem already proves on a fixed complex bidisk
\[
 I_N=N^{-2}A(w,z)e^{NP(w,z)}
          (1+O_{\rm hol}(N^{-1})),\qquad A(w,z)\ne0.
 \tag{7}
\]
The exact integral, not just its leading term, is used below. Set
\[
 E_N^-(w,z)=\mathcal T_N(w,e^{-2\pi iz})-I_N(w,z)
                         -\mathcal R_N^+(w,e^{-2\pi iz}).
 \tag{8}
\]
This is the same remainder as in the boundary-extension scope note.

**Theorem.** There are a fixed complex bidisk \(V\) about
\((-2,z_*)\) and a number \(\eta>0\) such that
\[
 \sup_V |e^{-NP(w,z)}E_N^-(w,z)|\le C e^{-\eta N}
 \tag{9}
\]
for all sufficiently large \(N\), at both parities. For every fixed
\(j,k\ge0\), on a smaller fixed bidisk,
\[
 \partial_w^j\partial_z^k
           [e^{-NP(w,z)}E_N^-(w,z)]=O_{j,k}(e^{-\eta N}).
 \tag{10}
\]
The neighborhoods are chosen before \(N\). Uniform versions hold on
compact reference subfamilies with the uniform source hypotheses and
fixed local-segment margins of the cited theorems. No uniformity in an
unbounded collection of word templates is asserted.

## 2. The signed ledger before the physical middle partition

Keep exactly the old deletion and cardinal filter
\[
 F_N^{\rm mid}=(I-\Pi_{\rm end})(F_N-R_N^a),\qquad
 K_N(y;w,z)=
 \frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_N(Y,Z)}{1-Y^N},
 \quad Y=e^{-2\pi iy}.
 \tag{11}
\]
The first-coordinate deletion starts at \(\lceil23N/24\rceil\);
the unchanged filter has lower cutoff
\(\lfloor\delta_{\rm old}N\rfloor\), \(0<\delta_{\rm old}<1/40\),
and upper cutoff \(B\). Its zero at \(Y=1\) is a polynomial identity
in the outside parameters, so the seam value of (11) is removable
on the whole neighborhood. No individual outgoing row is filtered.

Fix the same \(s\in(0,11/100)\) as the top seam-arc theorem. Define
all horizontal integrals toward increasing real part:
\[
 \begin{split}
 U_L&=\int_{[s,11/50]+iH}K_N\,dy,&
 U_H&=\int_{[9/20,1/2]+iH}K_N\,dy,&
 U_S&=\int_{[1-s,1]+iH}K_N\,dy,\\
 V_a&=i\int_c^H K_N(a+ih)\,dh\quad(a=L,1),\\
 J_-&=\int_{[L,1/2]+ic}K_N\,dy,&
 J_+&=\int_{[L,1/2]+iH}K_N\,dy .
 \end{split}
 \tag{12}
\]
At odd levels \(L=1/2\), so \(J_-=J_+=0\). At even levels both
short paths have length \(1/(2N)\); each source is estimated before
their difference is taken.

The complete lower-half theorem (23) supplies an exact holomorphic
error \(E_{\rm old}\), with normalized fixed-jet gap
\(\eta_{\rm actual}>0\), in
\[
 \mathcal T_N=I_N+\mathscr R_N^{(3)}+E_{\rm old},\qquad
 \mathscr R_N^{(3)}
 =\int_{[1/2,1]+ic}K_N
  -U_L-\int_{[9/20,1-s]+iH}K_N .
 \tag{13}
\]
This theorem already holds on a fixed complex outside neighborhood.
It is not being extended from its pointwise asymptotic.

Exact splitting of the top interval and the counterclockwise
right-rectangle identity give
\[
 \mathscr R_N^{(3)}
 =\mathscr R_N^{\rm cl}-U_L-U_H+U_S-V_1+V_L-J_-+J_+,
 \tag{14}
\]
where
\[
 \mathscr R_N^{\rm cl}
 =\int_{\partial([L,1]+i[c,H])}^{\rm CCW}K_N\,dy
 =\sum_{b=M}^{B-1}
       \frac{F_N^{\rm mid}(w,r^b)}{P_b}C_N(r^b,Z).
 \tag{15}
\]
There is no extra \(N\) after the last equality: it is already
present in (11). At retained nodes
\(F_N^{\rm mid}=F_N-R_N^a\). Thus put
\[
 D_N^a=\sum_{b=M}^{B-1}\frac{R_N^a(w,r^b)}{P_b}C_N(r^b,Z),
 \qquad
 T_N^{\rm far}=\sum_{b=B}^{D}
                  \frac{F_N(w,r^b)}{P_b}C_N(r^b,Z).
 \tag{16}
\]
Subtracting the entire right sum in (5), rather than a truncated
middle part, proves the exact identity
\[
 \boxed{\;
 E_N^-=E_{\rm old}-U_L-U_H+U_S-V_1+V_L-J_-+J_+
                              -D_N^a-T_N^{\rm far}.
 \;}
 \tag{17}
\]
These are the identities in Sections 3--4 of the complete-transfer
reduction, now with their outside parameters retained. They are
valid independently of estimates. In particular (17) makes no use
of its later physical-half-band continuation, small-\(k\) deletion,
or unresolved middle sum.

## 3. The real intervals that are actually available

The following bounds are for the full sources in (12), with every
inner index, denominator and original contour factor retained:

| Term | Source scope and bound |
| --- | --- |
| \(U_L\) | Selected-left complete source (5),(11): all \(w\in[-2,2]\), \(z=u+ih_z\), \(u\in[3/10,39/100]\), rate \(\Lambda_{123}(z)-1/10000\). |
| \(U_H\) | Half-grid/near-half complete source (9): the same real outside rectangle, rate \(\Lambda_{123}(z)-1/20000\). |
| \(V_L,J_-,J_+\) | That source (10): the same real outside rectangle, each at rate \(\Lambda_{123}(z)-10^{-13}\). |
| \(U_S\) | Top seam-arc source Section 2: a bound for each arc before integration on fixed complex outside neighborhoods, normalized gap \(1/2000\). |
| \(V_1\) | Actual deep radial seam (18): fixed complex outside neighborhoods, normalized fixed-jet gap \(10^{-16}\), including its removable seam point. |
| \(E_{\rm old}\) | Actual lower-half assembly (23): fixed complex outside neighborhoods, normalized fixed-jet gap \(\eta_{\rm actual}\). |

All displayed real rates allow a fixed polynomial in \(N\).
In the first three rows the reference heights stay fixed while \(u\)
runs through the indicated real interval. Their estimates are not
restricted to the single actual value \(u=\Re z_*\). The affine
comparison plane is the same in every row and satisfies (2).
This distinction supplies the continuation below.

For each fixed \(N\), each integrated current in the first three
rows is a polynomial in \(w,Z\) of separate degree at most \(D\).
Indeed the complete prefix has color degree at most \(D\), the
filter is linear in its \(Y\)-data and does not raise that degree,
and the following kernel has \(Z\)-degree at most \(D\).
The denominator in (11) depends only on the integration variable.
The paths, including the level-dependent \(L\) and the short grid
intervals, are independent of \(w,Z\). Integration therefore
preserves these outside degrees. At \(a=L\),
\(Y^N=-e^{2\pi Nh}\), so there is no parameter-dependent pole to
cross. The real source bounds are uniform in those paths and in
both parities.

Here is the explicit continuation argument. For any one of these
currents \(J_N(w,Z)\), let its real gap be \(g>0\). Choose
\(\alpha>0\) so that
\([\Re z_*-\alpha,\Re z_*+\alpha]\subset(3/10,39/100)\).
It may be shrunk until the oscillation of the affine rate on that
interval is less than any prescribed positive tolerance. Put
\[
 t=\tan\bigl(\pi(z-z_*)\bigr),\qquad a=\tan(\pi\alpha),\qquad
 \widehat J_N(w,t)
 =(1+t^2)^D J_N\!\left(w,Z_*\frac{1-it}{1+it}\right).
 \tag{18}
\]
This is a polynomial of degree at most \(D\) in \(w\) and \(2D\)
in \(t\). The original denominator \(P_k\) and all numerator zeros
remain inside \(J_N\); only the explicit nonzero chart factor in
(18) is divided out.

Let \(\mathcal E_\rho\) denote the usual closed Chebyshev ellipse
with foci \(\pm1\), and put
\(A_\rho=(\rho+\rho^{-1})/2\). On
\(w\in2\mathcal E_\rho\), \(t\in a\mathcal E_\rho\), with
\(aA_\rho<1\), the elementary two-variable Chebyshev estimate gives
\[
 |J_N(w,Z(t))|
 \le C N^{B'}
 e^{N\{\Lambda_*-g+\operatorname{osc}\Lambda_{123}\}}
 \exp\!\left\{
 D\left(3\log\rho+
       \log\frac{1+a^2}{1-a^2A_\rho^2}\right)\right\}.
 \tag{19}
\]
The degree factor \(3D=D+2D\) is retained. First choose
\(\alpha\) small and then \(\rho>1\) close to one; the added
rate in (19) is arbitrarily small. Both ellipses contain their
closed real intervals in their interiors, including the color
endpoint \(w=-2\). The inverse tangent is holomorphic on
\(|t|<1\), on its branch through zero. Hence these products contain
a fixed complex bidisk about \((-2,z_*)\).

Finally shrink that bidisk within the original action chart so
\(\Re P(w,z)\) differs from \(\Lambda_*\) by an arbitrarily small
amount. Choosing the oscillation, continuation cost and action
variation with total less than \(g/4\), and then absorbing the
fixed polynomial, proves a normalized bound with gap \(g/2\).
This is the elementary horizontal-complex-extension theorem applied
to the complete integrated current. It works just as well for
level-dependent contours because their degree and real estimates
are uniform. It does not infer a neighborhood estimate from
isolated physical-node values.

## 4. The two physical corrections already have complex scope

The complete first-coordinate end theorem (26) proves a positive
bound on every physical subset of the first-end rectangle:
\[
 |D_N^a|\le C N^A e^{11N/6}
 \qquad (|Z|\le e^{3\pi/20}).
 \tag{20}
\]
It holds for all real \(w\in[-2,2]\) and on a sufficiently small
fixed complex disk about \(-2\). Its proof keeps the complete
terminating first-cap polynomial and all outgoing rows. Thus the
partial deletion in (16) is eligible; it is not extracted from a
bound on a signed total. Its original normalized neighborhood
bound and fixed jets have gap \(1/96\).

For the last sum in (16), \(B\ge\lceil5N/6\rceil\). The actual
high-band theorem (18)--(19) therefore applies to exactly this
subset of its allowed physical indices, through the true terminal
index \(D\):
\[
 \sum_{b=B}^{D}
 \left|\frac{F_N(w,r^b)}{P_b}C_N(r^b,Z)\right|
 \le C_\tau N^{A_\tau}
                 e^{N(1499/720+\tau)},\qquad |Z|\le8/7.
 \tag{21}
\]
Its complete terminal-insertion estimate is valid on all real
ordinary colors and, with any prescribed rate allowance, on a fixed
complex color disk about \(-2\). Both parities, the consumed radical
normal and the remaining full terminal Hermite trace are retained.
The original action comparison
\[
 419/200-1499/720=47/3600>1/100
 \tag{22}
\]
gives its normalized gap \(1/200\) on sufficiently small fixed
complex outside neighborhoods. Strict \(|Z_*|<8/7\) permits such
a neighborhood inside the source disk. There is no outgoing
row deletion or lost physical endpoint in (21).

## 5. Conclusion and the remaining incoming issue

Intersect the finitely many fixed neighborhoods in Sections 3--4
with the local-source chart. One conservative choice of final rate is
\[
 \eta=\frac18\min\left\{
 \eta_{\rm actual},\,10^{-16},\,10^{-13},\,
 1/20000,\,1/2000,\,1/96,\,1/200
 \right\}>0.
 \tag{23}
\]
The continuation above leaves at least half the original gaps for
the newly continued currents. Existing complex gaps, finite sums and
polynomial factors fit inside the reserve in (23). Apply (17) to
obtain (9). The normalized expression in (9) is holomorphic.
Cauchy's formula on smaller bidisks proves (10), without
differentiating any contour, absolute value, or moving reference.

Consequently the exact transfer has the source identity
\[
 \mathcal T_N(w,e^{-2\pi iz})
       =I_N(w,z)+\mathcal R_N^+(w,e^{-2\pi iz})+E_N^-(w,z)
 \tag{24}
\]
with \(E_N^-\) now paid on a fixed complex bidisk. If the general
combined-envelope hypothesis of the boundary-extension scope note
is separately proved, its Proposition 1 pays \(\mathcal R_N^+\)
at \(w=-2\) on an outgoing disk. Together with (7),(9), this gives
the original nonzero transfer asymptotic there, with its fixed
normalized outgoing derivatives.

No incoming-color bound for \(\mathcal R_N^+\) is established in
this deduction. Its current sharp Fourier-observation input is at
complete color. Thus (24) does not yet extend the whole transfer
packet to a bidisk in \(w,z\), despite the bidisk estimate for
\(E_N^-\). The ordinary right-boundary closing is also a separate
complete Fourier observation. No composition, short-filling, or
finite-exception assertion follows merely from (9).

## 6. Frozen source bindings

The proof uses the following written sources at the indicated bytes.
No source was edited in making this deduction.

| Source | SHA-256 |
| --- | --- |
| [Boundary-extension scope](research_mixed_next_attachment_boundary_extension_scope.md) | 74bca3cd11850a0ab0b507de69fb42ae6e73d61434dc1bc67b1872bd5710d54a |
| [Original local source](research_mixed_three_four_next_local_source.md) | f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696 |
| [Complete-transfer reduction](research_mixed_next_three_complete_transfer_middle_reduction.md) | b8e2cf1b901fde9d962fab2d1d3d160dd7871321388750eb462cae7183cb4e46 |
| [Actual lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md) | e891cfb63b4ca3e5c1fb4682e31461eb63cc93296a016091ae04f8d0c040e52e |
| [Complete selected-left source](research_mixed_next_three_selected_left_complete_source.md) | 0192fae0b844f5e4e9505916d7f736726400edbb871aee2e14307c930795a78b |
| [Half-grid and near-half source](research_mixed_next_three_half_grid_and_near_half_complete_source.md) | ead6c765d9b49269bbaab61bd206a6a785b0ddeb54d018e7af5bfa352edd0bb6 |
| [Top seam-arc removal](research_mixed_next_top_seam_arc_removal.md) | 98f1d703059e9bd028231664a52a37d9b917ac3f9f298e66e95fd6a211b39ad0 |
| [Actual deep radial seam](research_mixed_next_three_actual_deep_radial_seam.md) | 6489199a1224c2de2a8455f3f35c7ad18938f8c96f7716794bfae6a8a7c054e4 |
| [Exact right paired insertion](research_mixed_next_right_paired_terminal_insertion.md) | 976f8bf4f46aa7011c8973e20e5335b914e9bc7a4cf5c76c1f0044a5aa2c56c1 |
| [Sectorwise first end](research_mixed_three_four_next_sectorwise_first_end.md) | bcf01896c2a7a0eda10a6d9859353ddb01be053910673c5ec07536700cbd3b3c |
| [Actual high band](research_mixed_next_right_insertion_actual_high_band.md) | 1e15ac042b91461b3bd9b619f8205db2266ad7fee4185a04d0c7c3acfd5a5be6 |
| [Horizontal complex extension](research_mixed_horizontal_complex_extension.md) | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
