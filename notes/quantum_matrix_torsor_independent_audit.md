# Independent audit of the quantum matrix/base torsor

Audit, 27 October 2026. Sections 2--4 of
[quantum_matrix_base_intertwiner_torsor.md](quantum_matrix_base_intertwiner_torsor.md)
pass this independent proof check. The noncommutative base and
weak-composition conventions are essential. No tests were rerun.

For \(DS=\zeta SD\), \(uv=(Q/\zeta)vu\), the two commutation factors
give exactly \(KE=QEK\). Distinct Laurent monomials retain distinct
\(u,v\) degrees, proving injectivity of the proposed map. Adjoining
the marked quantum roots with their stated cross relations recovers
\(D,S\), and their Fourier projectors give every matrix unit.
This is a noncommutative matrix cover, rather than a commutative
generic finite-dimensional representation.

The logarithmic scale is correct:
\[
 H=N\log(Q^N)=N^2\log(Q/\zeta),\qquad
 [X,P]=H,\quad X=N\log u,\ P=N\log v.
\]
For an independent derivation, the original \(N\)-th powers give
\(\exp(\operatorname{ad}X)P=P+H\). Since \(H\) is central, applying
the formal logarithm leaves only the first difference and gives
\([X,P]=H\). The recovered \(D,S\) commute with both logarithms,
have order \(N\), and obey \(DS=\zeta SD\). The resulting Poisson
form is \(-dX\wedge dP\), as stated.

The local root-lifting argument also preserves the quantum cross
relations. To make this explicit, suppose
\[
 ab=c^{N^2}ba,\quad u^N=a,\quad v^N=b,\quad c=Q/\zeta,
\]
with the roots marked by their scalar values at the regular root
place. Conjugation and uniqueness of these marked roots imply
\[
 b u b^{-1}=c^{-N}u,\qquad u v u^{-1}=cv.
\]
The first identity follows by taking the marked \(N\)-th root of
\(b a b^{-1}=c^{-N^2}a\); the second follows by taking that of
\(u b u^{-1}=c^Nb\). The same calculation gives the mixed
relations with \(K,E\). Thus the Hensel lift extends the whole
quantum cover, not merely its two power equations.

For the matrix splitting,
\[
 G'=\sum_i\alpha'(E_{i1})E_{1i}
\]
satisfies
\(\alpha'(E_{ab})G'=\alpha'(E_{a1})E_{1b}=G'E_{ab}\).
Its unit reduction makes it invertible. Conjugating by its inverse
therefore fixes every matrix unit, whose centralizer consists exactly
of scalar matrices over the possibly noncommutative base. This proves
the entrywise base isomorphism and the printed semilinear module map.
Holding that base map fixed leaves only central units; holding only
the matrix-unit transport fixed leaves arbitrary base units. These
two torsors must remain distinct.

The order in the coherence formulas checks directly. From
\[
 G_g\theta_g(G_h)=G_{gh}b_{g,h}
\]
one gets
\(\theta_{gh}=\operatorname{Ad}_{b_{g,h}}\theta_g\theta_h\).
Associating a triple matrix product in the two ways gives
\[
 b_{gh,k}b_{g,h}
   =b_{g,hk}\theta_g(b_{h,k}),
\]
with exactly the printed order. Central scalar cocycles arise only
after coherent base maps have been specified. The stated Hilbert-90
sum transforms by \(a_\gamma^{-1}\), so it descends the generic line
with the given cocycle convention.

The result constructs a local whole matrix/base transport from an
actual regular algebra isomorphism. It does not infer that
isomorphism, its coherent quantum base lift, source preservation,
or a nonzero selected evaluation from classical smoothness. The
separate source qualification in Section 6 is necessary.
