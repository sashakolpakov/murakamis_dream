# The global longitude word and the remaining decorated seam calculation

Private derivation, 1 November 2026. This report concerns the original ordered all-circle tree, not a comparison diagram. Its local inputs are the actual white/shaded chart in /private/tmp/md-nonparabolic-two-octahedron-pure-adapter.md and the matched punctures in Section 7 of /private/tmp/md-all-circle-edge-four-punctured-character-adapter.md.

Sections 1--6 isolate the original framing reduction and the missing
decorated seam calculation. Sections 7--9 then give the actual odd
path operator and the explicit pure switch used for a squared chain
identity. A local four-segment commutator is not multiplied over the
edges without checking both main routes at every attachment.

## 1. The topological peripheral correction is already fixed

Keep the prescribed main orientation and the original primitive crossing-circle pairs \((\mu_v,\lambda_v)\). Let \(\epsilon_v\in\{0,\pm1\}\) be the retained half twist, let \(p_v\) be the filling integer, and put
\[
 n_v=\epsilon_v-2p_v.
 \tag{1}
\]
Let \(L_{\mathrm{path}}\) be the original peripheral push-off defined by the pure and odd routes in Sections 5–6 of the preferred-cusp proof. It follows the main knot once. Its exact topological framing is
\[
 [L_{\mathrm{path}}]
 =w_\epsilon[\mu_K]+\sum_v\ell_v[\mu_v],
 \qquad
 \lambda_K=L_{\mathrm{path}}\mu_K^{-w_\epsilon}.
 \tag{2}
\]
Here \(\ell_v\) is the oriented intersection with the original crossing disk. These identities were proved using the original threading words and the two endpoint orientations. They are not consequences of parabolicity or of an additive cusp calculation. The equality in the second formula is an equality of boundary curve classes: both curves traverse the knot once, and the main meridian has primitive nonzero ambient homology, so their difference is exactly the stated meridian power.

The crossing circles are pairwise unlinked. The original integral fillings give
\[
 \lambda_{\mathrm{fill}}
 =\lambda_K\mu_K^{\sum_vp_v\ell_v^2}
 =L_{\mathrm{path}}\mu_K^{-w_\epsilon+\sum_vp_v\ell_v^2}.
 \tag{3}
\]
This is a fixed main-boundary word before imposing a representation. At a smooth filled endpoint it is the preferred zero-linking longitude. It remains the same word on a nearby nonparabolic representation of that filled group.

Let \(o_v=1\) for parallel strands in the original unturned braid box and \(o_v=-1\) for antiparallel strands. The literal crossing convention gives
\[
 \ell_v^2=2(1+o_v),\qquad
 w_\epsilon=\sum_vo_v\epsilon_v,\qquad
 w_{\mathbf n}=\sum_vo_vn_v.
 \tag{4}
\]
Consequently
\[
 -\sum_v\epsilon_v-w_\epsilon+\sum_vp_v\ell_v^2
 =-\sum_vn_v-w_{\mathbf n}=a(D).
 \tag{5}
\]
All these equalities are representation independent. The actual half-turns in the root exposure move the entire marked curves and therefore do not change (2)–(5).

On the source flag the positive main meridian has eigenvalue \(M^{-1}\). Define a longitude coordinate as the inverse of its eigenvalue on this flag. Multiplication of a longitude word by \(\mu_K^k\) therefore multiplies its coordinate by \(M^k\). If the marked path calculation supplies
\[
 L_{\mathrm{path,eff}}
 =-M^{-\sum_v\epsilon_v}
       \prod_e\frac{M^2-X_e}{1-M^2X_e},
 \tag{6}
\]
then (3)–(5), without any further analytic argument, give
\[
 L_{\mathrm{fill,eff}}
 =-M^{a(D)}\prod_e\frac{M^2-X_e}{1-M^2X_e}.
 \tag{7}
\]
Thus the exact missing task is (6), with the actual source flag, rather than a new framing or surgery calculation.

## 2. The native pure block and its four actual routes

