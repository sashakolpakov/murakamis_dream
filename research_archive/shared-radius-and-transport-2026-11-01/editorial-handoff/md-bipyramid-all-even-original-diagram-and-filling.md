# The original braid, packing and fillings of the opposite-offset bipyramid

This note concerns a fixed even integer \(m\ge6\). It identifies the original diagram and its complete packing for every \(m\), without inserting tangles. The quantum level is \(N\), and \(d=N-1\).

The topology is that of a closed three-strand braid with alternating generators. The exponents are the original signed crossing powers. This is an exact disk-labeled identification, not a deduction from component counts. The full long-filling volume consequence below uses the separately proved [all-even shared-radius theorem](md-bipyramid-all-even-shared-radius-family.md). All research in this note remains private.

## 1. The sphere and the theorem

Use poles \(N_0,S_0\), rim vertices \(v_0,\ldots,v_{m-1}\), and the oriented triangles
\[
 (N_0,v_j,v_{j+1}),\qquad(S_0,v_{j+1},v_j),
 \qquad j\in\mathbb Z/m.                                      \tag{1}
\]
Match north triangles across \(N_0v_j\) for odd \(j\), and south triangles across \(S_0v_j\) for even \(j\). Every triangle belongs to exactly one matched pair. This is a simple triangulated sphere with \(m\) matched pairs and \(m+2\) white vertices.

The cyclic quadrilateral order is \((x,b,y,c)\); the homogeneous source argument order is \((x,b,c,y)\). The original frames are
\[
\begin{array}{c|c|c}
 & (x,b,c,y)&\text{matching edge}\\ \hline
 j\text{ odd}&(N_0,v_{j-1},v_{j+1},v_j)&N_0v_j\\
 j\text{ even}&(S_0,v_{j+1},v_{j-1},v_j)&S_0v_j .
\end{array}                                                    \tag{2}
\]
The reversed south middle order is essential. Mark the unmatched edge \(v_0v_1\).

Retain a signed half twist \(\epsilon_j\in\{-1,0,1\}\) at each original crossing disk. In its primitive disk-framed basis, filling parameter \(p_j\in\mathbb Z\) inserts the power
\[
                         n_j=\epsilon_j-2p_j.                 \tag{3}
\]
Let the braid generators use the same positive crossing as \(R\), and write factors in the order encountered by the strands.

**Theorem.** The filled diagram is the ordinary closure of
\[
 \beta_m(\mathbf n)=
 \sigma_2^{n_0}\sigma_1^{n_1}\sigma_2^{n_2}\sigma_1^{n_3}
       \cdots\sigma_2^{n_{m-2}}\sigma_1^{n_{m-1}}.              \tag{4}
\]
The \(m\) crossing disks are the disks surrounding those syllables. The braid axis is not a link component. The main link is a knot exactly when the permutation of (4) is a 3-cycle. In particular, exactly one odd north exponent and one odd south exponent, with every other exponent even, gives a knot for every \(m\).

For each fixed \(m\), the shared-radius theorem and the established Morse filling theorems imply a finite \(B_m\) such that, whenever the fixed integers satisfy \(\min_j|n_j|>B_m\) and the knot test,
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|K_N(\widehat{\beta_m(\mathbf n)})|
  =\operatorname{Vol}(S^3\setminus\widehat{\beta_m(\mathbf n)}).
                                                                  \tag{5}
\]
Here \(K_N\) is the existing reduced enhanced Kashaev normalization. The signs and relative sizes of the fixed powers are unrestricted. There is no uniformity in growing \(m\), no growing-twist assertion, and no moving-color conclusion.

## 2. Exact strand maps and the three-strand braid

Number the sides of a cyclic quadrilateral by
\[
          0=xb,\quad1=by,\quad2=yc,\quad3=cx.                 \tag{6}
\]
These are the native cut corners \((C_1,C_2,C_3,C_0)\), respectively. The literal pure shaded map \(C_1\mapsto C_0,\ C_2\mapsto C_3\) gives main-strand pairs \((0,3),(1,2)\). Either signed odd half twist gives \((0,2),(1,3)\). The shaded grouping of corners is a different pairing and is not used to count main components.

