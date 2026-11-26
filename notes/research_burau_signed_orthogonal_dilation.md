# A signed Burau row model inside two positive row models

Written research proof, 22 November 2026.

The negative marked crossing has an exact isometric realization in
two copies of the positive marked row space. The image is selected by
two explicit orthogonal charge projectors and reduces all three lifted
generators and their adjoints. Consequently every ordered polynomial
in the original signed letters has an exact lift, without inserting a
projection between letters. The original initial row and final column
become specified entangled boundary vectors.

This is a common finite operator alphabet, not an entrywise positive
model or a completely positive representation of the scalar source.
It supplies no asymptotic lower bound. In particular its boundary
vectors cannot be replaced by products of positive terminal columns.

## 1. The two actual orthonormal row models

Let
\[
 N\ge2,\qquad d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,
 \qquad s_j=2\sin(\pi j/N),\qquad S_j=\prod_{a=1}^j s_a,
 \quad S_0=1.
 \tag{1}
\]
The positive row model [O] is a Hilbert space \(\mathcal H_+\)
with orthonormal rows \(f_{r,l}\), where \(r\in\mathbb Z/N\) and
\(0\le l\le d\). Its literal right actions are
\[
 \begin{aligned}
 f_{r,l}a&=\rho_l f_{r,l+1}\quad(l<d),& f_{r,d}a&=0,\\
 f_{r,l}b&=Q^{-2r}f_{r,l},&
 f_{r,l}c&=Q^l f_{r+1,l},
 \end{aligned}
 \qquad
 \rho_l=\frac{w_{l+1}}{w_l},\quad
 w_l^2=\sum_{h=0}^l\left|{l\brack h}_Q\right|^2.
 \tag{2}
\]
Here the Gaussian binomials have their polynomial values at the root
of unity. The weights are positive, \(\rho_l\le2\), and \(b,c\)
are unitary. All adjoints below are for this actual orthonormal row
metric. In particular
\[
 f_{r,l}a^*=\rho_{l-1}f_{r,l-1}\quad(l>0),\qquad
 f_{r,0}a^*=0,\qquad
 f_{r,l}c^*=Q^{-l}f_{r-1,l}.
 \tag{3}
\]

The negative Fourier row model [F] has orthonormal rows
\(F_{p,j}\), with \(p\in\mathbb Z/N\) and \(0\le j\le d\).
It carries the original negative letters:
\[
 \begin{aligned}
 F_{p,j}a_-&=Q^{-p}(1-Q^{j+1})F_{p,j+1}\quad(j<d),&
 F_{p,d}a_-&=0,\\
 F_{p,j}b_-&=Q^{2(j-p)}F_{p,j},&
 F_{p,j}c_-&=QF_{p-1,j}.
 \end{aligned}
 \tag{4}
\]
Its initial marked row and terminal column are exactly
\[
 e_-^{\mathsf T}=N^{-1/2}\sum_{p=0}^d F_{p,p},\qquad
 H_-(p,j)=\sqrt N\,\delta_{p,0}.
 \tag{5}
\]
Thus \(\|e_-\|=1\), \(\|H_-\|=N\). The diagonal sum in
(5), including its \(p\) register, is part of the source.
Neither basis in (2) or (4) is an eigenvalue-only Casimir quotient.
Both were obtained from the complete original marked cyclic source.

## 2. The exact reflected weight identity

The weight identity used for the lift is
\[
 w_{d-r}^2=\frac{Nw_r^2}{S_r^2}\quad(0\le r\le d),
 \qquad \rho_l\rho_{d-1-l}=s_{l+1}\quad(0\le l<d).
 \tag{6}
\]
It is already recorded in the endpoint calibration of the progress
ledger; the following finite proof makes the present argument
independent of that ledger.

