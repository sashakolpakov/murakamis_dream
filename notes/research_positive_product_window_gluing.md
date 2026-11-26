# A common positive-product baseline and exact two-endpoint window repair

Private written proof, 16 November 2026.

The regular row constructions can be assembled on a fixed positive
product chart. A finite boundary Cauchy integral gives one holomorphic
baseline with the original action bound. The endpoint-role comparison
controls this projection, including its actual normal data on the
chosen real windows. Two one-sided row repairs, with their common
mixed-jet correction subtracted once, then preserve both row families
exactly.

The windows remain fixed bulk windows. The conclusion is an angular
holomorphic representative with a designated-quadrant bound, not a
whole-grid or full-lens replacement. All original exterior and interface
currents retain their original spectator.

## 1. Fixed product domains and designated paths

Fix a positive pair \((t_*,u_*)\) in the original strips
\(\mathcal S=\{|\Re t|<\pi\}\). The pinned product-domain theorem
provides symmetric simply connected domains \(V_t,V_u\subset\mathcal S\),
containing the full real intervals and the target, on whose product
\[
 a=\tan(t/2),\quad b=\tan(u/2),\quad
 q_*^2=1+a^2+b^2\notin(-\infty,0],\quad \Re q_*>0.
 \tag{1}
\]
In tangent coordinates each domain is the union of a thin horizontal
strip and a thin neighborhood of the segment joining the target
tangent to its negative. Both pieces contain zero.

Choose bounded smooth Jordan domains
\[
 \Omega_v^0\Subset\Omega_v^1\Subset\Omega_v^2
                    \Subset\Omega_v^3\Subset V_v,\qquad v=t,u,
 \tag{2}
\]
containing zero, the target coordinate and fixed small positive real
seed intervals. They may be chosen symmetric, with star-shaped tangent
images. To see this, take a compact radial set consisting of the
required segments and small real intervals in the open star-shaped
tangent domain. A smooth positive radial boundary lying between that
compact set and the domain boundary gives a bounded star-shaped
Jordan neighborhood. Repeat with buffers and apply \(2\arctan\).
All choices precede \(N\).

The original phase \(\psi(t,u)\) is single valued on this product.
For precision its derivatives are
\[
 r_t=\tfrac12\Log\frac{q_*+a}{q_*-a},\quad
 r_u=\tfrac12\Log\frac{q_*+b}{q_*-b},\qquad
 \psi_t=-r_t/\pi,\quad\psi_u=-r_u/\pi .
 \tag{3}
\]
The logarithms have their original value at completeness. Their
arguments are units since \((q_*+a)(q_*-a)=1+b^2\), and similarly
for \(b\). The product is simply connected. Moreover
\(\partial_u r_t=\partial_t r_u=-ab/(2q_*)\), so (3), with the
original complete constant, defines the continued original phase.
It agrees with every row phase at its real seed.

**Lemma 1.** A nonzero point of either \(\Omega_v^2\) can be joined
to its positive real seed interval by a compact path avoiding zero
which stays in the sign of its imaginary part, apart from its real
seed. If the target is real, either side may be chosen. Fixed
buffered tubes supply the regular continuation domains, uniformly
for the other endpoint throughout a fixed buffered parameter compact.

**Proof.** Work in the star-shaped tangent domain. Follow its radial
target segment from a sufficiently small nonzero point to the target.
Join that small point to a positive real seed through a small arc
about zero on the same side, followed by the real spine. This arc
lies in a disk contained in the domain. For \(a=A+i\beta\),
\[
 \Im(2\arctan a)
 =\tfrac12\log\frac{A^2+(1+\beta)^2}{A^2+(1-\beta)^2},
 \tag{4}
\]
which has the sign of \(\beta\). Thus the angular path has the
claimed side. A thin tube about a simple version of this path is
simply connected and avoids zero and the angular endpoints.

