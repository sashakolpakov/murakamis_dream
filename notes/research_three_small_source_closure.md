# Full bilinear closure of two prepared sources

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Two actual sources in the small class of the
[source-propagation theorem](research_three_source_tail_propagation.md)
can be closed over the full Fourier period. The coefficient is nonzero
because the full complementary integral has a strict absolute gap.
This theorem assumes that both sources have reached that class; it
does not replace the still-required finite entrance attachments.

## 1. Exact source and hypotheses

Put
\[
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\qquad
 R=\frac1{200},\quad r=\frac1{100},\quad
 A=\frac{29}{20},\quad H_* =\frac1{2500},
 \qquad v(t)=\min\{\operatorname{dist}(t,\mathbb Z),r\}.
 \tag{1}
\]
Let \(F_N,G_N\) be literal finite half-band sources, each with
period sign \((-1)^{N-1}\). Suppose they have nonzero holomorphic
packets on a neighborhood of \(|z|\le R\):
\[
 \begin{split}
 F_N(x_h+z)&=\omega_{F,N}N^{\nu_F}b_F(z)e^{NS(x_h+z)}(1+O(N^{-1})),\\
 G_N(x_h+z)&=\omega_{G,N}N^{\nu_G}b_G(z)e^{NT(x_h+z)}(1+O(N^{-1})).
 \end{split}
 \tag{2}
\]
The amplitudes are holomorphic and nowhere zero on that neighborhood;
the factors \(\omega_{F,N},\omega_{G,N}\) are the original unit
phases, including their parity dependence. Write
\[
 \frac{S'(x_h+z)}{k_0}=-\sqrt{21}z+h(z),\qquad
 \frac{T'(x_h+z)}{k_0}=-\sqrt{21}z+g(z),
 \quad |h(0)|\le H_F\le H_*,\quad |g(0)|\le H_G\le H_*,
 \quad |h'|,|g'|\le\frac9{50}.
 \tag{3}
\]
Here \(H_F,H_G\) are certified upper bounds, not necessarily the
exact gradient magnitudes. On the entire real wire period assume
\[
 \begin{split}
 |F_N(x_h+t)|&\le CN^q
 e^{N[M_F+|k_0|H_Fv(t)-Av(t)^2]},\\
 |G_N(x_h+t)|&\le CN^q
 e^{N[M_G+|k_0|H_Gv(t)-Av(t)^2]},
 \qquad M_F=\Re S(x_h),\quad M_G=\Re T(x_h).
 \end{split}
 \tag{4}
\]
The conditions may hold uniformly with additional ordinary outside-color
parameters. All assertions below then hold on a smaller fixed
neighborhood of those parameters, with every fixed ordinary derivative.

**Theorem 1.** Under (2)--(4), the exact full-period bilinear closure
\[
             \mathcal C_N
       =N\int_{x_h-1/2}^{x_h+1/2} F_N(x)G_N(x)\,dx
 \tag{5}
\]
has the asymptotic
\[
 \boxed{\quad
 \mathcal C_N=
 \omega_{F,N}\omega_{G,N}N^{\nu_F+\nu_G+1/2}
 \frac{\sqrt{2\pi}\,b_F(z_c)b_G(z_c)}
      {\sqrt{-(S''+T'')(x_h+z_c)}}
 e^{N\Xi}(1+O(N^{-1})),\qquad
 \Xi=S(x_h+z_c)+T(x_h+z_c).
 \quad}
 \tag{6}
\]
The critical point \(z_c\) is unique in the source disk. The
Gaussian square root has positive real part; the coefficient in (6)
is nonzero. The formula retains both level parities and the original
bilinear orientation. It makes no Hermitian-positivity substitution.

## 2. Critical point and full complementary estimate

Set
\[
 D=2\sqrt{21},\qquad b=\frac9{25},\qquad
 L=H_F+H_G\le\frac1{1250},\qquad
 C_{\mathrm{cl}}=\frac{|k_0|(D+b)}{2(D-b)^2}.
 \tag{7}
\]
The critical equation is exactly
\[
              z=\frac{h(z)+g(z)}{D}.
 \tag{8}
\]
Its derivative has modulus at most \(b/D<1/25\), and its
right side maps the closed radius-\(R\) disk strictly into itself.
The complex contraction theorem gives the unique solution and
\[
 |z_c|\le\frac{L}{D-b}<\frac1{10000},\qquad
 -\Re(S''+T'')\ge D\Re k_0-b|k_0|>16.
 \tag{9}
\]
The same estimates on a slightly enlarged domain yield holomorphic
dependence on any parameters in the hypotheses.

The action in (6) must retain its actual normalization. For
\(U(z)=S(x_h+z)+T(x_h+z)\), the identity \(U'(z_c)=0\)
gives
\[
 U(z_c)-U(0)=-z_c^2\int_0^1 s\,U''(sz_c)\,ds,
 \qquad |\Xi-S(x_h)-T(x_h)|\le C_{\mathrm{cl}}L^2.
 \tag{10}
\]
This bound uses \(|U''|\le|k_0|(D+b)\); it does not identify
the critical action with the sum of the two center actions.

Let \(r_c=3/625=.0048\). Multiplying the original global bounds
(4), every real input with \(v(t)\ge r_c\) has exponent at most
\[
 M_F+M_G+|k_0|Lv(t)-2Av(t)^2.
 \tag{11}
\]
The function \(2Av^2-|k_0|Lv\) is increasing for
\(v\ge r_c\). Equations (10)--(11) therefore give the uniform
gap relative to \(\Re\Xi\)
\[
 2Ar_c^2-|k_0|\frac{r_c}{1250}
                  -C_{\mathrm{cl}}\left(\frac1{1250}\right)^2
                         >\frac1{20000}.
 \tag{12}
\]
This bounds the whole period outside \([-r_c,r_c]\), including
the real annulus inside the source disk. No increasing-order
interpolation or termwise replacement has been used.

Only the central segment is deformed, to height \(\Im z_c\).
Its full rectangle remains within the input disk, because
\[
 r_c^2+\left(\frac1{10000}\right)^2<R^2.
 \tag{13}
\]
On the translated horizontal segment, (9) gives a unique real maximum
at \(z_c\); each endpoint loses at least
\[
             8\left(r_c-\frac1{10000}\right)^2
                           >\frac1{20000}.
 \tag{14}
\]
At each fixed real endpoint, \(\Re U\) is convex in the imaginary
height, since its second height derivative is \(-\Re U''>16\).
Its value on the entire vertical join is consequently bounded by the
two endpoint values. The real endpoint is covered by (12), and the
translated endpoint by (14). Both original finite sources are
holomorphic there, so this is an exact contour deformation with its
two joins explicitly retained. All complementary integrals have
rate at most \(\Re\Xi-1/20000\), up to polynomial factors.

The horizontal saddle now gives (6). The original \(N\,dx\)
measure and the one wire Gaussian contribute \(N^{1/2}\) in
total. The square root in (6) is unambiguous because
\(\Re[-U''(z_c)]>16\); its Gaussian integral over the oriented
real tangent is \(\sqrt{2\pi}/\sqrt{-U''(z_c)}\).
The original nonzero factors in (2) remain nonzero. Holomorphic
uniform errors, followed by Cauchy estimates, retain the ordinary
outside-color derivatives. \(\square\)

## 3. Literal matrix word and the remaining entrance condition

The [original cardinal identity](research_three_cap_central_source.md)
holds at both parities on every horizontal period:
\[
                  N\int h(x)h(x)^T\,dx=I.
 \tag{15}
\]
If the literal sources are
\(F_N(x)=\ell^TB_1\cdots B_jh(x)\) and
\(G_N(x)=r^TC_1\cdots C_kh(x)\), equation (5) is exactly
\[
       \mathcal C_N
       =\ell^TB_1\cdots B_j C_k^T\cdots C_1^T r.
 \tag{16}
\]
No complex conjugation is present. In particular, both
\(A_N=JM^3\) and
\(\widetilde A_N=A_N-E_{40}\) are symmetric, by
\(M^TJ=JM\) and the symmetric original corner deletion.
Two prepared complete caps with \(j,k\) retained attachments have
the exact closure
\[
 \begin{split}
 F_N(x)&=v(w_L)^TA_N^2\widetilde A_N^{\,j}h(x),\\
 G_N(x)&=v(w_R)^TA_N^2\widetilde A_N^{\,k}h(x),\\
 \mathcal C_N&=v(w_L)^TA_N^2
                   \widetilde A_N^{\,j+k}A_N^2v(w_R).
 \end{split}
 \tag{17}
\]
This is the actual complete-ended retained word, with its endpoint
factors in their prescribed positions. Its undeleted counterpart is
\(v(w_L)^TA_N^{j+k+4}v(w_R)\); passage between these two words
uses the separate
[original corner-transfer theorem](research_three_chain_fourier_corner_transfer.md),
with its action comparison, rather than the present contour argument.

For the actual prepared cap, \(\nu_F=\nu_G=-1\), and retained
attachment preserves that power. Formula (6) then has exactly
\(N^{-3/2}\), with the original parity phases. If both caps have
actually reached the small class, the propagation theorem and the
present closure prove nonzero full retained closures after any further
fixed number of attachments on either side. Three analytic phase
contractions are sufficient to reach the small-gradient range, but
the three original-source entrance attachments remain a separate
requirement. Shorter fixed lengths are not inferred by this argument.

## 4. Reproduction and computational scope

Run

```sh
python3 experiments/check_three_small_source_closure.py --precision 192
```

The [checker](../experiments/check_three_small_source_closure.py) and
[record](../repro/results/research-three-small-source-closure.json)
verify the outward scalar margins in (8)--(14), the bilinear cardinal
identity by exact Fourier-frequency algebra at finite levels, and
the transposition order in (16)--(17). They do not assert that an
unprepared source meets (2)--(4), and do not certify a geometric
volume identity from the scalar integral alone.
