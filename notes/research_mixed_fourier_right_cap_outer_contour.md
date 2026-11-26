# An exact factorial chart for the outgoing Fourier-cap contour

Research deduction, 7 November 2026. The original cardinal coefficient
has a second exact interpolation on the central outgoing strip. It
uses the remaining finite factorial product, so it permits a tall
outgoing contour without crossing the unit-disk boundary of the older
Pochhammer series. Its action, leading symbol and lattice values are
unchanged. This pays the central outgoing aliases and reduces all
central joins to physical real faces and the original main plane.

Two elementary monotonicities also clip the outer physical tails.
The remaining real-face comparisons and one explicitly retained
physical wedge are not bounded by the main plane here. This is an
actual finite-source reduction, not a whole right-cap theorem. No
numerical evaluation or certificate replay is used.

## 1. The literal source and a different exact cardinal interpolation

Keep the source and actual reference of the
[bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md).
Write
\[
 r_N=e^{-2\pi i/N},\quad P_j=(r_N;r_N)_j,\quad
 X=e^{-2\pi ia},\quad Y=e^{2\pi iy},\quad y=x_0,
 \qquad \rho=|Y|.
 \tag{1}
\]
The original Fourier cap is exactly
\[
 V_N^{\rm F}(y,X)=
 \sum_{\substack{j,l\ge0\\j+l<N}}
 \frac{X^{-j}p_j(X)P_{j+l}}{P_j^3P_l}\,f_l(y),
 \qquad
 f_l(y)=\frac{e^{-\pi i(N-1)y}}N
     Y^l\prod_{k=l+1}^{N-1}(1-Yr_N^k).
 \tag{2}
\]
Thus the triangular support, the factor \(1/N\), the lifted
Fourier scalar and both level parities are retained. No additional
outside power of \(N\) or crossing scalar is inserted.

Use the negative-root factorial
\[
 \Pi_N(z)=G_N(Nz)
    \exp\!\left\{\frac{\pi i}{2}[N(z-z^2)-z]\right\},
 \quad
 \frac{\Pi_N(z+1/N)}{\Pi_N(z)}
       =1-e^{-2\pi i(z+1/N)}.
 \tag{3}
\]
Here \(G_N\) is the original
[exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md).
It is holomorphic and nonzero for \(0<\Re z<1\), at every
finite imaginary height. The recurrence and marks in (3) are also
recorded in the
[localized exact-current construction](research_mixed_localized_current_remainder_transport.md),
equations (2)--(3).

For \(0<\Re(q-y)<1\), define
\[
 \widehat f_N(q;y)=\frac{e^{-\pi i(N-1)y}}N
 e^{2\pi iNyq}\,
 \frac{\Pi_N(1-y-1/N)}{\Pi_N(q-y)}.
 \tag{4}
\]
For the fixed \(y=x_0\), the numerator argument also has real
part strictly between zero and one, for every \(N\ge2\).
At every physical \(q=l/N\) in this strip, the recurrence gives
\[
 \frac{\Pi_N(1-y-1/N)}{\Pi_N(l/N-y)}
       =\prod_{k=l+1}^{N-1}(1-Yr_N^k).
 \tag{5}
\]
Consequently \(\widehat f_N(l/N;y)=f_l(y)\) exactly.
Outside this strip all physical coefficients in (2), including
\(l=0\), remain their original finite products. No analytic
extension of (4) to such endpoints is asserted.

The central outgoing interval is
\(P=[11/50,9/20]\). Since
\(.18299<\Re y<.18301\), its difference from \(\Re y\)
is a fixed compact subinterval of \((0,1)\). Formula (4) is
therefore legal on every fixed-height rectangle over \(P\),
including the outgoing heights used below.

