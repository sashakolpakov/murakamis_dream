# The characteristic polynomial of the original source monodromy

Research note, 3 November 2026.

The complete product of the original resonant run transfers has exactly
the characteristic polynomial of its classical transfer, evaluated at
the \(N\)-th power of the auxiliary clock. This holds for both parities
of the crossing power and both signs. For two runs it identifies the
denominator in the marked affine transport equation. The numerator and
its source-bearing reset jet remain separate data.

## 1. The original transfers and the statement

Fix \(N\ge2\), \(q=e^{\pi i/N}\), \(Q=q^2\), and put
\[
 \eta=(-1)^{N-1},\qquad \epsilon=(-1)^N=-\eta.
 \tag{1}
\]
For a nonzero signed crossing power \(p\), set
\(k=\lceil |p|/2\rceil\), \(q_p=q^{\operatorname{sgn}p}\), and
\(Q_p=q_p^2\). In particular \(Q_p\) is primitive and \(q_p^N=-1\).
The channel matrix and its polynomial pole cancellation are
\[
 \begin{split}
 C_k(r)&=(r+r^{-1})I_k-T_k-rE_{11},\\
 \mathcal B_k(r;q_0)
   &=(1-r/q_0)[C_k(r)-q_0^{-1}E_{kk}]^{-1},
 \end{split}                                                    \tag{2}
\]
where \(T_k\) is path adjacency. The second expression extends
polynomially in \(r\), including \(r=q_0\), by equation (4) of the
[original two-run source calculation](research_two_run_source_transfer.md).

For \(\xi_j=zQ_p^j\), \(z\ne0\), define the original transfers
\[
 \mathcal T_p(j;z)=
 \begin{cases}
 (1-\xi_j^{-1})\mathcal B_k(q_p\xi_j;q_p),
                                      & |p|=2k,\\
 \mathcal B_k(q_p\xi_j;q_p)
       \operatorname{diag}(-\xi_j^{-1},
                       1-\xi_j^{-1},\ldots,1-\xi_j^{-1}),
                                      & |p|=2k-1.
 \end{cases}                                                     \tag{3}
\]
For \(k=1\), the odd diagonal has only its first entry. Retain the
full product, including the reset factor at color zero:
\[
 \mathcal P_{p,N}(z)
       =\mathcal T_p(N-1;z)\cdots\mathcal T_p(0;z).
 \tag{4}
\]
This is not the original initial-value recurrence by itself: the
source uses its prescribed residue vector at color zero. Its relation
to (4) is the marked reset-jet identity in the
[source-jet note](research_two_run_monodromy_source_jets.md).

Let \(T^{\mathrm{cl}}_r(x)\), \(r\ge1\), mean the matrix in (3)
with \(q_p=1\) and \(\xi_j=x\), using the indicated parity of \(r\).
It is a Laurent-polynomial matrix in \(x\).

**Theorem 1.** For every nonzero signed \(p\), \(z\ne0\), and
\(\lambda\in\mathbb C\),
\[
 \boxed{\quad
 \det(I_k-\lambda\mathcal P_{p,N}(z))
   =\det(I_k-\lambda\epsilon T^{\mathrm{cl}}_{|p|}(z^N)).
 \quad}                                                         \tag{5}
\]
The identity includes the reset \(z^N=1\). It asserts equality of
characteristic polynomials, not a controlled similarity or equality
of the marked input and output vectors.

## 2. A continuant with a last Robin term

We need a slight extension of the oscillator calculation in
[the endpoint monodromy proof](research_cyclotomic_endpoint_monodromy.md),
Section 2. Suppose a rational family of \(N\)-dimensional matrices
satisfies
\[
 BA-QAB=(1-Q)I,\qquad A^N=aI,\qquad B^N=bI.
 \tag{6}
\]
Here \(Q\) is primitive. Put \(Z=A+B\), and define the ordered
continuants and their scalar counterparts by
\[
 \begin{array}{c}
 F_{-1}=B,\quad F_0=I,\quad F_{j+1}=ZF_j-F_{j-1},\\
 p_{-1}=b,\quad p_0=1,\quad p_{j+1}=(a+b)p_j-p_{j-1}.
 \end{array}                                                     \tag{7}
\]
In each application below the family has a parameter value at which
\(A=B^{-1}\) and \(B\) has \(N\) distinct eigenvalues whose \(N\)-th
powers are \(b\ne0\).

