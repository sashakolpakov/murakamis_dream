# The ordinary boundary as a Casimir mark and a forced resolvent

Research deduction, 5 November 2026. This note specializes the
[marked-trace observation](research_mixed_marked_trace_observation.md)
to the original complete ordinary colors. The odd-level identity
uses the existing Fejér/Hermite interpolation, rather than a new
positive trace theorem. The even-level forcing is retained explicitly.
No global open-source lower bound is asserted.

## 1. Original pairing and evaluation defect

Use \(N\ge2\), \(D=N-1\), and the full Newton algebra
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
Here \(T_k\) denotes the ordinary Chebyshev polynomial. The original
Newton basis \(e_j\), vector \(v(z)\), crossing \(M\), and reversal
\(J\) are as in
[complete boundary transport, equations (1)--(4)](research_complete_boundary_coefficient_transport.md).
In particular \(\phi_N(e_i e_j)=J_{ij}\). Let \(C\) be multiplication
by \(z\) in this basis. Its only nonzero entries are
\[
 C_{jj}=c_j=2\cos((2j+1)\pi/N),\qquad
 C_{j,j-1}=-d_j,\quad d_j=4\sin^2(\pi j/N).
 \tag{2}
\]
Thus \(C^TJ=JC\), and the Newton recurrence, including its last row,
gives the polynomial identity
\[
 v(z)^T(C-zI)=\frac{(-1)^N P_N(z)}{N^2}\,\mathbf e_D^T .
 \tag{3}
\]
Indeed all components before the last cancel by
\(d_{j+1}e_{j+1}=(c_j-z)e_j\). The last is
\((c_D-z)e_D=(-1)^NP_N(z)/N^2\), since \(S_D=N\).
The symbol \(\mathbf e_j\) denotes a coordinate vector, not a Newton
polynomial.

Set \(v=v(-2)\), \(A_n=JM^n\), and let \(W\) be any fixed word in
\(A_3,A_4\). Its actual complete ordinary coefficient is
\[
                         F_N(W)=v^TWv.                  \tag{4}
\]
All the matrix identities below hold before any asymptotic estimate.

## 2. Odd levels: the exact Fejér idempotent