Embed the sphere with \(N_0\) inside the equator and \(S_0\) outside. The outside strips are exactly these:

* the edge \(v_jv_{j+1}\) joins boxes \(j,j+1\);
* an unmatched north spoke, at even rim index \(j\), joins odd boxes \(j-1,j+1\);
* an unmatched south spoke, at odd rim index \(j\), joins even boxes \(j-1,j+1\).

Under the pure pairing they form three nested planar circles: north, equator, south. There are no other strips. Straighten these three circles into concentric tracks while retaining the disjoint disk neighborhoods. Increasing angular coordinate is braid time; label the tracks from inside to outside by \(1,2,3\).

The forward endpoints at each box are
\[
\begin{array}{c|c|c}
 &\text{input, inner then outer}
 &\text{output, inner then outer}\\ \hline
 j\text{ odd}
 &(N_0v_{j-1},v_{j-1}v_j)
 &(N_0v_{j+1},v_jv_{j+1})\\
 j\text{ even}
 &(v_{j-1}v_j,S_0v_{j-1})
 &(v_jv_{j+1},S_0v_{j+1}).
\end{array}                                                     \tag{7}
\]
North boxes therefore act on tracks \(1,2\); south boxes act on tracks \(2,3\). The unused track simply passes the box through its outside strip.

The north source frame already has increasing angular time and the inside track on its left. At a south box, both the time direction and the transverse order are reversed. Thus the change from its source frame to (7) is a planar half-turn. It is not a reflection or a one-head orientation reversal.

For a single crossing a planar half-turn preserves each diagonal pair of endpoints and therefore preserves which diagonal is over. It retains the signed crossing \(R\). For \(R^n\) the order of the identical signed crossings is reversed, and the exponent is still \(n\). Reversing both strand orientations also preserves crossing writhe. This is a literal tangle isotopy with the ribbon normal transported; it is not the assertion \(T^2=I\) for typed quantum turns.

Cut the annulus before box 0. Formula (7) gives (4) with no sign inversion at the south boxes. Closing the cut tracks gives the ordinary braid closure. The half-turn and straightening carry the original crossing circles and their disk collars along, so the identification preserves the designated twist regions rather than just the unmarked link.

Components of a braid closure are the cycles of its strand permutation. With one odd box of each kind the permutation is a product of the two distinct transpositions \((12),(23)\), hence a 3-cycle, in either order. All even exponents give three components. All odd exponents give
\[
                    \#\text{main components}=\gcd(3,m/2).       \tag{8}
\]
These statements hold for every \(m\) by (7), not by a finite experiment. More general parity patterns are tested exactly by the permutation of (4).

The phrase “alternating generators” does not assert an alternating link diagram. For example, assigning opposite signs to the two generator types gives the usual alternating braid pattern; arbitrary signs need not.

## 3. Complete packing and the marked curvatures

Put
\[
                         \theta=\pi/m,\qquad a=\csc\theta.       \tag{9}
\]
In the complex projection plane take the north disk \(|z|\le a-1\), the south **exterior** disk \(|z|\ge a+1\), and the unit disks
\[
                    v_j:\quad |z-ae^{2ij\theta}|\le1.           \tag{10}
\]
Every rim disk is tangent to both pole disks. Rim centers at cyclic separation \(r\) have distance \(2a\sin(r\theta)\), which is 2 exactly for adjacent indices and strictly greater than 2 for every nonadjacent pair. The two pole disks are disjoint. Thus the contact graph, with its exterior south region, is exactly (1); no extra edge is introduced.

The marked contact of \(v_0,v_1\) is
\[
                  p=a\cos\theta\,e^{i\theta}.
\]
Use the holomorphic Möbius transformation
\[
                              w=\frac{2}{z-p}.                 \tag{11}
\]
A further rotation or translation puts the two protected circles into horizontal strip position without changing radii.

Under \(z\mapsto1/(z-p)\), a circle of center \(c\) and radius \(r\) has new radius \(r/\bigl||c-p|^2-r^2\bigr|\). A zero denominator gives a line. For the north and south boundaries the denominators before taking absolute value are \(2(a-1)\) and \(-2(a+1)\). Both circles have inversion radius \(1/2\), and their oriented disks become bounded because \(p\) is outside both original disks. The factor 2 in (11) gives both new radii one.

