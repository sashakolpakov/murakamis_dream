# Ordinary conditional concavity at the original early height

Private written deduction, 10 November 2026. The original ordinary
pair phase remains horizontally accretive when one retained real
coordinate is moved down to one tenth at its unchanged attached
reference height. The height interval is independent of that real
coordinate. This supplies a calibrated main-horizontal-contour
bound. It does not pay the real cuts, endpoint rows, joins or aliases,
and does not sign the prescribed moving-height physical taper.

## 1. Domains and the original pair determinant

Use the original primitive
\[
 g'(z)=\Log(1-e^{-2\pi iz}),\qquad
 g''(z)=\pi\cot\pi z-\pi i,
 \qquad V(s,a)=g(s+a)-g(s)-g(a).
\tag{1}
\]
All branches are those of the original conditional source. Put
\[
 \begin{split}
 \mathcal S_0&=[11/50,49/100]+i[-27/250,17/250],\\
 \mathcal A_0&=[1/10,9/20]+i[-39/500,21/1000],\\
 \mathcal P&=[11/50,9/20]+i[-3/25,3/25].
 \end{split}
\tag{2}
\]
Every individual argument and each pair sum used below has real
part strictly between zero and one. In particular, the phase and
its Hessian are holomorphic on a neighborhood of these closed
products.

For
\[
 S=\cot\pi s=u+iv,\qquad A=\cot\pi a=p+i\beta,
 \qquad C=\Re\cot\pi(s+a),
\tag{3}
\]
the exact pair matrix is
\[
 -\Re V''/\pi=
 \begin{pmatrix}u-C&-C\\-C&p-C\end{pmatrix},
\tag{4}
\]
and the determinant identity from
[horizontal zero-mode support](research_mixed_horizontal_zero_mode_support.md),
equation (6), is
\[
 up-(u+p)C
 =\frac{(u+p)^2-(pv-u\beta)^2}
              {(u+p)^2+(v+\beta)^2}.
\tag{5}
\]
This identity follows directly from
\(\cot\pi(s+a)=(SA-1)/(S+A)\). Its denominator is nonzero
because \(u,p>0\). We do not assume that both individual
imaginary cotangents have modulus less than one.

## 2. Scalar guards, including the larger outer cotangent

**Lemma 1.** On the product in (2),
\[
 0<u<5/4,\qquad -1/2<v<1,\qquad p>0,\qquad \beta>-1.
\tag{6}
\]
If \(\beta>1\), then in addition
\[
                    \frac{\beta-1}{p}<\frac38.
\tag{7}
\]

