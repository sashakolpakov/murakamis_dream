# Actual marked deformation and smooth filling for every strict Conway mask tree

31 October 2026. Internally reviewed geometric and local-source theorem.
This extends the [general strict-mask complete geometry](actual_conway_general_strict_mask_geometry.md)
to the original pure/odd face pairings, primitive peripheral paths and
absolute filled-volume calibration. Every complete leaf is at or above
the quarter index, so the proved high and quarter packet constructions
cover the entire fixed tree. The [general core theorem](actual_conway_general_core_packet_and_gap.md)
controls the all-core sector for every strict knot pattern. A global
nonempty-alias estimate remains separate. No enlarged full-invariant
limit is inferred from geometry or the local packet alone.

## 1. Scope and complete port data

Take a fixed literal expression \(C(FG)\) in leaves \(h\), ordered
products and actual turns \(T\). Delete only its forced final product,
whose coefficient is one, retaining its original complementary-wire
relation. Assume the reduced positive wire polytope has a strict state:
\[
0<a_i<\frac12,\qquad \max(x,y)<z<x+y<1
\tag{1}
\]
for every leaf and retained gate. The positive action has a unique strict
optimizer with negative-definite reduced wire Hessian. The complete
geometry theorem constructs its actual two-ball right-angled augmented
link exterior. It retains every original shaded triangle, ideal vertex
and oriented ribbon path; no two corners of one leaf become transitively
identified, and every edge cycle has four distinct occurrences.

The [exact compiler](actual_conway_single_leaf_source_composition.md)
assigns each open expression a strict type
\(L=(0,1/2)\), \(H=(1/2,1)\), \(A=(0,1)\), or empty.
The nonempty product rules, including reversed orders, are
\[
LL,LA,AA\longmapsto A,\qquad HL,HA\longmapsto H;
\qquad HH\longmapsto\varnothing.
\tag{2}
\]
Turns exchange \(L,H\) and preserve \(A\). The strict cylindrical root
pairs are \(AA,AL,AH,LH\), in either order.