For rim circle \(j\),
\[
\begin{split}
 |ae^{2ij\theta}-p|^2-1
 &=2a^2\cos\theta
       \{\cos\theta-\cos((2j-1)\theta)\}\\
 &=4a^2\cos\theta\sin(j\theta)\sin((j-1)\theta).
\end{split}
\]
It vanishes exactly at \(j=0,1\) and is positive elsewhere. Therefore the complete marked curvatures, meaning reciprocals of Euclidean circle radii, are
\[
 L_{N_0}=L_{S_0}=1,\qquad
 k_j=L_{v_j}
 =\frac{\cos\theta}{\sin^2\theta}
       \{\cos\theta-\cos((2j-1)\theta)\}.                       \tag{12}
\]
In particular,
\[
 k_0=k_1=0,\quad
 k_j>0\ (2\le j\le m-1),\quad
 k_2=k_{m-1}=4\cos^2\theta.                                    \tag{13}
\]
The two protected weights are exact zeros. They are never replaced by small positive curvatures.

The strip width is 2, since the radius-one north circle is tangent to both parallel lines. If another source convention uses width 1, a common rescaling multiplies all ordinary curvatures by 2. The action is unchanged by common scaling because total numerator degree equals total ordinary target. Formula (12) is the normalization with pole curvatures one.

## 4. The labeled hyperbolic polyhedron

The packing can be certified by an explicit convex right-angled ideal polyhedron, without assuming that equal volume identifies a link. Let
\[
\begin{split}
 h&=\tan(\theta/2),\qquad r=\sqrt{1-h^2},\\
 A_j&=(r\cos2j\theta,r\sin2j\theta,h),\\
 B_j&=(r\cos(2j+1)\theta,r\sin(2j+1)\theta,-h).
\end{split}                                                     \tag{14}
\]
Their Klein-ball convex hull is an ideal \(m\)-antiprism. In a rotated angular frame a side-face normal is
\[
 (c,\cos\theta,\sin\theta,b),\qquad
 b=\frac{r(1-\cos\theta)}{2h},\quad
 c=\frac{r(1+\cos\theta)}2.
\]
The adjacent top and lower-side normals are \((h,0,0,1)\) and \((c,1,0,-b)\). The Lorentz products vanish because
\(b-hc=0\) and \(\cos\theta-b^2-c^2=0\).
The normals are spacelike supporting normals of the stated convex hull. Rotations and top/bottom symmetry give every edge, so all dihedral angles are \(\pi/2\).

Double the antiprism across one polygonal face. Adjacent triangle pairs merge into white quadrilaterals, giving a convex right-angled ideal polyhedron \(Q_m\). Use the contact labels
\[
 Z_j=v_{j-1}\cap v_j,\qquad
 U_j^+=N_0\cap v_j,\qquad U_j^-=S_0\cap v_j .
\]
Its faces are
\[
\begin{array}{ll}
 W_{N_0}=(U_{m-1}^+,\ldots,U_0^+),&
 W_{S_0}=(U_0^-,\ldots,U_{m-1}^-),\\
 W_{v_j}=(Z_j,U_j^+,Z_{j+1},U_j^-),&\\
 T_j^+=(Z_j,U_{j-1}^+,U_j^+),&
 T_j^-=(Z_j,U_j^-,U_{j-1}^-).
\end{array}                                                       \tag{15}
\]
The \(W\)'s are white, the \(T\)'s shaded. The two pole white circles are coaxial, and rotational symmetry makes the rim circles congruent. Normalize the rim radius to one. Tangency to both pole circles forces their radii to be \(a-1,a+1\), and adjacent rim tangency forces \(a\sin\theta=1\). Thus this polyhedron certifies the same labeled packing (10).

The crossing-circle vertex at box \(j\) is \(U_j^+\) for odd \(j\), and \(U_j^-\) for even \(j\). The matching pairs are \(T_j^+,T_{j+1}^+\) and \(T_j^-,T_{j+1}^-\), respectively. The other \(2m\) ideal vertices are the original main strips.

