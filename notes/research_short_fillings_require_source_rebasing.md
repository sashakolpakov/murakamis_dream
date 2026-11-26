# Why a short filling can require a different source window

21 November 2026. Research audit. The frozen manuscripts and earlier
final notes remain unchanged.

The all-long filling theorem uses a window near the complete colors of
the original augmented link. That window need not contain the source
which survives a short partial filling. At a permitted zero physical
crossing power it is annihilated exactly, before taking any limit.

This note records that finite identity and identifies the precise
large-twist comparisons in the frozen proof. It does not question the
theorem within its stated long-filling regime. It also does not prove a
new short-filling volume identity. Its purpose is to distinguish the
analytic task still required from the exact boundary assembly already
established in the recent research notes.

## 1. The complete-color window in the frozen argument

Fix a strict Conway construction with \(b\ge2\) labeled crossing
circles. At level \(N\), write \(d=N-1\) and
\(P_N(X)=2T_N(X/2)+2\), with \(T_N\) the Chebyshev polynomial
of the first kind. At one original disk,
the full physical crossing power has the exact expansion
\[
 R^n=\kappa^n\sum_{j=0}^{N-1}\beta_j^{n/2}L_{j+1},
 \qquad L_{j+1}(X)=(-1)^jU_j(X/2),
 \qquad \kappa=e^{\pi i d^2/(2N)}.                    \tag{1}
\]
Here \(U_j\) is the Chebyshev polynomial of the second kind, and
\(L_{j+1}\) is the actual ordinary circle of color \(j+1\).
The coefficients are those of the full Hermite quotient
\(\mathbb C[X]/(2T_N(X/2)+2)\), including its repeated-root
directions. In particular (1) holds for zero, positive, and negative
integers \(n\). Its superscript \(n/2\) does not require \(n\)
to be even.

The physical crossing power and the original primitive surgery
coordinate obey
\[
                         n=\epsilon-2p,
 \qquad \epsilon\in\{0,1,-1\},\quad p\in\mathbb Z.    \tag{2}
\]
Thus the zero-power case below is an allowed partial filling when
\(\epsilon=0\) and \(p=0\). We do not assert that it occurs in
a fixed odd-parity pattern.

The complete-color window retains color deficits
\[
              h=N-1-j,\qquad 0\le h\le H_N^{\rm cut},
                         \qquad H_N^{\rm cut}<N-1,      \tag{3}
\]
at every original disk. The strict theorem takes a small fixed-fraction
window, so the last inequality holds at all sufficiently large levels.
Every retained color in (3) has \(j\ge1\). Its even holomorphic
extension and finite Fourier polynomial are built only after the
physical high-color source has been separated from its complement.
They do not change this finite support fact.

## 2. Exact annihilation at a zero power

**Proposition.** If one physical power in (1) is zero, filling that
coordinate annihilates any source restricted there to the window (3).
The assertion holds for every choice of the other physical powers and
every adjoining exterior tensor.

**Proof.** The ordinary circle polynomials \(L_{j+1}\),
\(0\le j<N\), form a basis of the full quotient: their degrees
are distinct and below \(N\), with nonzero leading coefficients.
Since \(R^0=1=L_1\), uniqueness of its expansion gives
\[
                            \beta_j^0=\delta_{j0}.       \tag{4}
\]
Every index retained in (3) is different from zero. Its coefficient
in (4) is therefore zero. The original network is linear in the
operator at that disk, so the entire restricted contribution vanishes
regardless of all its other tensors. All original phase carriers
remain in (1); at this disk \(\kappa^0=1\). No derivative at a
double node, alias, or asymptotic estimate is removed in this argument.
\(\square\)

The full evaluation need not vanish. Equation (4) says that it is
carried by the lowest color at that disk, which belongs to the
complement of the old window. Thus a statement that this complement
is negligible relative to a surviving contribution of the old window
cannot hold in this situation.

