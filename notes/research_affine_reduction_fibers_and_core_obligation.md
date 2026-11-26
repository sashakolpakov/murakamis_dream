# Exact reduction fibers and the remaining core theorem

Research note, 2 November 2026. The exceptions in this note are original
integer filling assignments. Neither replacing those assignments by knot
types nor discarding redundant coordinates is part of the argument.
The frozen manuscripts are unchanged.

The existing reductions give more than a warning about infinite fibers:
on each fixed structural branch, linear algebra decides whether a
nonempty fiber is a singleton or is infinite. In the latter case it
contains a family on which every genuinely varying original coordinate
tends to infinity. Thus the issue cannot be avoided by requiring all
remaining original coefficients to be long.

## 1. The data of a reduction branch

Let \(p=(p_1,\ldots,p_d)\in\mathbb Z^d\) be the original surgery
coefficients. A retained half-twist pattern has already been fixed, so
the crossing powers are \(n_i=\eta_i-2p_i\), with
\(\eta_i\in\{-1,0,1\}\) fixed. There is no additional parity restriction
on \(p\).

Consider one branch of an exact tangle reduction. Suppose its parameter
set has the form

\[
 \Omega=\{p\in\mathbb Z^d:
       Ap=a,\quad \ell_j(p)\ne c_j\quad(1\le j\le q)\},
 \tag{1}
\]

where all matrices, vectors, and linear forms have rational
coefficients. The reduced parameters are

\[
                 f(p)=Bp+b.
 \tag{2}
\]

The reduction must identify the actual closed knot, including the
zero-framing convention for the invariant. An equality between finite
quantum contractions alone is insufficient for this purpose.

These hypotheses apply to the zero-aware all-root reduction in
[the Conway reductions paper](../papers/conway-reductions/closures.tex).
Its branch is chosen by the original parities and the zero or nonzero
values of finitely many subset sums. Its surviving parameters are sums
over disjoint original label blocks. Substituting
\(n_i=\eta_i-2p_i\) gives precisely affine equations and inequalities
of the form (1), and the surviving weights give (2).
Fixed numerical values, including the values needed to make an
elementary factor an unknot, can be added to \(Ap=a\). Finite alternatives
such as a terminal exponent \(1\) or \(-1\) should first be split into
separate branches.

The same description applies to a prescribed finite sequence of the
proved degree-two \(0,\pm1\) moves: a \(\pm1\) move gives affine shifts,
and a zero move gives a sum. This statement does not assert a
classification of all partially filled exteriors.

## 2. A nonempty fiber is either a singleton or infinite

Fix a reduced assignment \(y\), and suppose
\(\Omega_y=\{p\in\Omega:f(p)=y\}\) is nonempty. Put

\[
                  H=\begin{pmatrix}A\\B\end{pmatrix}.
 \tag{3}
\]

**Proposition 1.** If \(H\) has column rank \(d\), then
\(\Omega_y\) consists of one point. If its rank is smaller than \(d\),
then \(\Omega_y\) is infinite. More precisely, for any
\(p_0\in\Omega_y\) there is a nonzero \(v\in\mathbb Z^d\) such that

\[
       p_0+kv\in\Omega_y
       \quad\hbox{for every integer \(k\) outside a finite set}.
 \tag{4}
\]

**Proof.** The difference of two points of the fiber lies in
\(\ker_{\mathbb Q}H\). Full column rank therefore gives uniqueness.
Otherwise this rational kernel contains a nonzero integral vector
\(v\). Every \(p_0+kv\) satisfies all equations defining the fiber.
If \(\ell_j(v)=0\), its \(j\)-th nonvanishing test remains true
because it was true at \(p_0\). If \(\ell_j(v)\ne0\), the equality
\(\ell_j(p_0+kv)=c_j\) holds for at most one integer \(k\).
There are finitely many tests, so only finitely many integers are
excluded. Since \(v\ne0\), the other points are distinct. \(\square\)

Thus the nonzero subset-sum tests do not cut an affine fiber down to
a nonempty finite set. They remove finitely many points from any
suitable line. This conclusion does not apply without further work
to a different parameter domain that imposes one-sided sign
conditions or arbitrary nonlinear inequalities. The present target
allows signed coefficients of unrelated magnitudes.

There is a useful stronger choice of direction. Let

\[
 I=\{i:v_i=0\text{ for every }v\in\ker_{\mathbb Q}H\},
 \qquad J=\{1,\ldots,d\}\setminus I.
 \tag{5}
\]

Every coordinate in \(I\) is constant on the affine fiber.

