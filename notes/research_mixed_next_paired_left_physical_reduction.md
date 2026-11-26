# The paired left remainder as a physical sum and two connectors

Private research deduction, 8 November 2026. A half-grid cut just to
the right of the central interval's left endpoint converts the paired
left remainder into an exact partial physical sum and two oriented
vertical currents. All added horizontal intervals are already paid.
The seam current is paid down to depth \(1/100\); any deeper part
remains literal. No estimate for the other vertical current or the
remaining physical band is inferred.

No numerical evaluation or modification of a frozen source is used.

## 1. Keep the source and choose the right half-grid

Use the ordinary-next family and old filter of
[the complete shoulder assembly](research_mixed_next_complete_lower_right_shoulder.md).
Both conditional vertices after the first cap are ordinary, with
the original flags \((0,1,\beta)\). Put
\[
\begin{gathered}
D=N-1,\quad r=e^{-2\pi i/N},\quad P_b=(r;r)_b,\quad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\quad \beta=0,1,\\
F_N^{\rm mid}=(I-\Pi_{\rm end})(F_N-R_N^{\rm node}),\\
l_N=\lfloor\delta N\rfloor,\quad B_N=\lceil11N/12\rceil,
\quad 0<\delta<1/40,\\
F_N^{\rm mid}(r^b)=0\quad(b\le l_N\ \hbox{or}\ b\ge B_N),\\
K_N(y)=
\frac{N F_N^{\rm mid}(w,Y)d_N(Y)C_{\beta,N}(Y,Z)}{1-Y^N}.
\end{gathered}
\tag{1}
\]
The first-node deletion \(R_N^{\rm node}\), both physical cutoffs,
the complete Fourier polynomial, and every conditional row are
unchanged. In particular \(\delta\) is the fixed sufficiently small
choice in the old low-physical theorem, not an arbitrary number
below \(1/40\). The full prefix is \(F_N=F_{34,N}\).

Let \(h=\Im y_*\in(-.102,-.001)\), \(H=1/100\), and let
\(s\in(0,.11)\) be exactly the fixed upper seam width from
[upper seam-arc removal](research_mixed_next_top_seam_arc_removal.md).
Write
\[
a_0=\frac{11}{50},\qquad
\mathscr L_N=
\int_{[0,a_0]+ih}K_N\,dy-\int_{[s,a_0]+iH}K_N\,dy .
\tag{2}
\]
All horizontal integrals are oriented rightward. These are precisely
the two left terms of the remaining signed chain; no coefficient
has been omitted.

Choose
\[
n_N=\lceil Na_0\rceil,\qquad c_N=\frac{n_N+1/2}{N}.
\tag{3}
\]
Thus \(a_0<c_N<a_0+3/(2N)\), with a non-strict upper inequality
also sufficient, and \(Nc_N\) is a half integer. In particular,
for all sufficiently large \(N\), \([a_0,c_N]\subset[.22,.23]\).
Choosing the cut on this side of \(a_0\) keeps both added horizontal
strips inside the already proved central intervals.

For a real \(c\) at which the following path is regular, define
the upward current
\[
V_N(c)=\int_{c+ih}^{c+iH}K_N(y)\,dy
       =i\int_h^H K_N(c+i\tau)\,d\tau .
\tag{4}
\]
Both \(c=0\) and \(c=c_N\) are allowed. At zero, the old filter
removes the physical pole. At \(c_N\), the half-grid identity
\(Y^N=-e^{2\pi N\tau}\) excludes a denominator zero.

## 2. Exact rectangle identity and every residue

Set
\[
S_N^{\rm mid}=
\sum_{b=0}^{n_N}
 \frac{F_N^{\rm mid}(w,r^b)}{P_b}C_{\beta,N}(r^b,Z).
\tag{5}
\]
For large \(N\), its nonzero terms have \(l_N<b\le n_N<B_N\).
The counterclockwise rectangle \([0,c_N]+i[h,H]\) encloses
exactly these possible nonremovable poles. The boundary point zero
is removable, so it contributes no half residue. As in the
[paired rectangle, equation (10)](research_mixed_next_paired_meromorphic_rectangle.md),
\[
\operatorname*{Res}_{y=b/N}K_N=
\frac{F_N^{\rm mid}(w,r^b)C_{\beta,N}(r^b,Z)}
     {2\pi iP_b}.
\tag{6}
\]
The derivative \(2\pi iN\) of the denominator cancels the original
\(N\) in \(K_N\). Thus the residue sum has no additional \(N\).

