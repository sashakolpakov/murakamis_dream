# The complete upper end and right-side currents of the outer cap

Research deduction, 8 November 2026. On the real incoming arc
\(1/2\le a\le7/10\), a real private cut at most \(49/100\)
pays every omitted upper physical cap row, both weighted right-side
currents, and the unweighted right connector to the actual cap height.
The proof uses the whole original endpoint coefficient throughout.

This is a source-sector theorem. It does not pay the entire upper or
lower horizontal alias, the left private source, or a full main path
through the cap saddle. No outer-cap asymptotic is inferred.
No numerical evaluation or earlier frozen-note edit is used.

## 1. Original source and previously proved own-action inputs

Retain the type-three cap, endpoint continuation and exact private row:
\[
\begin{gathered}
U_{0,N}(w,X)=\sum_{j=0}^{N-1}H_N(w,r^{-j})\frac{p_j(X)}{P_j},
\quad X=e^{-2\pi ia},\quad r=e^{-2\pi i/N},\\
P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
\mathscr A_N(e,a,w)=D_N(e)^{-1}C_N(e,w)
                          \frac{\Pi_N(a+e)}{\Pi_N(a)}.
\end{gathered}                                                     \tag{1}
\]
At \(e=j/N\), (1) is exactly the original physical cap row.
The ordinary color and every Newton term in \(H_N,C_N\) remain.
This is the chart and normalization of
[the original outer-cap contour](research_mixed_cap_outer_contour_reduction.md).

At \(w=-2\), use precisely
\[
 \Psi(e,a)=S(e)+J(a+e)-J(a)-i\pi ae,\qquad
 \mathcal T(a)=\Psi(e_*(a),a),\qquad M(a)=\Re\mathcal T(a).
                                                                    \tag{2}
\]
The [actual cap-path theorem](research_mixed_endpoint_actual_cap_path_bridge.md)
gives the original stationary branch \(e_*=E_*+ih_*\), with
\[
 .24<E_*<.45,\qquad -.06<h_*<0,\qquad E_*<v:=1-a.
                                                                    \tag{3}
\]
All branches and additive constants are original.
The [wrapped-row action comparison](research_mixed_cap_wall_action_gap.md)
proves a uniform positive gap between \(M(a)\) and
\(h(v)=\Re S(v)+J(v)\). It pays the complete wrapped positive
row sum \(j/N\ge v\) and a fixed sufficiently small real collar
before that wall. Also, on
\[
 .24\le\Re e\le.5,\qquad -.06\le\Im e\le0,
\]
it proves \(-\Re S''(e)>0\). Thus on the prewall portion
\[
 -\Re\Psi_{ee}(e,a)
       =-\Re S''(e)-\pi\Re\cot\pi(a+e)>0.                      \tag{4}
\]
The complete endpoint packet on
\([.27,.49]+i[-.06,.04]\), with a fixed complex neighborhood,
is supplied by
[the deeper endpoint rectangle](research_mixed_endpoint_cap_rectangle_deeper_extension.md).
No larger endpoint source rectangle is assumed.

## 2. The old upper cut remains paid until it reaches the wall

