# Exact torus composition with the two ordinary ends summed

Research identity, 5 November 2026. Both private endpoint indices can
be summed into the original cap polynomials. For a word of length at
least two, the remaining source has only attached endpoint variables,
the old interior conditional kernels, and one explicit finite Gram
polynomial. All triangular supports, scalar factors and Fourier
aliases are retained. This identity does not assert a packet for the
new Gram polynomial or global dominance of the open-word contour.

## 1. Symmetric original matrices and the two caps

Fix \(N\ge2\), put \(q=e^{\pi i/N}\), \(r=q^{-2}\),
\(P_a=(r;r)_a\), and let \(\kappa\) be the original crossing scalar.
Use the original Newton evaluation vector \(v(w)\), the change of
basis \(b(w)=Sv(w)\), and the symmetric matrices from
[exact wire contraction](research_mixed_wire_exact_contraction.md):
\[
\begin{split}
 (B_{3+\epsilon})_{ab}
 &=\kappa^{1+\epsilon}N^\epsilon
       \frac{P_{a+b}}{(P_aP_b)^\epsilon}\,
                   \mathbf1_{\{a+b<N\}},\\
 \Gamma_{ab}
 &=\frac{r^{-ab}P_{a+b}}{P_a^2P_b^2}\,
                   \mathbf1_{\{a+b<N\}},\qquad \Gamma=SS^T .
\end{split}                                                   \tag{1}
\]
The products \(P_a,P_b\) have indices less than \(N\), so their
denominators do not vanish. Formula (1) never asks to divide by
\(P_{a+b}\) on the zero part of the support. All transposes here
are bilinear, without complex conjugation.

Let \(\mathcal H_N(w,Y)\) and \(\mathcal U_{\epsilon,N}(w,X)\)
be the original degree-less-than-\(N\) polynomials of
[open torus composition](research_mixed_conditional_torus_composition.md),
Corollary 3. At a physical index,
\[
 b_a(w)=\frac{\mathcal H_N(w,r^{-a})}{P_a},\qquad
 \mathcal U_{\epsilon,N}(w,X)
 =\sum_{a=0}^{N-1}
     \frac{\mathcal H_N(w,r^{-a})p_a(X)}{P_a^{1+\epsilon}},
 \quad p_a(X)=(rX;r)_a.
                                                               \tag{2}
\]
Both equalities retain the entire ordinary boundary polynomial.
The exact first-cap contraction is
\[
 \sum_a b_a(w)(B_{3+\epsilon})_{aj}
 =\kappa^{1+\epsilon}N^\epsilon
                  P_j^{1-\epsilon}\mathcal U_{\epsilon,N}(w,r^j).
                                                               \tag{3}
\]
It follows directly from \(P_{a+j}=P_jp_a(r^j)\) on the
surviving triangle; \(p_a(r^j)=0\) on its complement.
By symmetry of \(B_{3+\epsilon}\), the same formula holds
with \(b(w)\) on the right. In particular the right cap is
\(\mathcal U_{\epsilon,N}(w,Y)\), not a conjugated cap or a
cap evaluated at \(Y^{-1}\).

## 2. One global polynomial for the remaining Gram pair

Define the normalized physical Gram entries
\[
 K_N(a,b)=P_aP_b\Gamma_{ab}
 =\begin{cases}
 r^{-ab}P_{a+b}/(P_aP_b),&a+b<N,\\
 0,&a+b\ge N.
 \end{cases}                                                \tag{4}
\]
Their exact global representative is
\[
 \boxed{\displaystyle
 \mathcal G_N(X,Y)=
   \sum_{\ell=0}^{N-1}
     \frac{r^\ell(X^{-1};r)_\ell(Y^{-1};r)_\ell}{P_\ell^2}.}
                                                               \tag{5}
\]
It is symmetric and has separate Laurent bands
\[
          \deg_X\mathcal G_N,\deg_Y\mathcal G_N
                                  \subset[-N+1,0].          \tag{6}
\]

**Lemma 1.** For every \(0\le a,b<N\),
\[
                         \mathcal G_N(r^a,r^b)=K_N(a,b).
                                                               \tag{7}
\]
In particular (5) has the exact triangular zeros in (4).
It is the unique interpolant of these \(N^2\) values with the
two bands (6).