**Lemma 2.** Under these hypotheses,
\[
 \boxed{\quad
       \det(F_m-sF_{m-1})
                   =\eta^m(p_m-s^Np_{m-1}).
 \quad}                                                         \tag{8}
\]
The identity extends across singular intermediate pivots.

*Proof.* The transformation
\[
              (A,B)\longmapsto(A+B-A^{-1},A^{-1})
 \tag{9}
\]
preserves (6) and sends the central powers to
\((a+b-a^{-1},a^{-1})\). For completeness, if \(C=AB-I\), then
\(CA=QAC\) and \(A^NB^N=I+\eta C^N\). The new first matrix is
\(A+A^{-1}C\); the root-of-unity binomial formula gives its \(N\)-th
power as \(a+b-a^{-1}\). This is the finite algebra calculation
already proved in the cited endpoint note.

On the nonempty rational open set of invertible pivots, put
\(Y_0=B^{-1}\) and \(Y_j=F_jF_{j-1}^{-1}\). Repeated use of (9)
gives
\[
                  Y_j^N=(p_j/p_{j-1})I.                 \tag{10}
\]
At the specified parameter value every \(Y_j=B^{-1}\), with simple
spectrum. In a neighborhood where this remains simple, (10) forces
each of the \(N\) roots of \(p_j/p_{j-1}\) to occur once. Therefore
\[
          \det(Y_j-sI)=\eta(p_j/p_{j-1}-s^N).
 \tag{11}
\]
This is an identity of rational functions, because it holds on a
nonempty open set. In particular \(\det F_j=\eta^jp_j\).
Since \(F_m-sF_{m-1}=(Y_m-sI)F_{m-1}\), (11) proves (8).
Clearing denominators extends it to the entire family. We have used
the simple-spectrum specialization to determine the full characteristic
polynomial; the central-power relation alone would not determine the
eigenvalue multiplicities. \(\square\)

## 3. Two Robin boundaries in a cyclic product

For arbitrary nonzero \(r\) and a scalar \(s\), set
\[
 H_j=C_m(rQ^j)-sE_{mm},\qquad
 R=\eta r^N,\qquad S=\eta s^N.
 \tag{12}
\]
On the open set \(1-(sr)^N\ne0\), all \(H_j\) are invertible.
The following identity is meromorphic in the parameters:
\[
 \boxed{\quad
 \det\!\left(I-\lambda H_{N-1}^{-1}\cdots H_0^{-1}\right)
   =\det\!\left(I-\lambda[C_m(R)-SE_{mm}]^{-1}\right).
 \quad}                                                         \tag{13}
\]

To prove it, form the cyclic color equations
\[
                   H_ju_j-tu_{j-1}=f_j,\qquad j\bmod N.
 \tag{14}
\]
Factoring the diagonal blocks and taking a cyclic Schur complement
shows that their determinant is
\[
 \left(\prod_j\det H_j\right)
       \det(I-t^NH_{N-1}^{-1}\cdots H_0^{-1}).           \tag{15}
\]
A cyclic rotation of the product does not change this determinant.
Now reorder simultaneously rows and columns by channel. Put
\[
 B=\operatorname{diag}(rQ^j),\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad A=B^{-1}-tE.
 \tag{16}
\]
These obey (6), with
\(b=r^N\), \(a=b^{-1}+(-t)^N\). The channel matrix has first
diagonal block \(A\), subsequent blocks \(A+B\), last subtraction
\(sI\), and adjacent blocks \(-I\). Its determinant is
\(\det(F_m-sF_{m-1})\), first by Schur complements and then by
polynomial continuation. Lemma 2 applies, since \(t=0\) supplies
the required specialization.