**Lemma 1.** For \(1/2\le a\le51/100\),
\[
                 G_{49}(a):=M(a)-\Re\Psi(49/100,a)>0.
                                                                    \tag{5}
\]
On the open interval before \(a=51/100\), in fact
\(G_{49}'(a)>\log3\).

*Proof.* Critical stationarity gives the original envelope derivative
\[
 \mathcal T'(a)
  =J'(a+e_*)-J'(a)-i\pi e_*.
\]
Consequently, before the upper cut reaches the real wall,
\[
 G_{49}'(a)
  =\log\frac{|\sin\pi(a+e_*)|e^{\pi h_*}}
                          {\sin\pi(a+49/100)}.                 \tag{6}
\]
In particular the signed term \(\pi h_*\) has not been omitted.

By (3), \(a+E_*\in(.74,.96)\), so
\[
 |\sin\pi(a+e_*)|\ge\sin\pi(a+E_*)>\sin(\pi/25)>3/25.
\]
The last inequality is the original sine chord
\(\sin(\pi s)\ge3s\) for \(0\le s\le1/6\), strict here.
Also \(e^{\pi h_*}>4/5\), since
\(3\pi/50<1/5<2/9<\log(5/4)\).
The real cut has
\[
       0<\sin\pi(a+49/100)\le\sin(\pi/100)<4/125 .
\]
Substitution in (6) gives a ratio greater than three.

The complete half-cap proof, equation (24), already gives
\(G_{49}(1/2)>0\) with its original action and real cut.
Integrating the just-proved derivative preserves that gap.
At \(a=51/100\), the logarithmic derivative is singular, but its
primitive and both actions are continuous. The continuous limit
therefore preserves the same positive gap. \(\square\)

No finite sum or source value is evaluated in this comparison.

## 3. One cut pays every upper physical row

Choose a fixed \(\delta>0\) small enough that
\[
 \delta<1/100,\qquad
 \delta<\tfrac12\min_a(1-a-E_*(a)),
\]
and that the entire real collar \(v-\delta\le e\le v\)
has the strict own-action bound from the wrapped-row theorem.
Define the continuous proof cut
\[
                         b(a)=\min\{49/100,v-\delta\}.           \tag{7}
\]
Then \(.29<b(a)\le.49\), \(E_*<b(a)\), and
\(a+b(a)\le1-\delta\). These inequalities have uniform strict
reserves except at the stated harmless closed endpoints.

If \(b(a)=v-\delta\), its upper physical tail is exactly the paid
collar followed by the wrapped sector. If \(b(a)=.49\), then
\(a<.51\). The additional compact prewall rows
\(.49\le e\le v\) have the original complete-coefficient rate
\[
                 R(e,a)=\lambda(e)+J(a+e)-J(a),
                 \qquad \lambda(e)=\Re S(e).                  \tag{8}
\]
This is the physical \(H_N\) estimate in
[wrapped-row transport](research_mixed_cap_wrapped_row_transport.md)
and its cited whole-real-color source; it is not an extrapolation
of a complex-index packet.

The real curvature in (4) gives \(\lambda'(e)<\lambda'(.35)\)
on this interval. The already printed saved scalar consequence in
[the bridge phase floor, equation (17)](research_mixed_endpoint_bridge_phase_floor.md)
is \(\lambda'(.35)<1/200\), without any new replay.
Furthermore
\[
 J'(a+e)\le\log(2\sin(\pi/100))
               <\log(8/125)<-\log3<-1.
\]
Thus \(R_e<1/200-1<0\) before the wall. Integrating through its
logarithmic endpoint shows \(R(e,a)\le R(.49,a)\).
Lemma 1 pays that last rate. All rows after the wall are already
paid by the wrapped-row theorem, including the true upper endpoint.

**Proposition 2.** There is a uniform \(\gamma>0\) such that
\[
 \sum_{\substack{0\le j<N\\j/N\ge b(a)}}
 \left|H_N(w,r^{-j})\,p_j(e^{-2\pi ia})/P_j\right|
            \le C N^B e^{N\{M(a)-\gamma\}}
                                                                    \tag{9}
\]
for every real ordinary color \(w\in[-2,2]\) and both level
parities. All numerator zeros and original coefficients are retained.

Indeed the compact physical coefficient and zero-safe product
bounds apply to (8), and the wrapped theorem supplies the remaining
rows and its separate true-end estimate. Each fixed positive reserve
can absorb the chosen uniform factorial tolerance and polynomial row
count. The same bounds hold on a sufficiently small fixed complete-color
disk with a prescribed further allowance. Markov applied to each whole
endpoint polynomial before the positive sum gives fixed real ordinary
derivatives, and Cauchy gives the corresponding local complex derivatives.

## 4. The entire right side of the retained contour

At a fixed base \(a\), set
\[
 K_N(a)=\lceil Nb(a)\rceil,\qquad
                   b_N=(K_N(a)-1/2)/N.                        \tag{10}
\]
The retained private indices lie below \(K_N(a)\).
For all sufficiently large \(N\), the real cut \(b_N\) and
every point \(b_N+i\sigma\), \(-3/50\le\sigma\le1/25\),
lie in the fixed neighborhood of the proved deeper endpoint
rectangle. Also \(a+b_N<1-\delta/2\), so the incoming
factorial stays in its regular original strip.
These assertions include the possible \(O(N^{-1})\) excursion
past real part .49; no macroscopic extension past .49 is made.

The real cut has a uniform own-action gap by Sections 2--3
and zero-safe continuity. The complete endpoint packet, not a
local saddle contribution alone, gives the rate
\(\Re\Psi(b_N+i\sigma,a)\) for the exact current (1).

First take the limiting cut \(b=b(a)\).
Horizontal concavity (4) from \(e_*\) to \(b+ih_*\)
gives a strict uniform gap at that main-height endpoint.
This phase comparison is legitimate on the whole segment:
the original endpoint branch there is in the bridge phase
domain, and \(a+\Re e<1\). It does not claim a finite
endpoint packet at every point of that horizontal segment.
The actual current endpoint \(b+ih_*\) itself is in the
proved deeper source rectangle.

Along the vertical side at \(b\), (4) makes
\(\Re\Psi(b+i\sigma,a)\) strictly convex for \(-.06\le\sigma\le0\).
Both the real endpoint and the endpoint at \(h_*\) are paid.
The entire unweighted right connector
\[
                       b+ih_*\longrightarrow b
\]
therefore lies below the own action with a uniform gap.
The same conclusion holds at \(b_N\) by continuity.

For both weighted side halves, use the original derivative
\[
 \Psi_e=-J'(e-u_c(e))+i\pi u_c(e)+J'(a+e)-i\pi a.                \tag{11}
\]
On the deeper rectangle, the original endpoint chamber has
\(0<\Re u_c<\Re e<1/2\) and \(0<\Re(e-u_c)<1/2\),
for both signs of the permitted height. Each sine logarithm
in (11) has imaginary part in \((-\pi/2,\pi/2)\). Hence at
the limiting cut
\[
                 -17\pi/10<\Im\Psi_e<99\pi/100.                \tag{12}
\]
For the upper side, subtract its exact alias penalty \(2\pi\sigma\):
its derivative is \(-\Im\Psi_e-2\pi<-3\pi/10\).
For the lower side \(\sigma\le0\), the derivative of the
penalized rate \(\Re\Psi+2\pi\sigma\) is
\(-\Im\Psi_e+2\pi>101\pi/100\).
Both weighted sides therefore have their maximum at their
already-paid real cut. Slightly weaken these strict constants
at \(b_N\), if needed.

The original cotangent decomposition supplies kernel bounds
\(2e^{-2\pi N|\sigma|}\) on this half-grid side and retains
the density \(+N\). Thus the complete weighted right-side
currents over \([-3/50,0]\) and \([0,1/25]\), and the full
unweighted right connector to height \(h_*\), have bounds
\[
                       C N^B e^{N\{M(a)-\gamma_R\}}
                                                                    \tag{13}
\]
for some uniform \(\gamma_R>0\).
Their orientations and the original scalar are those of (1)
and the exact outer-cap contour identity. No endpoint coefficient
has been divided out, and no current has been replaced by a
sampled value.

The contour estimate (13) is at complete ordinary color and
on a fixed sufficiently small complex complete-color neighborhood,
with all fixed mixed derivatives. It does not assert a
nonzero packet or the same contour rate at remote real colors.
At each base point hold the integer cut and paths fixed before
varying parameters; strict source gaps persist, and Cauchy's
formula applies to the locally normalized currents.
No derivative of the moving minimum or ceiling is taken.

## 5. Exact completed and remaining source groups

The new cut (7) and the proved endpoint source suffice for:

* every physical private row at or above the cut, including the
  original true end and all wrapped rows;
* the real upper cut and both complete weighted right-side halves;
* the unweighted right join between the real cut and actual
  cap critical height.

These estimates do not use a prescribed lower real cut or
a complete main path from the left. The two entire horizontal
aliases, the lower physical sector, the left weighted sides and
unweighted join, and the source-valid main bridge to the actual
saddle still require their own comparisons. In particular an
endpoint packet on a curved auxiliary-real locus does not by
itself pay an outer cap path on that locus.
The present theorem preserves the whole cap and exact current
inventory while closing only the specified upper-end groups.

