# A coherent outgoing collar at the right endpoint

Research deduction, 7 November 2026. A fixed real neighborhood of
the right endpoint is paid for the whole literal low retained
source on the outgoing critical-height line. The proof changes the
retained interpolation after using the exact periodicity of its
physical polynomial. It does not claim that each positive-height
correction in the older interpolation is small.

No numerical width is chosen and no new evaluation is performed.

## 1. Exact source and the alternative retained chart

Use the actual references, incoming allocation and plane
\(B_\eta(x)\) of
[the outgoing vertical-current completion](research_mixed_fourier_right_cap_vertical_current_completion.md).
In particular
\[
 a=x+i h_a,\quad x\in[11/50,9/20],\quad
 -.102\le h_q=\Im q_*\le-.001,\quad y=x_0.
 \tag{1}
\]
For own incoming type four, its height remains negative and
unselected. Keep the original finite polynomial
\[
 C_N^<(X,Z)=\sum_{j=0}^{M_N}
        \frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},
 \qquad M_N=\lceil N/2\rceil-1,\quad X=e^{-2\pi ia},
 \tag{2}
\]
and \(S_N^<(q)=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y)\).

Let \(q=z+i h_q\), \(q'=q-1\). Physical polynomial
periodicity gives the exact equality
\[
 S_N^<(q)=\widehat f_N(q;y)
       \sum_{j=0}^{M_N}\frac{X^{-j}p_j(X)p_j(e^{-2\pi iq'})}{P_j^3}.
 \tag{3}
\]
For the central retained rows \(L_N=\lceil N/8\rceil\le j\le M_N\),
use
\[
 \mathcal F_N^R(s,q')=
 \widehat f_N(q'+1;y)e^{2\pi iNas}
       \Pi_N(s+a)E_N(a)\Pi_N(s+q')E_N(q')E_N(s)^3.
 \tag{4}
\]
At every physical retained \(s=j/N\), the exact recurrence
identifies (4) with the corresponding summand of (3).
The four retained contour groups, their half-grid cuts
\(\sigma_\pm\), heights \(-1/5,h_s,5/4\), all Fourier
denominators, vertical joins and zero-mode coefficient \(+N\)
are unchanged.

Choose a preliminary real neighborhood \(|z-1|<1/16\).
Then \(s+q'\) stays in a fixed regular real strip throughout
the complete retained rectangle, for all sufficiently large
\(N\). The other \(s\)-dependent arguments remain regular too.
For \(E_N(q')\), use
[global lower-half factorial continuation](research_lower_half_factorial_continuation.md):
\(\Im q'=h_q\le-.001\) keeps its full compact neighborhood
strictly below the axis. This is not an application of the
original positive-real-part strip theorem to a negative
real argument.
The outgoing cardinal \(\widehat f_N(q'+1;y)\) is also
regular on a fixed neighborhood, since its shifted argument
has negative imaginary part and the output remains inside
its original global domain. All original scalars are retained.

The new chart therefore has uniform symbols on the fixed
retained contours. Its allocated phase is exactly
\[
 \begin{split}
 \mathscr F_\eta^R(s,a,q')={}&
 g(s+a)+g(s+q')-3g(s)-(1+\eta/2)g(a)\\
 &-g_-(q')+2\pi ias+\ell_{q'+1}(y),
 \end{split}
 \tag{5}
\]
where \(g_-\) is the original lower-half-plane disk primitive.
The lifted output in \(\ell\) is not reduced modulo a period.
In particular the right cardinal debit is part of (5).

## 2. A strict reference bound and uniform continuation

At \(z=1\), one has \(q'=i h_q\). The unweighted
right-return proof in the vertical-current completion gives,
on every retained contour point, the comparison with its
real-seam profile
\[
 \Re\mathscr F_\eta^R(s,a,i h_q)-\Re\Psi_\eta(s,a)
       \le(\pi+\phi)|h_q|-2\pi\Im y<-1/50 .
 \tag{6}
\]
The retained horizontal and vertical Fourier debits are
independent of \(q'\), so they are identical in (6).
The seam proof had raw reserve \(3/400\) for every such
complete profile. Hence at \(z=1\) all central retained
groups have raw reserve greater than
\[
                         3/400+1/50=11/400.
 \tag{7}
\]
This is the limiting \(q_L=i h_q\) version of the same
comparison, not a different reference action. At this
height \(\Re g_-(i h_q)=0\), and the exact leading
cardinal rate is the \(K_R(h_q)\) used in that proof.

Every function in (5), on each of the four complete retained
contours, varies continuously with \(z\) and the original
compact actual family. The imaginary height remains bounded
away from zero. Compactness therefore gives a fixed
\(0<\delta<1/16\) such that all those profile rates retain
at least \(1/50\) of gap for
\[
                           1-\delta\le z\le1 .
 \tag{8}
\]
This is a simultaneous continuation of the explicit paid
profiles and their original debits. It is not continuity
of the logarithm of a finite coherent sum.

The physical low retained rows \(j<L_N\) are treated
separately. At \(z=1\), their real-seam rate was below
\(B_\eta-3/400-1/35000\), and the same unweighted
right-return comparison supplies the additional \(1/50\).
Their full rate is continuous for
\(0\le j/N\le1/8\) and \(q'\) in this neighborhood.
In particular \(|e^{-2\pi iq'}|\le e^{-2\pi/1000}<1\),
so the moving outgoing product has no logarithmic zero
here; the own factorial endpoint still has its original
uniform \(O(\log N)\) upper bound.
After shrinking the same \(\delta\), their raw rate also
has a gap at least \(1/50\).

The finite symbols, physical-product bounds, original
incoming halfweight estimate and half-grid displacements
are uniform on this fixed compact neighborhood. Apply
the exact retained contour before taking a modulus,
and sum the separate physical low tail. Choosing one
aggregate source tolerance and absorbing the polynomial
factors proves the following.

**Theorem.** For a fixed \(\delta>0\), uniformly on the
actual reference family and incoming targets, eventually
at every level of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}
       \sup_{1-\delta\le z\le1}
          |S_N^<(z+i h_q)|
                  \le e^{N(B_\eta(x)-1/100)} .
 \quad}
 \tag{9}
\]
Consequently, with the original
\(\beta_N=1-1/(2N)\),
\[
 |d_N(X)|^{\eta/2}
 \left|N\int_{1-\delta}^{\beta_N}S_N^<(z+i h_q)\,dz\right|
                    \le e^{N(B_\eta(x)-1/200)}
 \tag{10}
\]
for all sufficiently large \(N\). The original \(+N\)
and cardinal \(1/N\) are already included.

Equation (3) preserves the literal polynomial before
changing its contour representation. No physical
support condition is imposed at off-grid points, no
finite halfweight is divided out, and no monodromy
denominator is used. In particular (9) does not imply
that an individually growing upper alias from the old
unshifted retained chart is small: the new exact chart
keeps the cancellation needed for the same finite
polynomial.

## 3. The remaining compact interval

The [exact main reduction](research_mixed_fourier_right_cap_main_reduction.md)
had retained one horizontal integral from \(11/50\) to
\(\beta_N\). Equation (10) removes a fixed terminal collar
from that integral with its original normalization.
The unpaid positive-height retained corrections may
therefore be confined to the fixed interval
\([9/20,1-\delta]\). The earlier central-plateau,
left-taper, right-main-sheet and nonpositive retained
estimates keep their own stated scopes.

Neither the compact interval's remaining coherent source
nor a lower asymptotic for the whole Fourier cap is proved
by this collar argument.
