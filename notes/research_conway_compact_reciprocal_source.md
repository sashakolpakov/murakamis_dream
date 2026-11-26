# A compact unweighted reciprocal integral for the original Conway source

24 November 2026. Research proof.

A known polynomial change of the normalization budgets makes the
positive source integral compact and unweighted after all linearly
entering packets have been integrated out. One packet per binary
product remains. Its polynomial residual vector retains the original
scalar closing, including its phases and all first-normal directions.
For a fixed tree the compact integral approximates the reciprocal
squared normalized source with relative error \(O(N^{-1})\).

The proof also works in any prescribed positive packet metrics after
consistent normalization. It does not evaluate the compact integral
from hyperbolic geometry or prove a new volume lower bound.

## 1. The source and the polynomial normalization

Fix a literal Conway tree with \(s\ge1\) proper vertices,
\(L\ge1\) prescribed leaf occurrences and \(p=L-1\) binary products.
Every packet is the complete \(N\)-dimensional physical algebra
\(\mathcal A_N\), \(N\ge2\), including the independent first normals
at double Casimir roots. Use the original products, genuine turns and
original scalar closing of [P]. The leaf choices may be arbitrary
complex physical packets, including prescribed short fillings.

Initially choose known positive budgets \(b_v\), including the scalar
root budget, so that the normalized leaves, turns, bilinear products
and closing row have their respective norms at most \(1/16\).
The product norm here is the supremum over two separately unit
inputs. No small coefficient-tensor Hilbert--Schmidt norm is assumed.
The physical budgets of [P] give one such choice. Write
\[
 B_N=\prod_v b_v,\qquad
 \widehat b_v=Nb_v,\qquad
 \widehat B_N=N^{s+1}B_N,\qquad
 \sigma_N={1\over16N}.                                      \tag{1}
\]
There are \(s\) proper budgets and one scalar root budget. In the
rest of the proof use these new budgets, and abbreviate
\(\sigma=\sigma_N\). Their normalized maps are \(\Phi_v\); their
normalized original closing row is \(c\), extended by zero off the
top packet. All their respective norms are at most \(\sigma\).
The original framing, mark and external scalars remain in these maps.

Choose orthonormal coordinates on every packet and product real
Lebesgue measure. Put \(D=Ns\), and set
\[
 G_v(x)=\Phi_v((x_j)_{j\text{ child of }v})-x_v,\qquad
 E_N(x)=\|G(x)\|^2+|cx|^2,\qquad
 \mathcal P_N={D!\over\pi^D}\int_{\mathbb C^D}E_N(x)^{-D-1}dx.
                                                               \tag{2}
\]
This is the reciprocal construction with the newly recorded budgets;
its numerical value need not equal an earlier normalized integral.
The base \(E_N\) has degree at most four.

The exact forward field \(a\) satisfies \(G(a)=0\). If \(s_v\) is
the number of proper vertices in the subtree at \(v\), induction gives
\[
 \|a_v\|\le\sigma^{s_v},\qquad
                 k:=ca={K_N\over\widehat B_N},\qquad
                         |k|\le\sigma^{s+1}.                 \tag{3}
\]
Indeed a leaf supplies one factor, a turn adds one factor, and a
product multiplies its two child bounds and adds one factor.
Neither \(a\) nor \(k\) is input to define the integral.

## 2. The compact polynomial integral

At every binary product retain exactly one child occurrence, as in
[L,F]. These are \(p\) distinct packets because each proper packet
has a unique parent. Write their coordinates as \(u\in\mathbb C^n\),
\(n=Np\), and the remaining coordinates as \(z\in\mathbb C^h\),
\(h=D-n\). The top packet is among the eliminated variables \(z\).

At fixed \(u\), every product is linear in its remaining variable.
Split the proper residual rows according to their output packets,
and include the scalar closing in the second list:
\[
 r_z=T(u)z+b_z(u),\qquad
 r_o=C(u)z+b_o(u),\qquad r_o\in\mathbb C^{n+1}.              \tag{4}
\]
In the tree order \(T=-I+A_{zz}\), with \(A_{zz}\) strictly
triangular. Thus \(T^{-1}\) is a finite polynomial for every
\(u\in\mathbb C^n\), and \(|\det T|=1\). Define the known maps
\[
 z_0=-T^{-1}b_z,\qquad
 \mathsf D=CT^{-1},\qquad F=b_o-CT^{-1}b_z,\qquad
 R=I_{n+1}+\mathsf D\mathsf D^*,\quad q=F^*R^{-1}F.          \tag{5}
\]
The field \(z_0(u)\) solves all eliminated gate equations exactly by
forward substitution. The components of \(F(u)\) are precisely the
retained gate residuals and the original scalar closing at this field.
In particular \(F\) is a known holomorphic polynomial vector.

