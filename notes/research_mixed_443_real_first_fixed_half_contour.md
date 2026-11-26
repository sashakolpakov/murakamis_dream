# Keeping the half-face contour on the missing real first arc

Private written alternative, 11 November 2026. This argument keeps
the first conditional contour chosen at the second coordinate
\(q=1/2\), while \(q\) moves to \(18/25\). The first conditional
phase need not have a critical point on this retained contour at
the new value of \(q\). Its rate, paired with the complete third
source, decreases. A separate finite upper contour pays the
sampling corrections.

The author has completed the full written readback and the direct
source checks. Independent full proof and direct-source review is
required before adoption. No frozen source or public document changes.

## 1. Objects, scope, and the comparison already available

Fix the actual reference of a positive three/four word beginning
with \(443\), of length at least four. Keep the original primitives,
endpoint coefficient, private heights, and affine action
\(\Lambda_{123}(z)\) of the complete half-face theorem. Write
\[
 a\in[1/2,7/8],\qquad q\in[1/2,18/25],\qquad
 z=b+ic_3,\quad b\in[11/50,9/20],\quad
 -13/200\le c_3\le17/250 .                         \tag{1}
\]
Put \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iq}\),
\(Z=e^{-2\pi iz}\), and retain the literal source
\[
 U_N(w,X)d_N(X)X^{-\nu N}C_{1,N}(X,Y)
                 d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z),
       \qquad \nu,\mu\in\{0,1\}.                       \tag{2}
\]
The notation is that of the complete core-pair theorem: the
\(C_{\epsilon,N}\) are the full sums through index \(N-1\),
\(U_N\) contains the complete coherent endpoint coefficient,
and \(d_N\) is the original polynomial Fourier weight.
There is no outgoing halfweight at the third, type-three, factor.

For the first conditional factor use
\[
 Q(s;a,q)=g(a+s)+g(q+s)-3g(s)-g(a)-g(q)+2\pi ias,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}).        \tag{3}
\]
All continuations below retain its original constants. Set
\[
 J(t)=\int_0^t\log(2|\sin\pi v|)\,dv,\qquad
 I_x(t)=J(x+t)-J(x),\qquad
 E_a(t;q)=I_a(t)+I_q(t)-3J(t),
\]
\[
 L(q)=E_{1/2}(1/8;q),\qquad \ell=3/40,\qquad
 h_U=\frac{\log2}{4\pi}.                              \tag{4}
\]
The function \(J\) is extended continuously and periodically.
In particular all real numerator zeros have their integrated
values in these definitions.

Let \(\mathcal A\) be the six-entry complete cap envelope at
real first input \(1/2\), defined in (3)--(5) of the complete
real-cap transport theorem. It includes its main, both real cuts,
both weighted horizontal rates, and the separate true-end constant.
That theorem bounds the complete cap on (1), with either first
weight, by \(\max\{\mathcal A,9/10\}\), up to any prescribed
positive rate allowance. The cap trial in Section 3 of the
selected-second real-first-arc proof gives
\(A_0>181/200>9/10\). Thus this ceiling is \(\mathcal A\).
No assertion that the main cap profile dominates its other five
entries is required.

Use the complete third envelope from Sections 3 and 7 of the
core-pair theorem. Its horizontal maxima are
\[
 B_\eta(q)=\max_{t\in I_q}\Re Q_0(t+i\eta;q,z),\qquad
 I_q=[1/8,\min(r_0,1-q-\varepsilon_3)],                 \tag{5}
\]
at the original third height \(h_3\), lower height \(-13/200\),
and upper height \(1/5\), with the appropriate sampling penalties.
Its other three carriers are the original half-face real-left,
half, and last rates. The third zero joins, all weighted sides,
and every physical row are bounded by this envelope. The two
fixed positive constants \(1/2-r_0\) and \(\varepsilon_3\)
can be chosen sufficiently small before \(N\).

The half-face and core-pair proofs give the following raw
comparisons, before finite summation.

