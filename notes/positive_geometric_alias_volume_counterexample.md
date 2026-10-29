# A positive geometric triangulation with an oversized integer-alias face

Research note, 28 October 2026.

**Universal wrong-edge alias-face volume domination is false, even for a
positive complete ideal triangulation of a hyperbolic knot, with the
complete marked meridian retained and the integer alias lattice enforced.**

This is a counterexample to a proposed intermediate geometric bound, not
to the volume conjecture. No nonzero coefficient of the face in the
original quantum cycle is asserted. Precisely that source-selection
question is indispensable.

All numerical inequalities below are proved by outward-rounded Arb
enclosures. Angle and lattice equations are checked by exact rational
arithmetic. Complete shapes and holonomy products are verified in an
explicit cubic field. The six topological moves are independently legal
in Regina; the initial triangulation is isomorphic to our previously
audited three-tetrahedron $5_2$ triangulation.

Artifacts:

- `experiments/audit_positive_alias_volume_counterexample.py`;
- `experiments/positive_alias_volume_counterexample_fixture.json`;
- `experiments/positive_alias_volume_counterexample_results.json`.

Run `python3 experiments/audit_positive_alias_volume_counterexample.py`.
The optional `--topology` additionally uses the installed Regina package
to replay and verify every move. In this workspace the complete rerun is:

```sh
PYTHONPATH=.venv/lib/python3.14/site-packages python3 experiments/audit_positive_alias_volume_counterexample.py --topology
```

## 1. The actual triangulation

Start with the standard three-tetrahedron $5_2$ triangulation. With
indices starting at zero, perform the following $2\to3$ moves, each
specified by (tetrahedron, opposite-face vertex):

\[
 (1,0),\ (2,1),\ (2,0),\ (1,2),\ (5,3),\ (1,0).
 \tag{1}
\]

All face permutations before and after each move are in the fixture.
The resulting nine-tetrahedron triangulation has isomorphism signature

```
jvLALQQcedhgighiifvfdxbfjrf
```

For every step, the audit reconstructs the edge-angle matrix from the
face permutations, checks one ideal vertex and torus vertex link, and
verifies complete positive shapes. Thus positivity is not a numerical
assumption about a large triangulation reached by randomization.

The field generator is the upper-half-plane root of

\[
 a^3-2a^2+3a-1=0,
 \qquad a\approx0.7849201454990+1.3071412786820i.
\]

The initial shapes are $a,\ 2-a+a^2,\ a$ in the recorded ordering
(equivalently, the exact coefficients in the fixture). The final shapes
are

\[
\begin{split}
 &\frac{121-80a+52a^2}{25},\quad
 1-4a+4a^2,\quad 17-12a+8a^2,\\
 &2-3a+2a^2,\quad -4+2a-a^2,\quad a^2,\\
 &2-3a+2a^2,\quad\frac{44-29a+19a^2}{7},\quad a^2.
\end{split}                                                   \tag{2}
\]

The audit isolates $a$, proves that all shapes at all seven stages lie
strictly in the upper half-plane, and verifies all edge and both
peripheral products by exact polynomial reduction. The marked logarithmic
sums are $2\pi i$ at each edge and zero at both peripheral curves.
They give complete positive metrics. Their common Bloch--Wigner volume
is rigorously enclosed near

\[
 V_g=2.82812208833078316276389880927663494277\ldots.              \tag{3}
\]

## 2. A rational wrong-edge face point

Write the three angles of tetrahedron (j), in units of \(\pi\), as
($ (a_j,b_j,c_j) $). Consider

\[
\begin{array}{c|ccc}
j&a_j&b_j&c_j\\\hline
0&0&1/20&19/20\\
1&0&2/5&3/5\\
2&0&1/10&9/10\\
3&1/2&3/10&1/5\\
4&1/10&1/20&17/20\\
5&13/20&3/20&1/5\\
6&1/2&3/10&1/5\\
7&17/20&1/10&1/20\\
8&13/20&3/20&1/5
\end{array}                                                    \tag{4}
\]

Each triple sums to one. Let (E) be the actual edge-angle incidence
matrix saved in the fixture, in its recorded edge ordering. Direct exact
multiplication gives

\[
 E\alpha=2k,\qquad
 k=(1,1,1,1,1,1,2,0,1)^T.                                    \tag{5}
\]

The zero-winding edge meets exactly tetrahedra (0,1,2); they are flat.
The other six tetrahedra are strictly positive.

The marked meridian row is

\[
 \mu(\alpha)=-c_1+c_2-c_6-b_7.
\]

At (4) it is **exactly zero**, its complete marked value. The second
recorded peripheral row also evaluates to exactly zero; the audit checks
both. Thus the example
does not merely satisfy edge windings while dropping the peripheral
condition.

