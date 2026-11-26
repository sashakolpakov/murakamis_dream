# A holomorphic central total-index packet for the merged pair

Research deduction, 7 November 2026. A symmetric finite cutoff in the
inner difference index gives an exact holomorphic source through the
actual complex total saddle. Its complete finite sum has a nonzero
Gaussian packet, uniformly on a fixed complex domain, for both
difference-index parities. Every row retained in this source is
controlled directly; there is no remaining inner contour current.

At physical total indices it equals exactly the central rows of the
original source. The discarded physical rows and the subsequent
oscillatory total-index sum remain separate. No numerical evaluation
is used.

## 1. The fixed finite source and its domain

Use the original factorial and symbol conventions from
[the merged source](research_mixed_two_adjacent_merged_source.md) and
[the physical total-index packet](research_mixed_two_adjacent_physical_total_index_packet.md):
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad X=e^{-2\pi ix},\quad E_N=\Pi_N^{-1}
 \tag{1}
\]
on the original regular strip. All factorial arguments below stay
inside that strip, so no reciprocal continuation through a wall is
needed.

For equal external endpoints define the exact row
\[
\begin{split}
 T_N(a;c,x)={}&e^{2\pi iNa(c-a)}
 \Pi_N(c)\Pi_N(a+x)\Pi_N(c-a+x)\\
 &\qquad\cdot E_N(a)^2E_N(c-a)^2E_N(x)^2.
\end{split}
 \tag{2}
\]
For \(\sigma\in\{0,1/2\}\), let
\[
 \mathcal D_{\sigma,N}
   =\{d\in\mathbb Z+\sigma:|d|\le N/5\},\qquad
 \mathcal H_{\sigma,N}(c,x)
   =\sum_{d\in\mathcal D_{\sigma,N}}
                  T_N(c/2+d/N;c,x).
 \tag{3}
\]
The index set is fixed independently of \(c,x\), and it is invariant
under \(d\mapsto-d\). In particular the finite source in (3) is
holomorphic, not an analytic continuation chosen after a physical
asymptotic.

Use the explicit domain
\[
 \mathcal D=
 \left\{(c,x):
       \frac{13}{20}<\Re c<\frac{17}{20},\quad
       \frac9{50}<\Re x<\frac{19}{100}\right\}.
 \tag{4}
\]
The imaginary parts can be any finite real numbers; all uniform
claims below are on compact subsets of \(\mathcal D\).
For real \(|t|\le1/5\), put \(a=c/2+t\) and \(s=c/2-t\).
Then
\[
 \frac18<\Re a,\Re s<\frac58,\qquad
 \frac{61}{200}<\Re(a+x),\Re(s+x)<\frac{163}{200}.
 \tag{5}
\]
Together with (4), these put every argument in (2) strictly
inside \(0<\Re z<1\), uniformly on compact parameter sets.

The actual critical point from
[the critical corridor](research_mixed_two_adjacent_critical_corridor.md)
has \(c_*=2a_*\), with
\[
 \frac23<\Re c_*<\frac45,\qquad
 \frac1{10}<\Im c_*<\frac15.
 \tag{6}
\]
Here the improved real bound is the elementary inverse-cotangent
consequence in
[the fixed-total interpolant](research_mixed_two_adjacent_fixed_total_interpolant.md),
section 1. The original \(x_0\) satisfies the external inequalities
in (4). Thus (3) is holomorphic on a fixed neighborhood of
\((c_*,x_0)\), as well as on a corridor joining it to real total
parameters.

## 2. Exact agreement with the original central physical rows

Let \(c=m/N\in[2/3,4/5]\), with \(m\) an integer, and choose
\(\sigma=0\) when \(m\) is even and \(\sigma=1/2\) when \(m\) is odd.
For \(d\in\mathcal D_{\sigma,N}\), the number
\(j=m/2+d\) is an integer. Since \(m/(2N)\ge1/3>1/5\), all
these indices satisfy \(0\le j\le m<N\). The original finite
factorial recurrence gives the exact identity
\[
 \boxed{\quad
 \mathcal H_{\sigma,N}(m/N,x)
  =\sum_{\substack{0\le j\le m\\|j-m/2|\le N/5}}
      \frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
                             {P_j^2P_{m-j}^2}.
 \quad}
 \tag{7}
\]
The factor \(P_m\), both phases, and both external products are
retained. Equation (7) holds for every free \(x\) in (4), hence
also for its derivatives.