On this tube the selected degree root is
\[
 \lambda_t=\frac{q_*+a}{q_*-a},\qquad
 1-\lambda_t^{-2}=\frac{4q_*a}{(q_*+a)^2}.
 \tag{5}
\]
Every factor is a unit on the compact buffered product, because
the first angle avoids zero. This proves the required uniform
separation without imposing off-real modulus ordering.
The same proof applies with the endpoints interchanged. \(\square\)

First choose the buffered tube and construct its mode. Then shrink
only the opposite-side collar to the width supplied by its positive
repair exponent. This order is important: no fixed preselected
collar is declared smaller than an exponent not yet constructed.
The path itself stays on the designated side, and its real seed
has a nonempty permitted collar. Compactness leaves an open
neighborhood of each target in the resulting bounded domain.

In particular, if both target angles are nonzero, the two endpoint
roles have a common designated product domain with two real physical
seed intervals. Use the same domains (1), choose the two paths
of Lemma 1 independently, and include each path in the other
construction's parameter domain. Their product is connected to
the joint seed and has both normalized bounds. This verifies the
hypotheses of the endpoint-role overlap theorem on compact subsets
of that product. Merely having two separate continuation paths
would not have supplied this common domain.

## 2. One finite boundary Cauchy projection

Use centered degree coordinates
\[
 N\ge2,\quad\eta=(-1)^{N-1},\quad
 X=(\pi-t)/(2\pi),\quad Y=(\pi-u)/(2\pi),\quad
 X_j=(j+\tfrac12)/N,\quad Y_k=(k+\tfrac12)/N,\quad
 C(X)=2\cos(2\pi X),\quad c_j=C(X_j),\quad
 P_N(z)=2T_N(z/2)+2.
 \tag{6}
\]
Fix bulk intervals \(I_X,I_Y\Subset(0,1/2)\), corresponding
to the positive real seed intervals in (2). Every local construction
below matches those same windows. All sufficiently large-level
rows in them are double spectral nodes.

Cover the compact curve \(\Gamma_t=\partial\Omega_t^1\) by
finitely many first-degree continuation charts. Each chart uses
Lemma 1, the same \(I_X\), and a second-parameter domain containing
\(\overline{\Omega_u^3}\) with a buffer inside \(V_u\).
The first-degree paths and their buffers lie in \(\Omega_t^2\).
Let \(A_{i,N}(t,u)\)
be its repaired representative and put
\[
                          a_{i,N}=e^{-N\psi}A_{i,N}.
 \tag{7}
\]
On a neighborhood of its boundary arc times
\(\overline{\Omega_u^3}\), this function is holomorphic and
has norm \(e^{o(N)}\). Its sign is chosen for that boundary arc.
Different arcs may require different signs; all arc neighborhoods
use their actual permitted collars.

Choose a fixed smooth partition of unity \(\chi_i\) on
\(\Gamma_t\), subordinate to these arcs. Define
\[
 H_N(t,u)=\frac1{2\pi i}\int_{\Gamma_t}
       \frac{\sum_i\chi_i(\zeta)a_{i,N}(\zeta,u)}
                         {\zeta-t}\,d\zeta .
 \tag{8}
\]
The integral is counterclockwise. It is holomorphic in
\(\Omega_t^1\times\Omega_u^3\), and
\[
 \sup_{\Omega_t^0\times K_u}|H_N|\le e^{o(N)}
                           \quad(K_u\Subset\Omega_u^3).
 \tag{9}
\]
Indeed the contour length and its distance from \(\Omega_t^0\)
are fixed, its cover is finite, and its integrand is holomorphic
in the exterior parameter. This gives a bounded projection
explicitly; no quantitative sheaf or \(\bar\partial\) theorem
is being assumed.