Take two copies of \(Q_m\). White faces pair across the projection copies by their labels. Pure shaded triangles pair within each copy with the map of Section 2. An odd disk exchanges the copies and the punctures through its signed half-twist collar. Cutting the link of Section 2 along the projection sphere and its disjoint crossing half disks gives exactly these two balls: drilling a boundary-parallel crossing semicircle and opening its original half disk cancel the same local handle. The labeled face quotient therefore reconstructs the original augmented link in \(S^3\).

At every ideal vertex the link is a rectangle. Normalize its two shaded sides to length one; each shaded triangle map preserves its canonical horocycles, including the odd puncture exchange. Every alternating white/shaded edge cycle has four right angles, fixes both ideal endpoints and preserves their horospheres. Its dilation is zero and its rotation is \(2\pi\), so its whole holonomy is identity. The cusp links glue to the actual compact flat tori. This proves complete finite-volume hyperbolic geometry, not merely angle equations.

The construction and explicit volume calculation are those of [the right-angled antiprism proof](/Users/sasha/volume-conjecture/notes/actual_augmented_pretzel_geometric_volume.md), Sections 1–3, with the matching just specified. The resulting volume is
\[
 \operatorname{Vol}(Y_m^\epsilon)
 =2\operatorname{Vol}(Q_m)
 =8m\left[
 \Lambda\!\left(\frac\pi4+\frac{\pi}{2m}\right)
 +\Lambda\!\left(\frac\pi4-\frac{\pi}{2m}\right)\right].          \tag{16}
\]
Here \(\Lambda(t)=-\int_0^t\log|2\sin u|\,du\). To recall the calculation, cone the oriented antiprism boundary to an axis ideal point. The two polygonal contributions cancel. Each side pair gives shapes
\(z_+=\tfrac12+\tfrac i2t\) and \(z_-=\tfrac12-\tfrac i{2t}\), with
\(t=\tan(\pi/4-\theta/2)\).
Their signed Bloch–Wigner volumes sum to twice the bracket in (16), by the Lobachevsky duplication identity. There are \(m\) side pairs per antiprism and four antiprisms in the quotient.

The usual augmented pretzel pairs \(T_j^+\) with \(T_j^-\) at \(Z_j\), not the pairs above at \(U_j^\pm\). Consequently the common polyhedron and volume are not an identification of the two links. Their pure main-component counts are already different: \(m\) for that pretzel matching and 3 here.

## 5. Original finite source and complete action

Put \(q=e^{\pi i/N}\), \(d=N-1\). Let \(H_V(x,b,c,y;\sigma)\) be the original full homogeneous numerator for
\[
 V_N(\sigma;\Omega)
   =(2T_N(\sigma/2)+2)(\sigma-\Omega)^{-1}.                     \tag{17}
\]
Polynomial division defines this matrix polynomial at every root. Its spectral degree is at most \(d\); values and first derivatives at repeated nodes are retained.

Let \(A,B\) be the two pole face variables and \(z_j\) the rim face variables. With \(z_0=z_1=0\), the full spectral source is exactly
\[
\begin{split}
 S_N(\boldsymbol\sigma)
 ={}&[A^dB^d\prod_{j=2}^{m-1}z_j^d]\,
 \prod_{j\,\mathrm{odd}}H_V(A,z_{j-1},z_{j+1},z_j;\sigma_j)\\
 &\qquad\cdot
 \prod_{j\,\mathrm{even}}H_V(B,z_{j+1},z_{j-1},z_j;\sigma_j).
\end{split}                                                     \tag{18}
\]
The actual filled scalar is
\[
 Z_N(\mathbf n)
       =(\bigotimes_j\mathcal L_N^{n_j})S_N,                    \tag{19}
\]
where \(\mathcal L_N^n\) is the original full-Hermite functional for \(R^n\).

For completeness, the finite Morse compiler keeps each numerator
\(N^{-1}H_V/(bc)^{d/2}\).
The face-boundary turning equation is \(M_f-T_f=2\) on bounded faces and \(-2\) on the exterior, where \(M_f\) counts middle passages and \(T_f\) outside minus inside turns. The physical reduced mark replaces its cap by the factor \(N^{-1}(z_1/z_0)^d\) before cancellation. The remaining primitive face lattice has \(m+1\) independent \(N\)-point grids, canceling \(N^{-m-1}\). Endpoint support precedes root specialization. This proves (18) with no omitted power of \(N\), and does not replace the cyclic tensor network by a scalar edge model.

