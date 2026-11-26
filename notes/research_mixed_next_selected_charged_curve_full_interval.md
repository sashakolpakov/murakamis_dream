# The selected charged cubic curve on the full frequency interval

Private phase theorem, 9 November 2026. The original selected charged
critical point continues uniquely and without degeneracy from the
half-frequency endpoint to zero frequency. It remains in a fixed
subrectangle of the already guarded inner-three phase domain. This
locates the entire candidate saddle family, including its logarithmic
lift and action, without extending the complete quantum packet beyond
its proved source domain.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used.

## 1. Original branch and statement

Use the original selected inner action
\(S(u)=S_3(0,u)\) of
[the cubic continuation theorem](research_mixed_next_inner_three_cubic_continuation.md).
Put
\[
 \mathcal U_+=\{u=a-ih:0\le a\le\pi/2,\ 0\le h\le1/2\},
 \qquad c(u)=\cos(t_*(u)/2).
\tag{1}
\]
That theorem constructs \(c,S\) holomorphically on a neighborhood
of the whole closed rectangle, with their original constants and
logarithmic lifts. Its equations (8),(9),(13),(15) give
\[
\begin{gathered}
 4c^3-3c-i(4c^2-1)=\cos(u/2),\\
 \Re c>3/4,\qquad 1/6<\Im c<1/3,\qquad
 |c|^2<127/144<1,\\
 S'(u)=-\pi^{-1}\operatorname{arsinh}
                         \{c(u)\tan(u/2)\}.
\end{gathered}
\tag{2}
\]
In particular the bound \(127/144\) is the original bound
\(|v|^2<127/36\), with \(v=2c\). No new cubic sheet is
selected here.

