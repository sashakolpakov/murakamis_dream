# The actual degree-selected boundary Ward packet has a nonzero entry

Written research proof, 23 November 2026.

For the literal reduced boundary crossing, the entire resonant Ward
sum is one donor-diagonal commutator. Its component with donor loss
one has no triangular-transfer cancellation. An explicit physical
input and output give a lower bound after both the required total
degree selection and the physical weight restriction. This holds at
every level, including even and composite levels, whenever the
indicated physical weight exists.

The result is a lower bound for a full first-normal matrix packet.
Its exhibited component can lie on an occupation boundary; it is
not identified with a growing geometric mode. The original marked
closing, arbitrary exterior and its possible scalar cancellation
remain. No knot-volume or general short-component lower bound is
claimed.

## 1. Original operators and the selected physical arrow

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad m=r+1,\quad r\ge2,\quad x(M)=-M/q,
 \quad x_0=x(1),\quad F_j=(Q;Q)_j.
 \tag{1}
\]
The quantum parameter remains fixed. All physical occupation bases
are orthonormal in the Euclidean norms used below. Split the
remaining \(r\) heads into a first donor and its ordered tail.
Write \(L|j\rangle=|j-1\rangle\) for \(j>0\), with bottom zero,
and \(Z|j\rangle=Q^j|j\rangle\). Let
\(K_{\rm T}(M),E_{\rm T}(M),F_{\rm T}(M)\) be the actual tail
coproducts. The complete remaining lowering and Cartan operators are
\[
 \begin{split}
 E(M)&=E_{\rm T}(M)+L(MZ^{-1}-M^{-1})K_{\rm T}(M),\\
 K_r(M)&=x(M)Z^{-1}K_{\rm T}(M)=M^rK_0.
 \end{split}
 \tag{2}
\]
In particular \(K_0L=QLK_0\). The root values are denoted by
omitting \(M\); thus \(E=E(1)\).

Retain the actual scalar \(\kappa(M)\). Source [R, (12)] gives
the literal positive reduced boundary crossing
\[
 \begin{split}
 b(M)&=\kappa(M)S_r(M)D(M),\\
 S_r(M)&=\sum_{j=0}^{d}
              \frac{(x(M)^{-1}LF_{\rm T}(M))^j}{F_j},\\
 D(M)|j\rangle&=(-1)^jQ^{j(j+1)/2}M^{-2j}|j\rangle.
 \end{split}
 \tag{3}
\]
All missing physical arrows are zero. Set \(b=b(1)\),
\(\kappa=\kappa(1)\ne0\), and
\(D=D(1)\). The matrix \(D\) is unitary and the zero donor-loss
part of \(S_r\) is exactly the identity.

Choose an actual eigenvalue \(\lambda\in\operatorname{spec}K_0\)
and its nonself reciprocal Ward order \(1\le t<N\), so
\[
 \lambda^2=Q^{-t},\qquad P_\lambda\ne0,
 \qquad a_0=\lambda/x_0,\qquad a_0^2=Q^{1-t},\quad |a_0|=1.
 \tag{4}
\]
Here \(P_\lambda\) is the original frozen Cartan projector.
At even \(N\), only orders occurring among these actual weights
are being asserted. No absent weight is supplied by interpolation.
The original flattened boundary Ward arrow of [W, (19)--(20)] is
\[
 \mathfrak D_tP_\lambda
 =2m\sum_{n=1}^t(-1)^{n-1}a_0^n
       \frac{F_t}{F_{t-n}(1-Q^n)}E^{t-n}bL^nP_\lambda.
 \tag{5}
\]
The total degree loss is already \(t\). Every transfer and scalar
in (5) is retained.

## 2. Whole-meridian conjugation and resonant cancellation

The transformed lowering row [C, (5)], applied to the remaining
prefix, is
\[
 S_r(M)^{-1}E(M)S_r(M)
       =E_{\rm T}(M)+L\bigl(MK_{\rm T}(M)Z^{-1}
                              -M^{-1}K_{\rm T}(M)^{-1}\bigr).
 \tag{6}
\]
The diagonal in (3) satisfies the exact finite relation
\(D(M)^{-1}LD(M)=-M^{-2}LZ\), including the bottom zero.
Define
\[
 \begin{split}
 C_M&=E_{\rm T}(M)-M^{-1}LK_{\rm T}(M),\\
 X_M&=MLZ^{-1}K_{\rm T}(M),\qquad
 Y_M=M^{-3}LZK_{\rm T}(M)^{-1}.
 \end{split}
 \tag{7}
\]
Equations (2),(3),(6) give the whole-meridian identities
\[
 E(M)=C_M+X_M,\qquad
 b(M)^{-1}E(M)b(M)=C_M+Y_M.
 \tag{8}
\]
Within (7), only the invertible Cartan matrices are inverted;
\(b(M)^{-1}\) in (8) is the actual inverse crossing. The scalar
\(\kappa(M)\) cancels in conjugation and will reappear in \(b\).