Write \(N_j=W_{j-1}^{-1}W_j\), with corners \(0,\infty,1,R\). The determinant-one punctures of the matched pure block are
\[
 A_g=M^{-3}N_3,\quad B_g=MN_0,\quad
 C_g=MN_1,\quad D_g=MN_2.
 \tag{8}
\]
The actual shaded paths satisfy
\[
 \begin{aligned}
 S_vC_gS_v^{-1}&=B_g^{-1},&
 S_vD_gS_v^{-1}&=A_g^{-1},\\
 S_wA_gS_w^{-1}&=B_g^{-1},&
 S_wD_gS_w^{-1}&=C_g^{-1}.
 \end{aligned}
 \tag{9}
\]
The four-segment traversal
\[
 \infty\longrightarrow0\longrightarrow R
       \longrightarrow1\longrightarrow\infty
 \tag{10}
\]
uses \(S_v,S_w^{-1},S_v^{-1},S_w\), respectively. Its based matrix is
\[
 \Lambda_\infty=S_wS_v^{-1}S_w^{-1}S_v.
 \tag{11}
\]
The positive oriented meridians transported along (10) are, in order,
\[
 C_g,\quad B_g^{-1},\quad A_g,\quad D_g^{-1}.
 \tag{12}
\]
Each has eigenvalue \(M^{-1}\) at its indicated geometric corner. This point is important: the native puncture matrices themselves do not all have eigenvalue \(M^{-1}\) at the drawn corners.

For \(f_e=(M^2-X_e)/(1-M^2X_e)\), the direct local calculation gives
\[
 \Lambda_\infty=
 \begin{pmatrix}-f_e^{-1}&*\\0&-f_e\end{pmatrix}.
 \tag{13}
\]
Its source flag is infinity and its local inverse-eigenvalue longitude is \(-f_e\). The projective derivative at that flag is \(f_e^2\).

The matched character construction uses \(V=S_v^{-1}\), \(T=S_w^{-1}\), not \(V=S_v,T=S_w\). The transport \(S_w^{-1}S_v\) carries the infinity basepoint and its marked meridian to the \(R\) basepoint. This conjugates (11) to the corresponding character commutator and preserves its selected eigenvalue. No independent change of flag is allowed in making that comparison.

## 3. What the literal terminal insertion does to the main routes

For a right insertion, the original endpoint rule is
\[
 \begin{array}{c|c}
 v_1-x_1&v_1-w_1,\quad w_2-x_1\\
 v_2-x_2&v_2-w_0,\quad w_3-x_2.
 \end{array}
 \tag{14}
\]
The pure terminal tangle has pairings \(w_0-w_1\) and \(w_2-w_3\). Suppressing its bivalent internal points, (14) therefore replaces the two old connections by
\[
 v_1-v_2,\qquad x_1-x_2.
 \tag{15}
\]
This is a reconnection of the two strands; it is not the insertion of independent scalar factors into their old individual routes. In particular the two modified portions can lie on the same main component or on different main components.

The left insertion is
\[
 \begin{array}{c|c}
 v_3-x_3&v_3-w_3,\quad w_0-x_3\\
 v_0-x_0&v_0-w_2,\quad w_1-x_0.
 \end{array}
 \tag{16}
\]
It is the same reconnection on the other original disk face. The physical quarter-turn, an inverse turn, or the root half-turn carries this entire ordered substitution. None can be replaced by a scalar identity.

An exact global proof of the product in (6) must consequently use the tensor product of the two transported main lines at this face. It cannot choose one of the two modified routes and treat the other as an unchanged spectator.

There is also a useful exact parity consequence. A reconnection of two edges in a disjoint union of cycles changes the number of cycles by one modulo two: it either splits one cycle or merges two. The pure one-edge closed block has one main cycle. Inducting with (14) or (16) gives
\[
 c_{\mathrm{main}}\equiv |E|\pmod{2}
 \quad\text{for the pure tree}.
 \tag{17}
\]
Replacing a pure circle seam by either retained odd seam switches its two strand pairings and toggles this parity. Hence in general
\[
 c_{\mathrm{main}}\equiv |E|+
             \#\{v:\epsilon_v\ne0\}\pmod{2}.
 \tag{18}
\]
Full twists have even parity and do not change it. Thus, if the exact local transport assigns one negative lift per edge and one per odd seam, their product has the required negative sign for a single main knot. Formula (18) is a topological sign count; it does not supply the unproved odd transport factor.

## 4. The two-line normalization and orientation reversal

For a projective map \(T(z)=(az+b)/(cz+d)\), direct differentiation gives
\[
 T'(q_1)T'(q_2)
 =\left(\frac{Tq_1-Tq_2}{q_1-q_2}\right)^2.
 \tag{19}
\]
The formula extends in local coordinates when a point is infinity. Equivalently, for a linear lift and two lifted flags,
\[
 \det(Tv_1,Tv_2)=\det(T)\det(v_1,v_2).
 \tag{20}
\]
These identities show precisely how the tensor product of the two flag lines can be normalized by their wedge. A seam comparison made with the same transported pair has no unrecorded shear in this tensor normalization.