* At \(q=1/2\), every cap entry paired with the first reference
  main maximum, first real-left carrier, and each third entry has
  a fixed positive surplus below \(\Lambda_{123}(z)\).
* On the entire interval (1), \(\mathcal A+L(q)\), paired with
  any entry of the complete third envelope, retains such a surplus.
* At first input \(a=1/2\), the first weighted upper horizontal
  at \(h_U\), its left side at \(t=1/8\), and its right side
  at \(r_0\), paired with that same complete third envelope,
  are paid with a positive surplus.

These are the profile statements in Sections 2--7 of the
core-pair proof and Section 7 of the half-face proof. They are
not inferred by dividing their final finite product bounds.

**Claim to be reviewed.** There is a fixed \(\epsilon>0\),
depending on the actual word, for which (2) is bounded by
\(CN^B e^{N(\Lambda_{123}(z)-\epsilon)}\), uniformly on (1),
both Fourier choices, both parities, and a fixed ordinary-color
disk about \(-2\). Fixed color derivatives satisfy the same
conclusion on smaller disks. Only this real first arc is asserted.

## 2. The fixed negative contour from the half face

The unit-incoming negative-shoulder theorem, extended to its
closed radius \(R=1\) in Section 7 of the half-face proof,
provides an original simple zero-lift critical point
\[
 s_*(a)=u_*(a)+ih_*(a),\qquad
 2/25<u_*(a)<1-a,
\]
\[
 \Theta(a)=Q(s_*(a);a,1/2),\qquad
 \Re\Theta(a)\le\Re\Theta(1/2)
 \le M_2:=\max_{1/8\le t\le r_0}
                      \Re Q(t+ih_2;1/2,1/2).           \tag{6}
\]
The critical point and all margins are uniform on the compact
first interval. We record explicitly that \(h_*(a)<0\).
On the real pre-incoming-wall interval, the original arguments give
\[
 \Im Q_s(t;a,1/2)=\pi(a+t-1)<0.
\]
Both shifted real arguments are between \(1/2\) and \(1\),
whereas \(0<t<1/2\). Hence \(\Re Q_{ss}<0\) at every
finite height. The imaginary derivative decreases with height,
so its zero at the critical point must lie below the real axis.

Choose a fixed small \(\varepsilon_1>0\), and put
\[
 r(a)=\min\{r_0,1-a-\varepsilon_1\}.                   \tag{7}
\]
The cuts enclose the compact critical family. At \(q=1/2\),
the source proof permits a fixed lower sampling height \(-T\)
below all \(h_*(a)\), with its weighted rate below
\(\Re\Theta(a)-1\). Its lower weighted sides decrease away
from their real cuts. Its two unweighted joins to \(h_*(a)\)
are bounded by their real cuts or by \(\Re\Theta(a)\), using
vertical convexity. The real right-cut profiles are uniformly
below the first left carrier, by the post-incoming-wall estimate
and continuity. Section 4 below supplies that estimate also for
the present larger outgoing interval.

For each fixed \(a\), retain this entire negative contour and
the real cuts (7) while \(q\) moves. In particular neither
\(h_*(a)\) nor the first cuts depend on \(q\).

## 3. Joint transport of every nonpositive-height first profile

First fix a first private point \(s=t+i\eta\), \(\eta<0\),
and retain any fixed lower sampling penalty. Write
\[
 D=|1-e^{-2\pi iq}|,\qquad
 N_2=|1-\rho e^{-2\pi i(q+t)}|,\qquad
 \rho=e^{2\pi\eta}\le1.
\]
The exact derivative is
\[
                  \partial_q\Re Q(s;a,q)=\log(N_2/D).
                                                               \tag{8}
\]
It is independent of the real incoming coordinate. It remains
valid beyond the outgoing numerator wall on the original lower
factorial continuation. Here the exact period multiplier has
zero upper exponential rate; it is still retained as a factor.

