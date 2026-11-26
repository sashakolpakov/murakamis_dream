# The exact top-column source quotient and its bounded section

Private written proof, 19 November 2026.

The actual top-column map has a complete linear image and kernel
description. Its image is the correct-weight commutant of the
literal lowering operator, and it has an explicit holomorphic right
inverse whose norm is at most \(|M|^{N-1}\). Consequently its
smallest nonzero coefficient-Hilbert--Schmidt singular value is
uniformly bounded below on every strict scaled meridian collar.
The source descends exactly through this linear quotient.

This bound concerns the top integral map. It is not a spectral gap
for the lowering operator or its commutator, and it does not estimate
a geometric source coefficient. The sole complete direct is T,
the actual top-column integral and bounded-source theorem, pinned below.

## 1. Actual map and the endpoint partition

Use T's physical fixed-root family, with
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad M=e^\mu,\quad x=-M/q.
 \tag{1}
\]
The remaining tensor \(U=V\otimes Z\) has \(r\ge1\) heads.
Its ordered total generators are \(E,K\), with
\(KE=QEK\), \(E^N=0\), and \(g=K^{-d}\).
The physical endpoints \(\iota_a,\pi_a\) refer to \(V\).
For \(r=1\), put \(Z=\mathbb C\) and \(K_Z=1\). Set
\[
 \eta_d=(-1)^dD_N(M),\qquad
 \mathcal B=\iota_d K_Z^{-d}\pi_0,
 \qquad \delta X=[E,X].
 \tag{2}
\]
Here \(D_N(M)=(M^N-M^{-N})/(M-M^{-1})\), with its removable
continuation at \(M=\pm1\), in particular \(D_N(1)=N\).
We work wherever \(\eta_d\ne0\), in particular throughout
\(|N\mu|<\eta<\pi\). T proves the exact physical partition
\[
                    \sum_{k=0}^d E^{d-k}\mathcal B E^k
                                      =\eta_d I_U.
 \tag{3}
\]
It retains every finite cap; its proof uses the endpoint invariance
of the lowering frame, not a bound for that frame.

Define the finite integral on all remaining-head matrices by
\[
 \mathcal P(Z)=\eta_d^{-1}\sum_{k=0}^dE^kZE^{d-k}.
 \tag{4}
\]
Let
\[
 \mathcal A_j=\{X:KX=Q^jXK\},\quad
 \mathcal A=\mathcal A_0,
 \qquad
 \mathcal Y=\{Y\in\mathcal A_d:[E,Y]=0\}.
 \tag{5}
\]
The weight spaces \(\mathcal A_j\) are independent of \(\mu\),
since \(K(\mu)=M^rK(0)\). T identifies the actual top-column map
of physical highest-block completion as
\[
       \mathcal C(H)=C_d(H)=\mathcal P(gH),\qquad H\in\mathcal A,
       \qquad \tau(H)=\operatorname{Tr}_U(gH).
 \tag{6}
\]
Thus all statements below concern this literal capped map, rather
than a replacement built from an unknown scalar source.

## 2. Exact image and a bounded physical right inverse

Nilpotence gives, by telescoping the sum in (4),
\[
                        \delta\mathcal P=0,
                          \qquad \mathcal P\delta=0.
 \tag{7}
\]
Also \(\mathcal P(\mathcal A_0)\subset\mathcal A_d\).
Consequently \(\mathcal C(H)\in\mathcal Y\).
Conversely, if \([E,Y]=0\), the partition (3) implies
\[
 \mathcal P(\mathcal B Y)
   =\eta_d^{-1}\sum_{k=0}^dE^k\mathcal B E^{d-k}Y=Y.
 \tag{8}
\]
Since \(K\mathcal B=Q\mathcal B K\),
\(\mathcal B Y\) has weight zero when \(Y\in\mathcal Y\).
Therefore an actual right inverse of (6) is
\[
 \boxed{\quad
 \mathcal R(Y)=g^{-1}\mathcal B Y
       =x^dQ^{-1}\iota_d\pi_0Y,\qquad
 \mathcal C\mathcal R(Y)=Y.
 \quad}\tag{9}
\]
For the second equality, the first remaining head has Cartan
eigenvalue \(xQ^{-d}\) at \(d\). Thus
\(K^d\iota_dK_Z^{-d}\pi_0
 =x^dQ^{-d^2}\iota_d\pi_0\), and \(Q^{-d^2}=Q^{-1}\).
Every spectator Cartan has canceled. In particular
\[
                         \operatorname{im}\mathcal C=\mathcal Y.
 \tag{10}
\]
No dimension count, division by a resonant Cartan eigenvalue, or
conditioning estimate for a string decomposition is used.