Every component has degree at most \(L\). To check this, treat each
retained child as an independent input of degree one, bounded by its
original subtree leaf count. Solved leaves are constant, turns preserve
the bound and products add the two child bounds. The extra retained
residual term \(-u_v\) has degree one. This proves the assertion for
the retained rows and the top closing as well.

Let \(\mathcal U_N\) be the product of the \(p\) closed unit packet
balls. Our compact unweighted integral is
\[
 \boxed{\qquad
 \mathcal J_N={n!\over\pi^n}\int_{\mathcal U_N}
                         \|F(u)\|^{-2(n+1)}du .\qquad}       \tag{6}
\]
All integrals are extended and nonnegative. When \(p=0\), use the
one-point convention for \(\mathbb C^0\); then \(F=k\) and
\(\mathcal J_N=|k|^{-2}\), with value \(+\infty\) at zero.
The polynomial \(\|F\|^2\) can have degree \(2L\); it is not
asserted to be a quartic after elimination.

For reference, the exact full-space integration of the linear packets
from [F] is
\[
 \mathcal P_N={n!\over\pi^n}\int_{\mathbb C^n}
                      {du\over\det R(u)\,q(u)^{n+1}} .      \tag{7}
\]
Indeed the change \(v=Tz+b_z\) preserves measure and gives
\(E_N=\|v\|^2+\|\mathsf Dv+F\|^2\). Completing its Hermitian
square uses \(I_h+\mathsf D^*\mathsf D\), whose determinant is
\(\det R\), and residual constant \(q\). The radial beta integral is
\(\pi^h n!/[D!\det R\,q^{n+1}]\). Tonelli proves (7), also
when either side is infinite. No bounded-field estimate is used here.

## 3. The determinant and the omitted exterior are controlled

On \(\mathcal U_N\), each row of \(A_{zz}\) has at most one
eliminated child, and each column enters at most one parent row.
Its nonzero blocks have norm at most \(\sigma\). The same holds for
\(C\), counting the closing as the top packet's unique parent.
Consequently the argument of [L] uses only bilinear operator norms and
gives
\[
 \|A_{zz}\|\le\sigma,\quad \|C\|\le\sigma,\quad
 \|T^{-1}\|\le(1-\sigma)^{-1},\quad
 \|\mathsf D\|\le{\sigma\over1-\sigma}.                    \tag{8}
\]
Set
\[
 \eta_N=(16N-1)^{-2},\qquad
 \tau_N=(n+1)\log(1+\eta_N),\qquad
 \delta_N=16DL\sigma^{2s+2}.                                \tag{9}
\]
Every eigenvalue of \(R\) lies between \(1\) and \(1+\eta_N\).
Also \(\|F\|^2/(1+\eta_N)\le q\le\|F\|^2\). Therefore,
pointwise with the extended convention at \(F=0\),
\[
 e^{-\tau_N}\|F\|^{-2(n+1)}
 \le {1\over\det R\,q^{n+1}}
 \le e^{\tau_N}\|F\|^{-2(n+1)}.                            \tag{10}
\]
Let \(\mathcal P_{N,\mathcal U}\) denote (7) restricted to
\(\mathcal U_N\). Integration proves
\(e^{-\tau_N}\mathcal P_{N,\mathcal U}\le\mathcal J_N
\le e^{\tau_N}\mathcal P_{N,\mathcal U}\).

To control the rest of (7), use the global residual coordinates
\[
 x=H(r),\qquad H(r)_v=\Phi_v((H(r)_j)_j)-r_v,\qquad
                         |\det_{\mathbb R}DH|=1.             \tag{11}
\]
The inverse is polynomial and triangular. On \(\|r\|\le1/4\),
upward induction bounds every packet by \(\sigma+1/4<1\): maps
on previously bounded inputs have norm at most \(\sigma\).
Hence a point whose retained packet lies outside \(\mathcal U_N\)
must satisfy \(\|r\|>1/4\). Since \(E_N(H(r))\ge\|r\|^2\),
\[
 0\le\mathcal P_N-\mathcal P_{N,\mathcal U}
 \le {D!\over\pi^D}\int_{\|r\|>1/4}\|r\|^{-2D-2}dr=16D
                                                               \tag{12}
\]
when the integrals are finite; the exterior bound remains valid in
the extended case.

