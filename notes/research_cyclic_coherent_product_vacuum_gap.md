# A positive cyclic vacuum operator for the actual coherent product

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

Two centered geometric-series inputs have explicit positive
annihilators with a constant gap. Their actual product has a
bounded cyclic first-order annihilator whose positive square has
that entire output line as its simple kernel and gap at least
\(N^{-2}\), uniformly on each compact complex input bidisk for
large \(N\). The endpoint wrap is explicitly determined by the
original source. No packet tail or repeated-root coordinate is removed.

This is one exact multiplication primitive, also preserved by a
genuine turn. It does not assert closure of this packet family
under further crossings or arbitrary binary composition.

## 1. The full source packets and their nonzero coefficients

Use the full original algebra and the two orthonormal bases of the
[centered compiler](research_centered_fourier_conway_compiler.md):
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\quad
 \mathcal H_N=\mathbb C[s]/(2T_N(s/2)+2).
 \tag{1}
\]
The Newton vectors \(e_j\) and centered vectors \(f_a\) are each
Hermitian orthonormal in the Newton coefficient metric. This is
the full \(N\)-dimensional algebra, retaining the value and
first-derivative coordinates at its repeated roots. It is not
the uniform physical Hilbert--Schmidt metric.

Put
\[
 Z_N(t)=\sum_{a=0}^d|t|^{2a},\qquad
 u_N(t)=Z_N(t)^{-1/2}\sum_{a=0}^d t^af_a,\qquad
 w_N(y,z)=u_N(y)u_N(z),\qquad D_N(t)=1-\eta t^N .
 \tag{2}
\]
The exact whole-output theorem gives the Newton coefficients
\[
 w_N=\sum_{j=0}^d b_je_j,\qquad
 b_j=\frac{\kappa^2(-q)^jD_N(y)D_N(z)}
               {N\sqrt{Z_N(y)Z_N(z)}}\,H_j,
 \quad
 H_j=\frac{(Q;Q)_j(Qyz;Q)_j}
                 {(-qy;Q)_{j+1}(-qz;Q)_{j+1}} .
 \tag{3}
\]
Here \((a;Q)_j=\prod_{h=0}^{j-1}(1-aQ^h)\).
Every \(b_j\) is nonzero for \(|y|,|z|<1\).
All norms and orthogonal complements below use this same
positive full coefficient metric.

Fix \(0<r<1\); all uniform statements concern \(|y|,|z|\le r\).
No unknown invariant or output norm is used in the operators below.

## 2. Each input has a constant-gap positive vacuum operator

In centered coordinates define the rectangular map
\[
 (\mathsf B_t x)_a=x_{a+1}-t x_a,\qquad 0\le a<d.
 \tag{4}
\]
Its kernel is exactly \(\mathbb C u_N(t)\), including \(t=0\).
The matrix \(\mathsf B_t\mathsf B_t^*\) has diagonal
\(1+|t|^2\), upper diagonal \(-\bar t\), and lower diagonal
\(-t\). Bounding each neighboring cross term gives
\[
 (1-r)^2I\le\mathsf B_t\mathsf B_t^*
                       \le(1+r)^2I.
 \tag{5}
\]
Thus \(\mathsf B_t^*\mathsf B_t\) has simple kernel
\(\mathbb C u_N(t)\) and all nonzero eigenvalues in that interval.
For completeness, on its kernel's orthogonal complement write
\(x=\mathsf B_t^*h\); applying (5) to
\((\mathsf B_t\mathsf B_t^*)^2\) proves the lower bound there.

If \(\mathsf P_t\) is projection onto this input line, the tensor
operator
\[
 \mathsf H_{\rm in}
   =\mathsf B_y^*\mathsf B_y\otimes I
                         +I\otimes\mathsf B_z^*\mathsf B_z
 \ \ge\ (1-r)^2(I-\mathsf P_y\otimes\mathsf P_z)
 \tag{6}
\]
has precisely the tensor input line as kernel. This follows by
decomposing each factor into its vacuum line and orthogonal complement.

## 3. The output recurrence includes a compulsory known wrap

The ratios of consecutive coefficients in (3) are exactly
\[
 \rho_j=\frac{b_{j+1}}{b_j}
 =-q\frac{(1-Q^{j+1})(1-Q^{j+1}yz)}
             {(1+qQ^{j+1}y)(1+qQ^{j+1}z)},
                         \qquad 0\le j<d.
 \tag{7}
\]
The original endpoint observations are
\[
 b_0=m(w_N)=
 \frac{\kappa^2D_N(y)D_N(z)}
  {N\sqrt{Z_N(y)Z_N(z)}(1+qy)(1+qz)},\qquad
 b_d=\phi(w_N)=
 \frac{1-(yz)^N}{(1-yz)\sqrt{Z_N(y)Z_N(z)}}.
 \tag{8}
\]
Consequently the missing cyclic step has the known nonzero coefficient
\[
 \boxed{\quad
 \rho_d=\frac{b_0}{b_d}
 =\frac{\kappa^2D_N(y)D_N(z)(1-yz)}
       {N(1+qy)(1+qz)(1-(yz)^N)} .
 \quad}
 \tag{9}
\]
It satisfies \(|\rho_d|\le C_r/N\). There are no denominator zeros
on the stated bidisk. In particular these formulas divide by no
unknown knot scalar. At \(y=z=0\), the actual product is
\((R^+)^2/N\) and the wrap is \(\kappa^2/N\).

