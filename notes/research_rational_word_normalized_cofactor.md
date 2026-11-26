# An exactly normalized determinant for a rational-word source

Research note, 3 November 2026.

The original boundary state of every fixed rational word has an
exact cofactor representation with a known normalization. Its
matrix has bandwidth bounded independently of the quantum level.
The formula includes the nonsemisimple endpoint and every first
normal. It does not require generic nullity, a favorable spectral
color, or an unspecified choice of source scale.

The resulting adjugate is positive after the prescribed reversal,
but the matrix whose cofactor is taken is generally indefinite.
The theorem is a finite source identity. It does not estimate that
determinant's exponential growth.

The earlier [pointed cofactor construction](root_orbit_pointing.md)
explains how an annihilator and source pointing can recover a
period. Here the original rational-word algebra fixes the rank and
the normalization directly. The original matrices and their adjoints
are those in [the Newton metric note](actual_newton_turn_positive_gram.md).
The fixed-band representation uses the known quantum trace algebra,
in its [full physical-angle realization](research_current_free_aw_crossing_transport.md).

## 1. The original word and its cap operator

Put \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\),
\(\eta=(-1)^D\), and \(c_j=2\cos((2j+1)\pi/N)\).
Use the original normalized Newton basis \(e_0,\ldots,e_D\);
its Frobenius pairing matrix is the reversal
\[
                 J_{ij}=\mathbf1_{i+j=D}.
 \tag{1}
\]
To distinguish polynomials from coordinate vectors, write
\(\mathbf e_j\) for the \(j\)-th coordinate column.
Multiplication by \(z\) and its turned operator are
\[
 Z_{jj}=c_j,\qquad
 Z_{j+1,j}=-4\sin^2((j+1)\pi/N),\qquad
                         L=JZJ=Z^T.
 \tag{2}
\]
Let \(M\) be multiplication by the original crossing \(R\),
with its actual scalar \(\kappa=q^{D^2/2}\).
Take any fixed word \(W_N\) in \(J\) and the signed powers
\(M^n\). No restriction on the intermediate rational pieces
is imposed. Define
\[
 f_N=W_N\mathbf e_0,\qquad
 F_N(z)=v_N(z)^T f_N,\qquad
 v_N(z)=(e_0(z),\ldots,e_D(z))^T,
 \tag{3}
\]
and
\[
                 D_{W,N}=W_N(L-c_0I)W_N^{-1}.
 \tag{4}
\]
The symbol \(D_{W,N}\) denotes a matrix, not the integer \(D\).
It retains the full original quotient
\(\mathbb C[z]/(2T_N(z/2)+2)\).

## 2. The normalized adjugate

**Theorem 1.** For every word and every level,
\[
 \boxed{\displaystyle
            \operatorname{adj}(D_{W,N})J
                             =N^2 f_N f_N^\dagger.}
 \tag{5}
\]
In particular \(D_{W,N}\) has rank \(N-1\), and its adjugate
does not vanish at the repeated endpoint eigenvalue.

*Proof.* The matrix \(L-c_0I\) is upper bidiagonal. Its
diagonal vanishes at indices \(0,D\), and nowhere else.
Every superdiagonal entry is nonzero. Its kernel is
\(\mathbb C\mathbf e_0\), and its left kernel is
\(\mathbb C\mathbf e_D^T\). Thus its adjugate is a scalar
multiple of \(\mathbf e_0\mathbf e_D^T\).
The complementary triangular minor gives that scalar:
\[
 \operatorname{adj}(L-c_0I)
    =\left(\prod_{r=1}^{N-1}4\sin^2(r\pi/N)\right)
                         \mathbf e_0\mathbf e_D^T
    =N^2\mathbf e_0\mathbf e_D^T.
 \tag{6}
\]
The product follows from
\(\prod_{r=1}^{N-1}(1-e^{2\pi ir/N})=N\), followed by
absolute squares. The signs from the superdiagonal and
the cofactor cancel.

