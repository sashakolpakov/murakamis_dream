# Actual crossed-block windows along a regular positive saddle family

Private written proof, 17 November 2026.

A crossed physical-product block can be continued beyond its thin
external seed neighborhood along an independently supplied regular
positive child-saddle family. The continued scalar is constructed
from the actual normalized row modes, not postulated as a model.
A finite Gaussian arc has the original seed-window values and
normals up to an exponential error. Its moving-endpoint derivative
terms are included in that error. A final short spectral repair
makes those original data exact throughout the prescribed target
domain and preserves a nonzero Gaussian coefficient.

The conclusion is an exact source representative for a closed
parent window. It keeps that window's exterior boundary currents
and all unmatched rows. It neither constructs the supplied saddle
family nor estimates the complete parent trace.

## 1. Original block and the geometric input

Use
\[
 D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 J=\lfloor D/2\rfloor,\quad
 F_j(C)=K_N(c_j,C),\quad
 G_j(C)=\left.\partial_zK_N(z,C)\right|_{z=c_j}.
 \tag{1}
\]
Fix the number \(m\ge1\), a positive integer \(p\), and
physical indices \(j_2,\ldots,j_m\). Their locations may vary
with \(N\). The original free source is the polynomial
\[
 H_{p,N}(w)=
 \phi_{N,C}\left(R(C)^pK_N(w,C)
                              \prod_{i=2}^mF_{j_i}(C)\right).
 \tag{2}
\]
It has degree at most \(D\) in \(w\). At every physical
external row,
\[
 H_{p,N}(c_j)=Z_{p,N}(j,j_2,\ldots,j_m),\qquad
 H_{p,N}'(c_j)=Z_{p,N,\{1\}}(j,j_2,\ldots,j_m)
 \tag{3}
\]
when the node is double. At the odd simple node only the
first equality is prescribed.

Let \(L\subset[-2,2)\) be a fixed eligible real seed interval:
a bulk interval or a fold interval from the short spectral
repair theorem. Choose a real buffer larger than \(L\).
The actual tuples with \(c_j\) in this buffer satisfy one
of the following adopted initializer conditions, uniformly:

* \(p\ge4\), with \(\sum_{i=1}^m j_i\ge\delta N\) for a fixed
  \(\delta>0\);
* \(p=2\) or \(3\), \(m\ge3\), with
  \(\sum_{i=1}^m j_i-D\ge\varepsilon N\) for a fixed
  \(\varepsilon>0\).

These are conditions on the actual physical tuples, with
\(j_1=j\). They are fixed before passing to shorter windows.
The other indices range over a compact macroscopic family
on which all geometric assumptions below are uniform.

Write \(C(t)=-2\cos t\). The original spectral edge action,
even in its angular lifts, is denoted by
\(\Psi_{\rm e}(w,C(t))=\psi(u,t)\), where \(w=-2\cos u\).
For \(x_i=j_i/N\), \(i\ge2\), put
\[
 \Phi(w,t)=\Psi_{\rm e}(w,C(t))
       +\sum_{i=2}^m\Psi_{x_i}(C(t))
       +\frac{ipt^2}{4\pi}-it,
\]
\[
 \Psi_x(C)=2\int_0^x
   \operatorname{arsinh}
       \left(\tfrac12\sqrt{2-C}\cot(\pi v)\right)\,dv .
 \tag{4}
\]
All branches and additive constants are the original ones.
At \(w=c_j\), the first term uses the centered external
degree \((j+\tfrac12)/N\); the initializer's \(j/N\)
profile differs by \(O(N^{-1})\) with fixed local
derivatives in the child variable \(t\).
This distinction changes no fixed contour gap. The actual
finite source logarithm below is not shifted.

