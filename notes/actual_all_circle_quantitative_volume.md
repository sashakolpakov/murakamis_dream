# An explicit volume theorem for ordered trees of crossing circles

The number of twists at a region is not the only quantity that can make
filling controllable. In the construction below, a crossing circle of
large degree meets many geometric pieces. Its complete cusp makes even
a small integer twist correspond to a long normalized filling slope.
This gives a numerical sufficient condition for the volume conjecture
in which some twist coefficients may be short or zero.

The [local subtree theorem](actual_all_circle_local_message_volume.md)
gives another sufficient condition for exactly this construction:
\(\max_v d_v/(d_v^2+n_v^2)\le2^{-120}\). Its constant is smaller,
but it has no sum over the vertices. In particular one universal
twist threshold suffices for any finite tree. The summed criterion
proved below remains a separate, often numerically better test.

## The knot construction

A two-string tangle is drawn in a ball with four ordered boundary
points: lower left, lower right, upper right, upper left. A product
places one ball above another and joins their two adjacent endpoints
by uncrossed arcs. The order of the factors is retained. The operation
\(T\) rotates an entire ball through the specified quarter-turn in the
diagram plane. Cylindrical closure joins lower left to upper left
and lower right to upper right outside the final ball.

Fix a finite tree \(\mathcal T\) with at least one edge, together with
the cyclic order of the edges and the tangle frame at each vertex.
There is one original crossing circle at every vertex, including the
terminal vertices. There is no unmarked product junction. Each edge
represents an actual quarter-turn of a child tangle, rather than a
crossing of two drawn edges.

Here is a precise recursive way to specify the diagrams. Choose a
terminal vertex as root. At a nonroot vertex \(v\), put the integer
braid \(R^{n_v}\) between the two ordered lists of its child tangles:
\[
 W_v=\left(\prod_{w\in I_v^-}T(W_w)\right)R^{n_v}
       \left(\prod_{w\in I_v^+}T(W_w)\right).
 \tag{1}
\]
The lists \(I_v^-\) and \(I_v^+\) specify the position of the crossing
box in the original cyclic order. Empty lists are allowed. If \(w\)
is the root's unique neighbor, close \(R^{n_0}T(W_w)\)
cylindrically. This is an actual link diagram, not a tensor network
considered only up to scalar identities. Other choices of cutting
section are related by the physical closed-collar moves, with their
induced rotations and reversals of factor order retained.

The augmented diagram replaces each \(R^{n_v}\) by its crossing circle
and a retained half twist \(\epsilon_v\in\{0,\pm1\}\), where
\(n_v\equiv\epsilon_v\pmod2\). Filling that circle on its original
disk-framed slope \(\mu_v+p_v\lambda_v\), with
\[
                         n_v=\epsilon_v-2p_v,
 \tag{2}
\]
restores exactly the indicated integer braid. Here \(\mu_v\) goes once
around the auxiliary circle and \(\lambda_v\) follows its punctured
disk. The main strands are not filled.

We require that the closed main strands form one knot \(K\). This
includes excluding a closed main component created inside an
intermediate box. The test uses only the strand pairings and the
parities of the \(n_v\); large magnitudes alone do not guarantee it.
Write \(d_v\) for the degree of \(v\) in the circle tree and
\(E=|E(\mathcal T)|\). This graph degree is unrelated to the quantum
level \(N\).

## The quantitative theorem

Let \(F_N(M)\) be the zero-framed reduced Akutsu--Deguchi--Ohtsuki
(ADO) invariant of the actual
knot, normalized to one on the unknot. Its marked meridian coordinate
is \(M\), and at \(q_N=e^{\pi i/N}\) its complete value is the reduced
Kashaev invariant \(K_N(K)=F_N(1)\). Moving the meridian on the scale
considered here means setting \(M=q_N^s\), with \(s\) in a fixed
complex disk. Define
\[
 \mathfrak S(\mathcal T,\mathbf n)
       =\sum_v\frac{d_v}{d_v^2+n_v^2},\qquad
 H_N(s)=\frac{\sin(\pi s)}{N\sin(\pi s/N)},\quad H_N(0)=1.
 \tag{3}
\]
Let \(w(D)\) be the oriented writhe of the actual filled diagram,
using the same positive checked-crossing convention as \(R\). The
exact framing and crossing factor is
\[
 A_N(s)=q_N^{a(D)s^2/2},\qquad
                         a(D)=-w(D)-\sum_v n_v.
 \tag{4}
\]
The power uses the fixed logarithm \(\log q_N=\pi i/N\). All crossing
and strand-turn factors are included in (4); it is not a chosen
normalizing phase.

