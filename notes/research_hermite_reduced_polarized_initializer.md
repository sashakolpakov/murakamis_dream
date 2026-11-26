# Hermite reduction before polarizing the original source

Private written proof, 22 November 2026.

The ordinary numerator of the full-midpoint construction can be reduced
in every selected spectral variable before its horizontal charge factor
is polarized. This gives a new off-endpoint family on the full
\(N\)-dimensional Frobenius algebra. It preserves the original cosine
source, every unit-charge readout, and a genuine all-order initializer.
The proof estimates the high Fourier coefficients of the actual
unreduced numerator, then uses an exact first-normal Chebyshev alias.

The resulting quotient has a uniformly equivalent positive
minimum-lift metric in Chebyshev coefficient coordinates. This metric
does not replace the original bilinear closing. No sharp geometric
upper bound or new volume-conjecture case is proved.

## 1. The retained source and its high Fourier coefficients

Use a fixed finite same-index graph, a nonempty selected set \(I\)
with no isolated selected vertex, and complete outside angles.
Keep all retained original edges \(E\), including complete-only factors.
Put \(m=|I|\), \(e=|E|\), and let \(d_v\) count the selected incidences,
twice for a loop. At \(N\ge2\), put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 F_N(\mathbf t)=\prod_{\{v,w\}\in E}K_N(t_v,t_w),\qquad
 M_0=eM_\infty,\qquad L_v=d_vD .
 \tag{1}
\]
Outside angles in (1) equal zero. The original crossing powers and
their carriers remain in the trace rows; they are not included in
this periodic polynomial.

The full ordinary numerator is separately even, with Fourier expansion
\[
 F_N(\mathbf t)=\sum_{|k_v|\le L_v}
                       c_{N,\mathbf k}e^{i\mathbf k\cdot\mathbf t}.
 \tag{2}
\]
There are constants \(C,A,c>0\), depending on this fixed graph but
not on the level or its parity, such that
\[
 |c_{N,\mathbf k}|\le CN^A e^{N(M_0-c)}
       \quad\hbox{if some selected }|k_v|\ge N .
 \tag{3}
\]

Here is a proof using the actual full kernel. The full-midpoint
proof gives the real profile and its weighted-polydisk extension:
\[
 |F_N(\mathbf s+i\mathbf y)|
 \le CN^A\exp N\left[
 M_0-\gamma\sum_vd_v(1-\cos s_v)
                  +(1+\gamma)\sum_vd_v|y_v|\right],
 \qquad\gamma=1/200 .
 \tag{4}
\]
Choose \(0<a<1\). On the central real cube \(|s_v|\le a\), the
original local full-kernel expansion is uniform on a fixed small
complex neighborhood. Its phase
\(W(\mathbf t)=\sum_E\psi(t_v,t_w)\) is real on the real cube.
Its first vertical real derivative therefore vanishes there.
Bounded second derivatives, and the actual polynomial prefactors,
give, uniformly in the selected coordinate \(v\),
\[
 |F_N(\mathbf s-ih\,\mathbf e_v)|
       \le CN^A e^{N(M_0+C_\Gamma h^2)}
                  \qquad (|s_u|\le a).
 \tag{5}
\]
The same bound holds for the opposite shift. The real critical
phase is at most \(M_0\), either by its real concavity or by the
real profile and the nonzero local expansion.

Outside that cube at least one selected \(|s_u|\ge a\). Formula (4)
instead gives, for either one-coordinate shift,
\[
 |F_N(\mathbf s\pm ih\,\mathbf e_v)|
 \le CN^A e^{N[M_0-c_a+(1+\gamma)d_vh]},\qquad
                       c_a=\gamma(1-\cos a)>0 .
 \tag{6}
\]
Choose a fixed \(h>0\) within the local expansion neighborhood so
small that
\[
 C_\Gamma h^2\le h/4,\qquad
       (1+\gamma)\max_vd_v\,h\le c_a/2 .
 \tag{7}
\]
If \(|k_v|\ge N\), shift the entire \(v\)-period in the Fourier
coefficient integral by \(-i\,\operatorname{sgn}(k_v)h\).
The integrand is entire and \(2\pi\)-periodic, including its
integer Fourier character, so its two vertical sides cancel
exactly. The character contributes \(e^{-|k_v|h}\).
The central bound (5) then has rate at most \(M_0-3h/4\);
the complementary bound (6) has rate at most \(M_0-c_a/2-h\).
This proves (3), for example with \(c=h/2\).
No Gaussian crossing factor was shifted in this argument.

