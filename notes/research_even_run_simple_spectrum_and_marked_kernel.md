# The simple spectral curve and the marked kernel of an even run

Research note, 3 November 2026.

The backward equation of an even crossing run has a globally simple
classical spectrum on its color circle. Its full quantum period also
has simple spectrum at the physical reset. The original source is
exactly the zero-eigenvalue line of that period, with an explicit
normalization. This identifies a particular quantum eigenline and
its marked section; its growth away from the reset remains to be
estimated.

All coordinates here are the auxiliary color coordinates of the
original Newton source. No identification with peripheral holonomy
coordinates is assumed.

## 1. A Jacobi matrix with a complex boundary parameter

Let \(T_k\) be adjacency on the path with \(k\) vertices, and let
\(E_{aa}\) have a single nonzero entry, equal to one, in position
\((a,a)\). Define
\[
 J_k(s)=T_k+E_{kk}+sE_{11},\qquad
 P_0(x)=1,\quad P_1(x)=x-1,\quad
 P_n(x)=xP_{n-1}(x)-P_{n-2}(x).
 \tag{1}
\]
For \(k=1\), both diagonal modifications belong to the same entry,
so \(J_1(s)=1+s\). Expanding the first diagonal modification gives
\[
 \det(xI-J_k(s))=P_k(x)-sP_{k-1}(x).
 \tag{2}
\]
The polynomials are the monic rescaling of the Chebyshev polynomials
of the third kind:
\[
 P_n(2\cos\omega)
     =\frac{\cos((n+\tfrac12)\omega)}{\cos(\omega/2)}.
 \tag{3}
\]
This is the classical identity recorded in
[DLMF 18.5.3](https://dlmf.nist.gov/18.5.E3); alternatively (3)
follows immediately from the recurrence and its two initial values.
The result below concerns a complex coefficient \(s\), and is
proved directly.

**Theorem 1.** The matrix \(J_k(s)\) has \(k\) distinct eigenvalues
for every \(|s|\le1\). There is a number \(R_k>1\) and holomorphic
eigenvalues \(\mu_0(s),\ldots,\mu_{k-1}(s)\) on \(|s|<R_k\),
distinct throughout that disk, with
\[
 \mu_j(1)=2\cos(j\pi/k),\qquad 0\le j<k.
 \tag{4}
\]
Every eigenvector has nonzero first and last coordinates. The
normalization with last coordinate one is the explicit vector
\[
 v_j(s)=\bigl(P_{k-1}(\mu_j(s)),P_{k-2}(\mu_j(s)),
                         \ldots,P_0(\mu_j(s))\bigr)^T.
 \tag{5}
\]
In particular these vectors form a holomorphic invertible frame,
with the frame, its inverse, and their derivatives bounded on
every smaller closed disk.

*Proof.* The case \(k=1\) is immediate. Suppose first that
\(\operatorname{Im}s>0\). For an eigenpair \(J_k(s)v=xv\), the
Hermitian inner product gives
\[
       \operatorname{Im}x\,\|v\|^2
                   =\operatorname{Im}s\,|v_1|^2>0.
 \tag{6}
\]
The strict inequality follows because the tridiagonal recurrence
would make the entire vector zero if \(v_1=0\). Thus every
eigenvalue lies in the upper half-plane, irrespective of its
algebraic multiplicity.

Write \(x=z+z^{-1}\), choosing the unique root with \(|z|<1\).
Then \(z=re^{-i\omega}\), where \(0<r<1\) and \(0<\omega<\pi\).
The denominator in the following expression is nonzero, and
(2)--(3) give
\[
        s=\frac{1+z^{2k+1}}{z(1+z^{2k-1})}.
 \tag{7}
\]
Indeed consecutive \(P_n\)'s have no common zero, by their
recurrence. The assumption \(|s|\le1\), after squaring (7), is
\[
 4r^{2k+1}\sin(2k\omega)\sin\omega
            \ge(1-r^2)(1-r^{4k})>0.
 \tag{8}
\]
Consequently every root belongs to one of the \(k\) disjoint
open angular sectors
\[
       \frac{j\pi}{k}<\omega<\frac{(2j+1)\pi}{2k},
                       \qquad j=0,\ldots,k-1.
 \tag{9}
\]

For \(s=i\varepsilon\) with \(\varepsilon>0\) small, there is
one root in each sector. To see this, at \(s=0\) the simple roots
of \(P_k\) have angles \((2j+1)\pi/(2k+1)\), strictly between
the bounds in (9). Under the small perturbation, (6) moves each
root off the real axis while preserving its sector.

Now follow any path from this parameter to any other point with
\(\operatorname{Im}s>0\) and \(|s|\le1\). The eigenvalues remain
bounded. On a compact such path they cannot approach the real
axis: any limiting eigenpair would contradict (6) and the
nonvanishing first coordinate. Thus the associated \(z\)'s
stay away from both zero and the unit circle. Inequality (8)
prevents a sector crossing. The number of roots in each sector,
counted with algebraic multiplicity, is therefore constant and
equals one. This proves simplicity, including the nonreal part
of \(|s|=1\), without assuming simplicity along the path.

Conjugation handles the lower half-plane. For real \(s\), the
matrix is a real symmetric irreducible Jacobi matrix. Its
eigenspace for any eigenvalue has dimension at most one by the
same recurrence, and symmetry gives algebraic simplicity.

The discriminant of (2) is a polynomial in \(s\), nonzero on
the closed unit disk. It has no zero on some larger disk
\(|s|<R_k\). The roots therefore have single-valued holomorphic
labels there, since the disk is simply connected. At \(s=1\),
the elementary Neumann path spectrum gives (4). Starting from
the last coordinate and applying the eigenvector recurrence
gives (5). No eigenvector can have last coordinate zero. Distinct
eigenvalues make the frame invertible; equivalently its
determinant is a nonzero Vandermonde determinant, up to sign,
because the \(P_n\)'s are monic of successive degrees. Compactness
and holomorphy give the asserted bounds. \(\square\)

For the classical backward matrix in the
[actual source equation](research_even_run_backward_source_growth.md),
\[
 H(\theta)=2\cos\theta\,I-T_k-e^{-i\theta}E_{11}-E_{kk},
 \tag{10}
\]
the eigenvalues are therefore
\(2\cos\theta-\mu_j(e^{-i\theta})\). They remain distinct
throughout the color circle. Their moduli need not be ordered
in the same way throughout it. Theorem 1 proves separation of
eigenvalues, not persistence of a dominant modulus.

## 2. The exact backward quantum period

Fix an even crossing power \(2k\) and a level \(N\ge2\). Put
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad D=N-1,\qquad
 \epsilon=(-1)^N,\qquad X=x^N,
\]
and, for nonzero \(x\), define
\[
 \begin{split}
 C_k(r)&=(r+r^{-1})I-T_k-rE_{11},\\
 H_j(x)&=C_k(qQ^jx)-q^{-1}E_{kk},\\
 B_N(x)&=H_0(x)H_1(x)\cdots H_{N-1}(x),\\
 H^{\rm cl}(X)&=C_k(X)-E_{kk}
                  =(X+X^{-1})I-J_k(X).
 \end{split}
 \tag{11}
\]
The order of the product is part of the definition. It is the
backward period, not the ordered product of the forward inverses.