**Theorem.** Fix the ordered tree, its diagram frames, and its signed
integer powers before letting \(N\) tend to infinity. Suppose the
main strands form a knot and
\[
                         \mathfrak S(\mathcal T,\mathbf n)\le2^{-25}.
 \tag{5}
\]
Then the knot complement is hyperbolic, and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                      =\operatorname{Vol}(S^3\setminus K).
 \tag{6}
\]
For every fixed \(R<1\), the stronger statements
\[
 \frac{F_N(q_N^s)}{F_N(1)A_N(s)H_N(s)}
       =1+O_{\mathcal T,\mathbf n,R}(N^{-1}),
 \qquad |s|\le R,
 \tag{7}
\]
and
\[
 \frac{2\pi}{N}\log|F_N(q_N^s)|
           \longrightarrow\operatorname{Vol}(S^3\setminus K)
 \tag{8}
\]
hold uniformly on that disk. In particular these values are nonzero
there for all sufficiently large levels. Both level parities and
composite levels are included. The tree, its degrees, its twist
numbers and the radius \(R\) do not grow with \(N\).

The constant in (5) is conservative. It makes the condition explicit;
no optimality is asserted. There is no additional strict-angle
hypothesis for this literal class. Indeed an unturned elementary
circle has attainable output interval \((1/2,1)\), and a turned
subtree has interval \((0,1/2)\). The exact product interval shows
that one upper-interval factor together with any number of
lower-interval factors again has the full upper interval, in any
fixed association. The turn changes it to the lower interval.
At the terminal root the two complementary intervals give a strict
closing pair. This inductive construction supplies the strict
augmented geometry used by the finite-source proof. In the two-circle
case the excluded two-odd pattern is not a knot; the knot test retains
the necessary even, or pure, leaf.

Two consequences make the range of (5) concrete.

* For a tree with \(E\) edges, every tuple satisfying
  \( |n_v|\ge8192\sqrt E\) satisfies (5), because
  \(\sum_vd_v=2E\).
* Start with any ordered tree on \(m\) vertices, with arbitrary fixed
  powers at those vertices. Attach \(B\) new terminal circles at
  each vertex and give each added circle a power of magnitude at
  least \(B\). The resulting sum is strictly less than \(2m/B\).
  Hence \(B\ge2^{26}m\) suffices, with the original powers still
  arbitrary, including zero. The knot/parity test remains necessary.

An unmarked product junction can also be included by inserting the
literal identity braid \(R^0\) at its prescribed position in the
ordered stack. Add a crossing circle there in the augmented diagram
and fill it with \(\epsilon=p=n=0\). The filled diagram is unchanged.
The augmented exterior is different, and the added degree-\(d\)
circle contributes \(1/d\) to (3). This gives a direct application
to constructions with sufficiently large-degree unmarked junctions
when the same total bound holds. It does not treat such junctions as
free or assert that a low-degree unmarked junction satisfies (5).

All these are finite constructions. Their potentially large size is
fixed before the quantum limit. Related results use several invariant and root conventions;
[the coverage discussion](general_untwisted_augmented_source_literature_coverage.md)
records their precise scopes.

## Why the original exterior has the required geometric pieces

Cut the augmented diagram along the projection sphere and the original
crossing disks. The two resulting balls carry white projection faces
and shaded disk triangles. At a leaf with half-segments
\((v_0,v_1,v_2,v_3)\), the shaded triangles are
\((O_v,v_1,v_2)\) and \((O_v,v_3,v_0)\), where \(O_v\) is the
auxiliary-circle end. The literal strand matching fixes every cyclic
vertex order and hence every white face boundary.