The physical relations
\(ZL=Q^{-1}LZ\) and
\(K_{\rm T}E_{\rm T}=QE_{\rm T}K_{\rm T}\) imply
\[
 X_MC_M=QC_MX_M,\qquad
 Y_MC_M=Q^{-1}C_MY_M.
 \tag{9}
\]
For example both summands of \(C_M\) have the indicated relation
with \(X_M\), by these two relations separately. The inverse
relations prove the statement for \(Y_M\). All are finite-matrix
identities with their actual endpoints.

On the frozen input weight in (4), powers of these operators obey
\[
 \begin{split}
 X_M^nP_\lambda
  &=M^{rn}a_0^nQ^{n(n-1)/2}L^nP_\lambda,\\
 Y_M^nP_\lambda
  &=M^{-(r+2)n}a_0^{-n}Q^{-n(n-1)/2}L^nP_\lambda.
 \end{split}
 \tag{10}
\]
Indeed \(X_M=M^rL(x_0^{-1}K_0)\) and
\(Y_M=M^{-(r+2)}L(x_0^{-1}K_0)^{-1}\).
Commuting their frozen Cartans through \(L\) proves (10).

Apply the finite binomial formula in the order \(C_M^{t-n}X_M^n\)
and \(C_M^{t-n}Y_M^n\). Since
\({t\brack n}_{Q^{-1}}=Q^{-n(t-n)}{t\brack n}_Q\), the ratio
of the two input-weight coefficients is
\(M^{-2mn}(a_0^{-2}Q^{1-t})^n=M^{-2mn}\). Thus exactly
\[
 \begin{split}
 \Delta(M)P_\lambda
 &:=(b(M)^{-1}E(M)^tb(M)-E(M)^t)P_\lambda\\
 &=\sum_{n=1}^t {t\brack n}_Q M^{rn}a_0^nQ^{n(n-1)/2}
       (M^{-2mn}-1)C_M^{t-n}L^nP_\lambda.
 \end{split}
 \tag{11}
\]
Every index is below \(N\). In particular
\(\Delta(1)P_\lambda=0\) and the root arrow intertwines.
Writing \(C=C_1\), \(X=X_1\) and differentiating in
\(\mu=\log M\) gives
\[
 \left.\partial_\mu\Delta(e^\mu)P_\lambda\right|_0
 =-2m\left.\partial_s(C+sX)^tP_\lambda\right|_{s=1}.
 \tag{12}
\]
The derivatives of the other factors in (11) are multiplied by
\(M^{-2mn}-1=0\), so no normal has been omitted in (12).

## 3. The true flattened normal is one donor commutator

