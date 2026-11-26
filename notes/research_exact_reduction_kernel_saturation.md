# Exact reduction preserves a complete boundary kernel

Research deduction, 7 November 2026. A proved complete boundary kernel
can be used on every marked degree-two corridor which reduces to it by
the original zero and unit moves. This includes infinite parameter
fibers, with no new analytic estimate. The deduction applies in
particular to the now proved ordinary three/four kernel. It enlarges the
covered original presentations and partial-assignment strata, rather
than asserting a new isotopy class of knots or arbitrary short-word
closure.

No numerical evaluation or source replay is used.

## 1. Exact canonical polynomials

Keep the original finite algebra, crossing matrix \(M_N\), reversal
\(J_N\), Newton evaluation column \(v(w)\), and unit scalar
\(\kappa_N\). Thus
\[
 J_N^2=I,\qquad
 J_NM_N^\sigma J_N
   =\kappa_N^\sigma M_N^{-\sigma}J_NM_N^{-\sigma},
       \qquad \sigma\in\{1,-1\}.                       \tag{1}
\]
These are the all-level identities in
[degree-two source reductions](research_degree_two_short_reductions.md),
Sections 1--4. They hold in the full Hermite algebra, including its
repeated-root normals.

For a word \(\mathbf n=(n_1,\ldots,n_k)\), put
\[
 A_{n,N}=J_NM_N^n,\qquad
 B_{\mathbf n,N}=A_{n_1,N}\cdots A_{n_k,N},\qquad
 E_{\mathbf n,N}(w_L,w_R)=v(w_L)^TB_{\mathbf n,N}v(w_R).
                                                               \tag{2}
\]
For an internal path of \(k\) selected degree-two vertices, (2) is its
literal two-boundary polynomial after all \(k\) original traces have
been taken. Expand the \(k+1\) edge kernels and use
\(\phi_N(R^ne_i e_j)=(A_{n,N})_{ij}\) to see this. There is no
additional power of \(N\). Its degree is at most \(N-1\) separately
in either outside ordinary color, regardless of \(k\).

An internal reduction history is a finite list of replacements
\[
 (a,0,b)\longmapsto(a+b),\qquad
 (a,\sigma,b)\longmapsto(a-\sigma,b-\sigma),
              \quad \sigma=1\ \hbox{or}\ -1,          \tag{3}
\]
each applied to consecutive entries. All outside entries remain in
their original order. Define \(j(\mathcal R)\) to be the sum of the
deleted unit signs; zero deletions contribute zero.
If \(e(\mathbf n)=\sum_i n_i\), then
\[
             j(\mathcal R)
                =\frac{e(\mathbf n)-e(\mathbf m)}{3}.            \tag{3a}
\]
Indeed a zero move preserves this sum, while deleting the sign
\(\sigma\) changes it by \(3\sigma\).

**Proposition 1.** If a history \(\mathcal R\) reduces
\(\mathbf n\) to \(\mathbf m\), then, for every \(N\ge2\),
\[
 B_{\mathbf n,N}
     =\kappa_N^{j(\mathcal R)} B_{\mathbf m,N},
 \qquad
 E_{\mathbf n,N}
     =\kappa_N^{j(\mathcal R)} E_{\mathbf m,N}.          \tag{4}
\]
The second equality is a polynomial identity at every pair of complex
ordinary colors. It preserves all their derivatives and every
subsequent original boundary observation.

*Proof.* Associativity, \(J_N^2=I\), and (1) give
\[
\begin{split}
 A_{a,N}A_{0,N}A_{b,N}&=A_{a+b,N},\\
 A_{a,N}A_{\sigma,N}A_{b,N}
     &=\kappa_N^\sigma
                  A_{a-\sigma,N}A_{b-\sigma,N}.        \tag{5}
\end{split}
\]
Multiply by the unchanged matrices on both sides, and iterate.
Sandwiching the result between the two evaluation columns proves the
polynomial equality. \(\square\)