For \(\ell\le t\le1/2\) and \(q\le18/25<3/4\), the angle
\(q+t\) lies between \(q\) and \(2-q\). Thus its cosine
is at least \(\cos2\pi q\). Convexity in \(\rho\) reduces
\(N_2\le D\) to \(\rho=0,1\); the former uses \(D>1\).
On \(1/2\le q\le21/40\), the shifted interval is contained
in \([23/40,41/40]\). Its cosine is at least
\(-\cos(3\pi/20)>-9/10\), whence
\[
                         N_2^2<19/5<31/8.              \tag{9}
\]
For an elementary witness, \(3\pi/20>15/32\) and the alternating
cosine bound give
\(\cos(3\pi/20)<1-(15/32)^2/2+(15/32)^4/24<9/10\).

At any maximizing third point in (5), the paired-upper proof
gives, on this first outgoing interval,
\[
 N_3^2<81/20,\qquad D^2>159/40,
 \qquad (31/8)(81/20)<(159/40)^2.                       \tag{10}
\]
After \(21/40\), it gives \(N_3\le D\). For the third upper
line at \(1/5\), that last inequality holds everywhere. Its
moving right endpoint contributes a nonpositive motion term.
The locally Lipschitz envelope argument in that source therefore
proves, for every fixed strictly negative first private point,
\[
 \Re Q(s;a,q)+B_\sigma(q)
 \le \Re Q(s;a,1/2)+B_\sigma(1/2),                    \tag{11}
\]
where \(\sigma\) is any of the three third heights in (5),
independent of the first height \(\eta\). Fixed penalties may be added
to either side. For these strictly negative first heights its
fixed-point rate is smooth in \(q\), including across the outgoing
wall, so the stated envelope argument applies literally. To obtain
\(\eta=0\), take \(\eta\uparrow0\) in (11), using continuity
of the integrated logarithmic rates, uniformly on the compact
parameter family. This avoids a local Lipschitz assertion at the
real zero \(q+t=1\). The same limiting argument extends the
separate nonincrease from (8). This separate comparison pays the
third real-left, half, and last carriers, which are independent
of \(q\).

Consequently every first main point, both negative unweighted
joins, the lower horizontal, and both lower weighted sides retain
their half-face calibration when paired with the complete third
source. One first point is fixed while the third maximum is
transported; no assumption about a maximizing first point at the
new value of \(q\) enters (11). Taking its supremum afterward
is harmless. This is the reason no new conditional critical-point
theorem is needed on (1).

## 4. All physical rows outside the first cuts

The elementary unit-input comparison in the far-right physical
envelope proof gives
\[
 I_a(t)\le I_{1/2}(t)\quad(0\le t\le1/2).
                                                               \tag{12}
\]
For \(0<t\le1/8\), the derivative of \(E_{1/2}(t;q)\)
has exponential equal to
\[
 \frac{2\cos\pi t\,|1-e^{-2\pi i(q+t)}|}
                         {(2\sin\pi t)^3}>1.
\]
The incoming modulus exceeds \(9/5\), the outgoing modulus
exceeds \(4/5\), and the denominator cube is below
\((4/5)^3\). Thus every physical row below \(\ell\) is
bounded by the calibrated \(L(q)\).

Put \(\delta_a=1-a\). For every \(\delta_a\le t\le1\),
periodicity and the sine-binomial inequality give
\[
 I_a(t)=J(\delta_a)+J(t-\delta_a)\le J(t).
                                                               \tag{13}
\]
The proof is valid on the whole interval through \(t=1\):
\(J(t)-J(\delta_a)-J(t-\delta_a)\) vanishes at its two
endpoints and has derivative positive before
\((1+\delta_a)/2\), negative afterward. The full disk
numerator estimate of the boundary-strip proof and the elementary
one-numerator proof of \(M_1(0)<7/15\)
therefore give
\[
 E_a(t;q)\le-2J((1-t)/2)-2J(t)<7/15
                       \quad(\delta_a\le t\le1).       \tag{14}
\]
This pays all post-incoming-wall middle rows and the entire high
block. No physical termination is imposed on the off-grid source.