This is a limitation of that particular decomposition, not of the
volume identity. The existing
[strict padding proposition](research_finite_exceptions_under_partial_fillings.md#8-a-consequence-of-counting-assignments-strict-padding)
also gives actual hyperbolic instances. For any fixed hyperbolic strict
core \(K=C(Q)\), its padded templates have a permitted zero leaf
and infinitely many assignments representing the same \(K\).
To specify the source normalization, the
[Newton source theorem](actual_newton_turn_positive_gram.md) uses
\[
 e_r(X)=\frac{\prod_{j=0}^{r-1}(c_j-X)}{S_r^2},\quad
 c_j=2\cos((2j+1)\pi/N),\quad
 S_r=\prod_{j=1}^r2\sin(\pi j/N),
\]
with empty products one, \(Je_r=e_{d-r}\), and
\(\phi_N(f)=(-1)^dN^2[X^d]\operatorname{rem}_{P_N}f\).
Since \(S_d=N\), \(c_d=c_0\), and
\(e_d=(-1)^dP_N/[N^2(X-c_0)]\), multiplication by any canonical
\(f\) gives \(e_df=f(c_0)e_d\) and \(\phi_N(e_d)=1\).
Moreover \((JQ)(c_0)=\phi_N(Q)\) by coefficient reversal.
The exact original source identity, up to the already specified
framing phase, is
\[
 \phi_N\bigl(e_dR^aJQ\bigr)
       =R^a(c_0)(JQ)(c_0)=\kappa^a\phi_N(Q).            \tag{5}
\]
Here \(J\) is the actual turn, \(e_d=J1\) the zero filled leaf,
and \(\phi_N\) the original marked Frobenius source. For cores in
the frozen all-long family, the full right side is eventually nonzero
with its proved positive hyperbolic-volume rate. Nevertheless the old
complete-color corridor at the padded zero disk vanishes by (4).
The cap isotopies, original marking, strictness, and knot-component
check used in this example are supplied by the cited complete padding
proof, not inferred just from a polynomial coincidence.

## 3. The quantitative large-twist comparisons

There are separate uses of large powers in the frozen proof. They must
not be replaced by the claim that a geometric critical point is unique.

First, the exact pure source has a holomorphic expansion near the
complete point with a nonzero amplitude. Its Fourier action is a germ
\(\Psi_0\), and the filled critical action is obtained from
\[
 \Psi_0(z)+\pi i\sum_j n_jz_j^2+2\pi i\sum_j\ell_jz_j. \tag{6}
\]
The all-unit-charge critical point is proved to lie inside this fixed
germ when all \(|n_j|\) are sufficiently large. The same small-domain
argument proves the positive imaginary displacements, negative real
Hessian, nonzero sine factors, and the charge comparisons. No theorem
in these files places every short-filling geometric critical point in
that germ or provides a new exact local source expansion there.

Second, errors are bounded at rates referenced to the complete value
\(F_0\). The full physical source differs from the selected corridor,
after filling, by at most
\[
 \prod_j2N(1+|n_j|/2)\,
                         e^{N(F_0-\gamma_*)},
                       \qquad \gamma_*>0.               \tag{7}
\]
The product is polynomial in \(N\) for any fixed filling tuple.
This useful bound is valid without concluding that its exponential
rate is below the filled geometric action. If a continued candidate
has action \(S\), the bound (7) alone is strictly lower than its
rate only when
\[
                              F_0-\Re S<\gamma_*.        \tag{8}
\]
The actual long-filling proof uses the stronger margin
\(F_0-\Re S_{\boldsymbol n}<\gamma_*/2\), obtained from
\(F_0-\Re S_{\boldsymbol n}=O(\sum_jn_j^{-2})\).
This is an estimate within the proved germ. It cannot be evaluated at
an arbitrary short tuple by substituting it into that asymptotic formula.

Third, the whole oscillatory filling theorem bounds contour side faces,
bounded nonlocal charges, distant charges, and the real exterior of
the local cube by rates of the form
\(F_0-\gamma_\nu\), with fixed positive margins. It chooses the
large-power threshold so that the all-unit action drop is smaller
than one quarter of every such margin and so that the unit charge lies
in the local range. The exact infinite-charge identity itself holds at
every fixed integer power. Its absolute convergence at fixed \(N\)
does not supply these comparisons with the filled leading term.

For example, the distant-charge cutoff
\(M_j=\lceil |n_j|/2+D\rceil\) still defines a finite retained
charge set for a short nonzero power. This does not identify which of
those retained charges contributes, nor bound their sum below the
desired geometric rate. The longness restriction is not merely a
technicality in summing infinitely many charges.

The final geometric comparison is also local to the complete branch:
the primitive classical shear, its retained logarithms, and the metric
completion identify the action there with the original knot-complement
volume. Hyperbolicity of a final short filling does not itself prove
that a formal continuation of (6) remains that same marked branch.

## 4. Consequence for the active finite-exception target

The target retains every fixed short partial filling which has
hyperbolic descendants, including the permitted zero leaves above.
It therefore needs a source presentation adapted to the partial
filling, or an equivalent whole-source argument including the old
complement. It cannot universally keep the old high-color corridor as
the surviving geometric term.

The recent exact convex boundary elimination retains the entire short
component, including the low colors in (4). It resolves an algebraic
assembly issue. To finish the volume argument one still needs actual
quantum boundary data with a positive lower certificate and matching
upper rate at the partially filled geometry. The inequalities (7)--(8)
explain why the old complete-source gap does not provide that upper
rate automatically. The exact vanishing in (4) explains why a nonzero
coefficient of the old corridor is not always the right lower-bound
target either.

This audit establishes no new volume-conjecture class. It rules out a
specific proposed extension of the frozen proof and identifies the
source which a successful short-filling theorem must retain.

## Complete matching sources and scope of this audit

All six complete matching files below were read. The first specifies
the frozen theorem and its quantifiers; the second gives the exact
circle expansion and the final error comparison; the third constructs
the pure window; the fourth gives the whole-charge estimates; the
fifth supplies the already proved marked padding construction. The
sixth fixes and proves the full Newton normalizations used in (5).

| Source | SHA-256 |
|---|---|
| [Conway asymptotics: theorem and conventions](../papers/conway-asymptotics/main.tex) | 98d34dcfe31f89e5c7c7f904da93f375386e9a94a113972fb0a8e78e08b0ca7b |
| [Integer powers and the full filling comparison](../papers/conway-asymptotics/filling.tex) | 215c5d27ef5c0d1e8abbeaae379ef6bdfbbb63ae92a654722b222f685b0c6036 |
| [Strict pure source window](../papers/conway-asymptotics/pure-window.tex) | 2832ccd4ad37a43f9f63c28124832d21c7242401fd0906f0b9f35c07829a45b8 |
| [Whole oscillatory filling proof](../papers/oscillatory-fillings/main.tex) | 275d76a8e12d963c6a4fc45bb828e0b7742761c94e4242272f15c64b56f3f203 |
| [Finite exceptions and marked strict padding](research_finite_exceptions_under_partial_fillings.md) | b9c7a1021de618c1f44ab4b645f98068bd5188f93e51928c1d5de5a55870c566 |
| [Original Newton source and turn](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |

The finite vanishing proposition is proved above. The audit checks the
explicit scope and uses of the displayed estimates. It is not a fresh
proof audit of every analytic, algebraic, and geometric companion
imported by those manuscripts.

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical computation, build, git operation
or edit to a frozen manuscript was performed.