Adding one terminal child supplies an explicit local cell attachment.
Let \(h_v\) denote the quarter-turned crossing-circle tangle. Write its parent's unturned box as \(P_v=T^{-1}h_v\), so its
exposed tuple is \((v_3,v_0,v_1,v_2)\). If the old downstream matches
are \(v_1-x_1\) and \(v_2-x_2\), insertion of \(h_w\) immediately
after \(P_v\) replaces them by
\[
 v_1-w_1,\quad v_2-w_0,\quad w_2-x_1,\quad w_3-x_2.
 \tag{9}
\]
Set \(C=(v_1,x_1)\), \(B=(v_2,x_2)\),
\(D=(v_1,w_1)\), and \(A=(v_2,w_0)\). An octahedron with opposite
vertices \(O_v,O_w\) and equator \(A,B,C,D\) has shaded faces
\[
 (O_v,B,C),\quad(O_v,D,A),\quad(O_w,D,C),\quad(O_w,B,A).
 \tag{10}
\]
Glue its first face to the old face \((O_v,C,B)\), with the opposite
boundary orientation. The other three faces are precisely the new
shaded faces prescribed by (9). The adjacent white sectors also
concatenate in the literal strand order. Thus this is an attachment
in the original cut, not a recognition based on equal volumes.

![Attaching one actual octahedron in a projection half. Equal vertex labels are identified, and the indicated boundary orientations are opposite. The triangle becomes internal; the other three shaded triangles retain the parent circle and introduce the new child circle. The same attachment is made in the other projection half. Only the glued faces are blue; the other disk faces are listed in (10). The cells come from the augmented knot diagram built by ordered two-string stacking and quarter-turns. The labels \(O_v,O_w\) belong to its actual auxiliary crossing circles.](../book/figures/octahedral-page-attachment.svg)

The left-insertion version attaches along the other parent triangle.
It allows the parent box to remain at its specified position among
its children. Start from one tree edge and insert the remaining
children in the appropriate left and right order, carrying each
rotated child ball with its frame. Each projection half is a tree of
\(E\) octahedra attached along \(E-1\) triangles. Its remaining
shaded faces are exactly the original two per circle.

The internal interfaces give the additional disk pages. At a circle
of degree \(d_v\), the \(d_v\) incident blocks occur in the original
cyclic order. One distinguished seam retains the original half twist;
the other seams are the untwisted insertion maps. In particular the
construction does not put one copy of the retained crossing on every
incident edge. It also retains the actual half-turn produced when a
turn is moved across the closing sphere. Restoring the labeled faces
recovers the original augmented link and its primitive disk paths.
The [ordered decomposition proof](actual_all_circle_octahedral_decomposition.md)
gives the full half-segment and face-word calculation.

## Positive cells and primitive filling periods

For an edge with endpoint angular variables \(t,u\), the finite
quantum sum has the following analytic phase. Its derivatives determine
the geometric logarithms below:
\[
 \begin{aligned}
 \psi(t,u)&=\operatorname*{stat}_{x}[b(x,t)+b(x,u)],\\
 b(x,t)&=\int_0^x\log(2\cos2\pi v+2\cos t)\,dv-2J(x),\\
 J(x)&=\int_0^x\log(2\sin\pi v)\,dv.
 \end{aligned}
 \tag{11}
\]
Branches continue \(x=1/4,t=u=0\). In particular
\[
 \tan^2(\pi x)=\frac1{1+\tan^2(t/2)+\tan^2(u/2)},\qquad
 \psi_t=-\frac1\pi\operatorname{arsinh}
                       (\tan(t/2)\cos(u/2)).
 \tag{12}
\]
Let \(\Psi=\sum_{vw}\psi(\tau_v,\tau_w)\). The first Fourier term
of the exact crossing traces has phase
\[
 \Psi(\boldsymbol\tau)+\frac{i}{4\pi}\sum_v n_v\tau_v^2
                                      -i\sum_v\tau_v.
 \tag{13}
\]
To locate its geometric branch, vary its last coefficient continuously
from zero to one. For \(0\le c\le1\) solve
\[
 \Psi_{\tau_v}+\frac{i n_v}{2\pi}\tau_v=ic,
                         \qquad\boldsymbol\tau(0)=0.
 \tag{14}
\]
The quantitative estimate (5) gives a unique branch with
\[
 |\tau_v(c)|\le
 \frac{2\pi c}{(1-1/50)\sqrt{d_v^2+n_v^2}}<0.00111,
                    \qquad\Im\tau_v(c)<0\quad(c>0).
 \tag{15}
\]
This is a bound on each local angular parameter. It is not a bound
requiring the total primitive meridian logarithm to stay near zero.

