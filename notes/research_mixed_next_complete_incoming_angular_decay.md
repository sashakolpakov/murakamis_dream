# Decay over the full incoming-color interval for the complete three-block transfer

Research proof, 9 November 2026. The complete \(343\) transfer is
exponentially smaller away from complete incoming color, with its
outgoing coordinate fixed at an eligible geometric reference.
The proof uses the full incoming-color bounds for both remainders
and the angular loss of the already completed \(34\) prefix.
This supplies a global estimate in one boundary variable. The
remaining outgoing composition and closing sums are separate.

## 1. Statement with the original normalization

Fix a complete word in powers three and four, beginning \(343\),
with at least five vertices. Keep its original geometric reference
and let \(z_*=t_3^*\), \(y_*=t_2^*\), and \(s_*=s_3^*\).
Write \(Z_*=e^{-2\pi iz_*}\). For \(r=e^{-2\pi i/N}\) and
\(P_b=(r;r)_b\), the full three-block transfer is
\[
 T_N(w,z_*)=\sum_{b=0}^{N-1}
       \frac{F_{34,N}(w,r^b)}{P_b}C_{0,N}(r^b,Z_*),
 \qquad
 C_{0,N}(Y,Z)=\sum_{j=0}^{N-1}
       \frac{Y^{-j}(rY;r)_j(rZ;r)_j}{P_j^2}.
 \tag{1}
\]
All factors and their normalizations are those of the
[complete two-variable theorem](research_mixed_next_transfer_complex_neighborhood.md).
In particular both original Fourier sectors are present in (1).
Set
\[
 P(w,z)=\mathcal P_0^+(w,z),\qquad
 \Lambda_*=\Re P(-2,z_*),\qquad
 Q_N(\theta)=T_N(-2\cos\theta,z_*).
 \tag{2}
\]
The coordinate \(z_*\) is an auxiliary outgoing coordinate,
not an ordinary right boundary color.