The scalar recurrence and
\[
 R+R^{-1}-t^N=\eta(a+b),\qquad S=\eta s^N
 \tag{17}
\]
give
\[
 \det(F_m-sF_{m-1})
             =\det(C_m(R)-SE_{mm}-t^NI).
 \tag{18}
\]
The normalization is exact:
\[
 \prod_j\det H_j
    =R^{-m}[1-(sr)^N]
    =\det(C_m(R)-SE_{mm}).                              \tag{19}
\]
Equations (15), (18), and (19), with \(\lambda=t^N\), prove (13).
The argument also covers \(m=1\), when the first and last diagonal
modifications occur in the same entry.

## 4. The actual even source

Throughout Sections 4--5, write \(q=q_p\) and \(Q=q_p^2\);
this includes either sign of the original power. Both choices
satisfy \(q^N=-1\), with \(Q\) primitive. Set \(x=z^N\) and
\(w(\xi)=(1-\xi)(1-\xi^{-1})\).
For an even run, equation (3) is
\[
 \mathcal T_{2k}(j;z)
     =w(\xi_j)[C_k(q\xi_j)-q^{-1}E_{kk}]^{-1}.
 \tag{20}
\]
Use (13) with \(r=qz\), \(s=q^{-1}\). Its new parameters are
\(R=\epsilon x\), \(S=\epsilon\), and
\[
                 \prod_{j=0}^{N-1}w(\xi_j)=w(x).
 \tag{21}
\]
If \(D_\epsilon=\operatorname{diag}(1,\epsilon,\ldots,
\epsilon^{k-1})\), then
\[
 C_k(\epsilon x)-\epsilon E_{kk}
   =\epsilon D_\epsilon[C_k(x)-E_{kk}]D_\epsilon.
 \tag{22}
\]
Thus the normalized cyclic product has the characteristic polynomial
of \(\epsilon w(x)[C_k(x)-E_{kk}]^{-1}
=\epsilon T^{\mathrm{cl}}_{2k}(x)\). This proves (5) away from
the intermediate poles. Both sides of (5) are Laurent polynomials in
\(z\), by the pole cancellation in (2), so the identity extends
across \(z^N=1\).

## 5. The actual odd source

The odd color edge is not scalar. Its oscillator realization
nevertheless has the same central reduction. Again write \(q\)
for \(q_p\), put \(\xi_j=zQ^j\), and let
\[
 X=\operatorname{diag}(\xi_j),\qquad
 E\mathbf e_j=\mathbf e_{j+1\bmod N},\qquad XE=QEX.
 \tag{23}
\]
The exact odd transfer is
\[
 \mathcal T_{2k-1}(j;z)=H_j^{-1}D_j,\qquad
 \begin{cases}
 H_j=C_k(q\xi_j)-q^{-1}E_{kk},\\
 D_j=\operatorname{diag}(1-\xi_j^{-1},w(\xi_j),\ldots).
 \end{cases}                                                     \tag{24}
\]
Form the cyclic equations \(H_ju_j-tD_ju_{j-1}=f_j\).
Their determinant is
\[
 \left(\prod_j\det H_j\right)
                       \det(I-t^N\mathcal P_{2k-1,N}(z)).
 \tag{25}
\]
No invertibility of the color edges \(D_j\) is needed for this
cyclic determinant formula.

After channel reordering, the first diagonal block, the difference
between a later block and the first, and the last Robin scalar are
respectively
\[
 \begin{split}
 A&=q^{-1}X^{-1}+t(X^{-1}-I)E,\\
 B&=qX+t(X-I)E,\qquad s=q^{-1}.
 \end{split}                                                     \tag{26}
\]
Later diagonal blocks are \(A+B\), adjacent blocks are \(-I\),
and the last diagonal has subtraction \(sI\). Direct multiplication,
using \(XE=QEX\) and \(Q=q^2\), gives
\[
                         BA-QAB=(1-Q)I.                 \tag{27}
\]
For example, its coefficients of \(E\) and \(E^2\) both vanish;
the constant coefficient is \(1-Q\).

