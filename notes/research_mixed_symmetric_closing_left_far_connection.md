# Bounding the far-left connection in the symmetric closing contour

Private written finite-source estimate, 9 November 2026.
The far negative horizontal and the full left endpoint descent
can be bounded using the original crossing matrices and the
complete Newton evaluation vector. No asymptotic for the inner
sum at reflected boundary parameters is needed on these pieces.

The unestimated part of the left connection is thereby reduced
to a fixed intermediate negative-angle interval. The right
connection remains separate.

## 1. The full Newton vector at complex angles

Let \(D=N-1\), and retain the original Newton polynomials
\[
 e_j(z)=S_j^{-2}\prod_{\nu<j}(c_\nu-z),\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N).
 \tag{1}
\]
Write \(\mathbf e(z)=(e_0(z),\ldots,e_D(z))^T\). Define the
continuous full-index profile
\[
 \begin{split}
 J(y)&=\int_0^y\log(2\sin\pi s)\,ds,\\
 V_{a-ih}(y)&=\int_0^y
   \log|2\cos(2\pi s)+2\cos(a-ih)|\,ds-2J(y),
                 \qquad 0\le y\le1 .
 \end{split}
 \tag{2}
\]
The original real-angle maximum is
\[
 m_0(a)=\max_{0\le y\le1}V_a(y),\qquad
 m_0(a)\le(\pi-|a|)/\pi\quad(-\pi\le a\le\pi).
 \tag{3}
\]
For the lower half of the index interval, write
\[
                m_-(a,h)=\max_{0\le y\le1/2}V_{a-ih}(y).
 \tag{4}
\]
This is the function called \(m(a,h)\) in the
[complete row-norm comparison](research_mixed_symmetric_closing_low_horizontal_norm.md).

**Lemma 1.** Uniformly for \(|a|\le\pi\), \(0\le h\le7/10\),
and both parities,
\[
 \|\mathbf e(-2\cos(a-ih))\|_2
     \le CN^B e^{N(m_0(a)+h)}.
 \tag{5}
\]
On the smaller region
\[
             \pi/2\le |a|\le\pi,\qquad17/30\le h\le7/10,
 \tag{6}
\]
there is the sharper bound
\[
             \|\mathbf e(-2\cos(a-ih))\|_2
                    \le CN^B e^{Nh}.
 \tag{7}
\]
All original indices \(0\le j<N\) occur in these inequalities.

*Proof.* The zero-safe midpoint argument in the
[complex Newton estimate](research_mixed_next_physical_three_kernel_fourier_bound.md),
Section 2, gives
\[
 |e_j(-2\cos(a-ih))|
             \le CN^B e^{NV_{a-ih}(j/N)}.
 \tag{8}
\]
Here the compact height range is extended to \(7/10\), just
as in the row-norm comparison. To check uniformity directly,
factor each numerator into
\[
 4\cos\!\left(\pi(\nu+1/2)/N+(a-ih)/2\right)
   \cos\!\left(\pi(\nu+1/2)/N-(a-ih)/2\right).
 \tag{9}
\]
Away from the bounded number of mesh cells nearest their
real zeros, logarithmic derivatives are bounded by a constant
times the inverse distance to a zero. Summing their midpoint
errors gives \(O(\log N)\). On each remaining cell, a height
at least \(1/N\) bounds the error directly, and at smaller
heights rescaling its logarithmic singularity gives a uniform
one-sided error. An exact zero only lowers the product.
The sine-factorial denominator has its original uniform
\(O(\log N)\) estimate. This proves (8) for every initial
product through \(j=N-1\), including \(h=0\).

For each cosine factor the change in logarithmic modulus
from height zero is nonnegative:
\[
 |\cos(x+ih/2)|^2=\cos^2x+\sinh^2(h/2)\ge\cos^2x .
 \tag{10}
\]
Its integral over one period in \(s\) is \(h/2\).
Indeed
\[
 2\cos(x+ih/2)=e^{h/2-ix}(1+e^{-h+2ix});
 \tag{11}
\]
for \(h>0\), the convergent logarithmic series shows that the
last factor has zero logarithmic mean. The height-zero
identity follows by the integrable logarithmic limit.
Both shifts in (9) have the same mean. Since their
differences from height zero are nonnegative, every initial
interval of length at most one gives
\[
                   0\le V_{a-ih}(y)-V_a(y)\le h.
 \tag{12}
\]
Together with (8), this proves (5).

