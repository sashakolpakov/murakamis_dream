# Second meridian normals recover the complete actual boundary vector

Private written proof, 15 November 2026.

The prescribed last-coordinate closing row becomes rank-one observable
at completeness for the Casimir transported through the actual turn.
Its missing observations have exactly a double meridian zero. Keeping
that double zero recovers every original boundary coefficient by second
derivatives, with a polynomial factor in the microscopic coordinate.
The derivative order is independent of the level; the number and degree
of the inserted observations are not.

This is an exact source statement for arbitrary holomorphic boundary
vectors in the specified physical coordinates. It neither identifies a
geometric critical summand nor proves that the prescribed uninserted
closing has a nonzero coefficient on it.

## 1. The actual transported Casimir and closing normalization

Fix \(N\ge2\), \(d=N-1\), \(\theta=\pi/N\), and \(q=e^{i\theta}\).
The physical main meridian is \(M=q^s\), with \(s\) near zero. Write
\[
\begin{split}
 c_j&=2\cos((2j+1)\theta),&
 S_j&=\prod_{r=1}^j2\sin(r\theta),\\
 e_j(z)&=S_j^{-2}\prod_{r=0}^{j-1}(c_r-z),&
 W_j(s)&=\prod_{r=1}^j
   \frac{\sin((r-s)\theta)\sin((r+s)\theta)}{\sin^2(r\theta)} .
\end{split}
 \tag{1}
\]
Empty products are one. The \(e_j\) are the **full complete Newton
polynomials**, including their repeated-node data, not polynomials of
the distinct-node quotient.

Equations (29) and (34) of the
[actual moving-meridian turn calculation](actual_main_meridian_turn_comparison.md)
give the following matrix in its fixed physical coefficient coordinates:
\[
\begin{split}
 (L_s)_{jj}&=c_j,\\
 (L_s)_{j-1,j}&=a_j(s):=-4\sin((j-s)\theta)\sin((j+s)\theta)
       \quad(1\le j\le d),\\
 (L_s)_{d,0}&=\beta_s:=(-1)^d4\sin^2(s\theta).
\end{split}
 \tag{2}
\]
All other entries vanish. In particular the bottom-left entry is retained.
It is the actual first-pair Casimir after the specified physical
intertwiner and turn adapters; it is not a guessed cyclic completion.
For the same-color turn the source identity is
\[
 \operatorname{coeff}\widehat{\mathcal T}_s(f)
   =\frac{q^{-s^2/2}}{H_N(s)}f(L_s)\mathbf e_d,\qquad
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{3}
\]
The physical mixed-order carrier is the one in that source. Thus the
polynomial insertions below are insertions in this transported actual
Casimir. The full scalar and carrier in (3) remain recorded.

Use \(\mathbf e_j\) for coordinate columns and
\(\ell=\mathbf e_d^T\) for the normalized coefficient closing row in
this specified adapter.
The [actual meridian compiler](actual_main_meridian_newton_compiler.md),
equations (5), (20), and (21), realizes coefficient extraction by the
actual partial pivotal trace after removal of the specified carrier.
For a closing endomorphism its primitive cut is \(H_N(s)\) times this
row; any further original framing scalar remains in the boundary vector
or is retained explicitly. For an intermediate mixed-order morphism
the carrier in (3) must also be retained before interpreting the
coefficient observation as a physical closure. At completeness all these
carriers specialize to the prescribed complete frame and \(H_N(0)=1\).
No identification of all orientation-dependent moving closing rows is
made from that specialization alone. None of these conventions divides
by the unknown invariant.

Let \(u(s)\in\mathbb C^N\) be any holomorphic actual boundary coefficient
vector in these coordinates. It may depend on fixed short powers and on
additional holomorphic boundary parameters. All claims below apply to
the complete vector, without discarding its high indices.

## 2. Exact inserted row identities

Define the uninserted observation and \(d\) inserted observations by
\[
 C_N(s)=\ell u(s),\qquad
 O_{j,N}(s)=\ell(L_s-c_0I)e_j(L_s)u(s),
                       \quad0\le j<d.
 \tag{4}
\]
The insertion degree is \(j+1\), at most \(d=N-1\).

**Proposition 1.** At every level, on the full holomorphic \(s\)-family,
\[
 \boxed{\qquad
 \ell(L_s-c_0I)e_j(L_s)=\beta_sW_j(s)\mathbf e_j^T,
 \qquad O_{j,N}(s)=\beta_sW_j(s)u_j(s).
 \qquad}
 \tag{5}
\]