**Theorem 2.** The characteristic polynomial satisfies the exact
identity
\[
        \det(tI-B_N(x))
                =\det(tI-\epsilon H^{\rm cl}(x^N)).
 \tag{12}
\]
Moreover
\[
        G_N(x)=B_N(x)-\epsilon(x^N+x^{-N})I
 \tag{13}
\]
is a polynomial matrix of degree at most \(N\). Its eigenvalues
on \(|x|<R_k^{1/N}\) are the distinct functions
\(-\epsilon\mu_j(x^N)\), including at \(x=0\).

*Proof.* Set \(w(z)=(1-z)(1-z^{-1})\). The original forward
transfer is \(w(Q^jx)H_j(x)^{-1}\) wherever this inverse
exists. Since \(\prod_{j=0}^{N-1}w(Q^jx)=w(x^N)\), its
ordered full product is
\[
                 U_N(x)=w(x^N)B_N(x)^{-1}.
 \tag{14}
\]
The [resonant characteristic theorem](research_resonant_source_monodromy_characteristic.md)
identifies its characteristic polynomial with that of
\(\epsilon w(X)H^{\rm cl}(X)^{-1}\). Taking reciprocal
eigenvalues proves (12) on the nonempty regular set. Both sides
are Laurent-polynomial expressions, so (12) holds everywhere
with \(x\ne0\), including all physical resets.