At even levels an explicit parity cochain is
\[
        t(v_j)=j\bmod2,\qquad t(N_0)=1,\qquad t(S_0)=0.          \tag{20}
\]
It agrees across matching spokes and differs across every strand edge. Thus the even coset is compatible with the protected mark and the same exact ordinary targets \(d\).

All these are the finite identities of [the matched-sphere source](/Users/sasha/volume-conjecture/notes/research_matched_sphere_morse_source.md), Sections 1–7, and [the uniform filling theorem](/Users/sasha/volume-conjecture/notes/actual_uniform_filling_supremum_bound.md), Section 1. Their hypotheses have been verified by the literal sphere and endpoint construction, rather than by a presumed flat-plat presentation.

Define the complete triangle rate for nonnegative weights, not all zero, by
\[
 Q(w)=
 \max_{\substack{\alpha_i\ge0\\\sum_i\alpha_i=1/2}}
 \left\{\frac1\pi\sum_i
 [\Lambda(\pi\alpha_i)+\Lambda(\pi/2-\pi\alpha_i)]
                   +\sum_i\alpha_i\log w_i\right\}.            \tag{21}
\]
At a zero weight restrict its load to zero. For at least two positive weights, the maximizer is
\(\alpha_i=\pi^{-1}\arctan(w_i/D)\),
\(D^2=w_1w_2+w_2w_3+w_3w_1\).
For one positive weight \(Q=\tfrac12\log w_i\).

For three tangent circles the center angle at circle \(i\) is \(2\arctan(w_i/D)\). Hence its complete star supplies total load one at each ordinary circle. This also holds at a protected-line limit; a circle tangent to both protected lines has the intervening center angle \(\pi\), which is the monomial load \(1/2\). Thus (12) solves every face stationarity equation. The ordinary graph after deletion of \(v_0,v_1\) is connected: both poles join the surviving rim path. The local positive Hessians leave only common scale, so the complete face saddle is nondegenerate on its quotient.

The source-normalized action is therefore
\[
 \Phi_m
 =2\sum_{j=0}^{m-1}Q(1,k_j,k_{j+1})
                -\sum_{j=2}^{m-1}\log k_j
 =\frac{\operatorname{Vol}(Y_m^\epsilon)}{2\pi}.                \tag{22}
\]
At stationarity the log-weight terms in (21) cancel the targets. The remaining calibrated triangle entropy is the positive cut volume. The exact source calibration is [the marked cofactor action](/Users/sasha/volume-conjecture/notes/actual_cross_cofactor_marked_action.md) and [the Morse geometric theorem](/Users/sasha/volume-conjecture/notes/actual_morse_geometric_contribution.md), Sections 2,4,6. Formula (16) is an independent closed expression for this actual geometric value; no arbitrary additive constant in \(Q\) is allowed.

## 6. Original primitive words and smooth filling

The two ordered input main meridians in a box are \(A_{\rm in},B_{\rm in}\). Its auxiliary longitude is the primitive based word
\[
                             P=B_{\rm in}A_{\rm in}.           \tag{23}
\]
The auxiliary meridian is the original disk-threading word, with its signed Hurwitz half-twist correction. The pure shaded map centralizes \(P\) and conjugates the full ordered input pair to the output pair. These based paths are carried along under the south half-turn of Section 2; they are not reconstructed from a symmetric trace formula.

Let \(\delta_j\) be the nearby angular spectral parameters. On the original complete branch the primitive squared-multiplier logs are
\[
 U_j=-\operatorname{Log}R_{0,j}
                    +2\pi i\epsilon_j\delta_j,\qquad
 V_j=-4\pi i\delta_j.                                          \tag{24}
\]
All logarithms vanish at the complete point. The exact collar matrices, including their nontrivial parabolic limits, are given in [the Morse geometric theorem](/Users/sasha/volume-conjecture/notes/actual_morse_geometric_contribution.md), equations (12)–(16). In particular the numerator \(C-I\) is not set to zero just because its eigenratio tends to one.

