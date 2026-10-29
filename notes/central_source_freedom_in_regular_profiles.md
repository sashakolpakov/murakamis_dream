# A same-operator central freedom in the whole regular profile

Independent algebraic audit, 27 October 2026. The actual root operator,
its bounded affine source, all integer-color values, reciprocity, and
qualitative finite exponential type do not by themselves force a
constant centered regular profile. They leave a central source freedom.
This is not a modification of the literature-defined invariant: it
identifies precisely which proposed uniqueness premises omit its
full marked source.

The starting objects are the actual
[regularized period](regularized_kashaev_period.md) and
[scaled meridian profile](scaled_meridian_regular_profile.md).
Fix \(Q_N=e^{2\pi i/N}\), \(U=Y^N\), and write
\[
 F_N=S_NR_N+P_N,\qquad S_N=(U-1)/(Y-1),\qquad K_N=F_N(1).
                                                               \tag{1}
\]
The specified root operator \(P\) annihilates \(F_N\). After the
fixed actual gauge, its affine operator \(A\) satisfies
\[
 A R_N=b_N,\qquad A p_N=-b_N,\qquad p_N=P_N/S_N.                 \tag{2}
\]
All coefficients and clearing factors of these actual operators
are retained.

## 1. An exact transformation preserving the operator and source

Let \(h(U)\) be any Laurent polynomial satisfying
\[
 h(1)=1,\qquad h(U^{-1})=h(U),
\]
and define an auxiliary comparison family
\[
 \widetilde F_N(Y)=h(Y^N)F_N(Y).                                \tag{3}
\]
The same \(h\) is used at every level. The following statements
are exact:

* Every specified root annihilator of \(F_N\) annihilates
  \(\widetilde F_N\), because \(T(U)=U\) for \(T(Y)=Q_NY\).
* Every ordinary and complete orbit value is unchanged, since
  \(U=1\) at \(Y=Q_N^j\). Thus \(P_N\), \(K_N\), and the given
  ordinary-color polynomial family are unchanged.
* Laurent polynomiality and actual Weyl reciprocity are preserved.
* The canonical regular quotient remains Laurent polynomial and
  satisfies the same affine equation with the same \(b_N\).

To prove the last assertion set
\[
 L_h(U)=\frac{h(U)-1}{U-1}\in\mathbb C[U,U^{-1}].
\]
Division is in the Laurent polynomial ring and is regular at
\(U=1\). The exact quotient is
\[
 \widetilde R_N
    =h(U)R_N+(Y-1)L_h(U)P_N
    =h(U)R_N+(h(U)-1)p_N.                                    \tag{4}
\]
Since \(A\) commutes with every central \(h(U)\), (2) gives
\[
 A\widetilde R_N=h b_N-(h-1)b_N=b_N.                         \tag{5}
\]
In particular both regular meridian lattices used to fix the
complete value are preserved, and
\(\widetilde R_N(1)=R_N(1)\). This agrees with the pointed
complete-value uniqueness statement: it does not imply
uniqueness of the whole meridian function.

This construction is rootwise and all-level. It does not supply
an off-root quantum-normal lift with the same q-jets, nor a
second actual knot invariant.

## 2. The freedom survives regularization and finite type

Assume the precise tail domination used in the scaled-profile
theorem:
\[
 \varepsilon_N=\frac{ND_N}{|K_N|}\longrightarrow0.
\]
Put \(Y=e^{z/N}\) and use the original centered full-state
monomial:
\[
 g_N(z)=F_N(e^{z/N})/K_N,\qquad
 \rho_N(z)=e^{(N-1)z/(2N)}\,NR_N(e^{z/N})/K_N .
\]
Equation (3) gives exactly
\[
 \widetilde g_N(z)=h(e^z)g_N(z).                              \tag{6}
\]
By (4) the difference between \(\widetilde\rho_N\) and
\(h(e^z)\rho_N\) is
\[
 e^{(N-1)z/(2N)}N(e^{z/N}-1)
       L_h(e^z)P_N(e^{z/N})/K_N.                            \tag{7}
\]
On every fixed compact z-set, \(N(e^{z/N}-1)\) is bounded
uniformly and \(P_N/K_N=O(\varepsilon_N)\). Hence (7) tends
uniformly to zero. Whenever the original whole regular
profile exists,
\[
 \rho_N\longrightarrow\rho
 \quad\Longrightarrow\quad
 \widetilde\rho_N\longrightarrow h(e^z)\rho .                 \tag{8}
\]
Convergence is locally uniform, including the exact resonance
centers, by (7) or by the proved uniform removable division.

For the concrete choice
\[
 h_m(U)=\tfrac12(U^m+U^{-m}),\qquad m\in\mathbb Z_{>0},
\]
the multiplier is \(\cosh(mz)\): an even entire function,
normalized to one at zero, of finite exponential type.
If \(\rho\) has finite exponential type, so does
\(\cosh(mz)\rho\). Since \(\rho(0)=1\), the latter cannot
coincide identically with \(\rho\). If a nonconstant \(\rho\)
already exists the proposed constancy inference has failed;
if \(\rho=1\), this same-operator construction gives the
explicit nonconstant comparison profile \(\cosh(mz)\).

Thus even the actual root operator and its actual bounded
affine source do not make qualitative finite exponential
type a constancy criterion. A sharp numerical type or
Laurent-degree window can impose additional constraints;
none is being discarded by this argument.

## 3. What the marked source still contributes

The comparison changes the full source and its normal jets.
For example \(h_m(U)-1\) has a second-order zero at \(U=1\);
the first meridian jet is preserved, but the second generally
is not. More generally
\[
 h(U)=1+\lambda(U+U^{-1}-2)^r
\]
preserves all orbit meridian jets of order below \(2r\),
while changing the whole profile by a finite-type multiplier.
Every prescribed finite jet budget can therefore be preserved
by choosing a larger fixed \(r\). This does not preserve all
analytic jets: the identity theorem would force an analytic
multiplier with every jet equal to one to be identically one.

The Laurent degree window also grows by \(O(N)\), and an
exact source lattice may prohibit that change. The result
therefore isolates a genuine missing premise rather than
refuting uniqueness for the fully pointed actual state.
The next comparison must retain its source lattice or its
whole normal connection; operator support, ordinary-color
values and an unspecified finite growth type do not replace it.

There is a constructive first-normal remedy. The
[source-corrected normal connection](source_corrected_quantum_normal_connection.md)
uses the same whole preoperator to turn its normal source into
a linear rule \(R_N(v)\). If the actual root section has
\(\iota(v)\ne0\), simultaneous lifting of \(v\) and \(h(U)v\)
forces \(Uh'(U)\iota(v)=0\), hence \(h\) is constant and the
anchor fixes it to one. That nonzero-symbol condition is not
automatic; the linked note gives an exact Jordan counterexample
and the actual factorial atom with its corrected connection.