## 2. An exact Hermite alias at every level

Let
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
                     B_k(z)=T_k(-z/2).
 \tag{8}
\]
Let \(\mathcal R_N\) be ordinary Euclidean remainder modulo \(P_N\).
For \(k=aN+r\), \(a\ge0\), \(0\le r<N\), its exact expression is
\[
 \begin{split}
 \mathcal R_N B_{aN}&=\eta^a,\\
 \mathcal R_N B_{aN+r}
   &=\eta^a\{(a+1)B_r-a\eta B_{N-r}\},
                                \qquad 0<r<N .
 \end{split}
 \tag{9}
\]
This identity retains first normals, not just values.

To verify it, use the physical angular lifts
\(\tau_j=\pi(D-2j)/N\), for which
\(\cos(N\tau_j)=\eta\) and \(\sin(N\tau_j)=0\).
At a double spectral root \(z=-2\cos\tau_j\),
\(B_k(z)=\cos(k\tau_j)\). For \(0<r<N\), both sides of (9)
have value \(\eta^a\cos(r\tau_j)\), and their angular derivatives
both equal
\[
                  -\eta^a(aN+r)\sin(r\tau_j).
 \tag{10}
\]
Since \(\sin\tau_j\ne0\), these are also equality of the first
spectral derivatives. For \(r=0\), the value is \(\eta^a\) and
the angular derivative is zero. The odd simple node at
\(\tau=0\) requires only the value, which also agrees.
The right sides have degree below \(N\), so full Hermite uniqueness
proves the Euclidean remainder formula.
This includes \(N=2\), both parities, and composite levels.
If the two indices on the second line coincide, their coefficients
are added; that addition preserves the normal channel.

On inputs of degree at most \(d(N-1)\), the sum of the absolute
Chebyshev coefficients in any alias column is at most \(2d+1\).
No estimate on a monomial-coordinate remainder operator is asserted.

## 3. The reduction error is small at the actual seed scale

Apply Euclidean remainder independently in each selected ordinary
spectral variable \(z_v=-2\cos t_v\), and set
\[
       \mathcal R_I=\bigotimes_{v\in I}\mathcal R_N^{(v)},\qquad
       Q_N=\mathcal R_I F_N,\qquad E_N=F_N-Q_N .
 \tag{11}
\]
The operations commute. They may be performed coefficientwise in
ordinary outside variables; the analytic estimates here specialize
those variables to their complete values.

Separate evenness rewrites (2) in the tensor basis
\(\prod_v\cos(k_vt_v)=\prod_vB_{k_v}(z_v)\), \(k_v\ge0\).
Its coefficients differ from the corresponding Fourier coefficients
by a factor at most \(2^m\). Every term with all \(k_v<N\) is
unchanged by (11). Every remaining coefficient has bound (3), and
its reduced tensor alias has coefficient sum at most
\(\prod_v(2d_v+1)\), by (9). Since the number of terms is
\(O_\Gamma(N^m)\), on the entire real angular torus
\[
                   |E_N(\mathbf s)|
                   \le CN^A e^{N(M_0-c)} .
 \tag{12}
\]
Its angular degree in variable \(v\) is at most \(L_v\), because
\(d_v\ge1\). Ordinary trigonometric Bernstein continuation, or the
unweighted polydisk argument used for (4), therefore gives
\[
 |E_N(\mathbf s+i\mathbf y)|
       \le CN^A\exp\left[N(M_0-c)+\sum_vL_v|y_v|\right].
 \tag{13}
\]
The constants may be enlarged and \(c\) decreased without depending
on the level. This estimate concerns this actual numerator; it is
not an assumed uniformly bounded remainder map on arbitrary input data.

## 4. A new reduced source with the same original readouts

