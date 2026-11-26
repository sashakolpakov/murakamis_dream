# The full boundary source of a subtree with zero crossing powers

Research theorem, 2 November 2026. A connected set of zero-power
vertices can be evaluated in the primitive Newton coordinates of its
original finite expression. These coordinates remain regular when the
imaginary-angle edge description reaches an endpoint. The resulting
theorem applies to every selected subtree whose original vertex degrees
are at least three. No bound on its size, and no degree condition beyond
three, is needed for the analytic statement.

The source in the theorem is the original finite polynomial, with all
internal and boundary indices, both level parities, and all closing
derivatives retained. The theorem gives a nonzero holomorphic boundary
asymptotic and a uniform bound away from its complete boundary value.
The geometric interpretation of the stationary action is proved
separately in
[the strict Conway geometry of the zero-filled region](research_zero_subtree_conway_geometry.md).
That proof also identifies the original remaining filling curves.

## 1. The source and the complete Newton action

Let \(T\) be a finite tree and \(S\) a nonempty connected proper
set of its vertices. Every selected crossing power is zero. Assume
that each selected vertex has original degree \(d_v\ge3\), counting
edges to vertices outside \(S\). Let \(b\) be the number of edges
leaving \(S\); then
\[
 b=\sum_{v\in S}d_v-2(|S|-1)\ge |S|+2\ge3.
 \tag{1}
\]
Each such edge has a distinct outside endpoint, because \(T\) is
a tree. Its angle \(u_\ell\) remains an independent variable.

Set \(D=N-1\) and
\[
 S_r=\prod_{j=1}^r2\sin(\pi j/N),\qquad
 e_r(z)=S_r^{-2}\prod_{j=0}^{r-1}
       \left(2\cos\frac{(2j+1)\pi}{N}-z\right).
 \tag{2}
\]
The full Newton algebra is \(\mathbb C[z]/(P_N)\), where
\[
 P_N(z)=\prod_{j=0}^{D}
       \left(z-2\cos\frac{(2j+1)\pi}{N}\right).
\]
Its original closing functional is
\[
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{3}
\]
Repeated roots in \(P_N\) are not separated or discarded.
The kernel and selected source are
\[
 K_N(t,u)=\sum_{r=0}^{D}e_r(-2\cos t)e_r(-2\cos u),
 \tag{4}
\]
\[
 Z_{S,N}(\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[
  \prod_{vw\subset S}K_N(t_v,t_w)
  \prod_{\substack{\ell=vw\in\partial S\\v\in S}}
                       K_N(t_v,u_\ell)
 \right].
 \tag{5}
\]
This normalization is part of the theorem. No extra power of \(N\)
or framing scalar is introduced in passing to the Newton expression.

The exact pairing \(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\)
shows that contracting an internal kernel reverses Newton
coefficients. Thus (5) is exactly a finite tree of Newton products
and reversals, with boundary coefficients
\[
 c_{N,r}(u)=e_r(-2\cos u).
 \tag{6}
\]
Resolve the products into binary products, and delete only the forced
final product by its exact complementary pairing. There are \(b-2\)
retained products. Their coefficient is
\[
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}},
 \qquad \max(i,j)\le r\le i+j\le D,
 \tag{7}
\]
and zero otherwise. All nonzero coefficients are positive.

The expression with low boundary leaves has a strict real state.
Indeed its reduced junction tree has the original selected vertices,
one reversal on every internal edge, and no flagged boundary leaf.
The reduced-junction criterion in
[the Newton support proof](../papers/newton-calculus/supports.tex)
applies because every junction degree is at least three.
Let \(P\) be its closed real polytope. At a leaf,
\(0\le a\le1/2\); at a product,
\(\max(x,y)\le z\le x+y\le1\); reversals retain the equation
\(x+y=1\); the closing pair is complementary.

Put
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
 \qquad g(a)=J(2a)-4J(a),
 \tag{8}
