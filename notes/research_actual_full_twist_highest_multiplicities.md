# The actual full twist on every highest multiplicity

Private written proof, 19 November 2026.

This note computes the normalized physical full twist directly from the
finite crossing matrices. It uses neither a ribbon-element formula nor
a scalar assertion inferred from braid centrality. The block crossings,
their root cutoffs, and the action on each multiplicity vector are
explicit. The reflected-meridian specialization is the one needed for
the complementary Gauss fusion.

The two complete directs are R, the actual reduced braid source, and
E, its finite Euler crossing factor. Their pins are at the end. All
representation decompositions and block-braid calculations used here
are proved below.

## 1. The finite statement and its scope

Fix
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad
 f_n=(Q;Q)_n,\quad x=-\mathsf M/q.
 \tag{1}
\]
The nonzero physical meridian in this section is \(\mathsf M\).
The fusion application has \(r\ge2\); one head supplies the induction
base. On one head,
\[
 Kw_a=xQ^{-a}w_a,\qquad
 Fw_a=(1-Q^{a+1})w_{a+1},\qquad
 Ew_a=(\mathsf M Q^{-a}-\mathsf M^{-1})w_{a-1}.
 \tag{2}
\]
The two endpoint arrows are zero. Totals are ordered by
\[
 K_{AB}=K_AK_B,\quad E_{AB}=E_AK_B+E_B,\quad
 F_{AB}=F_A+K_A^{-1}F_B.
 \tag{3}
\]
The integer physical degree is the sum of the original head indices.
It is not reduced modulo \(N\).

Let \(R_i=\kappa(\mathsf M)R_{i,0}\) be the actual positive checked
crossing. Thus
\[
 R_{i,0}=\mathsf P_iD_i\Theta(E_iF_{i+1}),\qquad
 D_i(a,b)=x^{-a-b}Q^{ab},
\quad
 \Theta(Z)=\sum_{n=0}^{d}
             \frac{(-1)^nq^{n^2}}{f_n}Z^n.
 \tag{4}
\]
Every matrix in (2)--(4) is at the fixed root \(Q\); only \(\mathsf M\)
varies. R proves that these are the actual braid and total-intertwiner
matrices throughout this family. E gives the literal finite factor (4).

Write
\[
 \Delta_r=(\sigma_1\cdots\sigma_{r-1})
                 (\sigma_1\cdots\sigma_{r-2})\cdots\sigma_1,
\quad
 Z_r=\kappa(\mathsf M)^{-r(r-1)}B(\Delta_r^2).
 \tag{5}
\]
Products of matrices act from right to left. A generic value of
\(\mathsf M\) means one outside the finite exceptional set specified
by the lowering products and Casimir differences in Section 3.

**Theorem.** At a generic \(\mathsf M\), the full \(r\)-head module is
a direct sum of \(N\)-dimensional highest strings. Their exact integer
highest degrees \(j\) have multiplicities
\[
 \sum_j m_r(j)z^j=(1+z+\cdots+z^d)^{r-1}.
 \tag{6}
\]
On every vector in every string of highest degree \(j\), including
every multiplicity copy, the actual matrix (5) acts by
\[
                 Z_r=x^{-2rj}Q^{j(j-1)}I.
 \tag{7}
\]
Consequently, at the reflected meridian \(\mathsf M=M^{-1}\),
\[
                 Z_{r,-}=M^{2rj}Q^{j(j+r-1)}I.
 \tag{8}
\]
For \(r\ge2\) and a physical degree \(0\le T\le d\), precisely \(0\le j\le T\)
occur in that degree. For larger degrees, the condition is
\(j\le T\le j+d\); (6)--(8) still apply with the exact integer \(j\).
Labels differing by \(N\) are not identified.