Use the literal full-midpoint operators
\(\mathcal T_{\sigma,n,\chi}^{h}=\mathcal H_\sigma^h+
\mathcal V_{\cos}^h\), with cuts \(\pm\pi\), from the pinned
full-midpoint proof. Its crossing carrier is
\[
                         C_{N,n}=e^{\pi inD^2/(4N)}.
 \tag{14}
\]
For fixed positive heights define a new carrier-removed family
\[
 \mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}
       (\mathbf n,\boldsymbol\chi)
     =\left[\bigotimes_{v\in I}
             \mathcal T_{\sigma_v,n_v,\chi_v}^{h_v}\right]Q_N .
 \tag{15}
\]
The canonical representative \(Q_N\) is chosen before polarization.
Thus (15) is a well-defined functional on the full tensor product
of the algebras \(\mathcal A_N\). It is generally a different
off-endpoint family from applying those operators to \(F_N\).

The exact original cosine source, unit endpoint, and fixed-height
heat identities are
\[
 \begin{split}
 2^{-m}\sum_{\boldsymbol\sigma}
       \mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}
       &=\widetilde Z_N(\mathbf n,\boldsymbol\chi),\\
 \mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}
                        (\mathbf n,\mathbf1)
       &=\widetilde Z_N(\mathbf n,\mathbf1),\\
 \partial_{n_v}
       \mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}
       &=-\frac{i}{4\pi N}\partial_{\chi_v}^2
       \mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}.
 \end{split}
 \tag{16}
\]
Here \(\widetilde Z_N\) is the original source of \(F_N\), with
the literal product of carriers removed. They are restored by (14).

Indeed \(F_N-Q_N\) belongs to the sum of the ideals generated by
the \(P_N(z_v)\). At every double physical root both \(P_N\) and
its first spectral derivative vanish. At the odd simple root its
value vanishes. Equivalently both
\(P_N(-2\cos\tau_j)\) and its first angular derivative vanish
at every physical angular point, including \(\tau=0\).
Multiplication by the crossing Gaussian, coupon and spectator
preserves those vanishing jets. Hence the full original tensor
trace kills this ideal, including all required mixed first normals.
Sign averaging and unit evaluation of the exact midpoint operators
give the first two identities. The last follows by differentiation
of the fixed contour operators; \(Q_N\) depends on neither parameter.
Their signed Gaussian heat readouts are convergent and have the
same original endpoints. No first-normal direction is removed:
\(\mathcal A_N\) still has its full dimension \(N\).

Fix real powers \(\mathbf b\), and choose the sufficiently small
positive seed and real heights of the full-midpoint initializer.
These heights have \(h_v=O_{\Gamma,\mathbf b}(\delta)\).
Applying the exact operators to (13), with the horizontal and
vertical weights from that proof, gives
\[
 |\mathcal G_{N,\boldsymbol\sigma}^{\mathbf h}
       -\mathcal G_{N,\boldsymbol\sigma}^{\mathrm{red},\mathbf h}|
 \le CN^A\exp N\left[M_0-c+
        \sum_v(d_v+|b_v|/2)h_v+\pi\sum_v|\Im\chi_v|\right].
 \tag{17}
\]
The source on the left before reduction is the actual family of
the pinned full-midpoint construction.
The seed action is \(S(\delta\mathbf1)=M_0+O(\delta^2)\).
Choose that seed still smaller if necessary, then shrink a fixed
complex neighborhood of it. Formula (17) is consequently
\[
             O\!\left(N^A e^{N(\Re S(\boldsymbol\chi)-c/2)}\right).
 \tag{18}
\]
It has the same estimate under every fixed charge derivative on smaller
neighborhoods, by Cauchy's formula. Thus the reduced family has the
same actual nonzero all-order seed expansion, phase, and full
normalizations as the unreduced family at that same seed, through
both level parities. This is an estimated seed equivalence, not
an inference from equal endpoint values.