We also have the exact full-index reflection
\[
        V_{a-ih}(1-y)=h-V_{a-ih}(y).
 \tag{13}
\]
The numerator integrand in (2) is invariant under \(s\mapsto1-s\);
its full-period integral is \(h\), by (11).
Use also \(J(1-y)=-J(y)\) to obtain (13).
The original real Newton comparison gives
\(V_a(y)\ge0\) for \(0\le y\le1/2\), so (12) implies
the same nonnegativity at positive height. Hence the
maximum on the upper half of the index interval is at
most \(h\).

For the lower half, the row-norm comparison proves that
\(m_-(a,h)\) is nonincreasing in \(a\in[0,\pi]\), at
every fixed nonnegative height. Its equations (20)--(24)
also give, for \(h\le7/10\),
\[
 m_-(\pi/2,h)
 \le b_2-\frac1{2\pi}+\frac{539}{2000\pi}
 =b_2-\frac{461}{2000\pi},
 \qquad b_2<7/12.
 \tag{14}
\]
Since \(\pi<4\), the last subtraction exceeds \(1/20\).
It follows that
\[
        m_-(a,h)<\frac{8}{15}<\frac{17}{30}\le h
                  \qquad(\pi/2\le a\le\pi).
 \tag{15}
\]
The profiles at \(a\) and \(-a\) agree, by conjugation of
the real Newton coefficients and evenness of cosine.
Equations (13),(15) therefore bound every index in (6)
by \(h\). Summing the at most \(N\) terms in (8) proves
(7). \(\square\)

The following consequence applies to arbitrary coefficient
vectors. If
\[
 P_{\sigma,N}(u)=\mathbf e(-2\cos u)^Tb_{\sigma,N},
 \qquad \|b_{\sigma,N}\|_2\le CN^B e^{N\sigma_\sigma},
 \quad \sigma=L,R,
 \tag{16}
\]
then, on \(u=-a-ih\) in (6), their product multiplied by
the complete trace kernel and a positive crossing power
\(n\ge4\) has exponential upper rate
\[
 \sigma_L+\sigma_R+
                \left(1-\frac{na}{2\pi}\right)h
 \le \sigma_L+\sigma_R .
 \tag{17}
\]
To verify this, (7) gives a total cost \(2h\) for the
two evaluation vectors. The crossing factor
\(e^{inNu^2/(4\pi)}\) has rate \(-nah/(2\pi)\),
and \(W_N(u)\) has rate \(-h\), with its denominator
uniformly bounded because \(h\ge17/30\).
The sine factor and the finite prefactor cost only a
polynomial. No positivity of either polynomial is used.

## 2. Applying the bounds to the original symmetric source

Keep the exact functions \(Q_N,F_N,G_N,W_N,C_{N,4}\) from
the [two-current assembly](research_mixed_symmetric_closing_two_remaining_currents.md).
In ordinary coordinates, the original matrix identity is
\[
 Q_N(w,u)=\mathbf e(-2\cos u)^TJ_NM_N^3\mathbf e(w).
 \tag{18}
\]
The [far-boundary estimate](research_mixed_symmetric_closing_far_boundary_payment.md)
proves, uniformly for real \(w\in[-2,2]\),
\[
 \|J_NM_N^3\mathbf e(w)\|_2
      \le CN^B e^{N\sigma_0},\qquad
 \sigma_0=2b_2+c<3/2.
 \tag{19}
\]
This uses the complete two-crossing and one-crossing matrix
norms, with the complete incoming evaluation vector. It has
no angular-domain assumption on the outgoing parameter.

Let \(u_g=\beta_g-iK_g\) be the original geometric point,
with \(17/30<K_g<7/10\), and put
\(M_g=\Re\Theta(-2,-2)>307/100\).
Use the same midpoint boundary \(a_N\) and short height \(h_c\)
as in that assembly:
\[
 a_N=\pi-2\pi\lfloor N/400\rfloor/N,\qquad
 a_F=\pi-\pi/200\le a_N,\qquad
 0<h_c\le1/1000<K_g.
 \tag{20}
\]
Define the far-left path by its vertices,
\[
 \Gamma_{L,N}^{\mathrm{far}}:
      -a_N-ih_c,\quad -a_N-iK_g,\quad-\pi/2-iK_g,
 \tag{21}
\]
with the indicated orientation.

