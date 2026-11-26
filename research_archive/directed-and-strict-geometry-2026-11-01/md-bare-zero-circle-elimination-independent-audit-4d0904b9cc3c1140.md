# Independent audit of zero-circle elimination at bare junctions

1 November 2026.

## 1. Conclusion and checked version

I fully read md-bare-geometric-zero-circle-elimination.md through its
final version with SHA256
b84b6c7467501dad650add1217bf9cb18ebc0659585ba75c5be98521c0edeaa8.
I compared its source and marking statements directly with:

* actual_conway_general_mask_marked_filling, Sections 1, 3–6;
* actual_main_meridian_component_pressure, Sections 2–4;
* actual_main_meridian_regular_bare_trace, Sections 1–4;
* actual_all_circle_geometric_characteristic, native white maps,
  S14a–S14d, rational character reconstruction, and the filling anchor;
* the already defined strict-tree filtered action and its physical-edge
  insertion.

The written argument supports the proposed geometric extension near the
original complete strict optimizer and then at its sufficiently long
filled point. The new Section 5 collar lemma is essential: it compares
the actual ordered based boundary groups, rather than inferring geometry
from a local trace or a stationary action.

The normalization correction (22d) is necessary and correct. The only
additional prose correction I requested was that the two boundary
products have traces \(-\beta\) and \(-\gamma\), respectively; the author
has applied it. No further mathematical correction is requested.

This conclusion does not assert that the drilled all-circle diagram is
geometrically positive at the pulled-back representation, or that its
new circles satisfy a long-filling or quantitative source bound.
Neither assertion is used. The original strict-tree quantum asymptotic
is the analytic input; the enlarged diagram supplies an algebraic
representation model and an exact stationary elimination.

## 2. The action at arbitrary valence

At a bare junction, the physical incident labels satisfy
\[
 0<x_j\le\tfrac12,\qquad \sum_jx_j>1,
\]
with at most one half label. These are consequences of the old
complete physical-edge theorem and the strict whole-hub support;
hidden complementary resolution labels are not being classified as
physical low labels.

For \(\tau=-iy\), \(y>0\), all arguments of the logarithm in the
incidence action are positive:
\[
 2\cos(2\pi r)+2\cosh y>0.
\]
Differentiating directly gives
\[
 b_\tau(x,-iy)
 =\frac{i}{\pi}\arctan\!\left(k\tan\pi x\right),\qquad
 k=\tanh(y/2).
\]
The derivative with respect to \(y\) of the corresponding real
quantity is
\[
 \frac{1-k^2}{2\pi}
 \frac{\tan\pi x}{1+k^2\tan^2\pi x}>0
 \quad(0<x<1/2).
\]
At a half label the quantity is \(1/2\) and its derivative is zero.
The remaining at least two labels contribute a strictly positive
derivative. Consequently the equation with total equal to one has
exactly one \(0<k<1\), as claimed. Its angular Hessian is the negative
of the displayed positive derivative sum and is nonzero.

The finite positive Fourier coefficient rate is
\[
 B_x(r)=J(2x)-2J(x)-J(x+r)-J(x-r).
\]
Its derivative gives the unique tilted maximizer
\[
 r=\pi^{-1}\arctan(k\tan\pi x).
\]
The identity
\[
 b(x,-iy)=\max_r(B_x(r)+yr)
\]
has the right absolute constant: at \(y=0\), both sides equal
\(J(2x)-4J(x)\), and their derivatives in \(y\) equal \(r\).
The constraint \(\sum r_j=1\) therefore yields
\[
 V_D(\mathbf x)=
 \operatorname{stat}_\tau\left(\sum_jb(x_j,\tau)-i\tau\right).
\]
The local trace supplies this equality of rates independently of any
global invariant asymptotic. At both parities the first alias has
coefficient one, and the positive coefficient convolution plus the
finite difference inequality makes its rate the constrained maximum.
Higher aliases have strictly smaller rate in each strict compact
low window.

