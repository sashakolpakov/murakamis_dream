# Complete conditional sources on a left transition product

Research proof, 4 November 2026. This note retains the complete canonical
finite sum, including every factorial row, both midpoint currents and
both cotangent remainders. It does not estimate an outer cyclic integral
or change any completed source theorem.

## 1. Domains and original normalization

Let
\[
 \begin{split}
 T_3&=\operatorname{conv}\{.10,.22-.03i,.22+.02i\},&
 B_3&=[.22,.45]+i[-.03,.02],\\
 T_4&=\operatorname{conv}\{.10,.22-.057i,.22+.014i\},&
 B_4&=[.22,.45]+i[-.057,.014].
 \end{split}                                                     \tag{1}
\]
For \(\eta,\epsilon\in\{0,1\}\), allow either ordered product
\(T_{3+\eta}\times B_{3+\epsilon}\) or
\(B_{3+\eta}\times T_{3+\epsilon}\).
Write \(d=2+\epsilon\), \(r=e^{-2\pi i/N}\), and retain the original
marked factorial \(P_N\) from the
[factorial continuation theorem](research_lower_half_factorial_continuation.md).
The literal source is
\[
 L_{\epsilon,N}(a,b)=\sum_{j=0}^{N-1}e^{2\pi iaj}
       \frac{P_N(Na+j)P_N(Nb+j)}{P_N(j)^d}.
                                                               \tag{2}
\]
Its equality with the fixed Pochhammer definition follows from the exact
factorial recurrence, for all complex parameters here, rather than only
on a physical grid. In particular no formerly zero row is deleted.

Use the original regular-strip phase
\[
 Q(s;a,b)=g(s+a)+g(s+b)-d g(s)+2\pi ias,\qquad
 g'(z)=\Log(1-e^{-2\pi iz}),\quad 0<\Re z<1.             \tag{3}
\]
The global cotangent theorem supplies the holomorphic, original
zero-lift root \(s_*(a,b)\), with \(0<\Re s_*<1/2\).
This use is legitimate on a neighborhood of every product (1): the
left-ramp cotangent estimate in the
[minimum-neighbor contour theorem](research_mixed_minimum_neighbor_contour.md)
gives \(|\Im\cot\pi a|,|\Im\cot\pi b|<.46\), while their real
cotangents are positive. The compact products stay strictly inside this
domain. All three critical factorial arguments have real parts in
\((0,1)\). The original triangle coercivity gives
\(-\Re Q_{ss}(s_*)>0\).

**Theorem 1.** On a fixed open neighborhood of each closed product (1),
uniformly as \(N\to\infty\),
\[
 L_{\epsilon,N}(a,b)=N^{(1-\epsilon)/2}
       A_\epsilon(a,b)e^{NQ(s_*;a,b)}(1+O(N^{-1})),         \tag{4}
\]
where
\[
 A_\epsilon=\frac{\sqrt{2\pi}\,a_0(s_*+a)a_0(s_*+b)}
                       {a_0(s_*)^d\sqrt{-Q_{ss}(s_*)}},
 \qquad a_0(z)=\sqrt{2\sin\pi z}\,e^{-\pi iz/2}.           \tag{5}
\]
The square roots are continued from the original regular strip and the
positive real half-plane for \(-Q_{ss}\). The amplitude is holomorphic
and nowhere zero. All fixed parameter derivatives have the corresponding
uniform expansion on smaller neighborhoods.

Consequently the exact conditional polynomial
\(C_{\epsilon,N}=L_{\epsilon,N}/[P_N(Na)P_N(Nb)]\)
has power \(N^{-(1+\epsilon)/2}\), action
\(Q(s_*)-g(a)-g(b)\), and amplitude
\(A_\epsilon/[a_0(a)a_0(b)]\). No outer Fourier weight or wrapped
alias is replaced by an unspecified continuation in this statement.

## 2. A finite polynomial test for the whole high half