Give all physical coefficient bases their Euclidean metrics.
The arrow \(\iota_d\pi_0\) has operator norm one. For every
Schatten norm \(1\le p\le\infty\), (9) gives
\[
                  \boxed{\quad
                  \|\mathcal R(Y)\|_p\le |M|^d\|Y\|_p.
                  \quad}\tag{11}
\]
At \(M=1\) the section is a contraction. On
\(|N\mu|\le\eta\), its norm is at most \(e^\eta\), independently
of both \(N\) and the fixed number of heads.

## 3. A finite homotopy and the exact kernel

Define on all remaining-head matrices the explicit finite map
\[
 \mathfrak h(Z)=\eta_d^{-1}
   \sum_{a=1}^d\sum_{j=0}^{a-1}
        E^{a-1-j}\mathcal B E^{d-a}ZE^j.
 \tag{12}
\]
It satisfies the operator identity
\[
 \boxed{\qquad
            \delta\mathfrak h(Z)=Z-\mathcal B\mathcal P(Z).
 \qquad}\tag{13}
\]
Indeed, for \(T_a=\mathcal B E^{d-a}Z\), the commutator of
\(E\) with the inner sum in (12) telescopes to
\([E^a,T_a]\). Summing over \(a\), inserting the harmless
zero term at \(a=0\), and using (3), gives
\[
 \eta_d\delta\mathfrak h(Z)
   =\sum_{a=0}^d E^a\mathcal B E^{d-a}Z
       -\mathcal B\sum_{a=0}^dE^{d-a}ZE^a
   =\eta_d Z-\eta_d\mathcal B\mathcal P(Z).
 \tag{14}
\]
The same finite sum also gives the complementary identity
\[
                  \mathfrak h\delta(Z)=Z-\mathcal P(\mathcal B Z).
 \tag{14a}
\]
To check it, write \(p=a-1-j\), \(q=j\) in (12).
After inserting \(EZ-ZE\), terms with positive \(q\) cancel
between adjacent pairs. The two remaining edges are
\(\sum_{p=0}^dE^p\mathcal B E^{d-p}Z\) and
\(\sum_{p=0}^dE^p\mathcal B Z E^{d-p}\), giving (14a) by (3).
Every power and every sum is finite. If \(Z\) has weight zero,
then \(\mathfrak h(Z)\) has weight \(Q^{-1}=Q^d\): the total
number of \(E\)'s in each term is \(d-1\), and \(\mathcal B\)
has weight \(Q\). Equations (7),(13) therefore prove
\[
 \boxed{\quad
 \ker\mathcal C
       =g^{-1}\delta(\mathcal A_d),\qquad
 H=\mathcal R(\mathcal C H)
                         +g^{-1}\delta\mathfrak h(gH).
 \quad}\tag{15}
\]
In particular the following two-periodic complex of actual Cartan
weight spaces is exact at both terms:
\[
 \cdots\longrightarrow\mathcal A_d
   \xrightarrow{\ \delta\ }\mathcal A_0
   \xrightarrow{\ \mathcal P\ }\mathcal A_d
   \xrightarrow{\ \delta\ }\mathcal A_0\longrightarrow\cdots .
 \tag{16}
\]
Exactness at \(\mathcal A_0\) is (13), and exactness at
\(\mathcal A_d\) is the explicit section (8).

Integer occupation degrees are not identified modulo \(N\).
If a matrix raises total occupation by \(\ell\), then
\(\delta\) lowers that degree by one, \(\mathcal P\) lowers it
by \(d\), \(\mathcal B\) raises it by \(d\), and
\(\mathfrak h\) raises it by one. Thus for an exact degree-zero
seed, \(Y=\mathcal C H\) has degree \(-d\),
\(\mathcal R(Y)\) has degree zero, and the commutator primitive
\(\mathfrak h(gH)\) has degree \(+1\).
The homogeneous restrictions of (13),(15) are exact with these
shifts; (16) is periodic in root weight, not in unshifted integer degree.

## 4. The quotient norm and the top-map singular gap

For any \(H\in\mathcal A\), (15) makes
\(H-\mathcal R(\mathcal C H)\) an actual element of the kernel.
Consequently, for every Schatten norm,
\[
 \boxed{\quad
 \operatorname{dist}_p(H,\ker\mathcal C)
                         \le |M|^d\|\mathcal C H\|_p.
 \quad}\tag{17}
\]
This holds on the exact integer-degree-zero subspace as well,
with its corresponding kernel and image.