The source polynomial \(f(r)=cH(r)\) has degree at most \(L\)
and \(f(0)=k\). Finite-fiber orthogonality [F] gives
\(\mathcal P_N\ge1/(L|k|^2)\) when \(k\ne0\). Equations
(3) and (12) thus make the omitted exterior a relative error at most
\(\delta_N\). Combining with (10) proves the all-level comparison
\[
 \boxed{\qquad
 (1-\delta_N)e^{-\tau_N}\mathcal P_N
       \le\mathcal J_N\le e^{\tau_N}\mathcal P_N .\qquad}   \tag{13}
\]
Here \(L\le s\) implies \(\delta_N\le1/(4096N^3)<1\): the
successive ratio of \(s^2\sigma^{2s+2}\) is at most
\(4\sigma^2<1\), so its maximum is at \(s=1\).

The full integral is finite exactly when \(k\ne0\), by [F] or the
residual-coordinate argument below. At \(k=0\), (12) has finite
exterior, so \(\mathcal P_{N,\mathcal U}=\mathcal J_N=+\infty\).
For nonzero \(k\), (13) also proves finiteness and positivity of
\(\mathcal J_N\). In particular, with reciprocal zero at infinity,
\[
 |K_N|^2\ge{(1-\delta_N)e^{-\tau_N}\widehat B_N^2
                                      \over L\mathcal J_N}  \tag{14}
\]
at every level, including zeros.

## 4. A short two-sided calibration in the same metrics

Assume \(k\ne0\) until the separate zero case below.
The polynomial normalization also supplies a direct affine comparison.
On the residual ball of radius \(1/4\), write \(DG=-I+A\).
The unique-parent pattern and the two children per product give
\(\|A\|\le\sqrt2\sigma\le1/8\), hence \(\|DH\|\le8/7\).
At a product the second derivative is
\(\Phi(h_L,k_R)+\Phi(k_L,h_R)\). Cauchy--Schwarz on sibling pairs,
followed by their disjointness, bounds its direct-sum norm by
\(\sigma\|h\|\|k\|\). Twice differentiating \(G(H(r))=r\)
therefore gives
\[
 \|D^2f\|\le M_N:=\sigma^2(8/7)^3<2\sigma^2\le1,
 \quad f(r)=k+dr+p(r),\quad |p(r)|\le{M_N\over2}\|r\|^2 .\tag{15}
\]
This uses \(\|c\|\le\sigma\), with no sharper physical closing
estimate. Put \(E_{\rm aff}=\|r\|^2+|k+dr|^2\). Completing its
Hermitian square gives the exact cancellation of slope and determinant:
\[
 {D!\over\pi^D}\int_{\mathbb C^D}E_{\rm aff}^{-D-1}dr
                         ={1\over|k|^2}\qquad(k\ne0).      \tag{16}
\]
Specifically the square has determinant \(1+\|d\|^2\) and residual
constant \( |k|^2/(1+\|d\|^2)\); their product is \( |k|^2\).

On this ball, \(|p|\le(M_N/8)\sqrt{E_{\rm aff}}\). Applying
the triangle inequalities to the augmented vector \((r,k+dr)\) yields
\[
 (1-M_N/8)^2E_{\rm aff}\le E_N(H(r))
                                  \le(1+M_N/8)^2E_{\rm aff}.\tag{17}
\]
Since \(-\log(1-t)\le t/(1-t)\), the relative integrand error
is at most \(\exp[(2/7)(D+1)M_N]-1\). Both energies dominate
\(\|r\|^2\), so each normalized exterior integral is at most
\(16D\). Comparing inside and outside, as in [R], proves
\[
 \big||k|^2\mathcal P_N-1\big|\le\epsilon_N^{\rm aff},\quad
 \epsilon_N^{\rm aff}:=
 e^{(2/7)(D+1)M_N}-1+32D\sigma^{2s+2}.                      \tag{18}
\]
In particular no lower bound on the possibly tiny nonzero source was
used. Its energy has no zero on a compact set, and the exterior is
integrable. At \(k=0\), \(f(r)=O(\|r\|)\) near zero makes the
radial integral dominate a multiple of \(\int_0^{1/4}t^{-3}dt\),
which verifies the divergence assertion used above.