For clarity, a uniform positive reserve below \(L(q)\) follows
directly from
\[
 -3J(1/8)>93/200,\qquad I_{1/2}(1/8)>1/14,
 \qquad I_q(1/8)>-1/32.
\]
The first uses \(2\sin\pi v<2\pi v\), \(\pi<22/7\), and
\(\log(14/11)>6/25\). The second uses
\(2\cos\pi v>9/5\) and \(\log(9/5)>4/7\). The third uses
the outgoing modulus \(>4/5\) and \(\log(5/4)<1/4\).
Hence
\[
 L(q)>93/200+1/14-1/32>7/15.                            \tag{15}
\]
Uniform continuity pays the collar immediately before
\(\delta_a\) with part of this reserve. If the other right
cut \(r_0\) is active, its real collar up to \(\delta_a\)
has arbitrarily small length, since \(\delta_a\le1/2\).
Its rate also tends uniformly to the bound (14) as
\(r_0\uparrow1/2\). Thus every physical row outside (7)
is accounted for. The original zero-safe product upper bounds
apply with one arbitrary allowance through both true ends,
both parities, and every revived row.

## 5. The upper horizontal and the left weighted side

For \(0\le\eta\le h_U\), set \(p=e^{-2\pi\eta}\), so
\(1/\sqrt2\le p\le1\). At a private point before the incoming
wall, including the chirp in (3),
\[
 \partial_a\Re Q(t+i\eta;a,q)
   =\log\frac{|p-e^{-2\pi i(a+t)}|}{|1-e^{-2\pi ia}|}
   \le0,\qquad 0\le t\le1-a.                           \tag{16}
\]
Indeed \(\cos2\pi(a+t)\ge\cos2\pi a\), and the difference
of the denominator square from the numerator square is at least
\[
 (1-p)(1+p-2\cos2\pi a)\ge0,
\]
since \(\cos2\pi a\le1/\sqrt2\). The exact outgoing period
multiplier is independent of \(a\), so (16) also applies after
its wall. The same sampling penalty is kept on both sides.
Every upper profile may therefore be compared to the same
\((t,\eta,q)\) at incoming input \(a=1/2\).

The extra interval \(\ell\le t\le1/8\) causes no loss. At
\(a=1/2\), put \(\rho=e^{2\pi\eta}\in[1,\sqrt2]\).
Throughout this interval the squared own modulus is at most one,
whereas the two squared numerator moduli obey
\[
 |1+\rho e^{-2\pi it}|^2\ge2+\sqrt2>17/5,
 \qquad |1-\rho e^{-2\pi i(q+t)}|^2>4/5.               \tag{17}
\]
For the latter, \(q+t\in[23/40,169/200]\) has cosine
less than \(3/5\); use \(\cos(3\pi/10)<3/5\).
The squared private force exceeds \((17/5)(4/5)>1\).
Consequently each such profile increases in \(t\) to \(1/8\).
This includes all intermediate heights on the left weighted side.

Equations (16)--(17) compare the entire upper horizontal at
\(h_U\) to the already calibrated core upper horizontal, and
the left weighted side at \(\ell\) to its side at \(1/8\).
The comparison is made before multiplying the unchanged complete
third envelope. Its core proof retains the outgoing period
multiplier and its cancellation of the upper sampling penalty.

## 6. The upper right weighted side at the incoming wall

When \(r(a)=r_0\), (16) compares this side to the same core
right side at \(a=1/2\). Suppose instead that the right cut
approaches the incoming wall \(t=\delta_a\). We first bound
the continuous limiting rates at that wall; finite cuts follow
by uniform continuity with a prescribed allowance.

If \(q<a\), the outgoing wall is still to the right. At the
incoming wall and every positive height, the incoming cotangent
has real part zero, the outgoing cotangent has negative real
part, and the own cotangent has nonnegative real part. Thus
\(\Re Q_{ss}\le0\). The upper weighted rate is convex in
height and is bounded by its two endpoints. Its real endpoint
is paid by (14)--(15); its upper endpoint is paid by Section 5.
When the limiting wall lies in \([r_0,r_0+\varepsilon_1]\),
compare its upper endpoint to the core endpoint at \(r_0\) by
uniform continuity. This costs an allowance tending to zero with
\(\varepsilon_1\), and does not extend the core interval silently.