This is not a pointwise identification of unreduced local angular
integrands. The quotient-algebra moves have first been applied to the
full finite component, and (2) is its canonical outside polynomial.
Consequently the normal-data issue in degree-two source reductions,
Section 4, is resolved before a global color estimate is used.

## 2. Uniform transfer of the full analytic theorem

Suppose \(E_{\mathbf m,N}(-2\cos s,-2\cos t)\) has the complete
kernel hypotheses: a zero-free holomorphic leading amplitude on a
fixed bidisk at \((0,0)\), its original calibrated phase, a uniform
holomorphic relative error \(O(N^{-1})\), and the whole-period bound
\[
 |E_{\mathbf m,N}(-2\cos(x+iy),-2\cos(u+iv))|
 \le C N^d
 e^{N\{M-c(1-\cos x)-c(1-\cos u)+B(y^2+v^2)\}}.        \tag{6}
\]
Then exactly the same estimates, phase, amplitude, color domains,
ordinary normal bounds, and prefactors hold for \(E_{\mathbf n,N}\),
apart from the displayed unit scalar in (4).

This assertion is uniform over every collection of integer words
with the same reduced word. The constants do not grow with the
number of zero/unit expansions or with the magnitudes of their
entries: the complete finite polynomials in (4) differ only by a
scalar of modulus one. If several histories are used, the scalar
must still be retained; its modulus does not affect these estimates.

In particular the
[complete ordinary three/four theorem](research_mixed_three_four_full_boundary_kernel.md)
and its reversal/conjugation consequences apply whenever
\[
 \mathbf m\in
       \{(3,4),(4,3),(-3,-4),(-4,-3)\}.                \tag{7}
\]
The power is still \(N^{-3/2}\), not a power depending on the number
of expanded vertices. Both level parities and all fixed mixed
ordinary derivatives are included. This is an exact closure property
of an already proved kernel class; no near invariance, positivity,
or scalar-overlap assumption is used.

For example,
\[
\begin{split}
 E_{(r,0,3-r,4),N}&=E_{(3,4),N} &&(r\in\mathbb Z),\\
 E_{(4,1,5),N}&=\kappa_NE_{(3,4),N},\\
 E_{(2,-1,3),N}&=\kappa_N^{-1}E_{(3,4),N}.             \tag{8}
\end{split}
\]
The first identity permits unbounded opposite signed powers at
fixed original parities. Iterating zero expansions gives arbitrary
length, while unit expansions give additional mixed-sign examples.
For any one original template only its fixed permitted parities are
used.

## 3. Finite canonical word recognition

There is a sufficient exact test which does not require finding a
particular zero/unit history. Put
\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 T^n=\begin{pmatrix}1&n\\0&1\end{pmatrix},\qquad
 G_{\mathbf n}=\prod_i ST^{n_i}.                        \tag{9}
\]
These are the linear parts of the original supported physical turns
and crossings in
[the definite corridor normal form](research_definite_rational_corridor_normal_form.md).
For the actual two-boundary operator, append the terminal turn:
\(W_{\mathbf n}=(\mathcal T R^{n_1})\cdots
(\mathcal T R^{n_k})\mathcal T\). Its quantum operator is
\(B_{\mathbf n,N}J_N\), and its Frobenius kernel coefficient matrix
is therefore \(B_{\mathbf n,N}\). Its linear matrix is
\(G_{\mathbf n}S\); comparing these matrices is equivalent to
comparing the \(G_{\mathbf n}\) in (9).
For the finite library (7), their representatives are
\[
\begin{array}{c|c}
 (3,4)&\left(\begin{smallmatrix}-1&-4\\3&11\end{smallmatrix}\right)\\
 (4,3)&\left(\begin{smallmatrix}-1&-3\\4&11\end{smallmatrix}\right)\\
 (-3,-4)&\left(\begin{smallmatrix}-1&4\\-3&11\end{smallmatrix}\right)\\
 (-4,-3)&\left(\begin{smallmatrix}-1&3\\-4&11\end{smallmatrix}\right).
\end{array}                                                    \tag{10}
\]
For any finite proved kernel library the same test uses its finite
list of matrices.

