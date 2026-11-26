# A total-weight limit for the positive-real-part symbol criterion

Private exact-symbol theorem, 9 November 2026. Every Fourier weight
satisfying the positive-real-part criterion of the original outer
symbol has total weight strictly less than \(1/6\), independently
of where its solved band stops below frequency \(1/2\).
The proof uses the complete symbol, a strip Schwarz lemma, and
elementary exact inequalities.

This restricts that sufficient inverse criterion only. It does not
restrict a criterion based only on a zero-free shifted symbol, prove
a lower bound for a signed observation, or establish failure of
actual cancellation. No mathematical numerical evaluation, saved-value
arithmetic, or frozen-source edit is used.

## 1. Exact symbol and two necessary height bounds

Retain the original full leading-shift convention from
[the finite compression theorem](research_mixed_next_outer_full_shift_low_frequency_inverse.md):
\[
\begin{split}
p(u,t)&=(2-2\cos u)^3d(u,-e^{3iu+2\pi it}),\\
d(u,\zeta)&=(\ell^2-1)m-(8+2\cos u)\ell+10,\\
\ell&=2+2a-a(\zeta+\zeta^{-1}),\\
m&=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}),\qquad
a=\cot^2(u/2).
\end{split}                                                       \tag{1}
\]
The apparent poles in the first line are removable. The full
\(p\) is an entire trigonometric polynomial of degree at most
eleven, real and strictly positive for real \(u\) and
\(0\le t<1/2\). Its original Fourier carrier is not changed.

Fix \(t\) and suppose a height \(\lambda>0\) satisfies
\[
              \Re p(u-i\lambda,t)>0\qquad(u\in\mathbb R).          \tag{2}
\]
This is exactly the direct condition in the
[complex-symbol weight theorem](research_mixed_next_outer_complex_symbol_weights.md).
That theorem imposes additional finite-band and reflection conditions;
they do not enlarge the class satisfying (2).

The complete square and highest coefficient in
[the endpoint restriction, equations (4)--(6)](research_mixed_next_outer_complex_symbol_endpoint_restriction.md)
give
\[
p(u,t)=\sum_{\ell=-11}^{11}p_\ell(t)e^{i\ell u},\qquad
p_{11}(t)=e^{6\pi it},\qquad 0\le p(u,t)\le12800
                                                   \quad(u\in\mathbb R).
                                                                    \tag{3}
\]
For clarity, (2) makes the periodic function
\(f(u)=\Re p(u-i\lambda,t)\) positive. Its mean is \(p_0(t)\)
and its eleventh Fourier coefficient is
\(p_{11}(t)\cosh(11\lambda)\), because
\(p_{-\ell}(t)=\overline{p_\ell(t)}\). The integral triangle
inequality therefore implies
\[
 \cosh(11\lambda)\le p_0(t)\le12800,\qquad
 \lambda\le L_*:=\frac{\log25600}{11}<1.                          \tag{4}
\]
The last strict inequality requires no evaluation of a logarithm:
\[
e>\frac83,\qquad
\left(\frac83\right)^2>7,\qquad
e^{11}>\left(\frac83\right)^{11}
       >7^5\frac83=\frac{134456}{3}>25600.
\]
The first bound follows from the first four positive terms of the
exponential series at one.

There is a second, frequency-dependent necessary bound:
\[
\boxed{\qquad
          \lambda\le\frac{\pi}{16}\cot(\pi t),
                               \qquad0<t<1/2.
\qquad}                                                          \tag{5}
\]
Unlike the local endpoint restriction, this bound holds at every
positive frequency.

## 2. Strip Schwarz lemma and the exact central derivative

We first justify the complex-analytic implication of (2).
For fixed real \(t\), reality on the real axis gives
\[
                 p(\overline z,t)=\overline{p(z,t)} .
\]
Thus the real part is positive on both boundary lines
\(\Im z=\pm\lambda\). Periodicity allows the strip maximum
principle to be applied on a compact cylinder. It follows that
\[
                  \Re p(z,t)>0\qquad(|\Im z|<\lambda).           \tag{6}
\]
This step keeps the whole symbol; positivity of a principal
matrix at real parameters alone would not imply (6).