Every original multiplication coupon is self-adjoint for
the bilinear Frobenius pairing. Also \(R^\sharp=R^{-1}\),
where sharp conjugates its polynomial coefficients.
Since the Newton basis is real,
\[
                         M^\dagger=JM^{-1}J.
 \tag{7}
\]
The same identity holds for \(J\). It is stable under
products, so
\[
             W_N^\dagger J W_N=J,\qquad
             W_N^{-1}=J W_N^\dagger J.
 \tag{8}
\]
These statements retain the nilpotent parts; they are not
identities just on distinct spectral values.

Adjugates commute with similarity, including for singular
matrices. Apply (6) and (8):
\[
 \begin{split}
 \operatorname{adj}(D_{W,N})J
  &=N^2 W_N\mathbf e_0\mathbf e_D^T W_N^{-1}J\\
  &=N^2 W_N\mathbf e_0\mathbf e_0^T W_N^\dagger
    =N^2 f_N f_N^\dagger.
 \end{split}
 \tag{9}
\]
This proves the formula and rank assertion. \(\square\)

The endpoint has not become semisimple. Indeed
\(\mathbf e_0^\dagger J\mathbf e_0=0\), and hence
\[
                          f_N^\dagger J f_N=0.
 \tag{10}
\]
This is consistent with the double zero eigenvalue and its
one-dimensional eigenspace.

## 3. Full boundary evaluation and the original closing functional

Equation (5) gives a polarized polynomial identity:
\[
 \boxed{\displaystyle
 F_N(z)F_N^\sharp(w)
     =\frac1{N^2}v_N(z)^T
                 \operatorname{adj}(D_{W,N})Jv_N(w).}
 \tag{11}
\]
It is an ordinary identity in the two free variables, not a
reduction modulo their physical relations. It therefore
retains all their mixed derivatives. In particular, for
any complex boundary value \(c\),
\[
 |F_N(c)|^2=\frac1{N^2}v_N(c)^T
              \operatorname{adj}(D_{W,N})J\overline{v_N(c)}.
 \tag{12}
\]
The rank-one determinant lemma, valid also for singular
matrices, turns this into
\[
 \boxed{\displaystyle
 \det\!\left(D_{W,N}
       +J\overline{v_N(c)}\,v_N(c)^T\right)
                         =N^2|F_N(c)|^2.}
 \tag{13}
\]
Thus the boundary update is fixed by the actual evaluation,
not by a choice of an adjugate column. Equivalently
\(JD_{W,N}\) is Hermitian, and
\[
 \det\!\left(JD_{W,N}
       +\overline{v_N(c)}\,v_N(c)^T\right)
                   =\det(J)\,N^2|F_N(c)|^2.
 \tag{14}
\]
The update in (14) is positive semidefinite. The unperturbed
Hermitian matrix need not be positive.

For the original closing functional
\(\phi_N(F_N)=\mathbf e_D^T f_N\), the dense boundary vector
disappears. From the corresponding cofactor in (5),
\[
 \boxed{\displaystyle
 N^2|\phi_N(F_N)|^2
    =\det(D_{W,N}+\mathbf e_0\mathbf e_D^T)
    =(-1)^D
      \det D_{W,N}[\{1,\ldots,D\},\{0,\ldots,D-1\}].}
 \tag{15}
\]
This includes zero sources: no division by the closing
scalar has been made. Whenever the original strand closure
defines a knot, the source-to-invariant normalization from
the original compiler applies to the same scalar. Any
remaining writhe unit has modulus one and leaves (15)
unchanged.

One further identity records the source norm without
selecting a boundary value. Since the adjugate of a
rank-\(N-1\) matrix has its single nonzero singular value
equal to the product of the matrix's nonzero singular values,
\[
        \prod_{j=1}^{N-1}s_j(D_{W,N})
                            =N^2\|f_N\|_2^2.
 \tag{16}
\]
This is a norm statement, distinct from the boundary period
in (12) or (15).

## 4. Fixed bandwidth, without a dense crossing conjugation