The factorization of \((z^N-1)/(z-1)\) at \(z=1\), together
with \(s_{N-a}=s_a\), gives \(S_d=N\) and
\(S_jS_{d-j}=N\). For \(h\le d-r\), therefore,
\[
 \left|{d-r\brack h}_Q\right|
 =\frac{S_{d-r}}{S_hS_{d-r-h}}
 =\frac1{S_r}\prod_{a=1}^r s_{h+a}.
 \tag{7}
\]
If \(d-r<h<N\), the last product contains \(s_N=0\).
Thus its squared sum can be extended to the whole cyclic grid.
Put
\[
 P_r(T)=\prod_{a=1}^r(1-Q^aT)
 =\sum_{h=0}^r(-1)^hQ^{h(h+1)/2}{r\brack h}_Q T^h.
 \tag{8}
\]
The coefficient formula follows by induction on \(r\), multiplying
by the last factor. Since \(r<N\), character orthogonality has
no aliases between the exponents in (8). Consequently
\[
 \sum_{h=0}^{N-1}|P_r(Q^h)|^2=Nw_r^2,
 \qquad
 w_{d-r}^2=S_r^{-2}\sum_{h=0}^{N-1}|P_r(Q^h)|^2.
 \tag{9}
\]
These are the first identity of (6). Taking its consecutive ratio
and using positivity proves the second. No inverse of two, parity
restriction or prime-level assumption enters this calculation.

In particular \(a\otimes a^*\) on the height-charge space
\(\operatorname{span}\{|j,d-j\rangle\}\) has precisely the
positive weights \(s_{j+1}\). Their accumulated magnitude is exactly
\[
 \left(\prod_{h=0}^{j-1}\rho_h\right)
 \left(\prod_{h=d-j}^{d-1}\rho_h\right)
       =\frac{w_jw_d}{w_{d-j}}=S_j\qquad(0\le j\le d).
 \tag{9a}
\]
Thus the paired transport retains the actual negative factorial
scale, rather than two independent positive weight products.
To recover the full negative triple, one must also retain its phases
and its cyclic register. We do so next.

## 3. The full triple and its reducing charge space

In \(\mathcal H_+\otimes\mathcal H_+\), define
\[
 \mathsf A=a\otimes(a^*c^*),\qquad
 \mathsf B=b\otimes b,\qquad
 \mathsf C=Q(c^*\otimes I).
 \tag{10}
\]
Products in (10) act from the right in their displayed order.
In particular \(a^*c^*\) first lowers height and then lowers
the cyclic register. The ambient bounds are
\(\|\mathsf A\|\le4\) and
\(\|\mathsf B\|=\|\mathsf C\|=1\).

Set
\[
 v_{p,j}=f_{p,j}\otimes f_{-j,d-j},\qquad
 \alpha_{p,j}=i^jQ^{pj}q^{j(j+5)/2},\qquad
 V(F_{p,j})=\alpha_{p,j}v_{p,j}.
 \tag{11}
\]
Every exponent in (11) has its displayed complex-exponential
meaning; no modular division by two is performed. The expression
is periodic in \(p\), including at the transition from zero to
\(N-1\). Its modulus is one. The vectors \(v_{p,j}\) are
distinct orthonormal rows, so \(V\) is an isometry onto an
\(N^2\)-dimensional space \(\mathcal V\).

**Theorem 1.** For each of the three letters and its adjoint,
\[
 V\mathsf A=a_-V,\qquad V\mathsf B=b_-V,\qquad
 V\mathsf C=c_-V,
 \qquad
 V\mathsf A^*=a_-^*V,\quad
 V\mathsf B^*=b_-^*V,\quad V\mathsf C^*=c_-^*V.
 \tag{12}
\]
Here \(V\) also denotes the matrix whose rows are the images in
(11), so \(VV^*=I\). In particular \(\mathcal V\) reduces
all three ambient operators.

**Proof.** For \(j<d\), (3) and (6) give
\[
 v_{p,j}\mathsf A=s_{j+1}Q^{j+2}v_{p,j+1},\qquad
 \frac{\alpha_{p,j+1}}{\alpha_{p,j}}
       =iQ^p q^{j+3}.
 \tag{13}
\]
Since \(1-Q^{j+1}=-i q^{j+1}s_{j+1}\), these are exactly
the first equation in (12). At \(j=d\), both sides vanish.
For the other two letters the ungauged actions are
\[
 v_{p,j}\mathsf B=Q^{2(j-p)}v_{p,j},\qquad
 v_{p,j}\mathsf C=Q^{1-j}v_{p-1,j},\qquad
 \alpha_{p-1,j}=Q^{-j}\alpha_{p,j}.
 \tag{14}
\]
They prove the remaining forward identities, including the cyclic
\(p=0\) boundary.