**Theorem.** On fixed complex neighborhoods of the two
real incoming-color intervals, at both parities,
\[
 \frac{N^2}{\pi}
 \int_{\Gamma_{L,N}^{\mathrm{far}}}
           |G_N(u;\mathbf w)W_N(u)|\,|du|
             \le C e^{N(M_g-1/20)}.
 \tag{22}
\]
Every fixed incoming ordinary derivative has the same
bound on smaller fixed neighborhoods.

*Proof.* First let \(w_L,w_R\in[-2,2]\).
On the horizontal part write \(u=-a-iK_g\), with
\(\pi/2\le a\le a_N\). Equations (7),(19), together
with the original crossing power four, give the rate
\[
     2\sigma_0+K_g(1-2a/\pi)<3.
 \tag{23}
\]
This is precisely (17), including every Fourier charge
in the rational kernel \(W_N\).

On the vertical part \(u=-a_N-ih\), \(h_c\le h\le K_g\),
use the more general bound (5). Equation (3) gives
\(m_0(a_N)\le1/200\), so its two full inner factors have
rate at most \(2\sigma_0+2m_0(a_N)+2h\).
At the half-grid boundary,
\[
 |W_N(-a_N-ih)|
       =\frac{e^{-Nh}}{(1+e^{-Nh})^2}\le e^{-Nh}.
 \tag{24}
\]
The crossing modulus is \(e^{-2Na_Nh/\pi}\).
Thus the complete vertical rate is at most
\[
 2\sigma_0+2m_0(a_N)+h(1-2a_N/\pi)
                         <301/100.
 \tag{25}
\]
The coefficient of \(h\) is negative because \(a_N>\pi/2\).
Both the sine factor and the total path length are bounded
uniformly in \(N\).

The integrand, with its outgoing variable fixed on the path,
is a polynomial of degree at most \(D\) in each incoming
color. Filled incoming ellipses of parameter \(e^{1/1000}\)
therefore extend the real-color bounds at a total rate cost
at most \(2/1000\), with polynomial factors. Spend an
additional \(2/1000\) on all fixed polynomial factors,
including the original \(N^2/\pi\). The resulting rate is
at most \(3014/1000\), and
\[
             3014/1000<307/100-1/20<M_g-1/20.
 \tag{26}
\]
This proves (22). Cauchy's formula on smaller incoming
neighborhoods gives its derivative assertion, applied
pointwise to the exact finite integrand before integration.
\(\square\)

## 3. The remaining intermediate left interval

The left path of the two-current assembly is the
concatenation of (21) and
\[
              [-\pi/2-iK_g,\ -\eta-iK_g].
 \tag{27}
\]
Consequently its left current differs, by a term with the
gap (22), from the literal current on (27). No estimate
for (27) follows from this theorem.
It requires the complete inner source at reflected
outgoing parameters or another argument that bounds
the same original finite sum. The right connection,
and the general short-partial-filling problem, remain
unresolved as well.

## Source versions

- Exact two-current assembly and original functions:
  15c28d0004bfcdebd26e55dfe48419aa54d14c563c95e33e1d32ef5b1ac6cad8.
- Complete matrix norms and original far-boundary constants:
  dc1942698fe442e9995c6bf1ee44ae67f7432c54f2f2d2086e108d83f132fd6b.
- Real full-index Newton profile:
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Lower-half complex row profile, angular monotonicity and curvature:
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Earlier full-index compact-height argument and reflection:
  5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d.
- Full-index complex midpoint estimate:
  c85592568185422cdad2de107effde33f73b9037ac914e0a2ee586af197ac2cd.

The full-index midpoint argument is also written in
[the physical-node Fourier bound](research_mixed_next_physical_three_kernel_fourier_bound.md),
Section 2. The proof above explicitly gives the needed
extension of its compact height range.
No mathematical numerical evaluation is used.