Those matrices assemble on this whole cyclic diagram. For a sequence of region labels the head is
\(\mathcal R_{F_i}^{+}\mathcal R_{F_{i-1}}^{-}\).
At each cup or cap the pattern \(F,G,F\) adds an ordered pair whose product is identity, so every later prefix survives unchanged. This proves the full based group relations at arbitrary Morse heights and at the cycles of the sphere. It is not a collection of unrelated local characters.

Let \(A_0(\delta)\) be the pure face-critical action with \(A_0(0)=\Phi_m\), and put
\[
\begin{split}
 A_\epsilon&=A_0+\pi i\sum_j\epsilon_j\delta_j^2,\\
 S_{\mathbf1}&=A_0+\pi i\sum_jn_j\delta_j^2
                               +2\pi i\sum_j\delta_j.
\end{split}                                                     \tag{25}
\]
Envelope differentiation of the original cofactor gives
\(dA_\epsilon=\sum_jU_j\,d\delta_j\). Hence the first unit-charge equations are exactly
\[
                           U_j+p_jV_j=-2\pi i.                \tag{26}
\]
At completeness
\[
 A_0''(0)=-2\operatorname{diag}(C_j),\quad
 C_j=\frac{\pi(T_{b_j}+T_{c_j})}{x_j+y_j}>0,\quad
 T_t=\sqrt{(x_j+y_j)t+x_jy_j}.                                 \tag{27}
\]
The outer pair of a matching edge is never the protected pair, and at least one of its triangles is nonmonomial. Thus (27) includes the boxes adjacent to the mark. The several-reciprocal-slope implicit-function theorem gives the selected point for independently long signed powers, with \(\delta_j=O_m(1/|n_j|)\).

The marked regulator equation, anchored at the actual complete cut, is
\[
 2\pi\operatorname{Re}A_\epsilon
 =\operatorname{Vol}(\rho)
             -\frac12\sum_j\operatorname{Im}U_j\operatorname{Re}V_j .
                                                                  \tag{28}
\]
Using \(V=-4\pi i\delta\) and (26),
\[
 \operatorname{Re}(-2\pi i p\delta^2+2\pi i\delta)
       =\frac{\operatorname{Im}U\operatorname{Re}V}{4\pi}.
\]
The boundary correction cancels, and
\[
                 2\pi\operatorname{Re}S_{\mathbf1}
                           =\operatorname{Vol}(\rho).         \tag{29}
\]

A metric completion is needed to turn (29) into a filled-complement identity. Its precise conditions hold here. The whole framed representation converges to the complete one as all powers become long. At the unit-charge critical point the actual equations give \(\operatorname{Im}\delta_j>0\) for either sign of \(n_j\). Thus
\(\operatorname{Re}V_j=4\pi\operatorname{Im}\delta_j>0\);
the longitude multiplier has nonunit modulus.

In the complete cusp frame, the second fixed point of that longitude escapes to infinity, while the developed two primitive generator paths remain bounded. Their logarithmic increments tend to zero and therefore equal the prescribed small \(U_j,V_j\), not those logs plus unknown multiples of \(2\pi i\). This comparison occurs before multiplication by \(p_j\). The invariant logarithmic metric is a complete flat torus with rank-two lattice. The primitive slope (26) has angle \(-2\pi\) and zero axial period; its complementary primitive period has nonzero real part. Adding the core axis is consequently a smooth solid torus with exactly that meridian. The main cusps remain complete.

The same finite boundary triangulation compares representation volume with this metric volume. The boundary homotopy to the axis-valued map has zero limiting volume, and the added filling tetrahedra have all vertices on the axis and zero volume. This is the completion and regulator argument in [the general metric theorem](/Users/sasha/volume-conjecture/notes/general_source_regulator_hyperbolic_equality.md), Sections 1–6, applied by the Morse theorem, Section 7.

Finally, the surgery along \(\mu_j+p_j\lambda_j\) in the original disk collar inserts \(-2p_j\) crossings. It recovers exactly (3)–(4) in \(S^3\). Therefore
\[
 2\pi\operatorname{Re}S_{\mathbf1}
       =\operatorname{Vol}(S^3\setminus\widehat{\beta_m(\mathbf n)})
                                                                  \tag{30}
\]
in the knot case. The target has not been changed to the untwisted parent or its isovolumetric pretzel partner.