The adjoint \(\mathsf A^*=a^*\otimes(ca)\) maps a basis row
\(v_{p,j}\), for \(j>0\), to a scalar multiple of
\(v_{p,j-1}\); it vanishes at \(j=0\). Explicitly its coefficient
is \(s_jQ^{-j-1}\), the conjugate of the coefficient in (13)
at the preceding height. The other adjoints preserve the span
because \(\mathsf B\) is diagonal and \(\mathsf C^*\) only
raises \(p\). Thus \(\mathcal V\) is invariant under the
ambient operators and their adjoints. Taking adjoints after
restriction to this reducing space proves all of (12). \(\square\)

The orthogonal projection \(\Pi=V^*V\) is explicit without
using any unknown source vector. On the tensor basis
\(f_{r_1,l_1}\otimes f_{r_2,l_2}\), it is
\[
 \Pi=\mathbf1_{\{l_1+l_2=d\}}
             \mathbf1_{\{r_2+l_1=0\ ({\rm mod}\ N)\}}.
 \tag{15}
\]
Indeed the two conditions give exactly the rows in (11). Equivalently
its diagonal entry is
\[
 \frac1{N^2}\sum_{u,v=0}^{N-1}
       Q^{u(l_1+l_2-d)+v(r_2+l_1)}.
 \tag{16}
\]
The first congruence is the literal charge equality in (15):
\(0\le l_1+l_2\le2d\) excludes \(d-N\) and \(d+N\).
The projection commutes with every operator in (10) and its adjoint.
There is therefore no projection loss between successive letters.
This assertion concerns the grouped letters in (10), not their
individual positive factors. For example
\(\Pi(a\otimes I)\Pi=0\), whereas
\(\Pi\mathsf A\Pi\ne0\). A projection cannot be inserted
between the factors \(a^*\) and \(c^*\) of a lifted letter.

## 4. Ordered source transport and the actual boundary vectors

For any noncommutative polynomial \(P\), including adjoint letters,
let \(\widetilde P\) be its literal ordered substitution from (10).
Repeated use of (12) gives
\[
 V\widetilde P=P(a_-,b_-,c_-)V,\qquad
 V\widetilde P V^*=P(a_-,b_-,c_-).
 \tag{17}
\]
No reordering or change of an auxiliary crossing sign is made.
The positive ambient letters and their adjoints are not being
identified with one another.

The original endpoints (5) become the row and column
\[
 \widetilde e_-^{\mathsf T}
  =N^{-1/2}\sum_{p=0}^d\alpha_{p,p}v_{p,p},\qquad
 \widetilde H_-(v_{p,j})
  =\sqrt N\,\overline{\alpha_{p,j}}\,\delta_{p,0},
 \tag{18}
\]
with the column zero off \(\mathcal V\). These are
\(e_-^{\mathsf T}V\) and \(V^*H_-\), respectively. Hence
\[
 e_-^{\mathsf T}P(a_-,b_-,c_-)H_-
       =\widetilde e_-^{\mathsf T}\widetilde P\widetilde H_-.
 \tag{19}
\]
Their norms remain one and \(N\). In particular the initial
diagonal sum has not been replaced by one basis row, and the
terminal column is not \(H_+\otimes H_+\).
Their pairing is exactly one, since (5) gives
\(e_-^{\mathsf T}H_-=1\).

For a complete marked braid source use (10) at every negative
auxiliary occurrence and leave every positive occurrence unchanged.
Tensoring the isometries gives \(V_{\rm all}\). It intertwines
every ordered operator in the original principal-minor construction.
If \(k\) is the number of crossing occurrences, that construction
has the exact compressed source [F, B]
\[
 K_N=\zeta\,E^{\mathsf T}
           \left(\sum_{r=0}^{L-1}C^r\right)H,\qquad
 L=kd+1,\quad C^L=0,\quad
 \zeta=Q^{(b-1+w)/2}.
 \tag{20}
\]
Here \(b\) is the number of physical braid heads, \(w\) the
physical writhe, and the auxiliary list is still the original
reversed, sign-mirrored list. With literal lifted polynomial
\(\widetilde C\), (17) gives exactly
\[
 K_N=\zeta\,(E^{\mathsf T}V_{\rm all})
       \left(\sum_{r=0}^{L-1}\widetilde C^{\,r}\right)
                          (V_{\rm all}^*H).
 \tag{21}
\]
Thus all framing, pivots, ordered minors and the original closing
are retained. The global endpoint norms remain one and \(N^k\).

