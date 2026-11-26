# Joint pointed nonvanishing by character-subgroup propagation

Private research note, 17 November 2026.

The tetrahedron equations propagate zero joint-character blocks without
refactorizing the vector after an edge projection. This gives a finite
incidence criterion for joint nonvanishing. A genuine single-edge
nonvanishing theorem supplies the last step when the remaining
constraints lie in the cyclic subgroup of one actual edge. The criterion
is not asserted for every positive triangulation.

## 1. Original tensor and exact block equations

Use the all-level root modules, integral edge lattice, and Weyl units of
the pointed gluing source. Let \(E\) be a primitive isotropic edge lattice
of rank \(r\), with a fixed integral basis and compatible prescribed
central-root characters. Normalize its commuting basis operators as
\(U_i^N=1\). Write

\[
 G=(\mathbb Z/N)^r,\qquad
 p=\bigotimes_t p_t,\qquad
 v_\chi=\Pi_\chi p,\qquad \sum_{\chi\in G}v_\chi=p\ne0.
\tag{1}
\]

The projectors are the literal finite commuting-edge projectors.
Their blocks may be entangled. We retain the local equations

\[
 (X_t+Y_t-1)p=0,
 \qquad X_t,Y_t\text{ invertible}.
\tag{2}
\]

Fix the common primitive root \(Q\). Define the full edge-character
shifts \(\alpha_t,\beta_t\in G\) by

\[
 U_iX_t=Q^{(\alpha_t)_i}X_tU_i,\qquad
 U_iY_t=Q^{(\beta_t)_i}Y_tU_i.
\tag{3}
\]

These commutators retain all orientation conventions. Central-root
and Weyl scalar units do not change them. Projecting (2) gives

\[
 v_\chi=X_tv_{\chi-\alpha_t}+Y_tv_{\chi-\beta_t}.
\tag{4}
\]

The exact cyclic version of (2), obtained by multiplication by
\(Y_t^{-1}\), is equally important:

\[
 p=(Y_t^{-1}-Y_t^{-1}X_t)p,
\qquad
 v_\chi=Y_t^{-1}v_{\chi+\beta_t}
          -Y_t^{-1}X_tv_{\chi-\alpha_t+\beta_t}.
\tag{5}
\]

No projected vector is assumed separately to satisfy (2). Equations
(4)--(5) couple the blocks of the original tensor exactly.

## 2. Subgroup propagation

Let \(Z=\{\chi:v_\chi=0\}\). For a subgroup \(H\le G\), say that
zeros are \(H\)-invariant when \(Z+H=Z\).

**Lemma.** Suppose zeros are \(H\)-invariant. If any one of

\[
 \alpha_t\in H,\qquad \beta_t\in H,\qquad
 \alpha_t-\beta_t\in H
\tag{6}
\]

holds, then zeros are invariant under
\(H+\langle\alpha_t,\beta_t\rangle\).

**Proof.** If \(\alpha_t\in H\) and \(v_\chi=0\), then
\(v_{\chi-\alpha_t}=0\). Equation (4) and invertibility of \(Y_t\)
give \(v_{\chi-\beta_t}=0\). The finite order of \(\beta_t\) makes
this inclusion invariant under both signs of that shift. The case
\(\beta_t\in H\) follows in the same way. If
\(\alpha_t-\beta_t\in H\), the last block in (5) vanishes together
with \(v_\chi\). Invertibility of \(Y_t^{-1}\) gives
\(v_{\chi+\beta_t}=0\), and finite order again supplies both signs.
Adding the shifts already in \(H\) proves the claim. \(\square\)

Start with \(H_0=0\) and repeatedly perform every enlargement permitted
by (6). Equivalently, set

\[
 H_{k+1}=H_k+
 \sum_{t:\ \alpha_t\in H_k\ \mathrm{or}\ \beta_t\in H_k
                  \ \mathrm{or}\ \alpha_t-\beta_t\in H_k}
          \langle\alpha_t,\beta_t\rangle.
\tag{7}
\]

This stabilizes in the finite group \(G\), at a subgroup \(H_\infty\).
It is the least subgroup closed under these rules; performing the
enlargements in any exhaustive order gives the same result. Indeed every
closed subgroup contains every successive enlargement starting at zero.
The lemma proves

\[
 Z+H_\infty=Z.
\tag{8}
\]

In particular, if \(H_\infty=G\), no block vanishes: otherwise (8)
would make every block zero, contrary to (1). This is an exact statement
for every prescribed compatible joint character, not a choice of a
nonzero block.

## 3. A genuine edge can supply the last step

Let \(e\in E\) be a genuine interior edge with a primitive integral
row, positive dihedral angles summing to \(2\pi\), and paired distinct
face occurrences as in the single-edge source. That theorem gives
nonzero projection of \(p\) at every compatible character of \(e\).

Evaluation at \(e\) is a surjection

\[
 \operatorname{ev}_e:G\longrightarrow\mathbb Z/N.
\tag{9}
\]

The actual normalized edge operator may differ from the product of the
chosen basis operators by a retained \(\mu_N\) scalar. This merely
translates its character labels. Its spectral projector is exactly the
sum of the joint projectors over a fiber of (9).

**Theorem.** If

\[
 \ker(\operatorname{ev}_e)\subset H_\infty,
\tag{10}
\]