\]
\[
 m(x,y,z)=J(x+y)+J(z)-J(x)-J(y)
                 -J(z-x)-J(z-y)-J(x+y-z).
 \tag{9}
\]
The complete action \(\mathcal A\) is the sum of \(g\) over
its \(b\) boundary leaves and \(m\) over its \(b-2\)
retained products. The strict Newton variational theorem in
[the variational proof](../papers/newton-calculus/variation.tex)
gives a unique strict maximizer \(y_*\), with a negative definite
Hessian in primitive coordinates. Write
\[
 F_0=\mathcal A(y_*),\qquad a_\ell^*=a_\ell(y_*).
 \tag{10}
\]
In particular \(0<a_\ell^*<1/2\). Internal physical edge indices
need not be below \(1/2\); no such restriction is imposed in \(P\).

## 2. The whole-boundary theorem

For \(x\) near a strict leaf index and \(u\) near zero, define
\[
 B(x,u)=\int_0^x\log(2\cos2\pi s+2\cos u)\,ds-2J(x),
 \tag{11}
\]
using the branch real at \(u=0\). Then \(B(x,0)=g(x)\).
In the primitive Newton coordinates put
\[
 F(y,\mathbf u)=
       \sum_{\ell=1}^{b}B(a_\ell(y),u_\ell)
       +\sum_{\text{retained products}}m(x(y),y'(y),z(y)).
 \tag{12}
\]
Here \(y'\) denotes a product input, not a derivative of the
primitive vector \(y\). All wire maps in (12) are the original
affine maps in the chosen binary expression.
Let \(y(\mathbf u)\) be the holomorphic stationary point near
\(y_*\), and set
\[
 W(\mathbf u)=F(y(\mathbf u),\mathbf u).
 \tag{13}
\]

**Theorem.** For every fixed selected subtree satisfying the assumptions
of Section 1, there is a complex polydisk about zero on which
\[
 Z_{S,N}(\mathbf u)=
 N^{-3(b-1)/2}A(\mathbf u)e^{NW(\mathbf u)}
                              (1+O(N^{-1})).
 \tag{14}
\]
The error is uniform and holomorphic, with all fixed derivatives on
smaller polydisks. The functions \(W,A\) are independent of \(N\),
holomorphic, and separately even in the boundary angles. The amplitude
is nonzero after shrinking the polydisk, and \(A(\mathbf0)>0\).
The selected action and boundary Hessian are
\[
 W(\mathbf0)=F_0,\qquad
 W_{u_\ell u_j}(\mathbf0)=
 -\delta_{\ell j}\frac{\tan(\pi a_\ell^*)}{2\pi}.
 \tag{15}
\]
For some \(c,C,\varepsilon>0\) and \(q\), one also has
\[
 |Z_{S,N}(\mathbf u)|\le C N^q
 \exp N\left[
 F_0-c\sum_{\ell=1}^b(1-\cos\operatorname{Re}u_\ell)
       +C\sum_{\ell=1}^b(\operatorname{Im}u_\ell)^2\right]
 \tag{16}
\]
whenever \(|\operatorname{Im}u_\ell|<\varepsilon\).
Both parities and all sufficiently large integer levels are included.

Formula (14) is about (5) itself, not a model with only positive
boundary coefficients or only low internal indices. The proof first
uses positivity at complete boundary angles to control its complement,
then uses exact holomorphic interpolation for its contributing terms.

## 3. The primitive lattice and the exact normalization

Keep one integer coordinate for every boundary leaf output and every
retained product output. There are \(b+(b-2)=2b-2\) such labels
before closure. A reversal replaces a label \(r\) by \(D-r\).
The two subtrees meeting at the closing pair are disjoint, so their
complementary relation eliminates one output coordinate with
coefficient \(1\) or \(-1\). Thus there are
\[
 K=2b-3
 \tag{17}
\]
free integer coordinates, with no residual congruence condition.
Every original wire has the exact form
\[
 r_w=N L_w(k/N)+\delta_w,\qquad k\in\mathbb Z^K,
 \tag{18}
\]
where \(L_w\) is integral affine and \(\delta_w\) is a fixed
integer. The constants \(\delta_w\) retain the \(-1\) in
\(D=N-1\); they are not dropped in the amplitude.

Choose a small rectangular window in these primitive coordinates about
\(y_*\). All its proper inequalities have fixed positive slack.
For sufficiently large \(N\), every point of the ordinary grid
\(N^{-1}\mathbb Z^K\) in the window is therefore an exact
admissible state after reconstruction by (18), at both parities.
No sublattice or parity-dependent covolume remains. The final pairing
has coefficient exactly one; it does not contribute a missing
Gaussian or normalization factor. All original factors \(N^2\)
in (3) have already been used in the exact identity (5) and the
pairing that produced (7).

## 4. Exact interpolation of a boundary coefficient

Use the normalized factorial interpolation \(G_N\) proved in
[the factorial construction](../papers/conway-asymptotics/factorial.tex).
It satisfies
\[
 G_N(r)=S_r,\qquad
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),
 \tag{19}
\]
and is holomorphic and nonzero on \(-1<\operatorname{Re}z<N\).
On fixed compact subsets of \(0<\operatorname{Re}x<1\),
\[
 G_N(Nx+\delta)=
 N^{1/2}(2\sin\pi x)^{\delta+1/2}e^{NJ(x)}
                       (1+O(N^{-1})),
 \tag{20}
\]
uniformly with fixed derivatives and bounded fixed complex offsets.
The branches in (20) are positive on the real interval.

Put \(s=u/(2\pi)\). The required interpolation is
\[
 \mathcal E_N(r,u)=
 \frac{G_N(D/2+Ns)G_N(D/2-Ns)}
 {G_N(D/2-r+Ns)G_N(D/2-r-Ns)G_N(r)^2}.
 \tag{21}
\]
For every integer low index \(r\), it is exactly
\(e_r(-2\cos u)\), not just an asymptotic interpolation. Indeed,
\[
 2\cos\frac{(2j+1)\pi}{N}+2\cos u
 =4\cos\left(\frac{(j+1/2)\pi}{N}+\frac u2\right)
     \cos\left(\frac{(j+1/2)\pi}{N}-\frac u2\right),
\]
and each product of cosine factors is a descending sine product with
upper argument \(D/2\pm Ns\). Iterating (19) gives (21).
The same identity holds for small complex \(u\) by holomorphy.

At strict indices all arguments of (21) lie in compact subsets of
their regular strips after division by \(N\). Notice the exact
half-offset \(D/2=N/2-1/2\), present at either parity. In (20),
this offset cancels the half power of \(2\sin\pi x\) in each
midpoint factorial. Consequently, if \(r=Nx+\delta\),
\[
 \mathcal E_N(Nx+\delta,u)=
 N^{-1}\frac{e^{\delta B_x(x,u)}}{2\sin\pi x}
                      e^{NB(x,u)}(1+O(N^{-1})).
 \tag{22}
\]
To check the phase and its absolute constant directly, the expression
from (21) is
\[
 J(1/2+s)+J(1/2-s)
 -J(1/2-x+s)-J(1/2-x-s)-2J(x).
 \tag{23}
\]
The first two terms cancel by \(J(1-z)=-J(z)\), with its real
normalization. Differentiation in \(x\), together with its value
zero at \(x=0\), identifies (23) with (11). Thus (22) has no
unspecified additive action constant. Its prefactor is independent
of the level parity.

## 5. The complete summand and its offsets

Interpolate (7) by replacing each factorial by \(G_N\). This agrees
exactly at the reconstructed integer labels. For a gate with leading
wire coordinates \((x,y,z)\), its unshifted density is
\[
 \rho_\mu(x,y,z)=
 \left[
 \frac{(2\sin\pi(x+y))(2\sin\pi z)}
 {(2\sin\pi x)(2\sin\pi y)(2\sin\pi(z-x))
       (2\sin\pi(z-y))(2\sin\pi(x+y-z))}
 \right]^{1/2}.
 \tag{24}
\]
All these arguments are strictly between zero and one on the chosen
window. If its three wire offsets are \(\delta_i,\delta_j,\delta_r\),
its full density is
\[
 \rho_\mu(x,y,z)
       e^{\delta_i m_x+\delta_jm_y+\delta_rm_z}.
 \tag{25}
\]
Its power of \(N\) is \(N^{-3/2}\).

Multiply (25) over the \(b-2\) retained gates and multiply
\[
 \frac{e^{\delta_\ell B_x(a_\ell,u_\ell)}}
             {2\sin\pi a_\ell}
 \tag{26}
\]
over the \(b\) boundary leaves. Denote this explicitly normalized
product by \(\rho(y,\mathbf u)\), with all wires and offsets
given by (18). At zero boundary angles it is strictly positive.
Equations (20)–(26) give the interpolated full summand
\[
 N^{3-5b/2}\rho(y,\mathbf u)e^{NF(y,\mathbf u)}
                                      (1+O(N^{-1})).
 \tag{27}
\]
The estimate and its fixed derivatives are uniform on a fixed complex
neighborhood of the window. The interpolation is exact on its full
primitive integer grid before (27) is used.

The negative definite real Hessian \(F_{yy}(y_*,\mathbf0)\)
gives \(y(\mathbf u)\) by the holomorphic implicit function
theorem. Define the amplitude by the actual density
\[
 A(\mathbf u)=
 \frac{(2\pi)^{K/2}\rho(y(\mathbf u),\mathbf u)}
      {\sqrt{\det[-F_{yy}(y(\mathbf u),\mathbf u)]}}.
 \tag{28}
\]
The square root is positive at zero and then continued holomorphically.
This specifies the endpoint and offset normalization of (14).

## 6. The finite lattice correction and the local asymptotic

Move the faces of the real window by at most \(1/N\) to half-grid
positions. Its complete real boundary has a fixed action gap because
the unique maximum lies inside it. In each primitive coordinate, use
the exact residue kernel \(\pi N\cot(\pi Nz)\), whose residue
is one at \(z=j/N\). Enclose the retained interval by its rectangle
at fixed small imaginary heights \(\pm\epsilon\).

On a vertical half-grid side the cotangent has modulus at most one.
On the horizontal sides it is
\(\mp i+O(e^{-2\pi N\epsilon})\). The complete phase is real
on real coordinates. An imaginary displacement in the fixed complex
tube therefore changes its real part by at most \(C\epsilon^2\).
Choose \(\epsilon\) before the boundary-angle disk so that this
cost is less than both one quarter of the window boundary gap and
\(\pi\epsilon\). Then shrink the angle disk. Evenness gives an
additional cost \(O(\|\mathbf u\|^2)\), and the strict gaps
persist. Every vertical face and every nonconstant cotangent mode is
exponentially smaller than the stationary value.

Iterating over all \(K\) primitive coordinates replaces the finite
sum by \(N^K\) times its integral, with an exponentially smaller
error. The two constant horizontal terms have weights \(1/2\)
each; their sum is one, not an extra factor of two per coordinate.
Primitivity from Section 3 supplies density one for this lattice.

Translate the local integral to the parallel real contour through
\(y(\mathbf u)\). Its connecting faces retain the same strict
gap. On a fixed ball about that point, the real part of
\(-F_{yy}\) remains positive definite. Gaussian integration gives
(28). Odd terms have zero Gaussian integral; the next surviving
terms give relative error \(O(N^{-1})\). This is uniform on a
complex angle polydisk, and Cauchy's formula gives the derivative
claims. The power of \(N\) is
\[
 N^{3-5b/2}N^{K}N^{-K/2}
        =N^{3-5b/2+(2b-3)/2}=N^{-3(b-1)/2}.
 \tag{29}
\]
This proves (14) for the finite window. Positivity of \(\rho\)
and the Hessian determinant proves \(A(\mathbf0)>0\).

## 7. Every term outside the window

First restrict only the boundary indices to be low, while leaving all
internal labels unrestricted. Every summand then has the positive
Newton gate coefficients (7), and for real boundary angles,
\[
 |e_a(-2\cos u)|\le e_a(-2),\qquad 2a<N.
 \tag{30}
\]
The complete zero-angle rate of each such summand is uniformly
\(\mathcal A\), with error \(O(\log N)\), including all
support endpoints. This follows from the uniform factorial estimate
and \(B(x,0)=g(x)\). The unique global maximum of
\(\mathcal A\) is strictly inside the window. Compactness and
(30) therefore bound every low-boundary term outside it, uniformly
for all real boundary angles, by
\[
 C N^q e^{N(F_0-\delta_1)}
 \tag{31}
\]
for some \(\delta_1>0\). The estimate includes high internal
indices, whether inside or outside their former edge-kernel range.
In this comparison the compact polytope is naturally scaled by
\(D=N-1\), whereas the primitive window uses \(k/N\).
The two normalized coordinate vectors differ by \(O(N^{-1})\)
uniformly on the fixed support. Choose a smaller fixed window about
the maximum whose closure lies inside the retained window. A state
outside the retained window remains outside this smaller one after
the displacement, so its compact gap applies at all sufficiently
large \(N\).

The remaining terms have a high boundary index. The
[high-boundary theorem](research_zero_subtree_high_boundary_gap.md)
applies to every unflagged selected tree with degrees at least three,
without the regular-height assumption. Its arbitrary-array estimate
uses low comparison weights \(e_a(-2)\) and high comparison
weights one. The full polynomial interval bound for a high Newton
basis element supplies only a polynomial factor, and the positive
comparison theorem has a strict loss for every high boundary band,
with all internal labels unrestricted. It gives
\[
 \sup_{\mathbf u\text{ real}}
 |\text{terms with a high boundary index}|
              \le C N^q e^{N(F_0-\delta_2)}.
 \tag{32}
\]
The reference action in that theorem is exactly (8)–(10), not an
action inferred from the imaginary-angle description.

Every boundary spectral degree is at most \(N-1\). Polynomial
continuation of (31) and (32) therefore preserves a strict exponential
gap on a sufficiently small complex boundary polydisk. Choose it
also small enough that \(\operatorname{Re}W\) stays closer to
\(F_0\) than this gap. The error is then exponentially smaller
than the nonzero local expansion in Section 6. This proves (14) for
the full source (5), uniformly holomorphically.

## 8. The boundary Hessian and the whole real torus

Every boundary coefficient and every interpolated boundary phase is
even in its angle. Hence \(F_{y u_\ell}(y,\mathbf0)=0\), and
the stationary-wire Schur correction vanishes at zero. Directly
from (11),
\[
 B_{uu}(x,0)=
 -\int_0^x\frac{ds}{1+\cos2\pi s}
             =-\frac{\tan\pi x}{2\pi}.
 \tag{33}
\]
This proves (15), including its strict negativity.

Within the retained window, every boundary leaf index lies in a fixed
compact subinterval of \((0,1/2)\). Its midpoint product has the
uniform real-angle estimate
\[
 |e_a(-2\cos u)|\le C N^q e_a(-2)
       \exp\left[-N\frac{\sin(2\pi a/N)}{4\pi}
                              (1-\cos u)\right].
 \tag{34}
\]
This is the full-circle estimate used in the isolated zero-power
proof. The coefficient in (34) has a positive lower bound on the
window. Multiplying it over the \(b\) leaves and summing positive
complete weights proves a strict angular loss for its contribution.
The complementary estimates (31) and (32) have a fixed gap for every
real angle. Since the angular sum is bounded by \(2b\), reducing
its coefficient incorporates both complements. This proves (16) on
the real torus.

Near a complete real boundary point, (14), holomorphy and (15) give
(16) with a quadratic imaginary-angle cost. On the compact real
complement, the strict angular gap persists on a thin complex strip
by polynomial continuation on finitely many products of real spectral
intervals. Reducing the angular constant again incorporates that
complement; periodicity gives the stated whole strip. This proves
all assertions of the theorem.

## 9. Comparison with the regular imaginary-angle proof

Suppose additionally that the minimizing imaginary-angle configuration
is regular. The earlier
[regular low-index theorem](research_regular_zero_subtree_low_source.md),
[internal high-index gap](research_zero_subtree_internal_high_gap.md),
and [high-boundary gap](research_zero_subtree_high_boundary_gap.md)
then give another holomorphic expansion of the same exact source,
with the same power of \(N\) and a positive complete amplitude.
The internal-high proof identifies its complete rate with \(F_0\).

These two phases and amplitudes agree as holomorphic germs; this is
stronger than equality of their boundary Hessians. Write the two
expansions with phases \(W_1,W_2\), amplitudes \(A_1,A_2\),
and their uniform holomorphic relative errors. After shrinking the
polydisk, the source and both amplitudes are nonzero for all large
\(N\). Taking its logarithmic derivative and dividing by \(N\)
gives
\[
 \frac1N\frac{\partial_{u_\ell}Z_{S,N}}{Z_{S,N}}
       =\partial_{u_\ell}W_j+O(N^{-1})\qquad(j=1,2).
 \tag{35}
\]
The derivative estimates follow from Cauchy's formula for the uniform
holomorphic remainders. Letting \(N\) tend to infinity shows
\(dW_1=dW_2\). Their complete values are both \(F_0\), so
\(W_1=W_2\). Dividing either expansion by their common exponential
and power of \(N\), then taking the limit, gives \(A_1=A_2\).
Thus (28), with its affine offsets, has exactly the normalization of
the earlier contour calculation on their overlap.

For two adjacent trivalent vertices, the imaginary-angle method reaches
a shared edge index \(1/2\). The present proof is unaffected: the
unique Newton optimizer is strict in its own original product and
leaf inequalities, and no inequality requiring that internal physical
index to be below \(1/2\) has been added. The theorem therefore
crosses that particular coordinate failure. It still does not by
itself identify \(2\pi F_0\) with the volume of the original
partially filled manifold, or prove a volume limit after further
nonzero fillings. Those steps are supplied by the separate
[marked strict Conway argument](research_zero_subtree_conway_geometry.md)
and [long-filling assembly](research_connected_short_filling_clusters.md#10-a-volume-theorem-after-further-long-fillings).

## 10. An explicit normalization at a three-edge star

The smallest case gives a direct check on the affine offset in (28).
For one selected trivalent vertex, use primitive coordinates
\((x,y,z)\), with the first two leaves multiplied to output \(z\)
and the third leaf paired at the root. The phase at complete boundary
angles is
\[
 F(x,y,z;\mathbf0)=g(x)+g(y)+g(1-z)+m(x,y,z).
 \tag{36}
\]
The exact third leaf label is \(D-r_z=N(1-z)-1\), so its offset
is \(-1\). All other chosen offsets are zero. The stationary point is
\[
 x=y=a=\frac{\arctan2}{\pi},\qquad z=1-a.
\]
Here \(\sin\pi a=2/\sqrt5\), \(\cos\pi a=1/\sqrt5\),
and \(g'(a)=2\log\cot\pi a=-\log4\). The third leaf
therefore contributes the essential factor
\(e^{-g'(a)}=4\) to the density.

Substituting these trigonometric values in (24)–(26) gives
\[
 \rho(y_*,\mathbf0)=\frac{125\sqrt2}{256},
 \qquad
 \frac1\pi F_{yy}(y_*,\mathbf0)=
 \begin{pmatrix}
 -25/2&-25/4&25/4\\
 -25/4&-25/2&25/4\\
 25/4&25/4&-25/2
 \end{pmatrix}.
 \tag{37}
\]
The determinant of the negative displayed matrix is \(15625/16\).
Since \(K=3\), formula (28) yields
\[
 A(\mathbf0)=
 \frac{(2\pi)^{3/2}(125\sqrt2/256)}
      {\pi^{3/2}(125/4)}=\frac1{16}.
 \tag{38}
\]
This agrees with the independent exact-trace asymptotic for the
degree-three zero-power vertex. Dropping the \(-1\) in the closing
label would remove the factor four and give the wrong coefficient.

## 11. The adjacent trivalent pair and a finite reproduction

For two adjacent selected trivalent vertices, there are four boundary
leaves. Put \(B_N(t)=K_N(t,0)\) at complete boundary angles.
The exact original contraction is
\[
 Z_{S,N}(\mathbf0)=
       \sum_{i=0}^{D}\phi_N(e_i B_N^2)^2.
 \tag{39}
\]
Equivalently, it is the sum of squares of all the Newton coefficients
of \(B_N^2\). Resolve the two products with a common output index
\(r\). The five primitive coordinates are the four leaf labels and
this common index; their affine offsets are all zero. The complete
phase is
\[
 F=\sum_{j=1}^{4}g(a_j)+m(a_1,a_2,r)+m(a_3,a_4,r).
 \tag{40}
\]
Its stationary point and value are
\[
 a_1=\cdots=a_4=a=\frac{\arctan\sqrt2}{\pi},
 \qquad r=\frac12,
 \qquad F_0=4g(a)+2m(a,a,1/2)
          =3.8343901862419081236\ldots.
 \tag{41}
\]
This is a strict Newton state: each product input is below its output,
the output is below the sum of its inputs, and their sum is below one.
The physical shared edge reaches the fold of the alternative
edge-kernel coordinates, but no proper Newton inequality is an equality.

In the coordinate order \((a_1,a_2,a_3,a_4,r)\), direct
differentiation gives
\[
 \frac{F_{yy}}{\pi\sqrt2}=
 \begin{pmatrix}
 -27/4&-9/4&0&0&3\\
 -9/4&-27/4&0&0&3\\
 0&0&-27/4&-9/4&3\\
 0&0&-9/4&-27/4&3\\
 3&3&3&3&-8
 \end{pmatrix},
 \qquad
 \det\left(-\frac{F_{yy}}{\pi\sqrt2}\right)=6561.
 \tag{42}
\]
The density is \(\rho=81\sqrt2/512\). Formula (28) consequently
gives
\[
 A(\mathbf0)=2^{-29/4},\qquad
 Z_{S,N}(\mathbf0)=
       2^{-29/4}N^{-9/2}e^{NF_0}(1+O(N^{-1})).
 \tag{43}
\]

The standalone
[normalization script](../experiments/check_zero_subtree_newton_normalization.py)
checks (37)–(43) and evaluates both original finite sources:

```sh
python3 experiments/check_zero_subtree_newton_normalization.py --output repro/results/research-zero-subtree-newton-normalization.json
```

It checks the scaled Hessian determinants and their positive principal
minors with exact rational arithmetic. It also checks the exact
normalizations \(A_{\mathrm{star}}^2=1/256\) and
\(A_{\mathrm{pair}}^4=2^{-29}\), using the rational squared densities.
The stationary gradients, full Hessians and density formulas are
evaluated independently from the \(J\)-linear actions.

For the finite values, the script reuses the complete kernel at every
original derivative-trace node. It computes every
\(\phi_N(e_i B_N^2)\), including high indices, before summing (39).
For the star, direct evaluation of \(\phi_N(B_N^3)\) is also
compared with its independent pairing expansion. Each finite value is
recomputed at a higher precision. The
[saved results](../repro/results/research-zero-subtree-newton-normalization.json)
use 100 decimal digits and a second calculation at 130 digits:

| Level \(N\) | Star: finite value / leading term | Trivalent pair: finite value / leading term |
|---:|---:|---:|
| 24 | 1.07171235 | 1.13276400 |
| 25 | 1.06881655 | 1.12722417 |
| 48 | 1.03566663 | 1.06488808 |
| 49 | 1.03493469 | 1.06353395 |
| 96 | 1.01778119 | 1.03207040 |
| 97 | 1.01759733 | 1.03173596 |

These finite ratios check normalization and parity behavior. Their
observed convergence is a numerical diagnostic; the uniform asymptotic
and its error estimate are proved in Sections 3–8, not inferred from
the table. No hyperbolic-volume comparison is made by this script.