Define a square cyclic first-order operator in Newton coordinates by
\[
 (\mathsf A_Nx)_j=x_{j+1}-\rho_jx_j\quad(0\le j<d),
 \qquad
 (\mathsf A_Nx)_d=x_0-\rho_dx_d .
 \tag{10}
\]
All ratios have modulus bounded by a constant depending only on \(r\),
so \(\|\mathsf A_N\|\le C_r\). Their product is exactly one,
as is also immediate from their definitions as consecutive ratios.
The first \(N-1\) equations therefore determine a vector from
its zeroth coefficient, and the last one is satisfied by (3).
Thus for every \(N\ge2\),
\[
          \ker\mathsf A_N=\mathbb Cw_N(y,z).
 \tag{11}
\]
This is an additional exact annihilator of the same original
packet. It does not alter the multiplication or its closing.
Prescribing its zeroth coefficient as in (8) recovers the actual
packet itself, with its original normalization.

The special last row must be retained. Let
\(\mathsf S e_j=e_{j-1}\) for \(j\ge1\), \(\mathsf S e_0=e_d\),
and \(\mathsf K e_j=Q^je_j\). Thus \(\mathsf S\) is the unitary
cyclic shift, including its wrap arrow. Then
\[
 \mathsf A_N=
 \mathsf S+q\frac{(I-Q\mathsf K)(I-Qyz\mathsf K)}
                   {(I+qQy\mathsf K)(I+qQz\mathsf K)}
       -\rho_d|e_d\rangle\langle e_d|.
 \tag{12}
\]
The two denominator factors have uniformly bounded inverses
on this bidisk. Formula (12) includes an explicit rank-one endpoint
correction of norm \(O_r(N^{-1})\); it is not asserted to be
a polynomial of fixed degree in the clock alone.
This coefficient-index clock is not the
Casimir spectral coordinate or the main-color meridian orbit.

## 4. The exact finite weights have one cyclic peak

For \(|v|=1\), define
\[
 R_N(v)=\frac{(1-v)(1-yzv)}
                   {(1+qyv)(1+qzv)},\qquad
 R_\infty(v)=\frac{(1-v)(1-yzv)}
                   {(1+yv)(1+zv)}.
 \tag{13}
\]
The whole-output theorem proves that
\(|R_\infty(e^{2\pi iu})|^2-1\) has exactly two simple zeros
\(0<u_-<u_*<1\), is positive between them, and is negative
on the remaining arc. The roots are uniformly separated
from each other and the endpoints on the compact input bidisk.
This is the theorem's exact single-cosine argument, not an
inference from a Gaussian approximation.

The denominators in (13) are bounded away from zero. Since
\(q=1+O(N^{-1})\), on the full circle
\[
 \bigl\||R_N|^2-|R_\infty|^2\bigr\|_{C^1}
                                      \le C_r/N .
 \tag{14}
\]
Here the derivative is with respect to the circle angle.
Choose disjoint small neighborhoods of the two limiting roots,
uniformly in the compact parameters. The limiting derivatives
have a fixed nonzero sign in their respective neighborhoods;
outside, the limiting function has modulus bounded below.
For large \(N\), (14) preserves these derivative signs and the
outside signs. The intermediate-value theorem then gives exactly
one root in each neighborhood and no others.

Set \(\mu_j=|b_j|^2>0\). Equation (7) gives
\[
             \mu_{j+1}/\mu_j=|R_N(Q^{j+1})|^2
                                     \quad(0\le j<d).
 \tag{15}
\]
For large \(N\) the initial and final sampled steps have ratio
less than one, the middle interval of steps has ratio greater
than one, and the wrap ratio \(\mu_0/\mu_d=|\rho_d|^2\) is
also less than one. Thus the weights have one peak and one
valley in cyclic order: from any index there is a path to a
maximizing index along which the weights weakly increase.
An exact crossing can land on a grid point, creating adjacent
equal weights. The maximizing index need not be unique, and
the argument includes such plateau steps.

## 5. A weighted-cycle inequality and the spectral gap