Although (4) defines the normalization conveniently, it is
not necessary to form its dense crossing matrices.
Put \(L_1=M^{-1}LM\). The exact quantum trace identities give
\[
 \begin{array}{lll}
 JZJ=L,&JLJ=Z,&JL_1J=L_{-1},\\
 M^{-n}ZM^n=Z,&M^{-n}LM^n=L_n,&
 M^{-n}L_1M^n=L_{n+1},
 \end{array}
 \tag{17}
\]
where all \(L_n\) are generated by
\[
             L_{n+1}+qZL_n+q^2L_{n-1}=8qI.
 \tag{18}
\]
The [weighted-shift proof](research_current_free_aw_crossing_transport.md)
establishes (17)--(18) in the full quotient and retains
the ordinary free-boundary forcing when these operators
are applied to a boundary polynomial.

All three generators \(Z,L,L_1\) have bandwidth one.
For the last assertion one may directly calculate the
angular shifts to obtain
\[
 (q^2-q^{-2})L_1
     =q^{-1}ZL-qLZ+8(q-q^{-1})I.
 \tag{19}
\]
For \(N\ge3\) the scalar on the left is nonzero, and the
right side is tridiagonal. The cancellation can also be
made explicit. With \(Q=q^2\),
\[
 \begin{split}
 (L_1)_{jj}&=4qQ^j-q(1+Q)Q^{2j},\\
 (L_1)_{j,j+1}&=(L_1)_{j+1,j}=-(1-Q^{j+1})^2 .
 \end{split}
 \tag{20}
\]
These formulas hold at \(N=2\) as well, by the original
two-dimensional matrices. They avoid an artificial
\(1/\sin(2\pi/N)\) coefficient bound.

Use (17)--(18) to transport \(L-c_0I\) through the fixed
word. This gives a noncommutative polynomial in \(Z,L,L_1\)
whose number and degree of terms depend on the word, not
on \(N\). Hence \(D_{W,N}\), and the minor in (15), have
bandwidth bounded independently of the level.
Every entry is uniformly bounded in \(N\) by a word-dependent
constant. In the bulk, each entry at a fixed diagonal offset
is a Laurent polynomial in \(q\) and \(Q^j\); only a bounded
number of rows involve the finite boundary truncation.
This follows directly by multiplying the three displayed
finite-band matrices. No asymptotic recurrence or division
by a possibly zero pivot is used.

## 5. A spectral-measure reduction of the original scalar

Let \(B_{W,N}\) be the closing minor in (15). The fixed-band
formula has an elementary singular-value limit. This is the
usual finite-band moment argument, applied to this specific
original source matrix; it is not a new general matrix theorem.

For a matrix entry in row \(j\), encode its column offset \(s\)
by \(Y^s\), and put \(X=e^{2\pi ix}\). The bulk symbols of
the three generators, after \(q\to1\), are
\[
 \begin{split}
 \mathsf z(X,Y)&=X+X^{-1}+(X+X^{-1}-2)Y^{-1},\\
 \mathsf l(X,Y)&=X+X^{-1}+(X+X^{-1}-2)Y,\\
 \mathsf b(X,Y)&=4X-2X^2-(1-X)^2(Y+Y^{-1}).
 \end{split}
 \tag{21}
\]
Apply the chosen polynomial expression for (4) to these
commuting symbols, with \(q=1,c_0=2\), and call the resulting
Laurent polynomial \(\mathsf d_W(X,Y)\).
These are bulk Newton coordinates, not independently chosen
peripheral meridian coordinates. The shift of the rows in
the minor multiplies its symbol by \(Y\), which does not
change its modulus on the unit torus.

**Proposition 2.** For every continuous function \(a\) on
a compact interval containing all the squared singular
values of \(B_{W,N}\),
\[
 \lim_{N\to\infty}\frac1N\sum_{j=1}^{N-1}
                  a(s_j(B_{W,N})^2)
 =\int_0^1\int_0^{2\pi}
       a\!\left(|\mathsf d_W(e^{2\pi ix},e^{i\vartheta})|^2\right)
                       \frac{d\vartheta}{2\pi}\,dx.
 \tag{22}
\]