The fixed-power moving-height construction in the full-midpoint
proof also admits this reduction. Near its sufficiently small seed
the complex heights have modulus \(O(\delta)\) and positive real
parts. Bound (13), together with its uniform complex-height
\(\cosh\)-denominator estimate and retained path measures, proves
the moving-height version of (18). Its endpoint and cosine identities
remain exact. The moving composed family is holomorphic on its
chosen parameter domain; no fixed-height heat equation is assigned
after that substitution. Cauchy's formula retains the estimate under
fixed derivatives in that parameter on smaller neighborhoods.

## 5. The coefficient quotient and its positive Gram

For one selected degree \(d\), let \(R_{d,N}\) be the matrix of
\(\mathcal R_N\) from input Chebyshev indices \(0,\ldots,dD\) to
output indices \(0,\ldots,D\), with Euclidean coefficient metrics.
Formula (9) gives
\[
 \|R_{d,N}\|_1\le2d+1,\qquad
 \|R_{d,N}\|_\infty\le2(d+1)^2,\qquad
 \|R_{d,N}\|^2\le C_d^2:=2(2d+1)(d+1)^2 .
 \tag{19}
\]
For the row bound, in each block \(aN+r\) an output row receives
at most two aliases, each of modulus at most \(d+1\), and there
are at most \(d+1\) blocks. Coincident aliases obey the same bound.
The operator bound is the elementary row-column Schur estimate.
Its first \(N\) columns are the identity, so
\[
                 I\preceq R_{d,N}R_{d,N}^*
                                      \preceq C_d^2I .
 \tag{20}
\]
These constants are independent of parity, compositeness and level.

For \(R=\bigotimes_{v\in I}R_{d_v,N}\), put
\(C_\Gamma=\prod_vC_{d_v}\) and \(G=(RR^*)^{-1}\).
The exact minimum-lift identity is
\[
 \min_{Rx=q}\|x\|^2=q^*Gq,\qquad
 C_\Gamma^{-2}I\preceq G\preceq I,\qquad
              x_{\min}=R^*Gq .
 \tag{21}
\]
It follows by orthogonal decomposition with respect to \(\ker R\).
In particular \(R^*GR\) is the orthogonal projection onto
\((\ker R)^\perp\). The induced quotient seminorm vanishes
precisely on the relation directions. Replacing \(G\) by \(I\)
is a graph-constant norm comparison, not an exact metric identity.
This positive Gram concerns Chebyshev coefficient geometry; the
original bilinear Frobenius pairing and marked closing are retained.
No transfer of these uniform bounds to monomial coordinates or the
physical Hilbert--Schmidt metric is inferred.

Let \(q_N\) be the \(N^m\)-dimensional coefficient vector of \(Q_N\)
in \(\bigotimes_v\{B_0,\ldots,B_D\}\). The reduced closing row is
still a single tensor product, now with local entries
\[
 \ell_{v,r}^{\mathrm{red}}
        =\mathcal T_{+,b_v,\chi_v}^{h_v}[\cos(rt_v)],
 \qquad0\le r<N,\qquad
 \mathcal G_{N,\mathbf+}^{\mathrm{red},\mathbf h}
       =\left(\bigotimes_v\ell_v^{\mathrm{red}}\right)q_N .
 \tag{22}
\]
Thus all polynomial relation directions have been removed for this
new family, without discarding the algebra's nilpotent channels.
The local rows are the full-midpoint functionals on canonical
representatives. They are not identified with the canonical
power-independent spectral charge coupons.

The raw polarized row need not kill \(\ker R\) off the endpoint;
the construction deliberately replaces that off-endpoint family.
No equality of its old quadratic minimum with a new one is asserted.
The new family still needs its own sharp complex geometric upper
estimate. No geometric coverage, volume lower bound, or
finite-exception theorem follows from (19)--(22).

## 6. Literal finite-algebra coupons and the relation directions

