# Independent proof audit of the divided Ward / marked-edge bridge

Audit, 27 October 2026. I checked the current proofs in
[the marked divided-adjoint note](divided_adjoint_marked_edge_pairing.md),
[factorial fusion](divided_ward_factorial_fusion.md),
[the general complete-color construction](complete_color_divided_ward_and_fusion.md),
and section 5.1 of
[the unfolded Ward theorem](unfolded_ward_factorial_and_regulator.md).
No defect was found in the stated operator, source, pivot, or
moving-representation identities. This is a proof audit; I did not
rerun the authors' matrix checks.

## 1. The divided adjoint and its exact marked pairing

For \(\mathcal E=\rho^2E\), the genuine generic Hopf adjoint is
\[
 A(T)=[\mathcal E,T]K^{-1}=X(T)+Y(T),\qquad
 X=L_{\mathcal E}R_{K^{-1}},\quad
 Y=-R_{\mathcal E K^{-1}}.
\]
The relation \(K\mathcal E=Q\mathcal E K\) gives \(XY=QYX\).
On the individual integral Weyl color, \(X^N=Y^N=0\)
identically before specialization. The mixed \(Q\)-binomial
coefficients have the single canceled factor \(1-Q^N\), giving
the stated regular divided Hopf adjoint. Ordinary commutation
by a one-factor divided matrix would lose these mixed terms.

For \(W=E_{N-1,0}\), the term \(Y^lX^j\), \(j+l=N\), has only
the entry \((l-1,l)\). Its phase is
\[
 (-1)^lQ^{-l(l-1)/2-jl}
       P_{N-1}\epsilon_lK^{-N}.
\]
Using
\[
 c_l=\frac{(-1)^{l-1}Q^{-l(l-1)/2}}{1-Q^l},\quad
 \epsilon_l=(1-Q^l)Q^{-l},\quad
 P_{N-1}K^{-N}=N,
\]
the sign is \(-1\) and the exponent is \(-lN\). Thus every
superedge coefficient is exactly \(-N\), including even and
composite \(N\):
\[
 J_{\rm ad}(W)=-N\sum_{l=1}^{N-1}E_{l-1,l}.
\]
For the literal marked row \(\Phi(T)=\operatorname{Tr}(eT)\),
\(e_{ab}=1/N\), this gives \(\Phi(J_{\rm ad}W)=-(N-1)\).

Consequently
\[
 \Phi_{\rm div}(T)=-\frac{\Phi(J_{\rm ad}(TW))}{N-1}
\]
has \(\Phi_{\rm div}(I)=1\). Its equality with the original row
on scalar cut operators is exact. The all-matrices homotopy
\[
 \Phi_{\rm div}-\Phi
    =(\Phi_{\rm div}-\Phi)h_W\delta_W
\]
follows directly from \(h_W\delta_W=I-ip\) and the fact that the
row difference kills \(I\). It neither assumes nor supplies a
geometric representative for that scalar cohomology class.

## 2. Partial trace: the generic pivot and the insertion order

For the genuine generic integral color, the compatible pivot
is \(K\). The all-matrices pivotal partial trace intertwines
the Hopf adjoint. This can be checked on generators:
the closed \(E\)-terms cancel because \(K^{-1}K=I\), and
the closed \(F\)-terms cancel by the same cyclic trace identity.
Thus it intertwines every power, and hence the quotient by
\(1-Q^N\) before specialization.

The total tensor-and-dual divided adjoint is regular: its
multinomial expansion has individual nilpotent powers and
the same canceled root factors. Therefore the divided
partial-trace identity specializes legitimately.

Only after this specialization does one use
\[
 g=K^{1-N}=(K^N)^{-1}K
\]
with \(K^N\) scalar. This proves the identity for the actual
root pivot \(g\). It does not replace the generic \(g\)-pivot
by \(K\) while taking a derivative. The nonconstant derivative
of \(K^{-N}\) is correctly retained in the separate normal
adapter calculation.

