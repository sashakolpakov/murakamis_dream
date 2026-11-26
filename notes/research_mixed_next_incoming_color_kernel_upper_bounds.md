# Incoming-color bounds on the original inner contours

Private finite-source deduction, 9 November 2026. The shortened first
edge has its complete-color phase upper bound uniformly for every
real incoming ordinary color. It therefore has the same bound, with
any prescribed fixed exponential tolerance, on a fixed complex
neighborhood of the complete color. The first-edge trace deletion
also extends to that neighborhood, including the radical rows that
revive at odd levels away from the complete color.

These are upper bounds for exact finite polynomials and exact trace
errors. No variable-color nonzero packet, outer Fourier estimate,
or complete attachment conclusion is asserted here. No mathematical
numerical evaluation, import, compilation, or frozen-source edit is
used.

## 1. Original kernels and the shortened first edge

Keep
\[
 \begin{gathered}
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad M=\lceil N/2\rceil,
 \quad U=m-1,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad \eta=(-1)^D,\\
 c_a=2\cos((2a+1)\theta),\quad
 S_j=\prod_{\nu=1}^j2\sin(\nu\theta),\quad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\\
 K_N(w,x)=\sum_{j=0}^{D}e_j(w)e_j(x),\qquad
 K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),\\
 \phi_N(f)=\eta N^2[x^D]\operatorname{rem}_{\,2T_N(x/2)+2}f,\qquad
 R_N(c_a)=\kappa(-1)^a q^{a(a+1)},\quad
 \kappa=q^{D^2/2},\qquad
 \mathcal A_N=\mathbb C[x]/(2T_N(x/2)+2).
 \end{gathered}
 \tag{1}
\]
The full Hermite trace, including every first normal and odd simple
node, is used throughout.

Let \(\Omega=\mathbb C\setminus[2,\infty)\), and retain the original
holomorphic slit-plane profile
\[
 \Psi(x)=\int_0^{1/2}
  2\operatorname{arsinh}\!\left(\frac{\sqrt{2-x}}2\cot(\pi s)\right)ds,
 \qquad \Psi(-2\cos t)=\psi(t,0).
 \tag{2}
\]
The square root has positive real part; the inverse hyperbolic sine
is principal. The normalization and the equality in (2) are those
of the adopted first-short slit theorem.

**Proposition 1.** Let \(\mathcal C\) be a compact subset of
\(\Omega\), and let \(\varepsilon>0\). There is a fixed complex
neighborhood \(V_\varepsilon\) of the real interval \([-2,2]\)
such that
\[
 |K_N^<(w,x)|\le C_\varepsilon
                  e^{N\{\Re\Psi(x)+\varepsilon\}},
 \qquad w\in V_\varepsilon,\quad x\in\mathcal C.
 \tag{3}
\]
For every fixed \(j,k\ge0\), on smaller fixed neighborhoods,
\[
 \left|\partial_w^j\partial_x^k
       \{e^{-N\Psi(x)}K_N^<(w,x)\}\right|
                         \le C_{\varepsilon,j,k}e^{N\varepsilon}.
 \tag{4}
\]
All sufficiently large levels of both parities are included.

*Proof.* Corollary 3, (23), of the slit theorem gives, for any
\(\tau>0\),
\[
 \sup_{w\in[-2,2]}|K_N^<(w,x)|
          \le C_\tau e^{N\{\Re\Psi(x)+\tau\}},
 \tag{5}
\]
uniformly on a slightly larger compact subset of \(\Omega\).
This is an estimate of the original coherent kernel from its exact
physical-row interpolation, including precisely the \(m\) double
nodes at odd levels. It is not a comparison of moduli of two
coherent kernels.

Let \(2\mathcal E_\rho\) be the filled ellipse with foci \(\pm2\)
and Chebyshev parameter \(\rho>1\). Polynomial degree \(U<N/2\)
and cosine orthogonality give on that ellipse
\[
 |K_N^<(w,x)|\le2(U+1)\rho^U
                   \sup_{\xi\in[-2,2]}|K_N^<(\xi,x)|.
 \tag{6}
\]
Take \(\tau<\varepsilon/4\), then \(\log\rho<\varepsilon/2\);
absorb the polynomial factor using the remaining tolerance.
The ellipse contains all of \([-2,2]\) in its interior.
The normalized function in (4) is holomorphic on the enlarged
product domain. Cauchy's formula on smaller fixed domains, using
the same argument with a smaller initial tolerance, proves (4).
No division by the kernel is made. \(\square\)