In particular, after reflection, the ratio of (8) at \(j+N\) and
\(j\) is \(M^{2rN}\). Its logarithmic-meridian derivative at \(M=1\)
is \(2rN\), even though the two generic total Casimir values agree.
Thus the full tensor product, or a sum of physical degree blocks
containing both strings, does not permit replacement of the full twist
by an unmarked function of the total Casimir alone. A single fixed
degree \(T\) has \(j\in[T-d,T]\), so it contains no such pair.
The fusion application in Section 6 stays at \(T\le d\), which is the
range of the separately evaluated Gauss product.

The generic splitting is a proof device. Every consequent equality
between the original finite matrices, after its displayed scalar
denominators are cleared, extends through all meridian collisions
by analyticity. This continuation retains the full Jordan and meridian
normal data. It does not assert that the generic projectors extend
separately.

## 2. Exact block crossings without a root carry

Let A consist of \(s\) consecutive physical heads and let B be one
head. On physical degrees \(a,b\), set
\[
 D_{A,B}(a,b)=x^{-a-sb}Q^{ab},\qquad
 D_{B,A}(b,a)=x^{-sb-a}Q^{ab}.
 \tag{9}
\]
The positive braid moving A to the right of B, with its \(s\) copies
of \(\kappa\) removed, is exactly
\[
 \mathcal R_{A,B}
       =\mathsf P_{A,B}D_{A,B}\Theta(E_AF_B).
 \tag{10}
\]
The positive return braid is
\[
 \mathcal R_{B,A}
       =\mathsf P_{B,A}D_{B,A}\Theta(E_BF_A).
 \tag{11}
\]
Here the flips exchange whole ordered blocks; they do not reverse
the order inside A.

We prove these identities from (4). If \(XY=QYX\), the finite
Gaussian-binomial identity gives, for \(n<N\),
\[
 (X+Y)^n=\sum_{a+b=n}
       Q^{-ab}\frac{f_n}{f_af_b}X^aY^b.
 \tag{12}
\]
It follows directly, since \(q^{(a+b)^2}Q^{-ab}=q^{a^2+b^2}\),
that
\[
                    \Theta(X+Y)=\Theta(X)\Theta(Y)
 \tag{13}
\]
provided every product of total degree at least \(N\) on the right
vanishes. Formula (12) itself follows by multiplication by \(X+Y\)
and the elementary Gaussian-binomial recursion; no infinite
root-of-unity series is involved.

For three ordered blocks in which C is one head, remove the final
block permutation from the two successive physical crossings. The
uncheck product is \(R_{AC,0}^{\rm un}R_{BC,0}^{\rm un}\). The Cartan
conjugations give
\[
 \begin{split}
 D_{AC}\Theta(E_AF_C)D_{BC}\Theta(E_BF_C)
  &=D_{AC}D_{BC}
       \Theta(E_AK_BF_C)\Theta(E_BF_C)\\
  &=D_{AB,C}\Theta((E_AK_B+E_B)F_C).
 \end{split} \tag{14}
\]
Indeed \(K_BE_B=QE_BK_B\), so the two arguments in the first
line satisfy \(XY=QYX\). Every term of total degree at least \(N\)
contains \(F_C^N=0\). The diagonal products in (14) are exactly
(9), with the full physical degrees, including any highest-degree
offsets. Induction proves (10).

For a single first head A and an ordered block BC, the analogous
uncheck order is \(R_{AC,0}^{\rm un}R_{AB,0}^{\rm un}\). This time
\[
 \begin{split}
 D_{AC}\Theta(E_AF_C)D_{AB}\Theta(E_AF_B)
  &=D_{AC}D_{AB}
       \Theta(E_AK_B^{-1}F_C)\Theta(E_AF_B)\\
  &=D_{A,BC}\Theta(E_A(F_B+K_B^{-1}F_C)).
 \end{split} \tag{15}
\]
Here \(K_B^{-1}F_B=QF_BK_B^{-1}\), and every omitted total
degree would contain \(E_A^N=0\). This proves (11).