Now take a second-degree chart \(B_{j,N}(t,u)\) whose degree
path and buffers lie in \(\Omega_u^2\), and whose first-endpoint
parameter domain contains \(\overline{\Omega_t^3}\) with a
buffer inside \(V_t\). Write \(b_{j,N}=e^{-N\psi}B_{j,N}\).
On each boundary arc, the common-domain construction of Lemma 1
and the endpoint-role theorem give
\[
                         a_{i,N}-b_{j,N}=O(e^{-c_{ij}N})
 \tag{10}
\]
uniformly on fixed compact parts of the chart. There are finitely
many \(i\). Cauchy's formula for \(b_{j,N}\) in its full
first-parameter domain and (8) therefore give
\[
 H_N-b_{j,N}=O(e^{-c_jN})
 \quad\text{on }\Omega_t^0\times K_j ,
 \tag{11}
\]
where \(K_j\) is any fixed compact subset of the second chart's
designated degree domain. All fixed derivatives satisfy the same
conclusion on smaller buffers.

The domain choices in (2) are deliberately asymmetric in each use:
degree paths stay inside the level-two domains, while the opposite
parameter domains contain level three. Thus every cross-role
comparison in (10) has the entire two-path product and joint seed.
No later enlargement or connectedness of an intersection of two
same-role paths is required.

The baseline also compares with any first-degree chart
\(A_N^0\) on a compact part of \(\Omega_t^0\), with its path
in \(\Omega_t^2\) and parameter domain containing
\(\overline{\Omega_u^3}\). First compare both with a fixed
second-degree chart about the real interval \(I_Y\).
Equation (11) and the endpoint-role theorem give an exponentially
small normalized difference on that real seed neighborhood, uniformly
in the compact first-degree set. Both \(H_N\) and
\(e^{-N\psi}A_N^0\) have \(e^{o(N)}\) bounds as holomorphic
functions of \(u\). Finite analytic propagation on the connected
second parameter domain gives
\[
 H_N-e^{-N\psi}A_N^0=O(e^{-cN})
 \tag{12}
\]
on every fixed smaller parameter compact, including \(u=0\).
This comparison is made where the first-degree chart itself is
regular. It does not continue that chart through its degree fold.

In particular choose \(A_N^0\) near the entire real window
\(I_X\), and use a second-degree chart near \(I_Y\) in (11).
The baseline consequently has exponentially small errors in both
actual row families, as holomorphic functions of the other endpoint.
This is stronger than comparing only isolated joint nodal values.
The Cauchy baseline is holomorphic even at \((t,u)=(0,0)\);
no physical data at that fold have been inferred from this fact.

## 3. Exact row identities and the compatible mixed repair

Write \(\mathcal H_N(X,Y)=H_N(t(X),t(Y))\) and
\(\Psi(X,Y)=\psi(t(X),t(Y))\). Use the original
\[
 F_j(w)=K_N(c_j,w),\qquad G_j(w)=\partial_zK_N(c_j,w),
 \tag{13}
\]
and the pinned full-normal representative \(\widehat G_j\).
Define the normalized first-row target functions
\[
 \begin{split}
 T_{j,0}(Y)&=e^{-N\Psi(X_j,Y)}F_j(C(Y)),\\
 T_{j,1}(Y)&=e^{-N\Psi(X_j,Y)}
 \{C'(X_j)\widehat G_j(C(Y))
                      -N\Psi_X(X_j,Y)F_j(C(Y))\}.
 \end{split}
 \tag{14}
\]
Define \(S_{k,0}(X),S_{k,1}(X)\) by interchanging the endpoints.
They are holomorphic on the full parameter neighborhoods in use.
The actual mixed physical-jet identity proves, exactly,
\[
 \partial_Y^bT_{j,a}(Y_k)=\partial_X^aS_{k,b}(X_j),
                  \qquad 0\le a,b\le1.
 \tag{15}
\]
This includes the derivatives of the normalizing exponential:
both sides are the same \((a,b)\) jet of
\(e^{-N\Psi}K_N(C(X),C(Y))\) at the physical pair. It uses
the required first normal of \(\widehat G_j\), not just its
value.

