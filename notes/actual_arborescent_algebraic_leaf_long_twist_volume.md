# Long twists in Conway tangles with an algebraic leaf certificate

31 October 2026. This research theorem enlarges the previously proved
three-or-more-leaf seed grammar to include two-leaf seeds. Its additional
hypothesis is a finite inequality on the selected complete geometric
solution. The conclusion concerns the original invariant and the
**hyperbolic volume of the knot complement**. It is not a theorem for all
arborescent knots.

## 1. The precise class and conclusion

Let \(\mathcal R\) denote the literal quarter-turn of an ordered tangle,
and let \(h=\mathcal R(L_N)\) be the original complete crossing-circle
coupon. Use distinct leaves in each seed and form a fixed finite expression

\[
 A_s=h^s,\quad s\ge2,\qquad
 E::=A_s\mid\mathcal R(E)\mid E_1E_2.                 \tag{1}
\]

Stacking and turning retain the original strand order, cups, caps,
disk framings and scalar normalization. Close \(FG\) by the original
cylindrical closure \(C(FG)\), where both children belong to (1).
The isolated closure \(C(A_2)\) is excluded.

At the unique strict complete optimizer, let \(a_\ell\) be the original
leaf coordinate, and put \(X_\ell=\cot(\pi a_\ell)>0\). Assume

\[
                    X_\ell\ge\frac23
             \quad\text{at every leaf}.                \tag{2}
\]

Choose a fixed retained half-twist pattern
\(\epsilon_\ell\in\{0,1,-1\}\) whose endpoint pairings give one main
component without internal circles. At each auxiliary crossing circle
insert the independently chosen disk-framed full twist \(R^{-2p_\ell}\).
Thus, after all auxiliary circles have been filled, the actual leaf is

\[
             \mathcal R(R^{\epsilon_\ell-2p_\ell}).     \tag{3}
\]

**Theorem.** For each fixed expression and such half-twist pattern there
is a finite threshold \(T(E,\epsilon)\) such that, whenever the fixed
signed integers \(p_\ell\) all satisfy \(|p_\ell|>T(E,\epsilon)\), the
resulting knot \(K_{E,\epsilon}(p)\) is hyperbolic and

\[
 \lim_{N\to\infty}\frac{2\pi}{N}
      \log\left|K_N\bigl(K_{E,\epsilon}(p)\bigr)\right|
   =\operatorname{Vol}\bigl(S^3\setminus K_{E,\epsilon}(p)\bigr).
                                                               \tag{4}
\]

Here \(K_N\) is the original marked one-cut invariant with its recorded
enhancement. The reduced enhanced Kashaev normalization has an outer
factor of unit modulus; the full modified one-cut normalization differs
by the recorded factor of modulus \(1/N\). Neither changes (4). This is
the comparison proved in the original
[normalization theorem](actual_complete_augmented_source_normalization.md)
and [crossing calculation](kashaev_crossing_and_period_lattice.md), not a
new normalization chosen to force a volume limit.

The diagram and slopes are fixed before \(N\) tends to infinity. Both
parities and composite levels are included. Slopes may have different
signs and unrelated magnitudes. There is no bound on the number of
leaves, branching or turn depth, but the threshold is allowed to depend
on the fixed expression. The knot cusp is never filled: the fillings
in this construction remove only the auxiliary crossing-circle cusps.

## 2. Why the condition is finite and algebraic

The geometry selects real \(B\) and positive \(X,Y\), with
\(B=\cot(\pi b)\) and \(X^2+Y^2-B^2=1\). For a two-leaf seed,

\[
          B=X-\frac1{2X},\qquad Y=\frac1{2X}.           \tag{5}
\]

For a seed of width \(s\), the corresponding formulas are
\(B_s=T_s(X)/U_{s-1}(X)\) and \(Y_s=1/U_{s-1}(X)\), on the
branch with the original positive product denominators. Products use
the original rational port rules; turns send
\((B,X,Y)\) to \((-B,Y,X)\); the two root ports match as
\((B,X,Y)\) and \((-B,X,Y)\). Thus (2) is checked on the selected
complete gluing branch by the polynomial inequalities