The reduced row also has an explicit realization with the original
bilinear Frobenius trace. To fix its normalization directly, take
zero crossing power and unit charge in the exact angular sampling:
\[
 \phi_N(p)=\eta\sum_{j=0}^{D}
     \left.\partial_t\{\sin t\,p(-2\cos t)\}\right|_{t=\tau_j}.
\]
For \(\deg p\le D\), the sine polynomial inside braces has
frequencies at most \(N\). Its \(N\)-th sine coefficient is
\(\eta[z^D]p\); only the top monomial can contribute it.
Every cosine frequency \(1,\ldots,N-1\) sums to zero on the grid,
while \(\sum_j\cos(N\tau_j)=N\eta\).
Differentiation supplies the remaining factor \(N\).
Using the full-jet ideal vanishing proved above then gives, on
the ordinary degree-less-than-\(N\) representative,
\[
 \phi_N(p)=\eta N^2[z^D]\operatorname{rem}_{P_N}p .
 \tag{23}
\]
Let \(\mathsf H_N=(\phi_N(z^{i+j}))_{0\le i,j<N}\).
Entries with \(i+j<D\) vanish and its anti-diagonal entries equal
\(\eta N^2\). Thus
\[
 \det\mathsf H_N=(-1)^{N(N-1)/2}(\eta N^2)^N\ne0 .
 \tag{24}
\]
This is bilinear nondegeneracy, without conjugation.
Here \(R_n\) denotes the original crossing class with the full
Hermite jets of \(C_{N,n}e^{inNt^2/(4\pi)}\) at the original physical
angular lifts. At the odd simple node only its value is prescribed.
For integral \(n\) it is the original signed crossing power.
For the local reduced functional
\(L_{\sigma,n,\chi}^h(p)=
\mathcal T_{\sigma,n,\chi}^h[\operatorname{can}_{P_N}p]\),
form its known column
\(\mathbf r=(L_{\sigma,n,\chi}^h(z^j))_{j=0}^{D}\).
The coefficient column
\(\mathbf c=\mathsf H_N^{-1}\mathbf r\) defines the unique class
\(\mathfrak b_{\sigma,n,\chi}^h=\sum_i c_i z^i\) satisfying
\[
 L_{\sigma,n,\chi}^h(p)=\phi_N(\mathfrak b_{\sigma,n,\chi}^h p),
 \qquad
 \mathfrak b_{\sigma,n,1}^h=C_{N,n}^{-1}R_n .
 \tag{25}
\]
The endpoint identity follows by testing all \(p\), using the exact
original unit-charge trace and (24). Every entry of \(\mathbf r\)
is a local prescribed contour integral; no unknown closed graph
scalar is divided out or inserted. Formula (15) is consequently
the original tensor trace with these local coupons and the class
of \(F_N\). They generally depend on the crossing power and height,
so they are not the canonical power-independent charge coupons.
No positive Hermitian interpretation of \(\mathsf H_N\) is claimed.

This reduction kills only the polynomial ideal relations
\(\ker\mathcal R_I\), rather than all vectors invisible to a chosen
closing row. The full Hermite algebra, including its Jordan
directions, remains. Since it is the actual algebra quotient,
\[
 \mathcal R_N(pq)
       =\mathcal R_N\!\bigl((\mathcal R_Np)(\mathcal R_Nq)\bigr).
 \tag{26}
\]
Reduction may therefore follow each algebra multiplication without
allowing an ideal relation to return. This identity does not supply
a new adapter for an arbitrary boundary turn or tree operation;
the original well-defined source operations must still be retained.

## Complete direct sources

- [Full-midpoint initializer and exact operators](research_full_midpoint_polarized_initializer.md),
  603 lines, SHA256
  65a91ee6538b05355bab5056d32b2fe563c47eeff1e1924b1be259ef5cd628ad:
  the ordinary real profile, weighted-polydisk bound, actual local
  full-kernel expansion, complete source, seed and moving-height
  denominator estimates.
- [Original full-Hermite polarized trace conventions](research_pattern_adapted_polarized_heat_initializer.md),
  370 lines, SHA256
  a27c25dae7f3be3f1ef52fb369ecca822b0896a4b034450131e05b12423c2694:
  exact original operators, carriers, physical normals and cosine
  source before and after signed heat steps.

Both complete proof sources and the entire final proof were read at
these matching versions before author freeze.
Only written mathematics, text reads and hashes are used.
No programs, numerical experiments, tests, builds or git commands
are run. Root's pre-freeze mathematical review is complete.
Independent matching entire-final peer review is separate.