Write
\[
                        x=z^N,\qquad \tau=\epsilon t^N.
 \tag{28}
\]
The two cyclic bidiagonal matrices in (26) have central powers
\[
 \boxed{\quad
 A^N=aI,\quad a=\tau-(1+\tau)x^{-1},\qquad
 B^N=bI,\quad b=\tau-(1+\tau)x.
 \quad}                                                         \tag{29}
\]
Here is a direct check that keeps the signs. For a diagonal matrix
with entries \(d_j\) and a cyclic shift with row weights \(\beta_j\),
the characteristic polynomial is
\(\prod_j(\lambda-d_j)-\prod_j\beta_j\).
For \(A\), the first product is \(\lambda^N+x^{-1}\), and the
second is
\[
 t^N\prod_j(\xi_j^{-1}-1)
                      =\epsilon t^N(1-x^{-1}).
 \tag{30}
\]
For \(B\), the corresponding expressions are
\(\lambda^N+x\) and \(\epsilon t^N(1-x)\).
Cayley--Hamilton proves (29).

At \(t=0\), \(A=B^{-1}\) with simple spectrum. Lemma 2 therefore
applies to (26). Since \(s^N=-1\), the reordered determinant is
\[
                         \eta^k(p_k+p_{k-1}).            \tag{31}
\]
Compare it to the classical odd matrix. Set
\[
 H^{\mathrm{cl}}=C_k(x)-E_{kk},\qquad
 D^{\mathrm{cl}}
      =\operatorname{diag}(1-x^{-1},w(x),\ldots).
 \tag{32}
\]
The first diagonal of \(H^{\mathrm{cl}}-\tau D^{\mathrm{cl}}\)
is \(-a\), the later bulk diagonals are \(-(a+b)\), and its
last subtraction is \(1\). Alternating channel signs, followed
by an overall minus sign, consequently give
\[
        \det(H^{\mathrm{cl}}-\tau D^{\mathrm{cl}})
                         =(-1)^k(p_k+p_{k-1}).            \tag{33}
\]
This statement includes \(k=1\), where the single entry is
\(-a-1\).
Finally
\[
 \prod_j\det H_j=\epsilon^k x^{-k}(1-x),\qquad
 \det H^{\mathrm{cl}}=x^{-k}(1-x).                       \tag{34}
\]
Since \(\eta^k=\epsilon^k(-1)^k\), equations (25), (31)--(34)
prove
\[
 \det(I-t^N\mathcal P_{2k-1,N}(z))
       =\det(I-\epsilon t^N T^{\mathrm{cl}}_{2k-1}(x)).
 \tag{35}
\]
Every complex \(\lambda\) is \(t^N\). Laurent-polynomial
continuation removes the temporary restriction \(x\ne1\).
This proves Theorem 1 for odd powers and completes its proof.

## 6. The explicit denominator for two original runs

Retain independent clocks \((z_a,z_b)\), the original transfer
ordering, and the literal turn interface. The top block of the
augmented source monodromy is exactly
\[
 U_N(z_a,z_b)=\mathcal P_{a,N}(z_a)\otimes
                              \mathcal P_{b,N}(z_b).
 \tag{36}
\]
The eigenvalues of a tensor product are all pairwise products,
with algebraic multiplicity, including for non-diagonalizable
matrices. Thus Theorem 1 gives the following explicit identity.

**Corollary 3.** For all nonzero signed \(a,b\),
\[
 \boxed{\quad
 \det(\lambda I-U_N(z_a,z_b))
  =\det\!\left(\lambda I-
        T^{\mathrm{cl}}_{|a|}(z_a^N)\otimes
        T^{\mathrm{cl}}_{|b|}(z_b^N)\right).
 \quad}                                                         \tag{37}
\]
The two level-parity signs have canceled. In particular, where
the marked affine row \(r_N(I-U_N)^{-1}\) exists, its denominator
is the fixed classical polynomial on the right of (37), evaluated
at \(\lambda=1\). Along the original signed clock leaf
\((z_a,z_b)=(x^{\operatorname{sgn}a},
x^{\operatorname{sgn}b})\), the two arguments become
\(x^{N\operatorname{sgn}a}\) and \(x^{N\operatorname{sgn}b}\).

