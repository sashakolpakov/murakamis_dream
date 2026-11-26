# A product domain and exact wire contour through a positive source point

Private written proof, 16 November 2026.

Fix a positive configuration of the original same-index circle-tree
edge geometry. There is a product of angular domains, independent of
the level, which contains every full real angular interval and this
configuration, and on which all stationary wire branches are single
valued, even and holomorphic. The domains narrow near the angular
endpoints; fixed-depth rectangular domains generally cannot do this.

The reciprocal factorial divisor theorem then gives an exact original
source contour through this entire stationary graph. Its wire endpoints
stay fixed, so no moving-wire seam current is introduced. A coherent
local Morse segment can be included. This is a reachability theorem
for a representative of the whole source, not an estimate on its
connectors or a proof of a surviving geometric coefficient.

## 1. The original stationary relation

Let a finite graph have angular variables \(t_v\), with

\[
 \mathcal S=\{t:|\Re t|<\pi\},\qquad
 a_v=\tan(t_v/2),\qquad
 \mathcal A=\mathbb C\setminus
       \bigl(i[1,\infty)\cup-i[1,\infty)\bigr).
 \tag{1}
\]

The maps \(t\mapsto\tan(t/2)\) and \(a\mapsto2\arctan a\)
are inverse biholomorphisms between these domains. The inverse is
the branch through zero. Loops and repeated edges are allowed.
Fixed outside angular parameters may be included in the geometric
statements and then held fixed. Every variable used in the positive
whole-phase Morse conclusion is assumed incident to at least one edge.

For a same-index edge \(e=vw\), the original unsummed phase is

\[
 F_e(x;t,u)=b(x,t)+b(x,u),\qquad
 b(x,t)=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),
 \quad J'(z)=\Log(2\sin\pi z).
 \tag{2}
\]

Branches in (2) are the continued original ones. The pinned
unsummed-source calculation gives

\[
 q_e^2=1+a_v^2+a_w^2,\qquad
 \cot(\pi x_e^*)=q_e,\qquad
 H_e=-F_{e,xx}(x_e^*)
   =\frac{2\pi q_e(1+q_e^2)^2}
          {(1+a_v^2)(1+a_w^2)}.
 \tag{3}
\]

Fix a configuration \(a_v^*\in\mathcal A\) at which every
original edge is positive. The exact positive-edge criterion is

\[
 \Re q_e>
 \sqrt{(\Re a_v^*)^2+(\Re a_w^*)^2},
 \qquad q_e(0,0)=1.
 \tag{4}
\]

No filling equation is needed until a geometric critical point of
the whole phase is specified. In the source application below, the
traced target angles have negative imaginary parts.

## 2. Independent tangent contractions and a product neighborhood

**Lemma 1.** If an original edge is positive at \((a,b)\), it
remains positive at \((\lambda a,\mu b)\) for all

\[
                         0\le\lambda,\mu\le1.
 \tag{5}
\]

**Proof.** Write \(a=A+i\alpha\), \(b=B+i\beta\), and

\[
 X=A^2+B^2,\qquad Y=\alpha^2+\beta^2,
 \qquad C=A\beta-B\alpha.
 \tag{6}
\]

The pinned positive-edge theorem proves that, for \(X>0\), (4)
is equivalent to \(C^2<X\); this inequality also excludes a
nonpositive real value of \(1+a^2+b^2\). For \(X=0\), the
criterion is \(Y<1\). If \(X>0\) and \(\lambda\mu>0\),

\[
 \lambda^2\mu^2 C^2
 <\lambda^2\mu^2(A^2+B^2)
 \le\lambda^2A^2+\mu^2B^2.
 \tag{7}
\]

If \(X=0\), independent contractions decrease \(Y\).
When one contraction is zero, the remaining endpoint belongs to
\(\mathcal A\). The one-complete-end edge is positive there:
if its tangent has nonzero real part, \(C=0<X\); if it is purely
imaginary, membership in \(\mathcal A\) gives modulus less
than one. Both zero endpoints give the complete point.
This proves every case. \(\square\)

This is an independent-coordinate strengthening of the archived
simultaneous contraction. It is not a path of solutions of fixed
primitive filling equations.

Set

