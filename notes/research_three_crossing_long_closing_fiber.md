# A long closing twist after two adjacent three-crossing blocks

Research deduction, 3 November 2026.

Closing either adjacent three-crossing piece by a sufficiently long
fixed signed twist gives a hyperbolic knot satisfying Kashaev's
original volume conjecture. The local boundary theorem supplies the
nonzero geometric coefficient, and the separate whole-period theorem
controls the rest of the closing trace.

For the original negative piece this settles all but finitely many
assignments \((2,2,p)\) of the original integer filling parameters,
with each outside carrier fixed. It does not settle arbitrary
assignments on that template.

## 1. The original words and the whole-period bound

Let \(R\) be the original crossing of two strands, \(T\) the physical
quarter-turn with its original ordered endpoints, and \(C\) the
cylindrical closure. Products are stacked in the original diagram
order. For \(\sigma\in\{1,-1\}\), put
\[
 P_\sigma=T\bigl(R^{3\sigma}T(R^{3\sigma})\bigr),\qquad
 K_{\sigma,c}=C(R^cP_\sigma),\qquad c\in\mathbb Z .
 \tag{1}
\]
The original quantum source is the ordinary boundary polynomial
\[
 F_{\sigma,N}(w)
   =\mathbf e(w)^TJM^{3\sigma}JM^{3\sigma}\mathbf e_0 .
 \tag{2}
\]
It retains the full quotient and its first normals. Fix all disk
frames, strand orientations, reduced cut, and half-twist carriers
of the original marked circle-tree construction.

Write \(M_0=\operatorname{Vol}(B_{\sigma})/(2\pi)\), where
\(B_\sigma\) is the partially filled exterior with its remaining
auxiliary cusp complete. The two signs have the same \(M_0\).
The [whole-period source theorem](research_three_crossing_whole_period_source.md)
gives angular coefficient \(1/4000\). In particular, for any fixed
small \(r>0\), with \([-2r,2r]\) inside the local boundary chart,
put \(\delta=(1-\cos r)/4000>0\). There are constants \(A,d\) such that
\[
 \sup_{r\le |t|\le\pi}|F_{\sigma,N}(-2\cos t)|
       \le A N^d e^{N(M_0-\delta)}
 \tag{3}
\]
for all sufficiently large integer \(N\).
Conjugation makes the two signs equivalent for this real bound.

The
[full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
supplies the even holomorphic expansion
\[
 F_{\sigma,N}(-2\cos u)
   =\varepsilon_{\sigma,N}A_\sigma(u)e^{NW_\sigma(u)}
       (1+O(N^{-1})),\qquad
 |\varepsilon_{\sigma,N}|=1,\quad A_\sigma(u)\ne0 .
 \tag{4}
\]
Its normalization is exactly
\(\varepsilon_{+,N}=\kappa^2\omega_N\),
\(A_+=C\) from that theorem, with conjugation for the negative sign.
The original marked geometric germ gives
\(-\Re W_\sigma''(0)>0\), and
\[
 2\pi\Re W_\sigma(0)=\operatorname{Vol}(B_\sigma),\qquad
 U_0=-2\pi W_\sigma'(u),\qquad V=2iu .
 \tag{5}
\]
These statements retain the original primitive curves; an outside
carrier has not yet been inserted.

## 2. The analytic inputs to the closing trace

After decreasing \(r\), the local expansion and negative real
curvature bound the real source near zero by a polynomial times
\(\exp N(M_0-a t^2)\), for some \(a>0\).
Combining this with (3) gives
\[
 |F_{\sigma,N}(-2\cos t)|
    \le A' N^{d'}e^{N\{M_0-c_1(1-\cos t)\}},
          \qquad -\pi\le t\le\pi,\quad c_1>0 .
 \tag{6}
\]
For example, choose \(c_1\) small enough to be bounded by the local
quadratic coefficient and by \(\delta/2\).

The degree in \(-2\cos u\) is at most \(N-1\). The harmonic-majorant
argument in equation (27) of
[the one-step theorem](research_uniform_large_power_turn.md)
therefore extends (6) to
\[
 |F_{\sigma,N}(-2\cos(x+iy))|
 \le A'N^{d'}\exp N\{M_0-c_1+c_1e^{-|y|}\cos x+|y|\}.
 \tag{7}
\]
To see the underlying normalization, write \(z=e^{iu}\) and multiply
the even trigonometric polynomial by \(z^{N-1}\).
On the unit circle its logarithmic bound has harmonic majorant
\(N(M_0-c_1+c_1\Re z)\). The maximum principle inside the disk gives
(7) for \(y\ge0\); evenness gives the other sign.