For an optimized port of output \(b\), set
\[
B=\cot(\pi b),\quad \kappa=e^{-f_E'(b)},\quad
X^2=\frac{1+B^2}{1+\kappa},\quad Y^2=\kappa X^2,\quad X,Y>0.
\]
Then \(X^2+Y^2-B^2=1\), and the exact port types are
\[
\begin{array}{c|c}
L&(B,X,Y)=(B,B,1),\quad B>0\\
H&(B,X,Y)=(-Y,1,Y),\quad Y>0\\
A&-Y<B<X.
\end{array}
\tag{3}
\]
A turn maps \((B,X,Y)\) to \((-B,Y,X)\). At a strict product the
children have common \(X\); with \(S=B_1+B_2>0\),
\[
B_o=\frac{B_1B_2+X^2-1}{S},\qquad Y_o=\frac{Y_1Y_2}{S}.
\tag{4}
\]

Number the port edges cyclically. FREE edges are \(0,2\). Let
\(\eta_j=1\) precisely when the adjacent nonport face is SHADED.
Its dihedral angles divided by \(\pi\) are
\[
\theta_j=\begin{cases}
b-\eta_j/2,&j=0,2,\\
1-b-\eta_j/2,&j=1,3.
\end{cases}
\tag{5}
\]
An \(L\) mask is supported only on CAP edges, an \(H\) mask only on
FREE edges, and an \(A\) mask vanishes. The leaf mask is \((0,1,0,1)\).
A turn rotates it; a product has mask
\((\eta^F_0,0,\eta^G_2,0)\). Its shared child FREE edge has angle
\(1-(\eta^F_2+\eta^G_0)/2\), and those two bits cannot both be one
at a strict product. Root complementary types likewise forbid two
shaded bits on a closing seam. These are individual edge statements;
the asymmetric \(H\) pattern must not be replaced by a pair-symmetric one.

## 2. A general quarter-index theorem

**Proposition.** At the complete optimizer of every strict closed tree,
every port has \(X,Y\le1\). Consequently
\[
\boxed{\frac14\le a_i<\frac12\quad\text{for every original leaf}.}
\tag{6}
\]

At the root, complementarity gives opposite \(B\)'s and equal ordered
metrics, hence common \(X,Y\). In type \(AA\),
\(|B|<\min(X,Y)\), so \(X^2+Y^2-B^2=1\) gives \(X,Y<1\).
In \(AL\), the \(L\) port has \(X=B,Y=1\); the other port has
\(B_A=-X>-1\), hence \(X<1\). In \(AH\), the \(H\) port has
\(X=1\), while the \(A\) inequality gives \(Y<1\).
In \(LH\), the explicit forms force \(X=Y=1\).

For the downward step put \(c=1-X^2\). The identity
\[
(B_1^2+c)(B_2^2+c)-(B_1B_2-c)^2=c(B_1+B_2)^2
\]
gives \(Y_o^2-B_o^2=1-X^2\), so positivity implies \(X_o=X\).
Every child type has \(B_i\le X\), and \(S>0\) gives
\(B_i>-B_j\ge-X\). Thus
\[
Y_i^2=1+B_i^2-X^2\le1.
\]
Products propagate the bounds to both children, and turns swap them.
At a leaf \(X=\cot(\pi a)>0\), proving (6).

Equality is genuine. For \(C(hT(h^s))\), the unturned \(h^s\) port
is \((1/s,1,1/s)\), its turn is \((-1/s,1/s,1)\), and the root
leaf port is \((1/s,1/s,1)\). The seed leaves have \(a=1/4\), the
root leaf has \(a=\arctan(s)/\pi\), and all retained gates are strict.
At a quarter leaf the source recurrence roots are \(+i,-i\): this is
an equal-modulus boundary, not an eigenvalue collision. No strict
quarter inequality is asserted for the enlarged syntax.

## 3. The selected source action and regular deformed charts

Keep each physical sign \(\epsilon_i\in\{0,\pm1\}\) in its original
leaf frame. On the continued complete branch define
\[
\begin{aligned}
J(s)&=\int_0^s\operatorname{Log}(2\sin\pi u)\,du,\\
g(x,t)&=J(2x)-2J(x)-J(x-t)-J(x+t),\\
v&=g_t=\operatorname{Log}\frac{\sin\pi(x-t)}{\sin\pi(x+t)},\\
\chi&=t-\frac{\epsilon v}{2\pi i},\qquad
f_\epsilon(x,\chi)=g(x,t)-\frac{\epsilon v^2}{4\pi i}.
\end{aligned}
\tag{7}
\]
The implicit derivative at completeness is
\(1-\epsilon i\cot(\pi x)\ne0\). Thus (7) is a unique holomorphic
germ, even in \(\chi\), and exactly
\[
df_\epsilon=g_x\,dx+v\,d\chi.
\tag{8}
\]
The [high-index source identity](actual_odd_conway_marked_peripheral_deformation.md),
§2, and the [quarter packet theorem](actual_conway_quarter_index_color_packet.md)
identify this same branch with the actual continued finite source,
including its original chirp. Proposition (6) covers every leaf of a
fixed strict tree. No continuation into arbitrary low complete indices
is being assumed.

For precision, the negative-source action and (7) have the same branch
of the algebraic equation
\[
K^2(1+E)^2+K[(H+H^{-1})E^2+2]+(1-E)^2=0,
\quad E=e^{2\pi ix},\ H=e^{2\pi i\chi},\ K=e^{-f_x},
\tag{9}
\]
selected by \(K=\tan^2(\pi x)\) at \(H=1\). The constant is fixed at
\(x=1/2\) for fixed small \(\chi\): then \(v=0\), \(t=\chi\), and
\(g(1/2,t)=0\) by \(J(1/2+t)=-J(1/2-t)\). The selected source
integral \(\int_x^{1/2}\operatorname{Log}\mu(u,\chi)\,du\) tends to
zero with regular \(\mu(1/2,\chi)=1\). The hidden \(t\) does not tend
to zero. Schwarz reflection gives the positive sign.

In the original reduced free wires \(y\), set
\[
\mathcal A_\epsilon(y,\chi)=
\sum_i f_{\epsilon_i}(a_i(y),\chi_i)+\sum_{\text{retained gates}}m.
\tag{10}
\]
At zero color this is the complete positive action. Its invertible wire
Hessian gives a unique holomorphic critical branch \(y_*(\chi)\);
write \(\Phi_\epsilon(\chi)=\mathcal A_\epsilon(y_*(\chi),\chi)\).
By (8), wire stationarity is exactly the original ordered metric
matching, evaluated at the hidden pure colors. Turns and the root
complementary relation are unchanged. All finitely many complete flags
and three-point charts are nondegenerate, so remain regular on one small
polydisk.

The second-copy charts are holomorphic: invert the prism angle phases,
without conjugating free source variables. Normalize a leaf port to
\((0,\infty,1,R)\), put \(T=e^{2\pi it}\), and select
\[
Z=\frac{1+E}{1+T},\qquad
R=\frac{T(1+E)^2}{E(1+T)^2},\qquad
Z^2-(1+E)Z+ER=0.
\tag{11}
\]
The projection apices are \(Z,Z/E\). This is the original reflected-minus
convention, including when deformed white pieces are not planar.

## 4. Actual and virtual white maps for every mask

Use the universal matrices
\[
\begin{aligned}
W_0&=\begin{pmatrix}1&0\\0&E\end{pmatrix},&
W_1&=\begin{pmatrix}1&E-1\\0&E\end{pmatrix},\\
W_2&=\begin{pmatrix}E-R&R(1-E)\\E-1&1-ER\end{pmatrix},&
W_3&=\begin{pmatrix}R&0\\1-E&ER\end{pmatrix}.
\end{aligned}
\tag{12}
\]
Each fixes the endpoints of its port edge. The strengthened invariant is:

- If \(\eta_j=0\), \(W_j\) is the actual transition on the adjacent
  WHITE piece to the other projection copy.
- If \(\eta_j=1\), \(W_j\) is a virtual WHITE completion map, not a
  map assigned to the actual SHADED face. It prescribes the transition
  that must lie across the surviving shaded edge after gluing.
- Every already internal shaded edge has its actual adjacent WHITE map
  equal to this completion map in the original leaf frame. WHITE pieces
  already joined carry the same entire Möbius map, including translation.

At a leaf, \(W_0,W_2\) are actual WHITE maps, sending \(Z\) to \(Z/E\)
by (11). The matrices \(W_1,W_3\) are virtual completions at its shaded
CAP bases. No fictitious white face is inserted.

In the original world charts, the [generic prism identities](actual_conway_marked_peripheral_deformation.md),
§3, are
\[
\begin{aligned}
W_{F,1}=W_{G,1}=W_{o,1}&=B_{\mathrm{top}},\\
W_{F,3}=W_{G,3}=W_{o,3}&=B_{\mathrm{bottom}},\\
W_{F,2}&=W_{G,0},\\
W_{o,0}=W_{F,0},\qquad W_{o,2}&=W_{G,2}.
\end{aligned}
\tag{13}
\]
Here the two \(B\)'s are actual WHITE prism triangle maps. These are
rational identities in independent prism phases, valid also above a
half-index wire label. They use the original ordered maps
\[
F:C\mapsto(v_0,v_1,P,\infty),\qquad
G:C\mapsto(\infty,P,v_2,v_3).
\]
They are not modulus-only identities or reflected substitutions.

There are exactly three seam checks.

1. At a child CAP seam the prism side is WHITE. A zero bit identifies
   two actual white maps across a flat seam by (13). A nonzero bit
   preserves the shaded triangle and supplies its actual completion
   from the prism map.
2. At the shared FREE edge the bits are \((0,0),(1,0)\), or \((0,1)\).
   In the first case actual WHITE pieces merge by \(W_{F,2}=W_{G,0}\).
   In the other two, the unmasked child's actual map supplies the masked
   child's completion. The edge stays right angled. The forbidden
   \((1,1)\) case would be a strict \(HH\) product.
3. The remaining output FREE maps inherit their status through the last
   line of (13); the two output CAP maps are actual prism WHITE maps.
   This is precisely the mask \((\eta^F_0,0,\eta^G_2,0)\).

The turn and closing identities are
\[
\begin{aligned}
T_Q(z)&=\frac{R-1}{z-1},&
T_QW_{j+1}(E,R)&=W_j(E^{-1},1-R)T_Q,\\
C_Q(z)&=\frac{z-R}{z-1},&
C_QW_j(E^{-1},R)&=W_{2-j}(E,R)C_Q.
\end{aligned}
\tag{14}
\]
A turn rotates the mask and transports actual/virtual status unchanged.
At the root, the complementary-type rule excludes two shaded bits on a
paired edge. Zero/zero pairs merge actual WHITE pieces; one/zero pairs
supply the required completion from the actual white side. No port
remains, so every original shaded base now has its required actual
adjacent WHITE map.

This proves the invariant without a pair-symmetric \(H\) pattern,
without restricting internal wire labels below \(1/2\), and without
using a virtual map as a premature face pairing. It includes turned
bare leaves and all strict root-leaf closures. Every triangular piece
in one original WHITE face has one entire common transition, even if
its deformed image is not planar. The original abstract face-paired
balls, rather than deformed embeddedness, determine the representation.

## 5. Original shaded words and the actual group

In each original leaf frame retain
\[
S=\begin{pmatrix}0&-ER\\1&-1-E\end{pmatrix},\quad
A=\begin{pmatrix}R&-R\\1&ER-1-E\end{pmatrix},\quad
B=\begin{pmatrix}R/E-1-1/E&R\\-1&R\end{pmatrix}.
\tag{15}
\]
The pure map \(S\) pairs within one copy. The odd maps \(A,B\) pair
\((Z,\infty,1)\) with \((Z/E,R,0)\), and \((Z,R,0)\) with
\((Z/E,\infty,1)\). At completeness these are the original half-disk
rotations. Every half-twist pattern therefore has the same complete
metric: the four edge occurrences remain distinct, changing the copy
permutation does not collapse original corners, and the canonical
length-one shaded decorations are preserved.

With \(\bar S\) denoting \(E\mapsto E^{-1}\), the pure relations are
\[
W_0S=\bar S W_0,\qquad W_2S=\bar S W_2,\qquad W_3S=\bar S W_1.
\tag{16}
\]
The odd relations are
\[
W_0^{-1}BW_2^{-1}A=I,\qquad
W_2^{-1}BW_0^{-1}A=I,\qquad
W_1^{-1}BW_3^{-1}A=I.
\tag{17}
\]
These hold for independent nearby \(E,R\), pointwise, including
translations and dilations. Section 4 makes every \(W\) in the base
words an actual final white transition for arbitrary masks.

The [original closed cut](actual_conway_bowtie_projection_cut.md)
supplies two actual topological balls. Their dual two-skeleton has face
transitions as generators and original edge words as relations. The
WHITE seams and all shaded relations have been verified. Hence these
maps define an actual holomorphic framed representation \(\rho_\chi\)
of the original signed augmented-link group near its oriented complete
holonomy. Products and turns conjugate the original leaf data into world
coordinates; they neither replace a physical leaf by a scalar coupon nor
change its integral disk curves.

At a main corner the two final original WHITE sectors have maps
\(W_{j-1},W_j\), one possibly supplied as a completion. The actual small
main meridian is \(W_{j-1}^{-1}W_j\), or its inverse. Their derivatives
at the common corner are equal: \(E^{-1}\) at \(C_0,C_2\), \(E\) at
\(C_1,C_3\), in finite local coordinates. Its multiplier is identically
one. It stays nonidentity near completeness and is therefore parabolic.
Its peripheral commutant consists of translations. All main cusp groups
remain parabolic, whatever their number of components.

## 6. Primitive auxiliary curves and the absolute action

The auxiliary collar remains in its original leaf box. Its two shaded
triangles and apex are untouched by port attachments. The original
primitive disk curves therefore persist through turns and closures;
world-coordinate transport conjugates their whole words.

Put
\[
\rho=\frac{Z}{1+E-Z},\qquad Q=\frac{E-Z}{Z-1}.
\]
The disk longitude is \(W_2^{-1}W_0\), with flag-at-infinity multiplier
\(Q^2\). The pure meridian \(S^{-1}\) has multiplier \(\rho\). The
odd primitive meridians \(A^{-1}W_0\), \(W_0^{-1}B\) have multipliers
\(\rho Q\), \(\rho/Q\). Their complete translations are \(-2\) and
\(2E\); the longitude translates by \(-2(E+1)\). The two-rectangle
lattice proves primitivity.

The [original threading calculation](actual_pretzel_mixed_regular_character_lift.md),
§§4–5, fixes the sign: the typed loop \([2,1,1,2]\) followed by
\(R^{-1}\) has actual auxiliary matrix
\(I-(P+I)/(1+E)\), \(\operatorname{Tr}P=-2\), preferred projective
longitude \(-P\), and translation ratio \(1+E\). Thus the physical
\(R^{-1}\) coupon uses the first odd path and \(R\) the second.
This is local to the original leaf frame; a port turn does not rename
its physical sign.

Using (11), \(\rho=e^{-2\pi it}\), \(Q=e^{-v}\). The actual centered
similarity logs are
\[
U_i=-2\pi it_i-\frac{\epsilon_iV_i}{2}=-2\pi i\chi_i,
\qquad V_i=-2v_i=-2\partial_i\Phi_\epsilon.
\tag{18}
\]
They are squared-eigenvalue logs; the original lift and pivot characters
are retained in the finite source. The half-longitude shear compares
actual primitive bases, not an integral half-longitude curve or an
ordinary rational filling of the pure partner.

With \(G=2\pi i\Phi_\epsilon\), on the same connected marked family,
\[
dG=\frac12\sum_iV_i\,dU_i,\qquad
G_\epsilon-G_{\mathrm{pure}}=-\sum_i\frac{\epsilon_iV_i^2}{8},
\qquad \Im G(0)=\operatorname{Vol}(Y_E^\epsilon)=2\pi\Phi_\epsilon(0).
\tag{19}
\]
The comparison uses the hidden pure colors and stationary wires. The
original ideal-chain Bloch differential cancels internal faces and keeps
each primitive torus's \(-2\) eigenlog wedge. Thus
\[
d\operatorname{Vol}(\rho)=\frac12\sum_i
(\Re V_i\,d\Im U_i-\Re U_i\,d\Im V_i).
\]
The complete degree-one anchor fixes the constant, giving
\[
\operatorname{Vol}(\rho_\chi)=\Im G(\chi)
-\frac12\sum_i\Re U_i\Im V_i.
\tag{20}
\]
This is the actual original fundamental class, not an unrelated Bloch
cycle with the same differential. Known real Cartan constants remain
recorded. The complete imaginary normalization is geometric.

## 7. Smooth actual fillings and knot pairing

Evenness makes all mixed wire/color first derivatives vanish at zero.
There is no wire Schur correction to the color Hessian. With
\(c_i=\cot(\pi a_i)>0\),
\[
\partial_i\partial_j\Phi_\epsilon(0)
=-\frac{2\pi c_i}{1-\epsilon_i i c_i}\delta_{ij}
=2\pi i\tau_i\delta_{ij},\qquad
\tau_i=\frac{ic_i}{1-\epsilon_i i c_i},\quad \Im\tau_i>0.
\tag{21}
\]
Choose any auxiliary subset to fill and set \(\chi_i=0\) elsewhere.
Separate evenness gives \(V_i=0\) at the unfilled auxiliary cusps,
so they remain parabolic. For independently signed integers \(p_i\),
the actual primitive equations are
\[
U_i+p_iV_i=-2\pi i.
\tag{22}
\]
Writing \(r_i=1/p_i\), their Jacobian in \(\chi\) at \(r=0\) is
\(-4\pi i\operatorname{diag}(\tau_i)\), invertible by (21).
The implicit-function theorem supplies the selected solution in one
fixed reciprocal-slope polydisk, without slope-comparability conditions.

Apply the [proved framed completion theorem](general_source_regulator_hyperbolic_equality.md),
also proved in [Appendix D](../manuscript/sections/D-marked-cell-calibration.tex),
§4. Its hypotheses are now all supplied: an actual nearby representation,
actual fixed flags, primitive small logs and parabolic unfilled cusps.
Its core/cusp development proves the actual log-link periods before
multiplying by the slopes, and completes each punctured tube by one
angular turn. The result is a smooth complete finite-volume metric on
the original disk-filled topology. The physical power is
\(R^{\epsilon_i-2p_i}\), once; a knot cusp is never filled.
At the saddle, (20) becomes
\[
\operatorname{Vol}(Y_E^\epsilon(\mathbf p))
=2\pi\Re\left[
\Phi_\epsilon(\chi_*)+\frac{\pi i}{2}
\sum_{i\,\mathrm{filled}}\frac{(\chi_i-1)^2}{p_i}\right].
\tag{23}
\]
This geometric theorem is unconditional for each fixed strict syntax
and sign pattern. If all auxiliaries are filled and the literal main
pairing has one component, it is the volume of the resulting **knot
complement**. No isotopy to a completed-root expression is asserted.

Such a one-component choice exists. For cyclic terminals write
\(I=(03)(12)\), \(U=(01)(23)\), \(X=(02)(13)\). A leaf offers
\(\{U,X\}\); turn exchanges \(I,U\) and fixes \(X\). The product table is

| Lower / upper | \(I\) | \(U\) | \(X\) |
|---|---|---|---|
| \(I\) | \(I\) | \(U\) | \(X\) |
| \(U\) | \(U\) | \(U\) plus an internal loop | \(U\) |
| \(X\) | \(X\) | \(U\) | \(I\) |

Only \(U\cdot U\) is forbidden. For sets \(A=\{I,U\}\),
\(B=\{I,X\}\), \(C=\{U,X\}\), the allowed output sets of
\(AA,AB,AC,BB,BC,CC\) are respectively
\(A,\{I,U,X\},C,B,\{I,U,X\},A\), also in reversed order.
Thus every node retains at least two loop-free choices. At the root
one of \(U,X\) closes to one main component. Full twists preserve that
endpoint permutation. This is a finite pairing proof, not an invariant
limit argument.

## 8. The exact local packet and the remaining source obligation

The [general core theorem](actual_conway_general_core_packet_and_gap.md)
gives the complete analytic details; we record why they apply to this
actual masked deformation. With \(H\) leaves, there are \(H\) leaf
indices and \(H-2\) retained gate-output indices before the final unit
relation. Eliminating that relation leaves the primitive lattice
\(\mathbb Z^K\), \(K=2H-3\), including a bare or turned root leaf.
Turns are the literal integer map \(r\mapsto d-r\), \(d=N-1\).
In primitive coordinates each exact wire is
\(r_w=NL_w(k/N)+\delta_w\), with its original fixed integer offset.

Choose a small fixed rectangular window \(B\) around the strict complete
optimizer. Every gate is strict there. By (6), shrink it inside either
a high-index or the proved quarter neighborhood for each leaf. Let
\(\ell_N^\epsilon\) be its exact finite continued-color core coefficient,
after extracting only the known constant unit chirp. The exact window is
\[
\mathcal C_N(\chi)=\sum_{k/N\in B}
\prod_i\ell_N^{\epsilon_i}(r_i,\chi_i)
\prod_g\mu_N(r_{g1},r_{g2},r_{g3}).
\tag{24}
\]
Its support is fixed before complex colors, and it is finite, separately
even and holomorphic on a fixed small color polydisk. The gates are the
exact seven-factorial Newton coefficients; every physical small-color
entry retains the original normal directions.

Use the specified high or quarter holomorphic index interpolant at each
leaf and the canonical factorial interpolant at each gate. Before any
oscillatory sum, the total grid residual is bounded by
\[
\operatorname{poly}(N)\exp N(F_0+C\|\chi\|^2-c),\qquad c>0.
\]
There are polynomially many states, and the even color perturbation is
uniformly quadratic. Shrink the fixed color disk to put this residual
strictly below the nearby critical action. The interpolated summand has
phase (10), leading power \(N^{3-H}\), and nonzero holomorphic density.
Indeed each of the \(H\) leaves contributes \(N^{1/2}\), and each of
\(H-2\) gates contributes \(N^{-3/2}\). Its density includes exactly
\[
\exp\left[
\sum_i\delta_i\partial_x f_{\epsilon_i}
+\sum_g\nabla m\cdot\delta_g\right],
\]
using the changed signed action at nonzero color.

Apply the finite half-grid cotangent rectangles in the primitive
coordinates. The strict local maximum gives a gap on side faces.
On horizontal contours of small height \(a\), nonconstant kernel terms
lose \(e^{-2\pi aN}\), while the analytic phase costs at most
\(e^{N(Ca^2+C\|\chi\|^2)}\). Choose height first and color disk second.
The constant term supplies \(N^K\) times the finite integral. Shift to
the nearby critical contour and apply its nondegenerate Gaussian, which
supplies \(N^{-K/2}\). All contours stay in the common fixed interpolation
domains; all joining pieces are retained and exponentially smaller.
Since \(3-H+K/2=3/2\), adding the grid residual back only now gives
\[
\mathcal C_N(\chi)=N^{3/2}a_\epsilon(\chi)e^{N\Phi_\epsilon(\chi)}
(1+O(N^{-1})),\qquad a_\epsilon(0)\ne0.
\tag{25}
\]
The extracted \(\eta_N\) multiplies both sides in the original source.
The density, original offset exponential and determinant branch are
nonzero at completeness. Both parities have the same primitive density.
Evenness gives the Hessian (21) without a wire Schur correction and the
usual fixed complex Gaussian envelope for this exact finite window.

For completeness, the all-core gap for \(H\ge3\) follows from gate
curvature even when leaf curvature is lost on a plateau. Put
\(p=z-x,q=z-y,r=x+y-z,w=1-x-y\). The exact three-atom identity is
\[
\pi m=V(y,x,w)+V(p,q,1-p-q)+V(p+q,r,r+w).
\tag{26}
\]
Each positive tetrahedral angle Hessian is negative definite on its
simplex. The first atom pins \(\delta x,\delta y\); the second then pins
\(\delta z\). The third is concave. Hence each strict gate is negative
definite in its three wires. Their combined label map has zero kernel
on the primitive tangent space: every leaf/output wire meets a retained
gate, except possibly one root leaf pinned by the complementary root
relation. Thus their total Hessian is negative definite for \(H\ge3\).

Use \(g\) for pure leaves and \(\widetilde g(a)=g(\max(a,1/4))\) for
signed cores. These are concave and have the same complete values and
first derivatives as \(g\), by (6). The complete stationary point is
therefore the global maximum of the core majorant. Gate curvature makes
it a strict local maximum; a second global maximum would force a constant
segment into that neighborhood. Compactness gives the global state gap.
The uniform closed coefficient upper estimate absorbs its \(o(N)\) error;
the compact window has every leaf below some \(\beta<1/2\), so the
collision-safe recurrence also gives the strict far-color loss. The
[core theorem](actual_conway_general_core_packet_and_gap.md) retains the
original finite targets and endpoint normalization in these estimates.

For \(H=2\), one pure leaf supplies the strict \(g+\widetilde g\) or
\(2g\) maximum. Both odd leaves instead give the flat majorant
\(2\widetilde g\) on \([0,1/4]\), although the actual complete action
\(2g\) has unique quarter maximum. This is an exception to this core
argument for that **link**, not a knot pattern: turns fix both odd
pairings \(X\), and \(X\cdot X=I\) closes to two main components.
It is not a counterexample to a sharper full-source estimate.

For every strict knot pattern, the remaining global input is therefore
a bound on the sum of nonempty alias sectors, with their original signs,
or an equally sufficient bound after the exact filling pairing.
The [whole-source transfer](general_original_source_long_filling_transfer.md)
then identifies (23) with the original invariant's full-sequence rate,
retaining the original currents, charges, parity and nonzero coefficient.
No general alias bound follows from port rigidity, the masked geometry,
or the all-core result. No theorem for all arborescent knots is claimed.

## Internal review scope

The parent reviewed the full masked construction, primitive marking,
absolute calibration, quarter proof and expanded packet/core argument.
The independent coherent-source reviewer read all sections analytically
and checked their original-source and topology scope. The local-source
reviewer independently checked the full finite-lattice/window/core part.
All reported PASS. The generic rational matrix identities are the
previously independently verified exact identities; this extension uses
no new numerical sampling. These are internal proof reviews, not external
peer review. The earlier manuscript and public theorem are unchanged.