Every classical odd transfer has eigenvalue \(-1\). One direct
proof sets \(\tau=-1\) in (29): \(a=b=-1\), and (7) gives
\(p_k=(-1)^k\), hence (33) vanishes. Therefore every odd--odd
pair has \(\det(I-U_N)\equiv0\); an inverse is not asserted there.
If at least one power is even, the full top product is zero at
the physical reset, and this denominator equals one there.
These are precisely the knot cases for the literal cylindrical
two-run closure, by the endpoint-pairing calculation in the
source-jet note.

In particular define the fixed Laurent polynomial
\[
 D_{a,b}(X)=\det\!\left(I-
 T^{\mathrm{cl}}_{|a|}(X^{\operatorname{sgn}a})\otimes
 T^{\mathrm{cl}}_{|b|}(X^{\operatorname{sgn}b})\right).
 \tag{38}
\]
For the natural signed leaf, the exact original top monodromy obeys
\[
 \boxed{\qquad
             \det(I-\widehat U_N(x))=D_{a,b}(x^N).
 \qquad}                                                        \tag{39}
\]
For every knot case \(D_{a,b}(1)=1\); for every odd--odd pair
\(D_{a,b}\equiv0\). The polynomial in (38) has degree bounded in
terms of the two fixed crossing powers, independently of \(N\).

The formula determines the denominator but does not bound the
marked numerator, its reset derivatives, or a similarity matrix.
The original source is the specified first or second derivative
of the accumulator row in the knot cases. A local holomorphic
shear can erase that row while preserving the characteristic
polynomial; its derivatives then retain the source. Thus (37)
does not prove a geometric asymptotic or noncancellation of the
coherent original color sum.

## 7. Literature and the scope of this calculation

Root-of-unity centers and the quantum Frobenius mechanism are
established ideas. Fock and Goncharov,
[*Cluster ensembles, quantization and the dilogarithm*](https://smf.emath.fr/download/pdf/43892),
Annales scientifiques de l'École normale supérieure 42 (2009),
865--930, Sections 3.1.1 and 3.4, describe quantum-torus centers
and a quantum Frobenius map compatible with mutation. No novelty
for that mechanism is claimed here. The proof above is an
independent finite oscillator calculation for the particular
original resonant matrices, with both level parities, the Robin
terms, the sign directions, and the source reset retained; it
does not invoke their theorem to supply these details.

Jun Murakami's
[*Complexified tetrahedrons, fundamental groups, and volume conjecture
for double twist knots*](https://arxiv.org/abs/2501.00225v3),
version 3 (2 May 2025), states a proof of the volume conjecture
for double twist knots. That proof is not audited or used in this
note. The present result is an exact intermediate description of
the original source and is not presented as new knot-family
coverage for the volume conjecture.

## 8. Reproduction

The existing [source-jet diagnostic](../experiments/check_two_run_monodromy_source_jets.py)
now also constructs the full actual run products at arbitrary
auxiliary clocks. Its [saved record](../repro/results/research-two-run-monodromy-source-jets.json)
checks 128 signed run cases at \(N=2,\ldots,9\), with
\(1\le |p|\le8\), through 320 power traces, and 112 actual
two-run characteristic denominators. The 110-digit run passed,
with largest relative residual \(5.34591726182\cdot10^{-106}\)
across the full diagnostic. It retains the original matrix/jet
comparisons and the derivative-free numerator extraction.

For reproduction:

    python experiments/check_two_run_monodromy_source_jets.py \
      --precision 110 \
      --output repro/results/research-two-run-monodromy-source-jets.json

These finite checks test normalization and implementation. The
all-level assertions are proved in Sections 2--6; no asymptotic
coefficient is inferred from the diagnostic.
