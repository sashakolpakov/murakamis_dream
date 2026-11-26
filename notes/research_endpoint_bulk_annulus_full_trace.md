# The full-normal bulk annulus for shared microscopic endpoints

Private written proof, 16 November 2026.

The moderate scalar compatibility theorem puts a full shared endpoint
product into the original double-pole trace on a compact physical
bulk window. One global scalar is used throughout the window. Its
artificial subdivision sides cancel exactly; the two external
vertical currents remain. No half-charge substitution or separate
normal-defect current is introduced.

This is a local source-placement result. It estimates neither the
joint spectator nor the external currents and does not complete the
whole original contour.

## 1. One scalar on the entire bulk interval

Retain
\[
 N\ge2,\quad D=N-1,\quad\eta=(-1)^D,\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 \tau_j=\pi-(2j+1)\pi/N,
\]
\[
 K_N(w,Z)=\sum_{k=0}^{D}e_k(w)e_k(Z),\qquad
 Q_N(Z;\boldsymbol\alpha)
       =\prod_{i=1}^{r}K_N(2\cosh(\alpha_i/N),Z).
 \tag{1}
\]
Here \(r\) is fixed, including \(r=0\), and all \(\alpha_i\) range
over fixed bounded complex disks. Multiplication in (1) is ordinary
multiplication before an original trace; no degree restriction is
imposed on the product.

Choose fixed \(0<a<b<\pi\), with fixed buffers inside this interval
and inside \((0,\pi)\) whenever needed. The scalar compatibility
theorem supplies one holomorphic scalar \(h_{i,N}(x,\alpha_i)\)
on a fixed neighborhood of a closed interval containing
\[
          \left[\frac{\pi-b}{2\pi},\frac{\pi-a}{2\pi}\right]
\]
in its interior. It has polynomial norm, matches the actual values
and first spectral normals at every covered physical node, and
is given by the global compact-interval repair in that theorem.
Define on a fixed neighborhood of the positive angular window
\[
 x_N(t)=\frac{\pi-t-\pi/N}{2\pi},\qquad
 \widehat Q_N(t;\boldsymbol\alpha)
             =\prod_{i=1}^r h_{i,N}(x_N(t),\alpha_i).
 \tag{2}
\]
Thus \(\widehat Q_N\) and its fixed derivatives have polynomial
bounds on smaller fixed domains. Its value and angular derivative
at \(\tau_j\in[a,b]\) are exactly those of \(Q_N(-2\cos t)\).
Since \(\sin\tau_j\ne0\), this includes the full spectral first
normal. The common scalar keeps all shared product-rule terms.

Define it on the separate negative window by
\[
                         \widehat Q_N(-t)=\widehat Q_N(t).
 \tag{3}
\]
This is an even holomorphic function on the union of two separated
neighborhoods. No extension across the central gap, through zero,
or to \(\pm\pi\) is required.

For all sufficiently large \(N\), choose midpoint endpoints
\[
 a_N=a+O(N^{-1}),\quad b_N=b+O(N^{-1}),\quad
 0<a_N<b_N<\pi,\qquad
               e^{iNa_N}=e^{iNb_N}=-\eta.
 \tag{4}
\]
They enclose a set \(\mathcal J_N=\{j:a_N<\tau_j<b_N\}\) of
distinct double physical roots. The odd simple root is outside.
Take a fixed sufficiently small \(H>0\) such that both closed
rectangles
\[
 \mathcal R_N^+=[a_N,b_N]+i[-H,H],\qquad
 \mathcal R_N^-=-\mathcal R_N^+
 \tag{5}
\]
and neighborhoods of them lie in the domains of (2)--(3).
All small levels not covered by the bulk theorem are excluded
from the asymptotic assertion; no finite-level approximation
is made at the levels to which it applies.

## 2. Exact positive-window and symmetric-annulus formulas

Let \(A_N(Z;\mathbf u)\) be the actual remaining joint spectator.
It may retain every other kernel, coupon, trace variable, and
ordinary free boundary parameter. Assume its angular pullback is
holomorphic on neighborhoods of (5), jointly in the parameters
being used. In particular an original polynomial spectator has
this property. Keep an original signed integer crossing power \(n\)
and its scalar
\[
 C_{N,n}=\exp\!\left(\frac{\pi i nD^2}{4N}\right),\qquad
 E_{N,n}(t)=\exp\!\left(\frac{inN}{4\pi}t^2\right).
\]
Set
\[
 g_N(t)=\sin t\,\widehat Q_N(t)A_N(-2\cos t;\mathbf u)E_{N,n}(t),
 \qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{6}
\]
On the separated domains \(g_N\) is odd and \(W_N\) is even.
The growth of \(A_N\), including any other crossing factors inside
it, is retained without an estimate.

