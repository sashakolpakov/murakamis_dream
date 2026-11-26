# The outgoing boundary current with real endpoint heights

Research deduction, 7 November 2026. Returning the main contour to
height zero at its two true ends moves the former unpenalized vertical
segment into that main path. The remaining boundary weight decays on
both sides. Its absolute physical-row envelope is bounded by the same
row rate at the real outgoing endpoint.

This pays fixed neighborhoods of the two ends of the retained
low-index interval. The central coherent seam and the new main path
are still unbounded. No numerical evaluation is used.

## 1. One exact regrouping with a bent main path

Use the literal global-factorial source
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(Z)=(rZ;r)_j,\quad
 M_N=\lceil N/2\rceil-1,\quad A_{j,N}=X^{-j}p_j(X)/P_j^3,\\
 \widehat S_N(q)=\sum_{j=0}^{M_N}
          A_{j,N}p_j(e^{-2\pi iq})\widehat f_N(q;y),\qquad
 \alpha_N=-1/(2N),\quad\beta_N=\alpha_N+1.
 \end{gathered}
 \tag{1}
\]
Here \(a=x+i\Im a_*\), \(X=e^{-2\pi ia}\), \(x\in[.22,.45]\),
and the actual correlated reference, \(y=x_0=\xi+i\upsilon\),
\(\eta\in\{0,1\}\), incoming halfweight and plane \(B_\eta(x)\)
are exactly those of the
[real-seam theorem](research_mixed_fourier_right_cap_real_seam_high_rows.md).
In particular the type-four incoming height is negative and
unselected. The interpolation is the specified
[global factorial cardinal](research_mixed_fourier_global_factorial_cardinal.md);
it is not replaced by a periodic interpolation.

Let \(\Gamma\) be a finite piecewise smooth path from \(\alpha_N\)
to \(\beta_N\), contained in the holomorphic half-plane of the
source. Both endpoints have height zero. Define
\[
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<0\}}.
 \tag{2}
\]
The finite-height residue identity with zero main height, followed
by [alias elimination](research_mixed_fourier_factorial_alias_elimination.md),
gives exactly
\[
 V_N^<=N\int_\Gamma\widehat S_N(q)\,dq+
 iN\int_{\mathbb R}w_{N,0}(v)
       [\widehat S_N(\beta_N+iv)-\widehat S_N(\alpha_N+iv)]\,dv.
 \tag{3}
\]
The first integral can be bent with its endpoints fixed by Cauchy's
theorem. The source is holomorphic throughout its half-plane, including
all reciprocal-factorial zeros, so this deformation adds no residues.
The two infinite tails are absolutely convergent at fixed \(N\),
as in the alias-elimination proof.
Equation (3) retains the whole main path; it does not delete the
pieces introduced by changing its endpoint heights.

## 2. The continuous rate of an outgoing boundary row

Write \(\phi=2\pi\xi\), \(\rho=|Y|=e^{-2\pi\upsilon}\).
For physical \(s=j/N\in[0,1/2]\), define
\[
 P(s,v)=\int_0^s\log|1-e^{2\pi v}e^{-2\pi iu}|\,du.
 \tag{4}
\]
Let \(g_-\) be the original lower-half-plane disk primitive,
with its continuous integrable real boundary values. Put
\[
 K(v)=
 \begin{cases}
 \pi\upsilon-\phi v+\Re g(1-y)
            -\Re g_-(-\xi+i(v-\upsilon)),&v\le\upsilon,\\
 D_+(y)+\pi v-\Re g_-(-\xi-i(v-\upsilon)),&v\ge\upsilon,
 \end{cases}
 \quad D_+(y)=\Re g(1-y)-2\pi\xi\upsilon.
 \tag{5}
\]
The two expressions agree at \(v=\upsilon\); they are the
continuous real rates of the same factorial cardinal chart.
In particular \(K(0)=\pi\upsilon\). Finally define the paid
outgoing row rate
\[
 L(s,v)=P(s,v)+K(v)-2\pi|v|,\qquad
                         L(s,0)=J(s)+\pi\upsilon.
 \tag{6}
\]
The term \(-2\pi|v|\) is the actual weight in (2).

**Lemma 1.** Put \(c_0=37/82368>0\). Uniformly for
\(0\le s\le1/2\),
\[
 \begin{split}
 L(s,v)&\le L(s,0)+(\pi-\phi)v &&(v\le0),\\
 L(s,v)&\le L(s,0)-(\pi+\phi)v &&(0\le v\le\upsilon),\\
 L(s,v)&\le L(s,0)-c_0-\pi(1-2s)(v-\upsilon)
                                                &&(v\ge\upsilon).
 \end{split}
 \tag{7}
\]
In particular \(L(s,v)\le L(s,0)\) on the entire real line.

*Proof.* For \(v<0\),
\[
 P(s,v)=\Re g_-(s+iv),\qquad
 P_v=-\Im g_-'(s+iv)>-\pi/2.
 \]