## 7. Nonzero full-period contribution and restoration of the invariant

All geometric and graph hypotheses of [the Morse CROSS period theorem](/Users/sasha/volume-conjecture/notes/actual_morse_cross_filling_period.md) hold: connected ordinary graph, primitive face lattice of rank \(m-1\), a positive face Hessian modulo scale, and a nonmonomial triangle at every matching edge.

Let \(S_{N,\mathrm C}\) be the original all-CROSS projection of (18), selected by polynomial linearity. It is not a separate covariant tangle. Its entire original filling period has
\[
\begin{split}
 Z_{N,\mathrm C}={}&q^{d^2\sum_jn_j/4}(-2i)^m
                 \sqrt{2\pi}\,N^{m+1/2}\\
 &\quad\cdot
 \frac{\prod_j\sin(2\pi\delta_{N,\mathbf1,j})}
 {\sqrt{\det H_N(\delta_{N,\mathbf1})}\sqrt{\det Q_{N,\mathbf1}}}
 e^{N S_{N,\mathbf1}}
 \left(1+O_{\mathbf n}(N^{-1})
                  +O_{\mathbf n}(e^{-\kappa_{\mathbf n}N})\right).
\end{split}                                                     \tag{31}
\]
The notation is that theorem's finite face-critical action, finite first-charge point and face/spectral Hessians. Its determinant roots are the selected Gaussian branches. The coefficient is nonzero after removing the displayed powers and action. All charges, endpoint currents, odd simple-node data and double-node normals are already included; no first-charge cancellation is assumed away. The action tends to (30), and its rate approaches \(\Phi_m\) as all fixed powers become independently long.

To restore the full source, use the proved all-even shared-radius lemma. Define
\[
 a_*=\frac94,\quad \lambda=\frac{a_*}{k_2},\quad
 w_j=\lambda k_j,\quad L_{N_0}=L_{S_0}=1.
\]
Let \(W\) be this whole vector, \(W^{(1)}\) replace only \(w_2\) by 1, and \(W^{(0)}\) replace only \(w_{m-1}\) by 1. With literal arguments \((x,b,c,y)\), put
\[
\begin{split}
 X&=Q(x,b,y)+Q(x,c,y),\\
 H&=\max(X,\{\log b:b>0\},\{\log c:c>0\}),\\
 A_L&=\max(\log c,Q(x,b,y)+\tfrac12\log c)\quad(c>0),\\
 A_R&=\max(\log b,Q(x,c,y)+\tfrac12\log b)\quad(b>0).
\end{split}                                                     \tag{32}
\]
A protected overloaded middle gives no surviving anchor. For anchors \(1L,0L\) use \(W^{(1)},W^{(0)}\), respectively; use \(W\) at all others. The all-even lemma proves
\[
 A_{j,s}+\sum_{i\ne j}H_i-\sum_{\mathrm{ordinary}\ f}\log L_f
                           <\Phi_m-\frac7{100}.              \tag{33}
\]
Every occurrence of a shared variable is retained. The only size-dependent numbers are the explicit trigonometric \(k_j\). The proof bounds the whole scaling cost by
\(16/9-1+\log(9/16)\), then uses uniform adjacent-ratio bounds and the two three-box boundary corrections. Its fixed constant enclosures are independent of \(m\).

For any \(0<\eta<7/100\), the weighted real-spectral source bounds and the Cauchy coefficient estimate applied to these whole vectors give
\[
 \|S_N-S_{N,\mathrm C}\|_{[-2,2]^m}
          \le \exp\{N(\Phi_m-\eta)+o_m(N)\}.                   \tag{34}
\]
Each non-CROSS sector has a surviving anchor or is zero; there are finitely many sectors for fixed \(m\). The exact target \(d/N\) differs from 1 by \(1/N\), costing \(O_m(1/N)\) at the fixed positive ordinary weights.