Set
\[
 d_{j,a}(Y)=T_{j,a}(Y)-\partial_X^a\mathcal H_N(X_j,Y),
 \quad
 e_{k,b}(X)=S_{k,b}(X)-\partial_Y^b\mathcal H_N(X,Y_k).
 \tag{16}
\]
Equations (11)--(12), with fixed buffers, give
\[
 d_{j,a}=O(e^{-cN}),\qquad e_{k,b}=O(e^{-cN})
 \tag{17}
\]
uniformly for all selected rows and on the respective full smaller
parameter domains. The same holds for every fixed derivative.
These estimates use the actual row-normal normalization of the
regular source theorem. The original canonical kernel is not
being bounded off-grid to prove (17).

For \(\sigma=\pm1\), define
\[
 L_j^\sigma(X)=e^{\sigma2\pi iN(X-X_j)}
                         \operatorname{sinc}^2(N(X-X_j)),
\]
\[
 V_{j,0}^\sigma(X)=[1-\sigma2\pi iN(X-X_j)]L_j^\sigma(X),
 \qquad V_{j,1}^\sigma(X)=(X-X_j)L_j^\sigma(X).
 \tag{18}
\]
They satisfy
\(\partial_X^aV_{j,b}^\sigma(X_\ell)=\delta_{j\ell}\delta_{ab}\)
for \(0\le a,b\le1\). Use \(W_{k,b}^\tau(Y)\) for the
same functions in the second coordinate. On bounded parts of
\(\sigma\Im X\ge0\), each function and fixed derivative
is polynomially bounded in \(N\). This follows from the
Fourier support of \(L_j^\sigma\) and its coefficient mass one.

The compatibility in (15) gives one joint error array
\[
 c_{jk}^{ab}=\partial_Y^bd_{j,a}(Y_k)
                         =\partial_X^ae_{k,b}(X_j).
 \tag{19}
\]
Define the three finite corrections
\[
 \begin{split}
 E_X^\sigma&=\sum_{j,a}d_{j,a}(Y)V_{j,a}^\sigma(X),\\
 E_Y^\tau&=\sum_{k,b}e_{k,b}(X)W_{k,b}^\tau(Y),\\
 E_{XY}^{\sigma,\tau}
       &=\sum_{j,k,a,b}c_{jk}^{ab}
                       V_{j,a}^\sigma(X)W_{k,b}^\tau(Y),
 \end{split}
 \tag{20}
\]
and the actual angular holomorphic representative
\[
 \boxed{\quad
 \mathcal K_N^{\sigma,\tau}(X,Y)
 =e^{N\Psi(X,Y)}
   [\mathcal H_N+E_X^\sigma+E_Y^\tau-E_{XY}^{\sigma,\tau}].
 \quad}
 \tag{21}
\]
All four choices are holomorphic on the same inner product domain.

**Theorem 2.** The representatives (21) obey both exact row families,
as holomorphic identities in the other variable:
\[
 \begin{split}
 \mathcal K_N^{\sigma,\tau}(X_j,Y)&=F_j(C(Y)),&
 \partial_X\mathcal K_N^{\sigma,\tau}(X_j,Y)
                  &=C'(X_j)\widehat G_j(C(Y)),\\
 \mathcal K_N^{\sigma,\tau}(X,Y_k)&=F_k(C(X)),&
 \partial_Y\mathcal K_N^{\sigma,\tau}(X,Y_k)
                  &=C'(Y_k)\widehat G_k(C(X)).
 \end{split}
 \tag{22}
\]
On compact subsets of their designated quadrants
\(\sigma\Im X\ge0,\ \tau\Im Y\ge0\),
\[
 e^{-N\Psi}\mathcal K_N^{\sigma,\tau}
           =\mathcal H_N+O(e^{-c_1N}),\qquad
 |\mathcal K_N^{\sigma,\tau}|
                         \le \exp\{N\Re\Psi+o(N)\}.
 \tag{23}
\]
The estimate includes fixed sufficiently thin opposite collars.
Every fixed derivative has the corresponding buffered estimate.