The other derivative in (5) is
\[
 K'(v)=-\phi+\Im\Log(1-Ye^{2\pi v})>-\phi-\pi/2.
 \]
The disk arguments are fixed, and the limiting cases \(s=0,1/2\)
cause no difficulty. Thus \(L_v>\pi-\phi>0\), proving the
first line of (7).

For \(v>0\), the exact reciprocal-product modulus identity gives
\[
                  P(s,v)=2\pi sv+\Re g_-(s-iv).
 \tag{8}
\]
The argument of \(1-e^{-2\pi v}e^{-2\pi is}\) lies between
zero and \(\pi(1/2-s)\). Therefore \(P_v\le\pi/2+\pi s\le\pi\).
For \(0<v<\upsilon\), (5) gives \(K'(v)<-\phi\). After the
debit \(-2\pi v\), this proves \(L_v<-\pi-\phi\), and the
second line of (7).

For \(v\ge\upsilon\), (5) and (8) give the exact expression
\[
 L(s,v)=D_+(y)-\pi(1-2s)v
       +\Re g_-(s-iv)-\Re g_-(-\xi-i(v-\upsilon)).
 \tag{9}
\]
On these rays, \(\Re g_-(s-iv)\le0\) and
\(\Re g_-(-\xi-i(v-\upsilon))\ge0\).
These signs follow directly by differentiating the disk series
in the radius, starting at radius zero.
Consequently the possible increase from \(v=\upsilon\) is at most
\[
 \begin{split}
 L(s,v)-L(s,\upsilon)
 &\le-\pi(1-2s)(v-\upsilon)
       -\Re g_-(s-i\upsilon)+\Re g_-(-\xi)\\
 &<-\pi(1-2s)(v-\upsilon)+\frac{85}{576}+\frac16.
 \end{split}
 \tag{10}
\]
The first constant uses
\(\operatorname{Li}_2(\rho)/(2\pi)<85/576\), proved by the
positive series in the
[uniform tail theorem](research_mixed_fourier_vertical_tail_payment.md).
The second is the original bound \(\max_{[0,1]}|J|<1/6\),
also used in the
[boundary-strip source estimate](research_mixed_boundary_strip_bounds.md).
The original \(\rho<5/8\) gives
\(\pi\upsilon>3/13\) by the positive atanh series.
Since \(\phi>8/7\) and \(\pi<22/7\),
\[
       (\pi+\phi)\upsilon>
       \frac3{13}\left(1+\frac4{11}\right)=\frac{45}{143},
 \qquad
       \frac{45}{143}-\frac{181}{576}=\frac{37}{82368}.
 \tag{11}
\]
Combine the second line of (7) at \(v=\upsilon\) with
(10)--(11). This proves the last line. All comparisons include
the continuous values at \(v=0,\upsilon\). \(\square\)

## 3. Uniformity for the finite chart, including its zero line

The rate calculation does not assume a nonzero symbol across
\(v=\upsilon\). Here is a finite-source justification.
On any fixed \(|v|\le H\), the zero-safe logarithmic product
bound from the
[right-half source proof](research_mixed_right_half_source_reduction.md)
gives
\[
 |p_j(e^{-2\pi i(\alpha_N+iv)})|
                      \le C_HN^{b_H}e^{NP(j/N,v)}
                         \qquad(0\le j\le M_N).
 \tag{12}
\]
These are midpoint samples of the integral in (4).
Truncating the logarithm below \(-\log N\) has variation
\(O(\log N)\) and changes its integral by \(O(1/N)\),
uniformly over the compact radius interval. Thus (12)
includes the real zero-height limit.

For \(\widehat f_N\), put \(z=q-y\) and choose an integer shift
\(m_N\) so that the real part of \(z+m_N/N\) lies in a fixed
compact subinterval of \((0,1)\). At either half-grid endpoint
this can be done with \(0\le m_N\le N\), for all sufficiently
large \(N\). The exact reciprocal continuation is
\[
 E_N(z)=
  \frac{\prod_{k=1}^{m_N}(1-e^{-2\pi i(z+k/N)})}
                         {\Pi_N(z+m_N/N)}.
 \tag{13}
\]
The denominator has its uniform nonzero regular-strip expansion.
The numerator has the same zero-safe finite-product upper bound
as (12), uniformly across \(v=\upsilon\). Its logarithmic integral
minus the denominator rate is \(-\Re g_-(z)\) below that line.
Above it, it is \(-\Re g_+(z)\), where
\[
                g_+(z)=i\pi(z-z^2)+\overline{g_-(\overline z)}.
 \tag{14}
\]
The real parts agree on the separating real line. This identity
also follows from the exact marked-factorial reflection.
It keeps the reciprocal zeros in (13), rather than dividing
through them.

Substitution in the original cardinal formula gives uniformly
on bounded vertical intervals
\[
 |\widehat f_N(\alpha_N+iv;y)|\le C_HN^{b_H}e^{NK(v)}.
 \tag{15}
\]
The \(O(1/N)\) real displacement costs \(O(\log N)\) in the
logarithm, including across a product zero. At the right endpoint
the corresponding cardinal rate is
\[
                         K(v)-2\pi\max\{\upsilon,v\}\le K(v).
 \tag{16}
\]
Below the zero line this follows from the period of \(g_-\);
above it use \(g_+(z+1)-g_+(z)=-2\pi iz\).
It is a comparison of the two finite-source upper envelopes,
not division by the potentially vanishing monodromy denominator.
The finite polynomial in (12) is exactly periodic.

For unbounded \(|v|\), use the explicit per-\(N\) cyclotomic
remainder in the uniform tail theorem. To compare its limiting
rates with the exact functions (4)--(6), add the disk-series
bound
\[
 \frac{\operatorname{Li}_2(e^{-2\pi H})
       +\operatorname{Li}_2(e^{-2\pi(H-\upsilon)})}{2\pi}
 \tag{16a}
\]
to its extra rate \(\epsilon(H)\). This controls the two
remaining \(g_-\) real parts at either end, uniformly in \(s\);
the incoming finite product is unchanged. The enlarged error
still tends to zero as \(H\to\infty\).
Choose one fixed large \(H\) so that this enlarged error is less than
\(c_0/2\). The last line of (7) then leaves, at physical \(j\),
the integrable factor
\[
                    e^{-\pi(N-2j)(v-\upsilon)},\qquad
                    N-2j\ge1 \quad(v\ge H).
 \tag{17}
\]
It also retains the reserve \(c_0/2\) in the exponential rate.
For \(v\le-H\), the first line of (7) and the same explicit
remainder leave uniform damping proportional to \(N|v|\),
after enlarging \(H\) if necessary. Together with (12)--(16),
these estimates justify integration over the whole vertical line
with a polynomial prefactor uniform in \(N\).

## 4. A finite row envelope and two paid retained strips

Write the physical seam rate from the real-seam theorem as
\[
 E_\eta^0(s;a)=
 I_a(s)-2J(s)-2\pi(\Im a)s+\pi\upsilon-\frac\eta2\Re g(a).
 \tag{18}
\]
For any subset \(\mathcal J_N\subset\{0,\ldots,M_N\}\), keep
its exact physical retained rows inside the boundary current.
Equations (7), (12)--(17), the original incoming product bound,
and the unchanged incoming Fourier estimate prove
\[
 \begin{split}
 &N|d_N(X)|^{\eta/2}\int_{\mathbb R}|w_{N,0}(v)|
 \sum_{j\in\mathcal J_N}|A_{j,N}|\,
       |p_j(e^{-2\pi i(\alpha_N+iv)})|\\
 &\hspace{23mm}\cdot
 \{|\widehat f_N(\alpha_N+iv;y)|
                       +|\widehat f_N(\beta_N+iv;y)|\}\,dv\\
 &\quad\le C_\tau N^{b_\tau}
    \exp N\left\{\sup_{s\in\mathcal J_N/N}E_\eta^0(s;a)+\tau\right\},
                                                        \qquad\tau>0 .
 \end{split}
 \tag{19}
\]
For the empty subset the left side is zero. This is an upper bound
after taking absolute physical row values. It does not replace a
coherent sum by a positive source.

The two endpoint rates are already paid:
\[
 E_\eta^0(0;a)=\pi\upsilon-\frac\eta2\Re g(a)
             <B_\eta(x)-387/70000,\qquad
 E_\eta^0(1/2;a)<B_\eta(x)-1/35000 .
 \tag{20}
\]
The first follows from the original endpoint payment, since its
additional term \(2\pi(-\Im a)_+\) is nonnegative. The second
is the real-seam theorem. Joint continuity of (18) on the
compact actual reference family supplies fixed
\(\delta_0,\delta_1>0\) such that
\[
 E_\eta^0(s;a)\le B_\eta(x)-1/70000
 \quad\text{for}\quad
 s\in[0,\delta_0]\ \cup\ [1/2-\delta_1,1/2].
 \tag{21}
\]
For the physical subset specified by (21), choose
\(\tau=1/280000\) in (19) and absorb the polynomial factor.
Its entire allocated boundary current, bounded absolutely as
in (19), is at most
\[
                      e^{N(B_\eta(x)-1/140000)}
 \tag{22}
\]
for sufficiently large levels of either parity.
No width in (21) has been evaluated or optimized.

The remaining indices
\(\delta_0<j/N<1/2-\delta_1\) retain their exact coherent
polynomial. Equation (19) alone gives no calibrated sign for
their absolute seam maximum. Nor does (22) bound the bent
main path in (3). The proof pays only the stated actual
retained portions of the real-endpoint boundary current.
