# Exact operator limits of the mixed three/four contraction

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The new exact Fourier contraction retains a useful finite source, but
pairing its Gram matrix with a vertex is a simultaneous similarity of
the original operators. There is an all-level obstruction to making
both vertex types positive in one metric. The relative insertion also
fails any exact accretivity or contraction shortcut stated below.
These conclusions do not obstruct coherent approximate vectors,
local Gaussian packets, or estimates retaining the quadratic phase.

## 1. The grouped operators and their relative insertion

Use the exact matrices \(S,B_3,B_4,\Gamma\) in
[the mixed Fourier contraction](research_mixed_wire_exact_contraction.md).
They satisfy
\[
 A_n=JM^n=S^TB_nS,\qquad \Gamma=SS^T,\qquad
 T_n:=\Gamma B_n=SA_nS^{-1},\quad n=3,4.
 \tag{1}
\]
In particular
\[
              T_3^{-1}T_4=SMS^{-1}.
 \tag{2}
\]
The opposite grouping \(B_n\Gamma=S^{-T}A_nS^T\) has the same
conclusions. The ordinary boundary vectors also change by the exact
matrix \(S\); no original first normal is omitted.

The original crossing is lower triangular, with eigenvalues
\[
 \lambda_j=\kappa(-1)^j q^{j+j^2},\qquad
 q=e^{\pi i/N},\quad 0\le j<N,\quad |\kappa|=1.
 \tag{3}
\]
These follow directly from its original entries in equation (6) of
the contraction note. We use their exact values, not an estimate of
the eigenvectors or a bound inferred from an eigenvalue gap.

## 2. No simultaneous positive Hermitian form

**Theorem 1.** At every integer level \(N\ge2\), there are no
positive definite Hermitian matrix \(H\) and nonzero complex scalars
\(\alpha_3,\alpha_4\) for which both \(\alpha_3T_3\) and
\(\alpha_4T_4\) are positive Hermitian operators in the inner
product \(\langle u,v\rangle_H=u^*Hv\).

*Proof.* If two invertible operators are positive Hermitian in the
same positive inner product, their relative product is similar to a
positive Hermitian matrix. It is diagonalizable and all its
eigenvalues are positive real. Thus (2) would imply this property
for \((\alpha_4/\alpha_3)M\).
For \(N>2\), however,
\[
                 \frac{\lambda_1}{\lambda_0}
                         =-e^{2\pi i/N}\notin\mathbb R_{>0}.
 \tag{4}
\]
No common scalar rotation can make both eigenvalues positive real.
At \(N=2\), the original formula instead gives
\[
       \kappa^{-1}M=\begin{pmatrix}1&0\\-i&1\end{pmatrix},
 \tag{5}
\]
a nontrivial Jordan block. It is not diagonalizable after any scalar
multiplication or similarity. This proves the theorem. \(\square\)

The assertion concerns one common positive metric. It does not say
that every possible separate representation or approximate source
estimate fails, and it does not replace the already known positive
similarity for the single three-crossing operator.

## 3. The relative insertion is not accretive

An operator \(T\) is accretive in a positive metric \(H\) if
\(\Re(u^*HTu)\ge0\) for every vector \(u\), and strictly
accretive if this is strictly positive for every nonzero \(u\).

**Theorem 2.** For \(N\ge6\), no nonzero scalar multiple of
\(T_3^{-1}T_4\) is strictly accretive in any positive metric.
For \(N\ge7\), no such scalar multiple is even accretive.

*Proof.* Accretivity forces every eigenvalue into the closed right
half-plane: apply its defining inequality to an eigenvector.
Strict accretivity forces every eigenvalue into the open half-plane.
At \(N=6\), (3) gives
\(\lambda_2/\lambda_0=e^{6\pi i/N}=-1\), so the open-half-plane
condition is impossible after any rotation.

For \(N\ge7\), put \(\theta=\pi/N\). Three normalized
eigenvalues are
\[
          1,\qquad e^{6i\theta},\qquad -e^{2i\theta}.
 \tag{6}
\]
They have the exact positive dependence
\[
 \sin(4\theta)
 +\sin(2\theta)e^{6i\theta}
 -\sin(6\theta)e^{2i\theta}=0.
 \tag{7}
\]
All three weights are strictly positive. These three points are
noncollinear; equivalently, their successive angular gaps are
\(6\pi/N,\pi-4\pi/N,\pi-2\pi/N\), all strictly between zero
and \(\pi\). Hence zero is strictly inside their convex hull.
No rotation of this triangle lies in a closed half-plane through
zero. Similarity (2) and any nonzero scalar multiplication preserve
this obstruction. \(\square\)

This theorem concerns the relative three-to-four insertion. It does
not assert that both grouped vertex operators separately fail every
accretivity test. The exact products and their closing boundary
observations still have to be estimated together.

## 4. Unit-modulus normalization cannot make the insertion contractive

**Proposition 3.** For every \(N\ge2\), every unit scalar \(\zeta\),
and every positive definite Hermitian \(H\),
\[
                  \|\zeta T_3^{-1}T_4\|_H>1.
 \tag{8}
\]

The [original full-jet crossing proof](research_original_almost_invariance_and_observation.md#1-original-operators-and-the-unitarization-obstruction)
gives, at the double physical root \(c_0=2\cos(\pi/N)\),
\[
 R(c_0)I+R'(c_0)\epsilon,\qquad \epsilon^2=0,\quad\epsilon\ne0,
 \qquad
 \frac{R'(c_0)}{R(c_0)}=\frac{i(N-1)}{4\sin(\pi/N)}\ne0,
 \quad |R(c_0)|=1.
 \tag{9}
\]
Thus the original crossing has a nontrivial unit-circle Jordan block
at every level, including its genuine first-normal direction.
Its powers are unbounded in every finite-dimensional norm, as are
those of any unit scalar multiple and every similarity. If the norm
in (8) were at most one, all powers would be bounded by one,
contradicting (9). This proves the proposition.

Scaling by a number of modulus less than one is a different operation;
it changes the original word normalization, and that compensation
must be retained. No assertion here excludes an estimate with such
an explicitly accounted normalization.

## 5. What remains available

The exact sine weights and quadratic oscillation in the contraction
formula remain valid. Their positive amplitudes are not a Hermitian
Gram representation: the integration pairing is bilinear, without
conjugation. The obstructions above exclude exact common positivity,
accretivity of the relative insertion, and unit-normalized contraction.
They do not exclude bounds for the complete oscillatory word or a
source-specific closing overlap. In particular the
[joint unsummed coercivity theorem](research_mixed_three_four_joint_coercivity.md)
controls a different object, the local analytic phase, and is fully
consistent with these finite operator statements.

Run `python3 experiments/check_mixed_three_four_operator_obstruction.py`.
The checker verifies the exact matrix/phase identities and all-level
sign reductions. Its finite tests are not substitutes for the proofs
above, and it claims no global mixed-word asymptotic.