If \(q\ge a\), put
\[
 t=\delta_a\in[7/25,1/2],\qquad d=q-a\in[0,t-7/25],
 \qquad \rho=e^{2\pi\eta}\in[1,\sqrt2].
\]
The outgoing numerator has crossed its period. Its exact
multiplier has rate \(2\pi\eta\), cancelling the upper
sampling penalty. Define
\[
 A_\theta(\rho)=\arg(1-\rho e^{-2\pi i\theta})
                         \quad(0<\theta<1/2).
\]
On the resulting original folded phase the imaginary private
derivative is
\[
 I=\pi(1-2t)+A_d(\rho)-3A_t(\rho).                    \tag{18}
\]
The incoming argument is the pre-incoming-wall limit \(-\pi\);
the outgoing folded argument is positive. At \(d=0\), use
\(A_0(\rho)=\pi\) for \(\rho>1\). The weighted height
derivative is precisely \(-I\), not \(-I-2\pi\).

For \(d>0\), \(A_d(\rho)\ge\pi(1/2-d)\); its argument
increases with \(\rho\ge1\). For \(t\ge7/25>1/4\),
\[
 |\partial_t A_t(\rho)|
 =\frac{2\pi\rho(\rho-\cos2\pi t)}
              {1+\rho^2-2\rho\cos2\pi t}
 \le\frac{2\pi\rho^2}{1+\rho^2}\le\frac{4\pi}{3}.
\]
Integrating from \(A_{1/2}=0\) gives
\(A_t\le(4\pi/3)(1/2-t)\). These inequalities, including
the stronger value at \(d=0\), imply
\[
 I\ge\pi(2t-1/2-d)\ge\pi(t-11/50)\ge3\pi/50>0.
                                                               \tag{19}
\]
Thus this weighted side decreases with height and is paid by
its real endpoint. The prefold and folded upper rates have the
same continuous limit at \(q=a\), because the multiplier has
been retained. No equality of their uncorrected phase branches
is asserted.

The compact family of these integrated rates is uniformly
continuous through the numerator walls and height zero. Choosing
\(\varepsilon_1\) and the fixed right collar sufficiently
small therefore pays every actual upper right side by the same
endpoint comparisons, with a small fixed allowance. This step
does not use a pointwise derivative bound near a logarithmic zero.

## 7. Exact finite contours, allowances, and conclusion

The first interpolant is the literal normalized expression
\[
 T_N(s;a,q)=e^{2\pi iNas}\Pi_N(a+s)\Pi_N(q+s)
                         E_N(a)E_N(q)E_N(s)^3.          \tag{20}
\]
The joint global chart proves its physical row identity and
holomorphy across the positive numerator wall. Its exact period
identity is
\[
 \Pi_N(w+1)=(1-e^{-2\pi iNw})\Pi_N(w).                 \tag{21}
\]
The incoming argument stays strictly before its wall on the
actual first contour; only the outgoing numerator may cross.
All own and outer denominators stay in compact regular strips.

Choose inward half-grid versions of \(\ell,r(a)\). The exact
split-cotangent formula has its \(+N\) real zero-mode integral,
two horizontal sampling currents with coefficient \(N/(2i)\),
and all four weighted vertical halves. Move the zero mode to
the fixed \(q=1/2\) height \(h_*(a)<0\), retaining its two
oriented joins. The lower sampling height is \(-T\), and the
upper height is \(h_U\). Sections 2--3 pay every negative
current paired with the entire third envelope; Sections 5--6
pay every positive weighted current. Section 4 keeps all rows
outside the first cuts. The third factor uses its complete
prewall contour and physical groups from the core-pair proof.