*Proof.* The exact formulas are
\[
 \Re\cot\pi(x+ih)
  =\frac{\sin(2\pi x)}{\cosh(2\pi h)-\cos(2\pi x)},
 \qquad
 \Im\cot\pi(x+ih)
  =\frac{-\sinh(2\pi h)}{\cosh(2\pi h)-\cos(2\pi x)}.
\tag{8}
\]
All real parts in (2) lie strictly between zero and one half,
so the real cotangents are positive. Moreover
\[
 u\le\cot(11\pi/50)<5/4.
\tag{9}
\]
For a written elementary witness, \(11\pi/50>69/100\), and
\[
 \tan t>t+t^3/3+2t^5/15\quad(0<t<\pi/2),
 \qquad
 \frac{69}{100}+rac{(69/100)^3}{3}
                 +\frac{2(69/100)^5}{15}>\frac45.
\tag{10}
\]
The first inequality follows by integrating
\(\tan'=1+\tan^2\) successively, first with \(\tan t>t\)
and then with \(\tan t>t+t^3/3\). This proves (9).

When \(\Im s\ge0\), the endpoint calculation in
[first-attached eligibility](research_mixed_first_attached_taper_root_eligibility.md),
Lemma 1, equations (7)--(9), gives
\[
 |v|<487/1000<1/2.
\tag{11}
\]
Here we use that calculation on the independent rectangle
\(\Re s\ge .22,\ |\Im s|\le .068\), not its taper
statement: its proof explicitly replaces the angular cosine by
\(\cos(.44\pi)\) and the absolute height by \(.068\).
The cosine only decreases as the real part increases to \(.49\),
so the same strict endpoint witness applies to every point here.
When \(\Im s<0\), the exact criterion for its positive
imaginary cotangent to be less than one is
\[
 \cos(2\pi\Re s)<e^{-2\pi|\Im s|}.
\tag{12}
\]
This holds because
\(\cos(.44\pi)<1/5<1/2<e^{-.216\pi}\).
The last exponential inequality is proved symbolically in
[the fixed-contour source](research_mixed_four_fixed_contour_transport.md),
equation (11), from the positive series for \(\log 2\).
These arguments give both bounds on \(v\) in (6).

For \(a\), a positive height gives a negative imaginary
cotangent. It has modulus less than one, since
\[
 \cos(2\pi\Re a)\le\cos(\pi/5)<13/16,
 \qquad
 e^{-2\pi\Im a}\ge1-2\pi\Im a
          >217/250>13/16.
\tag{13}
\]
We used \(\pi<22/7\), \(\Im a\le21/1000\) and
\(\cos(\pi/5)=(1+\sqrt5)/4<13/16\). At nonpositive
height \(\beta\ge0\). Thus \(\beta>-1\) everywhere.

Only a negative height can give \(\beta>1\). In that case
(8) gives the exact quotient
\[
 \frac{\beta-1}{p}
 =\frac{\cos(2\pi\Re a)-e^{-2\pi|\Im a|}}
        {\sin(2\pi\Re a)}.
\tag{14}
\]
Where it is positive, this fraction decreases with the real
coordinate and increases with the depth. For the former assertion,
the derivative of \((\cos\theta-r)/\sin\theta\) is
\((-1+r\cos\theta)/\sin^2\theta<0\), with \(0<r<1\).
The depth is at most \(39/500\), and
\[
 2\pi(39/500)<1/2,
 \qquad e^{-2\pi(39/500)}>3/5,
 \qquad \sin(\pi/5)>7/12.
\tag{15}
\]
The exponential estimate follows from
\(e^{1/2}<33/20<5/3\), proved by the factorial geometric
tail in [the upper-index source](research_mixed_first_attached_four_upper_index_barrier.md),
Section 2. For the sine estimate,
\(\sin^2(\pi/5)=(5-\sqrt5)/8>11/32>49/144\).
Equations (13)--(15) imply
\[
 \frac{\beta-1}{p}
 <\frac{13/16-3/5}{7/12}
   =\frac{51}{140}<\frac38.
\tag{16}
\]
This proves (7). \(\square\)

## 3. Uniform joint horizontal concavity

**Theorem 2.** There exists a fixed \(\nu>0\) such that
\[
                  -\Re V''(s,a)\succeq\nu I_2
          \quad ((s,a)\in\mathcal S_0\times\mathcal A_0).
\tag{17}
\]

*Proof.* If \(-1<\beta\le1\), then (6) gives both
\[
 pv-u\beta<p+u,
 \qquad u\beta-pv<u+p/2<u+p.
\tag{18}
\]
If \(\beta>1\), the first inequality follows already from
\(pv-u\beta<p\). For the other inequality use (7):
\[
 \begin{split}
 u\beta-pv
 &=u+p\left(u\frac{\beta-1}{p}-v\right)\\
 &<u+p\left(\frac54\frac38+\frac12\right)
   =u+\frac{31}{32}p<u+p.
 \end{split}
\tag{19}
\]
Thus \(|pv-u\beta|<u+p\) in all cases. Equation (5)
makes the determinant positive. It also gives
\(C<up/(u+p)<\min(u,p)\), so both diagonal entries of
(4) are positive. The matrix is positive definite at every point
of the closed compact product. Continuity supplies the common
positive constant in (17). No numerical value of \(\nu\) is
selected or asserted. \(\square\)

For \(\eta,\epsilon\in\{0,1\}\), keep the exact allocated
ordinary phase
\[
 \begin{split}
 F_{\eta\epsilon}(s;a,b)
 ={}&g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias\\
    &-(1+\eta/2)g(a)-(1+\epsilon/2)g(b)\\
 ={}&V(s,a)+V(s,b)-\epsilon g(s)
                  -\tfrac\eta2g(a)-\tfrac\epsilon2g(b)
                  +2\pi ias.
 \end{split}
\tag{20}
\]
The old horizontal-support theorem bounds the pair \((s,b)\)
on \(\mathcal S_0\times\mathcal P\) from below by
\(\mu_0 I_2\), where \(\mu_0=1/1250000\).
The extra own terms in (20) contribute nonnegative diagonal
entries, and the chirp has purely imaginary Hessian. Consequently,
with \(\mu=\min(\nu,\mu_0)>0\),
\[
 -\Re F_{\eta\epsilon}''\succeq\mu I_3
       \quad\hbox{on }\mathcal S_0\times\mathcal A_0\times\mathcal P.
\tag{21}
\]
This statement needs no moving conditional root.

## 4. Original-height calibration and its finite-source scope

Let \((s_*,a_*,b_*)\) be an actual original reference in the
product of (21). The original index equation is \(F_s=0\).
Write
\[
 M=\Re F(s_*;a_*,b_*),\qquad
 P_a=F_a(s_*;a_*,b_*),\quad P_b=F_b(s_*;a_*,b_*).
\tag{22}
\]
These are the derivatives of the original allocated conditional
critical action; no new root or phase has been substituted.
For real displacements keeping the three real coordinates in
their respective intervals in (2), set
\(s=s_*+d_s,a=a_*+d_a,b=b_*+d_b\). Integrating (21) along
their horizontal straight segment proves
\[
 \Re F(s;a,b)
 \le M+\Re P_a\,d_a+\Re P_b\,d_b
              -\frac\mu2(d_s^2+d_a^2+d_b^2).
\tag{23}
\]

The actual attached first-coordinate heights for open words of
length at least three lie in \(\mathcal A_0\): first type
three has height in \((-.072,.021)\), while first type four
has height in \((-.078,-.020)\) by
[the coupled attached-height theorem](research_mixed_first_four_attached_height_bound.md),
Theorem 1. This uses the coupled actual reference, not the larger
independent endpoint input disk. An application of (23) still
requires its actual private index and other outer coordinate to
belong to \(\mathcal S_0\) and \(\mathcal P\); no length-two
or independent-reference extension is inferred.

Here is the precise finite main-contour consequence. Retain the
literal conditional source
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}X^{-j}
           \frac{(rX;r)_j(rY;r)_j}{(r;r)_j^{2+\epsilon}},
             \qquad r=e^{-2\pi i/N},
