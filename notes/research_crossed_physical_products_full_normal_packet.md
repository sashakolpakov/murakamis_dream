# Full boundary normals and a scalar packet for crossed physical products

Private written proof, 17 November 2026.

The radial contour for a crossed product of physical value rows
also controls every original mixed first boundary normal. The
normal rows are replaced only inside the original trace by their
even Ward--Jacobi representatives. Their complete angular lens
is exact. Cofactor bounds pay its endpoint caps without dividing
by a row polynomial at a Jacobi root.

For selected bulk normal indices, the actual crossed scalar has
a nonzero leading normal coefficient. On a strict bulk tuple
chart, all these jets come from one holomorphic scalar packet:
its physical error is precisely the complement of a fixed
saddle arc. The exact scalar row correction removes an
independent normal-connection error from this comparison.

## 1. Source and conclusions

Use \(N\ge3\), \(D=N-1\), \(J=\lfloor D/2\rfloor\), and
\[
 \theta=\pi/N,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad c_j=2\cos((2j+1)\theta),\quad
 P_N(C)=2T_N(C/2)+2.
 \tag{1}
\]
The original trace, physical rows, and boundary normals are
\[
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,\qquad
 F_j(C)=K_N(c_j,C),\qquad
 G_j(C)=\left.\partial_wK_N(w,C)\right|_{w=c_j}.
 \tag{2}
\]
Only double physical nodes carry a prescribed \(G_j\).
The odd simple node carries its single value.

Fix \(m\ge3\), \(\varepsilon>0\), and an integer \(p\ge4\).
The indices satisfy
\[
             0\le j_i\le J,\qquad
             \sum_i j_i-D\ge\varepsilon N.
 \tag{3}
\]
For any subset \(I\) of the double-node positions put
\[
 Z_{p,N,I}(\mathbf j)=
  \phi_N\left(R^p\prod_{i\in I}G_{j_i}
                         \prod_{i\notin I}F_{j_i}\right),
 \qquad Z_{p,N}=Z_{p,N,\varnothing}.
 \tag{4}
\]
The ordinary factors are multiplied before the original
canonical trace. This notation retains all closing normals.

We use the actual saddle and action of the pinned radial
contour theorem. Namely, with \(\mathbf x=\mathbf j/N\),
\[
 \Psi_x(C)=2\int_0^x
   \operatorname{arsinh}
       \left(\tfrac12\sqrt{2-C}\cot(\pi u)\right)\,du,
 \quad
 \Phi_{p,\mathbf x}(t)=\sum_i\Psi_{x_i}(-2\cos t)
                         +\frac{ip t^2}{4\pi}-it,
 \tag{5}
\]
on the original slit branches. Its selected critical point
is \(t_p(\mathbf x)=s_p-ih_p\), with
\[
 0<s_p<2\pi/p\le\pi/2,\qquad h_p>0,\qquad
 M_p(\mathbf x)=\Re\Phi_{p,\mathbf x}(t_p)>0.
 \tag{6}
\]
All depths, endpoint distances, and critical Hessians have
uniform buffers under (3).
The actual finite-row phase has its nearby critical point
\[
 \Phi_{p,N}(t)=N^{-1}\sum_i\log F_{j_i}(-2\cos t)
                                  +\frac{ip t^2}{4\pi}-it,
 \qquad
 t_{p,N}=t_p(\mathbf j/N)+O(\log N/N).
 \tag{7}
\]
Set \(C_{p,N}=-2\cos t_{p,N}\). These spectral points lie
in a fixed compact subset of \(\Re C<2\).

