# The exact retained-polytope contour for the prepared adjacent source

Research note, 3 November 2026.

This note keeps the original lattice cuts while expanding every retained
cell into horizontal and vertical contour pieces. Finite differences of
the actual indicator collect the internal faces. In particular, the
slanted \(j-k\) cutoff has two mixed-current sheets; they are retained
along the entire staircase, not only at its ends.

The identity is exact at every applicable level and retains the ordinary
boundary polynomial and its normal derivatives. The
[boundary-current estimate](research_three_crossing_global_horizontal_and_wire_tails.md)
bounds all its nonprincipal terms. The
[full local asymptotic](research_three_crossing_full_boundary_asymptotic.md)
combines those estimates with the principal integral.

## 1. Interpolation and the actual cuts

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), and the exact scalar
\(A_N\) and original factorial interpolation \(\mathfrak G_N\) from
[the prepared source formula](research_three_crossing_prepared_boundary_sum.md).
Thus \(\mathfrak G_N(j)=S_j\). Define
\[
\begin{split}
 f_N(x,y,z;u)={}&A_NN^3\kappa^2
 \exp\!\left\{\frac{i\pi N}{2}
 [(x-y)^2-x+y+2xz+2z^2]+\frac{i\pi}{2}(x-y)\right\}\\
 &\times
 \frac{\mathfrak G_N(N(x+y))}
 {\mathfrak G_N(Ny)^2\mathfrak G_N(Nx)
  \mathfrak G_N(Nz)^3\mathfrak G_N(N(x-z))}
 \mathcal B_N(y,u),                                             \tag{1}\\
 \mathcal B_N(y,u)={}&
 \frac{N}
 {\mathfrak G_N(D/2-Ny+Nu/(2\pi))
  \mathfrak G_N(D/2-Ny-Nu/(2\pi))\mathfrak G_N(Ny)^2}.
\end{split}
\]
The last formula uses the exact factorial reflection identity.
At \(x=j/N,y=i/N,z=k/N\), (1) is precisely the complete summand,
including its outside scalar, in Proposition 1 of that note.
Also \(\mathcal B_N(i/N,u)=e_i(-2\cos u)\).

Choose integer cuts and put
\[
 \chi_N(j,i,k)=
 {\bf1}_{L_x\le j\le R_x}\,
 {\bf1}_{L_y\le i\le R_y}\,
 {\bf1}_{k\ge K}\,{\bf1}_{j-k\ge P}.                              \tag{2}
\]
The required application has limiting cuts
\[
 L_x/N,L_y/N\to1/10,\quad R_x/N\to1/2,\quad
 R_y/N\to2/5,\quad K/N\to1/100,\quad P/N\to1/400.                 \tag{3}
\]
Take integer rounding so the retained real colors obey the intended
strict or weak inequalities; all real cell boundaries differ from (3)
by \(O(N^{-1})\). In particular, for all sufficiently large \(N\),
all retained cells have
\[
 x,y,z>0,\qquad x,y,z<1,\qquad 0<x-z<1,\qquad 0<x+y<1.            \tag{4}
\]
The actual retained finite source is
\[
 Z_N^{\rm ret}(u)=
   \sum_{j,i,k\in\mathbb Z}\chi_N(j,i,k)
                       f_N(j/N,i/N,k/N;u).                    \tag{5}
\]
The sum is finite. The real outer-color removals are proved in
[the global preparation-error note, Section 6](research_three_crossing_global_preparation_error.md),
and the two wire removals in
[the horizontal and wire-tail note](research_three_crossing_global_horizontal_and_wire_tails.md).
No removal of a contour current is inferred from those real-lattice
estimates.

The divisor formula
\(\operatorname{ord}_{s=m}\mathfrak G_N(s)=\lfloor m/N\rfloor\),
proved in [the rectangular-extension note](research_adjacent_pair_rectangular_extension.md),
shows that (1) is holomorphic on a neighborhood of every retained
cell with arbitrary fixed finite imaginary heights. The shifted
Newton reciprocals also remain holomorphic for all \(u\) in a fixed
sufficiently small complex neighborhood of zero. The inequalities
in (4) are strict by fixed margins in the application. Thus no
factorial pole is crossed in any product contour below.
Every such interpolation and contour integral is even in \(u\).
The local analytic coordinate \(w+2=2-2\cos u=u^2+O(u^4)\)
therefore makes each of them holomorphic in the ordinary boundary
variable \(w\), including at \(w=-2\). Ordinary boundary derivatives
below refer to this exact even descent.

