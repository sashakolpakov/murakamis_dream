# A finite-channel recurrence for the original two-run source

Research note, 3 November 2026.

One original turn between two fixed crossing runs can be retained
exactly in a recurrence whose dimension is independent of the quantum
level. It computes every original color contribution before summing
them. Its coefficients have no poles at the physical colors. This
uses the resonant boundary of each run, rather than replacing it by
the bounded complete endpoint block.

For the original powers \((-4,-5)\), the recurrence has seven
coordinates. The construction is an exact source reduction. It does
not by itself prove a dominant mode or a nonzero asymptotic coefficient
for its complex matrix product.

## 1. A polynomial matrix for the resonant run

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(\kappa=q^{D^2/2}\). The original crossing and turn matrices are
\(M,J\). Put
\[
 \alpha_{p,j}=(M^p\mathbf e_0)_j,\qquad p\in\mathbb Z.
 \tag{1}
\]
These are all Newton coefficients, not evaluations at the distinct
roots. They determine the entire original boundary polynomial and
its first normals.

For \(k\ge1\), use the channel matrix
\[
 C_k(r)=(r+r^{-1})I_k-T_k-rE_{11}
 \tag{2}
\]
from the crossing-run construction, where \(T_k\) is path adjacency.
For a parameter \(q_0\ne0\), define
\[
 \mathcal B_k(r;q_0)
   =(1-r/q_0)[C_k(r)-q_0^{-1}E_{kk}]^{-1}.
 \tag{3}
\]
The inverse notation in (3) is only an initial expression on its
regular set. The matrix extends polynomially in \(r\) to the
apparent pole. In fact, with \(1\le a,b\le k\),
\[
 \boxed{\quad
 (\mathcal B_k(r;q_0))_{ab}
  =r^{|a-b|+1}
     \left[
       \sum_{\ell=0}^{k-\max(a,b)}r^{2\ell}
       -\frac r{q_0}
          \sum_{\ell=0}^{k-\max(a,b)-1}r^{2\ell}
     \right].
 \quad}                                                        \tag{4}
\]
An empty second sum is zero.

To verify (4), first invert (2):
\[
 (C_k(r)^{-1})_{ab}
    =\sum_{\ell=0}^{k-\max(a,b)}
                      r^{|a-b|+1+2\ell},\qquad
 (C_k(r)^{-1})_{a,k}=r^{k-a+1}.
 \tag{5}
\]
The determinant is \(r^{-k}\). A last-diagonal rank-one update has
determinant \(r^{-k}(1-r/q_0)\). Its inverse gives
\[
 \mathcal B_k
 =(1-r/q_0)C_k^{-1}
      +q_0^{-1}(C_k^{-1}\mathbf e_k)
                      (\mathbf e_k^TC_k^{-1}),
 \tag{6}
\]
which is (4), after canceling the largest power in the second term.
These are polynomial identities, so the calculation proves the
extension, including \(r=q_0\).
For \(|r|=|q_0|=1\), it also gives the explicit bound
\[
            \|\mathcal B_k(r;q_0)\|_2\le k(2k-1).
 \tag{7}
\]

## 2. Every color of one signed run

Let \(p\ne0\), \(\sigma=\operatorname{sgn}p\), and
\(k=\lceil |p|/2\rceil\). Set
\[
 q_\sigma=q^\sigma,\qquad z_j=Q^{\sigma j},
 \qquad r_j=q_\sigma z_j,\qquad
 (v_p)_a=q_\sigma^{k-a}\quad(1\le a\le k).
 \tag{8}
\]
Define \(u_{p,0}=v_p\) and, for \(1\le j<N\),
\[
 u_{p,j}=\mathcal T_p(j)u_{p,j-1},                       \tag{9}
\]
where
\[
 \boxed{\begin{aligned}
 \mathcal T_p(j)
  &=(1-z_j^{-1})\mathcal B_k(r_j;q_\sigma),
                          && |p|\text{ even},\\
 \mathcal T_p(j)
  &=\mathcal B_k(r_j;q_\sigma)
        \operatorname{diag}(-z_j^{-1},
                  1-z_j^{-1},\ldots,1-z_j^{-1}),
                          && |p|\text{ odd}.
 \end{aligned}}                                                \tag{10}
\]
In the odd case \(k=1\), the displayed diagonal has just its first
entry.

