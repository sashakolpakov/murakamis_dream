# Global horizontal concavity and two removable wire tails

These estimates concern the exact prepared triple sum in
[the full boundary-sum formula](research_three_crossing_prepared_boundary_sum.md).
They retain its original boundary polynomial. They prove a global
principal-horizontal comparison, remove two specified real lattice
sectors, and bound the seven other horizontal copies and every mixed
current in the exact cellwise contour identity. The original staircase
cut and all fixed ordinary boundary derivatives are retained.

Write
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 b_2=2G/\pi,\qquad c=2J(5/6),
\]
with the original analytic branches when the argument is complex.
The three indices are \(x=j/N\), \(y=i/N\), and \(z=k/N\),
with \(0\le k\le j\) and \(i+j<N\). Put \(p=x-z\).
The prepared phase at the complete boundary is
\[
 \Xi(x,y,z)=J(x+y)-J(x)-J(x-z)-3J(z)-6J(y)+J(2y)
 +\frac{i\pi}{2}\bigl[(x-y)^2-x+y+2xz+2z^2\bigr].       \tag{1}
\]
For real indices its real part is interpreted using the actual
absolute Newton product if \(y\ge1/2\), including the odd-level zeros.
No analytic continuation across that zero is needed for the tail bounds.

## 1. Two real wire sectors are exponentially smaller

**Proposition 1.** In the original finite prepared sum, retain either
of the sectors
\[
             k/N\le1/100,
 \qquad\hbox{or}\qquad (j-k)/N\le1/400.                  \tag{2}
\]
The absolute sum of either sector, uniformly on
\(|w+2|\le10^{-6}\), is bounded by a polynomial in \(N\)
times an exponential of rate at most, respectively,
\[
                 \frac{663}{500},\qquad
                 \frac{18229}{12000}<\frac{153}{100}.    \tag{3}
\]
The same strict rate bounds hold for each fixed ordinary boundary
derivative on the disk of half that radius. They hold at every integer
level and for both crossing signs.

*Proof.* The absolute triple summand splits into the remaining
\(JM^2\) entry, the boundary Newton polynomial, and the prepared
\(MJh\) summand. Their real exponential rates are bounded by
\[
                   b_2+b_2+T_3(x,z),
 \qquad T_3(x,z)=J(x)-J(x-z)-3J(z).                     \tag{4}
\]
The first two bounds, uniformly over all original indices, are proved
in [the global preparation-error note](research_three_crossing_global_preparation_error.md),
Lemmas 1--2. On the indicated complex boundary disk the second bound
increases by at most
\(\operatorname{arcosh}(1+10^{-6}/2)<1/1000\).
The uniform sine-factorial remainder is \(O(\log N)\), also at zero
indices. All prefactors and the at most \(N^3\) summands are therefore
absorbed in a polynomial.

