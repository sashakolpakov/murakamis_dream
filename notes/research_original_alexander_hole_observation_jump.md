# The observation-pole jump of an original Alexander-hole current

Private written proof, 18 November 2026.

The counterclockwise Alexander-hole contours in [K] occur with coefficient
\(+1\) in the original color formula. Their local continuation across the
observation pole can be computed exactly. The answer is a holomorphic
interior Cauchy term minus the canonical cutoff. Consequently the two-sheet
difference of this original hole term is the negative canonical minor
period. This fixes the local residue, its normalization, and its sign.

The holomorphic interior term is retained. No bound on its large-color
growth, or identification of a transported hole with a chosen physical
geometric cycle, follows from this calculation.

## 1. The original hole, with variable observation

Let \(v_*=\log\alpha\) be one logarithmic lift of the simple actual node
in [M]. Thus \(\alpha\ne0,1\), so \(v_*\ne0\). Use the global logarithmic
meridian \(v=\log Y\) and the local coordinate \(u=v-v_*\).
Choose a small disk \(D\) centered at \(v_*\), whose closure excludes
\(0\), the physical observation \(a_*=2\pi i\), and all other logarithmic
Alexander roots. It lies in the node chart of [M]. Let \(C=\partial D\)
be counterclockwise.

Choose \(R\ne0\) sufficiently small and the straight path
\(\gamma:0\to R\). The canonical series of [K] is jointly holomorphic
on a collar of \(C\) along \(\gamma\). The cutoff can be taken as
\(R=ir\), \(r>0\), with \(r\) as small as necessary, so this is also
one of the original physical contours in [K]. Choose it small enough
for the node formulas below. All these choices are independent of
the positive integer color \(L\).

Write \(\mathfrak b(v,\xi)\) for that actual canonical source, retaining
its original zero framing, normalization, and Borel histories. For
fixed \(L\ge1\), define on the actual collar
\[
 F_L(v)=\frac Lv\int_\gamma
                  e^{L(R-\xi)/v}\mathfrak b(v,\xi)\,d\xi.
 \tag{1}
\]
This is holomorphic in \(v\) on the collar; the exclusion of \(v=0\)
is explicit. For an observation \(a\ne0\), put \(h=a/L\).
The normalized original hole contribution in [K] is
\[
 H_{\rm out}(a)=\frac{e^{-LR/a}}{2\pi i}
                 \int_C\frac{F_L(v)}{v-a}\,dv,
                      \qquad a\notin\overline D.
 \tag{2}
\]
At \(L=N\), \(a=a_*\), this is precisely
\(\mathcal E_{N,r}(C)\) in [K], with coefficient \(+1\).
It is not a separately normalized period.

The same contour integral on the interior defines
\[
 H_{\rm in}(a)=\frac{e^{-LR/a}}{2\pi i}
                 \int_C\frac{F_L(v)}{v-a}\,dv,
                           \qquad a\in D.
 \tag{3}
\]
For each fixed \(L\), (3) is a single-valued holomorphic function on
all of \(D\). It uses only the source values on \(C\); no extension
of the density through its interior is being assumed. In particular
holomorphy of (3) does not assert a bound uniform in \(L\).

## 2. Exact observation-pole transfer

On the source collar, the canonical cutoff is
\[
 U_R(a/L,e^a)=\frac La\int_\gamma
                         e^{-L\xi/a}\mathfrak b(a,\xi)\,d\xi.
 \tag{4}
\]
The exact boundary identity is
\[
 \boxed{\qquad
 H_{\rm in}(a)-H_{\rm out}(a)=U_R(a/L,e^a).
 \qquad}
 \tag{5}
\]
Here the two Cauchy terms mean their analytic continuations to a common
collar. Equivalently, the inward continuation of the actual exterior
hole is
\[
                 H_{\rm out}^{\rm cont}=H_{\rm in}-U_R.
 \tag{6}
\]

To prove (5), take two nearby counterclockwise contours \(C_-\), \(C_+\)
inside the source collar, with \(C_-\) interior to \(C_+\).
The exterior Cauchy function continues across \(C\) using \(C_-\);
the interior one continues using \(C_+\). For \(a\) between them,
their difference is the residue of the single observation pole:
\[
 \frac1{2\pi i}\left(\int_{C_+}-\int_{C_-}\right)
                         \frac{F_L(v)}{v-a}\,dv=F_L(a).
 \tag{7}
\]
Multiplication by \(e^{-LR/a}\), followed by (1), gives
\[
 e^{-LR/a}F_L(a)
     =\frac La\int_\gamma e^{-L\xi/a}\mathfrak b(a,\xi)\,d\xi,
 \tag{8}
\]
which is (4). This proves the sign and every normalization factor.
In particular it is \(H_{\rm in}-H_{\rm out}\), rather than its negative,
that contains the positive observation residue.

