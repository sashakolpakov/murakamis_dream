# The preferred knot-cusp shape from a Conway construction

1 November 2026.

A cusp of a hyperbolic knot complement has a Euclidean torus cross-section. Its meridian goes once around the knot. Its preferred longitude follows the knot once and has linking number zero with it. Normalize the meridian's Euclidean translation to one; the longitude then translates by a complex number \(\tau_{\mathrm{main}}\), the **preferred cusp shape**. This note computes that number from the actual face maps of a Conway construction.

The constructions considered here begin with two-string tangles in a ball, with four ordered endpoints. They are joined by vertical stacking and quarter-turns in the projection plane, and then closed by the prescribed cylindrical matching. Each twist region has its original crossing circle: a small auxiliary circle bounding a disk punctured by the two main strands. The [strict Conway construction](actual_conway_all_strict_tree_long_twist_volume.md), Sections 1–3, specifies the endpoint order, closing convention, and angle conditions. In its positive angle domain the leaf angles satisfy \(0<x<1/2\), and every retained product cell satisfies
\[
                         \max(x,y)<z<x+y<1.
\]
Write \(T\) for the actual quarter-turn and \(C\) for this cylindrical closure. The symbol \(R\), when used as a tangle rather than a quadrilateral parameter, denotes the original positive checked crossing. An elementary piece \(h_\epsilon\) contains its retained crossing circle and the half twist \(\epsilon\), after the quarter-turn; \(p_\epsilon\) denotes the same piece before that turn. The forced flat final product is removed with its exact complementary-label relation. These hypotheses supply the actual complete augmented geometry, not just a combinatorial diagram.

The [original ribbon cut](actual_conway_bowtie_projection_cut.md) identifies the two geometric balls and their face pairings with the augmented link exterior. The [marked deformation](actual_conway_general_mask_marked_filling.md) continues those maps, keeps the main meridian parabolic, and fixes the primitive auxiliary filling curves. We use those geometric inputs throughout. The proof below first adds the translations of a specified longitudinal path, then determines its framing by homology. In particular, it does not identify a preferred longitude solely from a parabolic trace or from a quantum asymptotic.

The geometric result applies to the full strict class with one main knot component. Section 9 gives the quantum consequence for these strict presentations when the fixed signed twists are independently sufficiently long. Those analytic hypotheses are stated there; the geometric calculation is proved directly from the marked representation.

## 1. Statement and conventions

Fix a strict ordered Conway construction whose main strands form one component, with no additional internal main circle. Retain all original crossing circles and choose each half-twist sign \(\epsilon_i\in\{0,\pm1\}\) in its original leaf frame. The existing marked construction gives a holomorphic representation near its complete augmented holonomy, keeps the main meridian parabolic, and retains the original primitive auxiliary slopes. Let \(U_i,V_i\) be the continued squared-eigenvalue logarithms of the primitive auxiliary meridian and disk longitude, respectively. Fill the auxiliary circles with the original equations
\[
 U_i+p_iV_i=-2\pi i,\qquad n_i=\epsilon_i-2p_i.
\tag{1}
\]
The main knot cusp is not filled.

Group consecutive products with no intervening quarter-turn into a product junction. The resulting calculation tree has a quarter-turn on each edge between junctions; an original crossing-circle operator is retained at its own vertex. Let \(\mathcal E_T\) be these actual quarter-turn edges, including those incident to an original circle vertex. If the ordered quadrilateral at the input of this turn has normalized angle label \(b_e\), define \(x_e=1-b_e\). This is also the label shared by the two ends of the edge in the paired polynomial calculation, where it is called the covariant Newton label. A pair of successive turns may be retained or removed; its two cotangent terms cancel.

Let \(w_\epsilon\) be the oriented writhe of the original main diagram with its retained half twists, using the same positive braid convention as the actual \(R\). Let \(\ell_i\) be the linking number of the main component with crossing circle \(i\), in its primitive disk marking.