*Proof.* Fixed bandwidth and the uniform entry bound give
a uniform operator-norm bound. For \(a(t)=t^k\), the left
side is the normalized trace of \((B_{W,N}^\dagger B_{W,N})^k\).
Expand it as a sum of closed walks of length \(2k\).
There are only finitely many offset patterns, depending on
the fixed bandwidth and \(k\). Away from a bounded number
of boundary rows, a walk visits indices differing by \(O(k)\).
Its coefficients therefore differ by \(O(N^{-1})\), uniformly,
from the product of the limiting Laurent coefficients
evaluated at \(X=e^{2\pi ij/N}\).
The resulting sum of closed offset patterns is precisely
the constant coefficient in
\(|\mathsf d_W(X,Y)|^{2k}\) on \(|Y|=1\).
The remaining Riemann sum tends to the right side.
Boundary rows contribute \(O(N^{-1})\).
The constant moment also converges since \((N-1)/N\to1\).
Uniform polynomial approximation on the common compact
interval proves (22). \(\square\)

Define the regularized logarithmic mean
\[
 \mathfrak m_W=
   \lim_{\epsilon\downarrow0}
       \frac12\int_0^1\int_0^{2\pi}
        \log\!\left(|\mathsf d_W(e^{2\pi ix},e^{i\vartheta})|^2
                          +\epsilon\right)
                     \frac{d\vartheta}{2\pi}\,dx.
 \tag{23}
\]
The limit is decreasing and is permitted to be \(-\infty\).
Equations (15) and (22) imply the actual source bound
\[
 \boxed{\displaystyle
 \limsup_{N\to\infty}\frac1N\log|\phi_N(F_N)|
                                      \le\frac12\mathfrak m_W.}
 \tag{24}
\]
To prove it, use
\(\log s\le\frac12\log(s^2+\epsilon)\) in
\[
 \frac1N\log|\phi_N(F_N)|
       =\frac1{2N}\sum_{j=1}^{N-1}\log s_j(B_{W,N})
                                  -\frac{\log N}{N},
 \tag{25}
\]
with \(\log0=-\infty\). Apply (22) for fixed \(\epsilon>0\),
then decrease \(\epsilon\) to zero. No determinant has been
replaced by the product of selected local eigenvalues.

This also identifies a precise missing analytic estimate.
The reverse passage from (22) to (25) would require control
of the logarithmic contribution of small singular values,
for example
\[
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}
 \frac1N\sum_{\substack{j\\s_j(B_{W,N})<\delta}}
                         |\log s_j(B_{W,N})|=0.
 \tag{26}
\]
No such assertion is made here. It can fail for finite-band
matrices even when every continuous singular-value statistic
has the stated limit. Nor has \(\mathfrak m_W\) been identified
with the marked hyperbolic volume. Both issues remain separate
from the exact normalization in (15).

## 6. A small singular value in an original terminal closure

The missing logarithmic estimate is not automatic for the
source matrices just constructed. Take the actual word
\[
                             W_N=JM^2.
 \tag{27}
\]
Its state is the original terminal polynomial \(H_{2,N}\).
Its closing scalar is exactly
\(\phi_N(H_{2,N})=R^2(c_0)=\kappa^2\), so (25) has limit
zero through both parities.

The classical substitutions (17)--(18) give
\[
 \begin{split}
 \mathsf d_W
     &=6-\mathsf z-\mathsf l\mathsf b\\
     &=\frac{(X-1)^2(Y+1)(XY+X-Y)^2}{XY}.
 \end{split}
 \tag{28}
\]
The factors \(X-1\), \(Y+1\), and the monomial denominator
have zero logarithmic mean. Jensen's formula applied first
in \(X\) gives
\[
 \mathfrak m_W
    =2\int_0^{2\pi}
             \log\max\{|1+e^{i\vartheta}|,1\}
                         \frac{d\vartheta}{2\pi}>0.
 \tag{29}
\]
The integral is strictly positive because its integrand is
positive on an interval. Thus the bulk mean in (23) differs
from the actual logarithmic determinant rate, for this
original source and its original closing row.