**Proof.** The reflected nodes give \(c_d=c_0\), so the last row of
(2) gives
\[
                   \ell(L_s-c_0I)=\beta_s\mathbf e_0^T.
 \tag{6}
\]
Starting with \(\mathbf e_0^T\), successive factors
\((c_0I-L_s),\ldots,(c_{j-1}I-L_s)\) remove the diagonal term and
take the unique upper-diagonal path. The wrap row cannot be reached
before these \(j<d\) steps finish. Hence
\[
 \mathbf e_0^Te_j(L_s)
   =\frac{\prod_{r=1}^j[-a_r(s)]}{S_j^2}\mathbf e_j^T
   =W_j(s)\mathbf e_j^T.
 \tag{7}
\]
Combining (6) and (7) proves (5). No division by \(\beta_s\), spectral
separation, or semisimple specialization was used. \(\square\)

**Corollary 2.** Every complete boundary coordinate is recovered by
\[
 \boxed{\quad
 u_d(0)=C_N(0),\qquad
 u_j(0)=\frac{(-1)^dN^2}{8\pi^2}\,
                 \left.\partial_s^2 O_{j,N}(s)\right|_{s=0},
                    \quad0\le j<d .
 \quad}
 \tag{8}
\]
Equivalently, in the physical logarithmic meridian \(v=\log M\),
\[
 \boxed{\quad
 u_j(0)=\frac{(-1)^{d+1}}8
       \left.\partial_v^2
          O_{j,N}\!\left(\frac{Nv}{\pi i}\right)\right|_{v=0}.
 \quad}
 \tag{9}
\]

