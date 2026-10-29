# Independent audit of the common-Verma two-wall source

Audit, 27 October 2026. The proof in
[common_verma_two_wall_source.md](common_verma_two_wall_source.md)
is sound as stated. I checked the module, boundary maps,
excursion factor, extension class, coherent action, and
marked peripheral period directly. No new test run was needed.

## 1. The actual module and the two rank-one edges

With \(\delta=1-Q^N\) and \(w=MQ^{-N}-M^{-1}\), the
Jacobian in \((\log Q,\log M)\) at the marked point is
\[
 \begin{pmatrix}-N&0\\-N&2\end{pmatrix},
\]
of determinant \(-2N\). The walls are independent.
Adjacent products of the infinite coefficients give
\([\mathcal E,F]=\rho(K-K^{-1})\), including at index zero.
Thus the infinite object is a genuine module before
either wall is imposed.

The only head-to-tail \(F\)-edge is \(\delta U\);
the only tail-to-head \(\mathcal E\)-edge is \(wL\).
Their block multiplication gives
\[
 [F,P]=\delta U,\qquad [\mathcal E,P]=-wL,
\]
and the head commutator has defect
\(-\delta w\,LU=-\delta wP_{N-1}\).
The odd two-corner matrix squares to \(\delta w I\).
The source-coupon formulas follow by the same block
multiplication, with the stated signs.

At \(\delta=0\) the head is a submodule. At \(w=0\)
the tail is a submodule and the head is the quotient.
Near \(M=1\), the latter wall is the genuine integral
color \(M=-q^N\), rather than the fixed-root meridian
direction. These orientations are not conflated.

## 2. The braid excursion adapter and the Bockstein

The displayed balanced crossing coefficients agree
with the actual canceled factorial coefficients.
On head inputs, exiting through \(F\) has a Gaussian
numerator \(1-Q^N\) and no zero denominator, hence a
factor \(\delta\). Returning from a tail input through
\(\mathcal E\) crosses index \(N\) and has the factor
\[
 1-M^2Q^{-N}=-Mw.
\]
The inverse has the same property with its transfer
directions exchanged.

Every nontrivial ambient head-to-head path has a first
exit and return, hence a factor \(\delta w\). All
calculations take place in a finite invariant
total-position sector, so the path expansion has no
infinite convergence issue. At the node, division by
\(\delta w\) retains exactly the single-excursion
terms. The resulting adapter need not have rank one,
as the note correctly states.

At the fixed root,
\[
 \mathcal E^N=\gamma\kappa_N B,\qquad
 \gamma=(-1)^{N+1}.
\]
On the first two blocks, its derivative at \(M=1\)
is \(\gamma2N\begin{pmatrix}0&I\\0&0\end{pmatrix}\).
The zeroth central operator is zero, so a regular
first-normal change of splitting contributes a
commutator with zero and cannot remove this term.
A direct sum of the two head families has the
central operator identically zero. This proves
non-splitting of the stated first-normal extension;
it is stronger than a nonzero unclosed current.

## 3. Weyl orientation and the literal centralizer action

The divided \(F\)-matrix coefficient is
\(\binom{a+N}{N}_Q\), whose root value is \(r+1\)
on block \(a=rN+j\). Hence \(B=\partial_t,\ T=t\)
on \(t^r/r!\), and \([B,T]=I\).
The coherent-kernel identities have the stated
orientation; treating \(B\mapsto s,T\mapsto\partial_s\)
as a direct algebra homomorphism would be incorrect.

For \(\lambda_b=1+\kappa_Nb\),
\[
 U_bf(t)=e^{bt}f(\lambda_bt).
\]
Direct composition gives
\[
 U_bU_cf(t)=
 e^{(b+c+\kappa_Nbc)t}
 f((1+\kappa_N(b+c+\kappa_Nbc))t),
\]
which is the exact regular-centralizer group law.
Its coherent action is
\(s\mapsto\lambda_bs+b\), with anchor \(s=0\);
the locus \(1+\kappa_Ns\ne0\) is a genuine torsor.
The infinitesimal operator is \(T(1+\kappa_NB)\),
in that order. It changes the central source
character and is not claimed to be a fixed-fiber
quantum-group intertwiner.

## 4. The marked relative period and its scope

The head projection satisfies
\(\pi_0U_b\theta_0=I_H\) exactly. Applying the original
normalized head cut therefore gives the scalar
matrix coefficient one, before integration.
With the retained endpoint \(b=M^N\), the invariant
form integrates to
\[
 \frac{\Log(M^{2N})}{\kappa_N}
 =\frac N{u_N(M)}
       \frac{\Log(M^2)}{M-M^{-1}}.
\]
The complete value is one. The normalization and
the direction of the adapter \(u_N/N\) are correct;
the logarithm sheet and whole peripheral divisor
are not discarded.

The earlier unbalanced factorial basis change is
singular on tail root blocks. The proof correctly
does not identify the two infinite root lattices
or remove the earlier Alexander denominator.

The source remains an E-semicyclic/reducible
centralizer object. No map to the irreducible
hyperbolic framing class, selected Bloch regulator,
or volume norm is asserted. The explicit source
and Bockstein data are valid inputs for such a
future comparison, not a substitute for it.