\tag{24}
\]
and its exact original marked factorial interpolation. For the
principal horizontal integral on
\([.22,.49]+i\Im s_*\), the original zero-mode coefficient
is \(+N\). All factorial arguments stay in compact regular
strips. The interpolation therefore has exponent (20), uniformly
at the fixed outer heights, with an arbitrary prescribed source
tolerance and a polynomial level factor, as in
[the complete first-attached contour source](research_mixed_first_attached_complete_contour_envelope.md),
Sections 1 and 5. If a type-four outer halfweight is present,
retain its actual nonpositive reference height so that the
original absolute Fourier halfweight bound supplies precisely
the corresponding allocation in (20). No finite Fourier value
is divided out.

Consequently this principal integral, with its original coefficient
and allocated halfweights, is at most
\[
 C_\tau N^{A_\tau}
 \exp N\left\{M+\Re P_a\,d_a+\Re P_b\,d_b
                 -\frac\mu2(d_a^2+d_b^2)+\tau\right\}
\tag{25}
\]
for every fixed \(\tau>0\), at both parities. Half-grid endpoint
rounding is absorbed by the same tolerance.

The cut \(.22\) in this statement is deliberate. It does not
silently replace a lower cut \(.20\) in an existing complete
contour decomposition. A newly chosen central interval leaves
the intervening real rows and its own joins to be estimated.
Neither (25) nor (23) bounds those rows, the high physical tail,
the aliases or true endpoints. They are not a whole finite-kernel
bound. Nor does horizontal concavity bound the prescribed graph
where the first two retained heights change together: the vertical
part of a holomorphic phase has the opposite real curvature.

## Direct source bindings

The stated source portions were read directly. This proof uses
only exact differentiation and written inequalities. No mathematical
numerical evaluation, saved-value arithmetic, import, compilation,
test or frozen-source edit was performed.

| Source | SHA-256 |
|---|---|
| research_mixed_horizontal_zero_mode_support.md | 8cc704f6145773e9267a8fade870192dac729fb2ecd33ee8d6c854ce7deb5fa9 |
| research_mixed_first_attached_taper_root_eligibility.md | 87ecb9f32f57789c809d8fb9471545c3b3a818306d2e1eff7ef9565c3e9ff5d3 |
| research_mixed_four_fixed_contour_transport.md | a536a28babc3addc1299c23a57c1193a349b3ab1eb0c938030e8a2ad5123e5c3 |
| research_mixed_first_attached_four_upper_index_barrier.md | 863353130161d320a666d2da944eb5da5ef79bc3bbeac60ea1d651db24ea8f06 |
| research_mixed_first_four_attached_height_bound.md | 42329b71c8af492823bb5fd5a74b2a472eab8b4f0ecdf2b25cb83ae7f09d7bfe |
| research_mixed_first_attached_complete_contour_envelope.md | faa0afee38a1b18c2694e7bd2ad44c069d3880116352d66c3b11ac8d3dad1302 |