Here is the independent geometric input. Let
\(\Omega_0\Subset\Omega_1\Subset\Omega_2\) be bounded
simply connected spectral domains with fixed buffers,
contained in \(\mathbb C\setminus[2,\infty)\).
They contain the seed interval and its buffer, as well
as the desired compact parent path in \(\Omega_0\).
Assume that on a neighborhood of \(\overline{\Omega_2}\)
there is a holomorphic critical branch \(\tau(w)\) with
\[
 \Phi_t(w,\tau(w))=0,\quad
 |\Phi_{tt}(w,\tau(w))|\ge\mu>0,\quad
 \Im\tau(w)\le-h_*<0,\quad
 |\Re\tau(w)|\le\pi-d_* .
 \tag{5}
\]
Every incident pair along this family belongs to the original
positive-edge domain, with a compact positive buffer.
Exact zero rows, whose factors are one, are omitted from
this geometric requirement.
On a neighborhood of the real seed, select the branch
by analytic continuation of the applicable initializer's
selected branch under the centered half-step change
\(j/N\mapsto(j+\tfrac12)/N\) in the free external degree.
Retain the original additive phase constants. The limiting
phases are related by the preceding \(O(N^{-1})\) comparison,
not by literal finite-\(N\) equality; the actual logarithmic
source calibration in Sections 4--5 remains unshifted.
The action and the family then have a common single-valued
continuation. In particular, with
\[
                         \mathcal S(w)=\Phi(w,\tau(w)),
 \tag{6}
\]
the Hessian square root is chosen by continuation of the
initializer's oriented Gaussian. The domains may be reduced
around a supplied path to obtain this simply connected
setting. No existence of such a path or branch is inferred.

The spectral formulation allows a seed containing \(w=-2\).
There the edge action and all spectral representatives
descend through the even angular lift. There is no choice
of a nonholomorphic square root as an external coordinate.

## 2. Statement

**Theorem.** Under the preceding assumptions, there are
holomorphic functions \(\Lambda_N\), \(a_N\) on a neighborhood
of \(\overline{\Omega_0}\), with
\[
 \Lambda_N=\mathcal S+o(1)
       \quad\hbox{with every fixed buffered derivative},\qquad
                      0<c\le|a_N|\le C,
 \tag{7}
\]
and a holomorphic Gaussian scalar \(B_N\) such that
\[
 B_N(w)=N^{3/2}q^{pD^2/4}a_N(w)e^{N\Lambda_N(w)}
                               (1+O(N^{-1})).
 \tag{8}
\]
The error is uniform and holomorphic on buffered smaller
domains. Thus \(B_N\) is zero-free there for large \(N\).
At every physical row in the original seed buffer,
\[
 \left|\partial_w^b(B_N-H_{p,N})(c_j)\right|
 \le N^B\exp\{N\Re\mathcal S(c_j)-\gamma N\},
                 \qquad b<\nu_j,
 \tag{9}
\]
where \(\nu_j=2\) at a double node and \(\nu_j=1\) at the
odd simple node. All constants and \(\gamma>0\) are fixed
before choosing the final short window.

There is a fixed \(\delta_0>0\) such that any consecutive
subwindow \(I_N\) in that seed, with at most \(\delta_0N\)
distinct rows, has a holomorphic representative
\(\mathcal B_{I,N}\) on the same target domain satisfying
\[
 \partial_w^b\mathcal B_{I,N}(c_j)
       =\partial_w^b H_{p,N}(c_j),
                     \qquad j\in I_N,\quad b<\nu_j,
 \tag{10}
\]
\[
 e^{-N\Lambda_N}(\mathcal B_{I,N}-B_N)=O(e^{-\gamma_1N})
 \tag{11}
\]
on the fixed compact, with every fixed buffered derivative.
It is zero-free and has the same relative asymptotic (8).
In particular,
\[
 |\mathcal B_{I,N}(w)|
          =\exp\{N\Re\mathcal S(w)+o(N)\}
 \tag{12}
\]
uniformly above and below, up to the displayed polynomial
factor. This is a source-window conclusion on a fixed
parent domain, without a restriction to the thin
neighborhood of the real initializer.