Every fixed old first-angle contour contained in
\[
 t=a-ih,\qquad |a|\le a_F<\pi,\quad |h|\le1
 \tag{7}
\]
maps into a fixed compact subset of \(\Omega\). At \(a=0\) the
image is negative real; for \(h=0\) it is below \(2\); otherwise
its imaginary part is nonzero. Thus (3)--(4) apply on all such
contours with the original \(\psi(t,0)\). The half-grid cuts
converging to a fixed angle below \(\pi\) are included uniformly.
Removed samples approaching \(\pi\) are treated separately in
Section 4.

## 2. What can be said pointwise for the full first edge

The original radical Fourier theorem gives, for \(0\le r<m\),
\[
 \sup_{w\in[-2,2]}|e_{D-r}(w)|\le\sqrt{N-1},\qquad
 |e_{D-r}(-2\cos t)|\le\sqrt{N-1}\,e^{D|\Im t|}.
 \tag{8}
\]
At even levels these are exactly all indices beyond \(U\).
At odd levels there is in addition \(j=m\). Its exact expression is
\[
 e_m(w)=\frac{(-1)^m}{N}Q_d(w),\qquad
 Q_d(w)=U_m(w/2)-U_{m-1}(w/2),\qquad
                    \|e_m\|_{[-2,2]}\le1.
 \tag{9}
\]
Here \(S_m^2=N\), \(Q_d\) is the monic polynomial of the double
nodes, and \(\|Q_d\|_{[-2,2]}\le N\). Chebyshev degree \(m\)
therefore bounds this middle row by
\(2(m+1)e^{m|\Im t|}\) at \(-2\cos t\).

It follows, uniformly for real \(w\), that
\[
 |K_N(w,-2\cos t)-K_N^<(w,-2\cos t)|
                     \le C N^A e^{D|\Im t|}.
 \tag{10}
\]
Degree \(D\) in \(w\) extends (10) to a fixed neighborhood of
\([-2,2]\), at cost \(e^{N\varepsilon}\). Consequently, on
each compact family (7), the full kernel has the bound
\[
 |K_N(w,-2\cos t)|
 \le C_\varepsilon e^{N\{\max(\Re\psi(t,0),|\Im t|)
                                      +\varepsilon\}}.
 \tag{11}
\]

On the signed central box
\[
 |\Re t|\le\pi/2,\qquad |\Im t|\le1
 \tag{12}
\]
the adopted whole-box complete-edge gap, evenness, and real
coefficients imply
\(\Re\psi(t,0)>|\Im t|+1/500\). Thus (11) reduces there to
the complete-color phase bound in (3), now for the full kernel.
The gap persists on a fixed larger neighborhood. Cauchy's formula
gives the corresponding normalized fixed ordinary and angular
derivatives with arbitrary tolerance, as in (4).

Beyond (12), (11) retains its maximum. It does not assert that the
full kernel is bounded by the shortened-edge phase on every right
connector. The following trace identity is the eligible way to
use the shortened edge on those connectors.

## 3. The full first-edge trace tail, with every revived odd row

For any incoming color \(w\), put
\[
 \begin{split}
 Q_{N,w}^{\rm sh}(X)
   &=\phi_N^{(x)}[R_N(x)^3K_N(w,x)K_N^<(x,X)],\\
 Q_{N,w}^{<<}(X)
   &=\phi_N^{(x)}[R_N(x)^3K_N^<(w,x)K_N^<(x,X)],\\
 E_{N,w}(X)&=Q_{N,w}^{\rm sh}(X)-Q_{N,w}^{<<}(X).
 \end{split}
 \tag{13}
\]
This error has degree at most \(D\) in \(w\) and \(U\) in \(X\).
Define the original exact contraction coefficients
\[
 b_{ra}=(-1)^{r+a}
 \frac{2\sin((2a+1)\theta)S_r^2}{S_{r-a}S_{r+a+1}},
 \qquad 0\le a\le r<m,\qquad |b_{ra}|\le2.
 \tag{14}
\]
At both parities retain the entire radical contribution
\[
 E_{N,w}^{\rm rad}(X)=
 \sum_{r=0}^{m-1}e_{D-r}(w)
       \sum_{a=0}^r b_{ra}R_N(c_a)^3K_N^<(c_a,X).
 \tag{15}
\]
At even levels \(E_{N,w}=E_{N,w}^{\rm rad}\). At odd levels the
exact middle-row contraction gives instead
\[
 \begin{split}
 E_{N,w}(X)=E_{N,w}^{\rm rad}(X)+e_m(w)
 \bigg\{&
 \sum_{a=0}^{m-1}(-1)^{m+a}2\cos((m-a)\theta)
                  R_N(c_a)^3K_N^<(c_a,X)\\
 &+R_N(-2)^3K_N^<(-2,X)\bigg\}.
 \end{split}
 \tag{16}
\]
The last term is the original simple-node term, with
\(R_N(-2)^3=q^{3m^2}\). Formula (16) uses the exact middle-row
Frobenius identity from the first-edge tail theorem (11).
At \(w=-2\) the terms (15) vanish at odd levels, but at a general
incoming color they do not. They have not been removed here.