The preferred main-cusp shape on the filled branch is
\[
\boxed{\quad
\tau_{\mathrm{main}}
=2i\sum_{e\in\mathcal E_T}\cot(\pi x_e^{\mathrm{fill}})
  -\sum_i\epsilon_i-w_\epsilon+\sum_i p_i\ell_i^2.
\quad}
\tag{2}
\]
The meridian translates by one, and the orientation is chosen so the cusp shape at the complete point has positive imaginary part. A crossing circle has \(\ell_i=0\) when its two original strands are antiparallel, and \(\ell_i=\pm2\) when they are parallel. Full twists do not change this orientation relation. Consequently, if \(w_{\mathbf n}\) is the oriented writhe after the indicated fillings, the integer in (2) is
\[
 A=-\sum_i n_i-w_{\mathbf n}
   =-2\sum_{\text{parallel }i}n_i.
\tag{3}
\]
The first expression is convention-safe: both its integers are taken in the actual original braid convention. In particular the statement does not identify an unmarked cusp lattice with a preferred longitude merely by choosing a positive imaginary part.

We prove (2) by first constructing a definite framed longitude in the augmented exterior, computing its translation by local composition, and then determining its homology. The proof is valid for the entire nearby geometric representation, before the auxiliary filling equations are imposed.

## 2. Meridians, endpoint signs, and additive displacement

Normalize each ordered quadrilateral to
\((C_0,C_1,C_2,C_3)=(0,\infty,1,R)\), and put \(E=e^{2\pi i b}\).
In these charts, a white face is a piece of an original projection region; the other, shaded faces are pieces of the crossing disks. Use the actual white matrices
\[
\begin{split}
W_0&=\begin{pmatrix}1&0\\0&E\end{pmatrix},
&W_1&=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\\
W_2&=\begin{pmatrix}E-R&R(1-E)\\E-1&1-ER\end{pmatrix},
&W_3&=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
\end{split}
\tag{4}
\]
At an open shaded boundary some of these are completion maps. The marked geometry theorem proves that every occurrence used in the final closed peripheral paths is supplied by the actual adjacent white face.

Set \(d_j=(-1)^j\) and
\[
 \mu_j=(W_{j-1}^{-1}W_j)^{d_j}.
\tag{5}
\]
The coordinates
\[
\begin{split}
\xi_0(z)&=\frac{ER}{(E-1)z},
&\xi_1(z)&=-\frac{z}{E-1},\\
\xi_2(z)&=-\frac{E(R-1)}{(E-1)(z-1)},
&\xi_3(z)&=-\frac{R(R-1)}{(E-1)(z-R)}
\end{split}
\tag{6}
\]
send the corresponding corner to infinity and send \(\mu_j\) to \(u\mapsto u+1\). These identities follow by multiplying (4).

The endpoint sign has a geometric meaning. Orient a main arc into its leaf at corner \(j\). Its positively oriented small meridian is \(\mu_j^{d_j}\); orient the arc out of the leaf and it is \(\mu_j^{-d_j}\). This is the right-hand meridian convention in the ordered projection chart \(0,1,2,3\): crossing one white sector and returning through the preceding one gives \(W_{j-1}^{-1}W_j\) for an inward arc. Formula (5) therefore supplies exactly the displayed signs. At infinity use the finite local coordinate \(1/z\). Reversing the strand orientation reverses both its meridian and the direction of its longitude.

Consider an open main arc from corner \(j\) to corner \(k\), including its specified peripheral push-off. In the local coordinates its actual transport has the form
\[
                    u_k=-d_jd_k\,u_j+\beta.
\tag{7}
\]
The multiplier follows by transporting the same oriented meridian: it is \(d_j\) times the local unit at the incoming endpoint and \(-d_k\) times the local unit at the outgoing endpoint. Define the displacement of this arc to be
\[
                              D_{\mathrm{arc}}=-d_k\beta.
\tag{8}
\]
This definition does not depend on the direction in which the arc is followed. The inverse affine map has translation \(-\beta/(-d_jd_k)\), and its displacement is
\(-d_j[-\beta/(-d_jd_k)]=-d_k\beta\).
This simultaneously reverses the path and the oriented meridian; it does not add raw translations from incompatible meridian frames.

When two endpoints are joined by an actual identity segment, its coordinate change from \(j\) to \(k\) has the same affine multiplier \(-d_jd_k\). Its contribution is instead
\[
                              D_{\mathrm{join}}=d_k\beta.
\tag{9}
\]
Here the path leaves the first arc and enters the next. The same inverse-map calculation proves direction independence.