Define the original bulk contribution by its full spectral rows:
\[
 \begin{split}
 \phi_{\mathcal J_N}(R^nQ_NA_N)
 =\eta\sum_{j\in\mathcal J_N}\big[
 &(4-c_j^2)\partial_Z(R^nQ_NA_N)(c_j)\\
 &-c_j(R^nQ_NA_N)(c_j)\big].
 \end{split}
 \tag{7}
\]
The crossing in this expression uses its original full Hermite
values and first normals. The exact original Gaussian identity
and (2) give
\[
        \phi_{\mathcal J_N}(R^nQ_NA_N)
                    =2\eta C_{N,n}\sum_{j\in\mathcal J_N}g_N'(\tau_j).
 \tag{8}
\]
The factor two is necessary: a positive angular lift represents a
double spectral root with both of its symmetric angular lifts.
For example \(2\cos\tau_j=-c_j\) supplies the value term in (7),
and differentiating the spectral spectator supplies
\(4\sin^2\tau_j\partial_Z=(4-c_j^2)\partial_Z\).
Differentiating \(E_{N,n}\) gives the original crossing normal.

**Theorem 1.** With the counterclockwise orientation on
\(\partial\mathcal R_N^+\), one has
\[
 \boxed{\quad
 \phi_{\mathcal J_N}(R^nQ_NA_N)
       =-\frac{N^2C_{N,n}}{\pi i}
                         \oint_{\partial\mathcal R_N^+}g_N(t)W_N(t)\,dt.
 \quad}
 \tag{9}
\]
Equivalently, the coefficient is
\(-N^2C_{N,n}/(2\pi i)\) if the contour is the sum of the
counterclockwise boundaries of both rectangles in (5).

Writing the result with lower horizontal segments gives
\[
 \boxed{\begin{split}
 \phi_{\mathcal J_N}(R^nQ_NA_N)
 ={}&-\frac{N^2C_{N,n}}{\pi i}
  \left\{\int_{-b_N-iH}^{-a_N-iH}
              +\int_{a_N-iH}^{b_N-iH}\right\}
                                  g_N(t)W_N(t)\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
       \int_{-H}^{H}
       \frac{g_N(b_N+iv)-g_N(a_N+iv)}
                            {4\cosh^2(Nv/2)}\,dv .
 \end{split}}
 \tag{10}
\]
Both outer vertical currents are part of this equality.