To fix the action and symbol, put
\[
 A(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}.
\]
The original marked factorial expansion is
\(\Pi_N(z)=N^{1/2}A(z)e^{Ng(z)}(1+O(N^{-1}))\).
Using the exact recurrence once at the numerator of (4) proves
\[
 \widehat f_N(q;y)=\frac1N
 \frac{e^{\pi iy}}{\sqrt{(1-Y)(1-Ye^{-2\pi iq})}}
 e^{N\ell_q(y)}(1+O(N^{-1})),
 \tag{6}
\]
where the square roots are continued from the original central
domain, and now
\[
 \ell_q(y)=2\pi iy(q-\tfrac12)+g(1-y)-g(q-y).
 \tag{7}
\]
On the old lower-height domain, the unit-disk dilogarithm formula
for \(g\) makes (7) exactly the old cardinal phase. Analytic
continuation in the regular strip fixes the same branch everywhere
in (4). Its coefficient in (6) is likewise the old coefficient:
\(A(1-y)/A(q-y)=\sqrt{(1-Y)/(1-Ye^{-2\pi iq})}\).
Thus no additive action constant or leading density is changed.

This does not assert equality of two off-grid interpolations chosen
by their lattice values. Rather, (4)--(5) give an independently
specified exact interpolation of the same finite rows; (6)--(7)
prove its calibrated expansion. Every fixed derivative of the
normalized expansion is uniform on smaller compact neighborhoods.

## 2. An outgoing derivative strip at every finite height

Keep the original allocated phase
\[
 \begin{split}
 F_\eta(s,a,q)&=g(s+a)+g(s+q)-3g(s)
       -(1+\eta/2)g(a)-g(q)+2\pi ias+\ell_q(y),\\
 &\eta\in\{0,1\},\qquad
 \Re s\in[1/8,1/2],\quad \Re a,\Re q\in P .
 \end{split}
 \tag{8}
\]
The incoming height is its actual value, \(|\Im a|\le.108\),
and is negative when \(\eta=1\). The two contour heights may
vary independently in any fixed finite intervals. Every factorial
argument in (8), including \(q-y\), stays in its original regular
strip.

**Lemma 1.** On this domain,
\[
       -\frac{39\pi}{25}<\Im F_{\eta,q}
                                  <\frac{17\pi}{25}.
 \tag{9}
\]