**Proof.** Taking an \(X\)-jet at \(X_j\) in (20), equation
(19) gives exactly
\[
 \partial_X^aE_{XY}^{\sigma,\tau}(X_j,Y)
                       =\partial_X^aE_Y^\tau(X_j,Y).
 \tag{24}
\]
Thus the second and mixed corrections cancel in that row, and
\(\mathcal H_N+E_X^\sigma\) has precisely the two targets
(14). Multiplication by \(e^{N\Psi}\) proves the first line
of (22). The symmetric calculation proves its second line.
This is why the mixed correction is subtracted once.

There are \(O(N)\) terms in each single sum and \(O(N^2)\)
in the double sum. Equations (17)--(19) and the polynomial
cardinal bounds prove (23). On the opposite sides the only
additional exponential factor is at most
\[
 \exp\{4\pi N[
          (-\sigma\Im X)_++(-\tau\Im Y)_+]\}.
 \tag{25}
\]
Choose the collar widths after \(c\), with their sum sufficiently
small. The remaining exponential rate stays positive. Buffered
Cauchy estimates give fixed exterior and spatial derivatives.
\(\square\)

## 4. Original source and current scope

For a selected first window and any actual joint spectator \(P\),
the closed window contour of (21) is exactly the finite residue
expression
\[
 \Phi^\sharp_{N,I_X}(w)
 =\eta\sum_{X_j\in I_X}
 \{(4-c_j^2)[\widehat G_j(w)P(c_j)
                    +F_j(w)P_Z(c_j)]-c_jF_j(w)P(c_j)\}.
 \tag{26}
\]
This follows from (22), with every other variable held fixed.
The original window trace uses \(G_j\) instead. Their difference
is \(P_N(w)\) times a holomorphic slit function, and equality
with the original follows after the required subsequent complete
second trace, including all spectators and normal products.
The second-window statement is identical with the roles reversed.

At a joint selected physical pair, (22) retains the value, both
first normals and their mixed normal of the original kernel.
Thus the double selected-window trace is exact. A local parameter
domain need not contain the remaining second grid: a later full
trace is taken on the global finite residue expression (26), or
on a covering retaining all other rows. No arbitrary free-boundary
polynomial has been replaced.

The four representatives have one common baseline. Their normalized
differences are exponentially small where the relevant designated
bounds hold; the original trace kernels and the entire spectator
must still multiply those differences. The usual removable
one-sided real interface and every oriented exterior half-side
remain in each closed-window formula. An exponential local saving
does not by itself pay a larger spectator or parent action.

The Cauchy baseline extends through both angular folds, but (22)
matches only the chosen bulk rows. No new fold value or fold normal
is asserted. Neither the baseline nor the exact repairs are asserted
even in both angular variables, so no spectral descent at an
unmatched fold or parity-based full-lens substitution is inferred.
The original endpoint rows near \(\pm\pi\), all unmatched rows,
and the full geometric cycle and coefficient remain separate.

## Direct sources and coverage

The complete direct texts and their used implications were read at:

* [Regular positive continuation](research_physical_row_regular_positive_continuation.md),
  SHA256 3a7d81d55f60396c2e3058d5ebe967ae625ff47c4b527b4e102e37fa8f28d644:
  actual row modes, independent normal anchor, designated-half
  repair and exact \(\Phi^\sharp\) trace type.
* [Endpoint-role overlap](research_physical_row_endpoint_role_overlap.md),
  SHA256 67478e66259712bc648c23241c3c3e93bc4342c54b2dbcea39be97ee7b83edec:
  full mixed physical compatibility, shared-seed comparison and
  finite analytic propagation.
* [Positive product domains](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  tangent-domain construction, original discriminant branches and
  fixed product neighborhoods.

The earlier two-channel interpolation note already uses a Cauchy
correction followed by a finite sinc repair on a thin one-variable
strip. Here the boundary projection is controlled by the actual
opposite-endpoint source chart, and the two line families are
repaired together by (19)--(24). No general bounded Cousin solver
or global continuation of a raw finite factorial sum is used.

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical evaluation, test or compilation
was run. Adopted notes and public manuscripts were unchanged.