\[
 K_v=\mathbb R\ \cup\ [-a_v^*,a_v^*].
 \tag{8}
\]

The second set is the straight complex line segment. It lies in
\(\mathcal A\). Sign changes do not change the positivity
criterion in (6), so Lemma 1 applies to any pair of points in
the two finite segments.

**Theorem 2.** There are symmetric star-shaped open sets
\(U_v\subset\mathcal A\), containing \(K_v\), such that for
every edge and every \((a,b)\in U_v\times U_w\),

\[
                      1+a^2+b^2\notin(-\infty,0].
 \tag{9}
\]

Consequently the angular domains

\[
                     V_v=2\arctan U_v\subset\mathcal S
 \tag{10}
\]

are symmetric and simply connected, contain \((-\pi,\pi)\)
and \(t_v^*\), and have bounded imaginary parts. On their product
all the functions in (3) have globally defined branches satisfying

\[
 \Re q_e>0,\qquad 0<\Re x_e^*<\tfrac12,
 \qquad H_e\ne0.
 \tag{11}
\]

They are even in each independent endpoint angle. The branches
agree with the original positive branches at the target. All these
domains are chosen before \(N\).

**Proof.** On segment times segment, (9) follows from Lemma 1.
If \(a\) is real and \(b\in\mathcal A\), a nonpositive real
value of \(1+a^2+b^2\) would require \(b^2\) real. For real
\(b\) the sum is positive. For purely imaginary \(b\), its
modulus is less than one, and the sum is again positive.
Thus (9) holds on \(K_v\times K_w\).

Here is a neighborhood construction which also treats the unbounded
real tails. For small \(\epsilon>0\), let

\[
 U_v=\{a:|\Im a|<\epsilon\}
       \ \cup\ \{a:\operatorname{dist}(a,[-a_v^*,a_v^*])
                                      <\epsilon\}.
 \tag{12}
\]

Each of the two sets is convex and contains zero, so the union is
star shaped and symmetric. Choose \(\epsilon<1/4\) and smaller
than the positive distance of all the finite segments from the
inverse-tangent cuts. Then \(U_v\subset\mathcal A\).

The second set in (12) is uniformly bounded, say by \(M\), after
an initial choice of \(\epsilon\le1/4\). If both arguments lie
in the horizontal strips, then

\[
 \Re(1+a^2+b^2)
       \ge1-2\epsilon^2+(\Re a)^2+(\Re b)^2>0.
 \tag{13}
\]

If one argument lies in a bounded segment neighborhood and the
other in a horizontal-strip tail with \(|\Re a|>R\), choose
\(R^2>M^2+2\). The same real-part calculation gives positivity.
The remaining pairs lie in a fixed compact set. Their limiting
skeleton pairs satisfy (9), so their discriminants have positive
distance from the closed nonpositive real ray. Decreasing
\(\epsilon\) once more proves (9) for all these pairs. There
are finitely many edges, so one common choice works.

The principal square root now gives \(\Re q_e>0\) throughout.
The map

\[
 x(q)=\frac{1}{2\pi i}\Log\frac{q+i}{q-i},\qquad x(1)=1/4,
 \tag{14}
\]

is the inverse of \(\cot\pi x\) from the right half-plane
to \(0<\Re x<1/2\), with the logarithm specified by this
normalization. It supplies \(x_e^*\). The factors \(q_e\),
\(q_e\pm i\), and \(1+a_v^2\) do not vanish, proving the
last assertion in (11). The discriminant and its principal root
are even in the endpoint angles; uniqueness of (14) proves the
same for \(x_e^*\) and \(H_e\). Independent contraction to zero
identifies the branches at the positive target.

Finally, the inverse tangent has bounded imaginary part on the
horizontal strip in (12), because \(\epsilon<1\), and on the
bounded segment neighborhood away from its cuts. Thus each \(V_v\)
has bounded imaginary part. Its simple connectedness and symmetry
follow from (1) and (12). \(\square\)

The product domains need not consist entirely of positive edge
configurations. Equation (9), rather than positivity everywhere,
is what is proved on their mixed real-axis/segment neighborhoods.

## 3. Exact factorial admissibility

Use \(D=N-1\), \(N\ge2\), and the actual interpolation