For clarity, the Cartan conjugations used above follow immediately
from degree shifts:
\[
 D_{A,B}E_AD_{A,B}^{-1}=E_AK_B,\qquad
 D_{A,B}F_BD_{A,B}^{-1}=K_A^{-1}F_B.
 \tag{16}
\]
Thus (14)--(15) are literal finite identities. They do not specialize
an infinite generic-\(q\) factorization while dropping its root carry.
The shared single head is precisely what kills that carry here.

In particular (10)--(11) preserve the tensor product of any fixed
highest string in A with B, up to the displayed block flip. They
depend on that string only through its total \(E,F,K\) and its
physical degree. No basis or projector on its multiplicity space
has been inserted.

## 3. Generic highest strings, including their multiplicities

We record the necessary finite representation facts explicitly.
For a highest vector \(h\) with \(Kh=kh\), \(Eh=0\), define
\[
 v_a=\frac{F^a}{f_a}h,\quad 0\le a<N,\qquad
 \alpha_a(k)=-q^{-1}(kQ^{1-a}-k^{-1}).
 \tag{17}
\]
The head relations in (2), and then (3), give
\[
 Kv_a=kQ^{-a}v_a,\quad
 Fv_a=(1-Q^{a+1})v_{a+1},\quad
 Ev_a=\alpha_a(k)v_{a-1}\quad(a\ge1).
 \tag{18}
\]
For example commuting \(E\) through \(F^a\) gives
\[
 EF^ah=-q^{-1}(1-Q^a)(kQ^{1-a}-k^{-1})F^{a-1}h,
 \tag{19}
\]
which proves the last formula upon dividing by \(f_a\).
These commutations can also be checked inductively using
\([E,F]=(q-q^{-1})(K-K^{-1})\), which follows from (2).
The total \(E^N\) and \(F^N\) are zero: the summands in (3)
\(Q\)-commute, the intermediate Gaussian-binomial coefficients
at degree \(N\) vanish, and each one-head \(N\)-th power is zero.

If all \(\alpha_a(k)\), \(1\le a<N\), are nonzero, the \(N\)
vectors in (17) are nonzero and independent. Nonzero follows by
applying \(E^a\), and their distinct \(K\) weights give independence.
They form a simple string: any invariant subspace contains a weight
vector, and the nonzero adjacent arrows in (18) reach every weight.

Suppose A already contains such a string, with highest degree
\(j_0\) and \(k=x^sQ^{-j_0}\). Tensor it with one physical head.
For every \(0\le l<N\), there is a unique highest vector in the
degree-\(l\) subspace of these two strings whose \(v_0\otimes w_l\)
coefficient is one:
\[
 h_l=\sum_{a=0}^l b_a v_a\otimes w_{l-a},\quad b_0=1,
\quad
 \frac{b_{a+1}}{b_a}
 =-\frac{\alpha_{l-a}(x)}
          {\alpha_{a+1}(k)xQ^{-(l-a-1)}}.
 \tag{20}
\]
This is exactly the \(E_AK_B+E_B\) equation coefficient by
coefficient. Its highest \(K\) weight is \(kxQ^{-l}\).

The operator
\[
                         \Omega=FE+qK+q^{-1}K^{-1}
 \tag{21}
\]
commutes with \(E,F,K\), by the same head relations. On the string
generated by \(h_l\), it has scalar
\[
                  \lambda_l=qkxQ^{-l}+q^{-1}(kx)^{-1}Q^l.
 \tag{22}
\]
For generic \(x\), these \(N\) scalars are distinct and all new
lowering coefficients are nonzero. Each generated string has
dimension \(N\); their distinct Casimir scalars make their sum
direct, and their total dimension is \(N^2\). They therefore fill
the tensor product of the chosen prefix string with the head.

