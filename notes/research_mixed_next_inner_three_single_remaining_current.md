# The inner three-trace with one remaining angular current

Private assembly theorem, 8 November 2026. The original inner
finite trace is reduced to its nonzero geometric contribution and
one explicitly defined right-hand current. All other parts of the
chosen contour have a strict exponential gap. This is a reduction
of the missing estimate, not a complete asymptotic theorem for the
inner trace or the knot invariant.

No mathematical numerical evaluation or change to a frozen proof
is used. The optional additional second-edge cutoff is not used.

## 1. The exact finite trace and the remaining current

Use the original Newton polynomials, crossing \(R_N\), and full
Hermite functional \(\phi_N\). In angular variables put
\[
\begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad q=e^{\pi i/N},\quad
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N^{<<}(t,u)=K_N^<(t,0)K_N^<(t,u),\\
 g_N^{<<}(t,u)=\sin t\,f_N^{<<}(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered} \tag{1}
\]
The trace being estimated is still
\[
 Q_N(u)=
 \phi_N^{(x)}
 \left[R_N(x)^3K_N^{\rm ord}(-2,x)
                       K_N^{<,\rm ord}(x,-2\cos u)\right].
 \tag{2}
\]
Thus its first edge is full in its definition. The replacement
by the product in (1) has the separately proved trace-level error
in the first-edge tail theorem. All original values, normals,
and the odd simple node are retained in (2).

The parameter domain and critical data are
\[
\begin{gathered}
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},\\
 t_*(u)=a_*(u)-iH(u),\quad0<a_*<\pi/2,\quad1/2<H<1,\\
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it,\qquad
 S(u)=\Phi(t_*(u),u),\qquad s(u)=\Re S(u).
\end{gathered} \tag{3}
\]
The branch, logarithmic charge, and constant are the original ones.

For each \(u\), take any piecewise smooth path in the open lower
half-plane with endpoints
\[
 \gamma(u):\quad \pi/2-iH(u)
                        \longrightarrow 5\pi/6-i/10 .
 \tag{4}
\]
For example, one may first move horizontally at height \(-H(u)\)
and then vertically to height \(-1/10\). Define its original current
\[
 \mathcal R_N(u)=
 -\frac{N^2C_{N,3}}{\pi i}
       \int_{\gamma(u)}g_N^{<<}(t,u)W_N(t)\,dt .
 \tag{5}
\]
The value of (5) is independent of the chosen path (4). The
integrand is holomorphic in the open lower half-plane: the
finite kernels and crossing exponential are entire, and all
poles of \(W_N\) lie on the real axis. That half-plane is simply
connected. This observation permits changing the path when
estimating (5); it does not itself estimate the current.

## 2. Assembly theorem

**Theorem.** There is a fixed \(\epsilon>0\) such that, uniformly
for \(u\in\mathcal U_+\), at both parities and all sufficiently
large \(N\),
\[
 \boxed{\quad
 Q_N(u)=
 C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                         (1+O(N^{-1}))
       +\mathcal R_N(u)+O(e^{N(s(u)-\epsilon)}).
 \quad} \tag{6}
\]
Here
\[
 \mathcal A(u)=\frac{i\sqrt{2\pi}}{\pi}
       \frac{\sin(t_*(u))a_e(t_*(u),0)a_e(t_*(u),u)}
                       {\sqrt{-\Phi_{tt}(t_*(u),u)}}
 \tag{7}
\]
is the original Gaussian coefficient, with the original
left-to-right root. Its modulus is uniformly bounded away
from zero on \(\mathcal U_+\). Formula (6) does not assert
any bound for \(\mathcal R_N\).