Each edge block admits eight positively oriented ideal tetrahedra
whenever both angular parameters have modulus at most \(0.01\).
Their complete shapes are \(i\), and their deformed shapes stay
within distance \(0.4\) of \(i\). On a disk page put
\(Q=e^{i\tau_v}\). The three complex ratios on its incoming edges
are \((-Q^{-1},-Q,-Q^{-1})\); the outgoing ratios are their
inverses. These ratios keep both angle and shear, and depend only on
this circle's parameter. Consequently adjacent blocks fit even if
their other endpoints have different parameters. At the distinguished
odd seam the original cross-copy disk maps exchange the prescribed
punctures. Their full matrix edge words are identities. Positivity
and continuation fix every interior edge angle at \(2\pi\).

The actual meridian crosses the consecutive disk-page sectors once.
A pure edge contributes \(-2\pi\psi_{\tau_v}\); the single retained
half twist contributes \(-i\epsilon_v\tau_v\). The original
primitive logarithms are therefore
\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,\qquad
 V_v=2i\tau_v,
 \qquad U_v+p_vV_v=-2\pi ic.
 \tag{16}
\]
These are continued logarithms of actual paths. Their last identity
cannot be obtained by reducing \(U_v\) to a principal logarithm.

For completeness, the link of an auxiliary ideal vertex is a torus
with a nonsingular similarity structure. Since \(\Re V_v>0\), its
holonomy has a second fixed point \(q_v\) after the marked point
has been sent to infinity. The developing image avoids \(q_v\): a
zero of the invariant vector field \((z-q_v)\partial_z\) has
positive index, whereas a torus has total index zero. Hence
\(\log(z-q_v)\) develops a complete Euclidean torus. Near \(c=0\),
\(q_v\) tends to infinity and the periods on the fixed original
paths tend to zero. Their difference from (16) is a continuous
integer multiple of \(2\pi i\), and is therefore zero along the
whole path.

The slope in (16) has cone angle \(2\pi c\). Its independent
longitude has positive real period, so it bounds a punctured metric
tube with a positive core length. At \(c=1\), attaching the core
produces a smooth solid torus on precisely the original primitive
slope. The main cusp stays a complete parabolic cusp. This constructs
a complete finite-volume hyperbolic metric on the original knot
complement, including the short coefficients permitted by (5).
The [local angular cells](actual_all_circle_angular_octahedra.md) give
the explicit vertex and face formulas, and the
[geometric completion proof](actual_all_circle_geometric_completion.md)
retains the original odd seams and logarithmic periods throughout
this path.

## The action and the invariant have the same normalization

The same actual cells fix the additive constant of the complex action.
With \(V_v=2i\tau_v\), set
\[
 G=2\pi i\left(\Psi-\sum_v\tau_v\Psi_{\tau_v}\right)
                                  +\frac12\sum_v\epsilon_v\tau_v^2.
 \tag{17}
\]
Then \(dG=\frac12\sum_vV_v\,dU_v\). At zero, its imaginary part
is the volume of the original complete augmented link. The marked
boundary formula is
\[
 \operatorname{Vol}=\Im G-\frac12\sum_v\Re U_v\Im V_v.
 \tag{18}
\]
Let \(\mathcal C(c)\) be (13) with the last term multiplied by
\(c\), evaluated at (14). Substitution of the original filling
relation in (17)--(18) gives
\[
                         \operatorname{Vol}_c=2\pi\Re\mathcal C(c).
 \tag{19}
\]
At \(c=1\), the right side is thus the volume of the knot complement
just constructed.

The finite invariant selects this action without an assumption about
saddle dominance. The polynomial expansion of the finite invariant assigns an integer
label \(0\le k<N\) to every internal edge. Its normalized label is
\(x=k/N\); the high range is \(k>\lfloor(N-1)/2\rfloor\).
The complete contribution of an edge is maximized at \(x=1/4\). Outside
\([1/5,3/10]\), that edge loses a fixed exponential amount; a high
index loses a fixed amount as well. The total discarded source has
an absolute gap \(\pi/200\), independently of graph size, although
its polynomial prefactor can depend on the fixed tree and powers.
The exact finite angular sum has a Gaussian bound weighted by the
vertex degrees. Its real decay constant can be taken as \(1/400\)
and its imaginary growth constant as \(70\).