For \(0\le\delta\le1/2\), define
\[
\begin{split}
 \Psi_\delta(u)&=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\\
 f(u)&=\operatorname{arsinh}\{c(u)\tan(u/2)\},\\
 F(u,\delta)&=f(u)-i(3u/2-\pi\delta).
\end{split}
\tag{3}
\]
Thus \(\Psi_\delta'=-F/\pi\). The frequency in the original
cosine observation is \(k/N=1/2-\delta\).

**Theorem.** The local selected solution \(u_\delta\) of
\(F(u,\delta)=0\) continues holomorphically to a neighborhood
of the entire closed parameter interval \([0,1/2]\). It obeys
\[
 u_0=0,\qquad
 0<\Re u_\delta<4/3,\qquad
              -1/2<\Im u_\delta<0\quad(0<\delta\le1/2).
\tag{4}
\]
For each such positive real \(\delta\), it is the only zero,
counted with multiplicity, of \(F(\cdot,\delta)\) in the open
rectangle specified by (4). In particular
\[
             \Psi_\delta''(u_\delta)\ne0.
\tag{5}
\]
The original action along this family satisfies
\[
\begin{split}
 \mathcal S(\delta)&=\Psi_\delta(u_\delta),\qquad
 \Gamma(\delta)=\Re\mathcal S(\delta),\qquad M_3=\Re S(0),\\
 \Gamma'(\delta)&=\Im u_\delta<0,\\
 M_3-\Gamma(\delta)&=\int_0^\delta(-\Im u_s)\,ds.
\end{split}
\tag{6}
\]
The last two assertions hold for \(0<\delta\le1/2\).

This is a theorem about the original selected phase, not a
complete quantum coefficient theorem on the whole frequency band.
In particular (5) does not assert a globally contributing Gaussian
contour or a negative real Hessian on a fixed horizontal contour.

## 2. Holomorphy and elementary bounds on the fixed rectangle

Let
\[
 \mathcal R=\{u=a-ih:0\le a\le4/3,\ 0\le h\le1/2\}.
\tag{7}
\]
Since \(4/3<\pi/2\), this lies in \(\mathcal U_+\).
Write \(c=c_r+ic_i\) and \(\tan(u/2)=p-iq\). On this
rectangle \(p,q\ge0\), and they do not both vanish except
at zero. Consequently
\[
 \Re\{c\tan(u/2)\}=c_rp+c_iq>0\quad(u\ne0).
\tag{8}
\]
The principal inverse hyperbolic sine is therefore the original
branch throughout this rectangle. It extends holomorphically to
a neighborhood of it: its compact argument image avoids the two
imaginary cuts, while at \(u=0\) the argument is zero. The
selected cubic and the tangent have already been shown holomorphic
there. No continuation across an inverse-function cut is used.

We record three exact estimates. First,
\[
       \arg c<\arctan(4/9)<3/7.
\tag{9}
\]
The first follows from (2). For the second,
\(\tan x>x+x^3/3\) on \(0<x<\pi/2\), since the derivative
of their difference is \(\tan^2x-x^2>0\). At \(x=3/7\)
the latter polynomial is \(156/343>4/9\).

Second,
\[
        |\tan(u/2)|^2<27/41<2/3\quad(u\in\mathcal R).
\tag{10}
\]
Indeed
\[
 |\tan((a-ih)/2)|^2
       =\frac{\cosh h-\cos a}{\cosh h+\cos a}.
\]
The alternating cosine series and the positive hyperbolic series
give the written rational witnesses
\[
 \cos(4/3)\ge1-\frac89+\frac{32}{243}-\frac{256}{32805}
            =\frac{7709}{32805}>\frac7{30},
 \qquad
 \cosh(1/2)\le1+\frac{1/8}{1-1/48}
            =\frac{53}{47}<\frac{17}{15}.
\tag{11}
\]
The ratio in (10) increases with \(\cosh h\) and decreases
with \(\cos a\). Substitution of the strict bounds in (11)
therefore gives \(27/41\).
Combining (2),(10) gives
\[
       |c\tan(u/2)|^2<127/216<16/25.
\tag{12}
\]

Third, throughout this rectangle,
\[
                        |f(u)|<\frac{567}{392}|u|
                                      <\frac32|u|\quad(u\ne0).
\tag{13}
\]
For \(|z|^2<2/3\), the principal integral
\[
 \operatorname{arsinh}z
      =\int_0^1\frac{z}{\sqrt{1+s^2z^2}}\,ds
\]
has modulus at most \(\sqrt3|z|\). Also, along the segment
from zero to \(u/2\),
\[
 |\cos(su/2)|^2
      =\cos^2(sa/2)+\sinh^2(sh/2)
      \ge\cos^2(2/3)>(7/9)^2.
\]
The last inequality follows from \(\cos(2/3)>1-(2/3)^2/2\).
Integrating the derivative of the tangent yields
\[
                  |\tan(u/2)|\le\frac{81}{98}|u|.
\]
Apply this with \(|c|<1\), (10), and \(\sqrt3<7/4\).
The product is \(567/392<3/2\), proving (13).

For use on the boundary, if \(z\) is in the right half-plane
and \(w=\operatorname{arsinh}z=A+iB\) is principal, then
\(A>0\), \(|B|<\pi/2\), and
\[
 |z|^2=\sinh^2 A+\sin^2B,
 \qquad A\le\operatorname{arsinh}|z|.
\tag{14}
\]
If \(\Im z\ge0\), then
\(\arg z=\arctan(\coth A\tan B)\ge B\). If
\(\Im z<0\), then \(B<0\). Since
\(\arg(c\tan(u/2))\le\arg c\), these facts imply
\[
                     \Im f(u)<3/7\quad(u\in\mathcal R).
\tag{15}
\]
At zero this holds directly.

## 3. All four boundary exclusions

Fix \(0<\delta\le1/2\). We show that \(F\) has no zero
on any side of \(\mathcal R\), including their endpoints.

On the upper side \(u=a\), \(a>0\), (8) gives
\(\Re f(a)>0\), whereas the right side of
\(f=i(3u/2-\pi\delta)\) has real part zero.
At \(u=0\) that equation would require \(\delta=0\).

On the left side \(u=-ih\), \(h>0\), one has
\(|c\tan(u/2)|<\tanh(h/2)\). Thus (14) gives
\[
 \Re f(-ih)<\operatorname{arsinh}(\tanh(h/2))<h/2,
\tag{16}
\]
but the required real part of the right side is \(3h/2\).
The second strict inequality follows from
\(\tanh(h/2)<\sinh(h/2)\).

On the lower side \(h=1/2\), equations (12),(14) give
\[
                  \Re f(u)<\operatorname{arsinh}(4/5)<3/4.
\tag{17}
\]
For the last strict inequality,
\(\sinh(3/4)>3/4+(3/4)^3/6=105/128>4/5\).
The required real part is exactly \(3/4\), a contradiction.

On the right side \(a=4/3\), the required imaginary part is
\[
          2-\pi\delta\ge2-\pi/2>3/7,
\tag{18}
\]
using \(\pi<22/7\). This contradicts (15).
These four arguments also cover the lower corners; the upper
corners are covered by the upper-side argument.

## 4. The corner at zero and the exact root count

At \(\delta=0\), (13) shows that
\(f(u)=3iu/2\) has no solution in \(\mathcal R\) except
\(u=0\). Its derivative there is nonzero. More precisely, the
original endpoint root is
\[
 c_+=\frac{1+2i+\sqrt{5-4i}}4,
 \qquad F_u(0,0)=\frac{c_+-3i}{2}\ne0.
\tag{19}
\]
The original local selected branch, proved in
[the endpoint-root theorem, Section 3](research_mixed_next_outer_symbol_endpoint_roots.md),
is consequently
\[
          u_\delta=\frac{2\pi}{3+ic_+}\delta+O(\delta^3).
\tag{20}
\]
Since \(\Re c_+>0\) and \(\Im c_+<1/3<3\), the
coefficient in (20) has positive real part and negative imaginary
part. Thus this single local root enters the interior of
\(\mathcal R\) when \(\delta>0\) is sufficiently small.

There are no additional roots for those small positive parameters.
To see this without applying the argument principle to a zero on
the boundary, take a sufficiently small disk around zero in the
fixed holomorphic neighborhood. The implicit-function theorem
gives exactly one root there. On the compact remainder of
\(\mathcal R\), \(F(\cdot,0)\) is nonzero by (13), so it
remains nonzero for small \(\delta\). The local root is in the
open rectangle by (20).

For positive \(\delta\), Section 3 excludes every boundary
zero. The argument principle on the fixed rectangular boundary
therefore has constant count as \(\delta\) varies in
\((0,1/2]\). That count is one by the preceding paragraph.
It includes multiplicity, so the root is simple for every such
parameter. This proves (4),(5).

The implicit-function theorem at each root now gives its local
holomorphic dependence on \(\delta\); uniqueness makes the
local branches agree on overlaps along the real interval. A
finite cover of that compact interval, shrunk if needed, gives
a single holomorphic branch on a neighborhood of \([0,1/2]\).
This includes the original branch (20) at its left endpoint.

## 5. Original action, oriented factor, and remaining finite source

The original action in (2) is holomorphic on the required domain,
and (3) is its exact logarithmic stationary equation. Therefore
stationarity gives
\[
                    \mathcal S'(\delta)=-iu_\delta,
\tag{21}
\]
which proves (6) with its original additive constant.
In particular the depth divided by \(\delta\) extends continuously
and positively to zero, by (20). Compactness gives a constant
\(c_*>0\), without asserting its value, such that
\[
       -\Im u_\delta\ge c_*\delta,\qquad
       M_3-\Gamma(\delta)\ge\tfrac12c_*\delta^2
                          \quad(0\le\delta\le1/2).
\tag{22}
\]
These remain phase inequalities.

There is also an exact algebraic identification on this entire
interval. The unsquared identity of the endpoint-root theorem and
[the oriented-factor theorem](research_mixed_next_outer_oriented_root_barriers.md)
give, for small positive \(\delta\),
\[
 \mathscr F_+\!\left(e^{iu_\delta},
                        e^{i\pi(1/2-\delta)}\right)=0.
\tag{23}
\]
Both sides are holomorphic along the continued parameter
neighborhood, so the identity theorem extends (23) to all of
\([0,1/2]\). For \(\delta>0\), this root is outside the
unit circle because \(|e^{iu_\delta}|=e^{-\Im u_\delta}>1\).
No assertion is made that it remains the nearest outer root of
that factor beyond the local interval already proved. The action
integral (6) follows this selected root, not the minimum over
unselected algebraic branches.

The complete quantum cosine response is proved with this action
only on the sufficiently small frequency interval in
[the local source theorem](research_mixed_next_near_half_geometric_cosine_response.md).
The larger rectangle in (4) lies in the phase and shortened-edge
domains, but the
[single-current assembly](research_mixed_next_inner_three_single_remaining_current.md)
still retains its explicit off-grid right-middle inner current.
Its physical-node estimate is not a complex-neighborhood bound;
values on a proper node subinterval do not determine a degree-\(U\)
polynomial. The present root count neither estimates that current
nor controls a cumulative finite-recurrence error. A contributing
contour and a complete source gap remain necessary before extending
the selected quantum coefficient theorem to this whole interval.

## Frozen source versions

- Original cubic continuation, logarithmic lift and strict domain
  guards: `8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a`.
- Local selected root and unsquared symbol identity:
  `aa0a17aec890cfe3951feaafd14a0c35b0d809a348181009e497cdc02dcdee90`.
- Actual local quantum coefficient theorem:
  `19a62beac1f4e2ef3c900d18d402c316b2cf098cd7c32753924824fe2aedcc02`.
