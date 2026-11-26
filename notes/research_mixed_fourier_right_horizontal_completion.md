# The whole right-hand part of the outgoing horizontal integral

Research deduction, 7 November 2026. The coupled contour transport
now bounds the upper retained correction together with its positive
vertical sides. The other retained contour groups were already
bounded. The small physical retained indices also satisfy the same
rightward comparisons as the main phase. Combining these facts
controls the entire right-hand part of the original outgoing
horizontal integral, before taking a modulus of its central sum.

This is a complete bound for that part of the finite source. The
remaining central integral must still be evaluated to obtain a
nonzero leading term. No knot-family extension is inferred here.

## 1. The finite expression and the comparison rate

Keep the actual reference \((a_*,s_*,q_*)\), the incoming
parameter \(a=x+i\Im a_*\), and allocation \(\eta\) of
[the one-horizontal-integral reduction](research_mixed_fourier_right_cap_main_reduction.md).
In particular \(x\in P=[11/50,9/20]\),
\(h_s=\Im s_*\), \(h_q=\Im q_*\), and
\(-.102\le h_s,h_q\le-.001\). The original output is
\(y=x_0\). Let
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(Z)=(rZ;r)_j,\quad X=e^{-2\pi ia},\\
 L_N=\lceil N/8\rceil,\quad M_N=\lceil N/2\rceil-1,
 \quad\beta_N=1-1/(2N),\quad c=9/20,\\
 S_N^<(q)=\widehat f_N(q;y)
       \sum_{j=0}^{M_N}\frac{X^{-j}p_j(X)p_j(e^{-2\pi iq})}{P_j^3}.
 \end{gathered}
 \tag{1}
\]
All normalizations are the original ones; the cardinal contains
its original \(1/N\). The supporting plane and one useful gap are
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                      -\kappa(x-\Re a_*)^2,
 \qquad\kappa=1/2500000,
 \qquad\delta_Q=\kappa(9/100)^2.
 \tag{2}
\]

**Theorem 1.** Uniformly on this original family, for all
sufficiently large \(N\) of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}
   \left|N\int_c^{\beta_N}S_N^<(z+ih_q)\,dz\right|
                \le e^{N(B_\eta(x)-\delta_Q/8)}.
 \quad}
 \tag{3}
\]
The modulus is outside the outgoing integral. In particular
(3) does not assert a pointwise bound for the entire
conditional polynomial on this interval.

## 2. The small physical retained indices

For \(0\le u\le1/8\) and \(q=z+ih_q\), write their
allocated rate as
\[
 \begin{split}
 E_\eta(u;x,z)={}&
 \Re\{g(u+a)-g(a)+g_-(u+q)-g_-(q)-3g(u)\}\\
 &-2\pi h_a u-\frac\eta2\Re g(a)+\Re\ell_q(y).
 \end{split}
 \tag{4}
\]
The value at \(u=0\) is continuous and uses \(g(0)=0\).
This is the same physical-row rate as equation (17) of
[the bare inner-contour proof](research_mixed_fourier_right_cap_bare_inner_contour.md).
On the negative outgoing height, all shared and outgoing
terms use their original lower-half-plane branches.

For \(z\in P\), the proved left-tail comparison in that
note bounds (4) by its value at \(u=1/8\). The
[completed real-cut theorem](research_mixed_fourier_right_cap_bare_inner_completion.md)
then gives
\[
       E_\eta(u;x,z)<B_\eta(x)-1/35000
                \qquad(0\le u\le1/8,\ z\in P).
 \tag{5}
\]
The two outgoing comparisons in
[the right-main proof](research_mixed_fourier_right_cap_upper_main_arc.md)
apply also at these physical retained heights. Their proofs
use only \(0\le u\le1/2\) and
\(|e^{-2\pi iu}|\le1\), not the lower central cut.
Explicitly,
\[
 \partial_z E_\eta(u;x,z)
   =\log\frac{\rho|1-e^{-2\pi iu}e^{-2\pi iq}|}
                       {|1-e^{-2\pi iq}|\,|1-Ye^{-2\pi iq}|}
                  <-1/10\quad(c\le z\le3/4).
 \tag{6}
\]
The numerator is at most \(1+|e^{-2\pi iq}|\); the
two denominator factors have the same lower bounds used
in that proof, giving a ratio less than \(9/10\).
For \(3/4\le z\le1\), its half-period comparison gives
\[
             E_\eta(u;x,z)
                    <E_\eta(u;x,z-1/2)-1/200.
 \tag{7}
\]
The shared difference \(g_-(u+q)-g_-(q)\) is treated
together. The comparison permits \(u=0\), when this
difference vanishes identically. The strict gain then
comes entirely from the original lifted cardinal.