For \(x=1/2\), \(B_{1/2}(r)=0\), and the tilted maximum is \(y/2\).
This is also the direct value of \(b(1/2,-iy)\). Thus the half-label
limit is compatible with the action and its normalization. One need
not apply the regular-low finite trace theorem directly at its excluded
endpoint. First prove the real action identity below half and pass to
the analytic continuation. The incidence action is holomorphic near
the half tuple because \(y>0\); the old resolved hub is strict there
and has its analytic conditional maximum.

The derivative formula
\[
 \partial_{x_j}V_D
 =\log\frac{k^2+\cot^2\pi x_j}{1-k^2}
\]
follows from the envelope theorem. It agrees with the cubic
calculation and is valid for arbitrary valence.

## 3. The old longitude word and its normalization

The original mask proof (12)–(13) gives the complete world-frame
equalities for the top and bottom white maps across every unturned
product. Thus the side word is retained through the entire ordered
junction, not merely its trace or derivative.

With the raw representatives of (15),
\[
 \det(W_1^{-1}W_3)=R^2.
\]
Hence the determinant-one normalization is
\(P=R^{-1}W_1^{-1}W_3\), and direct multiplication gives
\[
 \operatorname{tr}P
 =2+\frac{(E-1)^2}{ER}
 =2-\frac{4\sin^2\pi b}{R}.
\]
Since \(R=(1+\kappa)^{-1}\) and
\[
 X_{\mathrm{met}}^2
 =\frac{1+\cot^2\pi b}{1+\kappa},
\]
this is \(2-4/X_{\mathrm{met}}^2\).