For a single oriented main segment, choose determinant-one eigenframes at its endpoints. If its transport has diagonal entries \(a,a^{-1}\), reversing the traversal and exchanging the selected meridian eigenline uses the second diagonal entry of its inverse, namely \(a\). Thus the scalar is unchanged. With an endpoint permutation the same statement holds up to the fixed permutation sign; it is exact after squaring.

This is the multiplicative counterpart of the direction-independent displacement convention in the parabolic longitude proof. It is not permission to exchange one flag while keeping its original transport matrix or white frame fixed. The two flags used in (19)–(20) must be the flags carried by the actual routes (14)–(16). With that condition, internal frame factors can telescope when the scalar line transports are multiplied in cyclic order.

The remaining pure insertion calculation is to match the two-line normalization in (19)–(20) to the normalization used in the closed traversal (11) for every transported endpoint frame. Its projective target is that adjoining one pure edge multiplies the total squared path coordinate by \(f_e^2\). This is a statement about the two actual routes at the deleted triangle, not about arbitrary pants decompositions or local commutator values alone.

## 5. Why the equal-eigenvalue Hurwitz identity is insufficient

The actual native disk flags have opposite eigenvalues for its two raw boundary generators. To make the issue explicit, take a basis \(a=e_1,b=e_2\) and write
\[
 A=\begin{pmatrix}\lambda&\alpha\\0&\lambda^{-1}\end{pmatrix},
 \qquad
 B=\begin{pmatrix}\lambda&0\\\beta&\lambda^{-1}\end{pmatrix}.
 \tag{21}
\]
Then \(Aa=\lambda a\) and \(Bb=\lambda^{-1}b\). Put
\[
 h=\lambda-\lambda^{-1},\qquad
 D=\alpha\beta+h^2,\qquad
 a_-=(-\alpha,h)^{\mathsf T},\quad
 b_+=(h,\beta)^{\mathsf T}.
 \tag{22}
\]
The latter two vectors are the other eigenflags. Let
\[
 K=(BA)^{-1}-I.
 \tag{23}
\]
Direct multiplication, without diagonalizing at the parabolic value, gives
\[
 Ka_-=D A^{-1}b,\qquad Kb_+=-\lambda^{-1}D a,
 \qquad \det K=-D,\qquad
 \det(a_-,b_+)=-D.
 \tag{24}
\]
For example
\[
 K=\begin{pmatrix}
 \alpha\beta+\lambda^{-2}-1&-\lambda\alpha\\
 -\lambda\beta&\lambda^2-1
 \end{pmatrix},
 \tag{25}
\]
which makes (24) immediate using \(\lambda h=\lambda^2-1\). Thus the regular Hurwitz conjugator does send the exchanged input flags to the desired permuted output flags. It does not send the original pair \((a,b)\) to that pair.

Wedge normalization of (24) is exact, but it compares two different input line pairs. It does not define a scalar identification between \(a\otimes b\) and \(a_-\otimes b_+\). Such an identification must come from the actual oriented disk paths and their transported white frames.

Consequently the valid identity for two equal raw eigenvalues cannot yet establish that the actual positive odd seam contributes \(M^{-1}\) to the inverse-eigenvalue path coordinate, or that the negative seam contributes \(M\). An actual collar calculation with its flag exchange is necessary. The desired squared correction is \(M^{-2\epsilon_v}\), with one contribution per distinguished original odd seam.

## 6. Exact remaining statement

The sufficient remaining local-to-global statement is:

1. Under each literal left/right pure terminal insertion, both transported main lines give the normalized squared path multiplier \(f_e^2\), with their endpoint wedge factors cancelled in the actual seam charts.
2. The actual positive and negative distinguished seams, with all white frames and eigenflags transported, give \(M^{-2}\) and \(M^2\), respectively.
3. Their determinant-one lifts have the local signs retained in (13) and in the actual collar calculation. Equation (18) then fixes the single global negative sign when the main strands form a knot.

These statements would establish (6). Equations (2)–(5) then prove (7) with the original preferred longitude and original filling integers. No cusp derivative, source asymptotic, reciprocity, or equality of abstract character polynomials is needed in that final framing step.