\[
                    X_\ell>0,\qquad 9X_\ell^2\ge4.    \tag{6}
\]

The branch signs and nonzero denominators must be retained. Squaring
equations and testing an arbitrary root of their elimination ideal is
not the criterion. No quantum limit must be computed to test (6).
More precisely, keep intermediate seed ports and all branch inequalities
when clearing the positive denominators. These are equations and
inequalities over \(\mathbb Q\), using rational tangent coordinates
to record the strict angle branches if needed. The local equivalence
with the critical-wire equations and their nonsingular Hessian makes
the selected point isolated. An isolated point of a semialgebraic set
over \(\mathbb Q\) has real-algebraic coordinates. Rational isolating
boxes and the retained branch signs therefore turn (6) into an exact
algebraic sign test. This does not require the entire complex solution
variety to be zero-dimensional.

The complete geometry proves, for every proper seed of width \(s\),

\[
       \cos\frac{\pi}{s+1}<X_\ell<1.                 \tag{7}
\]

Consequently every old proper seed with \(s\ge3\) passes (2)
automatically. Only the new two-leaf seeds require a test; by (5) it
is equivalently \(Y_2\le3/4\). The previously proved isolated
closures \(C(A_s)\), \(s\ge4\), also retain their original theorem.

There are actual passing expressions with the new seeds. For
\(C(A_2\mathcal R(A_2))\), both seed ports are
\((0,1/\sqrt2,1/\sqrt2)\), which are fixed by the turn and match
at the root. Their leaves have \(a=\arctan(\sqrt2)/\pi\), all
retained gates are strict, and \(X^2=1/2>4/9\). Strict concavity
identifies this stationary solution with the complete optimizer.
This is a genuine addition to the literal grammar; no topological
novelty claim about its resulting knots is needed.

## 3. Source and geometric proof

The new issue in admitting \(A_2\) is real: at even level its Newton
support stops at \(N-2\), not \(N-1\). The proof does not restore
that missing coefficient by changing the source. For any prescribed
interior seed output \(b\), choose

\[
                  b/2<a<\min(b,1/2).                  \tag{8}
\]

The two leaves and their product are then strict. This construction
propagates through actual turns and products. At the closed root the
only deleted gate has exact coefficient one and inputs summing to
\(d=N-1\). Contract turns and solve that root relation integrally;
all remaining wire coordinates form the original primitive lattice.
Rounding a strict continuous state in these free coordinates gives
admissible states at every sufficiently large level, including even
levels. No relation \(2r=d\) is introduced. The original uniform
factorial estimates and polynomial state count therefore give the
complete variational limit.

The boundary barrier and strict concavity give a unique interior
optimizer and a negative definite reduced Hessian. The complete port
inequality \(-Y<B<X\) starts already at (5), propagates under the
same operations, and proves (7). Every complete leaf lies in
\((1/4,1/2)\). The unchanged local ideal cells, ordered face maps,
closed bowtie cut, edge words and cusp decorations construct the
actual complete augmented link complement. The same local shaded
pairings handle every retained half-twist pattern. These arguments
are written in the [source extension](actual_conway_two_leaf_seed_source.md)
and [geometric extension](actual_conway_two_leaf_seed_geometry.md).

What is new analytically is the quantitative alias estimate. Define

\[
 \begin{split}
 J(x)&=\int_0^x\log(2\sin\pi t)\,dt,\\
 g(a)&=J(2a)-4J(a),\qquad k(u)=-2J(u/2).
 \end{split}                                           \tag{9}
\]

The [exact leaf certificate](actual_conway_algebraic_leaf_alias_certificate.md)
proves, whenever \(1/4\le a\le\arctan(3/2)/\pi\),

\[
 k(u)\le g(a)+g'(a)(u-a)-\frac1{2500},
                         \qquad 0\le u\le1.           \tag{10}
\]

The core envelope has the same supporting plane without this loss,
and equality only at the complete leaf. Add the original product
supporting planes. All linear terms cancel by the actual closed-wire
stationarity equations. Hence every nonempty alias subset has a
strict loss, uniformly over its full physical range. The all-core
majorant has the same unique complete maximum, giving the remaining
physical-color complement gap. All original normal terms, endpoint
offsets and both level parities are retained.