Define the three horizontal corrections
\[
B_N^{\rm strip}=\int_{[a_0,c_N]+ih}K_N\,dy,\qquad
U_N^{\rm strip}=\int_{[a_0,c_N]+iH}K_N\,dy,\qquad
U_N^{\rm seam}=\int_{[0,s]+iH}K_N\,dy .
\tag{7}
\]
Here \(B_N^{\rm strip}\) is an integral, distinct from the integer
upper cutoff \(B_N\) in (1).

**Exact identity.**
\[
\boxed{\quad
\mathscr L_N=S_N^{\rm mid}-V_N(c_N)+V_N(0)
              -B_N^{\rm strip}+U_N^{\rm strip}+U_N^{\rm seam}.
\quad}
\tag{8}
\]
Indeed the counterclockwise boundary is bottom rightward, right
upward, top leftward, and left downward. Consequently
\[
\int_{[0,c_N]+ih}K_N-\int_{[0,c_N]+iH}K_N
                   =S_N^{\rm mid}-V_N(c_N)+V_N(0).
\]
Subtract the added lower strip, add the added upper strip, and
restore the missing top segment \([0,s]\). This proves (8).
It also fixes all signs without a phase branch or an asymptotic
approximation.

## 3. The three horizontal corrections and the short seam are paid

The [lower central theorem](research_mixed_next_complete_lower_plateau.md)
bounds the complete lower density at
\(q\in[.22,.23]\) with a fixed loss. Indeed \(\alpha=\Re y_*>.24\),
so its equation (11) has
\[
\min\{2\kappa(q-\alpha)^2,10^{-11}\}=10^{-11},
\qquad \kappa=1/2500000 .
\tag{9}
\]
Its Section 4 retains the entire old correction polynomial and
the denominator. Since \(|1-Y^N|\ge1/2\) on this unchanged
negative height, this pays \(B_N^{\rm strip}\), including the
original \(N\) in \(K_N\).

The [complete selected-segment theorem](research_mixed_next_complete_prefix_selected_segment.md)
and its old-filter
correction pay \(U_N^{\rm strip}\). The exact identity used there
is
\[
-K_N=\frac{N F_N^{\rm mid}d_NY^{-N}C_{\beta,N}}{1-Y^{-N}},
\qquad |1-Y^{-N}|\ge\frac12 \quad(\Im y=H)
\tag{10}
\]
for large \(N\). The source is pointwise bounded on all of
\(P+iH\), so it bounds every subinterval in (7); no conclusion
is inferred merely from a small integral over the whole plateau.
Upper seam-arc removal separately pays \(U_N^{\rm seam}\).
Its opposite sign in that older theorem does not affect its
absolute bound.

There is also a paid part of \(V_N(0)\). Put
\[
h_c=\max(h,-1/100),\qquad
V_N^{\rm deep}=
\begin{cases}
\displaystyle\int_{ih}^{-i/100}K_N(y)\,dy,&h<-1/100,\\
0,&h\ge-1/100 .
\end{cases}
\tag{11}
\]
Thus \(V_N(0)-V_N^{\rm deep}\) is the upward segment from
\(ih_c\) to \(iH\).

To bound that whole segment, use the filtered versions of
[lower radial seam](research_mixed_next_lower_radial_seam.md) on
\([-1/100,0]\) and
[upper radial seam](research_mixed_next_upper_radial_seam.md) on
\([0,H]\). Outside a fixed small interval \([-t,t]\) about
height zero, the lower identity in (1) and upper identity (10)
have denominator bounded below by \(1/2\). Their respective
complete filtered density bounds therefore pay those two pieces.
Choose \(t>0\) small enough that
[the removable-pole collar](research_mixed_next_filtered_meromorphic_seam.md),
Theorem 1, pays \(K_N(i\tau)\) for \(|\tau|\le t\).
That theorem uses actual pole cancellation and maximum modulus;
it does not divide a density estimate by zero. These three pieces
exhaust the segment from \(ih_c\) to \(iH\).

All these sources have actual ordinary-reference bounds, both
parities, all-real-color upper estimates and fixed normalized
outside jets. After shrinking common complete-color and
actual-output neighborhoods and absorbing polynomial factors,
they imply, for every fixed \(j,k\),
\[
\boxed{\quad
\partial_w^j\partial_z^k
\left[e^{-N\mathcal P_\beta^+(w,z)}
\{\mathscr L_N-S_N^{\rm mid}+V_N(c_N)-V_N^{\rm deep}\}\right]
       =O_{j,k}(e^{-10^{-13}N}).
\quad}
\tag{12}
\]
Paths, \(h,h_c\), and integer cutoffs stay fixed at each base
reference before these derivatives are taken. The all-real
version uses the complete-color action and the original real-color
derivative bounds. No outgoing halfweight is divided out on an
independent target plateau.