On \(0\le t\le1\), \(J'(t)\le\log2\), whereas
\(-2J(t)\le c\). On \(0\le t\le1/2\), the chord bound
\(\sin\pi t\ge2t\) gives
\[
              -J(t)\le t(1-\log(4t)),                  \tag{5}
\]
with its continuous value at zero. The right side increases on the
small intervals used below.

If \(z\le1/100\), then
\[
 T_3\le z\log2-3J(z)
 <\frac7{1000}+\frac3{100}(1+\log25)
 <\frac{157}{1000}.                                    \tag{6}
\]
If \(p=x-z\le1/400\), then
\[
 \begin{split}
 T_3&=[J(x)-J(z)]-J(p)-2J(z)\\
 &\le p\log2-J(p)+c
 <\frac{67}{4000}+\frac13 .
 \end{split}                                           \tag{7}
\]
Here \(\log2<7/10\), \(\log25<4\), \(\log100<5\),
and the previously proved bound \(c<1/3\) suffice.
Also \(G<229/250\) and \(\pi>157/50\) imply
\(2b_2<146/125\). Adding this bound and \(1/1000\)
to (6)--(7) gives (3). The exact polynomial sector sums permit
Cauchy's formula on the smaller disk. Conjugating the original
matrices gives the opposite-sign statement. \(\square\)

This is a bound on specified summands of the original finite source.
It is not a statement that a future contour current on those cuts
automatically has the same bound.

## 2. A global principal-horizontal concavity region

For a complex variable \(t\), put
\(C_t=\Re\cot(\pi t)\) and \(T_t=\Re\tan(\pi t)\).
Both are positive when \(0<\Re t<1/2\), independently of its
imaginary part. Fix imaginary heights \(h_x,h_y,h_z\), with
\[
             |h_x|\le3/40,\qquad
             |h_y|\le13/200.                            \tag{8}
\]
There is no restriction on the finite height \(h_z\).

**Theorem 2.** On the convex real domain
\[
 \frac1{10}\le\Re x<\frac12,\qquad
 \frac1{10}\le\Re y<\frac12,\qquad
                 0<\Re z<\Re x,                       \tag{9}
\]
the function \(\Re\Xi\), restricted to those fixed heights,
has negative-definite real Hessian. It is uniformly negative
definite on every compact subset. In particular the selected
geometric stationary point is the unique global maximum on this
principal horizontal domain. All compact boundary pieces disjoint
from that point have a strict action gap.

*Proof.* The quadratic imaginary polynomial in (1) contributes no
real horizontal Hessian. Using
\(4\cot(2t)=2\cot t-2\tan t\), its negative real Hessian
divided by \(\pi\) has quadratic form
\[
 \begin{split}
 Q(v)={}&C_xv_x^2+(4C_y+2T_y)v_y^2+3C_zv_z^2
       +C_{x-z}(v_x-v_z)^2\\
       &\hspace{15mm}-C_{x+y}(v_x+v_y)^2 .
 \end{split}                                            \tag{10}
\]
Every coefficient except possibly the last is positive on (9).
If \(\Re(x+y)\ge1/2\), its last coefficient is nonpositive,
and (10) is positive definite immediately.

Suppose instead \(\Re(x+y)<1/2\). For \(t=a+ih\),
\[
 C_t=\frac{\cot(\pi a)}
            {1+\sinh^2(\pi h)/\sin^2(\pi a)} .          \tag{11}
\]
The height bounds (8), the lower real bounds in (9), and elementary
sine and hyperbolic-sine estimates give
\[
 C_x\ge\frac58\cot(\pi\Re x),\qquad
 C_y\ge\frac23\cot(\pi\Re y),\qquad
 C_{x+y}\le\cot(\pi\Re(x+y)).                           \tag{12}
\]
For explicit rational verification of the first two constants, use
\(157/50<\pi<22/7\), \(\sin a\ge a-a^3/6\), and
\(\sinh b\le b/(1-b^2/6)\) at these small positive arguments.
The last inequality follows termwise from
\((2n+1)!\ge6^n\).

Set \(u=\tan(\pi\Re x)\), \(v=\tan(\pi\Re y)\).
Then \(uv<1\) and \(v>8/25\), the latter following from
\(\tan a\ge a+a^3/3\). Drop the additional positive
\(C_{x-z}\) square in (10). Set \(a=8/5\), \(b=3/8\),
and \(v_0=8/25\). The rank-one comparison is bounded by
\[
 \begin{split}
 C_{x+y}\left(\frac1{C_x}+\frac1{4C_y+2T_y}\right)
 &\le R(u,v):=\frac{(1-uv)(au+bv)}{u+v},\\
 \partial_vR
 &=-\frac{u[au^2+a+2buv+bv^2-b]}{(u+v)^2}<0,\\
 R(u,v)&\le R(u,v_0)\\
 &\le a+(2a-b)v_0^2
                   -2v_0\sqrt{a(a-b)(1+v_0^2)}\\
 &<\frac{2966}{3125}<\frac{19}{20}.
 \end{split}                                            \tag{13}
\]
For the penultimate inequality put \(w=u+v_0\) and apply
the arithmetic--geometric mean inequality to
\(aw+(a-b)(1+v_0^2)/w\). The last rational bound uses
\(\sqrt{a(a-b)(1+v_0^2)}>1469/1000\).
The Cauchy inequality in the positive diagonal quadratic form
therefore makes (10) positive definite. Compactness gives the
uniform version. Strict concavity on the convex domain proves the
global maximum statement because the selected point is an interior
stationary point of the full logarithmic phase. \(\square\)

The exact outward root enclosures in
[the closing-action certificate](../repro/results/research-three-crossing-closing-action.json)
give \(|\Im x_*|<3/40\) and
\(|\Im y_*|<13/200\), so (8) includes the selected heights.
The selected point satisfies (9). Its stationarity is the original
logarithmic one proved in
[the remaining-saddle dictionary](research_three_crossing_geometric_remaining_saddle.md).
The argument also works for the conjugate contour.

For the application, the uniform statement extends to a fixed open
neighborhood of the closed retained polytope
\[
 \mathcal P_0=\{1/10\le\Re x\le1/2,\quad
 1/10\le\Re y\le2/5,\quad
 1/100\le\Re z\le\Re x-1/400\},                              \tag{13a}
\]
uniformly for the whole compact box of imaginary heights used below.
Indeed at \(\Re x=1/2\), one has \(C_x=0\), but
\(C_{x+y}<0\). The positive form
\(C_{x-z}(v_x-v_z)^2+3C_zv_z^2+(4C_y+2T_y)v_y^2\)
already controls all three directions. Thus the full Hessian stays
positive definite on that boundary as well. The fixed lower bounds
on \(\Re z\) and \(\Re(x-z)\), and \(\Re y\le2/5\),
make the whole set compact within its factorial domains. Positivity
and continuity give one strictly positive lower eigenvalue and then
a fixed open neighborhood. In particular all \(O(N^{-1})\)
half-grid and staircase offsets preserve the concavity and imaginary
convexity estimates for sufficiently large levels.

## 3. Seven penalized horizontal copies

Let \(h=(\Im x_*,\Im y_*,\Im z_*)\), where the third entry
is the selected inner saddle height. Thus \(h_x<0<h_y,h_z\).
For \(\sigma\in\{1,-1\}^3\), define
\[
 f_\sigma(r)=\Re\Xi(r_x+i\sigma_xh_x,
                       r_y+i\sigma_yh_y,r_z+i\sigma_zh_z),
 \qquad
 P_\sigma=2\pi\sum_{\sigma_j=-1}|h_j|.                 \tag{14}
\]
Use the closed polytope
\[
 \mathcal P=\{1/10\le r_x,r_y\le1/2,
                         \ 1/100\le r_z\le r_x-1/400\}.
                                                               \tag{15}
\]
Statements at its factorial-strip boundary are interpreted as
one-sided limits. The applications can also retain \(r_y\le2/5\),
which is a subset of (15).

**Proposition 3.** For each of the seven choices
\(\sigma\ne(1,1,1)\),
\[
                  \sup_{r\in\mathcal P}
                         [f_\sigma(r)-P_\sigma]<29/20.          \tag{16}
\]
This estimates the displayed functions. Identification of all their
coefficients in an exact original-cycle formula is a separate step.

*Proof.* Theorem 2 applies to every sign choice because the magnitudes
of the heights have not changed. At any interior rational point \(r_0\),
the global tangent inequality therefore gives
\[
 f_\sigma(r)\le f_\sigma(r_0)
                  +\nabla f_\sigma(r_0)\cdot(r-r_0).             \tag{17}
\]
The right side attains its maximum at one of the eight vertices
\[
 r_x,r_y\in\{1/10,1/2\},\qquad
                   r_z\in\{1/100,r_x-1/400\}.                  \tag{18}
\]
The exact outward certificate
[verify_three_crossing_formal_horizontals.py](../experiments/verify_three_crossing_formal_horizontals.py)
evaluates (17)--(18) at the following rational points, listed in
thousandths:

| \(\sigma\) | \(1000r_0\) |
|---|---|
| \((1,1,-1)\) | \((499,208,239)\) |
| \((1,-1,1)\) | \((251,249,140)\) |
| \((1,-1,-1)\) | \((434,242,220)\) |
| \((-1,1,1)\) | \((279,252,104)\) |
| \((-1,1,-1)\) | \((355,250,188)\) |
| \((-1,-1,1)\) | \((213,271,87)\) |
| \((-1,-1,-1)\) | \((251,271,169)\) |

The heights are the rational enclosures from the independently
certified original geometric root. All arithmetic is rational and
outward. The logarithm uses its convergent atanh series on the right
half-plane. The dilogarithm uses its disk series or the principal
identity
\[
 \operatorname{Li}_2(Z)=-\operatorname{Li}_2(1/Z)
                         -\pi^2/6-\tfrac12\operatorname{Log}^2(-Z).
                                                               \tag{19}
\]
Every inversion argument avoids the positive-real cut; the
negative-real axis is allowed. The factorial primitive is
\[
 J(t)=\frac{i\pi}{2}(t-t^2)
       +\frac{i}{2\pi}\left[\operatorname{Li}_2(e^{2\pi it})
                                                     -\pi^2/6\right].
                                                               \tag{20}
\]
Its arguments remain in the original open real strip at every
evaluation point, so (19) retains that branch. Binary interval powers
avoid rectangular wrapping; they do not change the series or its
explicit analytic tail bound. The real gradient is evaluated from
the principal logarithms of \(2\sin\pi t\), whose real parts are
positive on the open strip.

The saved [rational certificate](../repro/results/research-three-crossing-formal-horizontals.json)
records all phase, gradient, penalty, and tangent bounds and checks
(16) for every sign. For orientation, its largest certified bound
is less than \(1.413\). No sampled maximum is a proof input.
\(\square\)

## 4. All cellwise mixed currents have a strict gap

Use the original finite indicator and the exact contour identity in
[the retained-polytope contour theorem](research_three_crossing_retained_polytope_contour.md),
equations (2), (8)--(14). In particular the vertical factors are
integrated on half-grid lines, where their kernels have modulus at
most one; no limiting principal-value prescription is used.

Extend (14) to \(\sigma\in\{-1,0,1\}^3\), with zero indicating
zero imaginary height. On the retained polytope \(\mathcal P_0\)
in (13a), consider exactly the following six families:

| Real face | Allowed height vertices | Number |
|---|---|---:|
| \(x=1/10\) | all \(\sigma\in\{-1,0,1\}^3\) | 27 |
| \(y=1/10\) | all \(\sigma\in\{-1,0,1\}^3\) | 27 |
| \(y=2/5\) | all \(\sigma\in\{-1,0,1\}^3\) | 27 |
| \(z=1/100\) | all \(\sigma\in\{-1,0,1\}^3\) | 27 |
| \(x=1/2\) | \(\sigma_z\ne0\) | 18 |
| \(x-z=1/400\) | \(\sigma_y\ne0\) | 18 |

**Theorem 4.** On every face and height choice in this complete list,
\[
                 \sup_{r\text{ on the face}}
                       [f_\sigma(r)-P_\sigma]<151/100.           \tag{21}
\]
Consequently all nonempty-vertical-subset terms of the exact cellwise
contour identity have total size
\[
                         O(N^A e^{151N/100})                    \tag{22}
\]
for some fixed \(A\), on a fixed complex neighborhood of the complete
ordinary boundary. The same bound holds for every fixed ordinary
boundary derivative on a smaller neighborhood, at both level parities.

*Proof of the finite face inequalities.* For each fixed height choice,
Theorem 2 and the closed-boundary extension after (13a) give global
concavity on each entire face. Apply the tangent inequality (17) at
one rational point on that face. Its affine upper bound has its
maximum at one of the four vertices of that face. This remains valid
when the chosen tangent point itself lies on an edge: the phase is
holomorphic on a neighborhood, and the concavity extends to the
closed polytope.

The exact outward verifier
[verify_three_crossing_current_faces.py](../experiments/verify_three_crossing_current_faces.py)
checks that its case set equals precisely the table above, has no
duplicates, and contains 144 cases. The
[rational-point fixture](../repro/fixtures/research-three-crossing-current-face-points.json)
provides only the tangent points. They are not assumed maxima.
For each case the verifier reevaluates the phase, its real gradient,
the four vertex bounds, and the exact height penalty. The
[completed certificate](../repro/results/research-three-crossing-current-faces.json)
records every rational enclosure and comparison. All 144 inequalities
(21) pass. Its largest certified upper bound is less than
\(1.498719\), leaving a strict margin below \(1.51\).

Here are the branch and remainder details of this finite verification.
It uses (20), the principal inversion (19), and, when needed,
\[
 \begin{split}
 \operatorname{Li}_2(Z)
   &=\pi^2/6-\operatorname{Log}Z\operatorname{Log}(1-Z)
                            -\operatorname{Li}_2(1-Z),\\
 \operatorname{Li}_2(Z)
   &=-\operatorname{Li}_2\!\left(\frac Z{Z-1}\right)
                              -\tfrac12\operatorname{Log}^2(1-Z),\\
 \operatorname{Li}_2(Z)
   &=\tfrac12\operatorname{Li}_2(Z^2)-\operatorname{Li}_2(-Z).
 \end{split}                                                   \tag{23}
\]
The first two are used off their principal cuts. Duplication is used
only in the right-half-plane lens with a definite nonzero imaginary
part: the ray to \(Z\), its square, and its negative avoid the
relevant cuts. Thus these equalities follow from their power series
near zero by the indicated regular continuation. All eventual disk
series have certified radius less than \(9/10\), use 150 terms, and
retain the explicit geometric tail bound.

Before using the right-half-plane logarithm series, the verifier
multiplies its argument by \(1-i\) or \(1+i\) according to the
sign of its imaginary part and rescales by a positive power of two.
The exact correction is
\(-\tfrac12\log2\pm i\pi/4\) plus the corresponding integer
multiple of \(\log2\). The resulting atanh radius is explicitly
checked to be less than \(3/4\). This handles the small near-imaginary
arguments at the zero-height slanted face without relaxing a remainder
or changing a branch. Every arithmetic operation is rational and
outward. The root certificate, fixture, script, and direct source
dependencies are identified by hashes in the result.

*Proof that the list covers the currents.* Let \(V\ne\varnothing\)
be the set of vertical coordinates in the exact identity. Only a
coordinate in \(V\) can have a zero height at a convexity vertex;
all horizontal coordinates have their fixed nonzero heights.
If \(y\in V\), the independent \(y\)-indicator places the support
on one of the two \(y\) faces. These are covered with all 27 choices.
Assume henceforth that \(y\notin V\); its height is then nonzero.

If both \(x,z\in V\), the exact mixed difference is supported on
the two staircase sheets of the \(x-z\) cut, or on an intersection
of an \(x\) cut with the lower \(z\) cut. The former lies in the
last family, because the \(y\) height is nonzero; the latter lies
in the full lower-\(z\) family. Both staircase sheets are retained.
If only \(x\in V\), the support is on an \(x\) face or the
diagonal cut. Its upper-\(x\) part has nonzero \(z\) height,
and its diagonal part has nonzero \(y\) height, exactly as in
the table. If only \(z\in V\), its support is on the lower
\(z\) face or the diagonal cut, also covered. These cases exhaust
every nonempty \(V\), including all triple currents.

*Proof of the intervening heights and the source bound.* On the
compact retained domain and height box, Theorem 2 says
\(-\Re\Xi''\) is uniformly positive definite. Holomorphy gives
\[
          \partial_{h_i}\partial_{h_j}\Re\Xi(r+ih)
                              =-\Re\Xi_{ij}(r+ih),              \tag{24}
\]
so the real phase is convex in the simultaneous imaginary variables.
The exact kernel penalty is linear on each orthant of the vertical
height box. The maximum of phase minus penalty on that orthant is
therefore attained at a height vertex. All such vertices were just
covered by (21).

The uniform open-neighborhood extension following (13a) handles the
\(O(N^{-1})\) positions and widths of all actual half-grid faces and
staircase sheets. The interpolation is holomorphic on these fixed
bulk factorial domains. The strict finite gap persists after a
sufficiently small complex boundary perturbation. Its uniform
factorial estimates have only polynomial prefactors, the exact
finite-difference coefficients have modulus at most eight, and
only polynomially many integrals occur. The horizontal kernels
have the stated exponential penalties and bounded remaining factors;
the vertical half-grid kernels have the explicit logistic bound.
These facts prove (22) for their entire sum.

The boundary interpolation and all these fixed contour integrals are
holomorphic and even in \(u\), where \(w=-2\cos u\). They descend
to the ordinary boundary variable near \(-2\). Cauchy's formula on
a smaller fixed disk proves the derivative bounds. Conjugating the
original data proves the corresponding negative-source statement.
\(\square\)

## 5. Consequence for the exact cycle

Proposition 1 bounds the two removed real wire sectors. Proposition 3
bounds the seven nonprincipal full horizontals. Theorem 4 bounds every
mixed current with its actual finite indicator and kernel penalty.
The principal horizontal has coefficient exactly \(+1\) and, by
Theorem 2, the unique global maximum at the selected stationary point.
Thus the original triangular lattice constraint has been retained in
a complete contour comparison. The resulting nonzero original
boundary asymptotic and its normalization are assembled in
[the full boundary theorem](research_three_crossing_full_boundary_asymptotic.md).

These conclusions concern this specified source and its local
ordinary boundary germ. They do not imply a general adjacent-word
theorem or an unrestricted global boundary strip estimate.

The rational constants in Sections 1--2 are checked by
[check_three_crossing_horizontal_tail_constants.py](../experiments/check_three_crossing_horizontal_tail_constants.py).
