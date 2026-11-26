# Freeing the incoming color on the taller inner-three rectangle

Private finite-source theorem, 9 November 2026. The complete
inner-three packet on the outgoing rectangle of height \(7/10\)
persists when its incoming ordinary color varies in a fixed complex
disk about \(-2\). The remote currents are controlled first for
every real incoming color, using exact finite polynomials, and
then on a complex disk. No continuation of an error estimate known
only at the single color \(-2\) is used.

Both full edges, the full Hermite trace, all normal and simple-node
terms, and both level parities are retained. This is a boundary
source theorem, not a full ordinary closing or arbitrary
composition theorem. No mathematical numerical evaluation,
saved-value arithmetic, import, compilation, test, or frozen-source
edit is used.

## 1. Exact source and statement

Use the original notation
\[
\begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 c_a=2\cos((2a+1)\pi/N),\\
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\\
 \mathcal K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),\\
 \phi_N(f)=(-1)^D N^2[x^D]\operatorname{rem}_{\,2T_N(x/2)+2}f,
 \qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)} .
\end{gathered}                                                     \tag{1}
\]
The crossing \(R_N\) is unchanged. Define the complete source
\[
 Q_N(w,u)=\phi_N\!\left[
  R_N^3\mathcal K_N(w,x)\mathcal K_N(x,-2\cos u)\right],
 \qquad
 \mathcal V_+=\{\beta-iK:0\le\beta\le\pi/2,\ 0\le K\le7/10\}.
                                                                    \tag{2}
\]
In particular \(w\) is an ordinary color, not an incoming
angular coordinate.

The [complete rectangle theorem](research_mixed_symmetric_closing_complete_inner_asymptotic.md)
fixes the original critical point \(t_0(u)=a_0(u)-iH(u)\) and
\[
 \Phi_0(t,u)=\psi(t,0)+\psi(t,u)+3it^2/(4\pi)-it,\qquad
 S_0(u)=\Phi_0(t_0(u),u).
                                                                    \tag{3}
\]
Uniformly on \(\mathcal V_+\),
\[
 0<a_0<\pi/2,\quad 2/3<H<1,\quad
 s_0(u):=\Re S_0(u)>321/200,\quad
 \Phi_{0,tt}(t_0,u)\ne0.                                            \tag{4}
\]
No phase constant is changed below.

**Theorem.** There is \(r>0\), independent of \(N\) and parity,
and holomorphic functions \(S(w,u)\), \(A(w,u)\) on a neighborhood
of
\[
 \{|w+2|\le r\}\times\mathcal V_+
\]
such that \(A\ne0\) there after a fixed shrink and
\[
 \boxed{\quad
 Q_N(w,u)=C_{N,3}N^{-3/2}A(w,u)e^{NS(w,u)}
                         \{1+O(N^{-1})\}.
 \quad}                                                            \tag{5}
\]
The bound is uniform on that product. At \(w=-2\), these functions
are exactly the original \(S_0(u)\) and coefficient of the complete
rectangle theorem.

On smaller incoming disks, all fixed incoming derivatives of the
normalized relative error are \(O(N^{-1})\), uniformly for
\(u\in\mathcal V_+\). All fixed mixed \(w,u\) derivatives have
the same property on compact subsets of the outgoing interior.
The latter may equivalently use the ordinary outgoing coordinate
\(-2\cos u\). No normalized-error bound outside the closed
outgoing rectangle is asserted.

The exact incoming action derivative is
\[
 S_w(-2,u)=-\frac{\cos(t_0(u)/2)}{4\pi}\ne0 .                         \tag{6}
\]
Consequently, for each fixed integer \(j\ge0\),
\[
 \partial_w^j Q_N(-2,u)
 =C_{N,3}N^{j-3/2}A(-2,u)
       \left\{-\frac{\cos(t_0(u)/2)}{4\pi}\right\}^{j}
       e^{NS_0(u)}\{1+O(N^{-1})\},                                 \tag{7}
\]
uniformly on the entire closed outgoing rectangle. Equation (7)
is an ordinary derivative statement for the original full source.

## 2. Uniform finite control for real incoming colors

First shorten both edges, without changing the trace. For
\(t\) in the original lower contour, set
\[
\begin{gathered}
 f_{N,w}(t,u)=
  \mathcal K_N^<(w,-2\cos t)K_N^<(t,u),\\
 g_{N,w}(t,u)=\sin t\,f_{N,w}(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-(-1)^D e^{-iNt})^2}.