Fix positive heights \(H_x,H_y,H_z\), and the principal orientation
\[
                    \epsilon=(-1,+1,+1).                       \tag{6}
\]
The selected heights are \(H_x=-\Im x_*\), \(H_y=\Im y_*\),
\(H_z=\Im z_*\). Write \(r\in\{x,y,z\}\) for a coordinate and set
\[
 K_r(\zeta)=\frac1{1-e^{2\pi iN\epsilon_r\zeta}},
 \qquad I_\ell=[(\ell-1/2)/N,(\ell+1/2)/N],
 \qquad b_\ell=(\ell+1/2)/N.                                   \tag{7}
\]

## 2. The one-cell identity, with its orientations

For a function of the three variables define operators acting in the
\(r\)-th coordinate:
\[
\begin{split}
 \mathsf H_{r,s}^{\ell}f
   &=\epsilon_rsN\int_{I_\ell}
        f(\ldots,t+isH_r,\ldots)K_r(t+isH_r)\,dt,
               &&s\in\{+1,-1\},\\
 \mathsf V_r^\ell f
   &=-i\epsilon_rN\int_{-H_r}^{H_r}
        f(\ldots,b_\ell+it,\ldots)K_r(b_\ell+it)\,dt .
\end{split}                                                     \tag{8}
\]
Different coordinate operators commute. The exact one-cell formula is
\[
 f(\ldots,\ell/N,\ldots)
 =(\mathsf H_{r,+}^{\ell}+\mathsf H_{r,-}^{\ell}
                      +\mathsf V_r^\ell-\mathsf V_r^{\ell-1})f.
                                                                    \tag{9}
\]
Indeed the residue of \(K_r\) at \(\ell/N\) is
\(-\epsilon_r/(2\pi iN)\). Integrating counterclockwise around
\(I_\ell+i[-H_r,H_r]\), multiplying by \(-\epsilon_rN\), and
retaining the top, bottom, right, and left orientations gives (9).
The vertical lines are half-grid lines and contain no pole.

## 3. Every collected current

For \(V\subseteq\{x,y,z\}\), define the finite difference
\[
 (\Delta_V\chi_N)(\ell)=
 \sum_{\delta\in\{0,1\}^{V}}(-1)^{|\delta|}
                          \chi_N(\ell+\delta),\qquad
 \Delta_\varnothing\chi_N=\chi_N .                              \tag{10}
\]
Coordinates outside \(V\) of \(\delta\) are zero. All sums in the next
formula are finite.

**Theorem 1.** The full retained source has the exact contour expansion
\[
 \boxed{\displaystyle
 Z_N^{\rm ret}(u)=
 \sum_{V\subseteq\{x,y,z\}}\;
 \sum_{\ell\in\mathbb Z^3}
 (\Delta_V\chi_N)(\ell)
 \sum_{s\in\{\pm1\}^{V^c}}
 \left(\prod_{r\in V}\mathsf V_r^{\ell_r}\right)
 \left(\prod_{r\notin V}\mathsf H_{r,s_r}^{\ell_r}\right)
 f_N(\,\cdot\,;u).}                                             \tag{11}
\]
This includes all horizontal copies, codimension-one currents, mixed
currents, and triple currents. It remains valid after every fixed
ordinary boundary derivative and for the conjugate source.

*Proof.* Tensor (9) for each original cell and multiply by
\(\chi_N\). For a fixed vertical coordinate, the face with index
\(\ell_r\) is the right face of cell \(\ell_r\) and the left face of
cell \(\ell_r+1\). Its coefficient is therefore
\(\chi_N(\ell)-\chi_N(\ell+e_r)\). Repeating this collection in
all coordinates of \(V\) gives (10), with exactly the signs in
(11). There is no assumption that a mixed finite difference is
supported only at corners. Every integral is over a compact
pole-free contour of the holomorphic interpolation, so finite
Fubini and ordinary boundary differentiation are legitimate.
Conjugation reverses the heights and coefficients together.
\(\square\)