**Theorem 1 (all physical mixed normals).**
There are constants \(B,B',C\), depending on \(m,\varepsilon,p\),
such that
\[
 |Z_{p,N,I}(\mathbf j)|
        \le C N^B e^{NM_p(\mathbf j/N)}
        \le C N^{B'}|Z_{p,N}(\mathbf j)|
 \tag{8}
\]
for every allowed \(I\), uniformly over (3) and both
parities. The second inequality holds for sufficiently
large \(N\). Zero rows, even last normals, and odd simple
value rows are included.

For \(0<x<1/2\) define the holomorphic function
\[
 g(x,C)=-
 \frac{2\operatorname{arsinh}
       \bigl(\tfrac12\sqrt{2-C}\cot(\pi x)\bigr)}
                  {4\pi\sin(2\pi x)}
 \tag{9}
\]
on the original slit branch.

**Theorem 2 (nonzero bulk normal coefficient).**
If every \(j_i/N\), \(i\in I\), belongs to a fixed compact
subinterval of \((0,1/2)\), then
\[
 \boxed{\quad
 \frac{Z_{p,N,I}(\mathbf j)}{Z_{p,N}(\mathbf j)}
   =N^{|I|}
       \left\{\prod_{i\in I}g(j_i/N,C_{p,N})
                         +O(\log N/N)\right\}.
 \quad}
 \tag{10}
\]
The error is uniform; unselected value indices may still
approach either endpoint or the fold. Every selected
factor in (10) is uniformly nonzero.

The scalar packet assertion is local in the external
degree variables. Let
\[
 \mathcal B\Subset
 \{\mathbf x\in(0,1/2)^m:\ \sum_i x_i>1\},\qquad
 C_N(x)=2\cos(2\pi x+\theta).
 \tag{11}
\]
For this assertion choose a support margin from the positive
minimum of \(\sum_i x_i-1\) on \(\mathcal B\).

**Theorem 3 (one common crossed scalar).**
There is a finite cover of \(\mathcal B\) by real product
neighborhoods with fixed thin complex neighborhoods, on
each of which a holomorphic scalar \(\mathcal W_{p,N}\)
satisfies
\[
 \left|
 \left[\prod_{i\in I}
        C_N'(x_i)^{-1}\partial_{x_i}\right]
       \mathcal W_{p,N}(\mathbf x)\Big|_{\mathbf x=\mathbf j/N}
                 -Z_{p,N,I}(\mathbf j)\right|
 \le C N^B e^{-\gamma N}|Z_{p,N}(\mathbf j)|
 \tag{12}
\]
at every physical tuple in the real product, for all
subsets \(I\), including the empty subset.
The constants \(B,\gamma>0\) are uniform on that product.
The physical error in (12) is solely the omitted part of
an exact angular lens. The scalar normal-connection rate
only limits the width of the complex neighborhood.

For \(p\le-4\), all conclusions follow by exact conjugacy.
In Theorem 2 conjugate the positive-power coefficient.
For Theorem 3 use
\(\mathcal W_{-p,N}(\mathbf x)
 =\overline{\mathcal W_{p,N}(\overline{\mathbf x})}\)
when \(p>0\).
No statement for \(|p|<4\), a further signed observation,
or an arbitrary composed source is made.

## 2. Exact even normal representatives on the full lens

Let \(\mathcal J_j\) be the actual Jacobi matrix and let
\[
 F_j^\epsilon(C)=
   \frac{\det(\mathcal J_j(\epsilon)-CI)}
                    {\prod_{r<j}A(r+\epsilon)},\qquad
 R_j(C)=\left.\partial_\epsilon F_j^\epsilon(C)\right|_0,
 \tag{13}
\]
with \(c_0\) held fixed in the common shift and \(R_0=0\).
The adopted full-normal contour theorem supplies
\[
 \widehat G_j(C)=
 \frac{c'(0)F_j(C)\widetilde Q_N(C)+R_j(C)}{c'(j)},
 \qquad c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{14}
\]
Here \(\widetilde Q_N\) is the original even Ward
representative of \(G_0\).
At \(j=0\), (14) is simply \(\widetilde Q_N\).
The numerator is a sum of polynomial cofactors and a
polynomial times \(\widetilde Q_N\); it has no
Jacobi-resolvent poles.

At every physical inner-\(C\) node, (14) has exactly the
value and every required first normal of \(G_j\).
Thus replacing any subset in (4) by these functions
preserves the original trace, including the derivative
of \(R^p\) and the entire product rule.
At the odd simple inner node only its value is required.
No off-grid polynomial equality is used.

Define the angular product
\[
 \widehat f_I(t)=
       \prod_{i\in I}\widehat G_{j_i}(-2\cos t)
                    \prod_{i\notin I}F_{j_i}(-2\cos t).
 \tag{15}
\]
It is even and holomorphic inside the canonical strip
\(|\Re t|<\pi\), and bounded up to its endpoints on every
fixed-height rectangle, at each fixed \(N\).
This follows from the even Ward representative and the
polynomial cofactors in (14).

The full-grid lens identity consequently extends to (15):
\[
 Z_{p,N,I}=
 -\frac{N^2q^{pD^2/4}}{\pi i}
 \int_\Gamma
       \sin t\,\widehat f_I(t)e^{ipNt^2/(4\pi)}
                  W_N(t)\,dt,
 \qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},
 \tag{16}
\]
where \(\Gamma\) is the original lower arc from
\(-\pi\) to \(\pi\).

Here is the precise extension of the polynomial source
identity. First put the real endpoints at \(\pm a\),
past the last physical angular lifts but inside
\((-\pi,\pi)\), and close the lower arc by \(t\mapsto-t\).
The odd function
\(\sin t\,\widehat f_I(t)e^{ipNt^2/(4\pi)}\)
has the actual derivative-sampling data of (4).
The residue and integration-by-parts proof in the pinned
full-grid lens applies without alteration. Evenness of
\(W_N\) makes the two reflected halves add, with the same
factor in (16). Then let \(a\to\pi\) at fixed \(N\).
The Ward endpoint bound and \(\sin t\to0\) make the short
endpoint connectors vanish. This is a fixed-level
identity before any uniform estimate. It needs neither
angular periodicity nor spectral holomorphy through
the cut at \(C=2\).

In particular there is no extra odd-center residue:
its derivative-sampling term is
\(\widehat f_I(0)\), precisely the original single
simple-node value. Formula (16) retains the complete
Fourier denominator and both endpoint connectors.

## 3. The normal factors preserve every complement gap

On every fixed spectral slit compact the source formula
(14) gives
\[
                 |\widehat G_j(C)|\le C N^B|F_j(C)|
 \tag{17}
\]
uniformly over all double rows, with buffered fixed
derivatives. Indeed
\[
 \frac{R_j}{F_j}
     =\operatorname{Tr}((\mathcal J_j-CI)^{-1}\mathcal J_j')
                          -\sum_{r<j}A'(r)/A(r).
 \tag{18}
\]
The Jacobi spectrum is real and exceeds \(c_0\).
For large \(N\), its distance from a fixed slit compact
is bounded below. The source bounds
\[
 \|\mathcal J_j'\|\le6\pi N^3,\quad
 |A'/A|\le4\pi,\quad |c'(j)|^{-1}\le C N^2,\quad
 |\widetilde Q_N|\le C_H N^2(1+\log N)
 \tag{19}
\]
then prove (17). The zero row uses the last bound directly.

The endpoint caps require a different estimate, because
they approach \(C=2\). Fix \(d>0\) small, take \(N\) large
enough that \(2-c_0\le d\), and put \(z_0=2-3d<c_0\).
For \(|C-2|\le d\) and every Jacobi eigenvalue
\(\lambda=c_0+r\), \(r>0\),
\[
 |\lambda-C|\le r+d+(2-c_0)
                  \le\lambda-z_0,\qquad
                   \lambda-z_0\ge2d.
 \tag{20}
\]
The original normalization therefore gives
\[
 |F_j(C)|\le F_j(z_0).
 \tag{21}
\]
Diagonalize the real symmetric Jacobi matrix before
differentiating its determinant. Every cofactor term in
\(R_j\) is a product with one \((\lambda-C)\) factor
omitted; its coefficient has modulus at most
\(\|\mathcal J_j'\|\).
Equation (20) bounds each such term, after the original
determinant normalization, by
\((2d)^{-1}F_j(z_0)\).
Including the derivative of the denominator gives
\[
 |R_j(C)|\le
 \left(\frac{j\|\mathcal J_j'\|}{2d}
                       +\sum_{r<j}|A'(r)/A(r)|\right)F_j(z_0).
 \tag{22}
\]
There is no division by a row value at \(C\).
Combining (14), (19), and (22), on the angular endpoint
caps of any fixed-height lens,
\[
                 |\widehat G_j(-2\cos t)|
                           \le C_d N^B F_j(2-3d).
 \tag{23}
\]
This includes \(j=0\). The all-row half-plane bound in
the radial-contour source gives
\[
 \prod_iF_{j_i}(2-3d)
       \le N^B e^{Nm\Psi_{1/2}(2-3d)},\qquad
                   \Psi_{1/2}(2-3d)\longrightarrow0
                                      \quad(d\downarrow0).
 \tag{24}
\]

Use exactly the radial graph and its positive minimum
depth \(v\) from the pinned crossed-value theorem.
On its slit-compact portions, (17) loses only a polynomial,
so the strict gaps for the reflected half and the outer
horizontal intervals remain. At the endpoint caps,
(23)--(24) replace the corresponding value estimate.
The complete kernel is kept there:
\[
 |W_N(\pm\pi-iy)|
       =\frac{e^{-Ny}}{(1+e^{-Ny})^2}\le e^{-Ny},
                         \qquad 0\le y\le v.
 \tag{25}
\]
The Gaussian costs at most \(e^{Np y/2}\).
Since \(M_p\) has a uniform positive lower bound,
first choose \(d\), then \(v\), small enough to pay
the entire caps with a fixed strict gap, just as in
the value proof. These choices precede \(N\).

Near the selected saddle (17) costs only a polynomial.
On every graph portion at depth at least \(v\),
\[
                 W_N(t)=e^{-iNt}(1+O(e^{-Nv})).
 \tag{26}
\]
All nonleading aliases are included in this estimate;
at the endpoints they remain in (25).
Thus the complete mixed-normal contribution outside
any fixed small saddle neighborhood is
\[
                    O(N^B e^{N(M_p-\delta)})
 \tag{27}
\]
for a uniform \(\delta>0\).
On the local piece the actual phase from (7) differs
from the limiting phase by \(O(\log N/N)\), and has
a descending Gaussian neighborhood. Equations (17),
(26) give the upper bound in (8).
The actual nonzero value asymptotic in the radial source
also gives
\[
                   |Z_{p,N}|\ge N^{-B_0}e^{NM_p},
 \tag{28}
\]
which proves the relative upper bound in (8).

## 4. The actual leading normal multiplier

For selected bulk indices, apply the complete slit-normal
connection on a buffered compact spectral neighborhood of
the saddle family. Its image lies in \(\Re C<2\), and
the source has one actually anchored scalar mode \(A_N\)
with
\[
 \begin{split}
 A_N(j/N,C)&=F_j(C)(1+O(e^{-\kappa N})),\\
 \partial_xA_N(j/N,C)-C_N'(j/N)\widehat G_j(C)
                                      &=F_j(C)O(e^{-\kappa N}),\\
 \log A_N(x,C)&=N\Psi_x(C)+O(\log N).
 \end{split}
 \tag{29}
\]
Larger fixed domains precede Cauchy differentiation.
It follows that
\[
 \frac{\widehat G_j(C)}{N F_j(C)}
        =g(j/N,C)+O(\log N/N)
 \tag{30}
\]
with all fixed derivatives in \(C\).
The half-step difference in
\(C_N'(x)=-4\pi\sin(2\pi x+\theta)\) costs \(O(N^{-1})\);
no original spectral normal is replaced by a degree
derivative without this factor.

At the favorable saddle, \(\cos(t/2)\) has positive
real part, and
\(\tfrac12\sqrt{2-C(t)}=\cos(t/2)\) on the original
branch. For a real selected bulk degree \(x\),
\(\cos(t/2)\cot(\pi x)\) lies in the right half-plane.
The principal inverse hyperbolic sine also has positive
real part there. Hence \(\Re g(x,C(t))<0\).
Compactness makes every selected factor a uniform unit.

On the local saddle neighborhood put
\[
 a_{I,N}(t)=N^{-|I|}
       \prod_{i\in I}
            \frac{\widehat G_{j_i}(-2\cos t)}
                 {F_{j_i}(-2\cos t)}.
 \tag{31}
\]
It is holomorphic, with uniformly bounded fixed
derivatives. The actual finite-phase Gaussian proof
in the radial source applies with literal amplitude
\(\sin t\,a_{I,N}(t)\), instead of \(\sin t\).
The latter is uniformly nonzero at \(t_{p,N}\).
A local analytic Morse coordinate, or its Taylor
expansion through the first odd term, gives
\[
 \frac{\text{local inserted integral}}
      {\text{local value integral}}
             =a_{I,N}(t_{p,N})+O(N^{-1}).
 \tag{32}
\]
All constants are uniform because (30) supplies
bounded derivatives and the actual Hessian has a
fixed nonzero lower bound.
The normal complement (27), the value complement,
and all alias errors are exponentially smaller than
the nonzero value term (28).
Equations (30)--(32) prove (10), including its
original scalar and square-root orientation inherited
from the common contour.

## 5. A common scalar with exact saddle-arc jets

Fix a reference tuple \(\mathbf x^0\) in (11).
Choose its radial lens from the value theorem and a
short closed subarc \(\gamma_0\) containing its saddle
in its interior. Its spectral image and a fixed
neighborhood lie in \(\Re C<2\).
Keep the entire remaining lens as a complementary
chain with its original orientations and endpoints.

The complement has a strict gap relative to
\(M_p(\mathbf x^0)\), by the complete estimates above.
The profiles, saddle, and action depend continuously
on the real tuple. Therefore, after shrinking a real
product neighborhood of \(\mathbf x^0\), the same
reference chain satisfies, for some \(\delta_0>0\),
\[
 \left|\int_{\Gamma_0\setminus\gamma_0}
       \sin t\,\widehat f_I(t)e^{ipNt^2/(4\pi)}
                          W_N(t)\,dt\right|
           \le C N^B e^{N(M_p(\mathbf j/N)-\delta_0)}
 \tag{33}
\]
for all its physical tuples and all \(I\).
On slit-compact portions this follows from uniform
continuity and (17); the endpoint proof (20)--(25)
is already uniform on the larger support compact.
The reference contour need not remain the radial
minimum graph of a nearby tuple. Its strict
complement inequalities persist on the fixed chain.

Use the exact scalar correction from Section 6 of the
pinned slit-normal connection. On a sufficiently thin
fixed complex bulk degree neighborhood it gives
\(\mathfrak F_N(x,C)\), holomorphic on a neighborhood
of the spectral image of \(\gamma_0\), with
\[
 \mathfrak F_N(j/N,C)=F_j(C),\qquad
 \partial_x\mathfrak F_N(j/N,C)
                         =C_N'(j/N)\widehat G_j(C)
 \tag{34}
\]
as exact identities in \(C\).
Its normalized own-profile size is polynomial on
the present half-plane compact. The rate \(\kappa\)
in (29) limits the strip width needed for that
bound, but contributes no error to (34).

Define the holomorphic scalar
\[
 \boxed{\quad
 \mathcal W_{p,N}(\mathbf x)=
 -\frac{N^2q^{pD^2/4}}{\pi i}
 \int_{\gamma_0}\sin t\,
       e^{ipNt^2/(4\pi)}W_N(t)
             \prod_i\mathfrak F_N(x_i,-2\cos t)\,dt .
 \quad}
 \tag{35}
\]
The Gaussian and the entire grid kernel are retained.
The contour is fixed with respect to \(\mathbf x\);
hence the expression is jointly holomorphic.
At each physical tuple, every mixed first external
spectral derivative of its integrand is exactly the
corresponding product in (15), by (34).
Equation (16) therefore identifies the difference
between that packet jet and the original scalar (4)
with precisely the complementary-chain integral
in (33), including the original prefactor.
Divide by (28) to obtain (12), after adjusting a
polynomial power and choosing \(\gamma<\delta_0\).
A finite cover proves Theorem 3.

This is an exact compatibility statement on the
retained arc, and an exponential physical-jet comparison
after its complement is paid. It does not assert an
off-grid approximation to the canonical multivariate
polynomial
\(\phi_N(R^p\prod_iK_N(w_i,C))\) throughout the
complex neighborhood. Nor does it control an additional
closing or its exponential loss.

## 6. Scope and complete direct sources

Theorems 1--2 remove the external-first-normal exclusion
from the crossed physical-row theorem in precisely the
stated upper and bulk-leading senses. Theorem 3 supplies
one source-compatible local scalar for all those bulk
mixed jets. Unmatched external rows, nonbulk packet
construction, further turns, and further graph
observations require their own estimates. No geometric
volume identification is made.

The complete direct sources and their used implications
were read at the following pins:

* [Crossed physical products on the radial contour](research_crossed_physical_products_radial_contour.md),
  SHA256 db63d7bf100a6d35647b6c9b4832d16c6f5520a7a9c38c0fd322f87659c9d50e:
  actual saddle, full lens, uniform endpoint and alias
  gaps, and finite-row nonzero Gaussian coefficient.
* [Coherent uncharged full-normal contour](research_physical_products_full_normal_coherent_contour.md),
  SHA256 2f150a6d5a901521637f67c6db8fac96c6c6a14a0b23546e8383d1565189d574:
  exact Ward--Jacobi normal substitution, polynomial
  cofactor and endpoint bounds, and full physical-jet scope.
* [Original full-grid lens](research_full_grid_lens_source_continuation.md),
  SHA256 d141e6e8c23572bb13484807a2359395a0371d6a3d699198826a105b6dad5649:
  residue normalization, reflected orientation, complete
  Fourier denominator, and fixed-level endpoint limit.
* [Actual slit normal connection](research_physical_row_slit_normal_connection.md),
  SHA256 a5084adb4ff25cb08020e5f9485bd1aaea5b49468c6ab0af311ebc1c0c504d99:
  actual scalar normal anchor, half-plane logarithmic
  control, and exact scalar full-jet correction.

Only written mathematics, complete source reads and metadata
hashes were used. No mathematical programs, tests, numerical
evaluations, or builds were run. Frozen notes and public
manuscripts are unchanged.
