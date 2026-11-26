# Separating the geometric wire from its middle endpoint on filled paths

Private written proof, 17 November 2026.

The local cubic fold permits an endpoint Stokes change even inside
the positive edge domain. The actual integer filling equations impose
additional restrictions. We prove a phase separation criterion on
a whole fixed-height angle rectangle, then apply the established
height theorem to every edge of a same-sign filled path throughout
its full charge cube. The criterion concerns the original geometric
wire and the actual middle-Newton endpoint. It does not exclude
connections to other saddles, logarithmic lifts or source currents.

## 1. The original endpoint phase

Retain the original edge action \(\psi(t,u)\), normalized at
completeness by the finite Newton source, with
\[
 \psi_t=-r_t/\pi,\qquad \psi_u=-r_u/\pi,\qquad
 r_t=\operatorname{arsinh}\{\tan(t/2)\cos(u/2)\},
 \quad r_u=\operatorname{arsinh}\{\tan(u/2)\cos(t/2)\}.
 \tag{1}
\]
On the positive edge domain these are precisely the canonical
complete branches of [P]. The complete value \(\psi(0,0)\)
is real, as is its defining real factorial phase.

Write \(L=N-1-\lfloor N/2\rfloor\). The exact middle
polynomials [F](19), continued with \(H=it\), are
\[
 e_L(-2\cos t)=
 \begin{cases}
 \displaystyle\frac{2\cos(Nt/2)}
                    {N(\cos t-\cos(\pi/N))},&N\text{ even},\\[2mm]
 \displaystyle\frac{\sin(Nt/2)}
                    {N\sin(t/2)},&N\text{ odd}.
 \end{cases}
 \tag{2}
\]
For \(\Im t<0\), their growing factor is \(e^{iNt/2}\)
at both parities. The other exponential, every denominator
and its finite normalization remain in (2). In particular
the calibrated middle-endpoint action for the paired kernel is
\[
                  E_{\rm mid}(t,u)=\frac{i(t+u)}2.
 \tag{3}
\]
At a complete endpoint it is understood by continuation to
\(t=0\); the finite polynomial there remains (2), with its
removable odd expression evaluated. Thus define the actual
saddle-to-middle action difference
\[
                  \Delta(t,u)=\psi(t,u)-\frac{i(t+u)}2.
 \tag{4}
\]
No logarithmic constant is chosen to alter its imaginary part.

## 2. A fixed-height rectangle criterion

**Theorem 1.** Fix \(H,K\ge0\) with
\[
                 \tanh^2(H/2)+\tanh^2(K/2)<1.
 \tag{5}
\]
For \(0\le a,b<\pi\), put \(t=a-iH,\ u=b-iK\).
The principal returns in (1) give the continuation of the
original action throughout this angle rectangle. At every
point with \(a+b>0\),
\[
             \boxed{\quad -(a+b)<\Im\Delta(t,u)<0.\quad}
 \tag{6}
\]
At any positive geometric point in the rectangle this is its
original complete branch. The theorem does not assume that
every intermediate point of the rectangle is geometrically
positive.

**Proof.** First consider the convex open domain
\[
 {\cal D}=\{(t,u):0<\Re t,\Re u<\pi,\quad
                              \Im t,\Im u<0\}.
 \tag{7}
\]
Set \(A=\tan(t/2),\ B=\tan(u/2)\). Both tangents have
positive real and negative imaginary parts, so
\[
 \Im(1+A^2+B^2)<0.
\]
There is a single holomorphic square root
\[
                q=\sqrt{1+A^2+B^2},\qquad
                         -\pi/2<\arg q<0.
 \tag{8}
\]
Both cosines in (1) have positive real and positive
imaginary parts. Hence \(A\cos(u/2)\) and
\(B\cos(t/2)\) have positive real parts. Their principal
inverse hyperbolic sines are holomorphic, have positive
real parts, and satisfy
\[
                         -\pi/2<\Im r_t,\Im r_u<\pi/2.
 \tag{9}
\]
The square-root conventions agree exactly:
\[
              \cosh r_t=q\cos(u/2),\qquad
              \cosh r_u=q\cos(t/2).
 \tag{10}
\]
Indeed their squares agree algebraically, and each right
side has argument in \((-\pi/2,\pi/2)\), as does the
principal square root on the left. Differentiating gives
\[
                   \partial_u r_t=\partial_t r_u
                                  =-\frac{AB}{2q}.
 \tag{11}
\]
Thus the holomorphic one-form
\(-(r_t\,dt+r_u\,du)/\pi\) is closed on the convex domain
\({\cal D}\). It has a unique primitive after fixing its
real complete constant near \((0,0)\).