**Proposition 2.** If \(G_{\mathbf n}=\pm G_{\mathbf m}\), then
\[
 E_{\mathbf n,N}
   =\kappa_N^{\,\{e(\mathbf n)-e(\mathbf m)\}/3}
                       E_{\mathbf m,N}                         \tag{11}
\]
at every level and all complex ordinary boundary colors. The exponent
is an integer.

*Proof.* With the original exponential choice of its cube root, let
\(\widehat M_N=\kappa_N^{-1/3}M_N\). Equation (1) gives
\[
       J_N^2=I,\qquad (J_N\widehat M_N)^3=I.
                                                               \tag{12}
\]
The presentation \(PSL(2,\mathbb Z)
=\langle S,T\mid S^2=(ST)^3=1\rangle\) therefore defines the
same exact normalized word representation as in the cited normal
form. Equality up to sign in (9) gives equality of the products
\(\prod_i J_N\widehat M_N^{n_i}\). Restore the powers of
\(\kappa_N\) to obtain (11). The homomorphism to
\(\mathbb Z/3\mathbb Z\) taking \(S\) to zero and \(T\) to one
shows that the two exponent sums differ by a multiple of three.
\(\square\)

Thus arbitrary word length can be tested against four integer
matrices for the new library. This is a sufficient symbolic
recognition test, not a claim that any fixed-level quantum
representation is faithful. It yields exactly the full analytic
transfer of Section 2, not just a periodic trace identity.

The linear test is deliberately distinct from the marked topology.
Record also the affine lifts
\[
        \widetilde{\mathcal T}(x,y)=(-y,x+1/2),\qquad
        \widetilde R^{\,n}(x,y)=(x+ny+n/2,y),           \tag{13}
\]
where \(\mathcal T\) is the physical quarter-turn, with linear part
\(S\); the matrix \(T\) in (9) denotes the crossing shear. Compute
these affine lifts on the complete words \(W_{\mathbf n}\) and
\(W_{\mathbf m}\), including their terminal turns.
After their linear parts agree modulo the deck involution, the
remaining half-lattice translation is one of the four proper
half-turn classes. The original normal-form theorem retains this
rotation on the specified attached tangle; it does not erase it.
For a knot transfer one must propagate that rotation, the boundary
order, and all disk frames into the adjacent original subtree.
Only after this marked transport is the recognized library block
installed in the reduced tree. If no such admissible marked
installation is provided, Proposition 2 supplies a full quantum
kernel identity but no independent identification of knot
complements.

## 4. Marked topology and exact affine pullback

To turn the kernel statement into a statement about original knots,
use the physical rules of
[marked degree-two tangle moves](research_marked_degree_two_tangle_moves.md),
Sections 3--5. A zero retains the physical double-turn and all induced
stack reversals. A unit retains the proper half-turn on the indicated
attached branch, changes the two neighbor powers by \(-\sigma\), and
carries every disk frame and ribbon. It is not legitimate to delete
these rotations from an arbitrary attached state.

These rules give ambient isotopies after filling, with the original
component test and preferred zero framing transported. The
uncorrected finite source retains the unit scalar of (4). The
zero-framed invariant and the volume of the filled knot complement
are invariant under the marked isotopies. Exteriors with different
numbers of unfilled crossing circles are not being identified.

More generally, fix an original ordered tree and a prescribed
degree-two reduction history. Its zero/unit constraints are affine
integer equations on the original powers. Write the powers after
reduction as
\[
                         \mathbf n'=L\mathbf n+\mathbf b.       \tag{14}
\]
Each zero replaces two entries by their sum; each unit subtracts
its sign from both neighbors. Thus (14) is obtained using integer
row additions, deletions and translations. With
\(n_v=\eta_v-2p_v\), choose the new carriers with the resulting
parities, and obtain an affine integer map on the original filling
coordinates. The primitive-meridian shears for unit moves are exactly
those in marked degree-two tangle moves, equations (15)--(16).