\[
 B_N(x,t)=\frac{N}{
 G_N(D/2-Nx+Nt/(2\pi))
 G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{15}
\]

The pinned divisor theorem, derived from the original gamma
product, states

\[
 \operatorname{ord}_{z=k}G_N(z)=\lfloor k/N\rfloor,
 \qquad k\in\mathbb Z,
 \tag{16}
\]

and there are no other zeros or poles. In particular \(1/G_N\)
is holomorphic on \(\Re z<N\). Its zeros at \(z=-r\),
\(r\ge1\), have order \(\lceil r/N\rceil\).
This is an existing exact divisor result, not a new choice of
factorial interpolation.

**Lemma 3.** Put

\[
 b_N=-1/(2N),\qquad I_N=[b_N,b_N+1].
 \tag{17}
\]

For every compact subset of

\[
           \Re x\in I_N,\qquad |\Re t|<\pi,
 \tag{18}
\]

both \(B_N(x,t)\) and \(B_N(D/N-x,t)\) are holomorphic on
a neighborhood, with no restriction on the finite imaginary
heights.

**Proof.** The unshifted argument obeys
\(\Re(Nx)\le N-1/2<N\). For either shifted argument,

\[
 \Re(D/2-Nx\pm Nt/(2\pi))
       \le N/2+N|\Re t|/(2\pi)<N.
 \tag{19}
\]

Equation (16) proves the assertion. Reflection
\(x\mapsto D/N-x\) preserves \(I_N\), proving the other
orientation. Strictness of the bounds on a compact set supplies
the asserted open neighborhood. \(\square\)

In particular the entire graph in Theorem 2 is pole-free for the
exact factorials. Their values can be zero. Negative real
factorial arguments and the exact zeros in (16) are not removed
from the source, and no nonvanishing Stirling amplitude is inferred
across them. The statement concerns holomorphy of the reciprocal
factorials, not a globally nonvanishing logarithm of \(B_N\).

## 4. A representative of the original whole source

First take a closed network whose traced vertices and paired wires
are those of the pinned joint-lens theorem. At each vertex retain
its fixed signed power \(R^{n_v}\), its original full-Hermite
coupon and any specified polynomial spectator. Direct and reversed
halfwires use exactly their original arguments. The geometric
stationary assignment in Theorem 2 is asserted for the same-index
edges of (2); a reversed kernel is not silently assigned that phase.

Set

\[
 a_N=\pi-\frac{\pi}{2N},\qquad
 \eta=(-1)^D,\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 C_{N,n}=e^{\pi i nD^2/(4N)}.
 \tag{20}
\]

Choose full lower angular arcs \(\Gamma_{v,N}\subset V_v\)
from \(-a_N\) to \(a_N\), passing through \(t_v^*\) when
\(\Im t_v^*<0\). They can be chosen with horizontal tangent
at the target. Such arcs exist: in tangent coordinates the
neighborhood (12) contains the full real interval and the lower
radial arm to \(a_v^*\). Two nearby sides of that arm, joined to
the real spine, give a simple lower arc; a small local adjustment
passes through the target with the stipulated tangent. Apply the
biholomorphism (1), and make that last tangent adjustment in the
open angular domain. The endpoints remain fixed. The arc may
extend beyond their real coordinates but remains in \(\mathcal S\).

Together with its reflected upper arc, each lower arc encloses
exactly the original physical angular grid, once. There are no
additional grid poles in \(\mathcal S\). Thus the full-grid
lens identity of the pinned source remains valid on these arcs.
The odd-level simple spectral node and every double-node normal
have their original contributions.

Fix real wire heights \(h_e\) and write

\[
 A_{e,N}=b_N+ih_e,\qquad B_{e,N}=b_N+1+ih_e.
 \tag{21}
\]

For an edge assigned its stationary graph, use the broken path

\[
 \mathcal L_{e,N}(\mathbf t):
       A_{e,N}\longrightarrow x_e^*(\mathbf t)
                       \longrightarrow B_{e,N}.
 \tag{22}
\]

Both segments lie in \(\Re x\in I_N\), by (11), and depend
holomorphically and evenly on their angular variables. Keep any
other wire on its original horizontal interval. Parameterize each
path on \([0,1]\), with its midpoint at \(1/2\).

**Theorem 4.** Replacing every selected wire interval by (22)
in the joint factorial-lens integral preserves the entire original
source. In particular, for unit coupons the exact traced-network
scalar is

\[
 Z_N=\mathfrak c_N
  \int_{\prod_v\Gamma_{v,N}}
  \int_{\prod_e\mathcal L_{e,N}(\mathbf t)}
     \Omega_{{\rm fac},N},\qquad
 \mathfrak c_N=N^{|E|}\prod_{v\in V}
                   \frac{-N^2C_{N,n_v}}{\pi i}.
 \tag{23}
\]

Here \(\Omega_{{\rm fac},N}\) is exactly the pinned joint top
form, with its fixed coordinate order. It contains every actual
halfwire factor (15), all polynomial spectators, and
\(\prod_v\sin t_v\,W_N(t_v)e^{in_vNt_v^2/(4\pi)}\).
For a nonunit coupon its original cosine factor is retained.
Any pre-existing external framing normalization is unchanged.

**Proof.** The original horizontal joint integral is exact by
the pinned lens theorem. Lemma 3 extends its holomorphic factorial
domain from the closed substrip used there to all of (18).
For fixed wire values the factorial and polynomial spectators are
even and holomorphic on \(\mathcal S\), so its residue proof applies to the full lower
arcs just constructed. The original physical values and first
normals, and the ordinary free boundary polynomials when present,
have not changed.

Now fix a tuple of angular points on these arcs. Interpolate
pointwise between the horizontal path \(b_N+r+ih_e\) and (22).
The real part remains in the convex interval \(I_N\), and the
two endpoints stay at (21). Lemma 3 makes this a compact pole-free
homotopy. Cauchy's theorem therefore preserves that wire integral.
Apply the argument successively to every wire and then integrate
the angular variables. All chains are compact at this fixed level.
In the pullback of the joint top form, angular derivatives of a
wire path wedge to zero against the retained full angular volume
form, so this fiberwise calculation is exactly the stated joint
integral.

Thus no moving seam current occurs. The result also agrees with
the fixed-face relative-source identity: both wire endpoint faces
remain fixed throughout. Broken paths are piecewise smooth chains;
no embedding assumption on an intermediate wire path is needed.
This proves (23). \(\square\)

The result also holds as an identity in ordinary free boundary
polynomials when those ends retain the cardinal representative,
as required by the original compiler. It does not identify the
asymptotic phase of that free polynomial with a factorial phase.
Accordingly the stationary interpretation of a wire with such a
free end requires its own boundary-phase input; the exact contour
identity itself does not.

## 5. Coherent Morse segments and their limitation

For a compact angular product in Theorem 2, the holomorphic unit
\(H_e\) has a coherent square root, fixed by the original positive
value at completeness. A parameter Morse construction can be made
uniformly on a neighborhood of this compact product.

For precision put \(A=\cos^2(t/2)\), \(B=\cos^2(u/2)\),
\(z(x)=\sin^2\pi x\). Near \(x=x_e^*\), use the logarithm
equal to zero there in

\[
 F_{e,x}(x)=\Log\frac{(A-z(x))(B-z(x))}{z(x)^2}.
 \tag{24}
\]

All factors are units on the graph: besides \(\sin\pi x_e^*\ne0\),
the two differences equal \(A^2/(A+B)\) and \(B^2/(A+B)\).
Integrating (24) from \(x_e^*\) defines the original phase
difference \(F_e(x)-F_e(x_e^*)\), without resetting its critical
constant. Division by \((x-x_e^*)^2\), followed by the coherent
square root and the inverse function theorem, gives

\[
 x=X_e(\xi;\mathbf t),\qquad X_e(0;\mathbf t)=x_e^*,
 \quad F_e(X_e(\xi);\mathbf t)
             =F_e(x_e^*;\mathbf t)-\xi^2/2.
 \tag{25}
\]

The maps are even in each angular variable. Compactness gives a
common \(\rho_N>0\) such that \(X_e(\xi;\mathbf t)\) is
defined for \(|\xi|\le\rho_N\) on a neighborhood of all
the angular paths and stays strictly inside the wire strip.
Replace (22) by

\[
 A_{e,N}\longrightarrow X_e(-\rho_N;\mathbf t),\qquad
 \xi\in[-\rho_N,\rho_N]\longmapsto X_e(\xi;\mathbf t),
 \qquad X_e(\rho_N;\mathbf t)\longrightarrow B_{e,N}.
 \tag{26}
\]

The two connectors are straight. The same convex-strip homotopy
proves (23) for this path. At a positive whole-phase critical
point, horizontal angular tangents together with the real
\(\xi_e\) directions give precisely the adapted local contour
of the pinned unsummed-source theorem.

The radius \(\rho_N\) may shrink as the full angular paths
approach their moving endpoints. A separate fixed compact
neighborhood of the target has a fixed positive phase-Morse radius,
because its phase and Hessian do not depend on \(N\). No assertion
is made that this larger radius works over the whole product of
full lenses, or that its actual factorial amplitude is uniformly
nonzero.

In particular, (26) is a literal segment in a representative of the
full finite source. Its two connectors, all other angular portions,
all exact factorial zeros and the complete Hermite trace kernels
remain in (23). There is no estimate showing that these terms are
smaller than its geometric local contribution, or that their
coherent sum cannot cancel that contribution.

## 6. Why a rectangular stationary graph is generally unavailable

The pinched product construction cannot be replaced by an arbitrary
fixed-depth full-width rectangle. For an edge with two independent
angles, set \(t=s-ih\), \(u=-s-ih\). Direct trigonometry gives

\[
 1+\tan^2(t/2)+\tan^2(u/2)
 =\frac{4-(\cosh h-\cos s)^2}{(\cosh h+\cos s)^2}.
 \tag{27}
\]

For \(0<h<2\operatorname{arsinh}1\), this vanishes at
\(s=\arccos(\cosh h-2)\in(0,\pi)\). The discriminant
has nonzero derivative in either independent angular coordinate,
since \(\partial_t q^2=a(1+a^2)\ne0\) there. A local
holomorphic square root is impossible. Circling this divisor
exchanges \(q\) with \(-q\), hence \(x\) with \(1-x\)
near the merging stationary value \(x=1/2\).

More exactly, a rectangle with real half-width \(a_N\) and height
\(T\) contains such a point whenever

\[
 T>h_N:=\operatorname{arcosh}(2+\cos a_N)
          =2\operatorname{arsinh}\!\left(\sin\frac{\pi}{4N}\right).
 \tag{28}
\]

Thus every fixed \(T>0\) fails for all sufficiently large \(N\).
The construction of Theorem 2 avoids this divisor by narrowing the
angular neighborhoods near \(\pm\pi\). It concerns the actual
stationary relation, not a singularity of the finite cardinal
source, which remains holomorphic. No fold-transport coefficient
is inferred from the algebraic exchange of its two stationary
branches.

## Direct sources and author readback

- [Positive edge geometry](research_positive_edge_global_monotonicity.md):
  the exact positivity criterion, tangent characterization, original
  branches and the archived simultaneous contraction. Complete read
  retained at SHA256
  `da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500`.
- [Unsummed original phase](research_unsummed_network_phase_coercivity.md):
  (1)--(4), (25)--(30), same-index scope, stationary equation,
  Hessian and local adapted contour. Complete text reread at SHA256
  `b5441bb508d3ffad3274e38dda2d6aeb099d08ae2ab043a0d12c25234e4a1e1e`.
- [Exact factorial divisor](research_factorial_rectangle_divisor_criterion.md):
  Section 1, the specified canonical factorial and its entire divisor.
  Complete text read at SHA256
  `462b8c22c73f73b12152bca96cf6636708dcf153c2cbc2751458454827b3ddf8`.
- [Joint full-Hermite lens source](research_joint_factorial_lens_relative_source.md):
  the exact top form and prefactor, free-boundary convention, full
  physical normals and relative primitive for fixed coordinate faces.
  Complete author read retained and used implications reread at SHA256
  `a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54`.

All work here is written mathematics. No mathematical program,
numerical computation or test was run. The final complete proof
and all directly used source implications were reread before freezing.
