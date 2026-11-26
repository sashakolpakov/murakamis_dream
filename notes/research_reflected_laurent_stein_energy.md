# The exact Green energy of a reflected Laurent source

Research note, 3 November 2026.

For opposite even crossing powers, the marked Laurent equation has
an exact matrix Stein equation. For \(N\ge2k\), its Green matrix
at the physical reset is positive definite and its inverse has a
polynomial bound in the level. This retains the original closing source and every
channel of its resonant transfer.

The same matrix does not remain positive around the auxiliary clock
circle. Its inertia is determined by the stable and unstable
subspaces of the actual run monodromy. For every rank at least two,
even the Laurent numerator is indefinite on an open part of that
circle. Thus its physical positivity cannot be promoted to a
globally positive Fourier symbol.

These statements give an exact energy identity and a quantitative
bound for this original source. They do not give its sharp
exponential rate or a theorem for a general signed closing word.

The matrix-equation method is classical. P. Stein's
[Some General Theorems on Iterants](https://nvlpubs.nist.gov/nistpubs/jres/048/jresv48n1p82_A1b.pdf),
J. Res. Natl. Bur. Stand. 48 (1952), 82--83, relates decay of
matrix iterates to positivity of a Hermitian difference
\(H-B^*HB\). Here the additional work is to obtain the equation
from the original marked knot source, retain its observation term,
and establish the stated bounds and indefinite arcs. The necessary
matrix arguments are included below.

## 1. The marked row as a matrix

Fix \(k\ge1\), the original pair \((a,b)=(2k,-2k)\), and
\[
 N\ge2,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad D=N-1.
 \tag{1}
\]
Use the complete original transfers from
[the two-run source construction](research_two_run_source_transfer.md).
At an auxiliary clock \(x\), put
\[
 T_j(x)=\mathcal T_{2k}(0;Q^jx),\qquad
 Z_0(x)=I,\qquad Z_j(x)=T_{j-1}(x)\cdots T_0(x)
                    \quad(1\le j\le N),
 \qquad P(x)=Z_N(x).
 \tag{2}
\]
All these matrices are the polynomial extensions of the resonant
source transfer; no denominator is deleted at its reset.
Let \(E=e_ke_k^T\). On \(|x|=1\), the signed tensor transfer
is exactly \(T_j(x)\otimes\overline{T_j(x)}\).
The marked affine row of
[the Laurent numerator theorem](research_two_run_marked_laurent_numerator.md)
is
\[
 h_N(x)=r_N(x)\bigl(I-P(x)\otimes\overline{P(x)}\bigr)^{-1}.
 \tag{3}
\]
Here and below, conjugation in a formula on the unit circle describes
the restriction of the holomorphic signed-clock expression. It is
not an antiholomorphic definition off that circle.

Reshape this row into a \(k\times k\) matrix \(G_N(x)\) by
\[
 (G_N(x))_{ba}=(h_N(x))_{(a,b)}.
 \tag{4}
\]
Thus \(h_N(x)(v\otimes\bar v)=v^*G_N(x)v\). Define the finite
output Gram matrix
\[
 R_N(x)=\sum_{j=1}^N Z_j(x)^*E Z_j(x).
 \tag{5}
\]
The original accumulator row satisfies
\(r_N(x)(v\otimes\bar v)=v^*R_N(x)v\).

Write
\[
 d_k(X)=\mathcal D_{2k,-2k}(X),\qquad
 \det\bigl(I-P(x)\otimes\overline{P(x)}\bigr)=d_k(x^N).
 \tag{6}
\]
The second equality is the proved
[resonant source characteristic identity](research_resonant_source_monodromy_characteristic.md).
In particular \(d_k(1)=1\).

**Proposition 1.** At every unit clock where \(d_k(x^N)\ne0\),
\(G_N(x)\) is the unique solution of
\[
 \boxed{\qquad
       G_N(x)-P(x)^*G_N(x)P(x)=R_N(x).
 \qquad}                                                     \tag{7}
\]
It is Hermitian. Its one-step version, with the same original output,
is
\[
 G_N(x)=T_0(x)^*\bigl(G_N(Qx)+E\bigr)T_0(x).
 \tag{8}
\]

*Proof.* The defining identity \(h_N(I-U_N)=r_N\), evaluated
on \(v\otimes\bar v\), gives (7). The nonsingularity in (6)
gives uniqueness on all \(k\times k\) matrices. Taking adjoints
in (7) shows that \(G_N^*\) solves the same equation, so uniqueness
makes \(G_N\) Hermitian. The exact affine relation
\(h_N(Qx)A(x)=h_N(x)-c^TA(x)\) gives (8).
This derives the equations from the marked original row, rather
than introducing a different positive invariant. \(\square\)

## 2. Quantitative observation of the full channel state

The following constant is deliberately conservative:
\[
       K_k=k\,4^{\,k(k-1)/2+k-1}.
 \tag{9}
\]
For a trajectory \(v_{j+1}=T_j(x)v_j\) at a unit clock, put
\[
 \xi_j=Q^jx,\quad r_j=q\xi_j,\quad
 H_j=C_k(r_j)-q^{-1}E,\quad
 \delta_j=(1-\xi_j)(1-\xi_j^{-1}).
 \tag{10}
\]
The original implicit channel equations are exactly
\[
             H_jv_{j+1}=\delta_jv_j.
 \tag{11}
\]
They include all first-normal source data. On the unit circle,
\(0\le\delta_j\le4\), and \(\|H_j\|_2\le4\), since the
complex symmetric tridiagonal matrix has absolute row and column
sums at most four.

**Lemma 2.** For every integer \(L\ge k\),
\[
 \|v_L\|_2^2
       \le K_k^2\sum_{j=L-k+1}^{L}|e_k^Tv_j|^2.
 \tag{12}
\]
Consequently, if \(mN\ge k\), and
\[
 R_N^{[m]}=\sum_{\nu=0}^{m-1}(P^*)^\nu R_NP^\nu,
 \tag{13}
\]
then
\[
          R_N^{[m]}\ \ge K_k^{-2}(P^m)^*P^m .
 \tag{14}
\]

*Proof.* The rows
\[
 e_k^T,\quad e_k^TH_{L-1},\quad
 e_k^TH_{L-2}H_{L-1},\quad\ldots,\quad
 e_k^TH_{L-k+1}\cdots H_{L-1}
 \tag{15}
\]
form an observation matrix of determinant one. Row \(h\), starting
at \(h=0\), has leftmost nonzero entry \((-1)^h\) in column
\(k-h\). The column-reversal sign cancels the product of these
entries. Its row norms are at most \(4^h\), so Hadamard's
cofactor bound gives inverse norm at most
\(k4^{k(k-1)/2}\).
Equation (11) identifies its \(h\)-th observed component with
\((\prod_{\nu=1}^h\delta_{L-\nu})e_k^Tv_{L-h}\).
These multipliers are at most \(4^{k-1}\). This proves (12)
without dividing by any \(\delta_j\).

Apply (12) at \(L=mN\) to an arbitrary initial vector.
The left side is \(\|P^mv_0\|^2\); the complete output energy
through time \(mN\) is \(v_0^*R_N^{[m]}v_0\) and contains
the required final observation window. This proves (14).
\(\square\)

This is the same exact observation mechanism used for the actual
coefficient localization in
[the backward-source theorem](research_even_run_backward_source_growth.md),
but (12) also applies to arbitrary initial channel vectors.

## 3. The physical Green matrix and the original scalar

At \(x=Q\), the successive transfer factors are the physical
colors \(1,\ldots,N-1,0\). The last is the even reset
\(T_{N-1}(Q)=0\), so
\[
             P(Q)=0,\qquad G_N(Q)=R_N(Q)\ge0.
 \tag{16}
\]
Let \(v_a=q^{k-a}\), \(1\le a\le k\), be the prescribed
original residue vector. The literal reflected source is
\[
 \boxed{\quad
 \phi_N(R^{-2k}T(R^{2k}))
     =1+P_N(Q)(v\otimes\bar v)
     =1+v^*G_N(Q)v.
 \quad}                                                       \tag{17}
\]
The numerator \(P_N\) in (17) is the marked Laurent row, not
the one-run matrix \(P\) in (2). The two crossing units cancel
because their powers sum to zero. The initial term is exactly
one since \(e_k^Tv=1\).

**Theorem 3.** For every \(N\ge2k\),
\[
 \boxed{\quad
 G_N(Q)\ \ge c_kN^{-4k}I,\qquad
 \|G_N(Q)^{-1}\|_2\le c_k^{-1}N^{4k},\qquad
 c_k=\frac{16^k(k!)^4}{K_k^2}.
 \quad}                                                       \tag{18}
\]
The result holds at both level parities.

*Proof.* Consider the first \(k\) physical forward steps
\(u_j=\mathcal T_{2k}(j)u_{j-1}\), starting at an arbitrary
vector. They lie before the reset because \(k<N\) for
\(N\ge2k\). Their exact equations are
\[
 H_ju_j=4\sin^2(\pi j/N)u_{j-1}.
 \tag{19}
\]
The transfer is invertible at \(1\le j\le k\), and
\[
 \|u_k\|_2
 \ge4^{-k}\prod_{j=1}^{k}4\sin^2(\pi j/N)\,\|u_0\|_2
 \ge \frac{4^k(k!)^2}{N^{2k}}\|u_0\|_2.
 \tag{20}
\]
The last inequality uses \(\sin(\pi j/N)\ge2j/N\) for
\(j\le N/2\). Lemma 2 applied to these \(k\) steps gives
\(\sum_{j=1}^k|e_k^Tu_j|^2\ge K_k^{-2}\|u_k\|^2\).
This is part of the full energy in \(G_N(Q)\).
Squaring (20) proves (18). \(\square\)

Thus the full marked Green matrix at the physical clock has
no exponentially small eigenvalue. This does not bound its
largest eigenvalue by a polynomial; the actual reflected source
has the positive exponential lower bound proved in the
backward-source theorem. Nor does (18) control an unrelated
complex bilinear joining of two nonreflected runs.

## 4. The exact inertia away from the physical reset

Suppose \(|x|=1\), \(x^N\ne1\), and \(d_k(x^N)\ne0\).
Every \(T_j(x)\) is then invertible. Also \(P(x)\) has no
unit-modulus eigenvalue, since such an eigenvalue would force
the determinant in (6) to vanish.
Let \(n_s,n_u\) count its eigenvalues inside and outside the
unit circle, with algebraic multiplicity.

**Theorem 4.** The Hermitian matrix \(G_N(x)\) has inertia
\[
                         (n_s,n_u,0).
 \tag{21}
\]
If every eigenvalue of \(P(x)\) is outside the unit circle,
there is the uniform bound
\[
                         G_N(x)\le-K_k^{-2}I.
 \tag{22}
\]

*Proof.* When \(\rho(P)<1\), iteration of (7) gives the
convergent exact series
\[
       G_N=\sum_{\nu=0}^{\infty}(P^*)^\nu R_NP^\nu.
 \tag{23}
\]
When \(\rho(P^{-1})<1\), it gives instead
\[
       G_N=-\sum_{\nu=1}^{\infty}
                   (P^{-*})^\nu R_NP^{-\nu}.
 \tag{24}
\]
These statements need no normality or diagonalizability:
finite-dimensional matrix powers decay geometrically times
a polynomial on the indicated spectral subspaces.

For the general case, restrict the quadratic form of (7) to
the invariant stable subspace and iterate forward. Formula
(23) holds on that subspace and is strictly positive there.
Indeed choose \(m\) with \(mN\ge k\); its first \(m\) terms
are \(R_N^{[m]}\), which is positive definite by (14) and
the invertibility of \(P\).
Restricting to the invariant unstable subspace and iterating
backward similarly gives a strictly negative form there.
These subspaces have dimensions \(n_s,n_u\) summing to \(k\).
The dimensions of positive and negative subspaces of a
Hermitian form therefore force exactly the inertia (21).

If the entire spectrum is unstable, group (24) into blocks
of \(m\) periods. Its first grouped term gives
\[
 -G_N\ge(P^{-m})^*R_N^{[m]}P^{-m}\ge K_k^{-2}I,
 \tag{25}
\]
by (14). This proves (22) at every level. \(\square\)

The exact source characteristic theorem identifies \(n_s,n_u\)
with the corresponding counts for
\(T_{2k}^{\mathrm{cl}}(x^N)\). Its common factor \((-1)^N\)
does not change any modulus.

At \(x^N=-1\), all the eigenvalues are unstable. To see this
directly, write
\[
 T_{2k}^{\mathrm{cl}}(-1)=4H^{-1},\qquad
 H=-B,\qquad B=2I+T_k-E_{11}+E_{kk}.
 \tag{26}
\]
After conjugation by alternating channel signs, the quadratic
form of \(B\) is
\(\sum_{j<k}|z_j-z_{j+1}|^2+2|z_k|^2\).
The matrix \(4I-B=2I-T_k+E_{11}-E_{kk}\) already has the
path form \(\sum_{j<k}|z_j-z_{j+1}|^2+2|z_1|^2\).
Both forms are strictly positive.
Thus every eigenvalue of \(B\) lies in \((0,4)\), and every
eigenvalue of \(4H^{-1}\) has modulus greater than one.
There is no denominator zero there, and (22) applies.

## 5. The Laurent numerator is not a globally positive symbol

On the unit circle let \(\mathcal P_N(x)\) be the matrix
obtained by reshaping the actual Laurent numerator row \(P_N(x)\)
with the convention (4). Then
\[
                \mathcal P_N(x)=d_k(x^N)G_N(x).
 \tag{27}
\]
The scalar \(d_k(x^N)\) is real. For example, the eigenvalue
factorization of (6) pairs every factor
\(1-\lambda_i\overline{\lambda_j}\) with its conjugate.
Consequently \(\mathcal P_N\) is a Hermitian Laurent matrix
on the unit circle, including at denominator roots by
continuity. Near the first reset-stable arc its Green quotient
is positive. Globally this fails in a stronger way:

**Corollary 5.** For every \(k\ge2\) and \(N\ge2\), there
is a nonempty open arc of unit clocks on which the actual
Laurent numerator \(\mathcal P_N(x)\) is indefinite.
Consequently its Fourier coefficients do not define positive
semidefinite block Toeplitz sections of every size.

*Proof.* Set \(X_*=e^{i\pi/3}\). The classical transfer there
is \(H_*^{-1}\), because
\((1-X_*)(1-X_*^{-1})=1\), where
\[
 H_*=
 \begin{pmatrix}
 X_*^{-1}&-1&&\\
 -1&1&\ddots&\\
 &\ddots&\ddots&-1\\
 &&-1&0
 \end{pmatrix},\qquad
                         |\det H_*|=1.
 \tag{28}
\]
For \(k=2\), the diagonal in (28) consists just of
\(X_*^{-1},0\). Its determinant is \(-1\). If both
eigenvalues had modulus one, their sum would be purely
imaginary, since their product is \(-1\). Their actual sum
\(X_*^{-1}\) has nonzero real part, a contradiction.

For \(k\ge3\),
\[
               \operatorname{tr}(H_*^2)=3k-4+X_*^{-2},
 \qquad |\operatorname{tr}(H_*^2)|>k.
 \tag{29}
\]
Indeed its real part is \(3k-\tfrac92>k\).
If every eigenvalue had modulus one, the trace of their
squares would have modulus at most \(k\). This contradiction,
together with \(|\det H_*|=1\), shows that some eigenvalues
have modulus less than one and some greater than one.
The same is true for \(H_*^{-1}\).

The two strict spectral inequalities persist on a small
unit arc about \(X_*\), by continuity of the finite spectrum.
The nonzero Laurent polynomial \(d_k\) has only finitely
many zeros there. Choose a smaller open arc avoiding them.
On every corresponding \(N\)-th-root clock arc, the exact
characteristic identity and Theorem 4 make \(G_N\) indefinite.
Multiplication by the nonzero real scalar in (27) preserves
indefiniteness.

Finally choose a clock \(x_0\) and a vector \(v\) with
\(v^*\mathcal P_N(x_0)v<0\). The analytic polynomial vectors
\[
 f_L(x)=L^{-1/2}v\sum_{j=0}^{L-1}(\overline{x_0}x)^j
 \tag{30}
\]
have squared scalar weight equal to the Fejer kernel.
Continuity gives
\[
 \lim_{L\to\infty}\frac1{2\pi}
       \int_0^{2\pi}f_L(e^{it})^*
              \mathcal P_N(e^{it})f_L(e^{it})\,dt
          =v^*\mathcal P_N(x_0)v<0.
 \tag{31}
\]
Each integral is the quadratic form of a finite block Toeplitz
section of the actual Laurent coefficients. Some section
therefore has a negative direction. \(\square\)

This is a limitation of a specific proposed positivity route.
It neither excludes a different source-preserving block
factorization nor proves cancellation of the physical source.
The physical value (17) remains its positive original Gram sum.
The indefinite auxiliary symbol shows why that positivity
alone cannot turn the entire forced Laurent equation into
a positive Fourier energy for arbitrary signed compositions.

## 6. Finite source-normalization check

The [independent diagnostic](../experiments/check_reflected_laurent_stein_energy.py)
forms the original augmented transfer, reshapes its affine row,
and compares it with the directly accumulated output Gram matrix.
At the physical clock it also compares (17) with the norm of the
column obtained from the original \(N\times N\) crossing matrix.
The [110-digit record](../repro/results/research-reflected-laurent-stein-energy.json)
checks 96 cases, covering \(N=2,\ldots,9\), \(k=1,\ldots,4\),
the physical clock, the all-unstable clock, and a mixed-spectrum
clock. It checks both exact Stein identities, the stated physical
and unstable bounds, and the inertia. Its largest relative
identity residual is \(3.17726656662\cdot10^{-105}\).

These computations check finite source normalization. The
all-level estimates and all-rank indefiniteness are proved above;
they are not inferred from the finite examples.