For a fixed horizontal height \(y\), calibrate every shifted factor
separately by
\[
 g_-(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad \Im z<0,\qquad
 g_+(z)=\overline{g_-(\bar z)}+i\pi(z-z^2),\quad\Im z>0.
                                                               \tag{6}
\]
Use their continuous real parts on the axis. Let \(H(x,y)\) be the
real part of (3) with these full-plane calibrations applied separately
to \(s,s+a,s+b\). In particular upper shifted factors are not made
periodic when their real part crosses one. Put
\[
 R=e^{2\pi y},\quad A=e^{-2\pi ia},\quad B=e^{-2\pi ib},
 \quad w=-\cot\pi x\quad(1/2<x<1),
\]
\[
 \begin{split}
 N_Z(w)&=|1-RZ|^2w^2+4\Im(RZ)w+|1+RZ|^2,\\
 D(w)&=(1-R)^2w^2+(1+R)^2,\\
 F(w)&=N_A(w)N_B(w)(1+w^2)^\epsilon-|A|^2D(w)^d,\\
 G(w)&=wF'(w)-2F(w).
 \end{split}                                                    \tag{7}
\]
Away from its logarithmic zeros, the sign of \(H_x\) is exactly
the sign of \(F\). This follows from
\(e^{-2\pi ix}=(w+i)/(w-i)\) and
\[
 \left|e^{Q_s}\right|^2=
 \frac{N_A(w)N_B(w)(1+w^2)^\epsilon}{|A|^2D(w)^d}.
                                                               \tag{8}
\]
The identity concerns real derivatives of (6), so remains valid across
shifted phase walls by continuity of the phase and one-sided derivatives.

**Lemma 2.** If \(G(w)>0\) for \(w\ge0\), including its positive
leading coefficient, then the high-half profile has exactly one
interior minimum, and its maximum is at \(x=1/2\) or \(x=1\).
Indeed \(F/w^2\) is strictly increasing; \(G(0)>0\) gives
\(F(0)<0\), and the positive leading coefficient gives its positive
limit at infinity. Thus \(F\) has one positive zero. This is a
sufficient criterion, not a claim about arbitrary cotangent parameters.

The outward computation verifies this criterion at \(y=\Im s_*\)
on every distinguished boundary product of (1). It compactifies
\(w=t/(1-t)\): if \(G=\sum_{k=0}^n g_kw^k\), then
\[
 (1-t)^nG(t/(1-t))=
 \sum_{k=0}^n\frac{g_k}{\binom nk}\binom nk t^k(1-t)^{n-k}.
                                                               \tag{9}
\]
Strict positivity of subdivided Bernstein coefficients is an exact
certificate on \([0,1]\). No sampled root count is used.
The coefficients depend on the selected height; no harmonic maximum
principle is applied to \(G\).

The left-half circle argument also applies at either sign of the height.
For \(y<0\), write \(S=\cot\pi(x+iy)=r\sin\theta+i(v_0+r\cos\theta)\);
for \(y>0\), change the sign before \(i\), with \(v_0>1\) and
\(r^2=v_0^2-1\). Each logarithmic factor in
\[
 e^{Q_s}=\frac{(S+P)(S+Q_c)(S+i)^\epsilon}
                       {(2i)^\epsilon(P-i)(Q_c+i)},
 \qquad P=\cot\pi a,\ Q_c=\cot\pi b                         \tag{10}
\]
has squared modulus
\(p^2+B^2+r^2+2r(p\sin\theta+B\cos\theta)\), with \(p>0,B>0\)
for the original two factors: writing a shift as \(p+i\alpha\), the values are \(B=v_0+\alpha>0\) at negative height and \(B=v_0-\alpha>0\) at positive height, because \(v_0>1\) and \(|\alpha|<1/2\). The last factor has \(p=0\) and
\(B=v_0+1\) or \(v_0-1>0\). Its logarithm is concave on the first
quarter and decreasing on the second; the two original factors make
the total strict. The selected cotangent satisfies \(|\Im S_*|<1\),
so its angle is in the second quarter. It is the unique downward zero
of \(H_x\), with at most one earlier upward zero. At height zero,
\(S=\cot\pi x\) is real and all the factors in (10) increase
strictly with positive \(S\), giving the same conclusion directly.
Thus the only possible left-half maxima are its initial endpoint and
the selected root; its right endpoint is strictly below the root.

The certificate additionally proves both
\[
 M-H(0,y_*)>10^{-4},\qquad M-H(1,y_*)>10^{-4},
 \qquad M=\Re Q(s_*),\quad y_*=\Im s_* .                    \tag{11}
\]
Together with Lemma 2 these give a unique, nondegenerate full-horizontal
maximum, including the high half, on every boundary product.

## 3. Both midpoint currents and both aliases

The following elementary inequalities retain the entire original
right-midpoint multiplier. Write \(h_a=\Im a,h_b=\Im b\),
\(a_r=\Re a,b_r=\Re b\), and \(v_+=\max(v,0)\). The exact left
midpoint factorial formula and the exact period recurrence give the
rates
\[
 \begin{split}
 U(y)&=\Re\{g(a+iy)+g(b+iy)\}+d\pi y_+-2\pi a_r y,\\
 W(y)&=U(y)+2\pi\{(y+h_a)_++(y+h_b)_+-dy_+-h_a\}.
 \end{split}                                                    \tag{12}
\]
Uniformly for \(-2\le y\le2\), the literal rows on
\(l_N=-1/(2N)\), \(r_N=1-1/(2N)\) are bounded by
\(C N^{-\epsilon/2}e^{NU(y)}\) and
\(C N^{-\epsilon/2}e^{NW(y)}\), respectively. The numerator
factorials stay in fixed regular strips at the left midpoint. At the
right one the exact factor is
\[
 e^{2\pi iNa}\frac{(1+e^{2\pi Ny}e^{-2\pi iNa})
                         (1+e^{2\pi Ny}e^{-2\pi iNb})}
                        {(1+e^{2\pi Ny})^d},                 \tag{13}
\]
so (12) follows without dividing by a possibly zero numerator.
The half-grid displacement changes the exponent only by a bounded
factor. These estimates include \(y=0\).

For \(0<c<1/2\) and every \(v\),
\[
 0<\Arg(1-e^{2\pi v-2\pi ic})<\pi-2\pi c.                 \tag{14}
\]
Consequently \(U\) decreases on \(y<0\) and increases on \(y>0\).
Its zero-mode join from zero to \(y_*\) is bounded by \(U(y_*)\).
Expand the two positive parts in \(W\) as the maximum of four affine
choices. On the negative join each resulting branch is monotone. On
the positive join the same holds for type three. For type four, only
the branch selecting both positive parts can have an interior maximum;
it is
\[
 V(y)+2\pi h_b,\qquad
 V(y)=\Re\{g(a+iy)+g(b+iy)\}+\pi y-2\pi a_r y,
 \qquad 0\le y\le2.                                      \tag{15}
\]
It is strictly concave, because
\(V''=-\pi\Re\{\cot\pi(a+iy)+\cot\pi(b+iy)\}<0\).
The same function \(V\) bounds the only possibly increasing left
vertical cotangent remainder. All negative left remainders and both
right remainders attain their maxima at height zero: subtract
\(2\pi|y|\) from (12), expand its four branches, and use (14).

Besides (11), the computation proves
\[
 \begin{split}
 &M>0,\qquad |y_*|<1,\\
 &M-\Re\{g(a)+g(b)\}
       -2\pi\{(u-1)h_a+v h_b\}>10^{-4}\quad(u,v\in\{0,1\}),\\
 &M-\max_{0\le y\le2}V(y)-2\pi(h_b)_+>10^{-4}\quad(\epsilon=1).
 \end{split}                                                    \tag{16}
\]
The four middle inequalities retain the true rate \(W(0)\).
For the last, a rational proposed point \(y_0\in[0,2]\) and the
concavity bound
\(V(y)\le V(y_0)+V'(y_0)(y-y_0)\) certify the entire interval.
No optimizer value is an acceptance condition.

Take the two original residue horizontals at heights \(\pm2\).
Using \(|\Re g_-(x-iv)|\le e^{-2\pi v}/[2\pi(1-e^{-2\pi v})]\),
(6), \(.10\le a_r,b_r\le.45\), and
\(-.057\le h_a,h_b\le.02\), both full horizontal remainder rates
are less than \(-3/10\) after their exact penalty \(4\pi\).
For the upper horizontal a uniform explicit upper is
\[
 5\frac{e^{-2\pi(2-.057)}}{2\pi(1-e^{-2\pi(2-.057)})}
                      -\frac{\pi}{5}+.0912\pi<-3/10;          \tag{17}
\]
the lower one is smaller than the same disk-series bound minus
\(2.086\pi\). The \(O(N^{-1})\) extension to the midpoint real
ends costs a bounded factor. On each midpoint vertical,
\(\pi N\cot(\pi Ns)\) differs from its upper or lower constant
by at most \(2\pi N e^{-2\pi N|y|}\). Thus (11)--(17) bound every
original vertical and horizontal remainder strictly below \(M\).

## 4. From boundary contours to a holomorphic source packet

For all sufficiently large \(N\), the literal row
\[
 T_N(s)=e^{2\pi iNa s}
       P_N(N(s+a))P_N(N(s+b))/P_N(Ns)^d
\]
is holomorphic in the full midpoint residue rectangle of height two:
the denominator has no zeros there and the numerators have positive
real arguments. The exact cotangent residue formula sums precisely
\(j=0,\ldots,N-1\). Splitting its upper/lower constants gives the
zero mode \(N\int_{l_N}^{r_N}T_N(s)\,ds\), with the two full
horizontal and vertical remainders just estimated. Its subsequent
deformation retains both midpoint joins.

A small technical contour choice avoids any uniform-asymptotic assertion
at a shifted factorial wall. At a fixed boundary parameter, choose the
far zero-mode horizontal height arbitrarily close to \(y_*\), but
different from \(0,-h_a,-h_b\). All strict gaps away from a small
central saddle segment and on the midpoint joins survive. Each far
shifted factorial is now in a fixed open upper or lower half-plane,
so its original Gamma expansion applies there uniformly, across every
real index wall. Move only the central segment through the actual
saddle, inside the original regular strips, and retain the short
connecting pieces in the gapped region. The critical expansion gives
(4)--(5), since the exact zero-mode coefficient is \(+N\).
This procedure also works when \(y_*=0\), or a shifted height vanishes.
It supplies a neighborhood of that parameter; compactness gives a
finite cover of each distinguished boundary product, with uniform
bounds. No divergent limit of two half-plane expansions is taken.

Finally the original \(L_{\epsilon,N}\), its selected action, and
the nonzero symbol (5) are holomorphic on a neighborhood of each
convex parameter product. Therefore
\[
 E_N(a,b)=\frac{L_{\epsilon,N}(a,b)}
 {N^{(1-\epsilon)/2}A_\epsilon(a,b)e^{NQ(s_*;a,b)}}-1
                                                               \tag{18}
\]
is holomorphic. The boundary contour proof gives \(E_N=O(N^{-1})\)
on every edge product. Two successive maximum principles extend this
bound through the whole product. The boundary proof holds on an open
neighborhood, so the products can be enlarged slightly and Cauchy
estimates give the derivative assertion. This is an extension of a
proved normalized finite-source error; root uniqueness or a boundary
polynomial test alone would not justify it.

## 5. Certification and scope

The checker reconstructs the 96 triangle-edge/rectangle-edge products.
Rational affine Newton self-maps enclose the original zero-lift roots;
all selected cotangents remain in their strict strip. It evaluates (7)
by outward arithmetic and verifies (9) by exact de Casteljau bisection.
For its coefficient mean-value enclosure the height response is
\(dy=\Im[-(Q_{sa}da+Q_{sb}db)/Q_{ss}]\), with the full affine root enclosure
used in every derivative. The point coefficients are evaluated at a
separately enclosed exact midpoint root. Thus parameter correlation in
this finite polynomial is retained without treating its height as a
holomorphic function.
Endpoint and action comparisons use separately enclosed midpoint roots
and the exact implicit derivatives, retaining the height response.
The scalar vertical support uses a concave tangent on the entire
height interval. Exact dyadic covers exhaust every edge product.

The 256-bit author cover has 96 products, 35,651 accepted cells and
65,158 visits. It also checks 11 exact identities and two strict scalar
alias bounds. Saved-cover replay reconstructs the same rational parameter
cells and uses no new root or vertical-maximum proposals. A separate
direct interval-coefficient run passed the same 96 products with 120,983
accepted cells; it is a diagnostic corroboration of the canonical
mean-value acceptance, not a substitute for its proof.

```sh
python3 experiments/certify_mixed_transition_whole_period_source.py --precision 256
python3 experiments/certify_mixed_transition_whole_period_source.py --precision 320 --input repro/results/research-mixed-transition-whole-period-source.json --output /tmp/research-mixed-transition-whole-period-source-review.json
```

The full written/code review and a fresh 320-bit saved-cover replay also
passed all 96 products and 35,651 cells, without refinements or new
proposals. The canonical record binds this proof, the checker and all
current analytic inputs. No current or row is excluded
from Theorem 1. Its scope is a conditional source on (1); supporting
planes, neighboring reset costs, selected outer aliases and cyclic
cluster bookkeeping are separate statements.
