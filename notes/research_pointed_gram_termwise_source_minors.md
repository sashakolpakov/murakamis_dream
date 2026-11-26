# Every pointed Gram minor retains its actual color observation

Research note, 17 November 2026. The positive Cauchy--Binet formula
for the actual pointed quantum-A period has a termwise source
factorization. Each numerator minor for a specified color is that
same color value times its corresponding denominator minor. The
bounded jet nullity also makes the number of denominator terms
polynomial in the level.

These statements identify exactly what a triangular or path-minor
estimate would have to control. They do not supply a new lower
bound for the complete quantum period.

## 1. The actual pointed matrices

Use the uniformly scaled actual matrix and source from the complete
[pointed Gram theorem G](pointed_a_gram_period.md), Sections 2--5:
\[
 M y=b,\qquad
 R y=f=(C_{j_*}(q_N),\ldots,C_N(q_N))^{\mathsf t},
 \qquad \ker M\subset\ker R .
 \tag{1}
\]
Here \(q_N=e^{\pi i/N}\), \(M\) is square of size
\(n=(B+1)(N-j_*+1)\), and the fixed jet budget \(B\) retains
every singular recurrence step. Its rank and nullity are
\[
                  r=\operatorname{rank}M,\qquad
                  \nu=n-r\le B.
 \tag{2}
\]
The original fixed small-color jets form \(b\); no unknown large
color is inserted into this source. Every solution in (1) has the
same \(f\), including the prescribed complete value
\(f_N=C_N(q_N)=\langle K\rangle_N\). In subscripts on \(f\)
or rows of \(R\), colors are labelled by their original integers.

Keep the actual coefficient polynomials
\[
 \begin{split}
 Q(\lambda)&=\det(M^*M+\lambda I),\\
 D(\lambda,z)&=
 \det\begin{pmatrix}
 M^*M+\lambda I+zR^*R&M^*b\\
 b^*M&b^*b
 \end{pmatrix}.
 \end{split}
 \tag{3}
\]
Their coefficients of interest are
\[
 q_\nu=[\lambda^\nu]Q>0,\qquad
 d_\nu=[\lambda^\nu z]D,\qquad
                         G_N=d_\nu/q_\nu.
 \tag{4}
\]
G proves \(G_N=\sum_{k=j_*}^N|f_k|^2\). We will identify
the individual minors underlying this equality.

## 2. Exact factorization of every source minor

Let \(J,S\subset\{1,\ldots,n\}\), each of cardinality \(r\),
denote a matrix row set and a matrix column set, both in their
increasing order. For a color \(k\), set
\[
 \Delta_{J,S}=\det M_{J,S},\qquad
 T_{J,S,k}=
 \det\begin{pmatrix}
 M_{J,S}&b_J\\
 R_{k,S}&0
 \end{pmatrix}.
 \tag{5}
\]
The ordering in (5), with the observation row and source column
last, fixes the sign.

**Theorem 1.** For all such sets and every original color,
\[
                         T_{J,S,k}=-f_k\Delta_{J,S}.
 \tag{6}
\]
This includes zero minors, possible zero color values, and singular
pointed matrices.

**Proof.** First suppose the \(r\) full rows \(M_{J,:}\) are
independent. They span the row space of \(M\). By (1), \(R_k\)
annihilates \(\ker M\), hence is in that row space. There is
a row \(\gamma\) such that
\[
            R_k=\gamma M_{J,:},\qquad
            f_k=R_ky=\gamma b_J .
 \tag{7}
\]
Subtract \(\gamma\) times the first \(r\) rows in (5) from
its last row. That row becomes \((0,\ldots,0,-f_k)\),
so expansion along it proves (6). No inverse of \(M_{J,S}\)
was used; this proof includes a singular selected column minor.

If instead the rows \(M_{J,:}\) are dependent, their augmented
rows \((M_{J,:},b_J)\) have the same rank, because
\(b_J=M_{J,:}y\). Restricting to the columns in (5) cannot
increase that rank. Appending its last row therefore gives
rank at most \(r\), less than the size \(r+1\). Thus
\(T_{J,S,k}=0\), while \(\Delta_{J,S}=0\) as well.
This proves (6) in all cases. \(\square\)

## 3. The actual Cauchy--Binet terms