The calculation is finite and exact at every integer \(L\). There is
no large-color limit, infinite Borel integral, or removal of a primitive
history in (5).

## 3. The actual two node sheets and their hole-current difference

Use the exact action and minor from [M], in the local coordinate \(u\):
\[
 \rho=\xi+S(u),\qquad
 \mathfrak b(v,\xi)=E(u,\rho)+\rho^{-1/2}A(u,\rho),
 \qquad A(u,0)\ne0.
 \tag{9}
\]
Both \(A\) and \(E\) are jointly holomorphic on a full small polydisk.
The original starting lift at \(\xi=0\) is
\[
                    \tau_0(u)^2=S(u).
 \tag{10}
\]
It is holomorphic in \(u\): \(S(u)=u^2s(u)\), \(s(0)\ne0\), and its
unit square root is chosen by the original canonical source.
The endpoint lifts are
\[
                 \tau_{R,\pm}(u)=\pm T(u),\qquad
                          T(u)^2=R+S(u).
 \tag{11}
\]
For small \(R\), the two zeros of \(R+S(u)\) are simple and lie
inside \(D\). Indeed \(u\sqrt{s(u)}\) is a local coordinate and reduces
that equation to \(R+w^2=0\). The disk and cutoff can be chosen so
both zeros are well inside \(C\).

For \(h\ne0\), define the local holomorphic primitive
\[
 \Phi_h(u,t)=2\int_0^t e^{-s^2/h}
                         \{A(u,s^2)+sE(u,s^2)\}\,ds.
 \tag{12}
\]
On the actual source collar, and then by continuation on the node
cover, the cutoff has the exact endpoint expression
\[
 U_{R,\pm}(h,u)
   =\frac{e^{S(u)/h}}h
       \{\Phi_h(u,\tau_{R,\pm}(u))-\Phi_h(u,\tau_0(u))\}.
 \tag{13}
\]
This is just (4) with \(d\xi=2\tau\,d\tau\). The paths lie in the
full minor chart, where the differential in (12) is holomorphic.
It therefore retains the original histories and has no additional
winding constant. On the collar the initial endpoint sheet is the
one continued from \(\xi=0\) along the original short path.

Continuation around one simple zero of \(R+S\) changes the endpoint
sign in (11), while leaving (10) fixed. Thus both values in (13) are
actual continuations of the same exterior collar source. On a smaller
central node disk, excluding the two endpoint zeros, both endpoint
choices are holomorphic. This is the same pair and orientation as [M].

Continue (6) along those same two paths, using the same \(h=a/L\).
Since \(H_{\rm in}\) is single-valued on \(D\), one obtains
\[
 H_{{\rm out},\pm}(a)
                    =H_{\rm in}(a)-U_{R,\pm}(a/L,u),
                 \qquad u=a-v_*.
 \tag{14}
\]
Consequently, with \(D_R=U_{R,+}-U_{R,-}\) in the original orientation,
\[
 \boxed{\quad
 H_{{\rm out},+}(a)-H_{{\rm out},-}(a)
                =-D_R(a/L,u)
                =-\frac{2L}{a}e^{LS(u)/a}
                   \int_{-T(u)}^{T(u)}
                          e^{-Lt^2/a}A(u,t^2)\,dt .
 \quad}
 \tag{15}
\]
This is an exact finite Gaussian period for the difference of two
continuations of an original \(+1\) hole term. A particular loop
changes \(+\) to \(-\) or the reverse; its increment has the corresponding
orientation. Equation (15) fixes the branch labels without ambiguity.

Where the closed facing-sector and small-\(S\) conditions of [M] hold
for \(h=a/L\), its uniform estimate also gives
\[
 H_{{\rm out},+}-H_{{\rm out},-}
   =-2\sqrt\pi\,(L/a)^{1/2}A(u,0)e^{LS(u)/a}
                                      \{1+O(L^{-1})\}.
 \tag{16}
\]
This statement is restricted to such compact local observation sets.
The exact identity (15) has no facing-sector requirement.
Neither formula is an asymptotic for one chosen exterior-hole value.