*Proof.* At every physical angle \(\tau\),
\[
           W_N(t)=-\frac{\eta}{N^2(t-\tau)^2}+O(1).
 \tag{11}
\]
There is no simple-pole coefficient. Hence the residue of \(g_NW_N\)
is \(-\eta g_N'(\tau)/N^2\). The positive rectangle encloses
precisely \(\{\tau_j:j\in\mathcal J_N\}\), so the residue theorem
and (8) prove (9). Reflection \(t\mapsto-t\) maps its oriented
boundary to that of the negative rectangle and leaves the
differential \(g_NW_N\,dt\) invariant. This proves the alternative
normalization.

The lower positive side has its usual left-to-right orientation.
Reflection maps the upper positive side, with its right-to-left
orientation, to the lower negative segment from
\(-b_N-iH\) to \(-a_N-iH\). Thus those two sides give the two
integrals in the first line of (10). The right side is directed
up and the left side down, so their sum is
\[
 i\int_{-H}^{H}
       [g_N(b_N+iv)W_N(b_N+iv)
                    -g_N(a_N+iv)W_N(a_N+iv)]\,dv .
\]
At either midpoint in (4),
\[
                       W_N(a_N+iv)=W_N(b_N+iv)
                                      =-\frac{\eta}{4\cosh^2(Nv/2)}.
 \tag{12}
\]
Multiplying by the coefficient in (9) proves the second line
of (10), including its sign. No contour through the central gap
has been used. \(\square\)

The kernel is exactly the original unit-charge kernel. On either
lower segment its convergent expansion is
\[
                   W_N(t)=\sum_{\ell=1}^{\infty}
                       \ell\eta^{\ell-1}e^{-i\ell Nt}.
 \tag{13}
\]
Every alias and the factor \(\ell\) encoding the first normal
remain. Neither a half-charge kernel nor a separate defect term
occurs in (9)--(10).

## 3. Internal subdivisions and permitted deformations

Use the same global scalar (2) if the positive window is divided
into finitely many adjacent midpoint rectangles with the same
height. Their oriented common vertical sides cancel exactly:
the meromorphic differential on both sides is identical.
After reflection the same assertion holds for the negative
window. The two external currents in (10) survive with opposite
signs. This is exact cancellation of artificial boundaries,
not an estimate on the external boundaries.

In particular the varying local cutoffs used to prove scalar
compatibility do not create a collection of patch-dependent
normal currents here. The global compact-interval repair was
chosen once before the trace. Formula (10) would generally
require additional interface terms if different arbitrary
representatives were substituted independently on its pieces.

Each lower segment may also be replaced by a path with the
same endpoints, homotopic within the corresponding lower
holomorphic domain of the *whole* integrand. Cauchy's theorem
then preserves its integral and leaves both vertical currents
unchanged. The theorem does not provide an analytic extension
or a phase bound outside that domain.

## 4. Coupled graphs, outer faces, and the unreplaced source

The construction is coefficientwise in every other original
variable. For several traced vertices with fixed bulk windows,
first multiply the microscopic endpoint factors sharing each
vertex and represent them by (2). Let \(A_N(\mathbf z;\mathbf u)\)
retain all graph edges and all remaining spectators jointly.
On a common product neighborhood, the simultaneous restricted
trace is exactly
\[
 \begin{split}
 \left[\prod_{v\in T}
                  -\frac{N^2C_{N,n_v}}{\pi i}\right]
 \int_{\prod_{v\in T}\partial\mathcal R_{v,N}^+}
 A_N((-2\cos t_v)_{v\in T};\mathbf u)
 \prod_{v\in T}
   [\sin t_v\,\widehat Q_{v,N}(t_v)
                 E_{N,n_v}(t_v)W_N(t_v)\,dt_v].
 \end{split}
 \tag{14}
\]
Any remaining original traces are still applied to this expression.
Finite contour integration and those linear traces commute in
the common domain. Ordinary outside derivatives commute as well.
Shared colors and every mixed first normal are retained.

Expanding (10) at each vertex in (14) gives the tensor product of
one horizontal term and its two signed external vertical terms.
All intersections of these external faces are included in that
expansion. One cannot retain only the horizontal product without
estimating or otherwise accounting for the other terms.
Artificial internal subdivision faces cancel before or after
this tensorization, because the same joint differential is used.

The full original trace splits exactly into the bulk rows (7)
and their complementary physical rows. For several vertices this
is the corresponding finite expansion of bulk and complementary
row choices. The complementary rows retain their original
values and normals, including the odd simple-root value.
There is no reduction of an ordinary free boundary variable.

Thus the added assembly is a bounded scalar amplitude on the
compact bulk window with its original double-pole functional.
Whole-current control still requires the actual joint spectator,
the two external window currents, the complementary endpoint
rows, and any subsequent deformation to be handled coherently.
No source growth or noncancellation claim is made.

## 5. Coverage and direct sources

The original exact trace source already gives full-period and
central symmetric-window rectangle formulas. The two-half-plane
source gives global representatives with an explicit real
interface. The scalar compatibility theorem changes what can
be placed on a *bulk annulus*: one polynomially bounded scalar
now preserves both physical channels on both separated windows.
Equations (9)--(14) record its exact normalization and graph
assembly without an internal interface or a hidden normal defect.

The complete direct source proofs were read at these unchanged
versions, their used implications checked, and their hashes matched:

* [Bulk scalar compatibility](research_microscopic_endpoint_bulk_scalar_compatibility.md),
  SHA256 2b8713ed16b66f5faa004403ac1d032021eee0a6f8f38082481d002c672c0b2e:
  global compact-interval scalar repair, bounded complex endpoint
  parameters, and shared full-normal products.
* [Exact complete trace contour](research_exact_complete_trace_contour.md),
  SHA256 a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8:
  derivative sampling, original Gaussian carrier, double-pole
  kernel, midpoint currents, and all positive-charge aliases.
* [Two half-plane endpoint source](research_endpoint_two_half_plane_relative_source.md),
  SHA256 985fa3331379c3877734f28773d314b667ee87fa63314a5ef4513a3fe128d194:
  full-normal normalization at both parities and exact joint
  spectator placement; the prior interface construction used
  for comparison above.

Only written mathematics, source-text reads, and file hashes were
used. No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts remain unchanged.