The original all-index finite Newton estimates are
\[
 \sup_{\xi\in[-2,2]}|e_k(\xi)|\le C N^A e^{Nb_2},\qquad
 \sup_{|\Im u|\le2/3}|e_k(-2\cos u)|
                    \le C N^A e^{2N/3},\qquad 0\le k\le D,
 \quad b_2<729/1250.
 \tag{17}
\]
The angular supremum includes its full real period. Therefore
\[
 \sup_{\xi\in[-2,2]}
       |K_N^<(\xi,-2\cos u)|
            \le C N^A e^{N(b_2+2/3)}
                \quad(|\Im u|\le2/3).
 \tag{18}
\]
Combining (8)--(9), (14)--(18), and the unit moduli of the
physical crossing values proves the following bound before any
cancellation between terms.

**Proposition 2.** Uniformly for \(w\in[-2,2]\),
\[
 |E_{N,w}(-2\cos u)|\le C N^A e^{N(b_2+2/3)}
                  \quad(|\Im u|\le2/3),
 \tag{19}
\]
and the same bound holds for the sum of the absolute terms in
(15)--(16). For every \(\varepsilon>0\), there is a fixed
complex neighborhood \(V_\varepsilon\) of \([-2,2]\) such that
\[
 |E_{N,w}(-2\cos u)|
       \le C_\varepsilon e^{N(b_2+2/3+\varepsilon)}
 \quad(w\in V_\varepsilon,\ |\Im u|\le1/2).
 \tag{20}
\]
Every fixed mixed ordinary derivative in \(w,X\), with
\(X=-2\cos u\) in the closed height-\(1/2\) spectral ellipse,
has the same bound on a smaller incoming neighborhood.

Indeed (19) is a genuine real-interval bound for the degree-\(D\)
polynomial in \(w\). Apply (6) with that degree and
\(\log\rho\) arbitrarily small. The height-\(1/2\) spectral ellipse
is compactly inside the height-\(2/3\) ellipse in (19), so Cauchy
estimates give all ordinary \(X\)-normals as well, including its
two angular branch points. Cauchy estimates in a smaller incoming
ellipse give the \(w\)-normals. The contraction identities, rather
than a change to a distinct-node trace, consumed the particular
normals in (15)--(16).

## 4. Removed inner samples and short endpoint verticals

The first estimate in (17) is already a supremum over all real
ordinary colors. It is the estimate used for \(e_j(-2)\) in the
old far-sample proof. Thus replacing the complete end by real \(w\)
does not change its absolute budget. More explicitly, set
\[
 f_{N,w}^{<<}(t,u)
       =K_N^<(w,-2\cos t)K_N^<(-2\cos t,-2\cos u).
 \tag{21}
\]
Its ordinary degree in the traced coordinate is \(2U<N\).
For \(a_F=\pi-\pi/2000\), the literal termwise far bound of the
short-pair source transfer (22) becomes, with the same proof,
\[
 \sup_{a_F\le|t|\le\pi}|f_{N,w}^{<<}(t,u)|
   \le C N^A e^{NE_{\rm far}},\qquad
 E_{\rm far}=b_2+2/3+1/1000,
 \quad w\in[-2,2],\quad|\Im u|\le1/2 .
 \tag{22}
\]
Each incoming coefficient uses (17), each outgoing coefficient
uses its height estimate, and each of the two traced-angle Newton
polynomials has the old far-real rate \(1/2000\).

The same exact degree \(2U\) permits the old Markov estimates for
every first-normal sample and the old filled-ellipse continuation
to \(T_N+iv\), where
\[
 T_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},\qquad
 |v|\le h_c\le1/2000.
 \tag{23}