The uniform filling theorem gives
\[
 |(\bigotimes_j\mathcal L_N^{n_j})(S_N-S_{N,\mathrm C})|
 \le\prod_j(1+|n_j|/2)\,
                       \|S_N-S_{N,\mathrm C}\|_{[-2,2]^m}.   \tag{35}
\]
The product-node-vanishing version is stronger, but unnecessary here. For fixed powers the constant is independent of \(N\). All repeated-root normals remain.

Choose the threshold so the geometric rate drop from \(\Phi_m\) is below \(\eta/2\), and so the original analytic and metric filling theorems apply. Equations (34)–(35) are then exponentially smaller than the nonzero term (31). The full invariant has its rate, proving (5). The complete-color zero-framing character has modulus one. The stated full one-cut modified normalization additionally carries \(i^{N+3}/N\), also of zero logarithmic rate. There is no extra \(N^m\) in (19).

Taking the maximum over the finitely many retained half-twist patterns gives \(B_m\) for all knot-producing parity patterns. This does not produce a threshold uniform in \(m\).

## 8. Precise comparison with Conway coverage

The collapsed twist graph of this displayed diagram is
\[
 G_m=C_m^2,\qquad
 E(G_m)=\{\{j,j+1\},\{j,j+2\}:j\in\mathbb Z/m\}.                \tag{36}
\]
Equatorial strips give the distance-one edges; north and south strips give the distance-two edges. This is the \(m/2\)-antiprism graph.

Every vertex subset whose size and complementary size are at least two has edge boundary at least six. To prove this, write its indicator around the cycle and let \(r\) be its number of runs. Distance-one edges give \(2r\). If \(r\ge3\), this suffices. If \(r=1\), both runs have length at least two, giving four distance-two boundary edges as well as the two distance-one edges. If \(r=2\), the first contribution is four. Zero distance-two boundary would make the indicator 2-periodic, hence alternating, which would have \(r=m/2\ge3\). A nonzero distance-two boundary has even size and is therefore at least two.

Consequently no Conway circle lying outside the designated boxes and separating at least two boxes on each side meets only four outside strands. A binary two-string expression with at least four atomic boxes has an internal partition with at least two atoms on each side, and its defining diagram exhibits that four-ended tangle cut. Thus the displayed disk-labeled diagram is not already a literal Conway operation tree on these boxes.

This is a diagrammatic statement. It does not exclude an isotopy to another Conway presentation, a nonvisible Conway sphere, regrouped twist parameters, or cancellations after a change of presentation. The [strict-tree theorem](/Users/sasha/volume-conjecture/notes/actual_conway_all_strict_tree_long_twist_volume.md) requires an actual two-string expression and its strictness test. The [net-twist theorem](/Users/sasha/volume-conjecture/notes/actual_conway_net_twist_volume.md) and [closure reduction](/Users/sasha/volume-conjecture/notes/actual_conway_arbitrary_closure_volume.md) also start from such an expression. They are not classifications of all closed three-strand braids.

No uniform alternative expression is proved here, so those theorems cannot simply be invoked from the braid name. Conversely, this note does not prove that its knot types are disjoint from the earlier classes, and makes no novelty claim on that basis.

The standard closed-three-braid setting is treated, for example, in Birman–Menasco's [A note on closed 3-braids](https://arxiv.org/abs/0802.1072). The identification (4) here follows from the literal endpoint and overpass maps (6)–(7), not a knot table. A separate intrinsic classification is needed to decide exactly which exponent tuples also have covered strict Conway presentations.

## 9. Dependencies and what has been added

The geometric source inputs used above are the already established finite matched-sphere source, positive face-action calibration, Morse whole-period asymptotic, primitive metric completion and finite Hermite norm bound. Their scopes are checked in Sections 4–7. The new all-size identifications are:

1. the annular endpoint table (7), with its south half-turn and unchanged exponent;
2. the literal primitive-disk correspondence between the matched sphere and the braid;
3. the explicit packing and marked inversion (9)–(13);
4. the matching distinction in the common antiprism polyhedron (15);
5. the nontrivial four-ended cut obstruction (36) for this displayed diagram.

The all-even shared-radius inequalities are a separate complete proof, preserved alongside this note. No private conclusion here is a public manuscript claim until it is independently reviewed.