For an arbitrary full matrix \(T\),
\[
 \operatorname{ptr}_g(T(W\otimes I))
       =(\operatorname{ptr}_gT)W.
\]
Combining this with divided-adjoint naturality gives exactly
the stated ordered formula for \(\Phi_{\rm div}\operatorname{ptr}_g\).
It does not give a formula with the edge moved outside
\(J_{\rm ad,total}\). The note retains the correct order.

## 3. Fusion and the even-level character

The generic ordered factorial product equals the finite
quantum exponential of the total raising matrix.
At degree \(kN+s\), cancellation gives
\[
 \left[
 \frac{(Q;Q)_{kN+s}}{(1-Q^N)^k}
 \right]_{\rm root}
 =N^k k!(Q;Q)_s.
\]
Thus the full root defect is
\(\exp((-t)^NJ_b/N)\), not merely its first term.
All powers terminate by total-position degree.

The inherited block term is \(J_X\otimes\chi_Y\), where
\[
 \chi_Y=K_Y^N=(-1)^{(N-1)\operatorname{length}(Y)}.
\]
Expanding the two sides of the additive three-block identity
cancels every inherited \(J\) term. Within each side the
remaining operators commute because the inner mixed term
commutes with its block's total raising operator and \(K\).
Exponentiation therefore proves the displayed twisted
associativity. The factor \(\chi\) is essential at even \(N\);
the signs in the notes are correct.

The extension to both divided \(E\) and \(F\) directions is
explicitly not asserted unipotent. The invariant two-dimensional
block with opposite nilpotents generates an \(\mathrm{SL}_2\)
action, consistently with that qualification.

## 4. The moving representation retains exactly one resonant log term

In the integral lift, \(C(Q)\) is nilpotent generically and
\[
 C(Q)^N=(1-Q^N)J_b(Q)
\]
with \(J_b(Q)\) regular. Thus evaluating the unfolded logarithm
at \(-tC(Q)\) is a finite rational matrix calculation.

For \(m\ge N\) not divisible by \(N\), its denominator
\(1-Q^m\) is a unit at the root, while \(C(Q)^m\) has at least
one \(1-Q^N\) factor. For \(m=kN\), \(k\ge2\), its numerator
has \(k\) such factors and its denominator only one. These
terms vanish at the root. The only extra surviving logarithm
term is
\[
 \frac{(-t)^N J_b}{N}.
\]
Since \(J_b\) commutes with the root total raising operator,
exponentiation gives the exact finite ghost times the literal
nilpotent factorial. Higher ghost powers arise from this
exponential, even though higher dilogarithm powers vanish
before exponentiation.

With \(Q=Q_Ne^h\),
\(C(Q)^N=-NhJ_b+O(h^2)\). Substitution into the coefficientwise
pole \(-\operatorname{Li}_2((-tC(Q))^N)/(N^2h)\) gives the same
surviving term, with its sign. Setting \(C^N=0\) first would
incorrectly discard it.

## 5. The two normals and the remaining global issue

The absent generic edge
\[
 w(Q,M)=MQ^{-N}-M^{-1}
\]
vanishes on the integral Weyl curve \(M=-q^N\), but restricts
to \(\kappa\) on the root wall. The exact auxiliary defect
\[
 [\mathcal E,F]-\rho(K-K^{-1})
    =-(1-Q^N)w(Q,M)E_{N-1,N-1}
\]
is correct by direct adjacent-entry subtraction. The routewise
pivot/twist adapter is likewise the product of the \(b-1\)
closed factors \(K^{-N}\) and the writhe correction. Its root
value is one by knot parity; its derivative retains the
closed-position moment. The notes distinguish these normals.

The marked divided row is a concrete new realization of the
original cut class and is transported through exact finite
partial trace. It does not yet map the partial geometric
Gaussian block into that class. Ordinary full closure still
kills an uncompensated positive divided ghost by position
degree, and the nonzero marked-edge tests are cochain tests.
No passage to a selected global geometric coefficient follows
from these identities alone; the notes' scope statements
correctly preserve that distinction.