*Proof.* Start with the exact remaining-current formula (30)
of [the shortened-source transfer](research_mixed_next_inner_three_short_pair_source_transfer.md):
\[
 Q_N=\mathcal P_N^{<<}+\mathcal M_N
              +\mathcal C_N^L+\mathcal C_N^R
                     +O(e^{N(s-1/500)}).
 \tag{8}
\]
Its first term is the literal current from
\(-\eta-iH(u)\) to \(\pi/2-iH(u)\), and has the nonzero
asymptotic (7) with its \(C_{N,3}N^{-3/2}\) normalization.
That result retains the center, positive remote intervals,
and every angular Fourier charge.

The [mixed-height edge theorem, Section 7](research_mixed_next_shortened_edge_mixed_height_packet.md)
bounds the full-first-edge negative middle integrand on
\(-5\pi/12-iH(u)\) to \(-\eta-iH(u)\), including the
complete Fourier multiplier and original trace prefactor,
by \(C e^{N(s-\epsilon_-/2)}\) for a fixed
\(\epsilon_->0\). To apply it to the source in (1), use
equations (10)--(11) of the shortened-source transfer:
\[
 K_N^<(t,0)=K_N(t,0)(1+\varepsilon_N(t)),
 \qquad |\varepsilon_N(t)|\le C e^{-cN},
 \tag{9}
\]
on the signed angular box containing this whole interval.
No division by the second kernel is made. The same absolute
bound therefore holds for \(\mathcal M_N\).

Choose the particular left path in
[the complete left-connection theorem](research_mixed_next_inner_three_left_connector.md).
It gives
\[
                  |\mathcal C_N^L|\le C e^{N(s-1/5)} .
 \tag{10}
\]
The full endpoint vertical and all originally removed far
physical samples were already included in the error of
(8); no endpoint term is removed twice.

Choose the right path to be (4), followed by
\[
 5\pi/6-i/10\longrightarrow T_N-i/10
                             \longrightarrow T_N-ih_c ,
 \tag{11}
\]
where \(T_N\) and \(h_c\) are the original half-grid cut
and endpoint height. The
[right far-region theorem](research_mixed_next_inner_three_right_far_region.md)
bounds the full current on (11), with its original
orientation and prefactor, by \(C e^{N(s-1/50)}\).
Consequently
\[
                 \mathcal C_N^R=\mathcal R_N
                                  +O(e^{N(s-1/50)}).
 \tag{12}
\]
All these statements use the same shortened-kernel product
(1). In particular the optional top-strip deletion in the
stronger action-floor theorem has not altered any current.

Substitute these bounds and the existing partial Gaussian
into (8). For example, one may take
\[
 \epsilon=\min\{1/500,\ \epsilon_-/2,\ 1/5,\ 1/50\}>0 .
 \tag{13}
\]
This proves (6). The nonvanishing and uniform lower bound
for (7) are those in the partial-current theorem: the sine,
both local edge coefficients, and the Hessian are nonzero
on the compact selected family. \(\square\)

## 3. The precise sufficient estimate still missing

A uniform bound of the form
\[
 |\mathcal R_N(u)|\le C N^B e^{N(s(u)-\delta)}
             \quad(u\in\mathcal U_+),\qquad \delta>0,
 \tag{14}
\]
would give the complete inner asymptotic
\[
 Q_N(u)=
 C_{N,3}N^{-3/2}\mathcal A(u)e^{NS(u)}
                         (1+O(N^{-1})).
 \tag{15}
\]
Indeed the two exponential remainders in (6), divided by
the nonzero leading term, tend to zero faster than any fixed
inverse power of \(N\). This is a sufficient route; the
reduction (6) does not rule out a different treatment of
\(\mathcal R_N\) that preserves a nonzero total coefficient.

The positive phase comparison along a candidate path, by
itself, does not prove (14). The estimate must control the
literal second shortened kernel with its original factorial
continuations and any endpoint contributions. Only the
first shortened kernel currently has the global slit-plane
upper bound available on this whole region.

Even after (14) or another adequate non-cancellation theorem
is proved, the outer trace and stability under arbitrary fixed
short partial fillings remain separate requirements for the
finite-exceptions target. No conclusion about an additional
knot family is made by (6).