Preconditioning (14) by \((d_v-i n_v)/(2\pi)\) gives a contraction
with constant at most \(1/25\). The same estimates compare every
retained nonzero Fourier charge with charge one, with a strict loss
unless every charge has magnitude one. The exact crossing-trace identity has already paired the reflected
positive and negative modes, and the resulting coefficient of the first
charge is exactly one. Exact contour identities bound the omitted charge
tails and their joining segments by an absolute exponential error.
The possible drop of the first action is at most
\(\pi(2550/2401)\mathfrak S\), which (5) places below half the
available error gap. Thus the selected term is nonzero for both
parities of \(N\).

The physical closing trace contributes exactly \(H_N\), and all
remaining crossing, changes of tensor order and zero-framing factors combine
into the exact \(A_N\) in (4). The bounded insertion on each retained
edge is \(1+O(N^{-1})\); the conditioned saddle evaluation therefore
gives (7). The full constant and the scalar are retained when passing
to (6)--(8). Neither the volume of a comparison diagram nor the
complete augmented volume replaces the filled knot volume. The
[quantitative finite-sum proof](actual_all_circle_curvature_filling_limit.md)
contains the uniform contraction, Fourier-tail and joining-contour
estimates; the [elementary Newton bounds](all_circle_uniform_newton_bounds.md)
give an independent derivation of the graph-independent decay constants.
The [exact scalar proof](actual_main_meridian_exact_scalar.md) retains
the physical strand orientations and framing in (4).

## A geometric form of the numerical condition

At the complete auxiliary cusp the primitive shape is
\(2i c_v/(1-i\epsilon_v c_v)\), where \(c_v=1/d_v\).
The normalized length of a slope means its Euclidean length divided
by the square root of the cusp area. For the actual primitive filling
slope this gives
\[
 \mathcal L_v^2=\frac{d_v^2+n_v^2}{2d_v},\qquad
                 \mathfrak S=\frac12\sum_v\mathcal L_v^{-2}.
 \tag{20}
\]
Thus (5) is equivalently \(\sum_v\mathcal L_v^{-2}\le2^{-24}\).
This identity explains why high degree can compensate for a small
crossing power. The proof above establishes the completion for these
particular ordered exteriors; it does not import an unrelated
normalized-length criterion or classify all short fillings.

## The preferred cusp and the first correction

The remaining cusp belongs to the knot itself. Normalize its meridian
translation to one. Its preferred longitude, which has linking number
zero with the knot, then translates by a complex number
\(\tau_K\), the preferred cusp shape. This geometric normalization is
needed to interpret the first correction in the quantum profile.

Let \(x_e^*\) be the branch in (12) evaluated at
\(\boldsymbol\tau(1)\). The finite edge-insertion calculation retains
one further term:
\[
 \frac{F_N(q_N^s)}{F_N(1)A_N(s)H_N(s)}
 =1-\frac{\pi s^2}{N}\sum_e\cot(\pi x_e^*)
                 +O_{\mathcal T,\mathbf n,R}(N^{-2}).
 \tag{21}
\]
The [finite insertion calculation](actual_main_meridian_grouped_wire_packet.md),
Sections 5–6 and 8, gives an integrand independent of \(s\) multiplied
by \(1-\pi s^2\sum_e\cot(\pi x_e)/N+O(N^{-2})\), uniformly with
derivatives. At the nondegenerate joint saddle, the normalized
expectation of this coefficient differs from its critical value by
\(O(N^{-1})\). Its explicit factor \(1/N\) makes that an
\(O(N^{-2})\) error. The common saddle corrections cancel in the
ratio, and the other charges and contour terms are exponentially
smaller by the quantitative estimate. This proves the remainder in
(21) under the present summed criterion.

The geometric translation calculation gives, on the same filled branch,
\[
                   \tau_K=a(D)+2i\sum_e\cot(\pi x_e^*).
 \tag{22}
\]
This identification follows from the actual preferred longitude; it is
not a definition of the cusp shape from (21).

Let \(\lambda_{\mathrm{aug}}\) be the preferred main longitude in the
augmented exterior and \(\mu_K\) its meridian. For the fixed filling
integers retain the boundary word
\(\lambda_{\mathrm{fill}}=\lambda_{\mathrm{aug}}
\mu_K^{\sum_vp_v\ell_v^2}\), where \(\ell_v\) is the actual linking
number with crossing circle \(v\). Before the endpoint this is simply
a fixed curve on the unfilled main boundary. At \(c=1\), surgery
homology identifies it with the preferred longitude of the smooth
filled knot complement.