\end{gathered}                                                     \tag{8}
\]
The exact current prefactor remains
\(-N^2C_{N,3}/(\pi i)\).

The decisive first-factor input is the complete real outside-period
bound (23) of the [slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md):
for every fixed compact first-angle contour below a cut strictly
smaller than \(\pi\), and every fixed \(\tau>0\),
\[
 \sup_{w\in[-2,2]}
 |\mathcal K_N^<(w,-2\cos t)|
 \le C_\tau e^{N(\Re\psi(t,0)+\tau)} .                              \tag{9}
\]
The angular image is a compact subset of
\(\mathbb C\setminus[2,\infty)\), at both signs of the first
real angle. At the imaginary axis it is negative real.
This is an exact physical-row interpolation bound, including the
odd double-node range. It does not assert a pointwise comparison
with the complete-color coherent kernel.

Here is the full remote-current inventory.

* On the signed central horizontal, outside a fixed small
  neighborhood of \(t_0(u)\) and outside a still smaller center
  interval, the second edge has the independent packet of
  [the taller mixed theorem](research_mixed_symmetric_closing_taller_mixed_edge.md).
  Combine it with (9). Its calibrated concavity gives
  \[
   \Re\Phi_0(a-iH(u),u)
       \le s_0(u)-(a-a_0(u))^2/(8\pi).
                                                                    \tag{10}
  \]
  For negative \(a\), the exact evenness of the second finite edge
  and the calibrated signed phase are those in that theorem;
  no conjugation of a fixed crossing is used.

* The imaginary-axis interval is handled by the same exact
  polynomial bridge, uniformly in real \(w\).
  Choose the \(A,\eta,\epsilon_0\) of equations (49)--(51) of
  that theorem. On \(\eta\le a\le A\), (9)--(10) supply its
  required bound \(CN^B e^{N(s_0-\epsilon_0+H)}\).
  As a polynomial in \(x=-2\cos t\), \(f_{N,w}\) has degree
  \(2U<N\). Clearing the denominator after
  \(x_{\rm tan}=\tan(a/2)\) therefore gives degree
  at most \(4U<2N\), smaller than the original bridge's
  allowed degree \(3N\). Its same Chebyshev interval extension,
  clearing factor and crossing costs preserve a fixed gap.
  Restoring \(W_N\) cancels the displayed \(NH\), exactly as
  in the original proof. Every constant is uniform in \(w\).

* On the full left connection and the right far connection,
  the proof of the [fixed-remainder theorem](research_mixed_symmetric_closing_fixed_low_remainder.md),
  Sections 3--4, uses the first factor only through its
  \(\Re\psi(t,0)\) upper bound. Equation (9) supplies precisely
  that bound at all real \(w\). The same second-edge degree
  cost, negative or positive crossing, half-grid endpoint
  kernel, and original action comparison are unchanged.

* On the diagonal taper and its vertical, the
  [paid taper theorem](research_mixed_symmetric_closing_diagonal_taper.md)
  uses the same first bound and the unchanged second-edge
  saddle-or-endpoint envelope. Both phase comparisons therefore
  remain valid with (9).

* On the entire low horizontal, the
  [row-norm theorem](research_mixed_symmetric_closing_low_horizontal_norm.md)
  uses the first edge only in its slit bound (26).
  The exact Cauchy--Schwarz estimate for the second edge,
  its mirror-profile curvature, and the retained outgoing
  action loss do not involve \(w\). Thus its complete
  \(1/100\) gap remains valid, with a sufficiently small
  tolerance in (9).

For the removed far physical samples, use the all-real
Newton estimate \(|e_j(w)|\le CN^B e^{Nb_2}\) for \(w\in[-2,2]\).
This is the same bound used for \(e_j(-2)\) in Section 2 of the
fixed-remainder theorem. The product in (8) has the same degree
\(2U\) in the sampled spectral variable. Its Markov estimate
therefore pays every first normal on the far real interval,
and its fixed filled-ellipse continuation pays the two complete
short endpoint verticals. The exact odd simple node is still
part of that contour identity. No new residue is removed.

Choose a fixed small central interval
\[
 I(u)=[t_0(u)-\epsilon,\ t_0(u)+\epsilon]                             \tag{11}
\]
with \(\epsilon>0\) so small that it lies strictly inside the
positive first-angle portion and the common local packet charts.
All complements just listed have a uniform strict gap, once this
interval is fixed. Their proofs estimate absolute currents, so
one may take the minimum of their finitely many reserves and
then choose every occurrence of \(\tau\) in (9) smaller than a
fixed fraction of that minimum.