This primitive is the original \(\psi\) at every positive
point of \({\cal D}\). To verify the marking, the tangent
contraction \((A,B)\mapsto(\lambda A,\lambda B)\) from [P]
stays in the positive domain and in the same fourth tangent
quadrants for \(0<\lambda\le1\). Its angles stay in (7)
and approach completeness. The returns there are the same
principal returns, so the two primitives agree along this
path, with the same complete constant.

We next include the boundary of the fixed-height rectangle.
If \(q^2\) has zero imaginary part there, each tangent is
either real or purely imaginary. With both purely imaginary,
(5) gives \(q^2>0\). With one real and one purely imaginary,
\(q^2\ge1-\tanh^2(H/2)>0\), or the endpoint-swapped
inequality; with both real it is at least one. Thus \(q\)
never vanishes or reaches its cut on this rectangle.

The return arguments remain in the closed right half-plane.
An argument on its imaginary boundary is strictly between
\(-i\) and \(i\): at \(a=b=0\), for example,
\[
 \tanh(H/2)\cosh(K/2)<1
 \quad\Longleftrightarrow\quad
 \tanh^2(H/2)+\tanh^2(K/2)<1;
 \tag{12}
\]
the swapped inequality is identical. If the other height
is zero, the remaining factor \(\cos(b/2)\) only decreases
this modulus. A zero tangent gives zero. These are all
boundary cases. Consequently (9)--(11) extend regularly
to the entire rectangle, including zero heights.

At its corner \(t=-iH,u=-iK\), the action is real. In
fact the pure-height path \((-i\lambda H,-i\lambda K)\),
\(0\le\lambda\le1\), satisfies (5) throughout; both
returns are purely imaginary, so (1) has real differential
along that path. It starts at the real complete constant.
The value (3) is also real at this corner. Hence
\[
                        \Im\Delta(-iH,-iK)=0.
 \tag{13}
\]
Along the angle rectangle, with heights fixed, (1),(4),(9)
give the strict derivative bounds
\[
 -1<\partial_a\Im\Delta=-\frac{\Im r_t}{\pi}-\frac12<0,
 \qquad
 -1<\partial_b\Im\Delta=-\frac{\Im r_u}{\pi}-\frac12<0.
 \tag{14}
\]
Integrate first along either coordinate and then along the
other, starting at (13). If \(a+b>0\), both integrated
bounds are strict, proving (6). The extension at a boundary
height zero follows by the same regular formulas or continuity.
\(\square\)

This proof retains the actual middle phase even when it has
larger real part than the saddle phase. It does not use a
real-action dominance inequality.

## 3. Application to the actual integer-filled path family

Take any fixed finite selected path of original degrees at most
two, with at least one complete outside end, as in [C].
Fix its original integers \(n_v\ge3\), and let all charges
vary independently in \(0\le\chi_v\le1\). The full primitive
equations are
\[
 \sum_{e\ni v}r_{v,e}
                  =\frac{i n_v}{2}t_v-\pi i\chi_v.
 \tag{15}
\]
The established theorem [C] supplies the entire positive
charge cube with
\[
 t_v=a_v-iH_v,\qquad 0<a_v<\pi,\quad
                   0<H_v<23/20
 \tag{16}
\]
at every active vertex. A zero-charge or complete vertex
has \(t_v=0\). These are actual solutions of (15), not
independently selected endpoint angles.