*Proof.* Write
\(S_a=\prod_{j=1}^a2\sin(\pi j/N)\) and
\(\Delta_a=i^a q^{-a(a+1)/2}\), with empty product \(S_0=1\).
Here \(S_a\) is a scalar sine factorial, distinct from the matrix \(S\).
The original change of basis has entries
\[
 S_{a\ell}=\frac{\Delta_a^{-1}q^{a\ell}}
                        {S_\ell S_{a-\ell}}\quad(\ell\le a),
 \qquad P_a=\Delta_aS_a,
\]
and zero entries for \(\ell>a\). Its normalized column is
\[
\begin{split}
 P_aS_{a\ell}
 &=q^{a\ell}\frac{S_a}{S_\ell S_{a-\ell}}\\
 &=\frac{q^{-\ell^2}}{P_\ell}
       \prod_{j=0}^{\ell-1}(X^{-1}-r^{-j})
                   \quad\text{at }X=r^a.
\end{split}                                                   \tag{8}
\]
For \(\ell>a\), the displayed product is exactly zero, so
(8) applies to all \(\ell<N\). To verify the second equality
for \(\ell\le a\), use
\(\Delta_a/(\Delta_\ell\Delta_{a-\ell})=q^{-\ell(a-\ell)}\)
and
\[
 \prod_{j=0}^{\ell-1}(X^{-1}-r^{-j})
       =r^{-a\ell}P_a/P_{a-\ell}\quad(X=r^a).
\]
Multiplying the two normalized columns in
\(\operatorname{diag}(P)\Gamma\operatorname{diag}(P)
=(\operatorname{diag}(P)S)(\operatorname{diag}(P)S)^T\)
gives (5), since
\[
 \prod_{j=0}^{\ell-1}(X^{-1}-r^{-j})
 =(-1)^\ell r^{-\ell(\ell-1)/2}(X^{-1};r)_\ell,
 \qquad q^{-2\ell^2}r^{-\ell(\ell-1)}=r^\ell .
                                                               \tag{9}
\]
Thus (7) follows from the original finite Gram identity.
The two finite Fourier matrices in the bands (6) are invertible,
which proves uniqueness. Equivalently, the terminating
q-Chu--Vandermonde identity at \(X=r^a\) sums (5) to
\(r^{-ab}(r^{b+1};r)_a/P_a\); it gives the same exact zero
when \(a+b\ge N\). \(\square\)