Rotations caused by a zero depend only on the parities of the
transported powers. Once the original carriers and the reduction
history are fixed, the reduced ordered template is fixed. If the
branch data permit finitely many such marked records, keep all of
them and take the maximum of their thresholds below.

**Theorem 3.** Suppose every reduced marked record has the form
allowed by
[three/four component long fillings](research_three_four_component_long_fillings.md):
its selected components are the pairs (7), and all its other
surviving powers are free. For each fixed record there is a threshold
\(B\) such that every assignment on the original reduction branch
satisfies the original all-integer-level volume identity whenever
\[
          |n'_v|\ge B
          \quad\hbox{for every free reduced vertex }v,           \tag{15}
\]
and the original prescribed knot and component conditions hold.
The whole preimage of these reduced assignments is covered,
including every infinite zero-merger fiber.

*Proof.* Perform the marked reductions, preserving the specified
outside observations. The reduced original diagram satisfies the
cited component theorem at (15). The marked isotopy identifies its
filled knot complement and zero-framed invariant with those of the
original assignment. Alternatively, for expansions entirely inside
a selected corridor, (4) substitutes the full proved kernel before
any outside trace is evaluated; hence its full Hermite observation
is preserved without additional estimates. The reduced theorem
has no exceptional assignments within (15). Its pullback therefore
has no exceptional points in any of those fibers. \(\square\)

The threshold is determined by the reduced marked template and
selection, not by the sizes of canceled powers in a fiber.
For example, a selected \((3,4)\) component may be replaced by
\((2r,0,3-2r,4)\) for every integer \(r\), with fixed carriers
\((0,0,1,0)\). The original filling coordinates of its first and third
vertices can be chosen as \(-r\) and \(r-1\); their effective powers
sum to three. The same threshold on all untouched free powers works
for every \(r\). No separate source or geometric saddle is required
for the expanded zero-filled component.

Condition (15) concerns the surviving affine combinations. It is
not a condition on the absolute values of the separate original
powers: two arbitrarily long opposite powers can have any fixed
sum. The theorem does not change that distinction.

## 5. What re-rooting and padding do not add

Admissible re-rooting is a way to expose the local marked moves and
carry the original closing observation. It can reverse the boundary
order of a path; (7) already includes that case. It does not change
the degrees of vertices or establish a new boundary kernel for an
irreducible adjacent short word. No cyclic trace has been substituted
for the open polynomial (2).

The new consequence is that some previously unresolved *images* of
infinite fibers, namely those now covered by the full three/four
kernel and its admissible assemblies, are no longer unresolved.
No fiber is declared finite. The exact padding equality in
[original tree padding equivalence](research_original_tree_padding_equivalence.md)
continues to hold:
\[
 \mathcal F_{\mathrm{padded}}\cap\{p_0=0\}
             \simeq\mathcal F_{\mathrm{core}}\times\mathbb Z.    \tag{16}
\]
Thus the arbitrary-short partial-filling target still requires
every hyperbolic core reached on an unresolved infinite fiber.

For a word not reduced to an already proved kernel, inserting an
inverse word or changing the root supplies no additional conclusion
here. The existing
[affine-fiber audit](research_affine_reduction_fibers_and_core_obligation.md),
Sections 7, 9 and 10, already records the finite-parent long-filling
obstruction, the unique marked normal forms, and the distinction
between conjugating an operator and retaining its prescribed two
observations. The present deduction adds a constructive transfer on
the accepted reduction branches, rather than another version of
those obstructions.

The genuinely uncovered records include irreducible adjacent mixed
short words beyond the proved kernel library and short branching
components with their original multi-boundary observations.
Theorem 3 resolves neither class.