We use the following elementary fact. Let positive weights
\(\mu_0,\ldots,\mu_{N-1}\) admit one fixed maximizing index \(k\)
to which every index has a weakly increasing path on the cycle.
The single peak plateau just proved has this property.
Orient the cycle by \(j\mapsto j+1\), and assign edge conductance
\(\mu_{j+1}\), with indices modulo \(N\).
For any complex \(g_j\), choose a weakly increasing path from
each \(j\) to that \(k\). Along a forward
step its conductance is the destination weight; along a backward
step it is the departure weight. In either case it is at least
the starting weight \(\mu_j\) of that entire path.
The path has at most \(N-1\) edges. Cauchy--Schwarz therefore gives
\[
 \mu_j|g_j-g_k|^2
 \le N\sum_{e\text{ on its path}}\mu_{\operatorname{next}(e)}
                                      |\Delta_eg|^2 .
 \tag{16}
\]
Summing, and allowing every edge to appear in all \(N\) paths,
proves
\[
 \sum_j\mu_j|g_j-g_k|^2
       \le N^2\sum_{j=0}^{N-1}\mu_{j+1}|g_{j+1}-g_j|^2.
 \tag{17}
\]
If \(\sum_j\mu_jg_j=0\), the left side is at least
\(\sum_j\mu_j|g_j|^2\), by expansion of its square.
This proves the weighted variance inequality without any
lower bound for the smallest weight.

Apply it to \(x_j=b_jg_j\). All \(b_j\) are nonzero, and (10) gives
\[
 \|\mathsf A_Nx\|^2
    =\sum_{j=0}^{N-1}\mu_{j+1}|g_{j+1}-g_j|^2 .
 \tag{18}
\]
The condition \(x\perp w_N\) is exactly
\(\sum_j\mu_jg_j=0\). Hence, uniformly for large \(N\),
\[
 \boxed{\quad
 \|\mathsf A_Nx\|^2\ge N^{-2}\|x\|^2
                  \quad(x\perp w_N),\qquad
 \mathsf A_N^*\mathsf A_N
       \ge N^{-2}(I-\mathsf P_{\rm out}).
 \quad}
 \tag{19}
\]
Here \(\mathsf P_{\rm out}\) is orthogonal projection onto
\(\mathbb Cw_N\). The positive operator has a simple zero
eigenvalue, the displayed gap, and uniformly bounded norm.
All estimates apply on the entire packet space.

For any trial packet, decomposing into the kernel and its complement
also gives the a posteriori direction estimate
\[
 \operatorname{dist}(x,\mathbb Cw_N)
                            \le N\|\mathsf A_Nx\|.
 \tag{20}
\]
The exact kernel statement holds at every level. The explicit gap
(19) is asserted for \(N\ge N_0(r)\); no parity or composite
subsequence is excluded.

## 6. The exact multiplication step, turns and scope

The original multiplication \(M\) sends the input vacuum line to
the output vacuum line:
\[
 M(u_N(y),u_N(z))=w_N(y,z)\ne0,\qquad
 \mathsf A_N M(\mathsf P_y\otimes\mathsf P_z)=0 .
 \tag{21}
\]
Thus both the input and output lines are selected by explicit
positive operators with polynomial gaps. This identity is only
on the selected input line, not a full bounded intertwiner
identity for arbitrary incoming tensors.

The genuine turn is unitary, \(Je_j=e_{d-j}\). Consequently
\(J\mathsf A_NJ\) has kernel \(\mathbb C Jw_N\), the same norm
bound, and the same positive spectral gap. This transports the
complete line, including its endpoints and phases.

The original \(m\) and \(\phi\) observations remain exactly (8).
Their ratios to the output norm can be exponentially small:
the whole-output theorem gives positive exponential norm
growth while these endpoint values stay bounded on compact
bidisks. The gap does not turn them into positive norm closures.
It selects an actual full direction, not a nonzero geometric
coefficient of an arbitrary closed tangle.

In particular, no polynomial gap is inferred for conjugation
by an arbitrary nonunitary short word. No closure under
products of arbitrary output vacua, physical binomial
coherent inputs, or arbitrary short components is established.
The compact bound \(r<1\) is fixed before \(N\); no uniform
claim at the unit input boundary is made.

## Complete proof sources

Both complete matching proof texts were read:

| Source | SHA-256 |
|---|---|
| [Actual whole coherent-product output, 393 lines](research_centered_coherent_product_energy.md) | 73152328a77ba5d63a2a8eaa17647ed38b7683c613e0947e3bda9e451dda76e2 |
| [Full centered compiler and genuine turn, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

The exact source coefficients, original endpoints and uniform
single-cosine statement are the inputs. The cyclic completion,
finite-level peak argument and weighted gap are proved above.
Weighted path estimates and positive squares of difference
operators are standard methods; no novelty is claimed for them.
Earlier polynomial-gap results for different actual operators
include the [two-head Ward current](actual_two_head_ward_polynomial_contraction.md)
and the [elementary cap path Laplacian](research_elementary_cap_path_laplacian.md).
Their full texts were checked for coverage; their proofs are
not premises here. The additional source-specific construction
is (7)--(12) and its cyclic gap for this coherent-product family.
No volume-conjecture class or finite-exception theorem is proved.
Only written mathematics and text operations were used.