These displacements add under concatenation. For an arc \(i\to j\), a joining segment \(j\to k\), and an arc \(k\to l\), write their shifts as \(\beta_X,\beta_J,\beta_Y\). Multiplying the three affine maps gives shift
\[
 (-d_kd_l)(-d_jd_k)\beta_X
       +(-d_kd_l)\beta_J+\beta_Y.
\]
Multiplying by \(-d_l\) gives exactly
\[
              -d_j\beta_X+d_k\beta_J-d_l\beta_Y.
\tag{10}
\]
The product multiplier is \(-d_id_l\), as required. The same identity applies when a join creates a closed component. A closed component has multiplier one and its displacement is its actual longitude translation in the consistently oriented unit-meridian frame.

Let \(S(Q)\) be the sum of these displacements for the two open arcs and any already closed main components inside a tangle. If a boundary coordinate at a corner changes by \(u'_j=\alpha_j u_j+\beta_j\), with \(\alpha_j=d_j/d'_j\), then
\[
                    S(Q')-S(Q)=-\sum_{\text{four endpoints }j}d'_j\beta_j.
\tag{11}
\]
This follows from (8), once at each endpoint. Closed components do not change. Equations (7)–(11) are a local chain lemma: they apply regardless of how many odd leaves a component visits or which direction is used to evaluate it.

For an open expression, this is boundary-chart bookkeeping in the original two-ball cut, with its completion maps still labeled as such. It does not declare its metric quadrilateral to be a physical four-punctured tangle boundary or assign virtual white maps to new group generators. The product identities transport this bookkeeping. At the final closure every used white completion is the actual adjacent original white transition, by the marked mask theorem. Only then do the assembled paths give the asserted closed peripheral words.

Equivalently, for any one step write
\(\xi_bF\xi_a^{-1}(w)=\kappa w+\beta\), and let the globally oriented meridian be the local unit raised to \(\alpha_a,\alpha_b\in\{1,-1\}\). Consistency is
\(\alpha_b\kappa=\alpha_a\); the actual translation contribution is \(\alpha_b\beta\). Reversing the traversal replaces the shift by \(-\beta/\kappa\), and reversing the oriented meridian replaces the target sign by \(-\alpha_a\). Their product is again \(\alpha_b\beta\). Equations (8) and (9) are this rule at an arc and a joining segment respectively. This explicitly includes the multiplier-minus-one odd routes below.

## 3. The exact product potential

Define the boundary potential
\[
                  P(E,R)=\frac{E+R}{E-1},\qquad I(Q)=S(Q)-P(E,R).
\tag{12}
\]
For the original ordered product prism we claim
\[
                         I(FG)=I(F)+I(G).
\tag{13}
\]
This is an identity of actual coordinate transports, not an equality of their absolute values.

Here is a rational verification retaining every translation. Write the prism angle phases as \(a,b,c\), so its vertices are
\[
 v_0=1,\quad v_1=a,\quad v_2=ab,\quad v_3=abc,\qquad
 P_*=
 1+a-a\,\frac{ab(1+c)-1-a}{a^2b^2c-a}.
\tag{14}
\]
The lower, upper and output ordered quadrilaterals are
\((1,a,P_*,\infty)\), \((\infty,P_*,ab,abc)\), and \((1,a,ab,abc)\).
Their \(E\) parameters are \(bc,ab,abc\). Their normalized fourth vertices are
\[
\begin{split}
 R_F&=\frac{a(b-1)(bc-1)}{(ab-1)(abc-1)},\\
 R_G&=\frac{c(b-1)(ab-1)}{(bc-1)(abc-1)},\\
 R_o&=\frac{(b-1)(abc-1)}{(ab-1)(bc-1)}.
\end{split}
\tag{15}
\]
Apply (6) after the unique normalized three-point map for each quadrilateral. The two joining and four external rebasing maps all have multiplier one. Their translations are
\[
\begin{array}{c|c}
F_2\longrightarrow G_1&bc/(bc-1)\\
F_3\longrightarrow G_0&-a(b-1)/[(ab-1)(abc-1)]\\
F_0\longrightarrow o_0&0\\
F_1\longrightarrow o_1&0\\
G_2\longrightarrow o_2&ab(c-1)/[(ab-1)(abc-1)]\\
G_3\longrightarrow o_3&(b-1)(c-1)/[(ab-1)(bc-1)(abc-1)].
\end{array}
\tag{16}
\]
For example a world quadrilateral \((q_0,q_1,q_2,q_3)\) is normalized by
\((z-q_0)(q_2-q_1)/[(z-q_1)(q_2-q_0)]\), with the corresponding limits at infinity. Inserting this map into (6) gives (16).

By (9) and (11), the correction \(S(FG)-S(F)-S(G)\) is minus the first entry of (16), plus the second, minus the fifth and plus the sixth. Substituting (15) into (12) gives exactly that expression:
\[
 S(FG)-S(F)-S(G)
                  =P(abc,R_o)-P(bc,R_F)-P(ab,R_G).
\tag{17}
\]
This proves (13). All variables in (14)–(17) are independent wherever the displayed charts are nondegenerate. Thus the identity continues to the original complex deformed branch. In particular hidden binary resolutions inside a product hub contribute no uncancelled term.

## 4. Turns and the final closure

The actual quarter-turn is
\[
 T_Q(z)=\frac{R-1}{z-1},\qquad
 (E,R)\longmapsto(E^{-1},1-R),\qquad j\longmapsto j-1.
\tag{18}
\]
In the coordinates (6), the four rebasing maps have multiplier minus one. In old corner order \(j=0,1,2,3\), their shifts are
\[
 \frac{ER}{E-1},\quad-\frac1{E-1},\quad0,\quad\frac R{E-1}.
\tag{19}
\]
Equation (11) gives \(S(TQ)-S(Q)=(ER-R+1)/(E-1)\). Subtract the two potentials in (12). The result is
\[
 I(TQ)-I(Q)=\frac{2(E+1)}{E-1}=-2i\cot(\pi b).
\tag{20}
\]
This calculation retains the minus multipliers in (19); summing their shifts without (11) would give the wrong sign.

At the final reverse-order closing gluing, the two input parameters are \((E,R)\) and \((E^{-1},R)\), and the actual map from the second to the first is
\[
                       C_Q(z)=\frac{z-R}{z-1},\qquad j\longmapsto3-j.
\tag{21}
\]
Its four affine multipliers are one. In old corner order their shifts are
\[
       \frac R{E-1},\quad-\frac E{E-1},
                       \quad-\frac1{E-1},\quad\frac{ER}{E-1}.
\tag{22}
\]
The joining correction (9) is \(R-1\), whereas
\(P(E,R)+P(E^{-1},R)=1-R\). Therefore the total translation of the closed main components is exactly
\[
                             I(F)+I(G).
\tag{23}
\]
The original closed component decomposition is retained throughout. When the main strands form a knot, (23) is the translation of one primitive longitudinal traversal.

## 5. Pure and odd leaf paths

The actual pure and odd shaded maps are
\[
 S=\begin{pmatrix}0&-ER\\1&-1-E\end{pmatrix},\quad
 A=\begin{pmatrix}R&-R\\1&ER-1-E\end{pmatrix},\quad
 B=\begin{pmatrix}R/E-1-1/E&R\\-1&R\end{pmatrix}.
\tag{24}
\]
The pure arcs \(0\to1\) and \(2\to3\) use \(S^{-1}\) and \(S\). From (6),
the translations of \(S:1\to0\) and \(S:2\to3\) are
\((E+1)/(E-1)\) and \((R-1)/(E-1)\). Thus
\[
 S(h_0)=\frac{R-E-2}{E-1},\qquad
 I(h_0)=-\frac{2(E+1)}{E-1}=2i\cot(\pi x).
\tag{25}
\]

At an odd leaf the main arcs pair \(0\) with \(2\) and \(1\) with \(3\). The shaded maps \(B:0^+\to2^-\), \(A:1^+\to3^-\) switch projection balls. To express a path again in the plus frame, use the indicated actual adjacent white return. For the physical sign \(\epsilon=+1\), choose
\[
 L_{02}^{+}=W_1^{-1}B,\qquad L_{13}^{+}=W_2^{-1}A.
\tag{26}
\]
For \(\epsilon=-1\), choose
\[
 L_{02}^{-}=W_2^{-1}B,\qquad L_{13}^{-}=W_3^{-1}A.
\tag{27}
\]
These are specified peripheral paths. We will determine their framing by homology rather than assuming that an adjacent white-side choice is the preferred longitude.

In the plus \(\xi\) coordinates, all four maps have multiplier minus one, as (7) requires for equal-parity endpoints. Their shifts, in the order \(02,13\), are
\[
\begin{split}
\epsilon=+1:\quad&
  \frac E{E-1},\quad\frac{R-E-1}{E-1},\\
\epsilon=-1:\quad&
  \frac1{E-1},\quad\frac{R-2}{E-1}.
\end{split}
\tag{28}
\]
Using (8), rather than summing these raw shifts, gives
\[
 S(h_\epsilon)=S(h_0)-\epsilon,\qquad
                  I(h_\epsilon)=2i\cot(\pi x)-\epsilon.
\tag{29}
\]
The relations hold at independent nearby \(E,R\). The selected hidden auxiliary color affects \(R\) but does not change (29).

Every original \(h_\epsilon\) is the turn of its unturned crossing-circle piece \(p_\epsilon\). Its input label is \(1-x\). Equation (20) therefore says \(I(p_\epsilon)=-\epsilon\). Equations (13), (20) and (23) now prove for the specified closed longitudinal path
\[
                   \tau_{\mathrm{path}}
        =2i\sum_{e\in\mathcal E_T}\cot(\pi x_e)-\sum_i\epsilon_i.
\tag{30}
\]
This explains precisely why the sum is over physical turn edges, not arbitrary unturned edges in a binary product resolution. Lowering a turn makes its covariant index \(x_e\) complementary to its unturned input. Consecutive double turns contribute opposite cotangents and may be suppressed. Root changes merely reassociate this same geometric sum.

## 6. The integer framing of the constructed path

The original marked threading calculation identifies the actual auxiliary meridians as
\[
 M_+=W_0^{-1}B\quad\text{for physical }R,\qquad
 M_-=A^{-1}W_0\quad\text{for physical }R^{-1}.
\tag{31}
\]
These signs are fixed geometrically in [the marked geometric deformation](actual_conway_general_mask_marked_filling.md), Section 6, from the original threading word; they are not chosen from a quantum asymptotic.

The exact odd edge relations give
\[
\begin{array}{c|cc}
 &L_{02}&L_{13}\\ \hline
R&\mu_1M_+&M_+^{-1}\\
R^{-1}&M_-&\mu_0M_-^{-1}.
\end{array}
\tag{32}
\]
For example \(W_2^{-1}A=M_+^{-1}\), and
\(W_1^{-1}B=(W_1^{-1}W_0)M_+=\mu_1M_+\).
For the second row use
\(W_2^{-1}BW_0^{-1}A=I\) and
\(W_3^{-1}W_0=\mu_0\).
These are identities of actual group paths, using the already established edge words, and hence also identities in homology.

Orient the main knot. At an odd leaf let \(t_0,t_1\in\{1,-1\}\) record whether it follows the canonical arcs \(0\to2\), \(1\to3\) or their reverses. By the endpoint convention in Section 2,
\[
                        [\mu_0]=t_0[\mu_K],\qquad
                        [\mu_1]=-t_1[\mu_K].
\tag{33}
\]
The first row of (32), traversed with these signs, contributes
\[
              -t_0t_1[\mu_K]+(t_0-t_1)[M_+]
\tag{34}
\]
to the longitudinal homology. The second contributes
\[
               t_0t_1[\mu_K]+(t_0-t_1)[M_-].
\tag{35}
\]
The same coefficient \(t_0-t_1\) is the oriented intersection of the main strands with the original crossing disk. Thus it is their linking number with the circle.

The main-meridian coefficients in (34)–(35) are exactly the oriented writhe contributions. To check the convention, undo the literal quarter-turn \(h=T(R^\epsilon)\). Parallel upward strands of the unturned positive braid become \(t_0=1,t_1=-1\): one diagonal is reversed by this quarter-turn. Hence the positive crossing has sign \(-t_0t_1\), and the negative crossing has sign \(t_0t_1\). Reversing just one strand reverses both signs. This is the usual oriented crossing definition, applied to the actual ordered terminal map.

For a pure leaf its auxiliary meridian is \(M_0=S^{-1}\). Its two paths are \(M_0,M_0^{-1}\), so their homology contributes only \((t_0-t_1)[M_0]\), and no main-meridian term. Products and turns outside the leaf boxes are actual crossing-free identity strips and rotations. They do not introduce an additional homology contribution. Thus the full path from (30) has
\[
          [L_{\mathrm{path}}]
          =w_\epsilon[\mu_K]+\sum_i\ell_i[\mu_i].
\tag{36}
\]
It traverses the main knot once because every original segment and disk puncture is followed once in its actual oriented component. Therefore it differs from the preferred augmented longitude by exactly \(w_\epsilon\) main meridians:
\[
        \lambda_K=L_{\mathrm{path}}\mu_K^{-w_\epsilon},\qquad
        \tau_{\lambda_K}
          =2i\sum_e\cot(\pi x_e)-\sum_i\epsilon_i-w_\epsilon.
\tag{37}
\]
This step determines the integer part; parabolicity alone would not do so.

## 7. Actual auxiliary fillings and the preferred remaining longitude

The original crossing circles are pairwise unlinked: their disk boxes are disjoint, and no circle threads another. In the first homology of the augmented exterior,
\[
 [\lambda_i]=\ell_i[\mu_K],\qquad
 [\lambda_K]=\sum_i\ell_i[\mu_i].
\tag{38}
\]
Here \(\lambda_i\) is the primitive disk longitude used in (1). Filling kills the slope \(\mu_i+p_i\lambda_i\), so
\[
 [\mu_i]=-p_i\ell_i[\mu_K],\qquad
 [\lambda_K]=-\sum_i p_i\ell_i^2[\mu_K]
\tag{39}
\]
in the filled knot exterior. The original main meridian remains primitive. The image of \(\lambda_K\) still traverses the main knot once. Its preferred zero-linking correction is therefore
\[
                  \lambda_{\mathrm{fill}}
            =\lambda_K\mu_K^{\sum_i p_i\ell_i^2}.
\tag{40}
\]
The two peripheral elements commute, so their unit-meridian translations add. Equations (37) and (40) prove (2), including its surgery sign.

![Two fundamental parallelograms on the filled cusp: the image of the augmented longitude and its preferred correction by four meridians.](../book/figures/main-cusp-longitude-shear.svg)

The figure uses one filling with \(p=1\) and \(\ell=\pm2\), so \(c=4\). Both parallelograms belong to the same filled cusp lattice; \(\lambda_{\mathrm{aug}}\) denotes the image of \(\lambda_K\) on that cusp.

Finally let \(o_i=1\) for parallel original strands in the unturned braid box and \(o_i=-1\) for antiparallel strands. Equations (34)–(35) give
\[
 \ell_i^2=2(1+o_i),\qquad
 w_\epsilon=\sum_i o_i\epsilon_i,\qquad
 w_{\mathbf n}=\sum_i o_i n_i.
\tag{41}
\]
Use \(n_i=\epsilon_i-2p_i\) to obtain
\[
 -\sum_i\epsilon_i-w_\epsilon+\sum_i p_i\ell_i^2
 =-\sum_i(1+o_i)(\epsilon_i-2p_i)
 =-\sum_i n_i-w_{\mathbf n}.
\tag{42}
\]
This proves (3) and matches the separately derived exact scalar exponent. No cancellation of a carrier or framing factor has been assumed to identify the cusp.

## 8. Scope and analytic continuation

The proof uses only the original ordered face maps, actual cusp paths, and homology of the specified disk fillings. It holds for the full small auxiliary deformation furnished by the marked geometric theorem, including arbitrary strict product/turn syntax and arbitrary retained half-twist patterns whose main strands form a knot. The calculation uses no analytic source-growth assumption. The general source theorem now has the same strict-tree scope under its separate long-twist hypotheses.

On a sufficiently long filled branch the representation is the actual complete hyperbolic knot holonomy by the existing marked metric completion. Substituting its original critical wire values gives the geometric cusp shape in (2). This is not an identification made from the volume asymptotic, nor a claim that the polynomial annihilator is the knot A-polynomial.

For multiple main components the additive calculation tracks each component with its own meridian orientation, but their mutual linking and surgery change require a matrix of preferred-longitude corrections. The statement above deliberately assumes one main knot component.


## 9. The first quantum correction in the established moving class

The geometry above and the [filled meridian-profile theorem](actual_main_meridian_filled_volume.md) apply to every fixed strict Conway construction under the stated knot, marking and long-twist hypotheses. The [general component comparison](actual_main_meridian_general_component_comparison.md) removes the former adjacency, valence and path restrictions from the analytic theorem.

Fix such a strict presentation and its original knot and parity pattern. In the strict two-leaf knot case, retain the linked theorem’s pure-leaf qualification. Fix independently sufficiently long signed integers \(n_i=\epsilon_i-2p_i\), with no bound on their ratios. The source-dependent lower threshold is chosen once and is independent of the later radius \(R<1\). The presentation and the integers are fixed before the level \(N\) tends to infinity.

Let \(F_N(M)\) be its actual zero-framed reduced ADO invariant, with unknot value one and the marked coordinate \(M=q_N^s\), \(q_N=e^{\pi i/N}\). Its complete value \(F_N(1)\) is the reduced Kashaev invariant. The filled-profile theorem gives, uniformly on every fixed \(|s|\le R<1\),
\[
 \frac{F_N(q_N^s)}{F_N(1)A_N(s)H_N(s)}
 =1-\frac{\pi s^2}{N}\sum_e\cot(\pi x_e^{\mathrm{fill}})
                  +O_{\mathbf n,R}(N^{-2}),
 \qquad H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)}.
 \tag{44}