Away from a fixed neighborhood of \(x=0\), a sufficiently thin strip
absorbs the linear \(|y|\) cost into half the real gap. Near zero,
the holomorphic phase in (4), its evenness, and Young's inequality
give a quadratic estimate. Thus there are fixed \(c_2,B,h>0\) with
\[
 |F_{\sigma,N}(-2\cos(x+iy))|
 \le A''N^{d''}e^{N\{M_0-c_2(1-\cos x)+By^2\}},
 \qquad |x|\le\pi,\quad |y|\le h .
 \tag{8}
\]
All local phase bounds needed by the scalar closing theorem follow
from (4) on a smaller fixed disk. Markov's inequality on each fixed
outer spectral interval also bounds the first ordinary normal,
with the same exponential gap and a polynomial factor.
Consequently (3), together with the proved local theorem, supplies
every analytic input used in Section 7 of
[the fixed-domain closing theorem](research_fixed_domain_long_power_turns.md).
The preceding long-turn induction of that note is not needed for
this fixed input.

## 3. The closing deduction and its original filling parameters

**Theorem 1.** There is an integer \(B\)
such that every fixed \(c\) with \(|c|\ge B\), in either parity class
allowed by the chosen outside carrier, gives a hyperbolic knot
\(K_{\sigma,c}\) satisfying
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
          \log|\langle K_{\sigma,c}\rangle_N|
       =\operatorname{Vol}(S^3\setminus K_{\sigma,c}) .
 \tag{9}
\]
The limit uses all integer quantum levels. All twist powers are
fixed before \(N\) tends to infinity.

**Proof.** Apply the scalar closing proof to the literal full trace
\[
             Z_N=\phi_N(R^cF_{\sigma,N}).
 \tag{10}
\]
It supplies a unique small critical point \(u_c\) of
\[
 \mathcal V_{\sigma,c}(u)
       =W_\sigma(u)+\frac{ic}{4\pi}u^2-iu,
 \qquad
 W_\sigma'(u_c)+\frac{ic}{2\pi}u_c-i=0 ,
 \tag{11}
\]
and a nonzero asymptotic
\[
 Z_N=\varepsilon_{\sigma,N}C_{N,c}N^{3/2}D_{\sigma,c}
       e^{N\mathcal V_{\sigma,c}(u_c)}(1+O_c(N^{-1})),
 \qquad |C_{N,c}|=1 ,
 \tag{12}
\]
where
\[
 C_{N,c}=\exp\!\left(\frac{\pi i c(N-1)^2}{4N}\right),\qquad
 D_{\sigma,c}
 =i\sqrt{\frac2\pi}\,
    \frac{\sin u_c\,A_\sigma(u_c)}
      {\sqrt{-W_\sigma''(u_c)-ic/(2\pi)}}\ne0 .
 \tag{13}
\]
The input has no power of \(N\); the final trace contributes
\(N^{3/2}\). The scalar closing theorem retains all physical
values, normals, and higher Fourier charges.