Induction from one head proves the decomposition in the theorem.
Each prefix copy contributes one copy for each \(l=0,\ldots,d\),
so the highest-degree generating polynomial is multiplied by
\(1+z+\cdots+z^d\) at each step, proving (6). Only finitely many
products and differences in (17),(22) occur at fixed \(r,N\);
their vanishing is the stated finite exceptional set.

This construction does not assume distinct final Casimirs for all
integer \(j\). Such distinctness would be false for \(j\) and \(j+N\).
The direct sum is instead constructed one prefix copy at a time.
The calculation below acts on each of those actual copies.

## 4. The block monodromy on an arbitrary highest vector

Keep a particular prefix vector \(h\), without any choice or
restriction on its multiplicity label. Put
\[
                    H_l(k)=\prod_{a=1}^l\alpha_a(k).
 \tag{23}
\]
Equation (20) gives its extreme coefficient
\[
 b_l=(-1)^l x^{-l}Q^{l(l-1)/2}\frac{H_l(x)}{H_l(k)}.
 \tag{24}
\]
In the reversed tensor order, normalize the highest vector by its
\(w_0\otimes v_l\) coefficient one. The identical calculation,
now with highest weights \(x,k\), gives its last coefficient
\[
 \widetilde b_l=(-1)^l k^{-l}Q^{l(l-1)/2}
                                      \frac{H_l(k)}{H_l(x)}.
 \tag{25}
\]

In (10), the coefficient at \(w_0\otimes v_l\) can come only
from \(v_l\otimes w_0\) with Euler transfer zero. All positive
transfers raise the B occupation. Its Cartan coefficient is
\(x^{-j_0-l}\). Thus (10) takes \(h_l\) to the reversed
normalized highest vector times
\[
                           b_l x^{-j_0-l}.
 \tag{26}
\]
The intertwiner property ensures that it is a highest vector;
uniqueness in this fixed pair of strings makes this a vector
identity, not merely an extreme-entry comparison.

For the return (11), the coefficient at \(v_0\otimes w_l\)
similarly has only zero transfer from \(w_l\otimes v_0\).
Its diagonal factor is \(x^{-sl-j_0}Q^{lj_0}\).
Consequently the double-block braid has scalar
\[
 \begin{split}
 \mu_{s,1}(j_0,l)
 &=b_l\widetilde b_l\,x^{-2j_0-(s+1)l}Q^{lj_0}\\
 &=x^{-2j_0-2(s+1)l}Q^{l(l-1)+2j_0l}.
 \end{split} \tag{27}
\]
In the second line \(k=x^sQ^{-j_0}\) has been substituted.
Every lowering product has canceled. Because the double-block
braid commutes with the total \(F\), it has this same scalar on
all descendants of \(h_l\).

This proof applies separately to every prefix multiplicity vector.
In particular it rules out a hidden action on the multiplicity
space; centrality of the full braid alone would not do that.

## 5. Full-twist induction and analytic continuation

Let \(s=r-1\). The two block braids in (10)--(11) have words
\[
 \beta_{\rm f}=\sigma_1\cdots\sigma_s,\qquad
 \beta_{\rm b}=\sigma_s\cdots\sigma_1.
 \tag{28}
\]
The elementary half-twist identities are
\[
       \Delta_r=\beta_{\rm f}\Delta_s
                =\Delta_s\beta_{\rm b}.
 \tag{29}
\]
The first is the definition (5); the second follows by induction,
commuting the new outer generator past the nonadjacent generators
and using \(\sigma_i\sigma_{i+1}\sigma_i
=\sigma_{i+1}\sigma_i\sigma_{i+1}\) at the remaining adjacent
triple. Thus
\[
        B_0(\Delta_r^2)
          =B_0(\Delta_s)\,
             (\mathcal R_{B,A}\mathcal R_{A,B})\,
             B_0(\Delta_s),
 \tag{30}
\]
where \(B_0\) uses the stripped crossings.
The middle operator commutes with the internal prefix braid:
this follows directly from (10)--(11), since that braid preserves
physical degree and commutes with the prefix totals. Hence (30)
is its product with \(B_0(\Delta_s^2)\).