## 3. The defect belongs to the actual integer alias lattice

For each tetrahedron choose the cyclic quad rotation

\[
 r=(2,2,0,2,2,1,0,0,0).                                     \tag{6}
\]

This permutes positive geometric shape types cyclically and preserves
their positivity. Use edges (0,1,2,3,5,6,7,8), together with the marked
meridian, as the nine gluing rows. If their rotated incidence blocks are
(G_0,G_1,G_2), set

\[
 A=G_0-G_1,\qquad B=G_2-G_1.
\]

In the recorded ordering,

\[
B=\begin{pmatrix}
0&1&0&0&0&0&0&0&-1\\
0&0&0&1&1&1&-1&1&0\\
0&0&-1&0&-1&0&0&0&0\\
1&0&-1&0&0&0&1&-1&0\\
0&0&0&0&0&1&0&0&0\\
1&-1&1&1&0&-2&0&-1&1\\
-1&-1&0&0&0&0&0&0&0\\
-1&0&0&-1&0&0&0&0&0\\
0&0&1&0&0&0&-1&1&0
\end{pmatrix},\qquad\det B=-2.                              \tag{7}
\]

The actual full marked defect is

\[
 d=(0,0,0,0,0,1,-1,0,0)^T.
\]

It has the **integer** preimage

\[
 \boxed{\quad Bm=d,\qquad
 m=(0,1,0,0,0,0,-1,-1,1)^T\in\mathbb Z^9.\quad}              \tag{8}
\]

The audit also checks $AB^T=BA^T$. In the notation of the positive
Legendre chart, $C=B^{-1}A$ is symmetric, and with the original complete
mark \(\kappa\), point (4) satisfies exactly

\[
 \gamma=\kappa-C\theta+2m,\qquad
 \theta,\beta,\gamma\geq0,\qquad
 \theta+\beta+\gamma=\mathbf1,                              \tag{9}
\]

where angles are measured in units of $\pi$. It therefore belongs to
the **weak nonnegative alias angle locus** of the genuine
integer-shifted potential $W_m$, not just an
unrestricted edge-defect assignment or a rational shift on a larger
unrecorded phase cover.

The strictly positive alias locus is empty: a zero-winding edge forces
zero angles. Accordingly, this weak locus is **not** the topological
closure of a nonempty positive alias cell. No limiting chain or source
coefficient is inferred from (9).

## 4. Its volume is strictly greater than the hyperbolic volume

The three flat tetrahedra contribute zero. Summing the other six gives

\[
\begin{split}
 V_{\mathrm{alias}}=2\big[&\Lambda(3\pi/10)+2\Lambda(\pi/5)
              +\Lambda(\pi/10)\\
              &+\Lambda(\pi/20)-\Lambda(7\pi/20)\big].
\end{split}                                                   \tag{10}
\]

Arb proves

\[
 3.76403<V_{\mathrm{alias}}<3.76404,
 \qquad 2.82812<V_g<2.82813.                                \tag{11}
\]

In fact $V_{\mathrm{alias}}>3v_3$, whereas the initial complete
triangulation has only three tetrahedra. The failure of domination is
therefore robust; it does not depend on a delicate comparison of critical
values or on trusting a numerical face optimizer.

## 5. Consequence for the critical path

This example rules out the general assertion

\[
 \sup_{\text{weak nonnegative integer-alias loci}}V\leq V_g
\]

under geometricity, positivity, ideal topology, complete marked-meridian
compatibility, and integer-lattice membership alone. It also rules out a
universal retraction of such faces to the original angle polytope that
preserves or increases volume.

The compact clamped Legendre construction does not fix this obstruction.
On the weak alias locus it minimizes \(\operatorname{Im}W_m\), whose radial
infimum is that cell's Rivin volume. Restricting the radial minimization
to a finite box can only increase the infimum. At (4), that lower bound
already exceeds $V_g$. Compactness of the contour cannot supply the
missing comparison between different marked potentials.

For a proof of the original invariant's volume limit, the excessive
face must consequently be absent from the selected source, cancel as a
relative Ward/sewing charge, or be excluded by a further structural
hypothesis on the actual supported quantum chart. Its coefficient has
not been computed here. The result does not assert that the original
state acquires a growth rate larger than hyperbolic volume.

The positive complete geometry still controls the original angle
polytope. What fails is automatic domination of **all other winding
cells** by that one geometric maximum.

The subsequent [last-move trace](oversized_alias_last_pachner_wall.md)
finds a precise local obstruction: this face fails the very first
inverse Pachner replacement. Its new edge has winding zero rather
than one, and the exact five-term inverse meets a simultaneous norm
wall with retained root-frame monodromy. That calculation identifies
the source theorem needed; it does not supply the missing quantum
coefficient.