To prove the entrywise assertion (13), define
\[
 K(z)=I-qzT_k-zE_{kk}+q^2z^2(I-E_{11}),\qquad
 F(x)=K(x)K(Qx)\cdots K(Q^{N-1}x).
 \tag{15}
\]
Factoring the scalar from each \(H_j\) gives
\(B_N(x)=\epsilon x^{-N}F(x)\). Near zero \(K\) is invertible,
and the exact cyclic product identity gives
\[
                F(Qx)=K(x)^{-1}F(x)K(x).
 \tag{16}
\]
Write \(F(x)=I+\sum_{h\ge1}F_hx^h\). Inductively, if all
earlier coefficients vanish, the coefficient of \(x^h\) in
(16) is \((Q^h-1)F_h=0\). Since \(Q\) has order \(N\),
\(F_h=0\) for \(1\le h<N\). The matrix \(F-I\) is thus
divisible by \(x^N\). Also \(\deg F\le2N\), proving (13)
and its degree bound. Subtracting the scalar in (12) proves the
asserted characteristic polynomial of \(G_N\), first away from
zero and then at zero. Theorem 1 gives simplicity. \(\square\)

The spectral projections are consequently the holomorphic matrices
\[
 \Pi_{j,N}(x)=
  \prod_{r\ne j}
   \frac{G_N(x)+\epsilon\mu_r(x^N)I}
        {\epsilon(\mu_r(x^N)-\mu_j(x^N))}.
 \tag{17}
\]
They are rank-one idempotents and sum to the identity. Equation
(16), or the corresponding cyclic identity for \(B_N\), gives
their exact transport law
\[
       \Pi_{j,N}(x)H_0(x)=H_0(x)\Pi_{j,N}(Qx).
 \tag{18}
\]
This equality extends across a singular \(H_0\); no inverse of
that matrix is required in (18).

## 3. The physical kernel and its marked normalization

Use the original source vectors
\[
 (u_0)_a=q^{k-a},\qquad
 H_j(1)u_j=d_ju_{j-1},\qquad
 d_j=4\sin^2(\pi j/N),\quad 1\le j\le D.
 \tag{19}
\]
The coefficients of the crossing column are
\((M^{2k}e_0)_j=\kappa^{2k}e_k^Tu_j\), with the original
unit scalar \(\kappa=\exp(\pi iD^2/(2N))\). These equations
retain the full original source; all \(H_j(1)\), \(1\le j\le D\),
are invertible.

**Theorem 3.** At the physical reset,
\[
 \ker B_N(1)=\mathbb C u_D,\qquad
 u_0^Tu_D=\frac{\epsilon kN}{q},\qquad
 \Pi_{0,N}(1)=\frac{q}{\epsilon kN}u_Du_0^T.
 \tag{20}
\]
Here \(T\) means transpose, without complex conjugation. In
particular the original state is recovered exactly from the
marked projector column:
\[
                      u_D=\frac{\epsilon kN}{q}\Pi_{0,N}(1)e_k.
 \tag{21}
\]

*Proof.* The source equations and the sine product give
\[
 H_1(1)\cdots H_D(1)u_D=N^2u_0,
       \qquad H_0(1)u_0=0.
 \tag{22}
\]
The matrix \(H_0(1)\) has rank \(k-1\), and all other factors
are invertible. Thus the right kernel of \(B_N(1)\) is the
nonzero line generated by \(u_D\). Symmetry of \(H_0(1)\)
also gives the left kernel \(\mathbb C u_0^T\).

By (12), the eigenvalues of \(B_N(1)\) are
\(\epsilon\lambda_j\), where
\(\lambda_j=4\sin^2(\pi j/(2k))\), \(0\le j<k\).
Zero is simple and the product of the other eigenvalues is
\(\epsilon^{k-1}k\). Hence \(u_0^Tu_D\ne0\), and
\[
 \operatorname{adj}B_N(1)
       =\epsilon^{k-1}k\,\frac{u_Du_0^T}{u_0^Tu_D}.
 \tag{23}
\]
On the other hand, (12) gives
\[
 \det B_N(x)=\epsilon^k X^{-k}(1-X),\qquad
                (\det B_N)'(1)=-\epsilon^k N.
 \tag{24}
\]
In differentiating the matrix product, every term except the
derivative of its first factor vanishes after multiplication
on the left by \(u_0^T\). Equation (22) therefore gives
\[
 u_0^TB_N'(1)u_D
       =N^2u_0^TH_0'(1)u_0=-N^2/q.
 \tag{25}
\]
The last equality is the finite telescoping identity
\[
 (q-q^{-1})\sum_{a=0}^{k-1}q^{2a}-q^{2k-1}=-q^{-1}.
 \tag{26}
\]
It holds even when the sum on the left vanishes. Using
\((\det B)'=\operatorname{tr}(\operatorname{adj}B\,B')\)
in (23)--(25) proves the middle identity in (20). The projector
formula and (21) follow, since the last coordinate of \(u_0\)
is one. \(\square\)