## 4. What cancels in the original color formula

In [K], the actual cutoff and this counterclockwise hole occur as
\(+U_R+H_{\rm out}\). Continue the original formula into the node chart.
Equations (14)--(15) give the exact cancellation
\[
                       U_{R,\pm}+H_{{\rm out},\pm}=H_{\rm in}.
 \tag{17}
\]
All remaining contours can be kept fixed away from this disk.
Their Cauchy integrals are holomorphic in \(a\) on it. The entire
scalar endpoint, with its original coefficient, is retained as well.
Thus no branch discontinuity of the finite-color polynomial has been
introduced: the residue term transferred from the hole cancels the
cutoff's branch difference.

This does not prove that the large-\(L\) geometric contribution cancels
in the scalar. In particular \(H_{\rm in}\) is an exact \(L\)-dependent
contour integral, whose growth has not been estimated here. Nor has
the scalar endpoint or another contour been bounded by this local
holomorphy argument.

## 5. Relation to a later physical observation

The residue in (7) is the local mechanism by which the literal
kernel \(L e^{L(R-\xi)/v}/[v(v-a)]\) transfers an observation term.
It gives a coefficient \(+1\) when the interior contour minus the
exterior contour is counterclockwise about \(v=a\). Equations
(6) and (15) show how that residue enters the original exterior hole.

For clarity, a canonical odd ribbon transported along a regular branch
has fibers \(\xi=t^2-S(v)\). If the small fiber is
\(-t_0\le t\le t_0\), applying the same residue calculation at any
regular observation gives its local minor period
\[
                  \frac2h e^{S(a)/h}
                  \int_{-t_0}^{t_0}e^{-t^2/h}A(a,t^2)\,dt .
 \tag{18}
\]
In (18), the continued \(S\) and \(A\) are written in the global
logarithmic coordinate; on the initial node chart this means
\(S(a-v_*)\) and \(A(a-v_*,t^2)\).
This algebraic kernel identity does not identify that ribbon with the
original hole cylinder. Its fiber endpoints are
\(\xi=t_0^2-S(v)\), whereas the latter has the fixed boundaries
\(\xi=0,R\). A contour transfer between them must retain those
relative boundaries, both banks of every continued cut, and any
remaining relative cycles. Caps lying in a holomorphic endpoint
graph have zero pullback of \(dv\wedge d\xi\), but their required
fillings and the resulting chain relation still have to be constructed.

The original fixed-\(\xi\) contour surrounding the two local branch
points is a nonbounding cycle in the local fiber. This can be checked
in the same actual node coordinates, without a model-source replacement:
write \(S=w^2\), with \(w=u\sqrt{s(u)}\). At \(\xi\ne0\) the cover
obeys \((\tau-w)(\tau+w)=\xi\). On the canonical lift of the outer
circle, choose the sign so \(\tau\) is near \(w\). For sufficiently
small \(\xi\), the nonvanishing function \(\tau-w\) is near
\(\xi/(2w)\) and has winding number \(-1\). A filling in this fiber
would contradict that nonzero winding. The other initial sign gives
the equivalent test with \(\tau+w\).
Its positive coefficient in [K] therefore does not, by itself, fix an intersection
number of a transported ribbon at \(a=2\pi i\). The proven assertion
here is the actual local crossing identity (5), including its complete
source normalization, and the exact compensation (15)--(17).
No global contour deformation or physical noncancellation is inferred.

## 6. Complete proof sources

| Label | Complete proof direct | SHA256 |
|---|---|---|
| K | notes/research_canonical_shift_current_cauchy_cycles.md | 4506e2020820221c3f303d2e9a709ccfcbae5f099598b7282e60cc00a8d2ff56 |
| M | notes/research_canonical_borel_regular_square_root_minor.md | 23b1e6cfc5dcb303af37d7470ab262225c1ced3ede9772f183ab813eff94e42a |

K supplies the literal original Cauchy kernel, positive hole orientation,
finite-color normalization, and constructed short-cutoff source collar.
M supplies the exact local regular minor, action cover, and original
finite Gaussian-period normalization. The Cauchy splitting, inward
continuation, and compensation of this original hole are proved above.
Formula (18) is a local residue calculation on any supplied regular
minor tube, not an unlisted premise asserting global transport.

Only written mathematics and complete source-text reads were used.
No mathematical programs, tests or builds were run. Frozen notes and
public manuscripts are unchanged.