The same source proves \(\cosh(23/20)<7/4\). Therefore
\[
 \tanh^2(H_v/2)
 =\frac{\cosh H_v-1}{\cosh H_v+1}<\frac3{11},
 \quad
 \tanh^2(H_v/2)+\tanh^2(H_w/2)<\frac6{11}<1.
 \tag{17}
\]
Theorem 1 applies at every edge and every charge vector:
\[
 \boxed{\quad
 \Im\{\psi(t_v,t_w)-i(t_v+t_w)/2\}<0
       \quad\text{whenever the edge has an active endpoint}.
 \quad}
 \tag{18}
\]
In particular the geometric wire and its canonical middle
endpoint never have equal imaginary action along this
actual family. At an all-complete edge they remain the
unchanged complete source.

The mirror family with \(n_v\le-3\) has
\(t_v^-=-\overline{t_v^+}\). The original return formulas
and real complete constant give
\[
 \psi(-\bar t,-\bar u)=\overline{\psi(t,u)},\qquad
 \Delta(-\bar t,-\bar u)=\overline{\Delta(t,u)}.
 \tag{19}
\]
Thus its active edges have the opposite strict sign in (18).
The two signs are applied to whole same-sign components;
no independent vertexwise conjugation is asserted.

There is also an already available stronger distance
statement for this family. The tangent-sector theorem
[C](30) puts every nonzero squared tangent in
\(-2\pi/3<\arg z<0\). Its closed convex cone contains
one, and an active tangent contributes in its interior, so
\[
                 -2\pi/3<\arg q_e^2<0
 \tag{20}
\]
on active edges. Moreover [O](10)--(11), with
\(A=\cos^2(t_v/2),B=\cos^2(t_w/2)\), proves
\[
                       |q_e^2|=|1/A+1/B-1|>1.
 \tag{21}
\]
Hence this filled path family never approaches the cubic
fold \(q_e^2=0\). Equations (20),(21) are direct consequences
of existing results. The new assertion (18) concerns the
calibrated full action difference, which is not determined
solely by the argument of \(q_e^2\).

## 4. What is and is not protected

A descending connection between the specified geometric
saddle and this specified endpoint requires equality of
their imaginary actions. Equation (18) excludes that
connection throughout the actual charge cube, including
regions where the endpoint is larger in real action.
It therefore rules out this particular endpoint mechanism
for changing the local saddle coefficient.

It does not establish a nonzero coefficient for the full
source or transport one through every possible event.
Other saddles, factorial-wall continuations, logarithmic
lifts, aliases, the high radical and the original angular
closing functional remain. The statement keeps the branch
in (1)--(4); no logarithmic period is discarded modulo
\(2\pi i\).

Nor do the quoted path theorems cover arbitrary branching
components or arbitrary mixed signs. The fixed-height
criterion applies to any supplied geometric edge satisfying
(5) in the stated angle quadrant, but those hypotheses
must be proved for a new filling family. The marked
degree-two \(0,\pm1\) moves and same-sign \(\pm2\) run
reductions retain boundary shifts and turns; they do not
by themselves place arbitrary short components in (15)--(16).
No new filling case or global noncancellation theorem is
inferred here.

## Direct sources

All complete direct texts were read in full and their used
implications checked at the following pins:

* [F: Actual finite middle polynomials and fold source](research_actual_low_newton_fold_packet.md),
  SHA256 849e626407ed9e9c985d86e10fc93c111a1f305cdc32cb470fafa08c6406edfb.
* [P: Original positive-edge branches and tangent contraction](research_positive_edge_global_monotonicity.md),
  SHA256 da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500.
* [C: Actual fractional-charge path family](research_positive_path_fractional_charge_cube.md),
  SHA256 d3806cebb427d94b795e85c5c089592c4646b49ffc01238673f4f9d04f7f3bac.
* [O: Original wire order on that family](research_positive_path_real_wire_order.md),
  SHA256 aaaf88d30be6be6737cd27e78669f2cb42bc9d0ad98315e1104616928038d0bb.

The phase maximum-principle, connected-short-geometry,
degree-two reduction, marked tangle-move and two-run
coverage texts were also read. Their separate source and
topology conclusions have not been enlarged.
Only written mathematics, source reads and metadata hashes
were used. No mathematical program, numerical experiment,
test or build was run. Frozen notes and public papers
are unchanged.