Across the outgoing wall, (21) is never divided out. The finite
wall estimate in Section 5 of the core-pair proof applies to
(20): shift by a fixed short distance using its one-step product
recurrence, bound the regular starting factorial, and truncate
the logarithms only in the upper estimate of the finite product.
Uniform integrability of the finitely many logarithmic zeros
gives the continuous rate with any fixed allowance. This covers
the vertical sides at height zero as well as the two horizontal
continuations. It introduces no extra poles or omitted residues.

The complete cap has upper rate \(\mathcal A\). The first and
second full Fourier polynomials have upper rate zero on the
compact real arcs (1), since \(J(a),J(q)\ge0\); both monomials
in (2) have unit modulus. Every rate comparison above is made
before summing the finitely many currents and all physical rows.
Their counts, lengths, and original densities have polynomial
cost. Choose all fixed cuts first and spend their continuity,
factorial, and half-grid allowances inside the positive common
raw surplus described in Section 1. A fixed positive surplus
remains.

Finally the source is a polynomial of degree less than \(N\)
in its ordinary color. The elementary Chebyshev continuation
lemma extends the uniform real-color estimate to a sufficiently
small fixed disk about \(-2\), using less than the remaining
surplus. The other factors are retained constant multipliers;
none is divided out. Cauchy's formula gives fixed derivatives
on smaller disks. This proves the claim, subject to independent
review of the new comparisons and their direct-source bindings.

The argument supplies neither a lower bound nor a nonzero leading
coefficient. Its point is narrower: the missing real first arc
can be paid without continuing its conditional critical point
past the second half face.

## Direct sources

| Source | Direct implication | SHA-256 |
|---|---|---|
| research_mixed_443_core_first_complete_right_pair.md | original raw calibration, complete third source, finite upper currents and numerator-wall estimates | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_443_paired_upper_prewall_currents.md | third maximizing-index and joint derivative estimates, including moving endpoints | 9b851f2e88f14be3116be661d8377bae514c77c28fbe594011b5966acc4ea77e |
| research_mixed_443_complete_second_half_face.md | Section 7: complete half-face real-input source, closed-radius extension, and raw calibration | 11243b9bbf31c2ab1ec662fcb6b47f56f8017a8307f424b5bdf5efcf5d83079b |
| research_mixed_four_unit_incoming_negative_shoulder_source.md | half-face critical branch, all-height curvature, retained finite negative contours | 32ab90d92081f4741a48f295efe7b3af202ad29ca863e5e25a75b4109e26962f |
| research_mixed_initial44_complete_real_cap_transport.md | entire real cap with both first weights and six-entry half-face envelope | dd8d313e1e23240943421b6fbb340f28de769f46d2c0f98f3a4a749be20d4420 |
| research_mixed_complete44_second_selected_real_first_arc.md | Section 3: original cap trial above 181/200 | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_initial44_far_right_physical_envelope.md | unit-input comparison and sine-binomial inequality through the full row interval | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_boundary_strip_bounds.md | Section 2: full disk numerator ceiling, through every numerator zero | e288c5d0bcf77a073dbaa8bb2f27bd46ce208a56e63c8bd0e98dfdbbc8f8c6ff |
| research_elementary_one_numerator_rate_bound.md | complete elementary proof of M1(0)<7/15 | f2376d1732f241ef3214a413259615b56de935a7fde7ae17370e95f72dac4289 |
| research_mixed_conditional_contour_allowance.md | zero-safe all-row upper estimates with arbitrary fixed allowance | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_fourier_right_cap_joint_global_chart.md | exact interpolant, holomorphic numerator continuation and physical equality | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |
| research_mixed_fourier_weight_continuation.md | absolute full Fourier bound on compact real arcs | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | polynomial continuation from all real ordinary colors and fixed derivatives | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |

The author read the complete final proof and each of these thirteen
direct-source implications, and checked the source versions. The
one-numerator scalar estimate was read in its elementary proof,
without using its earlier numerical certification. No mathematical
numerical evaluation, saved-value arithmetic, test, import,
compilation, or frozen-source edit was used.
