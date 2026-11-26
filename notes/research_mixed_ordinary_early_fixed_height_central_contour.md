# The complete central ordinary contour at the original early height

Private written proof, 10 November 2026. The original allocated
ordinary phase is horizontally accretive on the entire private-index
interval `[1/5,1/2]` when its first retained real coordinate lies in
`[.1,.22]` at its actual unchanged reference height and its other
retained coordinate stays on the plateau. The proof uses the actual
first-type/next-type correlation. It also bounds every horizontal
alias, vertical alias and zero-mode join of this central finite sum.
The only additional rates are its two explicit real cuts. No
comparison of those cuts with the calibrated supporting plane is
asserted here, and no moving-height taper is covered.

## 1. Actual types, domains and the original phase

Let the first and second types be `3+alpha,3+epsilon`, with
\(\alpha,\epsilon\in\{0,1\}\), in an actual positive three/four
open word of length at least three. Use its original coupled
reference \((s_*;a_*,b_*)\), where \(a_*\) is the first attached
retained coordinate, \((s_*,b_*)\) is the ordinary output of the
second vertex, and the next input retains its actual reference.
There is no length-two or independent-reference assertion.

Put
\[
 \begin{split}
 S_3&=[1/5,1/2]+i[-27/250,17/250],&
 A_3&=[1/10,9/20]+i[-9/125,21/1000],\\
 S_4&=[1/5,1/2]+i[-27/250,0],&
 A_4&=[1/10,9/20]+i[-39/500,21/1000],\\
 P&=[11/50,9/20]+i[-3/25,3/25].
 \end{split}
\tag{1}
\]
The subscript in \(S_n,A_n\) here denotes the **second own type**;
these are auxiliary rectangles, not a redefinition of the older
attached-image sets carrying similar letters.

These products contain the actual reference and all the unchanged-
height targets used below. Indeed, the actual image bounds in
[three-row source assembly](research_mixed_three_row_source_assembly.md),
Section 1 and equations (7)--(8), put
\[
 .23\le\Re s_*\le .45,\qquad
 -.108\le\Im s_*\le .068,
\tag{2}
\]
and give negative heights to every actual own-four output. The
first attached type-three height lies in \((-.072,.021)\).
The [coupled first-four height theorem](research_mixed_first_four_attached_height_bound.md)
puts an actual first-four height above \(-.078\), and above
\(-.070\) when the second type is three. Thus the first outer
coordinate belongs to \(A_3\) for second own type three and to
\(A_4\) for second own type four. The other outer coordinate is
in \(P\), with negative height if \(\epsilon=1\). This is the
only type correlation used in the curvature proof.

Keep the original primitive and logarithmic lift
\[
 g'(z)=\Log(1-e^{-2\pi iz}),\qquad
 g''(z)=\pi\cot\pi z-\pi i,
 \qquad V(s,a)=g(s+a)-g(s)-g(a).
\tag{3}
\]
Every real factorial argument in the products below lies strictly
between zero and one. Set
\[
 \begin{split}
 Q_\epsilon(s;a,b)
  &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 F_{\alpha\epsilon}(s;a,b)
  &=Q_\epsilon(s;a,b)
        -(1+\alpha/2)g(a)-(1+\epsilon/2)g(b)\\
  &=V(s,a)+V(s,b)-\epsilon g(s)
       -\tfrac\alpha2g(a)-\tfrac\epsilon2g(b)+2\pi ias.
 \end{split}
\tag{4}
\]
The halfweights, chirp and index equation in (4) are unchanged.

## 2. The typed pair determinant down to one fifth

Write
\[
 \cot\pi s=u+iv,\qquad \cot\pi a=p+i\beta,
 \qquad C=\Re\cot\pi(s+a).
\tag{5}
\]
The original exact determinant is
\[
 -\Re V''/\pi=
 \begin{pmatrix}u-C&-C\\-C&p-C\end{pmatrix},
 \qquad
 up-(u+p)C
   =\frac{(u+p)^2-(pv-u\beta)^2}
          {(u+p)^2+(v+\beta)^2}.
\tag{6}
\]
See [horizontal zero-mode support](research_mixed_horizontal_zero_mode_support.md),
equation (6), and the direct derivation in the
[earlier early-height note](research_mixed_ordinary_early_height_horizontal_concavity.md).
Here \(p>0\) and \(u\ge0\), so its denominator does not vanish.