At this checkpoint the topological framing formulas, literal reconnection/parity calculation, local marked commutator, and linear-algebra identities above are established. The decorated insertion and odd-collar comparisons are the explicit outstanding word calculations. There is no assertion here that the general geometric eigenvalue identification has already been completed.

## 7. The actual odd paths give the inverse returned braid

The exact peripheral paths resolve an ambiguity left by an unbased
Hurwitz calculation. This section is an additional local result; the
global cancellation of the resulting endpoint frames remains separate.

Use the first row of the full boundary table in the pure-page sewing
note, and abbreviate
\[
 a=B_g,\qquad b=A_g,\qquad C_0=S_v^{-1},\qquad
 H=(ba)^{-1}-I,\qquad \delta=\det H.
 \tag{26}
\]
Then
\[
 C_0aC_0^{-1}=C_g^{-1},\qquad
 C_0bC_0^{-1}=D_g^{-1}.
 \tag{27}
\]
The actual positive auxiliary meridian is \(C_+=C_0H\).
The original longitudinal paths, with the original white-side choices,
are
\[
 L_{02}=C_g^{-1}C_+,\qquad L_{13}=C_+^{-1}.
 \tag{28}
\]
These are the words of the preferred-cusp proof, equation (32), with
its \(\mu_1=C_g^{-1}\). They are identities of the original
cut paths, so they survive a change of the developed white charts.
In particular (27) gives
\[
                         L_{02}=C_0aH.
 \tag{29}
\]
Reverse the second path and exchange its eigenline. In
determinant-normalized eigenframes this preserves its transport
coefficient. Both paths now cross the disk collar in the direction
of \(C_0\). Their ordered input lines are the
\(M^{-1}\) lines of \((a,b)\): the other line of \(B_g\)
at the first puncture, and the displayed line of \(A_g\) at
the second. Thus the pair used here is explicitly different from
the two native ideal flags.

After returning the output frame by \(C_0^{-1}\), and putting
the outgoing strands in their prescribed order, their tensor
transport is
\[
 \mathscr L_+
   =\delta^{-1}(H\otimes aH)\mathsf s,\qquad
 \mathsf s(u\otimes v)=v\otimes u.
 \tag{30}
\]
The determinant factor is the two-line normalization: the simultaneous
frame change \(H\) acts on a tensor pair by
\((H\otimes H)/\det H\), not by a chosen square root.
The extra \(a\) in the second factor is the actual extra
meridian in (28).

The returned braid of the separate linear-algebra calculation is
\[
 \mathscr B=
   \delta(H^{-1}a^{-1}\otimes H^{-1})\mathsf s.
 \tag{31}
\]
Since \(\mathsf s(X\otimes Y)=(Y\otimes X)\mathsf s\),
(30) is exactly \(\mathscr B^{-1}\).
On two equal eigenlines \(au=\lambda u,\ bv=\lambda v\),
that operator has the scalar
\[
 \mathscr L_+(u\otimes v)
       =-\lambda^{-1}u\otimes v.
 \tag{32}
\]
Taking \(\lambda=M^{-1}\), the inverse-eigenvalue path
factor is therefore \(-M^{-1}\). Its square is \(M^{-2}\).
This sign and exponent follow from the actual white-side route
(28), rather than from a cusp derivative.

The negative collar is equally explicit. Put \(C_-=C_0H^{-1}\).
The original negative paths are
\[
 L_{02}=C_-,\qquad L_{13}=aC_-^{-1}.
 \tag{33}
\]
Reverse and dualize the second one as before. The ordered returned
tensor is now
\[
 \mathscr L_-=
   \delta(H^{-1}a^{-1}\otimes H^{-1})\mathsf s
   =\mathscr B.
 \tag{34}
\]
It has scalar \(-\lambda\) on the equal pair, and consequently
inverse-eigenvalue path factor \(-M\), with square \(M^2\).
The pure returned pair is the identity. Thus both signs of the
desired local odd correction are now fixed by actual route words.

Equations (30)--(34) should not be applied to the original mixed
native ideal pair. The preliminary reversal and dualization is part
of the derivation. To use these local factors in (6), the same
determinant-normalized endpoint frames must be retained and cancelled
through the actual global peripheral circuit. That is the remaining
chain calculation.

## 8. A two-line formulation of the remaining pure insertion

Here is a precise scalar-line formulation which reduces the global
issue to the actual boundary substitution. It also explains why
merely multiplying matrices for closed local commutators is inadequate.