The lifted operator is in fact nilpotent on the entire ambient
space, so (21) is also its ordinary selected inverse element.
Here is the direct height argument, which does not infer an
ambient assertion merely from compression. Give a positive
occurrence its height \(l\), and a doubled negative occurrence
the height \(l_1\) of its first positive factor. Each lifted
\(a\)-letter increases this height by one, with zero output
at \(d\); every lifted \(b,c\)-letter preserves it.

In the original principal-minor definition [B, Section 2], setting
all \(a\)-letters to zero makes every local block a weighted
transposition. The full product has the one-cycle zero pattern
of the knot permutation. After deleting the distinguished head,
no nonempty remaining set of heads is invariant under this
permutation. Thus every principal-minor term without an
\(a\)-letter is zero by its index pattern, independently of
coefficient order. Every surviving monomial in \(\widetilde C\)
therefore increases the total first height by at least one.
That height lies in \(0,\ldots,kd\), so
\[
 \widetilde C^{\,L}=0,\qquad
 K_N=\zeta\,(E^{\mathsf T}V_{\rm all})
        (I-\widetilde C)^{-1}(V_{\rm all}^*H),
 \qquad L=kd+1.
 \tag{22}
\]
This proof retains the knot-permutation assumption from the
original source; no analogous single-cut assertion is made for
a braid closure with several permutation cycles.

## 5. Meaning and limitations

The scalar reflection of the positive row weights and the negative
sine-weighted shift now belong to one exact construction. The
additional cyclic register, adjoint order, phase gauge and entangled
endpoints extend that observation to the entire signed source.
They are needed even at even or composite levels.

The construction enlarges an \(N^2\)-dimensional negative local
space to a specified reducing subspace of an \(N^4\)-dimensional
positive tensor square. It does not reduce the dimension of the
original observable module. More significantly, a product of positive
letters and adjoints is not a matrix with nonnegative entries.
Neither (19) nor (21) is a positive trace or a completely positive
replacement of the original complex scalar. The known projection
and boundary vectors retain interference and cannot be omitted.
No geometric packet estimate, arbitrary-short-filling lower bound,
or new volume identity is inferred.
The modulus-one assertion for \(\alpha_{p,j}\) is a statement
on this finite grid Hilbert space. No continuation as an isometric
frame at complex peripheral or activity parameters is asserted;
any such continued phase factors would have to remain explicit.
The source comparison is for the original closed knot scalar
and the stated observable row module. It does not automatically
realize arbitrary free physical boundary polynomials, independent
Casimir-normal insertions, or generic-\(q\) derivatives. Such
insertions need their own exact marked operators before (17)
can be applied.

The prior row and Fourier models already give all local actions and
the complete signed source. The weight reflection was already proved
in the endpoint-calibration ledger. The assertion here is the explicit
simultaneous reducing lift (10)--(19) and its ordered source assembly;
no novelty is claimed for finite Fourier orthogonality or isometric
compression in general.

## Complete proof sources

All three complete proof texts were read at the following unchanged pins.
The complement-weight proof, charge projection, phase gauge and
intertwining calculations are given in full above.

| Label | Proof source | SHA-256 |
|---|---|---|
| O | [Orthogonal marked row model](research_burau_orthogonal_marked_row_model.md) | faade30be18b475de010b68cef3a5c5438e727fb17c599f38b97578ad369e4be |
| F | [Fourier height contraction](research_burau_fourier_height_contraction.md) | bd72b2891707846966ccb30e910ca58dc7d9243e692046694cee88b98321e350 |
| B | [Original cyclic marked source](research_burau_cyclic_marked_source_bridge.md) | 7edce1a2c39ddf213066de0026fa60b44545f9eaab25679580926e842092c496 |

Only written algebra and text/hash inspection were used. No mathematical
program, numerical experiment, test, build, git action or frozen-file
edit was performed.