Integrating (6) from \(c\) extends (5) to \([c,3/4]\).
For the shifted coordinate in (7), use (5) on
\([1/4,c]\) and this extension on \([c,1/2]\).
Therefore (5) holds on the entire outgoing right interval.
The last small retained index satisfies
\((L_N-1)/N<1/8\), so no enlarged physical support is used.

The original uniform product estimates give rate (4) with
an \(O(\log N)\) error, including \(j=0\), together with
the prescribed tolerance for the incoming weight. The
outgoing factors stay strictly below the real axis and
the incoming product arguments lie in a regular strip.
After summing the fewer than \(N\) rows and including the
outgoing factor \(N\), it follows that
\[
 |d_N(X)|^{\eta/2}N\int_c^{\beta_N}
 \sum_{j=0}^{L_N-1}
 \left|\frac{X^{-j}p_j(X)p_j(e^{-2\pi i(z+ih_q)})}{P_j^3}
                  \widehat f_N(z+ih_q;y)\right|dz
                 \le e^{N(B_\eta(x)-1/70000)}.
 \tag{8}
\]
Taking a modulus term by term is used only on these small
physical rows, not on the central retained sum.

## 3. The original positive retained correction is now bounded

For the central retained indices use the exact original row
\(T_N(s,q)\) and its half-grid cuts \(\sigma_\pm\).
Let \(U_N(q)\) be its upper horizontal retained current
and \(V_{N,+}(q)\) the positive-height part of the signed
retained vertical current, both with their original retained
factor \(N\). The
[complete upper-path transport](research_mixed_fourier_original_upper_shear_transport.md)
keeps precisely their sum. Its small upper path can be
translated while the total imaginary part of \(s+q\)
remains negative, so no additional interpolation pole is
introduced.

Section 6 of
[the uniform connector theorem](research_mixed_fourier_retained_side_shear_connectors.md)
passes this exact identity to infinite height. The translated
surface vanishes. The two retained endpoint faces and the
left outgoing face together have allocated gap \(1/140000\).
The remaining term is the right outgoing face, with its
original orientation factor \(i\).
Theorem 2 of
[the right-endpoint comparison](research_mixed_fourier_right_endpoint_shear_comparison.md)
bounds that face by gap \(1/200\). Thus, after absorbing
the sum of the two bounds,
\[
 |d_N(X)|^{\eta/2}
 \left|N\int_c^{\beta_N}\{U_N(z+ih_q)+V_{N,+}(z+ih_q)\}\,dz\right|
                  \le e^{N(B_\eta(x)-1/280000)}.
 \tag{9}
\]
The two parts in braces have been kept together throughout
the transport. No separate estimate for an old growing
upper profile is claimed.

## 4. Completing the right horizontal integral

The exact central retained decomposition consists of its
main current, lower alias, nonpositive vertical part,
and the sum in (9). The
[right-main theorem](research_mixed_fourier_right_cap_upper_main_arc.md)
gives its main rate at most \(B_\eta-\delta_Q\).
The
[nonpositive-correction theorem](research_mixed_fourier_right_cap_nonpositive_index_corrections.md)
gives the lower alias the stronger reserve \(3\pi/25\)
and the nonpositive vertical part the reserve
\[
                 \delta_s=\kappa(23/200)^2>\delta_Q.
 \tag{10}
\]
These bounds include the unpenalized negative-height joins,
all full Fourier denominators, and their original \(N^2\).

Choose the finite-source tolerances in those estimates
smaller than one quarter of their respective gaps.
After polynomial absorption, each of these three groups
has gap at least \(\delta_Q/2\). Equations (8)--(9)
give much larger gaps for the remaining small physical
rows and positive retained group. The five groups are
exactly the source in (3). The triangle inequality and
one further fixed-factor absorption prove (3), with
the stated conservative gap \(\delta_Q/8\).

## 5. Reduction to the central outgoing interval

The earlier full horizontal reduction has error gap
\(\delta_c/8\), where \(\delta_c=\kappa/2500\).
Subtracting the right part bounded in (3) leaves the
single central integral
\[
       I_N^{P}=N\int_{11/50}^{9/20}S_N^<(z+ih_q)\,dz.
 \tag{11}
\]
Since \(\delta_Q>\delta_c\), the original complete cap
satisfies, eventually at both level parities,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|V_N^{\mathrm F}-I_N^{P}|
                       \le e^{N(B_\eta(x)-\delta_c/16)}.
 \quad}
 \tag{12}
\]
Every discarded part of this exact finite source now has
a strict bound. The local stationary evaluation of the
central integral and its nonzero coefficient remain
separate assertions. In particular, (12) alone does not
justify dividing out a finite incoming weight at a zero,
or attaching the resulting open expression to an
arbitrary short-filled tangle.