For \(1/5\le\Re s\le49/100\), the exact cotangent formula gives
\[
 0<u<7/5.
\tag{7}
\]
For example \(u\le\cot(\pi/5)\), and
\(\cot^2(\pi/5)=1+2/\sqrt5<49/25\), since
\(\sqrt5>25/12\).

On \(S_3\) in this real interval,
\[
                         -4/7<v<1.
\tag{8}
\]
For negative height, the upper bound follows from the exact
criterion
\(\cos(2\pi\Re s)<e^{-2\pi|\Im s|}\): its left side is at
most \(\cos(2\pi/5)<5/16<1/2\), and
\(e^{-.216\pi}>1/2\), as proved in the sources of the earlier
early-height note. At positive height the modulus of the negative
imaginary cotangent is largest at \(\Re s=1/5\) and
\(\Im s=17/250\). To check the height monotonicity, differentiate
\(\sinh y/(\cosh y-c)\): its derivative has the sign of
\(1-c\cosh y\). Here \(c\le5/16\) and
\(\cosh(.136\pi)<\cosh(1/2)<5/4\). The last inequality
follows from
\(\cosh(1/2)\le1+(1/8)/(1-1/48)=53/47<5/4\).
The written series witnesses in
[first-attached eligibility](research_mixed_first_attached_taper_root_eligibility.md),
equation (7), give
\[
 \cosh(.136\pi)>437/400,
 \qquad \sinh(.136\pi)<2203/5000.
\]
Consequently
\[
 |v|<\frac{2203/5000}{437/400-5/16}
       =\frac{2203}{3900}<\frac47.
\tag{9}
\]
On \(S_4\) the same negative-height argument instead gives
\[
                              0\le v<1.
\tag{10}
\]

For both outer rectangles \(p>0,\ \beta>-1\). The latter is
exactly the independent positive-height estimate in the earlier
early-height note, equations (13)--(16): a negative outer height
has \(\beta\ge0\), and at positive height at most \(.021\)
the imaginary cotangent has modulus less than one.
When \(\beta>1\), the exact identity
\[
 \frac{\beta-1}{p}
 =\frac{\cos(2\pi\Re a)-e^{-2\pi|\Im a|}}
        {\sin(2\pi\Re a)}
\tag{11}
\]
decreases with the real coordinate where positive, and increases
with the depth. For \(a\in A_4\), the earlier note gives
\[
                         \frac{\beta-1}{p}<3/8.
\tag{12}
\]
For \(a\in A_3\) there is the stronger bound
\[
                         \frac{\beta-1}{p}<15/49.
\tag{13}
\]
Here is an entirely written witness. Since \(\pi<22/7\),
\(2\pi(9/125)<453/1000=:t\). The positive exponential series
and its successive-term ratios give
\[
 e^t\le1+t+\frac{t^2}{2(1-t/3)}<\frac{63}{40}.
\tag{14}
\]
For the last comparison,
\(63/40-(1+t)=61/500\), while
\(t^2/[2(1-t/3)]=205209/1698000\), and their difference is
\(1947/1698000>0\). Thus the exponential in the numerator of
(11) exceeds \(40/63\). With the original elementary guards
\(\cos(\pi/5)<13/16\), \(\sin(\pi/5)>7/12\),
\[
 \frac{\beta-1}{p}
 <\frac{13/16-40/63}{7/12}
   =\frac{179}{588}<\frac{15}{49}.
\tag{15}
\]

We now prove positivity of (6) on both typed products. If
\(-1<\beta\le1\), (7)--(10) give
\[
                  pv-u\beta<p+u,
       \qquad u\beta-pv<u+4p/7<u+p.
\tag{16}
\]
If \(\beta>1\), the first bound follows from \(pv-u\beta<p\).
For own type three, (7), (8), (13) give
\[
 u\beta-pv
 =u+p\left(u\frac{\beta-1}{p}-v\right)
 <u+p\left(\frac75\frac{15}{49}+\frac47\right)=u+p.
\tag{17}
\]
For own type four, (7), (10), (12) give instead
\[
                     u\beta-pv<u+\frac{21}{40}p<u+p.
\tag{18}
\]
Thus \(|pv-u\beta|<p+u\). Equation (6) makes the determinant
positive and gives \(C<up/(u+p)<\min(u,p)\).

## 3. The half-index endpoint and full supporting plane