Suppose \(N\) is odd. The physical root \(-2\) of \(P_N\) is simple,
with \(P_N'(-2)=N^2\). Define
\[
                  \pi_N(z)=\frac{P_N(z)}{N^2(z+2)}.
 \tag{5}
\]
This is a polynomial of degree \(D\). It equals one at \(-2\), and
its value and first derivative vanish at every other, double,
physical root. It is therefore the primitive idempotent of the
complete root in the full algebra. Moreover \(\phi_N(\pi_N)=1\).
For every \(f\in\mathcal A_N\),
\[
                  \phi_N(\pi_N f)=f(-2).                \tag{6}
\]
If \(p\) is the coefficient vector of \(\pi_N\), (6) and the
Frobenius pairing give \(p^TJ=v^T\), hence \(p=Jv\).
Multiplication by the idempotent sends \(f\) to \(f(-2)\pi_N\).
Consequently
\[
                         \boxed{\ \pi_N(C)=Jvv^T.\ }    \tag{7}
\]
This proves (7) on the original algebra, including every first normal;
it does not replace the algebra by its value-only quotient.

Let \(\rho_N=R(-2)\) be the original crossing value. Physical
multiplication gives \(v^TM=\rho_Nv^T\), and \(M^TJ=JM\) gives
\(MJv=\rho_NJv\). Thus \(A_3Jv=\rho_N^3v\). Cyclicity and (7) prove
\[
       \boxed{\ F_N(W)=\rho_N^{-3}
                   \operatorname{tr}\bigl(\pi_N(C)WA_3\bigr).\ }
 \tag{8}
\]
The scalar is the original one:
if \(N=2j+1\), then
\(\rho_N=\kappa(-1)^j q^{j(j+1)}\), with
\(q=e^{\pi i/N}\), \(\kappa=q^{D^2/2}\).
There is no extra power of \(N\) in (8).

For real \(\theta\), the removable values understood, (5) is
\[
 \pi_N(-2\cos\theta)
 =\left(\frac{\sin(N\theta/2)}{N\sin(\theta/2)}\right)^2
 =\frac1N+\frac2N\sum_{k=1}^{N-1}
                   \left(1-\frac{k}{N}\right)\cos(k\theta).
 \tag{9}
\]
This is \(F_N^{\rm Fej}(\theta)/N\), with the Fejér kernel already
used in
[polynomial crossing interpolation, equation (8)](research_polynomial_crossing_fourier_trace.md).
In particular it is between zero and one on the real interval and
has nonnegative Fourier coefficients. Those scalar facts do not
make (7) a positive Hermitian matrix: its operator norm is exactly
\(\|v\|_2^2\), and the actual insertion is \(Jvv^T\).

## 3. One exact twisted-trace integral

Define the finite matrix polynomial
\[
 \mathcal D_N(\theta,C)
       =I+2\sum_{k=1}^{N-1}\cos(k\theta)T_k(-C/2),\qquad
 Z_N(\theta;W)=\operatorname{tr}
                      \bigl(\mathcal D_N(\theta,C)WA_3\bigr).
 \tag{10}
\]
Fourier orthogonality and (9) give the exact, entire-period formula
\[
 \boxed{\ F_N(W)=\frac{\rho_N^{-3}}{2\pi N}
     \int_{-\pi}^{\pi}
       F_N^{\rm Fej}(\theta)\,Z_N(\theta;W)\,d\theta.\ }
 \tag{11}
\]
The \(N\)-dependent kernel stays inside the integral. Equivalently,
if \(Z_{k,N}=\operatorname{tr}(T_k(-C/2)WA_3)\), then
\[
 F_N(W)=\frac{\rho_N^{-3}}N
       \left[Z_{0,N}
          +2\sum_{k=1}^{N-1}(1-k/N)Z_{k,N}\right].
 \tag{12}
\]
These identities do not require estimating individual modes.

The family in (10) is not an unmarked cyclic trace or a proved
ordinary-color deformation of one. Its exact source meaning can be
made explicit. For every polynomial \(f\) and every matrix \(B\),
the Frobenius pairing implies
\[
 \operatorname{tr}(f(C)B)
          =\phi_N\bigl(f(z)\,v(z)^TBJv(z)\bigr).
 \tag{13}
\]
Indeed the coefficient of \(e_a\) in \(fe_b\) is
\(\phi_N(fe_be_{D-a})\); summing it against \(B_{ba}\) proves (13).
Since multiplication gives
\(A_3Jv(z)\equiv R(z)^3v(z)\pmod{P_N}\), its specialization is
\[
 Z_N(\theta;W)=
 \phi_N\!\left(\mathcal D_N(\theta,z)R(z)^3
                         v(z)^TWv(z)\right).
 \tag{14}
\]
Thus identifying a geometric critical component of the diagonal
ordinary source does not yet estimate the whole twisted trace.
The [current-free polynomial trace formulas](research_polynomial_crossing_fourier_trace.md),
equations (9)--(11), apply to (14) with all original normals and
Fourier charges. They are the existing exact integral mechanism.
Their same note gives an actual charge-one cancellation example,
so the positive coefficients in (9) supply no positivity assertion
for (11) or (12).

An integral proof of (11) would need a uniform nonzero packet for
this precise \(Z_N\), and an estimate for its full marked complement.
For example, on a fixed complement \(|\theta|\ge\delta>0\),
\(F_N^{\rm Fej}(\theta)/N\le
1/(N^2\sin^2(\delta/2))\). This is only a polynomial penalty;
it cannot absorb an unproved larger exponential rate of \(Z_N\).
The known local geometric boundary response alone does not supply
these missing global estimates.

## 4. Even levels: the exact residual is not zero

For even \(N\), \(P_N(-2)=4\), so \(-2\) is not a physical root.
Put \(G=(C+2I)^{-1}\). Equation (3), together with
\(C^TJ=JC\), gives
\[
 v^T=\frac4{N^2}\mathbf e_D^TG,\qquad
 v=\frac4{N^2}JG\mathbf e_0,\qquad
 \boxed{\ F_N(W)=\frac{16}{N^4}
                 \mathbf e_D^TGWJG\mathbf e_0.\ }
 \tag{15}
\]
This is an exact forced resolvent observation, not a positive
quadratic form.

There is also a precise obstruction to using a single Casimir mark
as in (8) at even levels. If a matrix \(f(C)\) gave
\(\operatorname{tr}(f(C)WA_3)=v^TWv\) for every matrix \(W\), the
nondegenerate trace pairing would imply
\(f(C)=A_3^{-1}vv^T=M^{-3}Jvv^T\). But \(M\) commutes with \(C\),
while (3) gives
\[
 [C,Jvv^T]=\frac4{N^2}
       \bigl(\mathbf e_0v^T-Jv\mathbf e_D^T\bigr)\ne0.
 \tag{16}
\]
The last matrix has \((0,0)\) entry one before multiplication by
\(4/N^2\), for every \(N\ge2\). Hence no such function of \(C\)
exists as a matrix identity. This does not exclude extra relations
on a restricted family of \(W\). It does exclude silently using
the odd simple-root observation at even levels.

Equations (8), (11), and (15) retain the original observation at both
parities and specify a concrete marked-source route. They do not
remove the boundary estimate. The new reduction is the exact
identification of the ordinary mixed-word coefficient with these
particular marks and residuals; the Fejér interpolation and
current-free trace identities themselves are inherited results.