The ordinary output is \(b=1-x\), and
\(f'(b)=-\partial_xV_D\). Substituting the preceding envelope derivative
gives
\[
 X_{\mathrm{met}}^2=1-k^2,\qquad
 \operatorname{tr}P=-2\cosh y=-(Q+Q^{-1}).
\]
Thus the claimed \(\beta=4/X_{\mathrm{met}}^2-2\) uses the actual old
side word. It is not obtained by choosing a matrix having the desired
eigenvalues.

The turn covariance of the complete white maps transports this word
to the inverse disk word at the other end, preserving its trace.
Inversion records the prescribed disk orientation; it does not change
the old main-meridian flags.

## 4. Full ordered page tuples and the zero-coupon anchor

The inserted object is literally the identity two-strand coupon.
Its framed collar \(D^2\times[0,1]\) retains the two ordered access
paths and the boundary basepath. Therefore
\[
 a_{\mathrm{out}}=a_{\mathrm{in}},\qquad
 b_{\mathrm{out}}=b_{\mathrm{in}},\qquad
 P=ba
\]
hold in the based fundamental group before any representation.
Meridian filling kills the new auxiliary meridian and restores that
same collar. It neither twists an access path nor adds a power of
the boundary curve.

The old side transports must next be compared in the correct matrix
representatives. The raw universal maps have respective determinants
\[
 E,\quad E,\quad E(1-R)^2,\quad ER^2.
\]
Multiplying them respectively by
\[
 E^{-1},\quad E^{-1},\quad
 [E(1-R)]^{-1},\quad(ER)^{-1}
\]
makes every determinant \(E^{-1}\), exactly the native \(M=1\)
normalization. Only after doing this are the puncture factors
\(M^{-3},M,M,M\) equal to one. Without (22d), an SL trace computed
from the raw consecutive maps would have the wrong normalization.

The actual native punctures then give the two complete ordered
boundary pairs
\[
 (B,A)\longrightarrow(C^{-1},D^{-1}),\qquad
 (B^{-1},C^{-1})\longrightarrow(A,D).
\]
Their ordered products are \(AB\) and \((BC)^{-1}\), respectively.
These are exactly S14a–S14b of the all-circle chart, including the
inverses caused by looking from the opposite side of a puncture.
They are not a redefinition of the identity-collar equation as a braid.

To compare representations, pull back the old complete holonomy along
the actual meridian-filling quotient. Split the white faces by the
added disk cut. Pieces of an old white face retain its full old
transport, because crossing the additional cut and returning inserts
the new meridian, whose image is identity. The original prism identities
are precisely the world-frame version of this full-map statement.
The small corner loops reduce to the old consecutive white words.

The paths through the new pages intertwine both generators of the
displayed native boundary pair, by the based collar and van Kampen.
Both generators have trace two. Their products have traces
\(-\beta\) or \(-\gamma\), with \(\beta,\gamma\ge2\).
The pair irreducibility obstruction is respectively
\((\beta+2)^2\) or \((\gamma+2)^2\), hence is nonzero.
Therefore two intertwiners of the same full ordered pair differ only
by a scalar. The pulled-back page transport equals the native transport
in PGL. At an old odd seam the same comparison is made after the
already calibrated full Hurwitz action.

This proves equality of the white and shaded generators in their
original frames. It is the missing representation anchor; a phase,
similarity, or equal-character calculation alone would not prove it.
The product framing fixes the arbitrary-valence order without commuting
the child factors.

## 5. The folded edge \(E=-1\)

The edge trace equations yield
\[
 E+E^{-1}=\frac{4-\beta\gamma}{\beta+\gamma+4}.
\]
The full white maps retain \(E\), rather than only this symmetric
combination. At the possible half wire \(E=-1\), the quadratic in
\(E\) can be ramified over the auxiliary parameters. The note correctly
does not claim it has a simple root.

The character denominators remain nonzero: \(E\ne1\),
\(\beta,\gamma\ge2\), and \(\beta+\gamma+4>0\). In particular the
two-generator pair remains irreducible. The full stationary system is
the appropriate local coordinate system at this point.

For each added circle its angular Hessian is nonzero. Eliminating those
angular variables has exactly \(V_D\) as its Schur complement in the
physical wire variables. Combining this with the original strict
conditional wire Hessian proves nondegeneracy of the enlarged system.
At a sufficiently long original filling this remains true by analytic
continuation. No division by the derivative of the folded edge
quadratic is required.

## 6. The nonparabolic germ and the longitude identity

The original filtered main-meridian action adds
\[
 \sum_{e\in\mathcal E_T}
 [2J(x_e)-J(x_e+t)-J(x_e-t)]
 +\frac{\pi i a(D)}2t^2.
\]
The inserted zero coupon changes neither the physical edge set nor
\(a(D)\). The added angular variable is eliminated exactly by the
identity in Section 2, including its constant. Hidden unturned
resolution wires do not acquire a new main-meridian insertion.

Every added auxiliary longitude has \(Q>1\) at the old complete point,
so \(Q^2\ne1\) persists nearby. Its meridian commutes with that
semisimple longitude; similarity one therefore forces a projectively
identity meridian. Thus the reconstructed enlarged representation
factors through the actual original group, not only through its
peripheral eigenvalue equations.

The old complete anchor, together with the marked local deformation
coordinate theorem, identifies this branch with the original
augmented geometric germ as the original auxiliary longitudes vary.
The sufficiently long original filling lies on the same branch.
At that filled point the original auxiliary longitudes are also
noncentral, so their prescribed slope words are projectively identity.
The main-meridian germ is the geometric germ of the original knot.

The all-circle squared longitude identity is rational on its integral
source variety. It can be evaluated at this regular representation,
including a folded edge, without using an individual simple-root
edge chart. The new zero fillings contribute no surgery exponent,
and the original filled-knot Seifert sign selects the negative lift.
Consequently the proposed formula retains precisely the original
physical edges:
\[
 L_{\mathrm{geom}}(M)
 =-M^{a(D)}\prod_{e\in\mathcal E_T}
             \frac{M^2-X_e(M)}{1-M^2X_e(M)}.
\]

The extension uses the rational identities beyond the neighborhood
where all newly added \(Q\)'s equal one. Its applicability there is
supplied by the explicit regular reconstruction and complete anchor,
not by an assertion of positivity for the newly drilled cells.

No public file was edited during this audit.