Indeed \(\beta_0=\beta'_0=0\), \(W_j(0)=1\), and
\(\beta''_0=(-1)^d8\pi^2/N^2\). Differentiating (5) twice therefore
leaves no derivative of \(u\) or \(W_j\). For (9), use
\(s=Nv/(\pi i)\), or directly
\(\beta_s=(-1)^{d+1}4\sinh^2v\).
These derivatives act on the entire finite matrix insertion in (4),
including its \(s\)-dependence.

If an inserted physical observation is written with a known scalar
\(h_N(s)\), holomorphic and nonzero at zero, its first two zero orders
are unchanged and
\[
 \left.\partial_s^2[h_N(s)O_{j,N}(s)]\right|_0
        =h_N(0)\,\partial_s^2O_{j,N}(0).
 \tag{10}
\]
Thus the actual cut and turn prefactors are restored exactly; their
derivatives cannot create an omitted term in (8). In particular this
holds for \(H_N(s)\) and the recorded turn phases in (3).

## 3. Smith factors and the ordinary Krylov determinant

Let \(\mathcal O_{s,0}=\mathbb C\{s\}\), with \(N\) fixed. Include both
the uninserted row \(\ell\) and the \(d\) rows in (5) in the observation
matrix. After ordering its output as
\((O_{0,N},\ldots,O_{d-1,N},C_N)\), that matrix is exactly
\[
                 \operatorname{diag}
                   (\beta_sW_0(s),\ldots,\beta_sW_{d-1}(s),1).
 \tag{11}
\]
Every \(W_j\) is a unit at zero, and \(\beta_s/s^2\) is a unit.
Multiplying rows by these explicitly nonvanishing units gives the
Smith factors
\[
                         1,\ s^2,\ldots,s^2 .
 \tag{12}
\]
In particular the observation cokernel is
\((\mathcal O_{s,0}/(s^2))^d\). This is an exact calculation of the
source lattice defect, not merely an order of a determinant.

For comparison, form the ordinary \(N\)-row Krylov matrix
\(\mathcal K_s\) with rows \(\ell L_s^k\), \(0\le k\le d\).
Then
\[
 \det\mathcal K_s
   =(-1)^d\beta_s^d
                    \prod_{j=1}^{d-1}a_j(s)^{d-j}.
 \tag{13}
\]
To verify the sign and every factor, replace \(z^k\), for \(k\ge1\),
by the monic polynomial
\[
 p_k(z)=(z-c_0)\prod_{r=0}^{k-2}(z-c_r),\qquad p_0=1.
 \tag{14}
\]
This is a unitriangular change of the polynomial list. Equations
(6)--(7) give row \(0\) equal to \(\mathbf e_d^T\), and row \(k\)
equal to \(\beta_s\prod_{j=1}^{k-1}a_j(s)\mathbf e_{k-1}^T\).
The column order \((d,0,\ldots,d-1)\) has sign \((-1)^d\), proving
(13). Rescaling the same polynomial list by its nonzero fixed-level
Newton constants shows that this Krylov matrix has the same Smith
factors (12).

Thus \(\mathcal K_s\) is invertible for \(0<|s|<1\), while at \(s=0\)
its rank is one:
\[
                      \ell L_0^k=c_0^k\ell.
 \tag{15}
\]
Its determinant has zero order \(2d\). This does **not** mean that
derivatives of order \(2d\) are needed. Formula (12) assigns order two
to each of \(d\) separate directions, and (8) recovers them all.

At a fixed nonzero \(s\), cyclicity implies that \(\ell\) pairs
nontrivially with every eigenvector of \(L_s\): a zero pairing would
make all rows \(\ell L_s^k\) kill that vector. At completeness the same
inference is unavailable. In particular (15) implies, for every
polynomial \(r\),
\[
                    \ell r(L_0)^k=r(c_0)^k\ell .
 \tag{16}
\]
This applies to an actual signed twist polynomial in the transported
pair Casimir, including its inverse polynomial when it is a unit.
It concerns that transported input pair and the fixed output closing
row; it does not replace the original Frobenius observation by a
different pair's trace. Generic cyclicity must therefore be transported
with its normal source lattice, not specialized after deleting the wrap.

## 4. Polynomial scale and exact scope of recovery

For any fixed \(0<R<1\), the paired-product estimate in the actual turn
proof is
\[
 0<c_R\le |W_j(s)|\le C_R
                  \qquad(|s|\le R,\ 0\le j<N),
 \tag{17}
\]
uniformly in \(N\). One may take
\(c_R=(\sin(\pi R)/(\pi R))^2\) and
\(C_R=(\sinh(\pi R)/(\pi R))^2\).
It follows by applying Euler's sine product to the distinct nonzero
integers \(r+kN\) in each factor of (1), and bounding that subset
product by the products over all nonzero integers.
Also, uniformly for \(0<|s|\le R\) and \(N\ge2\),
\[
                |\beta_s|\asymp_R |s|^2/N^2.
 \tag{18}
\]
For (18), the function \(\sin z/z\) is nonvanishing on
\(|z|\le\pi R/2<\pi/2\), so it and its inverse are bounded there.

For any coordinate \(\ell^p\) norm, \(1\le p\le\infty\), (5) gives
\[
 \left\|\left(
       \beta_s^{-1}O_{0,N}(s),\ldots,
       \beta_s^{-1}O_{d-1,N}(s),C_N(s)
              \right)\right\|_p
           \asymp_R \|u(s)\|_p .
 \tag{19}
\]
No factor growing with the dimension is hidden in this comparison:
it is diagonal multiplication by the bounded \(W_j\) and by one.
Thus the cost of undoing the common observation zero on this
microscopic disk is \(O_R(N^2/|s|^2)\). At completeness (8) has
the exact factor \(N^2/(8\pi^2)\); in the physical logarithmic
coordinate it has the constant factor in (9). The uniform disk
\(|s|\le R\) corresponds to \(|\log M|\le\pi R/N\), not a fixed
physical-meridian neighborhood as \(N\) grows.

The result applies coefficientwise in additional holomorphic boundary
parameters and to any fixed short component whose actual boundary
vector is represented in this chart. It recovers that vector, including
every original Hermite coordinate through the canonical polynomial.
It does not bound its size relative to the desired geometric action.

There are \(N\) observations and the largest Casimir insertion degree is
\(N-1\). Consequently the uniform derivative order two is not a fixed-size
observability certificate on a level-independent geometric module, nor
a finite coefficient-ideal identity for the original selected asymptotic.
The inserted observations (4) are additional source observations.
Nonzero values among them do not imply \(C_N(0)\ne0\), and do not
initialize a nonzero geometric component of the original state.
That requires the actual geometric quotient and its prescribed source
pairing, with the closing/current data preserved.

## 5. Direct written sources

- [Actual moving-meridian turn](actual_main_meridian_turn_comparison.md):
  equations (29), (34)--(35), the complete orientation normalization,
  and the uniform paired-product proof in §4. These supply the physical
  matrix and the bounds used here.
  SHA-256: 9a4e617838bbeebd640615cd3a6f0178486d60f1a3ee0c8b8f620dd31ed4ffec.
- [Actual meridian compiler](actual_main_meridian_newton_compiler.md):
  equations (5), (17)--(21) and §5. These supply the coefficient closing
  row, typed carrier, and the one primitive cut scalar.
  SHA-256: 567b13019bf0fb2a7120d4139b9da78ebc481dee8ad7af30e2722a20b9e6506f.

The new row identities, recovery formulas, Smith factors and determinant
are proved above. Only written reasoning and source-text reads were used;
no mathematical execution, numerical work, tests or compilation occurred.