\]
The [exact scalar calculation](actual_main_meridian_exact_scalar.md) independently proves
\[
              A_N(s)=q_N^{A s^2/2},\qquad
              A=-w_{\mathbf n}-\sum_i n_i.
 \tag{45}
\]
It retains the full crossing, the prescribed changes of tensor order, the reduced closing trace and the zero-framing correction. In particular it does not discard a carrier or a linear Cartan term by assumption. That scalar proof is separate from the geometric argument above.

Now set \(z=2\pi i s\). Then \(M=e^{z/(2N)}\), and define
\[
             \mathcal H_N(z)=
             \frac{\sinh(z/2)}{N\sinh(z/(2N))},
             \qquad \mathcal H_N(0)=1.
\]
Expanding the explicit exponential in (45), and using the geometric identity (2)–(3), yields
\[
 \boxed{\displaystyle
 \frac{F_N(e^{z/(2N)})}{F_N(1)\mathcal H_N(z)}
   =1+\frac{\tau_{\mathrm{main}}z^2}{8\pi iN}
                       +O_{\mathbf n,R}(N^{-2}),
 \qquad |z|\le2\pi R,\quad R<1.}
 \tag{46}
\]
The shape here is the preferred cusp shape of the actual filled knot complement. All crossing circles have been filled; the main knot cusp remains unfilled. The correction is evaluated at the filled geometric branch, not the complete augmented optimizer. Both level parities are included, and uniform holomorphy gives the corresponding fixed derivative statements on smaller disks. In particular,
\[
 N\left.\frac{d^2}{dz^2}
      \frac{F_N(e^{z/(2N)})}{F_N(1)\mathcal H_N(z)}
   \right|_{z=0}
                  \longrightarrow\frac{\tau_{\mathrm{main}}}{4\pi i}.
 \tag{47}
\]