For an ordered pair of puncture matrices \((a,b)\), select the
same eigenvalue \(\lambda=M^{-1}\) after coorienting the two
strands. Write their eigenlines as \(L_a,L_b\).
On the open set where their eigenvectors are independent, the tensor
\[
       \mathfrak t(a,b)=
          \frac{u\otimes v}{u\wedge v},
       \qquad u\in L_a\setminus\{0\},\
              v\in L_b\setminus\{0\},
 \tag{35}
\]
is independent of their separate scales. Its denominator belongs
to the determinant line of the two-dimensional representation space.
For every simultaneous change of developed frame \(G\),
\[
 \frac{G\otimes G}{\det G}\,\mathfrak t(a,b)
       =\mathfrak t(GaG^{-1},GbG^{-1}).
 \tag{36}
\]
Consequently a pure ordered disk-side identification contributes
one in these pair sections. This uses both puncture conjugacies,
not only the auxiliary boundary multiplier. Exchanging their
order changes the wedge sign. That sign disappears in the
squared longitude calculation.

An actual main arc can be evaluated in either direction: the inverse
path on the other meridian eigenline has the same coefficient in
determinant-normalized eigenframes. This permits every local disk pair
to be cooriented before using (35). The endpoint changes have to be
carried into the adjoining pair sections; (36) is the exact
cancellation identity when the two adjoining sections describe the
same transported punctures.

To complete the pure induction one must establish the following
boundary-torsor statement from the two-sided substitutions (14),(16).
After adjoining the new edge block and closing its new terminal circle
by its pure distinguished seam, the two original boundary routes
induce a map of the old pair section to the new pair section. Its
squared inverse-eigenvalue coefficient is \(f_e^2\).
The ordinary pure disk-side closure of that same local map gives
the four-segment word (11). Since the closure contributes one by
(36), this would identify its coefficient by (13).

There are two concrete checks in that statement. First, the pairs
used before and after the insertion must be the two transported
punctures in (14), including the dualization forced when the
reconnection reverses a strand. Second, the local closing operation
must be exactly the pure disk-side identification used to obtain
(11), rather than a different choice of boundary framing.
The endpoint compiler and full boundary tuple supply the data to
make these checks. A dimension-one argument without those checks
would only identify an unspecified scalar.

Once that boundary-torsor statement is proved, induction on terminal
insertions multiplies \(f_e^2\) over all edges. The endpoint
sections cancel by (36), independent of whether an insertion joins
two old peripheral cycles or splits one. At each distinguished odd
seam the actual maps (30),(34) then supply \(M^{-2\epsilon_v}\).
The topology parity (18) fixes the remaining global lift sign after
the individual lift normalization has been checked. This is a finite
chain calculation on the original ordered diagram; no isotropy of a
character variety or equality of cusp derivatives is part of it.

## 9. The explicit pure switch and its squared chain identity

The actual attachment labels supply the two checks specified in
Section 8. In the octahedron attached along
\((O_v,B,C)\) to the old face \((O_v,C,B)\), put
\[
       (A,B,C,D)=(0,\infty,1,R).
 \tag{37}
\]
The old exposed pair is \((\infty,1)\); the new inner pair
is \((0,R)\). The remaining new \(v\) face is
\((O_v,R,0)\). The two new \(w\) faces are
\((O_w,R,1)\) and \((O_w,\infty,0)\).
Thus the frame comparison from old to new is precisely \(S_v\):
\[
 S_v:\infty\longmapsto0,\quad1\longmapsto R.
 \tag{38}
\]
The actual pure terminal-circle identification is precisely \(S_w\):
\[
 S_w:R\longmapsto0,\quad1\longmapsto\infty.
 \tag{39}
\]
No three-point map has been chosen to fit a desired scalar: these
are the four original shaded triangles in the literal insertion
table. The same statement for left insertion is its transported
face table, with the actual endpoint reversal retained.

Here is the scalar-line switch identity used for those four strips.
Assign determinant-one eigenframes to their endpoints. Evaluate a
strip in either direction, exchanging its eigenline when its direction
is reversed. Its coefficient is unchanged by that operation.
Normalize a cut pair by (35). Suppose the old pair is replaced by
the two new connections (39), and identify its new inner endpoint
frames with its old frames by (38). The ratio of the squared
inverse-eigenvalue products of all resulting closed peripheral cycles
is the projective derivative of
\[
 \infty\xrightarrow{S_v}0
 \xrightarrow{S_w^{-1}}R
 \xrightarrow{S_v^{-1}}1
 \xrightarrow{S_w}\infty .
 \tag{40}
\]