Assume (7) for the prefix. On the descendant of the arbitrary
\(h_l\) in Section 4, the product in (30) is
\[
 \begin{split}
 &x^{-2s j_0}Q^{j_0(j_0-1)}
       x^{-2j_0-2r l}Q^{l(l-1)+2j_0l}\\
 &\hspace{25mm}=x^{-2r(j_0+l)}
                         Q^{(j_0+l)(j_0+l-1)}.
 \end{split} \tag{31}
\]
The one-head base is the identity. Equations (6),(31) prove the
theorem on the entire generic tensor product, with its
multiplicities and all original endpoints.

Finally \(x=-M^{-1}/q\) makes
\(x^{-2rj}=M^{2rj}Q^{rj}\), proving (8). The scalar
\(\kappa^{-r(r-1)}\) is exactly the number of positive crossings
in (5); no extra framing character is introduced.

All entries used above are finite Laurent-rational functions of
\(\mathsf M\), with the only fixed factorial denominators \(f_n\),
\(n<N\). If an equality assembled from these matrices is verified
using the generic splitting, multiplying its remaining scalar
denominators makes it an equality of analytic finite matrices on
an open set. It then holds identically and has the original
removable continuation wherever the unmultiplied expression has
one. This argument retains every derivative and generalized root
block. It is the appropriate use of (8) in whole-meridian fusion;
no root semisimple spectral substitution is required.

## 6. The exact fusion interface, without an additional premise

Here is the immediate cancellation supplied to the complementary
Gauss calculation. Suppose its literal two factors on degree
\(T\le d\) have, on each generic highest string \(j\le T\), the
already evaluated product
\[
 a_jb_j=
 M^{2r(T-j)}Q^{(T-j)(T+j+r-1)}\,\mathcal D_{r,T}(M),
\quad
 \mathcal D_{r,T}=
 \frac{(M^2Q;Q)_d(1-M^{-2(r+1)N})}
      {1-M^{-2(r+1)}Q^{-2T-r}}.
 \tag{32}
\]
This section does not re-prove the separate Gauss evaluation.
Multiplication by the actual full twist (8), with its reflected
meridian and every multiplicity fixed as above, gives exactly
\[
 A_-B_+Z_{r,-}
   =M^{2rT}Q^{T(T+r-1)}\mathcal D_{r,T}(M)\,I.
 \tag{33}
\]
Indeed \((T-j)(T+j+r-1)+j(j+r-1)=T(T+r-1)\).
The quotient in (32) has the finite interpretation
\[
 \frac{1-M^{-2(r+1)N}}{1-M^{-2(r+1)}Q^{-2T-r}}
    =\sum_{a=0}^{N-1}
          M^{-2(r+1)a}Q^{-(2T+r)a},
 \tag{34}
\]
since \(Q^{N(2T+r)}=1\). Thus its apparent poles are removable.
When (32) is proved from the original Gauss matrices, (33) is
a whole-meridian matrix identity by Section 5, including all
normal and Jordan data. Formula (33) is not used as an assumption
in the full-twist theorem.

The conclusion is exact finite source algebra. It supplies no
coherent-kernel bound, relative-window estimate, selected
geometric branch, or closed-source noncancellation.

## Complete proof-source pins

* R: notes/research_actual_reduced_braid_source.md, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243
  (330 lines).
* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256
  9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16
  (410 lines).

Both complete directs were freshly read nontruncated in this author
sequence, and every used implication checked. The initial truncated
E read was recovered by the full covering reads 1--190 and
191--end. The full-twist proof is the finite calculation above;
half-ribbon terminology from the literature was coverage only.
Only written mathematics and text operations were used. Frozen
and public files are unchanged.