For any original spectator \(P(w;\ldots)\), including a
parent crossing and all other shared variables, a closed
positive spectral contour \(\gamma_I\subset\Omega_0\)
enclosing exactly the selected nodes obeys
\[
 \boxed{\quad
 \phi_{N,I}(P H_{p,N})=
 \frac{\eta N^2}{2\pi i}\int_{\gamma_I}
       \frac{P(w;\ldots)\mathcal B_{I,N}(w)}{P_N(w)}\,dw .
 \quad}
 \tag{13}
\]
This is the original selected-window functional, with its
entire normal product rule. It is not an off-grid
polynomial equality. Every side of \(\gamma_I\), every
unmatched row, and every difference between neighboring
window choices remains part of a subsequent assembly.

For negative \(p\), conjugate the entire supplied family,
the source and the construction. There is no assertion
for unit powers or for a supplied family violating (5).

## 3. Actual unit row functions on a finite Morse tube

We first construct the integrand; its nonzero normalized
amplitude is a consequence of the actual row theorems.
The parameterized holomorphic Morse coordinate is
\[
 t=T(w,\xi),\quad T(w,0)=\tau(w),\qquad
                \Phi(w,T(w,\xi))=\mathcal S(w)-\xi^2/2 .
 \tag{14}
\]
It is available uniformly for \(|\xi|<r_2\) after choosing
a fixed small radius. For an explicit construction take
the square root of
\(-2[\Phi(w,t)-\mathcal S(w)]/(t-\tau(w))^2\)
near the graph, with the chosen Hessian square root,
and invert \((t-\tau)\) times that function.
Uniform (5), buffers, and simple connectedness give
one holomorphic coordinate on the product
\(\Omega_2\times D_{r_2}\).
Shrink \(r_2\) so the entire tube stays in the lower
canonical strip and in the positive pair domains.

Cover this compact tube by finitely many of the
positive product charts from the pinned product
construction. They contain common small real child
and external seed intervals. In tangent coordinates
their angular domains can be chosen star shaped
about zero. Intersections therefore remain connected
to these common seeds. For the external spectral
fold use their even descent.

On each chart the short spectral source theorem gives
one separately even representative \(\mathcal K_{i,N}\)
with both original line families:
\[
 \begin{split}
 \mathcal K_{i,N}(c_j,C)&=F_j(C),\\
 \partial_w\mathcal K_{i,N}(c_j,C)&=\widehat G_j(C)
                                  \quad(\nu_j=2).
 \end{split}
 \tag{15}
\]
The analogous child-row identities also hold.
Here \(\widehat G_j\) is the pole-free original
Ward--Jacobi representative, whose inner physical
value and first normal agree with \(G_j\).
All charts use the same short line windows, chosen
only after their finitely many baseline exponents.
The external eligible interval can include the fold.
On its larger eligible seed buffer the baseline
already has exponentially small normalized line
errors. The short spectral corrections and their
fixed derivatives are exponentially small throughout
the compact product, so this larger-buffer line
accuracy persists even outside the short windows
where (15) is exact. This supplies the full seed
buffer in (9), before the final window is chosen.

These local representatives are actual units on a
smaller tube. To verify the lower bound, take the
child angle as the regular degree variable: it is
nonzero throughout (5). The regular-row theorem
constructs a unit \(\mathcal A_{i,N}\), with the
actual scalar anchor, satisfying
\[
           \log\mathcal A_{i,N}-N\Psi_{\rm e}=o(N)
 \tag{16}
\]
on its continuation chart. Its real child-window
value and independent normal errors are exponentially
small. The common baseline in the product theorem
compares exponentially to this same unit. Equivalently,
the comparison follows by its actual child-grid
zeros and finite analytic propagation from the
common real seed. The spectral symmetrization and
short repair change that baseline by an exponentially
small normalized amount. Therefore
\[
 \mathcal K_{i,N}=\mathcal A_{i,N}
                   +e^{N\Psi_{\rm e}}O(e^{-c_iN}),\qquad
 e^{-o(N)}\le
       |e^{-N\Psi_{\rm e}}\mathcal K_{i,N}|
                         \le e^{o(N)}.
 \tag{17}
\]
This uses no stability assumption based on
\(|\lambda|>1\) at the complex target. The regular-row
construction crosses \(|\lambda|=1\) by its analytic
graph equation and compares to the actual source
only in its proved real attracting buffer.