On the remaining real interval \([49/100,1/2]\), the exact
guards in [the half-index contour theorem](research_mixed_half_index_contour.md),
Section 1, are
\[
                       0\le u<4/125,
                       \qquad |v|<17/50.
\tag{19}
\]
They hold on the larger height range in \(S_3\), hence also on
\(S_4\). The bounds \(\beta>-1\) and (12) apply to both outer
rectangles. If \(-1<\beta\le1\), (16) follows with
\(17/50\) in place of \(4/7\). If \(\beta>1\),
\[
 u\frac{\beta-1}{p}-v
       <\frac4{125}\frac38+\frac{17}{50}<1.
\tag{20}
\]
This proves the determinant condition through \(u=0\).
At \(u=0\), its numerator is \(p^2(1-v^2)>0\); in
particular \(C<0\) and both diagonal entries are strictly positive.
No degeneracy is introduced by the closed half endpoint.

By continuity on the two closed products, there is a uniform
\(\nu>0\) such that
\[
 -\Re V''(s,a)\succeq\nu I_2
   \quad\text{on }S_3\times A_3
             \text{ and }S_4\times A_4.
\tag{21}
\]
The half-index theorem also proves the old bound
\(-\Re V''(s,b)\succeq\mu_0 I_2\),
\(\mu_0=1/1250000\), on the whole product
\([.15,.5]+i[-.108,.068]\) with \(P\).
All extra own terms in (4) have nonnegative negative-real
Hessian, including at \(\Re s=1/2\), and the chirp Hessian
is purely imaginary. Therefore, with
\(\mu=\min(\nu,\mu_0)>0\),
\[
 -\Re F_{\alpha\epsilon}''\succeq\mu I_3
  \quad\text{on } S_{3+\epsilon}\times A_{3+\epsilon}\times P.
\tag{22}
\]
All constants are uniform over the actual reference families:
only these fixed compact products and the four flags occur.
No numerical value of \(\nu\) or \(\mu\) is selected.

Let \(M=\Re F(s_*;a_*,b_*)\),
\(P_a=F_a(s_*;a_*,b_*)\), \(P_b=F_b(s_*;a_*,b_*)\).
Since the original index equation is \(F_s=0\), integration of
(22) along horizontal segments gives
\[
 \begin{split}
 \Re F(v+i\Im s_*;x+i\Im a_*,z+i\Im b_*)
 \le{}&M+\Re P_a(x-\Re a_*)+\Re P_b(z-\Re b_*)\\
 &-\frac\mu2\bigl[(v-\Re s_*)^2
              +(x-\Re a_*)^2+(z-\Re b_*)^2\bigr].
 \end{split}
\tag{23}
\]
Denote its right side with the first square omitted by
\(B_{\rm early}(x,z)\). These are the same original action
and marginal derivatives as before. Only the uniform curvature
constant has been changed. In the following finite assertion,
\(x\in[.1,.22]\), \(z\in[.22,.45]\), and all three heights
remain their original reference heights.

## 4. Exact finite central sum and every contour current