For the full modified-trace ADO invariant, the modified-dimension ratio is exactly \(1/\mathcal H_N(z)\). Its complete-normalized profile is therefore the left side of (46), with the same correction. The reduced invariant retains \(\mathcal H_N\). Neither statement crosses the first ordinary-color resonances \(z=\pm2\pi i\).

The implication uses the moving asymptotic and the independent geometric translation identity proved above. The geometric proof determines the actual preferred cusp; the analytic proof determines the quantum correction. Neither statement identifies a classical factor of a quantum annihilator.

## 10. Exact finite reproduction

The [symbolic reproduction script](../experiments/audit_main_meridian_preferred_cusp.py) checks 75 local identities. It constructs the meridian frames and the three-point maps of the prism directly, checks every product, turn and root translation, verifies the four odd path words, and checks the finite endpoint-orientation and filling-sign formulas. The [saved record](../experiments/main_meridian_preferred_cusp_results.json) lists the checks.

The matrix identities are exact rational identities in independent variables, not numerical samples of knots. They support the local calculations in the proof. They do not replace the global identification of the original face pairing, the single longitudinal traversal, the homology calculation, or the marked metric completion.

With Python and SymPy installed, run from the repository root:

```bash
python3 experiments/audit_main_meridian_preferred_cusp.py
```

The default output is written beside the script. Pass `--output PATH` to select another file. The script performs no network access and uses no private inputs.