Source [W, (7)--(8)] supplies an analytic Cartan-preserving frame
\(G(M)\), with \(G(1)=I\), such that
\(G(M)^{-1}E(M)G(M)=E\). Its reduced normal is the derivative
of \(\widehat b(M)=G(M)^{-1}b(M)G(M)\), and its Ward arrow is
\([\widehat b'(1),E^t]P_\lambda\), with the derivative taken in
\(\mu\). More explicitly,
\[
 [\widehat b(M),E^t]=G(M)^{-1}[b(M),E(M)^t]G(M).
 \tag{13}
\]
At \(M=1\) the commutator on the right vanishes on \(P_\lambda\)
by (11). Since \(G\) preserves the input weight, its connection
terms vanish after that restriction when (13) is differentiated.
Also \([b(M),E(M)^t]=-b(M)\Delta(M)\). Therefore the actual
flattened normal, not an independently chosen lift, is
\[
 \mathfrak D_tP_\lambda
 =-b\left.\partial_\mu\Delta(e^\mu)P_\lambda\right|_0
 =2mb\left.\partial_s(C+sX)^tP_\lambda\right|_{s=1}.
 \tag{14}
\]
The scalar derivative of \(\kappa\) also multiplies the vanishing
root commutator, rather than being silently discarded.

The last derivative is explicitly diagonal. On the donor define
\[
 g_j(s)=\prod_{h=1}^j\frac{Q^{-h}-1}{sQ^{-h}-1}
             =\frac{F_j}{\prod_{h=1}^j(s-Q^h)},\qquad
 G_s|j\rangle=g_j(s)|j\rangle,\quad g_0=1.
 \tag{15}
\]
For each fixed level these are holomorphic and invertible near
\(s=1\), with \(G_1=I\). Their consecutive ratio proves
\[
 C+sX=G_sEG_s^{-1},\qquad
 \Gamma|j\rangle=\gamma_j|j\rangle,
 \quad \gamma_j=-\sum_{h=1}^j\frac1{1-Q^h},\quad\gamma_0=0,
 \qquad \Gamma=\left.\partial_sG_s\right|_1.
 \tag{16}
\]
The tail terms commute with this one-donor frame. The forced zero
arrow remains zero; no uniform \(s\)-collar is assumed. Equations
(14)--(16) prove the fixed-degree collapse
\[
 \boxed{\quad
 \mathfrak D_tP_\lambda=2mb[\Gamma,E^t]P_\lambda.
 \quad}
 \tag{17}
\]
It is also the ordered polynomial derivative
\(2mb\sum_{j=0}^{t-1}E^jXE^{t-1-j}P_\lambda\).
The diagonal \(\Gamma\) is the same for every physical order
and weight. No coefficient projection remains to be estimated
in (17).

For input donor occupation \(j\) and output \(j-n\), the entry
of this commutator is the corresponding entry of \(E^t\) times
\[
 \gamma_{j-n}-\gamma_j=\sum_{h=j-n+1}^j\frac1{1-Q^h},
 \qquad \operatorname{Re}(\gamma_{j-n}-\gamma_j)=n/2.
 \tag{18}
\]
All terms of \(E^t\) have donor loss \(n\ge0\). The loss-zero
entries in (17) vanish, and none of its positive-loss multipliers
is zero. These are exact root identities, not a replacement of
the co-source by a Hermitian norm.

## 4. The protected donor-loss-one component

Let \(J|j\rangle=j|j\rangle\) on the donor. Define the actual
matrix-entry projection
\[
 \mathsf R_1(T)=\frac1{2\pi}\int_0^{2\pi}
        e^{-i\phi}e^{-i\phi J}T e^{i\phi J}\,d\phi.
 \tag{19}
\]
It retains precisely donor occupation loss one. It is contractive
in physical operator norm and orthogonal in Hilbert--Schmidt norm.
The diagonal projector \(P_\lambda\) commutes with this degree
action, so input weights are not mixed by (19).

Put \([t]_Q=(1-Q^t)/(1-Q)\). In the coproduct
\(E=E_{\rm donor}K_{\rm T}+E_{\rm T}\), its two terms
\(Q\)-commute. The donor-loss-one part of \(E^t\) is consequently
\([t]_Q E_{\rm T}^{t-1}E_{\rm donor}K_{\rm T}\).
The loss-one multiplier in (18) cancels its donor coefficient:
\[
 \frac{Q^{-j}-1}{1-Q^j}=Q^{-j},\qquad
 \mathsf R_1([\Gamma,E^t])
                =[t]_Q E_{\rm T}^{t-1}X.
 \tag{20}
\]
Every term of \([\Gamma,E^t]\) has donor loss at least one.
Every term of \(S_r\) has nonnegative donor loss, and its zero-loss
term is the identity. Therefore in (17) the only contribution
to loss one is this zero-transfer term of the literal crossing.
Since \(XP_\lambda=a_0LP_\lambda\), the exact observed packet is
\[
 \boxed{\quad
 \mathsf R_1(\mathfrak D_tP_\lambda)
   =2m\kappa[t]_Q D E_{\rm T}^{t-1}XP_\lambda
   =2m\kappa a_0[t]_Q D E_{\rm T}^{t-1}LP_\lambda.
 \quad}
 \tag{21}
\]
There is also a short direct verification from the original sum (5).
Its terms with \(n\ge2\) have donor loss at least two. In its
\(n=1\) term, loss one forces the identity term of \(S_r\) and
the tail-only term of \(E^{t-1}\). Its scalar coefficient is
\(2ma_0F_t/[F_{t-1}(1-Q)]=2ma_0[t]_Q\), giving exactly (21).
Thus the selected-entry argument below does not depend on choosing
a flattening frame or estimating a diagonal meridian gauge.

All the higher transfers remain in the full matrix; they cannot
enter this particular entry projection. Because \(D\) is unitary,
(19)--(21) give in both of the stated physical norms
\[
 \|\mathfrak D_tP_\lambda\|
       \ge2m|\kappa|\,|[t]_Q|\,
                          \|E_{\rm T}^{t-1}LP_\lambda\|.
 \tag{22}
\]
There is no inverse or condition number of \(b\) in this inequality.

## 5. An explicit nonzero physical matrix entry

Write the actual weight as
\(\lambda=x_0^rQ^{-h}\), with \(0\le h<N\). Choose an input
with donor occupation \(j\), the next \(r-2\) occupations equal
to \(d\), and last-tail occupation \(A\). First set \(A=d\)
and solve
\[
                  j+(r-2)d+A\equiv h\pmod N,
                       \qquad 0\le j<N.
 \tag{23}
\]
If this gives \(j=0\), replace \(A\) by \(d-1\); the new
solution is \(j=1\). Thus in either case \(j>0\), the input
is in \(U_\lambda\), and \(A\ge t-1\).

In the output lower the donor to \(j-1\), the last tail head to
\(A-(t-1)\), and leave all other occupations unchanged. Exactly
one term of \(E_{\rm T}^{t-1}\) reaches that output: every lowering
is on the last head, so there is no later Cartan factor. Its coefficient
is \((-1)^{t-1}F_{t-1}\) for \(A=d\), and
\((-1)^{t-1}F_t/F_1\) for \(A=d-1\). Put
\(\delta_{j-1}=(-1)^{j-1}Q^{(j-1)j/2}\). The corresponding
entry of the full original \(\mathfrak D_tP_\lambda\) is exactly
\[
 2m\kappa a_0[t]_Q\delta_{j-1}(-1)^{t-1}
 \begin{cases}
 F_{t-1},&A=d,\\
 F_t/F_1,&A=d-1.
 \end{cases}
 \tag{24}
\]
Both phases \(a_0\) and \(\delta_{j-1}\) have modulus one.
All products have length below \(N\), including at \(t=N-1\).
For \(N=2,t=1\), the tail power and its product are empty,
and the same argument gives the specified nonzero entry.

Since \(|[t]_Q|\ge1\) for \(1\le t<N\) and
\([t]_QF_{t-1}=F_t/F_1\), either case of (24) proves
\[
 \boxed{\quad
 \|\mathfrak D_tP_\lambda\|_{\rm op},\quad
 \|\mathfrak D_tP_\lambda\|_{\rm HS}
       \ \ge\ \frac{2m|\kappa|\,|F_t|}{|1-Q|},
 \qquad r\ge2,\quad N\ge2,
 \quad}
 \tag{25}
\]
for every actual physical weight and order in (4). Equivalently the
normalized packet \(\mathfrak D_tP_\lambda/(2mF_t)\) has both norms
at least \(|\kappa|/|1-Q|\ge |\kappa|N/(2\pi)\).
No physical order, endpoint or meridian-normal direction was removed
to get this lower bound.

This estimates the actual degree-selected boundary normal packet,
not merely the matrix before its required coefficient observation.
The witnessing input is near occupation endpoints and has not been
identified with a geometric growing packet. The remaining source
functional in [W, (27)], its off-diagonal normal couplings, both
reciprocal arrows and any arbitrary short exterior stay in place.
They can annihilate or cancel matrix components even though (25)
holds. Exact negative-letter and word cocycles retain their actual
inverse and exterior factors. No general marked-scalar or geometric
volume lower bound follows from (25) alone.

More specifically, the Ward arrow has total integer degree loss
\(t>0\). For any degree-preserving exterior \(B_{\rm ext}\), its direct
ordinary trace \(\operatorname{Tr}(B_{\rm ext}\mathfrak D_tP_\lambda)\)
is zero. The original source is not that trace: [W, (24),(27)]
first reconstructs the normal blocks from both reciprocal arrows
and retains their diagonal and off-diagonal bilinear contractions.
The donor projection is not an invariant-preserving replacement of
that procedure. For a presentation with one boundary crossing,
the complete Markov contraction [W, (29)] still leaves the arbitrary
internal core and its unknown scalar; it is not a new nonvanishing
argument.

## Complete proof sources and coverage

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  549 lines, SHA256
  b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.
* R: notes/research_actual_reduced_braid_source.md, 330 lines, SHA256
  9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* W: notes/research_actual_word_normal_cocycle_and_source.md,
  458 lines, SHA256
  db453e02bc349e7740b2718b25819e9aa8ad1a71b86044fb7128524bea292106.
* Complete coverage: notes/research_boundary_ward_positive_toeplitz.md,
  338 lines, SHA256
  2df4811faadc585018011ef86e18d81cf0f8dc3745d05ac0f689d84f076979d9.

All four complete matching texts were read untruncated in the author
sequence. The Toeplitz proof controls the unprojected logarithmic
factor; it is not a premise for this selected-entry lower bound.
The whole-meridian conjugation, resonant derivative, one-donor
commutator and explicit physical observation are proved above.
This text is submitted for independent whole-text and whole-source
review. Only written mathematics and text/hash operations were used;
earlier frozen files were unchanged.