\]
In particular the original absolute removed derivative-sample sum
and the entire two-sided midpoint vertical, with their full
\(N^2C_{N,3}/\pi\), sine, crossing and \(W_N\) factors, retain the
rate \(E_{\rm far}+1/2000\). This is the absolute estimate preceding
the action comparison in the short-pair transfer (24)--(26).
No lower-\(u\) action comparison is imported for a different
outside domain.

Explicitly, these finite sources are unchanged except for \(w\):
\[
 \begin{gathered}
 C_{N,3}=q^{3D^2/4},\quad
 \tau_j=\frac{2\pi}{N}(D/2-j),\quad
 g_{N,w}(t,u)=\sin t\,f_{N,w}^{<<}(t,u)e^{3iNt^2/(4\pi)},\\
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\\
 \mathcal R_{N,w}(u)=
       \eta C_{N,3}\sum_{|\tau_j|\ge T_N}\partial_tg_{N,w}(\tau_j,u),\\
 \mathcal V_{N,w}(u)=
       \frac{\eta N^2C_{N,3}}{\pi}
       \int_{-h_c}^{h_c}
       \frac{g_{N,w}(T_N+iv,u)}{4\cosh^2(Nv/2)}\,dv .
 \end{gathered}
 \tag{23a}
\]
The bounds just stated hold also for the separate absolute sum and
absolute integral in (23a). The central odd node is not among
these removed endpoint samples; it remains in the full lower
trace contour.

The new incoming dependence is polynomial of degree at most \(D\).
Applying Chebyshev continuation to the real-\(w\) bounds just
proved gives the same complete estimates with any prescribed
\(+\varepsilon\) rate on a fixed incoming neighborhood. One may
perform this continuation to each derivative sample and each
vertical integrand before its positive sum or integral: the
degrees and bounds are uniform, and the number of samples is
polynomial. This also retains incoming normals on a smaller
neighborhood. There is no slit-plane extrapolation at \(t=\pi\).

## 5. Exact outer compatibility and remaining assembly

The adopted low-edge reduction proves, with arbitrary polynomial
incoming dependence,
\[
 e_M(X)\{K_N(X,x)-K_N^<(X,x)\}=0
             \quad\text{in }\mathcal A_N^{(X)}[x].
 \tag{24}
\]
Thus in the original outer observation
\(\phi_N^{(X)}[R_N(X)^3e_M(X)Q_{N,w}^{\rm full}(X)P_N(X)]\)
the second edge may be shortened exactly for every \(w\), and
after every fixed incoming derivative. The inner trace remains
full. Equations (13)--(20) then give the separate first-edge
trace error, with the odd revived rows retained.

On each old slit-compact inner contour the retained first edge
can now be bounded by its original complete-color phase with an
arbitrarily small fixed loss, by Proposition 1. Sections 2 and 4
supply the full central-kernel and far-sample/vertical upper
bounds where those source proofs require them. All these statements
concern the actual finite sources.

To obtain a sharp uniform outer Fourier bound one must still
assemble the specified inner and outer contours with their
original second-edge sources, alias penalties, endpoint sectors
and Gaussian phase comparison. A bound for an individual edge is
not itself such an assembly. In particular no pointwise
relative \(O(N^{-1})\) error is inserted into a cancelling outer
sum here, and no nonzero coefficient at variable incoming color
is inferred.

## 6. Frozen source bindings

| Source | SHA-256 |
| --- | --- |
| [First-short slit-plane theorem](research_mixed_next_first_short_edge_slit_plane_bound.md) | efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b |
| [Radical contraction and Fourier theorem](research_high_newton_radical_contraction.md) | 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03 |
| [Original first-edge tail](research_mixed_next_inner_three_first_edge_tail_contraction.md) | b31ac2d1cbf5f0e3ab4b71b36af9718151bced51e6959ee32b26ccf7fac5dfe6 |
| [Short-pair source transfer](research_mixed_next_inner_three_short_pair_source_transfer.md) | a835236285224a9df4ac41451c84882609b44b223eaa2c7c359f0f48518bccae |
| [Complete-edge gap](research_internal_pair_complete_edge_gap.md) | 1ac5e324eeb4f11425b6937332e08a682c802ce3d1fb3b6646cf7ecffed38ac3 |
| [All-index Newton source](research_mixed_next_outer_far_angles_and_verticals.md) | 5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d |
| [Exact second-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md) | 76524c28bdbafafe8922993093e3e5b4447ec033e4b0dd3928295047bfde797a |