In particular the seam current is wholly paid when \(h\ge-.01\).
For deeper references, (11) remains unestimated. The radial tube
does not contain that whole interval.

## 4. Optional full-prefix form, justified by positive partial-band bounds

The main identity (12) retains the old filtered physical sum.
One may replace it by the full-prefix sum only using the following
explicit positive estimates, not smallness of a complete transformed
correction. Define
\[
S_N^{\rm full}=\sum_{b=0}^{n_N}
\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z),\qquad
A_N=\lceil23N/24\rceil .
\tag{13}
\]
The first-coordinate polynomial is literally
\[
R_N^{\rm node}(w,Y)=
\sum_{a=A_N}^{D}U_{0,N}(w,r^a)C_{1,N}(r^a,Y),
\tag{14}
\]
by [sectorwise first-end removal, equations (2)--(4)](research_mixed_three_four_next_sectorwise_first_end.md).
Since \(n_N<B_N\), cardinal interpolation in (1) gives exactly
\[
\begin{split}
S_N^{\rm full}-S_N^{\rm mid}
={}&\sum_{b=0}^{l_N}\frac{F_N(w,r^b)}{P_b}C_{\beta,N}(r^b,Z)\\
&+\sum_{\substack{A_N\le a\le D\\l_N<b\le n_N}}
\frac{U_{0,N}(w,r^a)C_{1,N}(r^a,r^b)C_{\beta,N}(r^b,Z)}{P_b}.
\end{split}
\tag{15}
\]
The first line is bounded by the sum of moduli in
[low physical interval, Theorem 1, equation (10)](research_mixed_next_low_physical_interval.md).
For the second line, equation (26) of the sectorwise first-end
theorem bounds the sum of moduli over the entire rectangle
\(a\ge A_N,\ 0\le b<N\) by rate \(11/6\). Every subset,
including exactly the one in (15), inherits this positive bound.
Its equations (27)--(28) give the corresponding actual normalized
gap and fixed derivatives. Thus (15) is paid on the same actual
ordinary neighborhoods, with a gap larger than that in (12).
This proves (12) with \(S_N^{\rm full}\) in place of
\(S_N^{\rm mid}\), if desired.

There is an exact original-coefficient form for (13). With
\(q_N=e^{\pi i/N}\), \(\kappa_N=q_N^{D^2/2}\), and
\(\ell_{b,N}(w)=(v(w)^TA_3^2)_b\),
[the lowered-word identity](research_mixed_next_lowered_word_dual_observation.md)
gives
\[
S_N^{\rm full}=
\frac1{\kappa_N^2N}\sum_{b=0}^{n_N}
       (-q_N)^b\ell_{b,N}(w)C_{\beta,N}(r^b,Z).
\tag{16}
\]
The factorial cancellation and the entire outgoing kernel remain
literal. This is not a new observation bound.

## 5. The remaining obligation

The low physical theorem pays only its fixed small interval
\(b\le\delta N\). The
[low-node coefficient family](research_mixed_next_low_node_family_packet.md)
also explicitly distinguishes its coefficient-index Fourier
packet from the outgoing Newton observation. Neither theorem
pays the retained band \(l_N<b\le n_N\) in (5), nor the
same signed band in (16).

The exact remaining object supplied by this reduction is
\[
\boxed{\qquad S_N^{\rm mid}-V_N(c_N)+V_N^{\rm deep}.\qquad}
\tag{17}
\]
A uniform strict bound for this signed combination below the
original \(\Re\mathcal P_\beta^+\), with its outside jets,
would pay the paired left remainder. Separate estimates for
its three terms are not required. Precisely, if the normalized
fixed jets of (17) are \(O(e^{-\xi N})\) for some uniform
\(\xi>0\), then (12) gives those of \(\mathscr L_N\) as
\(O(e^{-N\min\{\xi,10^{-13}\}})\). No such bound for (17)
is asserted here.
The current \(V_N(c_N)\) is not controlled by the paid endpoint
values at its top and bottom, and no vertical interpolation of a
signed source is assumed.

All residues and both original Fourier sectors remain in (8)--(17).
The theorem is an exact reduction with paid correction pieces,
not a whole next-transfer or arbitrary-short-filling conclusion.
