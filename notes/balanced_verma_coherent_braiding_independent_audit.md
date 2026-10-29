# Independent audit of balanced Verma coherent braiding

Audit, 27 October 2026. I checked
[the balanced Verma proof](balanced_verma_coherent_braiding.md)
against the displayed actual coefficients, the earlier
[Verma period](frobenius_verma_period.md), and the
[F-semicyclic chart](semicyclic_carry_braiding.md).
The proof is sound as stated. No additional matrix test was
needed, and no geometric-source or volume conclusion is inferred.

## 1. The lattice, divided shift, and exact resonance

Substituting \(\mathcal E=\rho^2E\) into the original Euler
coefficient gives
\[
 q^{k(k-1)/2}\frac{\rho^k}{[k]_q!}\rho^{-2k}
   =\frac{(-1)^kq^{k^2}}{(Q;Q)_k},
\]
because \((1-Q)/\rho=-q\). The displayed balanced crossing
entry follows by multiplying the \(E\)-arrows and canceling
the \(F\)-product against \((Q;Q)_k\). Its Gaussian coefficient
is polynomial, so the root specialization is regular on
each finite total-position sector, including transfers
\(k\ge N\).

On root blocks, the literal \(E\)-wrap is \(\kappa B\), while
the \(F\)-edge at every block boundary is zero. The full
\(E\)-cycle is
\[
 \mathcal E^N=(-1)^{N+1}\kappa_N B.
\]
The canceled coefficient of \(F^N/(Q;Q)_N\) is
\(\binom{(r+1)N+\bar a}{N}_Q=r+1\). Thus
\(B=\partial_t,\ T=t\) on \(t^r/r!\), with
\([B,T]=1\). The coherent kernel has the stated
\(B\)-eigenvalue and \(T\)-derivative identities.
Those are kernel identities, not a commutator-preserving
substitution \(B\mapsto s,T\mapsto\partial_s\).

For the logarithm of \(P_Q(q\mathcal E_1F_2)\), the only
extra surviving term is the resonance \(m=N\):
\[
 -\frac{q_N^N}{N}\mathcal E_1^N
       \otimes\left[\frac{F_2^N}{1-Q^N}\right]_{\rm root}
   =\mathcal E_1^N\otimes T_2.
\]
Here \(q_N^N=-1\) at every level. For \(m=jN\), \(j\ge2\),
the numerator has \(j\) vanishing factors and the denominator
one; nonresonant \(m>N\) has a vanishing numerator and a
unit denominator. The low-degree part is the logarithm
of the nilpotent finite factorial. Since \(T_2\) commutes
with \(F_2\), it commutes with the resonance. Exponentiating
therefore proves the exact factorization, with its sign.
All operations are finite on each total-position sector;
the stated product completion is defined sectorwise.

## 2. Changing centers and the inverse

The resonance translates
\[
 (s_1,s_2)\mapsto
 (s_1,s_2+(-1)^{N+1}\kappa_{1,N}s_1).
\]
Its finite head coefficient depends on \(s_1\), not \(s_2\),
so no derivative of that coefficient is lost.
The Cartan block ratio is exactly
\(x_2^{-Nr}x_1^{-Ns}\); its \(Q\)-powers are full \(N\)-cycles.
It rescales the coherent parameters exactly as in the note.

For equal colors, with
\(\chi=x^N=(-1)^{N+1}M^N\),
\[
 (-1)^{N+1}\kappa_N=\chi-\chi^{-1}.
\]
After the checked flip this gives
\[
 L_+=
 \begin{pmatrix}1-\chi^{-2}&\chi^{-1}\\
                 \chi^{-1}&0\end{pmatrix},
\quad
 L_-=
 \begin{pmatrix}0&\chi\\ \chi&1-\chi^2\end{pmatrix}.
\]
They are literal inverses and fix the stated ordered line.
The inverse finite Euler coefficient is \(q_N^k/(Q;Q)_k\);
it has no additional \((-1)^k\). The recovered original
source parameter must be used after the flip and inverse
Cartan, as the proof does.

The regular infinite braid identity restricts through
injective coherent kernels, whose head projection is the
identity. This proves scalar-one changing-source coherence.
It does not identify the new E-semicyclic chart with the
older F-semicyclic chart; their positive center transports
are oppositely oriented, consistently with their formulas.

## 3. Source independence of the whole original cut

In every finite positive crossing, an \(E\)-wrap raises
integer residue position by \(N-1\) in place of a lowering
by one. Its net change from the ordinary crossing is
therefore \(+N\). The \(F\)-factor has no wrap.
The negative inverse uses the same \(E\)- and head-\(F\)
arrows, so it has the same nonnegative wrap-degree rule.
Flips and Cartan/pivotal factors do not change this degree.

After tracing \(b-1\) strands, a term with \(r\) wraps
would have cut change \(rN\). The open index range is
\(0,\ldots,N-1\), forcing \(r=0\) and equal cut endpoints.
Thus the entire cut matrix, not only a trace, agrees
with the original nilpotent one. The argument keeps
the full pivot, zero-framing scalar and external
\(d_N(M)\) line.

On the fixed source line this is a genuine endomorphism
evaluation. Before source closure, the same degree
argument remains a coordinate-matrix contraction;
it does not define a new topological invariant.

## 4. The boundary extension and earlier Verma period

Replacing \(\kappa s\) by the independent \(\mu\) makes
every finite crossing coefficient polynomial in \(\mu\).
The center transport remains regular and linear for
equal colors. The selected-cut identity holds for
\(\kappa\ne0\), hence extends as a whole polynomial
identity to \(M=1\), with \(\mu\) fixed.

The cycle product is exactly
\[
 \mathcal E_\mu^N
   =(-1)^{N+1}u_N(M)\mu,
\quad u_N(1)=N.
\]
No singular coherent kernel with \(s=\mu/\kappa\) is
evaluated separately at the boundary.

Finally, the generic factorial basis change has poles
on the tail root blocks. It cannot identify the two
root infinite modules. It does preserve diagonal
entries on every finite total-position sector as
generic whole identities, which continue to the root.
This is compatible with the earlier graded Verma trace
and its full Alexander divisor. The finite coherent
cut is a different selected contraction, and the proof
does not delete that divisor or replace the earlier
period formula.

The resulting source centers remain triangular/reducible.
The proof therefore supplies an exact coherent source
realization of the actual cut, with the regular boundary
chart, but no irreducible geometric A-component or
selected volume asymptotic.