It follows that, for some fixed \(g>0\),
\[
 Q_N^{<<}(w,u)=I_N(w,u)+\mathcal R_N(w,u),\qquad
 |\mathcal R_N(w,u)|\le C e^{N(s_0(u)-g)}
       \quad(w\in[-2,2],\ u\in\mathcal V_+),                      \tag{12}
\]
where \(I_N\) is the exact current (8) over (11), with its original
prefactor. Equality in (12) is the original full Hermite contour
identity, not an approximation at a single incoming color.
For each fixed \(u\), both terms on its right are polynomials
of degree at most \(U\) in \(w\). The possible nonholomorphic
dependence of the chosen endpoints on \(u\) has no effect on
this polynomial assertion or on its uniform bound.

## 3. Restoring both full edges and continuing the remainders

The [integer-power deletion theorem](research_all_integer_crossing_edge_deletions.md)
already treats the exact error
\(Q_N(w,u)-Q_N^{<<}(w,u)\), for every \(w\in[-2,2]\), with both
parity inventories. For \(n=3\), its estimates (6)--(8) give
\[
 |Q_N-Q_N^{<<}|
 \le CN^B\exp N\left\{2b_2+K/2+K^2/(4\pi)\right\}
 \le CN^B e^{N\,623/400}.                                         \tag{13}
\]
The strict floor \(s_0>321/200\) leaves a fixed reserve. These
identities retain the radical contractions, the revived odd
middle row, and the odd simple-node kernel. The error in (13)
is a polynomial of degree at most \(D\) in \(w\).

Let \(\mathcal E_\rho\) be the filled ellipse with foci
\(-2,2\) and Chebyshev parameter \(e^\rho\), \(\rho>0\).
For every polynomial \(P\) of degree \(d\),
\[
 \sup_{\mathcal E_\rho}|P|
     \le 2(d+1)e^{d\rho}\sup_{[-2,2]}|P|.                          \tag{14}
\]
Apply this separately to the exact remainder in (12) and
the exact deletion error (13), for each fixed \(u\).
Their degrees are at most \(U\) and \(D\), respectively.
Choose a sufficiently small fixed \(\rho>0\), then absorb
the polynomial factors into the remaining reserves. Since
\(-2\) lies in the interior of the filled ellipse, it contains
a fixed disk about \(-2\). On a slightly smaller such disk,
for a fixed \(g_1>0\), we have
\[
 Q_N(w,u)=I_N(w,u)+O(e^{N(s_0(u)-g_1)}),
                   \qquad u\in\mathcal V_+.                     \tag{15}
\]
This step uses an entire real interval of eligible finite-source
bounds. It never continues a small error from the single value
\(w=-2\), and it does not extend a shortened-edge bound to
the full first edge pointwise.

## 4. Local ordinary-color packet and critical deformation

The independent neighborhood in Theorem 1 of the taller mixed
theorem contains every \((t_0(u),0)\) and \((t_0(u),u)\),
uniformly over the compact outgoing rectangle. Near the former
set its first-edge phase, symbol and exact normalized error are
even in their second angular variable \(v\). For the phase this
also follows directly from its closed original one-form and
the value at \(v=0\); its \(v\)-derivative is odd. The symbol
formula and finite kernel are visibly even. Thus they descend
holomorphically through
\[
                         w=-2\cos v=-2+v^2+O(v^4)
\]
to an ordinary disk about \(-2\).
Write their descended phase and symbol as
\(\psi_{\rm in}(t,w)\) and \(a_{\rm in}(t,w)\).
Their normalizations at \(-2\) are exactly
\(\psi(t,0)\) and \(a_e(t,0)\).

The original local two-short integrand therefore has phase
\[
 \Phi(t;w,u)=\psi_{\rm in}(t,w)+\psi(t,u)
                         +3it^2/(4\pi)-it                         \tag{16}
\]
and edge coefficient \(N^{-3}a_{\rm in}(t,w)a_e(t,u)\),
with holomorphic relative error \(O(N^{-1})\) on fixed smaller
charts. On those charts the complete sampling factor is
\[
 W_N(t)=e^{-iNt}\{1+O(e^{-cN})\},\qquad c>0,                        \tag{17}
\]
because their depths have a uniform positive lower bound.
No higher charge is dropped without this exponential estimate.