On any buffered overlap, the normalized difference
of two \(\mathcal K_{i,N}\) is exponentially small.
Indeed it has exact zeros at all common physical
child rows, as identities in the external parameter
by (15), and has an \(e^{o(N)}\) bound.
A disk Blaschke estimate on the common real child
seed gives \(e^{-cN+o(N)}\). A finite chain of
buffered disks in the connected intersection
propagates it to the required overlap. The constants
are uniform in its buffered external parameter
compact; derivatives follow by Cauchy.
The star-shaped intersections supply the required
common path. Equality in the physical ideal alone
would not have supplied this estimate.

Pull the normalized functions back by (14):
\[
 f_{i,N}(w,\xi)=
 e^{-N\Psi_{\rm e}(w,C(T(w,\xi)))}
                  \mathcal K_{i,N}(w,C(T(w,\xi))).
 \tag{18}
\]
After refining the finite cover, choose a cover
\(\{U_i\}\) of the buffered base by planar domains
such that each \(U_i\times D_{r_1}\), \(r_1<r_2\),
lies in one such chart. On overlaps,
\[
              f_{i,N}-f_{j,N}=O(e^{-cN})
 \tag{19}
\]
with a single positive \(c\), after decreasing it
to absorb the uniform \(o(N)\).

Here is an explicit bounded gluing operation.
Choose a fixed smooth partition \(\chi_i(w)\)
subordinate to this cover and set
\(f_N=\sum_i\chi_i f_{i,N}\).
Since \(\sum_i\bar\partial\chi_i=0\), (19) gives
\[
              \bar\partial_w f_N=O(e^{-cN}).
 \tag{20}
\]
The derivatives act at fixed \(\xi\), which is why
the Morse trivialization precedes this step.
On a fixed larger base domain \(\Omega'\), still
inside the supplied buffers, solve this equation
by the Cauchy--Green integral
\[
 u_N(w,\xi)=\frac1\pi\int_{\Omega'}
       \frac{\bar\partial_\zeta f_N(\zeta,\xi)}
                              {w-\zeta}\,dA(\zeta).
 \tag{21}
\]
Then \(\bar\partial_wu_N=\bar\partial_w f_N\).
The kernel \(1/|w-\zeta|\) is integrable with a
uniform bound on this fixed bounded domain.
Thus \(u_N=O(e^{-cN})\), and it is holomorphic in
\(\xi\). The function
\(\mathfrak a_N=f_N-u_N\) is jointly holomorphic
and differs from every local \(f_{i,N}\) by
\(O(e^{-cN})\) on smaller overlaps.
Fixed derivatives have the same conclusion after
reserving buffers.

By (17), the correction is smaller than each
local lower bound \(e^{-o(N)}\). Consequently
\(\mathfrak a_N\) is a unit, with upper and lower
size \(e^{o(N)}\), on the fixed smaller tube.
Its logarithm is chosen from one actual initial
chart. The local logarithms in (16), their
exponentially small ratios on overlaps, and the
finite connected cover show
\(\log\mathfrak a_N=o(N)\), with fixed buffered
derivatives. This also follows for derivatives
from the harmonic real logarithm and its two-sided
bound, after fixing the value at the initial point.

Define the resulting unit edge function on the tube,
in its original \(t\) coordinate, by
\[
 A_N(w,T(w,\xi))=
 e^{N\Psi_{\rm e}(w,C(T(w,\xi)))}\mathfrak a_N(w,\xi).
 \tag{22}
\]
Near the initial real external seed it differs
exponentially, in normalized size and fixed
derivatives, from the local exact representative
in (15). In particular at the actual external
nodes it has \(F_j\) and \(\widehat G_j\) as its
value and fixed-\(t\) spectral normal up to that
exponential error.

The order of choices is fixed: first all product
charts and their baseline margins; then common
short line windows for (15); then the overlap
exponent and the gluing; finally the smaller
external repair window in Section 6.

## 4. The actual logarithmic Gaussian scalar

The remaining factors in the block are kept literal.
On the child tube their spectral argument lies in
a fixed slit compact. The actual root product
makes each \(F_{j_i}\) a unit there, with its
original logarithm and all-row estimate
\[
             N^{-1}\log F_{j_i}(C)
                       =\Psi_{j_i/N}(C)+o(1).
 \tag{23}
\]
Fixed derivatives are included. Zero and last
rows cause no exception. Define
\[
 \Phi_N(w,t)=N^{-1}\log A_N(w,t)
       +N^{-1}\sum_{i=2}^m\log F_{j_i}(C(t))
       +\frac{ipt^2}{4\pi}-it.
 \tag{24}
\]
Equations (16)--(23) give
\(\Phi_N-\Phi=o(1)\) with fixed buffered derivatives.
The actual critical point \(t_N(w)\) is holomorphic,
is uniformly \(o(1)\) from \(\tau(w)\), and has
a uniformly nonzero Hessian. Put
\[
                         \Lambda_N(w)=\Phi_N(w,t_N(w)).
 \tag{25}
\]
Its Morse coordinate, with the initial orientation
continued, is
\[
 t=T_N(w,z),\quad T_N(w,0)=t_N(w),\qquad
             \Phi_N(w,T_N(w,z))=\Lambda_N(w)-z^2/2.
 \tag{26}
\]
It exists uniformly on a fixed smaller disk.
Choose \(r>0\) in that disk and retain the finite
arc with parameter \(-r\le z\le r\).
All its points have a fixed positive lower depth.

With the full original grid kernel
\[
                  W_N(t)=\frac{e^{-iNt}}
                                      {(1-\eta e^{-iNt})^2},
 \tag{27}
\]
define
\[
 \boxed{
 B_N(w)=-\frac{N^2q^{pD^2/4}}{\pi i}
   \int_{-r}^{r}
    \sin T_N\,A_N(w,T_N)\prod_{i=2}^mF_{j_i}(C(T_N))
    e^{ipNT_N^2/(4\pi)}W_N(T_N)
                           \partial_zT_N\,dz .
 }
 \tag{28}
\]
This is holomorphic in \(w\), with the parameter
endpoints fixed at \(\pm r\). The physical child
endpoints \(T_N(w,\pm r)\) are not fixed.
The definition retains their dependence.

On this lower tube the denominator in (27) is
\(1+O(e^{-cN})\) after its leading \(e^{-iNt}\)
is included in (24). Thus (28) is an ordinary
finite real Gaussian with phase
\(N\Lambda_N-Nz^2/2\) and analytic amplitude
\(\sin T_N\,\partial_zT_N\).
The amplitude and all needed derivatives are
uniformly bounded, and its value at zero is
a uniform unit. The symmetric odd term integrates
to zero, giving
\[
 B_N(w)=
 \frac{iN^{3/2}}{\pi}q^{pD^2/4}
 \sin(t_N(w))
 \sqrt{\frac{2\pi}{-\Phi_{N,tt}(w,t_N(w))}}\,
 e^{N\Lambda_N(w)}(1+O(N^{-1})).
 \tag{29}
\]
The square root is the continued oriented one.
The finite endpoints and all other aliases
contribute only exponential errors to this local
formula. This proves (7)--(8), with the displayed
nonzero coefficient; it was not assumed in advance.

## 5. Calibration to the original seed values and normals

At a physical external seed row, replace \(A_N\)
on (28) by \(F_j(C(t))\). Its fixed-\(t\) external
derivative is correspondingly replaced by
\(\widehat G_j(C(t))\).
Equation (22), including its fixed derivatives,
shows that these changes have exponentially small
normalized size. The literal other physical rows
remain in place.

The adopted initializer supplies the complete
original lower lens and its mixed-normal estimates,
uniformly in every physical seed row, including
fold limits. Near the seed, the actual critical
point in (24) differs exponentially from that of
the literal value-row product. Indeed their phase
derivatives differ exponentially by (22).
The finite arc in (26) can therefore be inserted
into that original lens by a small local deformation.
In a local Morse coordinate the initializer's
descending tangent lies strictly inside a Gaussian
descent sector. Its two short connections to the
real Morse arc can be chosen in that sector with
radius bounded below; they have a fixed quadratic
gap as well.
Keep the entire complement, including both
endpoints, the reflected half and all aliases.
On the complement of this arc it has a fixed
gap: locally the endpoints have the Morse loss
\(r^2/2\), and away from the local neighborhood
the initializer gives its original uniform gap.
The same is true with \(\widehat G_j\), at a
polynomial cost. This last substitution preserves
the complete child trace with all crossing normals;
it is not an off-grid equality with \(G_j\).

For clarity, differentiation of a moving arc
does produce endpoint terms. If \(J_N(w,t)\,dt\)
denotes its integrand before the original constant,
and \(t_\pm(w)=T_N(w,\pm r)\), then
\[
 \frac d{dw}\int_{t_-(w)}^{t_+(w)}J_N(w,t)\,dt
 =\int_{t_-(w)}^{t_+(w)}
                      \partial_wJ_N(w,t)\,dt
      +J_N(w,t_+)t_+'-J_N(w,t_-)t_-'.
 \tag{30}
\]
The integral derivative holds \(t\) fixed.
Both endpoint derivatives are uniformly bounded.
At the real physical seed their integrands have
size at most
\[
          N^B e^{N\Re\mathcal S(c_j)-r^2N/2+o(N)}.
 \tag{31}
\]
Thus these terms are retained and paid. They
cancel the corresponding boundary terms if
the complete complementary chain is differentiated.
Dropping them would not give the original normal.
The value, normal, and gluing comparisons above
prove (9), with any fixed sufficiently small
positive exponent below all the finitely many
source, overlap, and local Morse gaps.
At the odd simple row only the value is compared.
The spectral formulation makes the even last
normal regular and introduces no angular division.

This is the point at which the construction uses
the actual crossed block (2). An arbitrary unit
model with the same limiting phase would not
supply (22), (3), or the complete-lens comparison.

## 6. Exact short-window repair and the original parent trace

Normalize the actual seed error by the actual
reduced phase:
\[
 d_{j,b}=
 \left.\partial_w^b
       [e^{-N\Lambda_N(w)}(H_{p,N}(w)-B_N(w))]
                                      \right|_{w=c_j},
                       \qquad b<\nu_j .
 \tag{32}
\]
The derivative in (32) is determined by the
original value and normal in (3).
Equation (9), \(\Lambda_N-\mathcal S=o(1)\),
and \(\Lambda_N'=O(1)\) give
\[
                         |d_{j,b}|\le e^{-\gamma_0N}
 \tag{33}
\]
after decreasing a fixed positive exponent.

Let \(V_{j,b}\) be the ordinary spectral Hermite
cardinal polynomials of the pinned short-window
theorem, with the original multiplicities. On
any fixed buffered spectral compact \(K\),
its operator bound for \(n_I\) consecutive rows is
\[
 \left\|\sum_{j\in I_N}\sum_{b<\nu_j}
                       d_{j,b}V_{j,b}\right\|_K
 \le C N^B
   \exp\{C_Kn_I(1+\log(N/n_I))\}
                         \max_{j,b}|d_{j,b}|.
 \tag{34}
\]
The same bound holds for fixed derivatives on
smaller buffers. It is uniform at the fold,
using the actual quadratic node separation,
and prescribes no normal at an odd simple node.

Choose \(\delta_0>0\), only now, so that
\[
       C_K\delta_0(1+|\log\delta_0|)<\gamma_0/4,
 \tag{35}
\]
and set
\[
 E_{I,N}(w)=\sum_{j\in I_N}\sum_{b<\nu_j}
                                d_{j,b}V_{j,b}(w),\qquad
 \mathcal B_{I,N}=B_N+e^{N\Lambda_N}E_{I,N}.
 \tag{36}
\]
The exact cardinal identities prove (10).
Equations (33)--(35) prove (11), with fixed
derivatives after the usual buffers.
The normalized Gaussian in (29) has size
comparable to \(N^{3/2}\), whereas the correction
is exponentially small. This proves zero-freeness,
the same relative coefficient, and (12).
In particular the continuation constants and
interpolation losses are fixed operator bounds;
there is no uncontrolled propagation through
a large exact transfer matrix.

Finally, (10) and the original partial fractions
of \(1/P_N\) prove (13). The residue at a double
node is exactly
\[
 \eta\{(4-c_j^2)
       [P'(c_j)H_{p,N}(c_j)+P(c_j)H_{p,N}'(c_j)]
                          -c_jP(c_j)H_{p,N}(c_j)\}.
 \tag{37}
\]
At an odd simple selected node it is
\(P(-2)H_{p,N}(-2)\).
This includes the parent crossing derivative
and every shared spectator in its original
product rule.
All exterior sides of the closed contour
remain in (13). Replacing neighboring windows
by their own representatives creates their
actual difference on a common side; neither
zero-freeness nor (11) deletes that current
or pays an unrelated parent action.

## 7. Coverage and complete direct sources

The earlier one-sided characteristic and two-half
source theorems already supply row continuation,
Hermite kernels and exact window interfaces.
The compact endpoint seam theorem retains the
adjacent exterior currents. No new assertion
about those individual constructions is made here.
The new application is to the actual integrated
arbitrary-\(m\) crossed block: its unit integrand
is glued on a supplied regular saddle tube,
the actual logarithmic Gaussian is calibrated
with its moving-endpoint normal terms, and the
original block's prescribed window jets are
repaired on the full parent target domain.

The hypotheses (5), their coherent original
branches and the real initializer are essential.
Only the one free parent color is continued here;
the other inputs in (2) remain their literal
physical value rows.
This note does not prove their validity along
an arbitrary graph contour. It gives neither
a whole-grid off-real equality nor a nonzero
complete parent trace. Cuts and exterior
currents outside the fixed lower tube are
handled only at the real initializer by its
complete-lens theorem; no global cut term is
silently removed during continuation.

Complete direct texts and directly used
implications were read at these fixed pins:

* [Actual regular positive row continuation](research_physical_row_regular_positive_continuation.md),
  SHA256 3a7d81d55f60396c2e3058d5ebe967ae625ff47c4b527b4e102e37fa8f28d644:
  actual scalar anchor, unit modes across modulus
  crossings, full normal calibration and finite
  analytic comparison.
* [Common positive product baseline](research_positive_product_window_gluing.md),
  SHA256 ace4f667038c494e2690a77496ce32e8bc8538535356b78600e8ad8ced8183d5:
  fixed product domains, common seeds, unit-mode
  comparison, full line data and branch coherence.
* [Short spectral source repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550:
  separately even representatives, bulk/fold exact
  line data, uniform finite Hermite operator bound
  and original window multiplicities.
* [Bounded-minimax crossed initializer](research_crossed_physical_products_bounded_minimax.md),
  SHA256 07ad86f4b34ff057f6f1ebfad630b6b6b464aced08be875f047609aeda8e0bcf:
  complete actual scalar and all-row normal
  contour estimates for \(|p|\ge4\).
* [Power-two/three crossed initializer](research_crossed_physical_products_two_three_radial_contour.md),
  SHA256 15ed14b3cc0d2032832a3fcd7d6540f259aebb2dfbcf26f954b8e458be3f7662:
  the corresponding full scalar and normal
  estimates under strict support.

Only written mathematics, complete source reads,
and metadata hashes were used. No mathematical
programs, tests, numerical evaluations, or builds
were run. Frozen notes and public manuscripts
are unchanged.