**Proposition 1.** The complete original coefficient column is
\[
                 \boxed{\quad
       \alpha_{p,j}=\kappa^p\mathbf e_k^T u_{p,j}
                      \quad(0\le j<N).
                 \quad}                                      \tag{11}
\]
There is no omitted low or high color in this formula.

Here is the normalization and pole cancellation behind it. The
[resonant crossing-run source](research_resonant_crossing_run_source.md)
obtains the original column from the pole at \(\lambda=1\) of the
conjugated clock resolvent. In the channel system this changes
\(C_k(r_j)\) to
\[
                   C_k(r_j)-(\lambda/q)E_{kk}.            \tag{12}
\]
At \(\lambda=1\), only color zero is singular. Its nullvector with
last coordinate one is \(v_a=q^{k-a}\), and its resolvent residue
in \(\lambda\) is exactly \(-qvv^T\).
The original eigenvector has initial coefficient \(\kappa^p\);
the projector normalization therefore gives the initial state in
(8), without an arbitrary amplitude.

For positive even \(p\), the next color equation multiplies by
\([C_k(r_j)-q^{-1}E_{kk}]^{-1}s_j^2\), with
\(s_j=2\sin(j\pi/N)\). Since
\[
       \frac{s_j^2}{1-Q^j}=1-Q^{-j},                    \tag{13}
\]
this gives the first line of (10). For positive odd \(p\), the
color edge is
\(\operatorname{diag}(1-Q^{-j},s_j^2,\ldots,s_j^2)\).
The first quotient is
\((1-Q^{-j})/(1-Q^j)=-Q^{-j}\); the others are (13).
This proves the second line, in the stated order. Finally
\(\overline M=M^{-1}\) in the real Newton basis, so entrywise
conjugation proves the negative-power case. The first and last
physical rows have both been retained.

All entries in (10) are Laurent polynomials in \(z_j\), with
coefficients Laurent polynomial in \(q_\sigma\). In particular
\[
                    \|\mathcal T_p(j)\|_2\le2k(2k-1)
 \tag{14}
\]
uniformly in \(N\) and the color. This bound includes their
polynomial extension to \(z_j=1\). The actual initial state still
comes from the residue; it is not obtained by applying the zero
color transfer to an unspecified vector.

## 3. The literal turn and the closed scalar

For fixed nonzero signed integers \(a,b\), retain the original
word \(M^bJM^a\), and let \(T\) denote the original turn represented
by \(J\). The Frobenius pairing and transpose identity
\((M^b)^T=JM^bJ\) give
\[
 \begin{split}
 \mathcal Z_{a,b,N}
   &=\phi_N(R^b\,T(R^a))\\
   &=\mathbf e_D^TM^bJM^a\mathbf e_0
     =\sum_{j=0}^D\alpha_{b,j}\alpha_{a,j}.
 \end{split}                                                   \tag{15}
\]
The pairing in (15) is bilinear. There is no conjugation unless
the actual powers themselves supply it.

Let \(k=\lceil|a|/2\rceil\), \(\ell=\lceil|b|/2\rceil\), and put
\[
 c^T=\mathbf e_k^T\otimes\mathbf e_\ell^T,\qquad
 w_0=v_a\otimes v_b,\qquad \zeta_0=1.
 \tag{16}
\]
For \(1\le j<N\), use the \(k\ell+1\) dimensional recurrence
\[
 \begin{pmatrix}w_j\\\zeta_j\end{pmatrix}
 =
 \begin{pmatrix}
  \mathcal T_a(j)\otimes\mathcal T_b(j)&0\\
  c^T[\mathcal T_a(j)\otimes\mathcal T_b(j)]&1
 \end{pmatrix}
 \begin{pmatrix}w_{j-1}\\\zeta_{j-1}\end{pmatrix}.         \tag{17}
\]
The scalar \(\zeta_j\) accumulates the color contributions.