The nonzero original Hessian and compactness give a unique
holomorphic solution \(t_*(w,u)\), near \(t_0(u)\), of
\(\Phi_t=0\) for \(w\) sufficiently close to \(-2\). The local
solutions patch by uniqueness. They preserve the original
logarithmic lift and Hessian square root. Define
\[
\begin{split}
 S(w,u)&=\Phi(t_*(w,u);w,u),\\
 A(w,u)&=\frac{i\sqrt{2\pi}}{\pi}
 \frac{\sin t_*(w,u)\,a_{\rm in}(t_*(w,u),w)
                          a_e(t_*(w,u),u)}
                   {\sqrt{-\Phi_{tt}(t_*(w,u);w,u)}} .
\end{split}                                                       \tag{18}
\]
Every factor is nonzero on a fixed smaller product neighborhood.

Here the finite local contour, rather than only its phase, may
be moved. Translate the central part of (11) to pass horizontally
through \(t_*(w,u)\) and join its endpoints back to the two
original endpoints. For a sufficiently small fixed incoming
disk, all these segments stay in the common analytic packet
chart and strictly below the sampling poles.
At \(w=-2\), the portions at the two ends have the strict
quadratic loss supplied by (10). Uniform continuity preserves
a fixed end loss for the short joins and exterior pieces.
Also \(\Re\Phi_{tt}<0\) persists on the central chart.
Cauchy's theorem and the local complex Gaussian calculation,
with the same left-to-right orientation, consequently give
\[
 I_N(w,u)=C_{N,3}N^{-3/2}A(w,u)e^{NS(w,u)}
                              \{1+O(N^{-1})\}.                    \tag{19}
\]
This is uniform in \(u\) on the closed rectangle and in \(w\)
on a fixed disk. The error includes the exponentially small
joins and charges. No moving-endpoint derivative is inferred
from (19).

Shrink the incoming disk once more so that
\[
                    |\Re S(w,u)-s_0(u)|<g_1/4 .
\]
The remainder in (15), divided by the nonzero leading term
in (19), then decays exponentially. Equations (15),(19)
prove (5).

## 5. Exact derivatives and scope

The exact normalized error
\[
 E_N(w,u)=C_{N,3}^{-1}N^{3/2}A(w,u)^{-1}
                         e^{-NS(w,u)}Q_N(w,u)-1                   \tag{20}
\]
is holomorphic in both variables on the fixed local product
neighborhood. Equation (5) bounds it on a disk in \(w\)
times the full closed outgoing rectangle. Cauchy's formula
in \(w\) proves the uniform incoming derivative statement.
On an outgoing interior compact, Cauchy's formula in both
variables gives all fixed mixed derivatives. The ordinary
outgoing change of coordinates is valid there because
\(\sin u\ne0\). This argument uses the final exact function
(20), not derivatives of the nonholomorphic contour choices.

At \(v=0\) the original edge derivative is
\[
 \psi_{vv}(t,0)=-\frac{\cos(t/2)}{2\pi}.
\]
Since \(w+2=v^2+O(v^4)\), it gives
\(\partial_w\psi_{\rm in}(t,-2)=-\cos(t/2)/(4\pi)\).
The critical-point derivative contributes zero to \(S_w\),
proving (6). The first half-cosine is uniformly nonzero on
the compact selected image. Differentiating (5) using (20)
therefore gives (7), including its relative error and
original scalar.

This proves a complete incoming ordinary neighborhood for
the larger inner source. It does not extend the outgoing
rectangle, estimate the outer closing trace's complement,
or prove stability for arbitrary short partial fillings.
In particular the positivity of a physical Gram diagonal
plays no role in this result: its lower bound comes from
a nonzero local coefficient and strict bounds for every
remaining signed current.

## Frozen source bindings

- Complete original inner source and calibrated coefficient:
  4e6d58951cff746a5daf6b3efcf3df917233e64d773d936a232dbc6bb870c96c.
- Exact full contour and its original remote inventory:
  03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0.
- Independent edge packets, signed phase and exact center bridge:
  01630dd45f907e7d116fc8d51fed0ef00e13176f379b5ce1ab0186403cd1a94c.
- All-real incoming slit bound and its exact cardinal source:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Original incoming polynomial continuation and normal data:
  9ffa400456a8439d55352156707fab0aacfb8f1f8b0f622fd66824c9f1e553db.
- Both full-edge deletions for every real incoming color:
  f7abba0175c558ee9ca7f94799f9cd4d58adc249fea3f6b8c425e55a8136da66.
- Complete diagonal taper and right vertical:
  7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Complete low-horizontal current with original normalization:
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- All-real Newton rows, including far samples and endpoints:
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.