**Proposition 2.** If \(\Omega_y\) is infinite, the vector \(v\) in
(4) can be chosen so that \(v_j\ne0\) for every \(j\in J\).
Consequently \(p_i=p_{0,i}\) for \(i\in I\), while
\(\lvert p_j\rvert\longrightarrow\infty\) for every \(j\in J\),
along the family (4) as \(\lvert k\rvert\longrightarrow\infty\).

**Proof.** For each \(j\in J\), the equation \(v_j=0\) defines a
proper linear subspace of \(\ker_{\mathbb Q}H\). A vector space
over the infinite field \(\mathbb Q\) is not a finite union of proper
linear subspaces. One direct verification is to choose a rational
basis \(w_1,\ldots,w_r\) and evaluate
\(w_1+t w_2+\cdots+t^{r-1}w_r\): each nonzero coordinate form is a
nonzero polynomial, so it vanishes at only finitely many rational
\(t\). Choose another \(t\), clear denominators, and use Proposition 1.
\(\square\)

The original coefficients need not tend to infinity with the same
sign. For a zero merger, the familiar direction is \((1,-1)\).
Allowing independent signed long fillings is exactly what makes
these directions relevant.

## 3. What can be pulled back from a cofinite theorem

Suppose an exact reduction identifies the knot at \(p\in\Omega\)
with the knot at \(f(p)\). Let \(E\) be a finite collection of
reduced assignments for which the volume identity remains unresolved.
Outside \(f^{-1}(E)\) the reduced theorem transfers to the original
family.

For a fixed branch (1), Proposition 1 gives the complete fiber test:

* If \(H\) has full column rank, at most \(\lvert E\rvert\) original
  assignments remain unresolved.
* If \(H\) has deficient rank, every nonempty fiber over an element
  of \(E\) is infinite. To prove a cofinite conclusion on this
  branch, each hyperbolic knot represented by such an exceptional
  fiber must satisfy the volume identity.

The second assertion is a requirement for the proof, not a claim
that any of these knots fails the conjecture. If one did fail, every
assignment in its fiber would be a counterexample.

For a finite collection of structural branches, apply this test to
each branch separately. All equations accumulated earlier in the
reduction must remain in \(A\). Keeping only the final effective
coordinates would lose exactly the information being tested.

There is also a direct consequence for a proposed long-remainder
theorem. Suppose that, for every fixed partial assignment of the
original template, all sufficiently long remaining original
coefficients giving hyperbolic knots satisfy the volume identity.
If a hyperbolic reduced knot has an infinite fiber in (1), fix the
coordinates in \(I\) from (5) and apply that theorem along (4).
Eventually all coordinates in \(J\) satisfy its threshold, and the
knot is the same reduced knot at every point. The long-remainder
theorem therefore proves the volume identity for that particular
core. It cannot merely leave the core among finitely many reduced
exceptions.

## 4. The four-vertex example and the matrix test

Use the original crossing \(R\), physical quarter-turn \(T\), and
cylindrical closure \(C\). On the four-vertex path write

\[
 K_4(a,v,b,c)=C\bigl(R^aT(R^vT(R^bT(R^c)))\bigr).
 \tag{6}
\]

The proved marked zero move gives

\[
                  K_4(a,0,b,c)\simeq K_2(a+b,c).
 \tag{7}
\]

For clarity, temporarily use the crossing powers as coordinates in
one fixed parity class. Fixing the reduced pair \((s,c_0)\)
imposes

\[
            v=0,\qquad a+b=s,\qquad c=c_0.
 \tag{8}
\]

The matrix of these three equations in four variables has kernel
spanned by \((1,0,-1,0)\). On the fixed parity lattice, take twice
this vector. Hence every hyperbolic \(K_2(s,c_0)\) has infinitely
many preimages of one fixed original parity pattern, with \(a,b\)
both long and of opposite signs.