The \(V=\varnothing\) term has eight horizontal pieces. On the
principal one \(s=\epsilon\), the orientation coefficient is
positive and the product of kernels is
\(1+O(e^{-2\pi N\min H_r})\). Its real integration domain is the
union of the retained cells; it differs from the limiting polytope
only by an \(O(N^{-1})\) boundary layer. For the other seven pieces
the kernels supply their full Fourier penalties, not an arbitrarily
selected mode.

All mixed current supports are specified by the exact formula (10).
The following consequences explain why they have a smaller rate list
than a radial deformation would give. Use \(n=\ell_x-\ell_z\).

* If \(y\in V\), then \(\ell_y=L_y-1\) or \(R_y\), because the
  \(y\) indicator in (2) is an independent interval.
* A single \(x\) difference is supported on the two \(x\) cuts or
  \(n=P-1\). A single \(z\) difference is supported on the lower
  \(z\) cut or \(n=P\).
* If \(x,z\in V\), its support lies either in
  \(n\in\{P-1,P\}\), or at an intersection of an \(x\) cut
  with \(\ell_z=K-1\). For the diagonal indicator alone,
  \[
  \Delta_x\Delta_z{\bf1}_{j-k\ge P}
       =\begin{cases}-1,&n=P-1,\\+1,&n=P,\\0,&\text{otherwise}.
         \end{cases}                                           \tag{12}
  \]
  Thus both entire sheets along the slanted staircase remain.

For the third statement, away from those two values of \(n\) the
diagonal indicator is constant on the four relevant vertices.
The mixed difference then factors as the product of the differences
of the separate \(x\) and \(z\) cutoffs, forcing their intersection.
This also proves the corresponding statements with an additional
\(y\) difference.

In particular an \(x\)-upper current with variable \(z\)-height is
forced onto the lower \(z\) cut or the diagonal cut. A diagonal current
with variable \(y\)-height is forced onto a \(y\) cut. These are
properties of the original finite indicator, not asymptotic guesses
about cancellation.

## 4. The exact exponential penalties

On a horizontal line and for all sufficiently large \(N\),
\[
 |K_r(t+isH_r)|\le
 \begin{cases}2,&s=\epsilon_r,\\
 2e^{-2\pi NH_r},&s=-\epsilon_r.
 \end{cases}
\]
On every vertical half-grid line,
\[
 K_r(b_\ell+it)=\frac1{1+e^{-2\pi N\epsilon_rt}},
 \qquad
 |K_r(b_\ell+it)|\le e^{-2\pi N(-\epsilon_rt)_+}.                 \tag{13}
\]
Consequently the exact rate to compare for a term of (11) is
\[
 \Re\Xi(v+ih;u)
 -2\pi\sum_{\substack{r\notin V\\s_r\ne\epsilon_r}}H_r
 -2\pi\sum_{r\in V}(-\epsilon_rh_r)_+ ,                         \tag{14}
\]
where \(h_r=s_rH_r\) for horizontal coordinates and
\(-H_r\le h_r\le H_r\) for vertical coordinates.
The real variables range over the cells or half-grid faces carrying
\(\Delta_V\chi_N\). There are only polynomially many such terms;
\(|\Delta_V\chi_N|\le2^{|V|}\). Uniform factorial bounds on these
fixed bulk sets therefore convert a strict rate gap in (14) into
an exponentially small bound for the corresponding complete
current.

The global horizontal-concavity theorem cited above implies convexity
of \(\Re\Xi\) in the simultaneous imaginary variables on the retained
limiting real polytope. The penalty in (14) is linear on each choice
of signs of the vertical heights. Thus, for rate comparisons, the
vertical heights reduce to
\[
                         h_r\in\{-H_r,0,H_r\}.                  \tag{15}
\]
This reduction uses only convexity on each of the sign boxes.
It does not discard any integral, and the support restrictions
following (12) must still be imposed at every vertex.
Finite \(O(N^{-1})\) shifts of the real cuts are handled by uniform
continuity on the same compact factorial domains, after a strict
limiting gap is proved.