**Theorem 2.** The recurrence computes the exact original source:
\[
                     \boxed{\quad
       \mathcal Z_{a,b,N}=\kappa^{a+b}\zeta_D.
                     \quad}                            \tag{18}
\]
Moreover each retained color contribution is exactly
\[
            \alpha_{a,j}\alpha_{b,j}
                       =\kappa^{a+b}c^Tw_j.             \tag{19}
\]

*Proof.* Induction gives \(w_j=u_{a,j}\otimes u_{b,j}\).
Its pairing with \(c^T\), followed by (11), is (19).
Both initial last channel coordinates are one, so the contribution
at color zero is exactly the initial \(\zeta_0=1\).
The last row of (17) then sums every contribution through color
\(D\). Equation (15) proves (18). \(\square\)

This constructs a bounded-coefficient finite-dimensional recurrence
for the original source, not just its annihilator or a determinant
with the same characteristic curve. For \((a,b)=(-4,-5)\), one
has \(k=2,\ell=3\), hence seven coordinates. All original scalar
phases and both level parities are retained. If an admissible
marked closure gives a knot, the usual source-to-invariant writhe
unit is still applied to this same scalar; no tangle rotation or
twist assignment has been changed.

The full arrays in (11) and (19) remain available before the turn
is contracted. A specified diagonal weight \(\omega_j\) at that
interface is inserted by replacing the last row in (17) with
\(\omega_j c^T[\mathcal T_a(j)\otimes\mathcal T_b(j)]\), and
initializing the accumulator with \(\omega_0\). This is an exact
weighted color pairing. It is not an assertion that an arbitrary
free geometric boundary acts by a diagonal weight, nor a proof of
a whole-boundary asymptotic.

## 4. What positivity survives

When \(b=-a\), the original coefficients themselves are conjugate,
so (15) gives the actual positive identity
\[
                   \mathcal Z_{a,-a,N}
                           =\sum_{j=0}^D|\alpha_{a,j}|^2>0.
 \tag{20}
\]
For equal-sign powers, (17) retains their oscillatory phases and
does not turn the sum into a Gram pairing.

The elementary case \(a=2,b=-2\) also explains why the nonresonant
endpoint block cannot replace this interface. The original
two-crossing formula gives \(|\alpha_{2,j}|=S_j\), hence
\[
                   \mathcal Z_{2,-2,N}=\sum_{j=0}^D S_j^2.
 \tag{21}
\]
With
\(\gamma=-\int_0^{1/6}\log(2\sin\pi x)\,dx>0\), the uniform
factorial estimate in the
[weighted Green calculation](research_elementary_weighted_green_transport.md)
proves
\[
             \lim_{N\to\infty}\frac1N
                  \log\mathcal Z_{2,-2,N}=2\gamma>0.
 \tag{22}
\]
Indeed the largest summand has rate \(2\gamma\), near color
\(5N/6\), and there are only \(N\) nonnegative summands.
In contrast, the complete one-channel endpoint maps are scalars
of modulus \(N^2\). A fixed composition using only those maps
and polynomially bounded connecting maps cannot produce (22).
The resonant states and their full color interface are necessary.

The recurrence (17) now exposes that interface without moving
contours or dropping endpoint terms. A general asymptotic theorem
still requires control of its complex matrix product and final
accumulator. A uniform bound on individual transfer matrices gives
an exponential upper bound, but neither the correct geometric
rate nor a nonzero leading coefficient for equal-sign short powers.

The [original-source verifier](../experiments/check_two_run_source_transfer.py)
compares all run coefficients and all retained paired-color terms
with the original full matrices before checking the final scalar.
Its [saved result](../repro/results/research-two-run-source-transfer.json)
is a finite normalization diagnostic.