Put \(p_c=p(0,t)>0\) and
\[
h(z)=\frac{p(z,t)-p_c}{p(z,t)+p_c}.
\]
By (6), \(h\) maps the strip \(|\Im z|<\lambda\) into the unit
disk and \(h(0)=0\). The conformal map
\[
                     \chi(z)=\tanh\frac{\pi z}{4\lambda}
\]
takes that strip onto the unit disk, sends zero to zero, and has
\(\chi'(0)=\pi/(4\lambda)\). Applying the ordinary Schwarz lemma
to \(h\circ\chi^{-1}\) proves
\[
 \frac{|p_u(0,t)|}{2p(0,t)}
       =|h'(0)|\le\frac{\pi}{4\lambda}.
                                                                    \tag{7}
\]

The derivative in (7) is explicit with the actual carrier.
Write \(\vartheta=\pi t\). On substituting
\(\zeta=-e^{3iu+2i\vartheta}\) into (1),
\[
\ell=2+4a\cos^2(\vartheta+3u/2),\qquad
m=2+4a\cos^2(\vartheta+u).
\]
The unique term of degree three in \(a\) in (1) gives
\[
\begin{split}
p(u,t)={}&64(2+2\cos u)^3
 \cos^4(\vartheta+3u/2)\cos^2(\vartheta+u)
                                      +u^2R(u,t),              \tag{8}
\end{split}
\]
where \(R\) is analytic near \(u=0\). Indeed every other term
has degree at most two in \(a\); multiplication by
\((2-2\cos u)^3\) leaves a factor \(2-2\cos u\), and hence
an analytic multiple of \(u^2\).
Consequently the exact value and first derivative are
\[
\begin{split}
p(0,t)&=4096\cos^6(\pi t),\\
p_u(0,t)&=-32768\cos^5(\pi t)\sin(\pi t),\\
\frac{|p_u(0,t)|}{p(0,t)}&=8\tan(\pi t)
                                      \qquad0<t<1/2.
\end{split}                                                       \tag{9}
\]
No finite-level derivative or sampled symbol is used here.
Combining (7) and (9) proves (5).

## 3. A uniform limit for the accumulated weight

Let \(0<\alpha<1/2\), and let
\(\lambda:[0,\alpha]\to(0,\infty)\) be continuous and satisfy
(2) at every frequency. In particular every admissible weight
of the complex-symbol theorem is covered. Set
\[
                         W(\alpha)=\int_0^\alpha\lambda(t)\,dt.
\]
Equations (4)--(5) prove the more explicit bound
\[
W(\alpha)\le
 \int_0^\alpha\min\left\{L_*,\frac{\pi}{16}\cot(\pi t)\right\}dt,
                                                                    \tag{10}
\]
with the cotangent term omitted at zero.

**Total-weight theorem.** Uniformly over all such \(\alpha\)
and weights,
\[
\boxed{\quad
W(\alpha)\le
 \frac{L_*-\log\sin(\pi/16)}{16}<\frac16 .
\quad}                                                            \tag{11}
\]

If \(\alpha\le1/16\), (4) gives
\(W(\alpha)\le L_*/16\), which is smaller than the first bound
in (11). If \(\alpha>1/16\), use (4) below \(1/16\) and (5)
above it:
\[
\begin{split}
W(\alpha)
&\le \frac{L_*}{16}
       +\frac1{16}\log\frac{\sin(\pi\alpha)}{\sin(\pi/16)}\\
&\le \frac{L_*-\log\sin(\pi/16)}{16}.
\end{split}                                                       \tag{12}
\]

Here are elementary witnesses for the final strict comparison.
The usual rational bounds \(25/8<\pi<16/5\) put
\(x=\pi/16\) between \(25/128\) and \(1/5\). The sine bound
\(\sin x\ge x-x^3/6\) then gives
\[
\sin(\pi/16)>
 \frac{25}{128}\frac{149}{150}
 =\frac{149}{768}>\frac5{26},                                   \tag{13}
\]
where the last cross-multiplication is \(3874>3840\).
The first six positive exponential terms give
\[
e^{5/3}>
 \sum_{j=0}^5\frac{(5/3)^j}{j!}
 =\frac{7663}{1458}>\frac{26}{5},                               \tag{14}
\]
since \(38315>37908\).
Thus \(-\log\sin(\pi/16)<5/3\). Together with \(L_*<1\),
this proves the strict inequality in (11). The same bound
holds for an integrable positive weight on the open interval
\([0,1/2)\) satisfying (2), by taking increasing endpoints;
its total integral is still bounded by the fixed first
quantity in (11), which is strictly below \(1/6\).

## 4. Consequence for the stated sufficient attachment criterion

The
[actual residual profile theorem](research_mixed_next_outer_variable_frequency_weight.md)
keeps
\[
E_Z(t)=\mathcal E(1/2+t,Z),\qquad
\delta_W(\alpha,Z)=
 \min_{0\le t\le\alpha}
 \{E_Z(0)-E_Z(t)+W(\alpha)-W(t)\}.                               \tag{15}
\]
This is the bound for the literal residual, including all eleven
generated boundary output modes and the original higher-degree
tail. The competitor \(t=0\) in (15) gives
\[
                    \delta_W(\alpha,Z)\le W(\alpha)<1/6.        \tag{16}
\]
The positive-real-part implementation of this criterion therefore
cannot certify the strict comparison
\[
\delta_W(\alpha,Z_*)>
                \mathfrak M_3+\mathcal E(1/2,Z_*)-\Lambda        \tag{17}
\]
at any eligible actual reference whose right side is at least
\(1/6\). This is a conditional interpretation of the proved
uniform limit, not a claim that the actual right side has that
size. No saved action value or excess enclosure is evaluated here.

Conversely, an excess smaller than \(1/6\) is not thereby paid:
(10)--(11) are necessary restrictions and do not construct an
admissible weight. Nor does a large upper endpoint of an enclosing
interval establish a lower bound for the actual excess.

The original finite source, both parity forcing terms, and all
Hermite endpoint conditions remain those of the cited residual
theorem. The argument proves no lower bound for the coherent
correction or for its absolute value. A proposed inverse based
only on zero-free shifted symbols need not satisfy (2), so (11)
does not apply to that distinct criterion. The general
short-partial-filling and finite-exception questions remain open.

## Frozen source versions

- Original full shifts and exact Fourier convention:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
- Positive-real-part complex-symbol inverse criterion:
  858546c9a2762175c32c1ef7b6dd62385051335a613665c9ff1848e0af711ff1.
- Exact square, highest Fourier coefficient and endpoint restriction:
  a072317a34adf75b02aec9c1d20421e88016820040b73cb9cdaa41468d12aed8.
- Original residual profile, forcing and complete attachment:
  09caa456c9f27ca22a91521a64c24ded42b4bad7546b591696daaaa82212bfcf.