Write \(X=e^{-2\pi ia},Y=e^{-2\pi ib}\),
\(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and retain
\[
 R_{j,N}(X,Y)=X^{-j}\frac{(rX;r)_j(rY;r)_j}{P_j^{2+\epsilon}}.
\tag{24}
\]
For sufficiently large \(N\), of either parity, set
\[
 \ell_N=\frac{\lfloor N/5\rfloor+1/2}{N},
 \qquad h_N=\frac{\lceil N/2\rceil-1/2}{N},
 \qquad
 C_N^{\rm cen}=\sum_{j=\lfloor N/5\rfloor+1}^{\lceil N/2\rceil-1}
                                  R_{j,N}(X,Y).
\tag{25}
\]
These are literal finite indices. In particular the enlarged
central sum includes the formerly separate `.20`--`.22` and
`.49`--half-index rows with the endpoint assignment in (25).
Rows at most \(\lfloor N/5\rfloor\)
and at least \(\lceil N/2\rceil\) are not silently discarded.

The exact original marked factorial interpolation is
\[
 A_N(s;a,b)=e^{2\pi iNas}
 \frac{\widehat P_N(N(s+a))\widehat P_N(N(s+b))}
      {\widehat P_N(Na)\widehat P_N(Nb)
                               \widehat P_N(Ns)^{2+\epsilon}}.
\tag{26}
\]
Its functional equation gives \(A_N(j/N;a,b)=R_{j,N}(X,Y)\).
On the rectangle with vertical sides \(\ell_N,h_N\) and heights
\(-1/5,2\), its real factorial arguments remain in fixed regular
strips: limiting ranges for \(s,s+a,s+b\) are
\([.2,.5],[.3,.72],[.42,.95]\). The original interpolation
theorem permits any fixed finite imaginary height. No new branch,
interpolation pole or off-grid row replacement is introduced.
The exact source is therefore
\[
 C_N^{\rm cen}=
     \frac{N}{2i}\oint_{\partial\mathcal R_N}^{\rm CCW}
                       \cot(\pi Ns)A_N(s;a,b)\,ds.
\tag{27}
\]

For clarity, every current can be retained without an implicit
cancellation. On the lower/upper halves of the outer rectangle,
put \(c(s)=i\) / \(-i\), respectively. The constant pieces
of (27) give exactly \(+N\int_{\ell_N}^{h_N}A_N(s)\,ds\).
The remaining integral has kernel \(\cot(\pi Ns)-c(s)\)
on both horizontal sides and all four vertical half-sides.
For \(h_0=\Im s_*\), the zero mode equals
\[
 N\left\{
 \int_{\ell_N+ih_0}^{h_N+ih_0}A_N(s)\,ds
 +\int_{\ell_N}^{\ell_N+ih_0}A_N(s)\,ds
 -\int_{h_N}^{h_N+ih_0}A_N(s)\,ds\right\}.
\tag{28}
\]
This fixes its sign, both joins and its original factor \(N\).

## 5. Alias payment on the enlarged interval

The argument proof in
[the complete first-attached contour source](research_mixed_first_attached_complete_contour_envelope.md),
Section 2, uses only regular real arguments and the coarse outer
height bounds, not its separate outer-cotangent cone. It remains
valid at \(\Re s=1/2\). Here are the details needed for that
extension. If
\(A(t,y)=\arg(1-e^{2\pi y-2\pi it})\) on the original lift,
then
\[
 \pi\min(1-2t,0)\le A(t,y)\le\pi\max(1-2t,0),
\tag{29}
\]
and
\[
 \Im Q_{\epsilon,s}
 =A(v+x,y+\Im a)+A(v+z,y+\Im b)
                      -(2+\epsilon)A(v,y)+2\pi x.
\tag{30}
\]
For \(.2\le v\le.5\), this gives
\[
                         -2\pi<\Im Q_{\epsilon,s}<\pi.
\tag{31}
\]
For the upper bound the divided expression is at most
\(\max(1-2v,2x)+(1-2v-2z)_+\le1\).
At \(v<1/2\) the own argument makes the bound strict;
at \(v=1/2\) its upper expression is \(2x\le.44<1\).
The four lower expressions from the cited source are
\(-1+2v-2z\), \(-2+4v+2x-2z\),
\(-2+4v\), \(-3+6v+2x\).
Their previous lower bounds remain valid because each increases
with \(v\); the only potentially equal lower endpoint is strict
by the original finite-radius argument. The present plateau
restriction on \(z\) is stronger than that source's restriction.

Consequently the lower horizontal alias has rate
\[
 \Re F(v-i/5)-2\pi/5
      <\Re F(v+ih_0)-33\pi/250
      <\Re F(v+ih_0)-1/3.
\tag{32}
\]
For the upper alias, the same large-radius identity gives, for
\(y\ge1/2\),
\[
 \left|\Im Q_{\epsilon,s}
           -\pi(-\epsilon+2\epsilon v-2z)\right|
                         <8e^{-2\pi y}.
\tag{33}
\]
Indeed each shifted inverse radius is less than
\(2e^{-2\pi y}\), and the own inverse radius is
\(e^{-2\pi y}\); the source's logarithmic remainder estimate
applies unchanged. The limiting expression is still at least
\(-8\pi/5\). Integrating (31) to height \(1/2\) and (33)
above it proves
\[
 \Re F(v+2i)-4\pi-\Re F(v+ih_0)
                <-48\pi/125+1/15<-1.
\tag{34}
\]

On a vertical half-grid side the exact alias kernel has modulus
at most \(2e^{-2\pi N|y|}\). Equation (31) proves that its
rate decreases away from zero on either half-side:
\[
 \partial_y(\Re F(c+iy)-2\pi y)<0\ (y\ge0),
 \quad
 \partial_y(\Re F(c+iy)+2\pi y)>0\ (y\le0).
\tag{35}
\]
Thus every vertical alias is paid by its own real cut, with no
curvature assumption at heights \(-1/5\) or \(2\).
For the two zero-mode joins in (28), the interval from zero to
\(h_0\) lies inside the corresponding typed box (1).
Equation (22) and holomorphy make
\(y\mapsto\Re F(c+iy;a,b)\) strictly convex there. Its
maximum is bounded by its real-cut value or (23).

All assertions are stable under the half-grid displacement of
the real sides. Strict compact curvature extends to a small
neighborhood of the closed products, and the alias inequalities
have uniform slack on their finite-height contours. In
particular \(\ell_N\) may lie slightly below \(1/5\) without
requiring an unproved fixed interval of lower rows. Their
\(O(N^{-1})\) shifts cost only a bounded rate-exponent factor.

## 6. The complete central-piece bound and its remaining cuts

Let \(J(v)=\Re g(v)=\int_0^v\log(2\sin\pi t)\,dt\) for
\(0\le v\le1\). For the two regular real cuts write
\[
 \begin{split}
 \mathcal R_{\alpha\epsilon}(c;a,b)
  ={}&\int_0^c\log|1-e^{-2\pi i(a+t)}|\,dt
       +\int_0^c\log|1-e^{-2\pi i(b+t)}|\,dt\\
    &-(2+\epsilon)J(c)-2\pi(\Im a)c
       -\tfrac\alpha2\Re g(a)-\tfrac\epsilon2\Re g(b)
     =\Re F_{\alpha\epsilon}(c;a,b),
 \qquad c\in\{1/5,1/2\}.
 \end{split}
\tag{36}
\]
The equality uses only regular original branches; these are
continuous rates, not finite half-row values.

Let \(d_N\) be the original degree-less-than-\(N\) polynomial
with \(d_N(r^j)=P_j^{-1}\), \(0\le j<N\).

**Theorem.** For each prescribed \(\tau>0\), the literal sum
(25), with the original allocation, obeys
\[
 \begin{split}
 |C_N^{\rm cen}(X,Y)|
       |d_N(X)|^{\alpha/2}|d_N(Y)|^{\epsilon/2}
 \le C_\tau N^{A_\tau}\exp N\bigl\{
    \max\bigl(B_{\rm early}(x,z),
       \mathcal R_{\alpha\epsilon}(1/5;a,b),
       \mathcal R_{\alpha\epsilon}(1/2;a,b)\bigr)+\tau\bigr\}.
 \end{split}
\tag{37}
\]
It is uniform in the actual reference families of length at least
three, the independent real targets
\(x\in[.1,.22],z\in[.22,.45]\) at unchanged reference
heights, and both level parities.

*Proof.* Apply the original regular-strip factorial bound to
(26)--(28). Equation (23) bounds the complete principal
horizontal integral. Equations (32), (34) bound both horizontal
aliases with strict losses; (35) bounds all four vertical alias
halves; vertical convexity bounds both zero-mode joins by the
maximum in (37). All lengths, exact contour coefficients and
regular symbols have at most polynomial costs. The original
[Fourier-weight continuation theorem](research_mixed_fourier_weight_continuation.md)
gives precisely the allocation \(-\Re g\) for every present
type-four weight, since that actual outer height is nonpositive
and its real part is below one half. Multiply the halfweights;
no finite Fourier value or complete Newton zero is divided out.
Choose the finitely many source tolerances and rounding
allowances with total at most \(\tau\). This proves (37).
\(\square\)

The result closes the entire central contour inventory, not just
its principal horizontal integral. It does not claim that the
cut at \(1/5\) is below \(B_{\rm early}\). Nor does it assign
the physical low rows, high rows or a changing-height contour
to this theorem. Those require their own joint cap/ordinary
comparison. One may add their literal finite contributions to
(25); no exponential payment of them is implied here.

## Direct source bindings

The stated source arguments were read directly. This proof uses
only exact identities and written inequalities. No mathematical
numerical evaluation, saved-value arithmetic, import, compilation,
test or frozen-source edit was performed.

| Source | SHA-256 |
|---|---|
| research_mixed_ordinary_early_height_horizontal_concavity.md | 44e395eb2b538f410660a476156634d3e9886d70127a9b1defd7d5d5364c7e66 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_first_attached_taper_root_eligibility.md | 87ecb9f32f57789c809d8fb9471545c3b3a818306d2e1eff7ef9565c3e9ff5d3 |
| research_mixed_half_index_contour.md | ed8d13779e734803090f778d01ddc334469cbfb7a35154ba48d6eb462c28c57e |
| research_mixed_first_attached_complete_contour_envelope.md | faa0afee38a1b18c2694e7bd2ad44c069d3880116352d66c3b11ac8d3dad1302 |
| research_mixed_horizontal_zero_mode_support.md | 8cc704f6145773e9267a8fade870192dac729fb2ecd33ee8d6c854ce7deb5fa9 |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