**Theorem.** There are constants \(c>0\), \(C>0\), and \(B\)
such that, for every real \(-\pi\le\theta\le\pi\) and every
sufficiently large level of either parity,
\[
 |Q_N(\theta)|
 \le CN^B\exp N\{\Lambda_*-c(1-\cos\theta)\}.
 \tag{3}
\]
There are also \(h>0\), \(b>0\), and \(c'>0\) such that
\[
 |Q_N(x+iy)|
 \le C'N^{B'}\exp N
       \{\Lambda_*-c'(1-\cos x)+b y^2\},
 \quad -\pi\le x\le\pi,\quad |y|\le h.
 \tag{4}
\]
The constants may depend on the fixed reference. No uniformity
over unbounded word length or over arbitrary short powers is asserted.

For a fixed \(0<\rho<\pi\), (3) gives a positive exponential
gap on \(\rho\le|\theta|\le\pi\), relative to the actual
complete-color action \(\Lambda_*\).

## 2. The exact local integral retains the incoming angular loss

Let \(J_*\) be a sufficiently short fixed horizontal segment
through \(y_*\), and keep the exact integral
\[
 I_N(w,z_*)=N\int_{J_*}
 F_{34,N}(w,e^{-2\pi iy})d_N(e^{-2\pi iy})
 C_{0,N}(e^{-2\pi iy},Z_*)\,dy.
 \tag{5}
\]
Here \(d_N(r^b)=P_b^{-1}\) is the original degree-\((N-1)\)
Fourier polynomial. Equation (5) is the integral in the
[local-source theorem, (15)](research_mixed_three_four_next_local_source.md),
with next type three. It is defined for every ordinary color,
including colors far from \(-2\).

The actual matching equation is \(y_*=q_{34}(s_*)\).
The parameter \(s_*\) lies strictly inside the ordinary enclosure
\(O_3\), by
[the reference-domain theorem, Section 1](research_mixed_actual_last_row_reference_domains.md).
The following map \(q_{34}\) is holomorphic and univalent
on a neighborhood of that enclosure, as used in the
[complete following-prefix theorem](research_mixed_three_four_following_complete_prefix.md).
It therefore maps a neighborhood of \(s_*\) onto a neighborhood
of \(y_*\). We can and do take \(J_*\) inside the image of a
compact neighborhood of \(s_*\) contained in \(\operatorname{int}O_3\).
This choice is made before \(N\).

Theorem 2 of the following-prefix theorem now applies at every
\(y\in J_*\), not just at \(y=y_*\). Its original action identity
and angular estimate give one \(c_{34}>0\) with
\[
 |F_{34,N}(-2\cos\theta,e^{-2\pi iy})|
 \le CN^{B_0}
 e^{N\{\Re\mathcal P_{34}(-2,y)-c_{34}(1-\cos\theta)\}}.
 \tag{6}
\]
No comparison of the moduli of the prefix at two different colors
is being made. The bound is its proved absolute source estimate.

The other factors in (5) are independent of \(\theta\). On this
short segment their complete local expansions are equations
(19)--(20) of the local-source theorem. Define
\[
 \varphi(y)=\mathcal P_{34}(-2,y)-g(y)+\psi_0(y,z_*),
 \tag{7}
\]
where \(\psi_0\) is the original stationary conditional action.
Its critical point is \(y_*\), its value is \(P(-2,z_*)\),
and its negative second derivative has positive real part.
After shortening \(J_*\), this gives
\[
 \Re\varphi(y)\le\Lambda_*-a|y-y_*|^2
 \quad(y\in J_*),\qquad a>0.
 \tag{8}
\]
The local expansions have polynomial prefactors and bounded
relative errors. Thus (6)--(8), with the original factor \(N\),
imply
\[
 |I_N(-2\cos\theta,z_*)|
 \le CN^{B_1}
 e^{N\{\Lambda_*-c_{34}(1-\cos\theta)\}}.
 \tag{9}
\]
There is no fixed positive exponential tolerance in (9):
(6) has a polynomial-prefactor bound at its stated rate, and
the two remaining factors have relative local expansions.

## 3. The full remainder is smaller for every real incoming color

Retain the exact decomposition
\[
 T_N(w,z_*)=I_N(w,z_*)+R_N^+(w,Z_*)+E_N^-(w,z_*),
 \tag{10}
\]
where \(R_N^+\) is the entire sum in (1) over
\(\lceil N/2\rceil\le b\le N-1\).
Equation (37) of the
[incoming-color outer theorem](research_mixed_next_incoming_color_outer_upper_bound.md)
already gives, after choosing its tolerance and absorbing its
polynomial factor,
\[
 \sup_{-2\le w\le2}|R_N^+(w,Z_*)|
       \le C e^{N(\Lambda_*-g_0/2)},\qquad
                 g_0=\frac1{2\cdot10^{13}}.
 \tag{11}
\]
This uses the whole real color interval before any complex
continuation. It is not inferred from the theorem near \(w=-2\).

We next record explicitly the real-color scope of \(E_N^-\).
Its exact signed decomposition is (17) of the
[left-remainder theorem](research_mixed_next_left_remainder_complex_extension.md):
\[
 E_N^-=E_{\rm old}-U_L-U_H+U_S-V_1+V_L-J_-+J_+
                         -D_N^a-T_N^{\rm far}.
 \tag{12}
\]
All paths, filters and finite index ranges in that identity remain
unchanged. Its first three real-interval estimates already cover
all \(w\in[-2,2]\). At \(z=z_*\), their affine rate is
\(\Lambda_*\). Its two physical correction bounds, (20)--(22),
also hold for all those colors, with strict positive gaps.
It remains to check that the other three terms in (12) have
the same real-color scope. This follows from their actual sources:

* For \(U_S\), the
  [upper radial theorem](research_mixed_next_upper_radial_seam.md),
  Theorem and Section 5, bounds the complete selected density
  and the old filtered density on its fixed tube for all real
  ordinary colors. The two arcs in
  [the top seam-arc theorem](research_mixed_next_top_seam_arc_removal.md),
  (6)--(9), lie in that tube. Their denominator is bounded below
  by \(1/2\). Consequently each arc, and hence \(U_S\), has
  a positive gap uniformly in real \(w\).
* For \(V_1\), Theorem 1 of
  [the deep radial theorem](research_mixed_next_three_actual_deep_radial_seam.md)
  gives the all-real estimate on the lower radial segment.
  The theorem in
  [the shallow lower radial note](research_mixed_next_lower_radial_seam.md)
  covers the rest up to one, also for all real colors.
  In the polynomial continuation in Section 5 of the deep radial
  proof, keep \(w\) real and continue only \(Y\); the same tube
  bound remains uniform in \(w\). The zero
  \(F_N^{\rm mid}(w,1)=0\) holds identically in \(w\).
  Its divided difference therefore has the uniform Cauchy bound
  used in (16)--(17) of that proof. The upper radial theorem
  handles the segment above one in the same way. Integrating
  gives a strict gap for the full original \(V_1\), uniformly
  for real \(w\), including its removable seam value.
* For \(E_{\rm old}\), use the component estimates before their
  complex-color continuation in the
  [lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md).
  The lower-left bound (9), the
  [lower-right shoulder bound (7)](research_mixed_next_complete_lower_right_shoulder.md),
  and the off-\(J_*\) central bound from
  [the lower central theorem (11)](research_mixed_next_complete_lower_plateau.md)
  all hold for every real \(w\).
  The last bound has a fixed positive loss because
  \(\gamma_0\setminus J_*\) stays a fixed distance from \(y_*\);
  choose its tolerance within that loss.
  The corresponding filter corrections are controlled by
  the all-real unit-disk bound \(CN^B e^{77N/50}\) and the
  attached estimates in Sections 3--4 of these same proofs.
  The extra factors \(Y^N/(1-Y^N)\) have a strict loss on
  the unchanged lower height.
  On the upper central segment the
  [complete selected-source theorem (7)](research_mixed_next_complete_prefix_selected_segment.md)
  is explicitly all-real.
  Finally
  [paired localization, Corollary 3](research_mixed_next_low_cardinal_paired_localization.md)
  bounds the complete old-filter transfer correction, with
  the same real-color scope and every overlap retained.
  The exact paired-cycle and arc decompositions therefore
  yield the original error \(E_{\rm old}\), with a strict
  complete-color gap for all real \(w\).

There are finitely many bounds in this list. After choosing their
tolerances inside the respective strict margins, their sum gives
some \(\eta_->0\) with
\[
 \sup_{-2\le w\le2}|E_N^-(w,z_*)|
       \le CN^{B_2}e^{N(\Lambda_*-\eta_-)}.
 \tag{13}
\]
This proof uses the raw real-color estimates. Analyticity near one
color, by itself, would not imply (13).

If \(J_*\) has been shortened in Section 2, the change to (12)
is exactly the integral over the removed portions of its former
local segment. The lower central bound (11) just cited gives
those portions a positive gap for all real \(w\).
Thus (13) remains true, possibly with a smaller \(\eta_-\).

## 4. Angular decay and the fixed complex strip

Combine (9)--(13) and put
\[
 \eta=\min\{\eta_-,g_0/2\},\qquad
 c=\min\{c_{34},\eta/2\}.
 \tag{14}
\]
For \(D(\theta)=1-\cos\theta\in[0,2]\),
\[
 \min\{c_{34}D(\theta),\eta\}\ge cD(\theta).
 \tag{15}
\]
The triangle inequality proves (3) with a polynomial prefactor.
It does not discard any term of the exact transfer.

For completeness, the strip estimate follows from the actual
degree and the local asymptotic, as in Lemma 1 of the
[source-stability reduction](research_mixed_open_source_stability_reduction.md).
The polynomial in (1) has ordinary degree at most \(N-1\);
therefore \(Q_N(\theta)\) is an even Laurent polynomial of
angular degree at most \(N-1\). The
complete two-variable theorem gives its local holomorphic
asymptotic with phase
\[
 W(\theta)=P(-2\cos\theta,z_*),\qquad W(0)=P(-2,z_*).
 \tag{16}
\]
The original derivative formula (21a) of the local-source
theorem yields
\[
 W'(0)=0,\qquad
 W''(0)=-\frac{\tan(\pi u_L)}{2\pi},\qquad
                 -\Re W''(0)>0,
 \tag{17}
\]
where \(u_L\) is the original endpoint auxiliary coordinate.
Here \(0<\Re u_L<1/2\), and the exact identity
\[
 \Re\tan(\pi u_L)=
 \frac{\sin(2\pi\Re u_L)}
      {\cos(2\pi\Re u_L)+\cosh(2\pi\Im u_L)}>0
\]
establishes the sign.

Thus a local Taylor bound gives
\(\Re W(x+iy)\le\Lambda_*-a_1x^2+b_1y^2\) near zero.
Away from a fixed small real neighborhood of zero, (3) has
a uniform positive gap. The ordinary polynomial degree extends
(3) to a strip with the additional cost \(N(1+c)|y|\):
multiply \(z^{N-1}Q_N\), \(z=e^{i\theta}\), by \(e^{-Ncz}\)
and apply the maximum principle in the unit disk; evenness
handles the other sign of the height.
Choose the strip width so that this linear cost is absorbed by
half the real gap away from zero. The two regions overlap,
and their bounds give (4). This uses no positivity of the
quantum coefficients.

The theorem treats the complete incoming period at fixed
auxiliary outgoing coordinate. It does not supply a global
outgoing contour estimate, an ordinary two-boundary component
theorem, arbitrary short-filling stability, or finite exceptions.
No numerical evaluation is used.

## Source versions

| Source | SHA-256 |
| --- | --- |
| Complete two-variable transfer | 3baac5dfce1f55588166e519b5408f6d374a37ef6c3ca3b3b80731e73118f6fe |
| Original local integral and phase | f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696 |
| Actual last-row reference domains | c6cecc3e935116829c9f222553d24a5503c092d8544764ac95082299fc039798 |
| Complete following prefix | 87719e2611321df26470e87b614a83859b3e09f56a75af29a54a22fa71ac91de |
| Incoming-color outer bound | 5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49 |
| Left remainder | fbdc20aba05f2895e1fada626ff6ea8f26b7c8e6300a76fd6c51bb16b9c6f092 |
| Upper radial seam | b351d9e4177b9a9454b2a748f00b159a00c7209954164dccac793c9eb5aac3bb |
| Top seam arcs | 98f1d703059e9bd028231664a52a37d9b917ac3f9f298e66e95fd6a211b39ad0 |
| Actual deep radial seam | 6489199a1224c2de2a8455f3f35c7ad18938f8c96f7716794bfae6a8a7c054e4 |
| Shallow lower radial seam | 10e32a30ff442e42813b0097049be6d1369d2779d1a5f92e1e197a23a2bce94f |
| Actual lower-half assembly | e891cfb63b4ca3e5c1fb4682e31461eb63cc93296a016091ae04f8d0c040e52e |
| Lower-right shoulder | ec680bcc94bf6b475439356eba037172b2016053e41ac9c3e0cec8a4af3c1b3d |
| Complete lower central interval | 6ce61829958c6a163d849e45d666bc080ad20dd97bc18a7e29e4e240bd915b62 |
| Complete selected central segment | 2e21f8d1f47f609d965af6d0be481b73298e2bb3d1262e99dad3cc6d71315026 |
| Paired localization and full filter correction | c4732366d3dcaecf97b9f4977af533cb44498cf9b889ed753b91de57f4365866 |
| Source-stability reduction | 5d501024dddb98ff28f1ae3d44110d4a34bfc82d8063ff01353315c3efbfc31c |