Every intermediate source vector belongs to the same labeled
projector along the physical orbit:
\[
          u_j\in\operatorname{im}\Pi_{0,N}(Q^{j+1}),
                         \qquad 0\le j\le D.
 \tag{26a}
\]
Indeed the cyclic period at \(Q^{j+1}\) has its rightmost
segment \(H_0(1)\cdots H_j(1)\), which annihilates \(u_j\)
by (19). Its zero eigenspace is simple by (12). The scalar
relations (19), together with \(u_0\), give the original
normalization at every point of this orbit. Holomorphic extension
of the projectors is not an assertion that the same normalized
source equation has a nonzero solution at arbitrary clocks.

The Euclidean operator norm at this reset is particularly explicit:
\[
          \|\Pi_{0,N}(1)\|_2
                    =\frac{\|u_D\|_2}{\sqrt{k}\,N}.
 \tag{27}
\]
For fixed \(k\ge2\), the
[proved endpoint asymptotic](research_even_run_backward_source_growth.md)
therefore gives
\[
 \lim_{N\to\infty}\frac{\|\Pi_{0,N}(1)\|_2^2}{N}
       =\frac4k\sum_{r=1}^{k-1}r^2
                                  \cos^2\frac{\pi r}{2k}>0.
 \tag{28}
\]
For \(k=1\) the projector is the identity, of norm one.

## 4. What is resolved and what remains

The original source is now a specified section of a simple quantum
eigenline. The projectors extend holomorphically across the entire
auxiliary disk, including its center; the physical reset has an
exact nonzero marked normalization. No eigenvalue collision is
responsible for the remaining even-run growth problem.

Holomorphic projectors can still have large norms, and distinct
eigenvalues can exchange their modulus ordering. Equation (18)
does not bound the selected section on an arc of the color circle.
The original intermediate coefficients are obtained by transporting
that section through a proper part of the period and restoring the
original sine factors. Their sharp global growth rate still needs
proof. Joining several runs also retains a coherent pairing of
their marked sections. Neither a volume identity for an untreated
knot nor finite-exception coverage follows from (12) or (20)
alone.

The Chebyshev representation is classical. The arguments here
establish the sector count, the entrywise polynomial shift, and
the original-source normalization explicitly; no novelty claim
about general Jacobi-matrix perturbation theory is needed.

## 5. Reproducing the finite identities

The [focused diagnostic](../experiments/check_even_run_simple_spectrum_and_marked_kernel.py)
checks the classical determinant, sector assignments and explicit
eigenvectors. It constructs the coefficients of the quantum matrix
product before evaluation, checking their low-degree cancellation
and cyclic identity. At complex clocks, including zero, it checks
the characteristic polynomials, projectors and their transport.
At the physical reset it compares the marked section with the full
original crossing column and checks its bilinear normalization.

The [120-digit record](../repro/results/research-even-run-simple-spectrum-and-marked-kernel.json)
contains 66 classical parameter cases and 48 quantum cases with
\(N=2,\ldots,9\) and \(k=1,\ldots,6\). Ten of these have
\(k>N\). It checks 216 vanishing coefficients, 672 cyclic
coefficient identities, 240 complex-clock/projector cases and
264 original-source colors. The maximum relative residual is
\(8.479849990321062\cdot10^{-117}\).

Run it with

    python3 experiments/check_even_run_simple_spectrum_and_marked_kernel.py \
      --precision 120 \
      --output repro/results/research-even-run-simple-spectrum-and-marked-kernel.json

These checks concern normalization and implementation. The sector
argument proves simplicity for every parameter in the disk, and
the polynomial identities above prove the all-level assertions.
No large-level growth law is inferred from the finite diagnostic.