For \(p=2\), give \(\mathcal A\) and its image the inherited
coefficient-Hilbert--Schmidt inner products. On the orthogonal
complement of its kernel, the distance in (17) equals \(\|H\|_2\).
Therefore the smallest nonzero singular value of the literal map is
\[
 \boxed{\qquad
                \sigma_{\min}^{+}(\mathcal C)\ge |M|^{-d}
                                      \ge e^{-\eta}
                \quad (|N\mu|\le\eta).
 \qquad}\tag{18}
\]
The assertion includes all widths \(r\ge1\). It is a gap for
\(\mathcal C\) restricted to its image, not a lower bound for
\(E\) or \(\delta\) on their nonzero singular spaces.

Neither (11) nor (18) bounds the forward norm of \(\mathcal C\)
or the homotopy (12) polynomially. The latter contains extensive
powers of the actual \(E\). The direct triangle estimate is
\[
 \|\mathfrak h(Z)\|_p\le
  \frac{d(d+1)}{2|\eta_d|}\|\mathcal B\|
                          \|E\|^{d-1}\|Z\|_p,
 \tag{19}
\]
which can have exponential cost at fixed width. This is compatible
with the bounded section: solving the integral quotient and solving
its commutator primitive are different quantitative problems.

## 5. Holomorphic section, true jets, and the retained source

The spaces of allowable seeds \(\mathcal A\) are fixed in \(\mu\).
All finite maps above are holomorphic on the stated collar, and the
right inverse (9) is a holomorphic formula even on the ambient
matrix space. For a holomorphic compatible family \(Y(\mu)\),
\[
 \partial_\mu^k\mathcal R_\mu(Y(\mu))
   =x^dQ^{-1}\iota_d\pi_0
                              (\partial_\mu+d)^kY(\mu).
 \tag{20}
\]
Thus the section's fixed true meridian jets have polynomial cost.
In the scaled coordinate \(u=N\mu\), the last operator is
\(N^k(\partial_u+d/N)^k\); buffered Cauchy estimates give the
same conclusion for uniformly bounded holomorphic families.
The \(\mu\)-dependence of the compatible space \(\mathcal Y\)
through the actual \(E(\mu)\) is retained, not frozen.

T's original source formula becomes the exact descended functional
\[
 \boxed{\quad
 \tau(H)=\lambda(\mathcal C H),\qquad
 \lambda(Y)=\operatorname{Tr}_U(\mathcal B Y),\qquad
 \tau(\mathcal R(Y))=\lambda(Y).
 \quad}\tag{21}
\]
The difference in (15) contributes
\(\operatorname{Tr}[E,\mathfrak h(gH)]=0\).
This is a holomorphic identity, so all true meridian jets also
vanish for this difference. Differentiation retains the actual
terms \([E',X]+[E,X']\); neither moving term is discarded.
All scalar lines and the derivative of \(\mathcal B\) remain as
in T. In particular \(\mathcal B'=-(r-1)d\mathcal B\).

The chosen representative in (9) is supported on the first remaining
output row \(d\). Its physical coherent kernel consequently has
that output monomial factor. The bounded section therefore supplies
no ordinary low-output seed unit, no factorial-gauge endpoint
asymptotic, and no geometric window merely by a change of coordinates.
The quotient (15) is linear and source-compatible; it is not an
identification with a reduced geometric critical algebra.

More explicitly, each compatible top operator has the affine fiber
\[
 \{H\in\mathcal A:\mathcal C H=Y\}
             =\mathcal R(Y)+g^{-1}\delta(\mathcal A_d).
 \tag{22}
\]
Thus its finite-level lifting torsor is explicitly split, and the
original source is constant on it. At fixed \(N\), the section is
Laurent monomial in \(M\) and is regular on the admissible algebraic
base \(M\ne0,\eta_d(M)\ne0\). This also gives the displayed lift
for any holomorphic compatible family. This \(N\)-dependent linear
construction is not a fixed A-polynomial torsor or a geometric period.

Finally, \(\lambda(Y)\) is one prescribed bilinear contraction.
Its bounded observer does not make it nonzero on a specified actual
word, and (18) gives no lower bound for that scalar from \(\|Y\|\).
No volume-conjecture case or source-cycle coefficient is inferred.

Complete proof direct:

* **T:** notes/research_top_column_integral_and_bounded_source.md,
  277 lines, SHA256
  2bb41be20d0541ed480f07f10b394560fb9676d290c28f5c20ce001fe83baa4f.

Only written mathematics and text operations are used. Frozen notes
and public manuscripts are unchanged. The entire matching final and
the complete direct T were freshly whole-read nontruncated in this
author sequence. Every used implication was checked, and both pins
were renewed after the final changes. Independent matching review
and parent adoption remain separate.