The exact topology behind (7), including the reversal under
\(T^2\), is proved in
[the scope audit](research_finite_exception_scope_audit.md#2-an-infinite-fiber-on-a-four-vertex-path).
The rank calculation adds no topological assumption.

Thus a finite reduced exceptional list for two-circle knots is
not enough to prove the cofinite statement for this four-circle
template. Every hyperbolic knot on that list must be settled before
its entire zero-merger fiber is covered.

## 5. A bounded-size form of the padding implication

The preceding obstruction is not restricted to paths. The existing
strict-padding argument has the following quantitative form.
The grammar is the enlarged literal strict class of
[the asymptotics manuscript](../papers/conway-asymptotics/main.tex),
which permits an elementary closing child; the statement does not
assert membership in its older completed-root subfamily.

**Proposition 3.** Let \(K=C(Q)\) be a hyperbolic knot represented by
a literal strict Conway expression with \(m\) labelled leaves,
whose integer powers are all fixed. There is a literal strict
template with \(m+2\) labelled leaves and one fixed parity pattern
having infinitely many assignments representing \(K\).
Consequently, a cofinite assignment theorem for every strict
template with at most \(m+2\) leaves proves the volume identity for
every such hyperbolic \(m\)-leaf core, without exceptions.

**Proof.** Put \(h(b)=T(R^b)\) and form

\[
                E(a,b)=C\bigl(h(b)[R^aT(Q)]\bigr).
 \tag{9}
\]

This uses the permitted operations because \(R^a=T^3h(a)\).
Reopening \(Q\) turns its former closing product into a retained
product. Each allowed closing pair \(AA,AL,AH,LH\), in either order,
also has a nonempty open product, of type \(A,A,H,H\), respectively,
by the [literal type table](../papers/newton-calculus/supports.tex).
Its other products remain allowed. Hence \(Q\), now used as an open
tangle, has type \(A\) or \(H\). A new strict state may be chosen;
the old closed optimizer is not being reused at its former root.
Thus \(T(Q)\) has type \(A\) or \(L\), while \(R^a\) has type
\(H\). Their product has type \(H\), and the outer closing pair
has types \(L,H\), which is allowed. Strictness is a property of
this formal expression and does not require \(b\ne0\).

Let \(D\) denote cap closure and \(\tau=T^2\) the physical
half-turn. The proved cap isotopies give, at \(b=0\),

\[
\begin{aligned}
 E(a,0)&\simeq D(R^aT(Q))\\
       &\simeq D(R^a)\mathbin{\#}D(T(Q))\\
       &\simeq U\mathbin{\#}C(\tau Q)
        \simeq K.
\end{aligned}
 \tag{10}
\]

Here \(U\) is the unknot. These are the actual marked cap
isotopies of
[the reductions paper](../papers/conway-reductions/closures.tex),
not commutations of open tangles. They retain components and the
transported framing; the final zero-framing correction gives the
same reduced Kashaev invariant.
The last step rotates the entire closed picture: the physical
\(\tau\) permutes the prescribed cylindrical closing pairs
\(\{0,3\},\{1,2\}\) and their empty outside arcs. It is not an
erasure of a half-turn on an open tangle.

Fix either parity for \(a\), even parity for \(b\), and the
original core parities. Vary \(a\) through that infinite parity
class, keeping \(b=0\). Equation (10) identifies every resulting
knot with \(K\). If \(K\) failed the identity, one fixed
\((m+2)\)-leaf template would have infinitely many failing
assignments. \(\square\)

For an explicit family in original surgery coordinates, take
\(\eta_a=\eta_b=0\) at the two new circles. Then
\((p_a,p_b,\mathbf p_Q)=(r,0,\mathbf p_Q)\), \(r\in\mathbb Z\),
gives \((a,b)=(-2r,0)\). These are distinct original assignments
with the core parameters fixed. This one retained pattern passes
the full knot test: even changes in a braid power preserve both
endpoint pairings and any internal component, while (10) shows
that the resulting link is exactly the knot \(K\).

In particular, for the entire strict Conway class the following
statements are equivalent:

1. Every fixed admissible template has finitely many exceptional
   hyperbolic assignments.
2. Every hyperbolic strict Conway core satisfies the volume
   identity at every integer assignment.

The implication from 2 to 1 has no exceptions at all; the reverse
implication is (9)--(10). The proposition makes the increase in
template size explicit. It does not claim that all hyperbolic
knots lie in this Conway class.

## 6. A reduction scheme that does not assume its conclusion

For one fixed input template, a valid finite proof can have three
kinds of terminal record:

1. A whole-boundary source theorem proves the volume identity for
   all sufficiently long remaining original assignments. Only
   the finitely many choices of a bounded remaining coordinate
   require successor records.
2. An exact reduction reaches a knot whose volume identity is
   already proved, or a branch with no hyperbolic final knot.
3. An unresolved final record has a finite fiber in the original
   assignment space.

The reduction tree must have finite branching and a strictly
decreasing nonnegative integer complexity, or a specified
lexicographic combination of such complexities. Then it is finite.
The union of the type-3 fibers is finite. This is the elementary
finite-branching argument, now with an exact fiber test available
for affine reduction branches.

A type-2 reduction is allowed to pass through an intermediate
exterior outside the current geometric source class. What it
cannot do is declare its hyperbolic closed descendants solved
merely because that intermediate exterior has simplified.
The padded family (9) already proves this independently of any
classification of those intermediate exteriors.

Nor can an essential-tangle or JSJ decomposition alone bypass
the issue. If it supplies an exact reduction of a padded family,
every original assignment still represents the same core in
(10). A decomposition theorem might locate that core and remove
unnecessary parameters, but the required numerical volume
identity for the core is unchanged. This observation asserts no
unproved JSJ classification.

For a *single* fixed template, a finite reduction tree may expose
only finitely many collapsed hyperbolic cores. Proving their
individual identities could finish that template. A theorem for
*every* strict template cannot use a fixed list of solved cores
as a substitute: Proposition 3 lets any hyperbolic strict core
appear in this role.

The present long-filling and short-component theorems therefore
give genuine terminal records of type 1 and 2, but not a general
reduction theorem of this form. The remaining general input
must handle the connected short sources and their exact
degenerations, including every collapsed hyperbolic core that
has an infinite original fiber. This is the precise point at
which a purely cofinite induction would otherwise become
circular.

## 7. Why arbitrarily long presentations in finitely many parents do not bypass this

A different proposed shortcut would be to represent a fixed core by
arbitrarily long fillings of an already controlled strict parent,
until the existing long-filling theorem applies. Within a fixed
finite collection of such parents this cannot work in general.
The following obstruction follows directly from the primitive
volume differential already proved in
[the strict geometry paper](../papers/strict-conway-geometry/fillings.tex);
no assertion about cancellation in quantum sums is needed.

**Proposition 4.** Fix one complete strict parent \(Y\), a nonempty
set of its crossing-circle cusps to fill, and a hyperbolic knot
exterior \(X\). There is a constant \(B(Y,X)\) such that no filling
of those cusps with all \(\lvert p_i\rvert>B(Y,X)\) is isometric
to \(X\).

Here the other cusps, if any, stay complete, and an asserted
homeomorphism to \(X\) can be substituted for isometry whenever
its hyperbolic volume is known to be the same. The conclusion is
that a fixed \(X\) cannot occur arbitrarily far out in the region
where every slope is long; it is not a finiteness assertion about
all possible presentations of \(X\).

**Proof.** Write \(r_i=1/p_i\). The near-complete implicit solution
also exists with the meridian equation

\[
       U_i+p_iV_i=-2\pi i\lambda,\qquad 0\le\lambda\le1,
 \tag{11}
\]

for all sufficiently small real \(r_i\). To see the uniformity,
solve \(V_i+r_iU_i=-2\pi i\lambda r_i\) near the complete point:
the derivative with respect to the deformation variables at
\(r=0\) is the same invertible diagonal matrix for every
\(\lambda\in[0,1]\). The implicit neighborhoods can be chosen
uniformly on that compact interval, and local uniqueness patches
the solutions. The original positive chain and its bounded
frames remain in their fixed near-complete neighborhood.

In the conventions of that paper,
\(U_i=-2\pi i\chi_i\) and
\(V_i=\widetilde\tau_i U_i\), where the removable holomorphic
ratio satisfies \(\operatorname{Im}\widetilde\tau_i>0\).
Equation (11) gives

\[
 \chi_i=\frac{\lambda r_i}{\widetilde\tau_i+r_i},
 \qquad
 \operatorname{Re}V_i=
 \frac{2\pi\lambda r_i^2\operatorname{Im}\widetilde\tau_i}
      {\lvert\widetilde\tau_i+r_i\rvert^2}>0
 \quad(\lambda>0).
 \tag{12}
\]

Let \(\mathcal V\) be the volume of the original ideal chain.
Its proved differential is

\[
 d\mathcal V=\frac12\sum_i
   \bigl(\operatorname{Re}V_i\,d\operatorname{Im}U_i
        -\operatorname{Re}U_i\,d\operatorname{Im}V_i\bigr).
 \tag{13}
\]

The real and imaginary parts of (11) imply
\(\operatorname{Re}U_i=-p_i\operatorname{Re}V_i\) and
\(d\operatorname{Im}U_i+p_i\,d\operatorname{Im}V_i
=-2\pi\,d\lambda\). Hence

\[
              \frac{d\mathcal V}{d\lambda}
                  =-\pi\sum_i\operatorname{Re}V_i<0
                  \quad(\lambda>0).
 \tag{14}
\]

At \(\lambda=0\), the absolute volume is
\(\operatorname{Vol}(Y)\); at \(\lambda=1\), the calibrated
chain is the smooth filled metric. Consequently every such long
filling has volume strictly smaller than
\(\operatorname{Vol}(Y)\). Its volume tends to
\(\operatorname{Vol}(Y)\) as all \(r_i\to0\), by continuity of
the same chain at the complete point.

If no \(B(Y,X)\) existed, a sequence with
\(\min_i\lvert p_i\rvert\to\infty\) would have every filled
volume equal to \(\operatorname{Vol}(X)\). Convergence would
force \(\operatorname{Vol}(X)=\operatorname{Vol}(Y)\), contrary
to the strict inequality for each member of the sequence.
\(\square\)

The maximum of these constants works for a fixed finite set of
parents. Thus an exact rewriting procedure cannot guarantee a
proof for an arbitrary fixed core simply by making every
coefficient arbitrarily long while keeping the parent in a
finite controlled set. At least one short parameter, a
degeneration outside those parents, or unbounded parent
complexity must remain. This agrees with, but is independent
of, the affine-fiber obstruction above.

## 8. A terminal splitting inside the original circle-tree class

There is a padding construction that stays within the original
ordered circle-tree syntax, including its subclass of paths.
It does not use the enlarged strict closing grammar of Section 5.
It also makes a stronger statement for one prescribed template:
cofiniteness for a single enlargement forces the identity at
every hyperbolic assignment of the smaller template.

Fix a nontrivial original ordered circle-tree template \(Q\).
Choose its terminal root as in
[the circle-tree paper](../papers/circle-tree-volume/main.tex).
Closed cyclicity puts the evaluated expression in the form
\[
                 K_Q(s,\mathbf n)=C(R^sT(F_{\mathbf n})).
 \tag{15}
\]
Here \(s\) is the terminal crossing power; \(\mathbf n\)
contains the other original powers. The ordered expression
\(F_{\mathbf n}\) and all its disk frames are retained.
Write \(\tau=T^2\) for the physical half-turn, and define
one enlarged template
\[
 P_Q(a,v,b,\mathbf n)=
 C\!\left(R^aT\!\left(R^vT\!\left(R^b
                              T(\tau F_{\mathbf n})\right)\right)\right).
 \tag{16}
\]
This replaces the terminal vertex by a three-vertex path.
It adds two vertices and does not create a bare product junction.
The half-turn \(\tau\) propagates through the old expression by
reversing its indicated stacks, commuting with \(T\), and
preserving every signed integral power. Thus (16) is one fixed
original ordered circle-tree template. If \(Q\) is a path, so
is \(P_Q\).

**Proposition 5.** At \(v=0\), for every integer assignment,
\[
                  P_Q(a,0,b,\mathbf n)
                            \simeq K_Q(a+b,\mathbf n).
 \tag{17}
\]
The isotopy retains all components and transports ribbons.
After the prescribed zero-framing correction, the reduced
Kashaev invariant and knot-complement volume agree.

**Proof.** The actual ordered rotation and closure identities of
[the reductions paper](../papers/conway-reductions/moves.tex) give
\[
 \begin{split}
 P_Q(a,0,b,\mathbf n)
 &=C\!\left(R^a\tau(R^bT(\tau F_{\mathbf n}))\right)\\
 &=C\!\left(R^aT(F_{\mathbf n})R^b\right)\\
 &\simeq C\!\left(R^bR^aT(F_{\mathbf n})\right)
   =K_Q(a+b,\mathbf n).
 \end{split}
 \tag{18}
\]
The second line uses the reversal
\(\tau(GH)=\tau(H)\tau(G)\), together with
\(\tau T=T\tau\), \(\tau^2=1\), and \(\tau(R^b)=R^b\).
The third line is closed cyclicity, not commutation of open
tangles. All moves are ambient isotopies with the indicated
marks and components carried. The knot complement and its
preferred zero framing therefore agree. \(\square\)

Fix the carriers of \(Q\), writing
\(s=\eta_s-2p_s\). Give the three vertices in (16) carriers
\[
                       (\eta_a,\eta_v,\eta_b)=(0,0,\eta_s)
 \tag{19}
\]
and transport the remaining carriers with \(\tau\).
For every original assignment \((p_s,\mathbf p)\) and every
integer \(r\), the enlarged assignment
\[
              (p_a,p_v,p_b,\mathbf p)
                         =(r,0,p_s-r,\mathbf p)
 \tag{20}
\]
has \(a+b=s\). The map
\(((p_s,\mathbf p),r)\mapsto(r,0,p_s-r,\mathbf p)\)
is a bijection onto the full slice \(p_v=0\) of this one
enlarged integer parameter space. The knot-component test
is unchanged on corresponding points by (17).

Let \(\mathcal F_Q\) denote the set of hyperbolic assignments
of \(Q\) at which the volume identity fails, and define
\(\mathcal F_{P_Q}\) in the same way. This notation expresses
a logical implication; no failing knot is asserted to exist.
Under the bijection (20),
\[
          \mathcal F_{P_Q}\cap\{p_v=0\}
                           =\mathcal F_Q\times\mathbb Z.
 \tag{21}
\]
Consequently, if \(P_Q\) has only finitely many exceptional
hyperbolic assignments, then \(\mathcal F_Q\) is empty.
The same enlarged template works simultaneously for all
assignments of \(Q\); it is not chosen anew after fixing a
core knot.

There is an equally sharp consequence for the proposed
partial-filling induction. Fix \((p_s,\mathbf p)\), fix
\(p_v=0\) and all entries of \(\mathbf p\), and leave only
\(p_a,p_b\) free. Along (20), both free absolute values tend
to infinity as \(|r|\to\infty\), while the knot stays fixed.
Thus a long-remainder theorem for these two-free-coordinate
strata already proves the volume identity for every hyperbolic
assignment of every \(Q\) to which it applies. A residual
finite exceptional list of smaller cores is insufficient.
This is a necessary implication of the original target,
not a change to it.

## 9. What the rational normal form leaves unresolved

The exact
[rational corridor normal form](research_definite_rational_corridor_normal_form.md)
reduces a fixed nondegenerate corridor to a chain of one sign
with coefficient magnitudes at least two, with integral
boundary shifts and a recorded proper rotation. Its shifts
are injective translations of surviving original parameters.
It therefore gives a valid reduction of the required source
theorem to that family of chains. It does not provide their
whole-boundary asymptotics.

A simple exact family shows why the available reductions do
not finish this step. Consider the normalized negative
continued fraction with \(r\ge2\) entries, all equal to three.
Put
\[
 k_0=1,\qquad k_1=3,\qquad
                     k_j=3k_{j-1}-k_{j-2}.
 \tag{22}
\]
Its normalized two-boundary matrix is
\[
                    \begin{pmatrix}
                       k_{r-1}&k_{r-2}\\
                       k_r&k_{r-1}
                     \end{pmatrix},
 \qquad
              \frac{k_r}{k_{r-1}}=[3,\ldots,3]_- .
 \tag{23}
\]
The continuant identity
\(k_{r-1}^2-k_rk_{r-2}=1\) follows by induction from
(22). In particular this is the determinant-one normalized
matrix, not only a slope calculation.
Also \(1<k_{r-1}<k_r-1\). Hence neither diagonal entry is
congruent to \(1\) or \(-1\) modulo \(k_r\).
The exact
[one-vertex compression criterion](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_rational_corridor_compression.md)
therefore rules out compression of this whole corridor to
one internal vertex, even allowing the prescribed integral
boundary shifts and proper half-turn.

The ceiling algorithm is unique, so normalization again gives
the same string of threes. There is no zero or unit coefficient
to eliminate and no string of twos to compress. Original path
vertices have degree at most two, so re-rooting cannot meet
the high-valence threshold in
[the hybrid tree theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_hybrid_tree_filling_closure.md).
For \(r\ge3\), the new internal \(3,3\) kernel also leaves
an adjacent short filling: its
[proved composition rule](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_three_kernel_compositions.md)
requires a sufficiently long intervening power.
These observations concern the stated reductions and source
theorems; they do not exclude a different exact identity or a
future uniform chain theorem.

For a fixed original template, finite branching can produce
only finitely many fixed short records at each stage. That
does not make their original assignment fibers finite, nor
does it prove the missing boundary theorem for such a record.
Equations (20)--(21) show that even a record representing one
fixed hyperbolic core can already carry the full obstruction.
Accordingly, a complete reduction argument still has to do
both things: establish the original source theorem for every
short record it uses, and settle every unresolved hyperbolic
core whose original fiber is infinite. The existing normal
form, local eliminations and high-valence theorem do not
jointly supply those two conclusions.

## 10. Which short corridors can be made long, and what conjugation preserves

This section concerns exact presentations. It neither gives a
counterexample to the volume conjecture nor asserts that an arbitrary
fixed-level quantum representation is faithful.

First apply the marked degree-two moves only where their valence and
attachment hypotheses hold. A unit deletes one vertex and translates
the two neighboring powers; a zero merges powers and retains the
fiber test of Sections 1--3. The physical half-turns, branch ordering,
primitive curves, and original component test are part of each record.
At a branching vertex these degree-two moves are not automatic.
For a fixed remaining rational corridor, the exact ceiling normal form
then has internal magnitudes at least two. Its integral end twists are
bijective translations of the still-free original parameters; its
degenerate zero case is a merger, not such a translation.

Thus the local elimination rules remove \(0,\pm1\) from an
irreducible degree-two record, but they do not remove adjacent
coefficients of magnitudes two through seven. The
[new path source theorem](research_uniform_path_trace_assembly.md#7-the-source-theorem-at-powers-seven-and-eight)
proves the original scalar and a local outside packet for the stated
positive-seven and signed-eight classes. The
[whole-boundary upgrade](research_network_whole_boundary_decay.md)
now supplies the additional real-period and quadratic-strip estimates
required by the long-turn reset theorem. Path endpoints already have
canonical degree at most \(N-1\), so this is a proved admissible source.
This does not give the same conclusion for an arbitrary adjacent
short block.

### 10.1. An exact threshold criterion for the two uniform-sign forms

Let \(\mathbf b=(b_1,\ldots,b_m)\), \(b_i\ge2\), be the
normalized negative list of a nondegenerate fixed corridor, and let

\[
 [D(\mathbf b)]_-=
          \frac{[\mathbf b]_-}{[\mathbf b]_--1}.
 \tag{24}
\]

The full matrix and affine marking results in
[the definite normal form](research_definite_rational_corridor_normal_form.md)
and [the complement classification](research_binary_negative_corridor_positive_reexpression.md#7-what-repeated-complementation-can-reach)
show that, with the original two outside frames, the only
uniform-sign lists with magnitudes at least two, allowing integral
end twists and the retained proper rotations, are \(\mathbf b\)
and \(D(\mathbf b)\). The pendant assertion uses the original
cap and its established stabilizer, not an arbitrary attached tangle.

**Proposition 6.** Fix an integer \(K\ge3\). Such a corridor has
a uniform-sign presentation with all internal magnitudes at least
\(K\) if and only if at least one of the following holds:

1. Every \(b_i\ge K\).
2. The list is all twos, of length \(m\ge K-1\).
3. For some \(k\ge1\),
   \(\mathbf b=(2^{r_0},3,2^{r_1},\ldots,3,2^{r_k})\), with
   \(r_0,r_k\ge K-2\) and \(r_i\ge K-3\) for \(0<i<k\).

These are exact marked presentation criteria; applying a source
theorem still requires that theorem's boundary hypotheses.

*Proof.* Uniqueness leaves only the two lists just specified.
The recursion for the complement is

\[
 D((a))=(2^{a-1}),\qquad
 D((a,\mathbf b'))=(2^{a-2},d_1+1,d_2,\ldots),
 \quad D(\mathbf b')=(d_1,d_2,\ldots).
 \tag{25}
\]

For its output to have no two, the input must be binary with
both ends two, apart from the excluded singleton two. For a
binary input its complement is exactly

\[
 D(2^m)=(m+1),\qquad
 D(2^{r_0},3,\ldots,3,2^{r_k})
       =(r_0+2,r_1+3,\ldots,r_{k-1}+3,r_k+2).
 \tag{26}
\]

Comparing each entry with \(K\) proves necessity and sufficiency.
The matrix equality, fixed end shifts, and proper rotation are those
of the cited normal form, so no outside parameter is identified with
another. \(\square\)

For example \(K=7\), the positive path theorem with complete retained
ends, and its whole-boundary upgrade give admissible two-boundary
kernels for every fixed binary corridor with endpoint runs of twos
of length at least five and internal runs of length at least four.
The older threshold-64 proof gave the stronger run requirements
62 and 61. This is a family of arbitrarily long fixed short
corridors, not a bounded list of knot checks. Their end twists are
retained using the proved canonical boundary-multiplication theorem.
All words remain fixed as the quantum level tends to infinity.

### 10.2. Arbitrarily long conjugators do not remove a cyclic short core

Use the actual pillowcase linear generators

\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 A_b=\begin{pmatrix}1&b\\0&1\end{pmatrix},\qquad U=SA_1.
 \tag{27}
\]

The presentation proved in Section 4 of the definite-normal-form
note is \(\mathrm{PSL}_2(\mathbb Z)=\langle S,U\mid
S^2=U^3=1\rangle=C_2*C_3\). A reduced word alternates
nonidentity syllables from the two factors. For a cyclically reduced
word of length greater than one, record the cyclic sequence of
exponents \(1\) or \(2\) of its \(U\)-syllables; \(S\) occurs
between consecutive recorded syllables. Conjugacy preserves this
sequence up to cyclic rotation. Indeed, when a reduced conjugator
meets a cyclically reduced word, cancellation either removes an
outer conjugator syllable or moves one end syllable of the word to
the other end. Iterating gives precisely the cyclic rotations.

**Proposition 7.** Suppose

\[
 C(\mathbf b)=SA_{b_1}\cdots SA_{b_m},\qquad |b_i|\ge3.
 \tag{28}
\]

In its cyclic \(U\)-exponent sequence, the block \(b_i\) leaves
at least \( |b_i|-2\) consecutive equal exponents. In particular,
for every \(r\ge1\), the element \((SA_3)^r\) is not conjugate
to any word (28) all of whose powers have magnitude at least four.
More strongly, if it is conjugate to a word (28), every one of that
word's powers has magnitude exactly three.

*Proof.* Since \(A_1=SU\), the original blocks are

\[
 SA_b=U(SU)^{b-1}\quad(b>0),\qquad
 SA_{-b}=S(U^2S)^b\quad(b>0).
 \tag{29}
\]

At a positive-positive seam, the two adjacent \(U\)'s merge to
\(U^2\). At a negative-negative seam, the adjacent \(S\)'s
cancel and the adjacent \(U^2\)'s merge to \(U\).
At opposite-sign seams there is no cancellation. This description
also applies at the cyclic seam. Each block has at least three
\(U\)-syllables before these operations, so its first and last
syllables are distinct and at least one interior syllable remains.
There is consequently no further cancellation. At most the first
and last \(U\)-syllables of each block change; its remaining
\(|b_i|-2\) interior syllables have the same exponent and remain
consecutive in the recorded sequence.

For a positive list, the entire cyclic exponent sequence is
\(2,1^{b_1-2},2,1^{b_2-2},\ldots,2,1^{b_m-2}\), up to rotation.
For \(b_i=3\) it alternates \(2,1\), with no constant run of
length two. Conjugacy preserves that fact, so (29) forces every
\(|b_i|-2\le1\). \(\square\)

This rules out a genuine conjugation of the all-three cyclic core
into the signed-eight path class, regardless of the length or size
of the conjugating word. Proper marked rotations cannot evade it:
their pillowcase linear part is the identity. It does not classify
all isotopies of a particular capped tangle, and it does not forbid
a different nonconjugate presentation or an analytic theorem for
the original core.

At the exact source level a similarity also transports both
observations. If \(Q'_N=P_NQ_NP_N^{-1}\), then

\[
 (\ell_NP_N^{-1})Q'_N(P_Na_N)=\ell_NQ_Na_N.
 \tag{30}
\]

Here \(P_N\) denotes the invertible conjugating operator, not the
Casimir polynomial. Unitary carrier scalars and the actual physical
rotation are retained separately by the marked quantum identities.
Keeping the old cap or readout instead of the transported one changes
the observed tangle. Thus (30) provides no new nonzero coefficient
for the original observation. The long-turn reset theorem starts
with an already admissible source; it cannot be invoked for an
arbitrary short block solely because that block has been conjugated.

There is a positive similarity for \(JM^3\), namely
\(M(JM^3)M^{-1}=\kappa M^*M\), but the
[positive-cycle theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_positive_three_crossing_cycle.md#1-exact-source-and-positive-conjugacy)
retains two different transformed boundary vectors for the original
open kernel. Its positivity controls matched adjoint caps and the
cyclic trace. It is not a positivity theorem for all transported
bilinear observations in (30).

The resulting next source problem is therefore concrete: prove a
whole-boundary theorem for the normalized chains with coefficients
at least two, or a closure theorem for their genuinely adjacent
short blocks, with the marked boundary chirps and full normal data.
For branching components the corresponding multi-boundary source
is still needed. The affine-fiber obligation of Sections 6--8
continues to apply even if this rational-source problem is solved.

The exact finite checks of the complement criterion, signed seams,
matrix normalization, and conjugacy signatures are reproduced by
`python experiments/check_short_corridor_conjugation.py --output repro/results/research-short-corridor-conjugation.json`.
They validate the algebra in this section, not an asymptotic estimate.