## 5. Why a radial deformation needs extra coherent grouping

For comparison, a smooth polytope with the half-grid cuts
\[
 a\le x\le b,\quad c\le y\le d,\quad z\ge e,\quad x-z\ge p
                                                                    \tag{16}
\]
contains exactly the same lattice indices as (2), when
\(a=(L_x-1/2)/N\), \(b=(R_x+1/2)/N\), and similarly for \(c,d,e,p\).
A simultaneous imaginary translation produces a particularly simple
but less favorable exact identity.

Partition the integer Fourier modes in each coordinate according to
the sign of the height, assigning the zero mode to \(\epsilon_r\).
For \(\sigma\in\{\pm1\}^3\), put
\[
 h_\sigma=(\sigma_xH_x,\sigma_yH_y,\sigma_zH_z),\qquad
 \mathcal K_\sigma(\zeta)=
 \prod_r\frac{e^{2\pi iN\sigma_r\zeta_r\,{\bf1}_{\sigma_r\ne\epsilon_r}}}
                  {1-e^{2\pi iN\sigma_r\zeta_r}}.                 \tag{17}
\]
Let \(\mathcal P_N\) be (16). The corresponding exact identity is
\[
\begin{split}
 Z_N^{\rm ret}
 ={}&N^3\sum_\sigma\int_{\mathcal P_N}
       f_N(v+ih_\sigma)\mathcal K_\sigma(v+ih_\sigma)\,dv\\
 &-iN^3\sum_\sigma\int_0^1\int_{\partial\mathcal P_N}
    (h_\sigma\cdot\nu)\,
    f_N(v+it h_\sigma)\mathcal K_\sigma(v+it h_\sigma)\,dS\,dt .
\end{split}                                                      \tag{18}
\]
The slanted face \(z=x-p\), parameterized by \(x,y\), has coefficient
\(h_{\sigma,z}-h_{\sigma,x}\). The lower \(z\) face has coefficient
\(-h_{\sigma,z}\), and the two \(x\) and \(y\) faces have their usual
outward signed coordinate heights.

For completeness, insert a factor \(r^{|m|}\), \(0<r<1\), in each
Fourier mode. The sum of the eight kernels on the real domain is the
product of three Poisson kernels. Its integral, multiplied by \(N^3\),
converges to (5), because no lattice point lies on (16).
For each orthant, differentiate the translated integral with respect
to its translation parameter. The divergence theorem gives (18)
with the regularized kernels. The regulator can then be removed
in every individual face integral. On a coordinate half-grid face
one denominator is bounded below by one. On the slanted face the
\(x\) and \(z\) phases differ by a minus sign, so at least one of
their denominator moduli is at least one. Integrating the remaining
two denominators over their independent real coordinates gives
at most
\(C[1+\log_+(1/(Nt))]^2\), which is integrable at \(t=0\).
The same bound is uniform in \(r\). This proves (18) without an
unlisted principal-value current.

However, the radial face at the upper \(x\) cut cannot be bounded
by its pointwise absolute rate below the selected action. At its
limiting real point
\[
 x=1/2,\qquad y=z=1/4,\qquad t=0,
\]
the exact value is
\[
                  \Re\Xi=\frac{11G}{2\pi}>\frac85 .              \tag{19}
\]
Here \(\mathcal J(1/4)=-G/(2\pi)\),
\(\mathcal J(3/4)=G/(2\pi)\), and \(\mathcal J(1/2)=0\).
The strict lower comparison follows already from ten terms of
Catalan's alternating series and \(\pi<22/7\).
The selected action, on the other hand, is less than \(1.54\)
by its exact outward certificate. Continuity preserves this
inequality on a short positive translation interval.
Thus (18) would require additional coherent grouping on that
face. Formula (11) supplies the preferable exact representation:
it retains the independent height structure and the finite
difference supports that exclude this uncontrolled combination
from its upper-\(x\) currents.