*Proof.* Let \(v=\Re s\), \(z=\Re q\), \(\xi=\Re y\).
The exact derivative is
\[
 F_{\eta,q}=g'(s+q)-g'(q)-g'(q-y)+2\pi iy.
 \tag{10}
\]
For an original regular argument with real part \(u\in(0,1)\),
the imaginary part of \(g'\) lies between zero and
\(\pi(1-2u)\), at every finite height, with the endpoints
ordered according to the sign of \(1-2u\). This follows by
moving the radius in \(1-re^{-2\pi iu}\), without changing
its original logarithmic lift.

Here \(z\) and \(z-\xi\) lie in \((0,1/2)\). If
\(v+z\le1/2\), the lower bound from (10), divided by
\(\pi\), is \(-2+4z\ge-28/25\); if \(v+z\ge1/2\),
it is \(-1-2v+2z\ge-39/25\). The two upper bounds are
\(1-2v-2z+2\xi<17/25\) and \(2\xi<17/25\).
The limiting argument bounds are strict at finite radii whenever
needed at an extremum. This proves (9). \(\square\)

The inner derivative retains its old all-height strip
\[
      -49\pi/25<\Im F_{\eta,s}<121\pi/100 .
 \tag{11}
\]
The four-case argument proof in the
[own-four left-cut theorem](research_mixed_four_left_cut_extension.md),
equation (17), uses only these real ranges and the original chirp;
it does not require the other index's height to be small.

Choose the fixed central contours
\[
 s:\ [-1/5,5/4],\qquad q:\ [-1/5,1/2]
 \tag{12}
\]
in imaginary height. Let \(h_s,h_q\in[-.102,-.001]\) be
the actual critical heights. Uniformly for every
\(h\in[-.102,0]\), (9) gives
\[
 \begin{split}
 \Re F_\eta(s,a,z-i/5)-2\pi/5
     &<\Re F_\eta(s,a,z+ih)-33\pi/125,\\
 \Re F_\eta(s,a,z+i/2)-\pi
     &<\Re F_\eta(s,a,z+ih)-761\pi/12500.
 \end{split}
 \tag{13}
\]
For example the upper increment is at most
\(\{(39/25)(1/2+.102)-1\}\pi=-761\pi/12500\).
These inequalities allow every fixed inner contour height in (12).
Once the outgoing height is in \([-.102,0]\), the old inner
alias comparison applies with its own base height anywhere in that
same interval. Its smaller reserve is \(7/50\). Both reserves
in (13) exceed \(7/50\), using only \(\pi>3\).

Both (9) and (11) lie strictly inside \((-2\pi,2\pi)\).
Consequently a penalized vertical coordinate can always be reset
to height zero without increasing
\(\Re F_\eta-2\pi\sum|\Im z_j|\). The real endpoint
marker of that coordinate is retained during this reset.

## 3. Every central alias and join reduces to a physical face

Put
\[
 C=[1/8,1/2]\times P,
 \quad
 E_\partial(a)=\max_{(s,q)\in\partial C}\Re F_\eta(s,a,q),
 \tag{14}
\]
where \(s,q\) are real in this definition and \(a\) keeps
its actual height. The boundary is the union of all four closed
real faces, with their complete free-coordinate intervals.

At the actual reference \((s_*,a_*,q_*)\), define the original
\(M_\eta,p_\eta\) as in the bare inner-contour theorem, and let
\[
 B_\eta(a)=M_\eta+p_\eta(\Re a-\Re a_*)
                   -\frac\mu2(\Re a-\Re a_*)^2,
 \qquad \mu=1/1250000.
 \tag{15}
\]
The joint main-sheet bound already proved there is
\[
 \Re F_\eta(s+ih_s,a,q+ih_q)
 \le B_\eta(a)-\frac\mu2
       \{(s-\Re s_*)^2+(q-\Re q_*)^2\}.
 \tag{16}
\]
Since \(\Re s_*,\Re q_*\in[.24,.36]\), each real
central face in (16) has loss at least
\[
                    \delta_C=\mu/5000>0.
 \tag{17}
\]
No value of \(E_\partial\) relative to \(B_\eta\) is
asserted here.

The exact central row is obtained from (2) by replacing
\(p_j(X),P_{j+l}/P_l,P_j\) by their ratios of \(\Pi_N\),
and \(f_l\) by (4). In particular it is exactly
\[
 T_N(s,q;a,y)=e^{2\pi iNas}
  \frac{\Pi_N(s+a)\Pi_N(s+q)}
       {\Pi_N(a)\Pi_N(q)\Pi_N(s)^3}\,
                                      \widehat f_N(q;y).
 \tag{18}
\]
It matches the physical rows of (2) throughout \(C\).
All arguments in (18) are regular on the whole product (12).
Its row power is \(N^{-5/2}\); the exact two-index residue
formula has coefficient \(+N^2\) for the zero mode. Incoming
\(|d_N(X)|^{\eta/2}\) is handled as a separate nonnegative
modulus, with rate \(-\eta\Re g(a)/2\) on the specified
unselected incoming family. No finite halfweight is divided out.

**Proposition 2.** Write \(I_N^*(a,y)\) for the exact
zero-mode current of (18) on the actual two critical-height lines.
For every \(\tau>0\), the difference between the central physical
sum and this current, multiplied by its incoming halfweight, is
bounded by
\[
 C_\tau N^{A_\tau}
 \exp N\{\max(E_\partial(a),B_\eta(a)-\delta_C)+\tau\}.
 \tag{19}
\]
The current itself has upper rate \(B_\eta(a)+\tau\).

*Proof.* Use the exact
[regrouped residue identity](research_exact_vertical_current_regrouping.md)
with zero-mode height zero in each coordinate, retaining its signed
vertical subtraction before taking a modulus. There are fifteen
nonmain tensor products before splitting vertical sides.

If a product contains a vertical factor, use (9), (11) to reset
all its penalized heights to zero. It is then bounded by the
real face marked by that factor, hence by \(E_\partial\).
If both factors are horizontal aliases, first apply (13), then
the old inner alias comparison; (16) bounds the result with a
strict reserve at least \(7/50\).

If exactly one coordinate is an alias and the other is a real
zero-mode integral, translate the latter to its critical height.
Its horizontal part is treated by the same alias comparisons.
On either joining side, write the translated height as
\(\theta h_j\), \(0\le\theta\le1\). Compare the aliased
coordinate with \(\theta h_k\), using (13) if it is outgoing,
or the old inner alias estimate if it is incoming. The remaining
phase is now on the common-height path
\((\theta h_s,\theta h_q)\), on one real face.

The original joint negative Hessian has floor \(\mu\) throughout
these common-height paths: the bare ordinary bound applies, and
the cardinal adds positive horizontal curvature since \(q_R\in P\)
and \(\theta h_q\le0\). Therefore the real phase is convex in
\(\theta\). Its maximum is at the real face or the critical-height
face, bounded respectively by \(E_\partial\) and
\(B_\eta-\delta_C\). The same convexity controls all joining
faces when the double real zero mode is translated simultaneously
to \((h_s,h_q)\). No mixed, independently reset zero-mode corner
is silently discarded.

This covers every central tensor current, including all vertical
and joining terms. Half-grid cuts differ from the stated cuts by
\(O(N^{-1})\); uniform factorial symbols absorb that perturbation
and all prefactors in the single prescribed tolerance. Every
identity retains both parities. \(\square\)

## 4. Two monotone physical-tail reductions

On the supported real triangle \(s,q\ge0\), \(s+q\le1\),
write the original allocated physical rate as
\[
 \begin{split}
 E_\eta(s,q;a)={}&I_a(s)+J(s+q)-J(q)-3J(s)-2\pi h_a s\\
 &-\frac\eta2\Re g(a)+\Re\ell_q(y),\qquad
 I_a(s)=\int_0^s\log|1-e^{-2\pi i(a+t)}|\,dt.
 \end{split}
 \tag{20}
\]
Integrable zeros are retained. The original zero-safe finite-product
bounds give this rate, with logarithmic endpoint errors and an
arbitrarily small uniform tolerance, for every physical row of (2).
The original root-Pochhammer expansion remains valid for the
physical \(q\)'s over \([0,1]\), since \(|Y|<1\).
No off-grid use of (4) outside its strip is involved.

For interior supported rows,
\[
 \partial_q E_\eta
 =\log\frac{\rho\sin\pi(s+q)}
                {\sin\pi q\,|1-Ye^{-2\pi iq}|}.
 \tag{21}
\]
This derivative is independent of the incoming leg and allocation.

**Lemma 3.** Throughout \(q\ge9/20\),
\[
                 \partial_q E_\eta<-\log(7/5).
 \tag{22}
\]
Hence every such physical row is bounded by its value on \(q=9/20\),
with at least \((q-9/20)\log(7/5)\) additional loss.

*Proof.* For \(9/20\le q\le1/2\), the rotated angle
\(2\pi(q-\Re y)\) lies between \(\pi/2\) and \(\pi\),
so \(|1-Ye^{-2\pi iq}|>1\). Also
\(\sin\pi q\ge\cos(\pi/20)>49/50\). The ratio in (21)
is thus less than \(125/196<5/7\).
For \(1/2\le q\le1\), support gives
\(\sin\pi(s+q)\le\sin\pi q\). On this interval
\(\cos(2\pi(q-\Re y))\le\cos(2\pi\Re y)<21/50\).
Consequently
\[
 |1-Ye^{-2\pi iq}|^2-\frac{49}{25}\rho^2
 >1-\frac{21}{25}\rho-\frac{24}{25}\rho^2
 \ge\frac1{10}>0,
 \tag{23}
\]
using \(\rho\le5/8\). This proves (22). Decreasing \(q\)
preserves the original triangular support. Integrate and extend to
its closed boundary by continuity. \(\square\)

**Lemma 4.** If \(1/8\le s\le1/2\) and \(0<q\le11/50\),
then \(\partial_qE_\eta>\log(6/5)\). If instead
\(0<s\le1/8\) and \(0\le q\le11/50\), then
\(\partial_sE_\eta>4/25\).

*Proof.* For the first assertion, the sine ratio in (21) is at least
\[
 \min\{\cos(\pi/8)+\sin(\pi/8)\cot\pi q,\ \cot\pi q\}.
 \tag{24}
\]
When \(q\le1/10\), use
\(\cot(\pi/10)>3\), \(\cos(\pi/8)>9/10\),
\(\sin(\pi/8)>3/8\). Thus (24) exceeds \(81/40\).
The original \(\cos(2\pi\Re y)>2/5\) gives
\(|1-Ye^{-2\pi iq}|^2<1+\rho^2-(4/5)\rho<1\).
The ratio in (21) exceeds \(243/200>6/5\).

For \(1/10\le q\le11/50\), the rotated angle has modulus
less than \(53/100\), so its cosine exceeds \(17/20\).
The function \(1+\rho^2-(17/10)\rho\) decreases on
\([3/5,5/8]\), and is \(17/50<(3/5)^2\) at its left
endpoint. Hence the cardinal factor \(\rho/|1-Ye^{-2\pi iq}|\)
exceeds one. Meanwhile
\(\cot(11\pi/50)>77/64>6/5\), and (24) exceeds \(6/5\).
For an exact elementary witness to the cotangent bound, put
\(t=121/175>11\pi/50\) and use
\[
 1-t^2/2+t^4/24-t^6/720>77/100,
 \qquad t-t^3/6+t^5/120<16/25.
 \tag{25}
\]
These are rational comparisons of the alternating Taylor bounds.

For the low-index assertion, \(s+q\le.345<1/2\), so
\(\sin\pi(s+q)\ge\sin\pi s\). Direct differentiation gives
\[
 \partial_s E_\eta
 \ge\log\frac{|\sin\pi(a+s)|}{2\sin^2\pi s}-\pi h_a
 >\log(15/8)-.108\pi>4/25.
 \tag{26}
\]
Indeed \(\Re(a+s)\in[.22,.575]\), so its sine modulus
exceeds \(3/5\), while \(\sin(\pi/8)<2/5\).
Finally \(\log(15/8)>1/2\) and \(.108\pi<17/50\).
All these are elementary rational/Taylor inequalities. \(\square\)

Thus every low-outgoing physical row with \(s\le1/2\) can
first raise a low \(s\) to \(1/8\), and then raise \(q\)
to \(11/50\). Both moves preserve support and the low-outgoing
marker until it reaches that real face. What remains from the
low-outgoing region is the genuine original wedge
\[
             0\le q<11/50,\qquad 1/2<s\le1-q.
 \tag{27}
\]
It is not removed by Lemma 4.

## 5. The remaining whole-source comparisons

The source (2) is the central physical sum plus its literal
supported real complement. Proposition 2 settles its central
aliases and joins once that physical complement and its real
boundary faces are paid. Lemmas 3--4 simplify the complement but
do not prove its calibrated sign.

For \(q\in P\), the old complete
[real-row tail theorem](research_mixed_right_tail_endpoint_bound.md)
and left monotonicity still reduce the inner physical tails to
the rates at \(s=1/8,1/2,1\), with \(q\) real. The last
rate means its original zero-safe extended row bound; it does not
revive a forbidden physical row. The high-outgoing tail in Lemma 3
lands on \(q=9/20\), including the full supported inner interval
there. The low-outgoing tail lands on \(q=11/50\) except for
(27). Consequently it suffices to compare those three real-inner
profiles, the two real outgoing faces, and the retained wedge
with the same original \(B_\eta(a)\).

These are physical-height comparisons. Bounds for the three inner
profiles at the negative critical outgoing height cannot be
substituted for them without a proved transport or coherent
replacement. Conversely, a proof controlling the original full
physical complement would require no additional outgoing alias
or joining families under the present factorial chart. A whole
right-cap asymptotic, global boundary contraction and knot-invariant
lower bound remain separate until those comparisons are proved.