Inside a fixed strict complex neighborhood the old local coefficient
interpolation applies, because its hypotheses are \(1/4<a<1/2\)
and strict factorial arguments, not a seed-width condition. With
\(H\) leaves the primitive wire lattice has dimension \(2H-3\).
The leaf and gate powers together with its Gaussian sum give the
same finite analytic packet

\[
 C_N^\epsilon(\chi)
    =N^{3/2}a_\epsilon(\chi)e^{N\Phi_\epsilon(\chi)}
                      \bigl(1+O(N^{-1})\bigr),
              \qquad a_\epsilon(0)\ne0.                \tag{11}
\]

The original integer shifts and normalization remain in this formula.
Restoring the original source also restores its explicitly stripped
unit phase \(\eta_N=\exp[(i\pi(N-1)/4)\sum_\ell\epsilon_\ell]\).
Its color Hessian is diagonal at completeness, with entries
\(-2\pi X_\ell/(1-\epsilon_\ell iX_\ell)\), whose real parts
are negative. Equations (10)--(11), together with the whole complement
gap, verify the hypotheses of the existing
[original-source filling transfer](general_original_source_long_filling_transfer.md).
It proves a nonzero full-sequence asymptotic for the original finite
invariant, not only for a selected saddle contribution.

For completeness, the action selected by that transfer is

\[
 S_{\epsilon,p}(\chi)=\Phi_\epsilon(\chi)
       +\frac{\pi i}{2}\sum_\ell\frac{(\chi_\ell-1)^2}{p_\ell}.
                                                               \tag{12}
\]

The marked geometric extension retains
\(U_\ell=-2\pi i\chi_\ell\),
\(V_\ell=-2\partial_\ell\Phi_\epsilon\), and the absolutely
calibrated primitive \(G=2\pi i\Phi_\epsilon\). At its selected
small saddle, (12) imposes the original primitive filling equations
\(U_\ell+p_\ell V_\ell=-2\pi i\). The complete-volume anchor and
the original representation-volume differential give

\[
 2\pi\Re S_{\epsilon,p}(\chi_*)
       =\operatorname{Vol}\bigl(S^3\setminus K_{E,\epsilon}(p)\bigr).
                                                               \tag{13}
\]

The bounded marked branch completes to the intended smooth
hyperbolic knot complement. Combining the full invariant asymptotic
with (13) proves (4).

## 4. Arborescent scope and the remaining general problem

Each all-filled leaf (3) is a rational tangle. Actual stacking and
quarter-turns preserve Conway algebraicity, so their prescribed
one-component closure is an arborescent knot. The old loop-free
endpoint induction also extends: a two-leaf seed realizes the two
types \(I,U\), turns permute types, and products retain at least
two feasible choices while avoiding the circle-producing pair.
Thus every expression has a constructible knot parity pattern.
Full twists preserve that endpoint pattern.

The strongest tangent version replaces (2) by
\(a_\ell<a_{\mathrm{crit}}\) at every leaf, where \(a_{\mathrm{crit}}\) is
the unique root in \((\arctan(3/2)/\pi,1/3)\) of

\[
 g(a)+(1-a)g'(a)=0.                                    \tag{14}
\]

Condition (2) is the simpler algebraic sufficient test, with an
explicit uniform margin. It is not automatic for every two-leaf
tree. For example, the strict complete optimizer of
\(C(A_2\mathcal R(A_4))\) has two leaves with
\(X=1/\sqrt3\), or \(a=1/3\); their tangent at the genuine alias
endpoint \(u=1\) has negative deficit. This disproves an automatic
application of this supporting-plane argument. It does not disprove
the full source gap or the volume conjecture for that expression.

The next general problem is therefore concrete: control the original
closed-source aliases when local tangent deficits are not individually
positive, allowing compensation through the shared tangle constraints,
or find a different estimate preserved under the actual contractions.
The theorem above allows any finite number of suitably certified
tangles and independently long twists; it does not remove the
geometric certificate or cover every arborescent template. Nor does
it construct a generic main-meridian quantum A-operator. The selected
algebraic boundary branch, its logarithmic lifts and its calibrated
period remain essential data beyond an elimination polynomial.