Formula (5) specifies the whole off-grid finite function. Agreement
in (7) is not an identification with the canonical factorial
continuation of \(r^{-ab}P_{a+b}/(P_aP_b)\). Nor is (5) the
ordinary-color bare kernel \(\sum_\ell e_\ell(w)e_\ell(w')\)
in the [bare-kernel packet theorem](research_bare_kernel_thin_rectangle.md).
The latter uses a different evaluation basis and different variables.
Its packet cannot be imported for (5) without an additional identity
and the required source bounds.

## 3. The exact finite contraction for every length at least two

Let \(m\ge2\), \(n_j=3+\epsilon_j\), and \(k=\sum_j\epsilon_j\).
Use the remaining leg indices
\[
 a_1=t_1,\ldots,a_{m-1}=t_{m-1},\qquad a_m=s_m,
 \qquad X_j=r^{a_j}.                                      \tag{10}
\]
The notation in (10) denotes the original discrete leg positions;
after rescaling their critical coordinates are the corresponding
attached legs. In particular neither remaining endpoint variable
is a private endpoint.

**Theorem 2.** The entire original ordinary boundary polynomial is
\[
\begin{split}
 &v(w_L)^TA_{n_1}\cdots A_{n_m}v(w_R)\\
 &\quad=\kappa^{m+k}N^k
  \sum_{a_1,\ldots,a_m=0}^{N-1}
  \mathcal U_{\epsilon_1,N}(w_L,X_1)
  \left[\prod_{j=2}^{m-1}C_{\epsilon_j,N}(X_{j-1},X_j)\right]\\
 &\hspace{34mm}\times
  K_N(a_{m-1},a_m)\,
  \mathcal U_{\epsilon_m,N}(w_R,X_m)
                  \prod_{j=1}^m P_{a_j}^{-\epsilon_j}.
\end{split}                                                   \tag{11}
\]
For \(m=2\) the conditional product is empty; the two caps
are joined by precisely one original normalized Gram pair.

*Proof.* Start with the exact scalar
\(b_L^TB_{n_1}\Gamma B_{n_2}\cdots\Gamma B_{n_m}b_R\).
Apply (3) at the two ends. For each internal vertex use the
unchanged conditional identity
\[
 \sum_i\Gamma_{hi}
       \frac{(B_{3+\epsilon})_{ij}}
            {\kappa^{1+\epsilon}N^\epsilon}
       =\frac{P_j^{1-\epsilon}}{P_h}
                               C_{\epsilon,N}(r^h,r^j).
                                                               \tag{12}
\]
This sums exactly its two triangular supports. The remaining
factorials telescope to
\[
 \left[\prod_{j=1}^{m-2}P_{a_j}^{-\epsilon_j}\right]
 P_{a_{m-1}}^{1-\epsilon_{m-1}}\,
 \Gamma_{a_{m-1},a_m}\,P_{a_m}^{1-\epsilon_m}
 =K_N(a_{m-1},a_m)\prod_{j=1}^mP_{a_j}^{-\epsilon_j}.
                                                               \tag{13}
\]
Each original block contributes its one factor
\(\kappa^{1+\epsilon_j}N^{\epsilon_j}\). This proves the
scalar and all factors of (11), including the empty-product case.
No additional shared boundary has been inserted. \(\square\)

## 4. Arbitrary radii and every Fourier alias

Let \(d_N\) be the original polynomial of degree less than \(N\)
with \(d_N(r^a)=P_a^{-1}\). For arbitrary positive radii, (11)
is exactly
\[
\begin{split}
 &\kappa^{m+k}N^{m+k}
 \oint\cdots\oint
 \mathcal U_{\epsilon_1,N}(w_L,X_1)
 \left[\prod_{j=2}^{m-1}C_{\epsilon_j,N}(X_{j-1},X_j)\right]\\
 &\qquad\times
 \mathcal G_N(X_{m-1},X_m)
 \mathcal U_{\epsilon_m,N}(w_R,X_m)
 \prod_{j=1}^m\{d_N(X_j)(1+X_j^{-N})\}^{\epsilon_j}
                           \prod_{j=1}^m\frac{dX_j}{2\pi iX_j}.
\end{split}                                                   \tag{14}
\]
All circles are counterclockwise.

To see this, the unweighted band in each variable is contained in
\([-N+1,N-1]\). At the left end this pairs the nonnegative
cap band with the first negative conditional band, or with the
negative Gram band if \(m=2\). At the right end it pairs the
nonnegative cap with the second negative Gram band. The variable
\(X_{m-1}\) pairs the last positive conditional band with the
first negative Gram band. All other variables have the old
conditional positive/negative pair.

An unweighted root average therefore selects only the zero
frequency. Multiplication by \(d_N\) enlarges the band to
\([-N+1,2N-2]\); its only possible multiples of \(N\) are
zero and \(N\). Hence the original root sum equals \(N\)
times the constant term after multiplication by
\(1+X^{-N}\) at precisely the four-type variables. Performing
these \(m\) exact averages proves (14). There are no extra
aliases at either new cap. Laurent-polynomial holomorphy on
\((\mathbb C^\times)^m\) proves radius independence and legal
simultaneous radial deformation before any asymptotic estimate.

All identities are identities of the whole ordinary boundary
polynomial. Differentiating in \(w_L,w_R\) retains every original
ordinary jet and both level parities. If signed jet polynomials
defined using \(E_{\ell,a}=(-1)^ae_\ell^{(a)}(-2)\) are used
instead, the common factor is \((-1)^{a+b}\), exactly as in
the one-cap identity.

## 5. One vertex and the remaining source obligation

A one-vertex word has only one matrix \(B_{3+\epsilon}\).
Applying (3) twice would use this matrix twice and is not an
identity. Its correct existing formula remains
\[
 \kappa^{1+\epsilon}N^{1+\epsilon}
 \oint \mathcal U_{\epsilon,N}(w_L,X)
       \mathcal H_N(w_R,X^{-1})
       \{d_N(X)(1+X^{-N})\}^{\epsilon}
                                \frac{dX}{2\pi iX}.
                                                               \tag{15}
\]
One may exchange the left and right ordinary colors by the symmetry
of the original single block. Formula (15) does not become a
product of two cap polynomials.

For \(m\ge2\), (14) removes the former conditional kernel with
a private \(E\)-valued outgoing argument: both private indices
are already inside the original caps. The remaining endpoint
variables have the certified attached ranges of their types.
The price is explicit: the new closing factor is the whole
finite polynomial (5), not a formal factorial ratio. Its
local packet and all its complementary rows or currents, and
the remaining open-word contour comparison, still need proof.
No global dominance or nonzero open-word coefficient is inferred
from the exact identity alone.

## 6. Exact finite checks

The focused checker compares the two physical and torus expressions
with the literal original crossing matrices in exact
\(\mathbb Q(i,\sqrt2,\sqrt3)\) arithmetic at \(N=2,3,4,6\).
It checks every coefficient in both original boundary bases, all
words of lengths one through three, and both alternating words of
length four. It separately checks the normalized columns, Gram
support and Fourier alias signs. These finite checks guard the
normalizations; the proofs above establish the identities for
arbitrary levels and lengths.

    python3 experiments/check_mixed_two_cap_torus_composition.py
    python3 experiments/check_mixed_two_cap_torus_composition.py --input repro/results/research-mixed-two-cap-torus-composition.json --output /tmp/research-mixed-two-cap-torus-composition-review.json