then \(v_\chi\ne0\) for every \(\chi\in G\).

**Proof.** If \(v_{\chi_0}=0\), (8) and (10) make every block in
the entire fiber \(\chi_0+\ker(\operatorname{ev}_e)\) vanish. Its sum
is the corresponding single-edge projection of the original tensor,
contrary to the cited genuine-edge theorem. \(\square\)

Thus the tensor structure is used by the single-edge theorem only
before any projection. The propagation step itself retains all
entanglement and never substitutes independent local marginals for a
joint block.

## 4. Exact quotient test, including composite levels

At closure, the three classes

\[
 0,\quad\overline\alpha_t,\quad\overline\beta_t
       \quad\text{in }G/H_\infty
\tag{11}
\]

are either all equal or pairwise distinct, for every tetrahedron.
Otherwise one equality triggers (6), forcing both remaining classes to
be zero. Conversely this condition is exactly stability under (7).
The least such subgroup containing zero is the subgroup constructed
above; no division or saturation is part of the rule.

Under the perfect finite pairing between \(G\) and \(E/NE\), put

\[
 E_{\mathrm{res},N}
 =\{u\in E/NE:\ \chi(u)=0\text{ for every }\chi\in H_\infty\}.
\tag{12}
\]

These are the residual edge constraints. Condition (10) is equivalently

\[
 E_{\mathrm{res},N}\subset\langle e\bmod NE\rangle.
\tag{13}
\]

This follows by taking annihilators of (10), since the annihilator of
\(\ker\operatorname{ev}_e\) is precisely the cyclic subgroup generated
by the primitive \(e\). Formula (13), rather than a dimension count,
is the test at composite levels. A cyclic residual group unrelated to
any genuine edge does not by itself invoke the single-edge theorem.

There is also an all-level sufficient integral test. Form the same
closure with the actual integral shifts in \(E^*=\operatorname{Hom}(E,\mathbb Z)\),
adding generators without saturation, and call the resulting subgroup
\(L_\infty\). There are finitely many shifts to add, so this procedure
stabilizes. Its reduction modulo \(N\) is contained in \(H_\infty\)
for every \(N\). Therefore the literal inclusion

\[
 \{f\in E^*:f(e)=0\}\subset L_\infty
\tag{14}
\]

implies (10) at every level. Primitivity of \(e\) ensures that reducing
the left side of (14) gives the full kernel in (9). An inclusion only
after tensoring with \(\mathbb Q\) is insufficient: its finite indices
must be retained and checked modulo \(N\).

## 5. What the test says about actual incidence

For an actual edge row \(f\), write its local opposite-pair counts as
\((a_f,b_f,c_f)\). In the source convention
\(A=X,B=Y^{-1}\), \(AB=Q^\epsilon BA\), and
\(\beta(f)=\epsilon(a_f-c_f,b_f-c_f)\). Direct commutation gives

\[
 \alpha_t(f)=c_f-b_f,\qquad
 \beta_t(f)=c_f-a_f,\qquad
 (\alpha_t-\beta_t)(f)=a_f-b_f.
\tag{15}
\]

Thus a first step at tetrahedron \(t\) occurs exactly when two of its
opposite-pair multisets of global edge labels have equal multiplicities
modulo \(N\). The actual edge rows generate \(E\), so checking their
values in (15) is enough. For \(N\ge3\), multiplicity differences lie
between \(-2\) and \(2\), and this is ordinary integral equality of
the multisets. At level two only their parity is required.

This supplies a concrete limitation. If every tetrahedron has six
distinct global edge labels, each of the three differences in (15)
takes the value \(1\) or \(-1\) on some actual edge row. None is zero
modulo any \(N\ge2\). Hence (7) never starts and
\(H_\infty=0\). If \(r\ge2\), condition (10) then fails for every
primitive edge. This is a test of that incidence pattern, not a claim
that its pointed joint projection vanishes.

More generally, the closed residual system in (11) may retain
tetrahedra with three distinct shift classes. The positive angle sums
used by the single-edge theorem do not, within this proof, eliminate
that residual system. No assertion is made that every positive
triangulation satisfies (10), or that it can be changed to one that
does by moves preserving the entire original edge projector and
pointing. Such a move theorem would have to transport those operators,
all characters, and the selected vector; an unpointed lattice change
does not suffice.

The result is joint algebraic nonvanishing under the explicit incidence
test. It supplies no uniform lower norm, identification with the
original relative quantum source, or regulator asymptotic.

## Direct sources

1. [Pointed tetrahedron modules and all-level edge reduction](pointed_tetrahedron_gluing.md),
   SHA256 `ba91c4be463e38add42b2f8ebc53c3cd3a7e96e97ac4247330dc325e7f6b3a7c`.
   This fixes the actual tensor, torus commutators, compatible characters,
   and primitive edge lattice at every level.
2. [Nonvanishing of every single-edge pointed projection](research_single_edge_pointed_nonvanishing.md),
   SHA256 `157c5011dfe4bd702c0dbb7749fc484cf4301cd367489442b17aa3981c8ad770`.
   This proves the genuine-edge marginal used in Section 3, including
   face incidence, positive \(2\pi\) angle, and every compatible character.

Both complete texts were read in this author sequence. The new proof
uses exact finite group identities and the original local equations;
no numerical or symbolic program is used.