For clarity, this identity does not require the two outside routes
to lie on the same cycle. Choose the frames at \(0,R\) to be
the \(S_v\)-transports of the frames at \(\infty,1\).
Then the old-to-new comparisons contribute one on their selected
lines. At a reversed strip use the dual frame, so its coefficient
is still the original coefficient, rather than its reciprocal.
All unaffected outside strips occur once in both products and
cancel. The remaining inner and outer connections are exactly
the second and fourth arrows of (40); restoring the chosen
comparison frames inserts its first and third arrows. Their
product is the based return in (40).
Changing either endpoint eigenframe rescales the two adjacent
coefficients reciprocally. Changing the simultaneous developed
frame at a cut pair cancels by (36).
Exchanging the pair order changes only the determinant sign,
which disappears after squaring. These statements also cover
the split-cycle and merged-cycle cases of the reconnection.

Equivalently, in these transported full eigenframes write the
two maps in (39) as
\[
 S_w:R\longrightarrow0:\ 
       \operatorname{diag}(c,c^{-1}),\qquad
 S_w:1\longrightarrow\infty:\ 
       \operatorname{diag}(d,d^{-1}).
 \tag{40a}
\]
Here the frame at \(R\) in the first display is the one
transported by \(S_v\), with its dual chosen whenever the
actual route is reversed. The selected coefficient of (40)
is \(d/c\). Its inverse-eigenvalue square is
\((c/d)^2\), which is the same switch ratio obtained by
cancelling the outside strips. This makes the inverse on the
inner connection visible; multiplying \(c\) and \(d\)
without that reversal would be incorrect.

By (11)--(13), the derivative in (40), at the selected infinity
flag in its finite coordinate \(1/z\), is \(f_e^2\).
Therefore every actual pure terminal insertion has squared
path multiplier
\[
 \frac{L_{\mathrm{path,new}}^2}
      {L_{\mathrm{path,old}}^2}=f_e^2.
 \tag{41}
\]
There is a native-frame qualification in using this calculation
through the whole tree. The local page chart at an edge can use
the parameter \(M_e=M^{-1}\), as required by the bipartition
of its two disk-side frames. In that chart
\(f(M_e,X_e)=f(M,X_e)^{-1}\).
The globally selected \(M^{-1}\) meridian line is then the
other line of the canonical local meridian, whose displayed
eigenvalue is \(M_e^{-1}=M\).
The projective derivative of the local return on that other line
is \(f(M_e,X_e)^{-2}=f(M,X_e)^2\).
Reversing the physical traversal exchanges the line and inverts
the return simultaneously, leaving the same answer.
Thus (41) always uses the original global parameter \(M\);
it does not multiply factors formed with inconsistent native
choices of \(M_e\).
The formula is an identity of the normalized scalar-line products;
it does not identify the old and new individual peripheral
cycles. For a single knot their product is its own path coordinate.
For several intermediate cycles, the direction/dual convention
is used before taking that product.

Induction with the original ordered terminal insertions proves
the pure product. At an odd distinguished seam the very same
pair normalization is used in (30),(34), after the explicit
coorientation of its second path. Those two operators act
scalarly on that pair, so no mixed native eigenline is silently
identified with a different one. Consequently the squared
formula for the actual ordered construction is
\[
 L_{\mathrm{path,eff}}^2
       =M^{-2\sum_v\epsilon_v}\prod_e f_e^2.
 \tag{42}
\]
This argument retains every original half-turn frame and every
left/right insertion, since they transport the entire switch
(37)--(40). It uses the actual odd path words (28),(33),
not just a mapping-class action on unframed punctures.

Formula (42), together with (3)--(5), gives the exact squared
preferred-longitude identity. The squared chain proof deliberately
does not conceal the remaining lift sign in a choice of square
root. It can be fixed independently by the Seifert-surface frame
argument in /private/tmp/md-preferred-longitude-negative-lift-seifert-frame.md:
at an actual complete filled knot point the preferred longitude
has negative unipotent lift. Every factor \(f_e\) is one
there, and the holomorphic two-valued ratio is constant. This
gives the negative sign in (7) on the connected geometric germ.
The calibration concerns only the remaining sign; it is not used
to infer the squared dependence in (42).