For the geometric interpretation keep the actual outside carrier
\(\eta\) and write
\[
                     c=\eta-2p,\qquad p\in\mathbb Z .
 \tag{14}
\]
Inserting this carrier once changes (5) to \(U=U_0-i\eta u\).
Replace the final \(i\) in (11) by \(i\lambda\),
\(0\le\lambda\le1\). For sufficiently large \(|c|\) this charge
path stays in the marked positive geometric chart, with
\(\Im u_\lambda<0\) for \(\lambda>0\). Its exact peripheral equation is
\[
 U+pV=-2\pi\left(W_\sigma'(u)+\frac{ic}{2\pi}u\right)
                         =-2\pi i\lambda .
 \tag{15}
\]
Thus it fills the original primitive curve \(\mu+p\lambda_{\rm disk}\);
neither a multiple nor a shifted longitude has been substituted.
The notation \(\lambda_{\rm disk}\) distinguishes this curve from
the real charge parameter.

The two earlier filled slopes remain fixed throughout this path,
by the marked germ in
[the geometric branch theorem](research_three_crossing_pendant_geometric_branch.md)
and its mirror. The newly filled core has length
\(-2\Im u_\lambda\). The original positive-cell completion at
\(\lambda=1\) is therefore the actual hyperbolic filling.
Schläfli's formula and the absolute initial value (5) give
\[
 2\pi\Re\mathcal V_{\sigma,c}(u_c)
       =\operatorname{Vol}(S^3\setminus K_{\sigma,c}) .
 \tag{16}
\]
There is no uncalibrated real additive constant.

For completeness, the component test permits both parities of
the closing power. The inner odd block has the crossed pairing of
its four endpoints. A quarter-turn preserves that pairing.
Stacking the second odd block gives the vertical pairing; the
outer quarter-turn then gives the horizontal pairing of
\(P_\sigma\). Stacking \(R^c\) above this horizontal pairing
preserves it for every \(c\). The cylindrical closure joins its
two arcs into one component, with no internal closed component.
This proves that the filled diagram in (16) is the specified knot.
The reduced zero-framed invariant differs from (12) only by its
prescribed writhe unit. Equations (12) and (16) prove (9).
\(\square\)

For example, the original negative piece in the branch theorem has
inner carriers \(+1,+1\) and inner filling coefficients \(2,2\),
giving powers \(-3,-3\). Fixing an outside carrier \(\eta\) and
varying its original integer \(p\) in (14) is an infinite fiber of
the original filling lattice. The theorem settles every assignment
\[
                 (p_v,p_w,p_b)=(2,2,p)
                 \quad\hbox{with}\quad |\eta-2p|\ge B .
 \tag{17}
\]
The untreated values lie in the finite set
\[
 E_\eta=\{p\in\mathbb Z:|\eta-2p|<B\}
       =\mathbb Z\cap\left(\frac{\eta-B}{2},\frac{\eta+B}{2}\right),
                         \qquad |E_\eta|\le B .
 \tag{18}
\]
No assertion that these remaining values fail the conjecture is made.
The mirrored fiber has fixed inner coefficients \((-2,-2)\)
and the mirrored outside carrier. Covering both parity classes
means choosing the corresponding original outside carrier in each
class, not dropping the integral condition in (14).

This deduction treats one specified adjacent short pair and its
mirror. It does not settle arbitrary connected groups of short
powers or the full cofinite-template objective.

## 4. Arbitrarily many copies in the existing tree construction

The same piece can be used repeatedly as a terminal piece of an
ordered tree of tangles. This requires its whole-period estimate,
not merely the nonzero coefficient at the complete boundary.

**Corollary 2.** Enlarge the initial family of
[the hybrid theorem with mixed pendant pieces](research_hybrid_trees_with_mixed_pendant_seeds.md)
by the two original pieces \(P_+\) and \(P_-\) in (1).
There are finite integers \(M_*\ge3\) and \(B_*\ge2\) such that
the theorem remains valid with this enlarged family.
At every attaching vertex, including the final root, require
\[
                  m\ge M_*\quad\hbox{or}\quad |n|\ge B_* ,
 \tag{19}
\]
where \(m\) is the number of whole child pieces and \(n\) is the
original power at that vertex. The high-valence alternative permits
every fixed signed integer \(n\). The number and signs of the
new pendant leaves are arbitrary.

For every fixed finite tree satisfying (19) and the original
one-component knot test, the original reduced zero-framed
Kashaev invariant satisfies the volume conjecture along all
integer quantum levels. The constants \(M_*,B_*\) do not depend
on the number or placement of the new leaves, tree size, or depth.
The full tree and all its powers are fixed before the quantum
level tends to infinity.

**Proof.** The prior initial family already has common constants
for a nonzero local expansion of power \(N^0\), a bounded normalized
phase, positive real curvature, and the whole-period quadratic
strip bound. Equations (4), (5), and (8) give all these properties
for the two new pieces.

Choose one smaller radius \(R>0\) whose closed doubled disk lies
inside the old domains, the two new nonzero-amplitude domains,
and their marked geometric deformation charts. On this disk let
\[
\begin{split}
 a_3&=\min_{\sigma=\pm1,\ |u|\le2R}
                     \Re[-W_\sigma''(u)]>0,\\
 H_3&=\max_{\sigma=\pm1,\ |u|\le2R}
                     |W_\sigma(u)-W_\sigma(0)|<\infty .
\end{split} \tag{20}
\]
Take the minimum of the old and new curvature and strip-width
constants, the maximum of their normalized phase and quadratic
strip constants, and decrease the common angular loss if needed.
The fixed choice in Section 2 of the cited hybrid theorem can
then be repeated, including its bare-edge constants. Its explicit
threshold inequalities are eventually satisfied, giving finite
\(M_*,B_*\) before any particular tree is chosen.

The induction uses only this common class and the canonical
boundary degree \(N-1\); it does not inspect a child's internal
crossing formula. At a nonroot vertex it retains exactly
\[
 \phi_N^{(t)}
       \left[R^nK_N(t,u)\prod_{\nu=1}^{m}F_{\nu,N}(t)\right],
 \tag{21}
\]
and the final root omits \(K_N(t,u)\).
The input powers are \(N^0\), and the outgoing edge, trace and
Gaussian powers restore \(N^0\) after each nonroot operation.
The last trace has power \(N^{3/2}\).
The units of the new leaves are retained as
\[
 \varepsilon_{+,N}=\kappa^2\omega_N,\qquad
 \varepsilon_{-,N}=\overline{\kappa^2\omega_N}.
 \tag{22}
\]
At every new vertex they multiply by the original unit \(C_{N,n}\)
in (13), exactly as in the existing induction. They are not
absorbed into a new twist or discarded as a parity convention.

Geometrically, each \(P_\sigma\) is already the native marked
two-edge circle-tree pendant, with its original outgoing interface.
The geometric branch theorem and its mirror retain both internal
primitive filling curves, the free boundary periods (5), and the
positive deformation chart. No re-expression of its tangle or new
interface identification is required. The recursive marked
construction therefore attaches it in exactly the same way as
an old child. Every new carrier occurs once, every older filled
slope remains fixed, and the complete child volumes supply the
absolute constants in the subsequent Schläfli integrations.
The resulting action is the volume of the actual knot complement
under the unchanged global component and framing conditions.
\(\square\)

In this corollary each copy is a one-boundary pendant leaf.
It counts as one child at its attaching vertex; its two internal
short powers are not subject to (19). The statement does not
provide a two-boundary kernel for placing that pair at an arbitrary
internal position. The original global strand tracing must still
give one main knot component and no internal closed component.
Vertices outside the specified pieces remain subject to (19), so
the corollary does not give cofinite coverage on an arbitrary fixed
template.