Here is why its translation formula applies beyond the initial
small-deformation neighborhood. The edge blocks form a
positive ideal triangulation of the original augmented exterior. Near
completeness, prescribing the main meridian logarithm and the primitive
auxiliary longitude logarithms determines its marked shape germ
uniquely. The [marked multicusp gluing theorem](general_marked_multicusp_gluing_rigidity.md),
Sections 2--3 and 5, proves precisely these mixed peripheral coordinates
and the corresponding decorated representation statement. Its
logarithmic gluing Jacobian has the form
\(A+B\operatorname{diag}(1/(z_j-1))\). The edge and peripheral rows
are Lagrangian, whereas positivity of the shapes gives
\(\Im(1/(z_j-1))<0\); pairing a supposed kernel vector with its
complex conjugate proves that the Jacobian is invertible.

Developing this triangulation with the earlier marked representation
and its actual cusp flags therefore identifies the two representation
germs. The exact circle-variable elimination identifies their retained
physical-edge labels by (12), before any edge is eliminated. The
[preferred-longitude face-word calculation](actual_main_meridian_preferred_cusp.md)
then supplies the translation
\(a(D)+2i\sum_e\cot(\pi x_e)\) for this fixed boundary word near
completeness. Both sides continue holomorphically on the small angular chart: the main meridian remains
a nonidentity parabolic, so the commuting longitude has a uniquely
defined translation in its unit-meridian frame. This ratio has no
logarithmic integer ambiguity. Their equality thus continues along the
whole positive charge path. At the smooth endpoint the
fixed word is the preferred longitude, giving (22). The same original
surgery homology gives exactly the integer
\(a(D)=-w(D)-\sum_vn_v\), with no unrecorded framing shear.

The [preferred-cusp continuation proof](actual_all_circle_preferred_cusp.md)
gives the representation comparison and peripheral calculation in full.

Put \(z=2\pi i s\) and
\[
 \mathcal H_N(z)=\frac{\sinh(z/2)}{N\sinh(z/(2N))},
                         \qquad\mathcal H_N(0)=1.
 \tag{23}
\]
Combining the exact factor (4), the expansion (21), and the geometric
identity (22) gives
\[
 \frac{F_N(e^{z/(2N)})}{F_N(1)\mathcal H_N(z)}
   =1+\frac{\tau_K z^2}{8\pi iN}
                         +O_{\mathcal T,\mathbf n,R}(N^{-2}),
                         \qquad |z|\le2\pi R<2\pi.
 \tag{24}
\]
All fixed derivatives have the corresponding limits on smaller disks.
The shape in this formula belongs to the filled knot complement, not
the complete augmented link. The exact scalar in (4) remains part of
the statement; its quadratic expansion is the integer contribution
to the preferred cusp in (24).


## The same limit from a pointed quantum A-operator

Fix a genuine all-level quantum A-operator \(P\) annihilating the
knot's reduced ADO family. Fix the finite initial vector \(c_0\) of
ordinary-color polynomials selecting that family. The
[pointed operator construction](actual_conway_pointed_quantum_a_volume.md),
Sections 2–3, forms the ordered recurrence row \(r_N(q)\) and proves
the exact identity
\[
 \mathscr P_N(P,c_0)
 =\operatorname{CT}_{t=0}
    \bigl[r_N(q_N(1+t))c_0(q_N(1+t))\bigr]=K_N(K).
 \tag{25}
\]
Here \(\operatorname{CT}\) extracts the constant Laurent coefficient
of the whole product. This retains the cancellations at singular
recurrence steps and the required derivatives of the fixed initial
data. It does not evaluate each singular factor separately.

Applying (6) to this identity gives
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|\mathscr P_N(P,c_0)|
                  =\operatorname{Vol}(S^3\setminus K).
 \tag{26}
\]
The condition is still (5), with the original knot and framing
qualifications. Thus the new quantitative class also has an operator
period on the left and its actual complement volume on the right.
The finite initial data remain essential. Identifying the selected
geometric factor of the classical symbol of \(P\) is a separate
problem; no such identification is assumed in this corollary.