There is also a quantitative small-singular-value statement.
For \(N\ge3\), let \(a_1\ge\cdots\ge a_{N-1}>0\) be
the nonzero singular values of \(D_{W,N}\), and
\(b_1\ge\cdots\ge b_{N-1}\ge0\) those of the closing
minor. Deleting one row and one column gives the elementary
compression inequalities
\[
                    b_i\ge a_{i+2}\quad(1\le i\le N-3).
 \tag{30}
\]
They follow by applying the singular-value min--max principle
once for each deleted coordinate. Equations (15)--(16)
therefore imply, whenever the closing scalar is nonzero,
\[
 \begin{split}
 b_{N-2}b_{N-1}
   &\le a_1a_2
       \frac{\prod_i b_i}{\prod_i a_i}
     =a_1a_2\frac{|\phi_N(F_N)|^2}{\|f_N\|_2^2},\\
 s_{\min}(B_{W,N})
   &\le \|D_{W,N}\|\,
                     \frac{|\phi_N(F_N)|}{\|f_N\|_2}.
 \end{split}
 \tag{31}
\]
If the closing scalar is zero, the minor is singular and
the second inequality still holds.

For (27), the exact
[terminal formula](research_two_crossing_terminal_filling.md)
has Newton coefficients of modulus \(N/S_j\), where
\[
                     S_j=\prod_{r=1}^j2\sin(\pi r/N).
 \tag{32}
\]
Choose \(j=\lfloor N/6\rfloor\). The elementary sine-product
Riemann sum, retaining its logarithmic endpoint error, gives
\[
 \log S_j=-N c_*+O(\log N),\qquad
 c_*=-\int_0^{1/6}\log(2\sin\pi x)\,dx>0.
 \tag{33}
\]
Consequently \(\|f_N\|_2\ge\exp(Nc_*+O(\log N))\).
The fixed-band matrix norm is uniformly bounded, and
\(|\phi_N(F_N)|=1\). Equation (31) proves
\[
             s_{\min}(B_{W,N})
                    \le \exp(-Nc_*+O(\log N)).
 \tag{34}
\]
Thus an exponentially small singular value is present in
the actual normalized determinant. It cannot be discarded
on the grounds that the matrix has a fixed bandwidth and a
smooth bulk symbol. This example concerns a closure with
zero exponential rate; it makes no claim against a
hyperbolic volume theorem.

## 7. What the determinant formula does and does not settle

For a fixed original word, (15) is one normalized determinant
of a finite-band matrix, rather than a sum of separately
estimated color contributions. Its rank, source scale, and
endpoint normal have all been fixed at every integer level.

The remaining question is the growth of this particular
minor. Its entries are oscillatory, and positivity of the
final scalar does not make its intermediate minors positive.
A product of local spectral radii or an adiabatic transfer
argument is not supplied by (15). In particular very small
singular values can change the logarithmic determinant by
an order-\(N\) amount. The exponential inverse example in
the weighted-shift note is one reason to retain that issue.

Thus the formula supplies an exact determinant problem for
the original period, including its boundary forcing. It
does not yet prove the geometric exponential rate for
arbitrary adjacent short components.

## 8. Reproduction

[The finite checker](../experiments/check_rational_word_normalized_cofactor.py)
uses the original crossing matrices and computes adjugates
from their minors. It compares them with (5), checks the
closing minor and free-boundary determinant, and differentiates
the polarized identity in both boundary variables.
It also checks the explicit tridiagonal formula and (19),
including \(N=2\).

The [saved 110-digit record](../repro/results/research-rational-word-normalized-cofactor.json)
contains 56 level-word cases and 448 polarized value/normal
comparisons, with source and dependency hashes. It includes
both parities, signed crossings, turns, and zero closing
scalars. These finite checks do not test the asymptotic
spectral-measure statement or a volume limit.
The [150-digit replay](../repro/results/research-rational-word-normalized-cofactor-root.json)
checks the same cases directly from minors of the original matrices;
its largest relative error is less than \(1.5\cdot10^{-141}\).
