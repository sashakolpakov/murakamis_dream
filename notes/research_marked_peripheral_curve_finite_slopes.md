# Finite filling slopes on a marked peripheral curve

Written research proof, 22 November 2026.

This elementary algebraic adapter retains full peripheral matrices,
including noncentral unipotents. It does not construct a coefficient
of the original quantum source or prove a volume asymptotic.

## 1. The curve and its marked filling equations

Let \(C\) be an integral finite-type algebraic curve over \(\mathbb C\).
Let \(\mathcal L\) be a line bundle on \(C\), and let \(s\) be a
nonzero regular section. Locally \(\mathcal L\) is free of rank one
and \(s\) is a regular function; changing a trivialization multiplies
that function by a unit. Thus its zero set \(Z(s)\) is well defined.
A section is a unit at a point when its local representative is a unit.

Let \(U,V:C\to\mathrm{SL}_2(\mathbb C)\) be regular maps satisfying
\(U(z)V(z)=V(z)U(z)\). A slope is a primitive pair
\((p,q)\in\mathbb Z^2\), modulo \((p,q)\sim(-p,-q)\).
The marked projective filling equation is
\[
                         U(z)^pV(z)^q\in\{I,-I\}.       \tag{1}
\]
In particular the result below allows the stricter equation with \(I\).
Negative powers are regular because the matrices have determinant one.

**Theorem.** Suppose \(\langle U(z),V(z)\rangle\) is infinite at
every \(z\in Z(s)\). The number of slope classes satisfying (1) at
some zero of \(s\) is at most the number of distinct points of \(Z(s)\).
In particular it is finite.

**Proof.** On an integral curve a nonzero section is nonzero at the
generic point. Its zero set is therefore a proper closed subset.
It has dimension zero. A Noetherian zero-dimensional space has finitely
many irreducible components, each a point; here these are closed complex
points. Hence \(Z(s)\) is finite. This argument also applies on a
nonproper or singular curve.

Fix a zero \(z\), and abbreviate its commuting matrices by \(U,V\).
Suppose two different slope classes \((p,q)\), \((p',q')\) satisfy (1).
Primitivity makes
\(d=pq'-p'q\ne0\). Raising the two equations to powers \(q',-q\)
and multiplying gives \(U^d\in\{I,-I\}\); using powers \(-p',p\)
gives \(V^d\in\{I,-I\}\). Consequently
\[
                         U^{2d}=V^{2d}=I.              \tag{2}
\]
Commutativity then makes every group element one of the finitely many
\(U^aV^b\), \(0\le a,b<2|d|\). This contradicts the hypothesis.
Each zero therefore supplies at most one slope class. \(\square\)

The same proof works for a finite list of nonzero regular sections:
use the union of their finite zero sets, with the infinite-group
hypothesis at that union. It also works on an integral finite algebraic
cover where the same hypotheses hold. An unrestricted logarithmic
covering is not a finite-type algebraic curve.

## 2. The additive datum at unipotent peripheral matrices

For a fixed nonzero \(E\) with \(E^2=0\), consider
\[
 U=I+uE,\qquad V=I+vE,\qquad
 U^pV^q=I+(pu+qv)E.                                  \tag{3}
\]
If \((u,v)\ne(0,0)\), the generated subgroup is infinite and a filling
requires \(pu+qv=0\). The projective ratio \([u:v]\) records this
condition although both peripheral eigenvalues are one. A common
conjugation of the nilpotent line rescales the two coefficients
together and preserves their ratio.

For example take \(C=\mathbb A^1_\varepsilon\) and
\[
             U=I+E,\qquad V=I+\varepsilon E.            \tag{4}
\]
For every nonzero integer \(n\), slope \((1,n)\) satisfies its full
matrix equation at \(\varepsilon=-1/n\). These are distinct marked
points, even though their peripheral eigenvalue pair is constantly
\((1,1)\). Any nonzero regular section on this curve still vanishes
at only finitely many of these points.

The infinite-group assumption is separate. At a point with \(U=V=I\),
every slope satisfies (1). Hyperbolicity of a surrounding filled
manifold alone does not exclude a trivial or torsion peripheral image
on the chosen representation branch.

## 3. Why several active parameters require more

Here is a full-matrix algebraic countermodel, with no claimed hyperbolic
or Rivin realization. On \(X=\mathbb A^3_{\varepsilon_1,\varepsilon_2,
\varepsilon_3}\), set \(U_i=I+E\), \(V_i=I+\varepsilon_iE\).
Fix a nonzero integer \(n_0\), and put
\[
 s=\varepsilon_1+1/n_0+\varepsilon_2-\varepsilon_3.
                                                               \tag{5}
\]
It is a unit at the origin and restricts nontrivially to every coordinate
subspace through the origin. Nevertheless it vanishes at
\((-1/n_0,-1/n,-1/n)\) for every nonzero integer \(n\), where the
three full filling slopes are \((1,n_0),(1,n),(1,n)\).
After fixing the first coordinate, its restriction is
\(\varepsilon_2-\varepsilon_3\), nonzero even on either coordinate
axis but zero on this infinite diagonal family. A nonzero section
on a higher-dimensional parameter space need not give finite bad slopes.

## 4. Conditional meaning for the original quantum source

An application would first need an actual nonzero regular source
coefficient section on such a marked algebraic curve, possibly on a
finite algebraic cover, and the stated infinite peripheral groups at
its zeros. These are hypotheses, not consequences of a formal
Gaussian prefactor or equality of peripheral eigenvalues.

Suppose independently that, for every fixed filling under consideration,
the whole original marked quantum source has a controlled asymptotic
with this leading section, nonzero remaining factors, and the required
global gap, and that its action has the actual filled-volume value.
Then outside the finite slope set above its leading coefficient is
nonzero. If finitely many level classes have different sections, use
their finite union. The filling is fixed before the quantum level tends
to infinity; no joint level/slope uniformity is inferred.

None of those quantum or geometric hypotheses is proved here. A zero
of the leading section is not a counterexample to a volume limit:
a later coefficient may retain the same rate. The result is
one-dimensional and does not settle arbitrary fixed short partial
fillings or the finite-exception program.

The finite-zero and commuting-matrix arguments are standard elementary
mathematics; no general novelty or external theorem premise is claimed.
Only written mathematics and text operations were used. No earlier
final, public manuscript, mathematical program, test, build, or git
operation was changed or run.
