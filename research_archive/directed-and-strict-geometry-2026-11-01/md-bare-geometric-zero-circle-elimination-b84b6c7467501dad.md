# Zero-power circles at bare Conway junctions

This private note separates three statements. A zero-power crossing circle can be inserted at a bare product junction and removed by its meridian filling without changing the ordered tangle. Its angular variable can be eliminated exactly from the classical action. The remaining geometric comparison is a comparison of full face and boundary-group maps at the original complete representation; a stationary value alone does not establish it.

The authoritative inputs are the marked mask construction in
\`notes/actual_conway_general_mask_marked_filling.md\`, the full-circle representation in
\`notes/actual_all_circle_geometric_characteristic.md\`, the complete physical-edge theorem in
\`notes/actual_main_meridian_component_pressure.md\`, the regular-window statement in
\`notes/actual_main_meridian_general_component_comparison.md\`, and the filtered action in
\`notes/actual_main_meridian_filtered_characteristic.md\`.
No public source is changed.

## 1. The literal insertion

Use the reduced tree of original product junctions, with consecutive unturned products already grouped. A bare vertex has full valence at least three. Its incident edges are the original quarter-turns; a binary resolution used to describe its positive kernel does not add physical edges.

At a bare vertex insert the literal unturned coupon \(R^0=I\), at the distinguished position immediately before the original ordered child product. Encircle its two strands by a new crossing circle. Keep every child in its original order. Put
\[
 \epsilon_v=p_v=n_v=0
 \tag{1}
\]
at this new circle. Filling its original primitive meridian removes the auxiliary circle and restores the literal identity coupon. Thus the filled tangle, its endpoints, its framed main strands and its original peripheral curves are unchanged. No new quarter-turn is inserted. Repeating the operation at all bare vertices produces a literal all-circle tree on the same physical edge set.

This is an ordinary local meridian filling, not the assertion that an exponentiated peripheral equation suffices. For a representation the added meridian must be the identity matrix projectively. The noncentral longitude criterion below verifies this separately.

The original crossing powers, writhe and integer
\[
 a(D)=-w(D)-\sum_v n_v.
 \tag{2}
\]
are unchanged. The added circles have filling parameter zero, so their preferred-longitude surgery correction \(p_v\ell_v^2\) also vanishes.

## 2. A unique regular zero-power angular saddle

Let a bare hub have \(D\ge3\) incident covariant labels \(x_1,\ldots,x_D\), with
\[
 0<x_j\le\tfrac12,\qquad
 \#\{j:x_j=\tfrac12\}\le1,\qquad
                         \sum_jx_j>1.
 \tag{3}
\]
These conditions hold at the original complete strict optimizer. All physical labels are strictly below half except for the internal edge of the two-trivalent-hub component; that exception supplies at most one half label to either hub. Strict whole-hub support gives the final inequality. Hidden resolution labels are not included in (3).

Use the circle-incidence action
\[
 b(x,\tau)=\int_0^x
       \log(2\cos(2\pi r)+2\cos\tau)\,dr-2J(x),
 \qquad J'(x)=\log(2\sin\pi x).
 \tag{4}
\]
For \(\tau=-iy\), \(y>0\), every logarithm in the integral is real and finite. Put \(k=\tanh(y/2)\). Direct integration gives
\[
 b_\tau(x,-iy)=\frac{i}{\pi}
             \arctan\bigl(k\tan(\pi x)\bigr),
 \quad 0<x<\tfrac12,
 \tag{5}
\]
with value \(i/2\) at \(x=1/2\). Indeed
\[
 \int_0^x\frac{\sinh y}{\cosh y+\cos2\pi r}\,dr
   =\frac1\pi\arctan\bigl(k\tan\pi x\bigr).
\]
The zero-power first-charge equation is therefore
\[
 \sum_jb_\tau(x_j,\tau)-i=0
 \quad\Longleftrightarrow\quad
 \sum_j\arctan(k\tan\pi x_j)=\pi.
 \tag{6}
\]
A half label contributes \(\pi/2\). The left side is strictly increasing for \(0<k<1\), starts at zero or \(\pi/2\), and tends to \(\pi\sum_jx_j>\pi\). Thus (6) has exactly one solution \(0<k<1\). Consequently
\[
 y=2\operatorname{arctanh}k>0,\qquad
 Q=e^{i\tau}=e^y=\frac{1+k}{1-k}>1.
 \tag{7}
\]
At least two labels are strictly below half. Differentiating (6) shows that its derivative is strictly positive, so the angular Hessian is nonzero. The saddle and its selected logarithms extend holomorphically to a complex neighborhood of the fixed label tuple. The half-label case causes no singularity: the integrand of (4) remains nonzero at \(y>0\), and (6)'s derivative still has the contributions of the other labels.

In particular the new auxiliary longitude has distinct eigenvalues. If its meridian has similarity one and commutes with that longitude, it is projectively identity. The possible unipotent ambiguity at \(Q^2=1\) is absent.

## 3. Exact elimination of the angular action

Let \(V_D(\mathbf x)\) be the complete positive whole-hub action: resolve the original ordered product by any fixed binary association, sum its cubic gate actions, and optimize the hidden complementary labels. The conditional optimizer is strict and has negative definite Hessian on the strict whole-hub support.

Then on (3),
\[
 V_D(\mathbf x)=
 \underset{\tau}{\operatorname{stat}}
       \left\{\sum_jb(x_j,\tau)-i\tau\right\},
 \qquad \tau=-iy \text{ from (6)}.
 \tag{8}
\]
The equality includes its constant.

Here is one derivation retaining the exact complete normalization. For a low complete Newton factor the Laurent coefficient rate is
\[
 B_x(r)=J(2x)-2J(x)-J(x+r)-J(x-r),\qquad |r|\le x.
 \tag{9}
\]
The complete trace of a product has first Fourier charge one with coefficient exactly one. Its higher charges have strictly smaller rate; this follows from strict concavity of the positive coefficient convolution, or directly from the regular bare-trace theorem. The same exact complete trace is the positive binary-resolution sum. Therefore its rate is both \(V_D(\mathbf x)\) and
\[
 \max_{\substack{\sum_jr_j=1\\ |r_j|\le x_j}}
                               \sum_jB_{x_j}(r_j).
 \tag{10}
\]
This comparison uses only the exact local Frobenius trace, not a global quantum-volume theorem.

For \(0<x<1/2\),
\[
 B_x'(r)=\log\frac{\sin\pi(x-r)}{\sin\pi(x+r)}.
\]
The unique maximizer of \(B_x(r)+yr\) is
\[
 r=\frac1\pi\arctan\bigl(\tanh(y/2)\tan\pi x\bigr).
 \tag{11}
\]
Moreover
\[
 b(x,-iy)=\max_{|r|\le x}\{B_x(r)+yr\}.
 \tag{12}
\]
To verify the constant, at \(y=0\) both sides are
\(J(2x)-4J(x)\). Their \(y\)-derivatives are the same \(r\) by (5) and (11). The constrained maximizer (10) has common multiplier \(y>0\), determined by \(\sum r_j=1\). Equations (10)--(12) prove (8). A half label follows by continuity. Equivalently \(B_{1/2}(r)=0\), so its tilted maximum is \(y/2\), as also follows directly from (4).

For a cubic vertex one can avoid the finite trace altogether. The old action is
\[
 t(x_1,x_2,x_3)=
 \sum_{i<j}J(x_i+x_j)-\sum_iJ(x_i)-J(x_1+x_2+x_3-1).
 \tag{13}
\]
Writing \(a_j=\tan\pi x_j\), equation (6) gives
\(k^2=(a_1+a_2+a_3)/(a_1a_2a_3)\).
The derivative of the right side of (8) in \(x_j\) is
\[
 \log\frac{\cosh y+\cos2\pi x_j}{2\sin^2\pi x_j}
   =\log\frac{k^2+\cot^2\pi x_j}{1-k^2},
 \tag{14}
\]
which is exactly \(\partial_jt\). As \(\sum x_j\downarrow1\), \(y\to\infty\), and both actions tend to \(-2\sum_jJ(x_j)\). This proves the cubic identity with its absolute constant.

Both sides of (8) are holomorphic near the fixed strict tuple. Their equality on an open real set proves equality of the continued germs. At the possible half label, use their holomorphic continuation from labels below half; both Hessians remain invertible there.

## 4. The actual added longitude in the old prism geometry

The previous section identifies actions. The following independent matrix calculation identifies the candidate new circle inside the original marked geometry.

In an ordinary output port of the bare product write
\[
 E=e^{2\pi ib},\qquad R=\frac1{1+\kappa},\qquad
 \kappa=e^{-f'(b)}.
\]
The old universal white maps are
\[
 W_1=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\qquad
 W_3=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
 \tag{15}
\]
They are the actual top and bottom white-face maps at an unmasked bare product. Through every original binary product, the full matrix identities give
\[
 W_{F,1}=W_{G,1}=W_{o,1},\qquad
 W_{F,3}=W_{G,3}=W_{o,3}
 \tag{16}
\]
in the original world frame. Consequently the same ordered side word is seen at every port of that hub.

Insert the zero coupon in the original disk frame. Its primitive disk-longitude path crosses these two white sides, giving \(W_1^{-1}W_3\), up to the inversion required when the circle's orientation is reversed. The determinant-one normalization is
\[
 P=\frac1R W_1^{-1}W_3,\qquad
 \operatorname{tr}P
   =2-\frac{4\sin^2\pi b}{R}.
 \tag{17}
\]
This is the same \(W_1^{-1}W_3\) disk word used at the corresponding end of an all-circle edge; it is not a trace chosen to fit (6).

The old response metric is
\[
 X_{\mathrm{met}}^2=\frac{1+\cot^2\pi b}{1+\kappa}.
\]
Therefore
\[
                 \operatorname{tr}P=2-\frac4{X_{\mathrm{met}}^2}.
 \tag{18}
\]
At a boundary incidence with covariant label \(x\), the ordinary output is \(b=1-x\), and the conditional action satisfies \(f'(b)=-\partial_xV_D\). Using (14), valid at any valence by the envelope identity (8), gives
\[
 X_{\mathrm{met}}^2
 =\frac1{\sin^2\pi x\,[1+\exp(\partial_xV_D)]}
 =\operatorname{sech}^2(y/2)=1-k^2.
 \tag{19}
\]
Thus
\[
             \operatorname{tr}P=-2\cosh y=-(Q+Q^{-1}).
 \tag{20}
\]
This proves that the actual added longitude has the regular eigenvalues required by the angular saddle. The proof retains the old group word, and shows why a bare hub has a common \(Q\) across all its pages.

When an incidence is viewed through its physical turn, the old identity
\(T W_{j+1}(E,R)=W_j(E^{-1},1-R)T\)
takes the \(W_1^{-1}W_3\) word to the appropriate inverse of the \(W_2^{-1}W_0\) word. Its trace is unchanged. The auxiliary flag may be selected on the eigenvalue \(-Q\), \(Q>1\); the main meridian flags are not changed by this auxiliary choice.

## 5. What the edge equations see at the complete bare representation

Pull the original complete holonomy back along the exact filling quotient obtained in section 1. This gives a representation of the enlarged augmented link with every newly added meridian equal to identity. It is a representation-theoretic pullback; no assertion that the drilled link carries this metric is needed.

### The marked zero-coupon collar

Choose the coupon in a framed ball \(D^2\times[0,1]\), with its two strands
\(\{p_1,p_2\}\times[0,1]\). Choose a basepoint \(z_*\in\partial D^2\),
an ordered pair of disjoint access paths from it to small circles around
\(p_1,p_2\), and transport that entire system by the product framing.
Orient and name the resulting based puncture loops \(a,b\) so that
the oriented disk-boundary word is \(ba\). The boundary basepath is
\(\{z_*\}\times[0,1]\). Transport across this literal zero coupon gives
\[
                        a_{\mathrm{out}}=a_{\mathrm{in}},\qquad
                        b_{\mathrm{out}}=b_{\mathrm{in}}.
 \tag{22c}
\]
These are equalities in the based fundamental group, before taking any
representation. No permutation of punctures, turn of an access path,
or power of the disk-boundary curve is included.

Place the new auxiliary circle at the disk boundary in the middle
of this collar, with the original disk framing. Its longitude is
the parallel copy of that boundary and retains the based word \(ba\).
The meridian filling deletes the auxiliary circle and returns exactly
the framed collar just described. Its quotient on fundamental groups
fixes \(a,b\), their access paths, and the boundary basepath. Thus it
also fixes the ordered maps by which this collar is joined to all
earlier and later product factors. This remains true when there are
several child factors: transport the same system through them in
their recorded order. It never requires the factors to commute.

For comparison with a pair of projection faces, transport the framed
loops to the face basepoints along the original specified paths.
If the old transport is \(C_0\), (22c) becomes the simultaneous
conjugacy \(C_0aC_0^{-1}=a'\), \(C_0bC_0^{-1}=b'\).
Reading the other side of a puncture changes the corresponding
native generator to its inverse. Those inversions are recorded
explicitly in (22b) below; they do not change (22c) into a braid.
This is the marked van Kampen statement used at every added seam.
Only a retained nonzero half twist changes (22c), by the separately
calibrated Hurwitz action.

On a physical turn edge use the original ordered port coordinate \((0,\infty,1,R)\) and its phase \(E=e^{2\pi ix}\). At \(M=1\) the four native all-circle white matrices are exactly the universal old \(W_j(E,R)\), projectively. This follows by putting \(m=1\) in the explicit native chart, without specializing the auxiliary eigenvalues to one.

The two disk words have normalized traces \(-\beta,-\gamma\), where
\[
 \beta=\frac{2R-(E+E^{-1})}{1-R},\qquad
 \gamma=\frac{2-(E+E^{-1})-2R}{R}.
 \tag{21}
\]
At an inserted hub these are supplied by (20); at an original circle they are its original marked longitude trace. Eliminating \(R\) yields
\[
 A=\frac{4-\beta\gamma}{\beta+\gamma+4},
 \qquad A=E+E^{-1},
 \tag{22}
\]
which is exactly the all-circle edge equation at \(M=1\). Thus the old phase is one of its two reciprocal roots. The native white maps retain \(E\) itself, not just \(E+E^{-1}\); the existing native/character comparison identifies the all-circle source variable with that \(E\).

All character-chart denominators are units at this point: \(\beta,\gamma\ge2\), \(E\ne1\), and the displayed original port vertices are distinct. The allowed value \(E=-1\) on the two-hub half edge does not cause a character-matrix singularity. In that case the edge quadratic may ramify over its endpoint parameters; one must use the full stationary branch or another local coordinate, not assert that \(E\) is a simple quadratic root.

Here is the boundary-group comparison, including the tuple that has to be retained. First choose the normalized native matrix representatives for the four old projective white maps. In terms of the raw universal representatives used in (15), their scalar factors are respectively
\[
                E^{-1},\quad E^{-1},\quad
                [E(1-R)]^{-1},\quad (ER)^{-1}.
 \tag{22d}
\]
Each normalized matrix has determinant \(E^{-1}\) at \(M=1\).
The raw universal representatives do not all have that determinant:
in particular the factors involving \(R\) and \(1-R\) cannot be
discarded when taking an SL trace. With \(W_j\) now denoting these
normalized native representatives, put in each original edge frame
\[
 N_j=W_{j-1}^{-1}W_j,\qquad
 (A,B,C,D)=(N_3,N_0,N_1,N_2)
 \tag{22a}
\]
with the subsequent determinant-one puncture normalizations from the
all-circle chart. These subsequent powers of \(M\), not the scalar
factors in (22d), are one at \(M=1\). Thus every \(N_j\) has determinant
one and trace two. The actual page table is
\[
\begin{array}{c|c|c|c}
\text{end}&(a,b)&(a',b')&ba=b'a'\\ \hline
v&(B,A)&(C^{-1},D^{-1})&AB\\
w&(B^{-1},C^{-1})&(A,D)&(BC)^{-1}.
\end{array}
\tag{22b}
\]
The entries refer to paths, with the inverse on each puncture determined by its side of the disk. They are exactly the table of the literal all-circle cut, not a new identification of equal traces.

To apply that table to the old holonomy, first insert the zero coupon in the actual diagram, before assigning matrices. The main strands and their ordered endpoint paths are unchanged. Add the new circle and perform the literal projection/disk cut. The filling quotient takes every old main meridian and its old basepath to itself and kills the new circle meridian. In particular the four small corner paths reduce to the original consecutive-white words in (22a). A white face split by the added cut retains the same transport on both of its pieces: crossing the extra cut and returning differs by the new meridian, whose image is identity. This is also the full-map invariant (16) through every prism of the original product. Thus the developed four white transitions of the pulled-back representation are exactly the four \(W_j\) already compared above.

The paths across the added disk pages are still the paths of this cut. By van Kampen they intertwine both generators in the appropriate row of (22b), with precisely the displayed inversions; the product column is their original primitive disk boundary. The inserted coupon has no crossing, so no Hurwitz exchange is made at its distinguished seam. The old retained half twists keep their original exchanges.

At \(M=1\), either input pair in (22b) is irreducible. Both punctures have trace two, and the products in the two rows have traces \(-\beta\) and \(-\gamma\), respectively, with \(\beta,\gamma\ge2\). Their irreducibility obstructions are \((\beta+2)^2\ne0\) and \((\gamma+2)^2\ne0\). Two intertwiners of either full ordered pair differ by its scalar centralizer. Therefore the pulled-back page transport equals the native pure transport in PGL. At an original odd seam the same argument is applied after the already calibrated full Hurwitz action. The corner flags on the main cusp are the old parabolic flags, and the extra auxiliary flags are chosen from (20); these choices do not alter a group generator.

All white and shaded generators of the cut now agree, in their original tree frames. This proves equality of the complete representations, not only of the local character triples or the main-cusp translation. It identifies the selected all-circle algebraic point with the pullback of the original bare-tree holonomy. The newly introduced ideal vertices need not form positive tetrahedra in this pulled-back representation. In particular an edge with \(E=-1\) can make that added subdivision flat. No metric on the enlarged unfilled exterior is asserted or required.

## 6. Stationary elimination at a nonparabolic main meridian

Let \(t\) be the actual main deformation parameter, \(M=e^{\pi it}\).
In the existing strict-tree filtered action it enters only through
\[
 \sum_{e\in\mathcal E_T}
       \{2J(x_e)-J(x_e+t)-J(x_e-t)\}
       +\frac{\pi i a(D)}2t^2.
 \tag{23}
\]
It does not enter the old bare tensor action or its hidden resolution wires.

The enlarged all-circle action replaces a bare hub by
\(\sum_jb(x_j,\tau_v)-i\tau_v\), with \(n_v=0\).
Eliminating \(\tau_v\) by (8) returns exactly the old whole-hub action, including its constant, for complex physical wires in the regular neighborhood. The edge set and (23) do not change, and neither does \(a(D)\). Hence the two full critical-value germs are equal after stationary elimination.

The new angular Hessian at each bare hub is nonzero. Its Schur complement is precisely the old conditional hub Hessian. Combining it with the original nondegenerate filled critical point shows that the enlarged joint critical point is nondegenerate. Its analytic branch therefore exists with all the original logarithms retained. Original sufficiently long fillings keep their auxiliary \(Q_v^2\ne1\); every added zero-power circle has \(Q_v^2\ne1\) by (7), and this persists near the complete branch.

By section 5 this branch reconstructs the original filled knot representation, rather than only an algebraic solution of the slope eigenvalue equations. Near the old augmented complete point the original auxiliary deformation is fixed by its primitive peripheral rows. Equality at completeness and the marked gluing/representation local inverse identify the two nearby deformations. The original sufficiently long filling point lies on that same small branch. There every original filled circle, as well as every added zero circle, has \(Q_v^2\ne1\); the filling words are projectively identity by section 2. The nondegenerate main-meridian branch is then the geometric germ of the original filled knot.

The all-circle squared longitude identity is a rational identity on its integral source variety. It extends to this regular representation, including the half-edge fold, without solving for an individual edge root. The added zero fillings contribute no surgery exponent, the Seifert sign is that of the same original complete knot, and stationary elimination leaves the effective longitude unchanged. Consequently the proposed extension is
\[
 L_{\mathrm{geom}}(M)
   =-M^{a(D)}
      \prod_{e\in\mathcal E_T}
                \frac{M^2-X_e(M)}{1-M^2X_e(M)}
 \tag{24}
\]
on the original strict-tree filled branch, with \(X_e=e^{2\pi ix_e}\).

The substantive comparison to be independently checked is the complete face-word argument in section 5, especially its zero-coupon cut and the two rows of (22b). It is now stated as a full argument, rather than replaced by a trace or phase match. No additional quantum growth theorem is used: the strict-tree source estimates are already available. No statement treats a similarity-one parabolic slope as trivial.