The denominator is the Gram determinant of the stacked matrix
\(\binom{M}{\sqrt\lambda I}\). Its coefficient of
\(\lambda^\nu\) chooses exactly \(\nu\) identity rows and
\(r\) rows of \(M\). Expanding the chosen identity rows leaves
precisely the complementary column set \(S\), with \(|S|=r\).
Consequently
\[
                    q_\nu=\sum_{|J|=|S|=r}|\Delta_{J,S}|^2.
 \tag{8}
\]
For the numerator use the actual rectangular Gram factor from G,
\[
 \mathcal Z(\lambda,z)=
 \begin{pmatrix}
 M&b\\
 \sqrt z R&0\\
 \sqrt\lambda I&0
 \end{pmatrix}.
 \tag{9}
\]
The coefficient of \(\lambda^\nu z\) selects exactly \(\nu\)
identity rows, one observation row \(R_k\), and \(r\) matrix
rows. Expanding the identity rows leaves (5), up to a row or
column ordering sign which disappears after taking its squared
modulus. Hence
\[
 \begin{split}
 d_\nu
   &=\sum_{k=j_*}^N\ \sum_{|J|=|S|=r}|T_{J,S,k}|^2\\
   &=\sum_{k=j_*}^N |f_k|^2
                   \sum_{|J|=|S|=r}|\Delta_{J,S}|^2.
 \end{split}
 \tag{10}
\]
Thus the positive expansion already has the same source
factor in each term, before different minors are added.

A useful additional restriction is that a nonzero
\(\Delta_{J,S}\) cannot omit any constant-jet coordinate
selected by \(R\). If that coordinate were outside \(S\),
then \(R_{k,S}=0\), while (7) and invertibility of \(M_{J,S}\)
would force \(\gamma=0\) and \(R_k=0\), a contradiction.
Only normal-jet coordinates can be omitted in a nonzero term.

## 4. Exact normalization of a selected minor family

Define the actual denominator weights
\[
              \omega_{J,S}=\frac{|\Delta_{J,S}|^2}{q_\nu}.
 \tag{11}
\]
They are nonnegative and sum to one. For any family
\(\mathcal F_N\) of the row-column pairs in (5),
\[
 \frac{\sum_{(J,S)\in\mathcal F_N}|T_{J,S,k}|^2}{q_\nu}
       =|f_k|^2\,\theta_N,\qquad
 \theta_N=\sum_{(J,S)\in\mathcal F_N}\omega_{J,S}\in[0,1].
 \tag{12}
\]
The family may be selected by a triangular pattern, paths in
the fixed band, or any other rule. No independence assumption
on this selection is needed for the exact equality.

There are at most
\[
                  L_N=\binom n\nu^2\le n^{2B}
 \tag{13}
\]
denominator terms, since the nullity budget in (2) is fixed.
Choose a pair \((J_N,S_N)\) maximizing
\(|\Delta_{J,S}|^2\). It has nonzero minor and satisfies
\[
 \frac1{L_N}\le\omega_{J_N,S_N}\le1,\qquad
 \frac{|f_k|^2}{L_N}
 \le\frac{|T_{J_N,S_N,k}|^2}{q_\nu}
 \le |f_k|^2 .
 \tag{14}
\]
Thus this source-independent choice of denominator minor loses
at most a polynomial factor in the normalized squared observation.
Its bordered minor nevertheless obeys the exact relation
\(T_{J_N,S_N,k}/\Delta_{J_N,S_N}=-f_k\). There is no
additional source overlap supplied by its large denominator mass.

For the terminal color, (12) is literally
\[
 \frac{\sum_{\mathcal F_N}|T_{J,S,N}|^2}{q_\nu}
                       =\theta_N|\langle K\rangle_N|^2.
 \tag{15}
\]
Every terminal source minor vanishes if that original complete
value vanishes. A proposed lower bound based on such minors
must estimate their source border as well as their denominator
normalization. A nonzero triangular denominator or a polynomial
lower bound on \(\theta_N\) alone does not do this.

For completeness, families selected separately for different
ordinary colors have normalized sum bounded above by
\(\sum_{k<N}|C_k(q_N)|^2\). The actual ordinary-color estimate
in G, Section 6, makes that sum polynomial in \(N\) for the
fixed knot. Thus the ordinary-color terms cannot supply a
positive exponential lower rate for (4).

## 5. Scope and proof source

G already proves the aggregate coefficient ratio and coefficient
positivity. The additional calculation here is its termwise
factorization (6), with the exact selected-family normalization
and fixed-nullity count (12)--(14). All jet rows and the original
initial source are retained.

This does not rule out a further exact evaluation or lower bound
for a bordered minor using special structure of the actual
operator. Such a calculation would estimate the original color
value through (6). The present calculation supplies no such
factorization of the complex entries, no positivity of their path
expansion, and no geometric exponential estimate.

The sole complete proof source is G,
[pointed_a_gram_period.md](pointed_a_gram_period.md), SHA256
\[
 \texttt{8de50a01f06b406e76325d09ea7d6c415afe6a4629c8d2380a809d447c64583c}.
\]
It was read in full; its actual consistency, kernel-annihilation,
nullity bound, coefficient polynomials and ordinary-color bound
are precisely the inputs used above. Every determinant
factorization and counting argument here is written explicitly.
No mathematical computation or numerical test is used.