For a fixed tree, \(\tau_N=O_T(N^{-1})\),
\(\epsilon_N^{\rm aff}=O_T(N^{-1})\) and \(\delta_N=O(N^{-3})\).
For nonzero sources a fully known common error is
\[
 \epsilon_N=e^{\tau_N}(1+\epsilon_N^{\rm aff})-1+\delta_N
        =O_T(N^{-1}),\qquad
                       \big||k|^2\mathcal J_N-1\big|\le\epsilon_N.
                                                               \tag{19}
\]
The lower estimate follows from (13) and (18); if
\(\epsilon_N^{\rm aff}>1\), it follows instead from nonnegativity.
For all sufficiently large levels, \(\epsilon_N<1\), and hence
\[
 (1-\epsilon_N){\widehat B_N^2\over\mathcal J_N}
 \le |K_N|^2\le
 (1+\epsilon_N){\widehat B_N^2\over\mathcal J_N}.            \tag{20}
\]
The zero convention makes (20) valid at source zeros too.

## 5. Metric choice, normalization and the remaining lower bound

One may prescribe any positive Hermitian metric on each complete
packet space, independently of the unknown closed value. In its
orthonormal coordinates choose known base budgets making the actual
leaf, linear, bilinear and closing norms at most \(1/16\), then use
(1). The unique-parent arguments, triangular real Jacobian one,
finite-fiber degree bound and affine proof remain unchanged.
The measure and every norm in (2)--(7) must be rebuilt consistently.
No comparison with the old packet metrics is required.

The added budget factor is exactly \(N^{s+1}\). For a fixed tree
its logarithm is \(o(N)\); every actual budget and external phase
still has to be restored. Neither the numerical integral nor its
polynomial residual vector is claimed to be metric independent.
The denominator exponent \(n+1\) grows with the level.

The improvement is removal of the unbounded retained integration
domain and its Gram determinant after a specified polynomial
normalization, together with a short two-sided comparison in those
same metrics. The fixed-ball affine argument is already in [R];
[U] proves an undamped physical comparison with unchanged budgets.
Here no physical shrinking-row estimate or Wick coefficient estimate
is needed. The present proof does not improve their original
normalization constants.

To prove a geometric lower bound one still needs a geometric upper
estimate on \(\mathcal J_N/\widehat B_N^2\). The original signed
closing remains a component of \(F\); a zero source gives an infinite
integral. Compactness and positivity alone supply no such upper
estimate. Both its dimension \(n=Np\) and denominator exponent
\(n+1\) still grow with the level; the prefactor \(n!/\pi^n\)
remains. This is not a fixed-dimensional Laplace reduction or an
identification with a classical angle integral. There is no new
arbitrary-short-filling or finite-exception volume theorem.

## Complete inputs and coverage

The five complete matching texts fix the actual source and the closest
reductions. The new compact estimates and normalization are proved above.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| P | [Physical compiler](research_conway_uniform_physical_quartic.md) | 477 | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| F | [Finite fibers and exact linear integration](research_conway_reciprocal_finite_fiber_lower_bound.md) | 285 | 4e708365d2d6f14a557c3af4d17bd7c489f784faf905b490e6e4bcfeec0f26cb |
| L | [Linear packet elimination](research_conway_orthogonal_linear_elimination.md) | 344 | aa53b79685296193d5bf7fc66e53f3a3fbe03fc72a36481fb3aee23afe2ae113 |
| U | [Unchanged undamped physical integral](research_conway_undamped_reciprocal_source.md) | 311 | 4ce9ae44a5ed6f7f54145d96712a7937f2e8c4181e2292aa5f2c44e84ffb3a8a |
| R | [Fixed-ball affine comparison](research_conway_reciprocal_quartic_source_formula.md) | 233 | ead3945544c91ed81b87423f05c80dde29439d2be183b391005b133610e84e97 |

Only written mathematics, text reads and metadata operations were used.
Earlier final notes, the progress ledger and public manuscripts are unchanged.