If \(B_{N,m}\) denotes the complete inner sum of the physical
total-index theorem, its exact remainder here is
\[
 B_{N,m}(x)-\mathcal H_{\sigma,N}(m/N,x)
  =\sum_{\substack{0\le j\le m\\|j-m/2|>N/5}}
      \frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
                             {P_j^2P_{m-j}^2}.
 \tag{8}
\]
There is no assertion that (3) equals the full source at a
nonphysical \(c\), or that the right side of (8) can already be
discarded at the eventual outer critical rate.

## 3. Global dominance within the complete retained interval

The original regular phase and symbol of (2) are
\[
\begin{split}
 F_c(a;x)={}&g(c)+g(a+x)+g(c-a+x)
                -2g(a)-2g(c-a)-2g(x)+2\pi ia(c-a),\\
 b_c(a;x)={}&
 \frac{\mathfrak a(c)\mathfrak a(a+x)\mathfrak a(c-a+x)}
 {\mathfrak a(x)^2\mathfrak a(a)^2\mathfrak a(c-a)^2}.
\end{split}
 \tag{9}
\]
The original factorial theorem gives, uniformly on compact sets
of (4) and the full interval \(|t|\le1/5\),
\[
 T_N(c/2+t;c,x)
  =N^{-3/2}b_c(c/2+t;x)e^{NF_c(c/2+t;x)}
                                      (1+O(N^{-1})).
 \tag{10}
\]
All factors of the symbol are nonzero. The expansion and its
normalized fixed derivatives follow on slightly smaller regular
complex neighborhoods.

**Lemma 1.** For every \((c,x)\in\mathcal D\), the real function
\[
             t\longmapsto\Re F_c(c/2+t;x),\qquad |t|\le1/5,
 \tag{11}
\]
is strictly increasing for \(t<0\) and strictly decreasing for
\(t>0\). Its unique maximum is at \(t=0\), which is an actual
complex critical point of \(F_c\) in its inner argument.

*Proof.* Exact symmetry under \(a\mapsto c-a\) proves the
critical-point assertion and the symmetry of (11).
Write \(C=\Re c\), \(\xi=\Re x\), \(h=\Im c/2\), and
\(\upsilon=\Im x\). The two internal arguments have common
height \(h\), and the two shifted arguments have common height
\(h+\upsilon\). Put \(r_h=e^{2\pi h}>0\) and
\(R=e^{2\pi(h+\upsilon)}>0\).
The original logarithmic derivative gives
\[
\begin{split}
 \frac{d}{dt}\Re F_c(c/2+t;x)
 ={}&
 \log\frac{|1-R e^{-2\pi i(C/2+t+\xi)}|}
               {|1-R e^{-2\pi i(C/2-t+\xi)}|}\\
 &-2\log\frac{|1-r_h e^{-2\pi i(C/2+t)}|}
                  {|1-r_h e^{-2\pi i(C/2-t)}|}.
\end{split}
 \tag{12}
\]
The derivative of the chirp is \(-4\pi it\), which has zero
real part. All logarithms in (12) are finite by (5).

For \(0<t\le1/5\), the squared numerator difference in the
first ratio is
\[
             4R\sin\pi(C+2\xi)\sin(2\pi t)<0,
 \tag{13}
\]
because \(101/100<C+2\xi<123/100\).
The squared numerator difference in the second ratio is
\[
                    4r_h\sin(\pi C)\sin(2\pi t)>0.
 \tag{14}
\]
Thus both terms in (12) are strictly negative. Symmetry gives
the other half of the assertion. The proof works for every
finite pair of parameter heights, not only nonnegative ones.
\(\square\)

Define the exact central action and inner Hessian
\[
\begin{split}
 \Phi(c,x)&=g(c)+2g(c/2+x)-4g(c/2)-2g(x)
                                      +\frac{\pi i}{2}c^2,\\
 \mathcal K(c,x)&=
       2\pi\cot\pi(c/2+x)-4\pi\cot(\pi c/2)-2\pi i.
\end{split}
 \tag{15}
\]
Throughout (4),
\[
 \Re(c/2)\in(13/40,17/40),\qquad
 \Re(c/2+x)\in(101/200,123/200).
 \tag{16}
\]
For arbitrary finite imaginary part, the real part of the
cotangent is positive in the first real interval and negative
in the second. Consequently
\[
                         \Re\mathcal K(c,x)<0.
 \tag{17}
\]
The holomorphic square root \(\sqrt{-\mathcal K}\) is chosen
with positive real part. Set
\[
 \mathcal A(c,x)=
 \frac{\sqrt{2\pi}\,\mathfrak a(c)\mathfrak a(c/2+x)^2}
 {\mathfrak a(x)^2\mathfrak a(c/2)^4\sqrt{-\mathcal K(c,x)}}.
 \tag{18}
\]
This is holomorphic and nonzero on \(\mathcal D\).
Its phase and branch are exactly those of the physical inner
packet, not a new uncalibrated saddle solution.

On every fixed compact subset, (17) and analytic Taylor
expansion give constants \(\eta,\mu>0\) such that
\[
 \Re\{F_c(c/2+t;x)-\Phi(c,x)\}\le-\mu t^2
                                      \qquad(|t|\le\eta).
 \tag{19}
\]
Lemma 1 and compactness give a strictly positive loss on
\(\eta\le|t|\le1/5\). After decreasing \(\mu\), (19) therefore
holds throughout \(|t|\le1/5\). This bounds every retained
row, including the two cutoff ends.

## 4. The complete holomorphic central packet

**Theorem 2.** For either \(\sigma\in\{0,1/2\}\), uniformly on
compact subsets of \(\mathcal D\),
\[
 \boxed{\quad
 \mathcal H_{\sigma,N}(c,x)
  =N^{-1}\mathcal A(c,x)e^{N\Phi(c,x)}
                                  (1+O(N^{-1})).
 \quad}
 \tag{20}
\]
Both level parities are included. On every smaller compact set,
all fixed mixed \(c,x\) derivatives of the normalized error are
\(O(N^{-1})\).

*Proof.* The bounds (10) and (19) control every term outside a
growing Gaussian window, relative to \(e^{N\Re\Phi}\).
Inside \(|d|\le N^{1/2+1/16}\), exact symmetry makes both
phase and symbol even in \(t=d/N\), so
\[
 F_c(c/2+d/N;x)
     =\Phi(c,x)+\frac{\mathcal K(c,x)d^2}{2N^2}
                                      +O(d^4/N^4).
 \tag{21}
\]
The symbol differs from its central value by \(O(d^2/N^2)\).
The ordinary Gaussian Poisson identity gives, for both
lattice shifts,
\[
 \sum_{d\in\mathbb Z+\sigma}
       e^{\mathcal K d^2/(2N)}
   =\frac{\sqrt{2\pi N}}{\sqrt{-\mathcal K}}
                                      (1+O(e^{-\gamma N})).
 \tag{22}
\]
Uniformity follows from the positive real parts of
\(-\mathcal K\) and \((-\mathcal K)^{-1}\) on compact sets.
This Gaussian summation identity is used only to evaluate
the localized finite sum; it drops no current of the original
factorial source.

Gaussian moment estimates make the quartic phase error
\(O(d^4/N^3)\) and the quadratic symbol error \(O(d^2/N^2)\)
both relative \(O(N^{-1})\) after summation. The row error
in (10) has that same relative size. The remaining tails,
including the extension in (22) outside the finite cutoff,
are exponentially or stretched-exponentially smaller.
Multiplying the row power \(N^{-3/2}\) by the
\(\sqrt N\) Gaussian density yields (20) with exactly (18).

For derivatives, the functions in (3) are holomorphic on
the fixed domain (4), and \(\mathcal A\) is nonzero.
Apply the already proved uniform estimate on a slightly
larger compact neighborhood to
\[
 \frac{N e^{-N\Phi(c,x)}\mathcal H_{\sigma,N}(c,x)}
                 {\mathcal A(c,x)}-1.
 \tag{23}
\]
Cauchy estimates on nested bidisks give all fixed mixed
derivatives, with no differentiation of a moving cutoff.
\(\square\)

In particular (20) is a complete nonzero inner packet at
\(c=c_*\) and on a fixed complex neighborhood of that point.
It does not follow by continuing the physical
\(O(N^{-1})\) asymptotic through an oscillatory outer sum;
it is proved directly for the exact source (3) on its
whole complex domain.

## 5. Parity and the remaining outer-source obligation

For an actual total index \(m\), equation (7) selects the
correct parity \(\sigma\) of \(m/2\). The two functions
\(\mathcal H_{0,N}\) and \(\mathcal H_{1/2,N}\) are distinct
exact holomorphic sources with the same leading packet.
No equality, or exponentially small difference, between
them is needed here. An outer contour treatment may keep
the even and odd \(m\) sums separately, each at spacing
\(2/N\), retaining their original endpoints and aliases.

To replace the full physical inner sum in the merged pair,
one must additionally bound the literal discarded rows (8)
below the final outer critical rate, and retain every
complementary total index. A relative \(O(N^{-1})\) error
on the physical axis would not suffice for that step.
Neither that quantitative discarded-source estimate nor
the complete outer contour is asserted in this note.
The exact original outer scalar remains \(e^{2\pi i(N-1)x}\).

Finally, the \(c\)-derivatives in (23) are derivatives of
the chosen finite interpolants (3). They are not identified
with an ordinary normal adapter of the original finite
source. Exact physical central-row equality and any
compiled complementary rows remain the interface.

