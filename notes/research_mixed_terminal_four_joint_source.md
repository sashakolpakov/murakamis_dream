# A joint coherent source for the type-four terminal transform

Research deduction, 5 November 2026. The type-four terminal polynomial
has a literal three-index interpolation whose phase is exactly the
original endpoint action. An explicit product of rectangles contains
all its certified endpoint roots and has a uniform positive negative
real Hessian. This gives the original local three-dimensional Gaussian
and a fixed-height supporting plane. The other constant-mode currents,
residue aliases and real complement remain unestimated. In particular
this is not the already refuted nested positive-cap comparison.

## 1. An exact triple sum without a private-index triangle inequality

Use the original conventions
\[
 r=e^{-2\pi i/N},\quad q=e^{\pi i/N},\quad
 P_j=(r;r)_j,\quad S_j=\prod_{k=1}^j2\sin(\pi k/N),\quad
 \delta_j=P_j/S_j,
 \tag{1}
\]
with the continuous value \(\delta_0=1\). Let \(w\) denote
the ordinary endpoint color and \(X=e^{-2\pi ia}\).
The exact reversed-cap identity is
\[
 \mathcal V_{1,N}(w,X)
 =\sum_{j<N} C_{1,N}(X,r^j)
                    \frac{\mathcal H_N(w,r^{-j})}{P_j}.
 \tag{2}
\]
The original boundary change of basis gives the whole-polynomial
identity
\[
 \mathcal H_N(w,r^{-j})=P_j b_j(w),\qquad
 b_j(w)=\delta_j^{-1}\sum_{l=0}^j
              \frac{q^{jl}e_l(w)}{S_lS_{j-l}}.
 \tag{3}
\]
These are the ordinary-color versions of
[the boundary coefficient formula](research_complete_boundary_coefficient_asymptotic.md#1-the-coefficient-and-its-asymptotic)
and [conditional composition, Section 5](research_mixed_conditional_torus_composition.md#5-open-words-with-the-original-complete-boundary-jets).
They include every fixed ordinary derivative and both level parities.

Expand only the exact conditional polynomial in (2). On its physical
support, \(p_i(r^j)=P_{i+j}/P_j\); outside that support the
product is exactly zero. Therefore
\[
 \boxed{\displaystyle
 \mathcal V_{1,N}(w,X)=
 \sum_{\substack{i+j<N\\0\le l\le j}}
 \frac{X^{-i}p_i(X)P_{i+j}}{P_i^3P_j}\,
 \delta_j^{-1}\frac{q^{jl}e_l(w)}{S_lS_{j-l}} .}
 \tag{4}
\]
There is no extra scalar \(N\) in (4). The three physical
indices are the attached transform leg \(t=i/N\), private
endpoint leg \(e=j/N\), and ordinary Newton variable \(u=l/N\).
Both support walls \(t+e<1\) and \(u\le e\) remain literal.
No absolute value has been taken at either of the two inner levels.
In particular the extra type-four private factorial has not been
removed by the type-three binomial identity.

## 2. Simultaneous interpolation and its original action

Let \(G_N\), \(\mathcal E_N(u,w)\), and
\(\mathfrak P_N\) be the prescribed sine-factorial, whole-color
Newton, and marked factorial interpolants in
[the exact joint source](research_mixed_terminal_three_joint_zero_mode.md#4-the-controlled-finite-current-and-its-unestimated-joins).
Write
\[
 \Delta_N(e)=\exp\!\left\{\frac{i\pi}{2}
                       ((N-1)e-Ne^2)\right\},\qquad
 \mathfrak P_N(e)=\Delta_N(e)G_N(Ne).
 \tag{5}
\]
Thus \(\Delta_N(j/N)=\delta_j\). The exact triple summand
on a regular product is interpolated by
\[
\begin{split}
 \mathcal J_N(a;e,t,u,w)={}&
 e^{2\pi iNat}
 \frac{\mathfrak P_N(a+t)\mathfrak P_N(e+t)}
      {\mathfrak P_N(a)\mathfrak P_N(t)^3\mathfrak P_N(e)}\\
 &\quad\cdot\Delta_N(e)^{-1}e^{i\pi Neu}
             \frac{\mathcal E_N(u,w)}
                  {G_N(Nu)G_N(N(e-u))}.
\end{split}
 \tag{6}
\]
At each retained lattice triple this equals (4) exactly. The equality
\(\mathfrak P_N(a+i/N)/\mathfrak P_N(a)=p_i(X)\)
uses its exact finite-difference equation. Neither an unspecified
periodic factor nor a new ordinary-color continuation occurs.

Set \(V_0(u)=-2J(1/2-u)-2J(u)\),
\(B(e,u)=V_0(u)-J(u)-J(e-u)\), and
\(g(v)=J(v)+i\pi(v-v^2)/2\). At complete color, (6) has
the phase
\[
\begin{split}
 \mathcal F_1(a;e,t,u)={}&B(e,u)+J(e+t)+J(a+t)
              -3J(t)-J(e)-J(a)\\
 &+i\pi\{e(u-t)+at+(e^2+t^2-e-t)/2\}.
\end{split}
 \tag{7}
\]
This is exactly the original own-type-four endpoint action in
[the open Hessian lemma, equation (1)](research_mixed_open_word_hessian.md)
with its external adjacent leg held at \(a\). For a direct
check before simplifying marks, its phase is
\[
 B(e,u)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
   -i\pi(e-e^2)/2+i\pi eu+2\pi iat.
 \tag{8}
\]
Equations (7)--(8) are algebraically identical on the original sine
strips. The \(\Delta_N(e)^{-1}\) mark is essential here.
No exponentiated equation or additive calibration constant is used
to identify this action.

The uniform factorial symbols give
\[
 \mathcal J_N(a;e,t,u,-2)=
 N^{-7/2}\mathcal A_1(a,e,t,u)
         e^{N\mathcal F_1(a;e,t,u)}(1+O(N^{-1})),
 \tag{9}
\]
where the nonzero amplitude is
\[
 \mathcal A_1=
 e^{i\pi(e+t)/2}
 \frac{\sqrt{2\sin\pi(a+t)}\sqrt{2\sin\pi(e+t)}}
 {(2\sin\pi a)^{1/2}(2\sin\pi t)^{3/2}
  (2\sin\pi e)^{1/2}(2\sin\pi u)^{3/2}
  (2\sin\pi(e-u))^{1/2}}.
 \tag{10}
\]
All square roots continue from the positive real sine values.
Indeed the marked-factorial quotient in (6) has power \(N^{-3/2}\),
and \(\mathcal E_N/[G_N(Nu)G_N(N(e-u))]\) has power
\(N^{-2}\). Their order-one marks multiply to
\(e^{i\pi(e+t)/2}\), which fixes (10).
On a small fixed ordinary-color disk, replace \(V_0(u)\) by its
original holomorphic \(V(u,w)\); the normalized symbol and its fixed
derivatives are uniform on smaller regular compact products.

## 3. One convex product covering every type-four endpoint root

Define the following closed real intervals and allow every coordinate
to have imaginary part in \([-3/25,3/25]\):
\[
 a\in[11/50,9/20],\quad t\in[1/5,2/5],\quad
 e\in[3/10,2/5],\quad u\in[1/10,7/25].
 \tag{11}
\]
The real shifted ranges are
\[
 a+t\in[.42,.85],\quad e+t\in[.50,.80],\quad
 e-u\in[.02,.30],\quad 1/2-u\in[.22,.40].
 \tag{12}
\]
Thus every primitive and the simultaneous interpolant is regular on
a neighborhood of the product. Summed imaginary parts can reach
\(.24\); the original factorial theorem applies on all compact
subsets of its regular strip, not only heights at most \(.12\).
The real triple rectangle lies strictly inside both support walls.

The exact endpoint rectangles give, for own type four and either
original external disk,
\[
\begin{split}
 .333<\Re e_*<.363,&\qquad -.051<\Im e_*<-.019,\\
 .246<\Re t_*<.350,&\qquad -.108<\Im t_*<-.020,\\
 .21<\Re u_*<.25,&\qquad .01<\Im u_*<.10.
\end{split}
 \tag{13}
\]
The first two rows are
[the saved endpoint-image extraction](research_mixed_open_word_endpoint_rectangles.md),
and the last is the original localization's auxiliary rectangle.
The full input disks \(D_3,D_4\) also lie strictly within the
external box in (11). Consequently this product contains all the
original endpoint roots, including the actual terminal roots of every
open word of length at least two.

**Lemma 1.** On the full complex product (11),
\[
                         -\Re\mathcal F_1''\succ
                                      \frac{\pi}{20}I_4.
 \tag{14}
\]
Here the real Hessian matrix is the entrywise real part of the complex
holomorphic Hessian. The variables in (14) are \((a,t,e,u)\).

*Proof.* Put \(C(z)=\Re\cot\pi z\) and
\(V(z,w)=J(z+w)-J(z)-J(w)\). The real-coefficient imaginary
quadratic in (7) has zero real Hessian. Its remaining action decomposes
exactly as
\[
           V(t,a)+V(e,t)-J(t)+B(e,u).
 \tag{15}
\]
Use the already established scalar \(\cosh(.24\pi)<4/3\).
On the full external box, \(C(a)>9/70\); on the stated
\(t,e\) boxes, \(C(t),C(e)>3/14\). These follow from
\[
 C(x+ih)=\frac{\sin(2\pi x)}
                    {\cosh(2\pi h)-\cos(2\pi x)},
 \tag{16}
\]
using denominator less than \(7/3\), and numerator greater than
\(3/10\) for \(a\) or \(1/2\) for \(t,e\).

For \(V(t,a)\), if \(\Re(t+a)\ge1/2\), its negative
real Hessian is at least \(\pi\operatorname{diag}(C(t),C(a))\),
which exceeds \((\pi/20)I_2\). Otherwise both individual
real coordinates belong to \([.20,.30]\). There
\(\sin(2\pi x)>19/20\), \(\cos(2\pi x)>-1/3\), so
\(C(t),C(a)>57/100\). Also
\[
 0<C(t+a)\le\cot(.42\pi)=\tan(2\pi/25)<13/50.
 \tag{17}
\]
For the last inequality, \(\sin x<x\),
\(\cos x>1-x^2/2\), and \(x<44/175\) give
\(\tan x<7700/29657<13/50\). Since
\((dt+da)^2\le2(dt^2+da^2)\), the pair's negative real
Hessian is greater than
\(\pi(57/100-26/50)I_2=(\pi/20)I_2\).

The pair \(V(e,t)\) has \(\Re(e+t)\ge1/2\), so it
contributes more than \((3\pi/14)(de^2+dt^2)\).
The term \(-J(t)\) is positive in the negative real Hessian.
Finally, exactly as in the endpoint Hessian formula,
\[
 -\Re B''=
 \pi\Re(2\tan\pi u+3\cot\pi u)\,du^2
            +\pi C(e-u)(de-du)^2.
 \tag{18}
\]
Both tangent and cotangent real parts at \(u\) exceed \(3/14\):
their numerators exceed \(1/2\), and their positive denominators
are less than \(7/3\). The first coefficient in (18) therefore
exceeds \(15\pi/14\). The second is positive by
\(0<\Re(e-u)<1/2\), regardless of its imaginary part.
Adding these bounds proves (14). \(\square\)

For a neighboring unselected type-four halfweight, subtract
\(\nu g(a)/2\), \(\nu=0,1\), from the phase. Its extra
negative real Hessian is nonnegative, so (14) persists. This is an
action statement; the finite Fourier interpretation still requires
the actual negative external type-four height.

**Lemma 1a (broader regular product).** Allow all four imaginary parts
in \([-3/25,3/25]\), and enlarge the real intervals to
\[
 a\in[.22,.45],\quad t\in[.15,.50],\quad
 e\in[.27,.49],\quad u\in[.10,.269].
 \tag{18a}
\]
Then
\[
                 -\Re\mathcal F_1''\succ\frac{\pi}{100}I_4.
 \tag{18b}
\]
Every source factor remains regular: the shifted real ranges are
\(a+t\in[.37,.95]\), \(e+t\in[.42,.99]\),
\(e-u\in[.001,.39]\), and \(1/2-u\in[.231,.40]\).
The real rectangle remains strictly inside both physical support
walls and contains all the roots (13).

*Proof.* Write \(b=C(a)\), \(p=C(t)\), \(q=C(e)\),
\(c=C(e-u)>0\), \(D=C(e+t)\), \(d=C(a+t)\), and
\(B=\Re(2\tan\pi u+3\cot\pi u)\). The exact quadratic form is
\[
\begin{split}
 -\pi^{-1}\Re\mathcal F_1''={}&
 b\,da^2+3p\,dt^2+q\,de^2+B\,du^2
       +c(de-du)^2\\
 &-D(de+dt)^2-d(da+dt)^2.
\end{split}
 \tag{18c}
\]
Discard the positive form with coefficient \(c\). For
\(\Re t\le.45\), the first three row-sum lower bounds of
the remaining matrix are
\(b-2d_+\), \(3p-2d_+-2D_+\), and \(q-2D_+\).
The first two are bounded below exactly as the external and transform
rows of [the enlarged type-three joint Hessian, equations (6)--(10c)](research_mixed_terminal_three_joint_zero_mode.md#2-a-joint-quantitative-hessian-bound).
Indeed, those estimates allowed the other summed variable to have
real part as small as \(.10\); here \(\Re e\ge.27\), so
every positive-part upper bound for its shifted cotangent improves.
The upper endpoint \(.49\) creates no adverse term: a sum at least
\(1/2\) has nonpositive real cotangent. Thus both rows exceed
\(1/100\), including the strip \(.15\le\Re t\le.20\).

For clarity, the new private row has the complete bounds
\[
\begin{array}{c|c}
 \Re e& q-2D_+\text{ is greater than}\\ \hline
 [.27,.30]&7/12-2(13/50)=19/300\\
 [.30,.35]&2/5-2(17/100)=3/50\\
 [.35,.49]&1/50 .
\end{array}
 \tag{18d}
\]
Use the same scalar lower function
\(C_0(x)=\sin(2\pi x)/(13/10-\cos(2\pi x))\)
as in that proof. It decreases for \(x\ge.20\).
The bound \(C_0(.30)>7/12\) is already recorded there;
\(C_0(.35)>2/5\) follows from
\(\sin(.7\pi)>4/5\), \(\cos(.7\pi)>-3/5\).
Also \(C_0(.49)>1/50\), since its numerator exceeds
\(3/50\) and its denominator is less than \(23/10\).
The last sine estimate follows directly from
\(\sin x>x-x^3/6\), \(157/50<\pi<22/7\).
For the first two rows in (18d), the least real shifted sums are
\(.42\) and \(.45\); use respectively the cotangent bounds
\(13/50\) and \(17/100\) from the cited scalar proof.
For the last row the sum is at least \(.50\).
Finally, \(C(u)>7/12\) on \([.10,.269]\), by the same
function's endpoint bounds and absence of an interior minimum.
Since \(\Re\tan\pi u>0\), this gives \(B>7/4\).
All four row-sum bounds therefore exceed \(1/100\).

For \(.45\le\Re t\le.50\), one has \(D,d\le0\),
\(p\ge0\), \(b>13/100\), \(q>1/50\), and \(B>7/4\).
The right-strip argument of the cited Lemma 1a gives \(-d>1/5\):
it uses only \(\Re(a+t)\in[.67,.95]\) and summed height at
most \(.24\). Dropping the remaining positive rank-one forms
in (18c) leaves
\[
 \operatorname{diag}(13/100,0,1/50,7/4)
       +\tfrac15(e_a+e_t)(e_a+e_t)^T
       \succ\tfrac1{100}I_4,
\]
where \(e_a,e_t\) are coordinate vectors. After subtracting
\(I_4/100\), the \(a,t\) block has positive diagonal entries
and determinant \(13/625\), and the other two diagonal entries
are positive. This includes \(\Re t=1/2\), where \(p=0\).
Adding back the omitted positive forms proves (18b). \(\square\)

The neighboring halfweight modification stated after Lemma 1 also
preserves (18b). This enlarged regular product supplies a wider
possible fixed contour; it does not assert any new flattened-face
or alias comparison.

## 4. Original critical point and the one controlled joint current

The unexponentiated endpoint map at own type four has exactly the
three derivatives \(\mathcal F_{1,e},\mathcal F_{1,t},\mathcal F_{1,u}\)
of (7). Thus its saved root, with its original logarithmic lift, is
a stationary point of the literal triple source. At that point
\[
 \mathcal F_1(a_*;e_*,t_*,u_*)=\mathcal P_1(a_*),\qquad
 \mathcal F_{1,a}(a_*;e_*,t_*,u_*)=\mathcal P_1'(a_*).
 \tag{19}
\]
One can also verify the first equality by substituting
\(S(e)=B(e,u_*(e))+i\pi eu_*(e)\) into
[the terminal action](research_mixed_terminal_transform_tails.md), equation (3).
This retains its full terminal diagonal, not the neighboring halfweight.

At fixed external \(a\), (14) makes the full holomorphic gradient
in \((e,t,u)\) injective on its convex product and its critical
point simple. At an actual reference fix all four imaginary parts
and vary their real parts independently within (11). Taylor integration
gives
\[
\begin{split}
 \Re\mathcal F_1(y+i\Im a_*; e,t,u)
 \le{}&\Re\mathcal P_1(a_*)+
       \Re\mathcal P_1'(a_*)(y-\Re a_*)\\
 &-\frac{\pi}{40}\bigl((y-\Re a_*)^2+
          (\Re e-\Re e_*)^2+(\Re t-\Re t_*)^2+
          (\Re u-\Re u_*)^2\bigr).
\end{split}
 \tag{20}
\]
No moving root at the independent real target is assumed.
On the broader product (18a), the same statement holds with the
quadratic coefficient \(\pi/200\), by (18b).

Choose inward half-grid cuts in the three real intervals (11), or
in the broader triple rectangle (18a).
Applying the original marked residue formula in each index is exact
on this retained triple rectangle and has constant-mode coefficient
\(+N^3\). Deform the three constant-mode paths to their actual
critical heights. Define \(Z_N^{HHH}\) to be the resulting
horizontal-horizontal-horizontal current, retaining \(+N^3\)
and the literal interpolation (6). At the actual external target,
with \(H_*=-\mathcal F_{1,(e,t,u)}''\), (9), (14), and (20)
give
\[
 Z_N^{HHH}(a_*,-2)=
 \frac{(2\pi)^{3/2}}{N^2}
 \frac{\mathcal A_1(a_*,e_*,t_*,u_*)}{\sqrt{\det H_*}}
 e^{N\mathcal P_1(a_*)}(1+O(N^{-1})).
 \tag{21}
\]
The Gaussian square root is the holomorphic accretive branch. Its
coefficient is nonzero. The power is exactly
\(N^3N^{-7/2}(2\pi/N)^{3/2}=(2\pi)^{3/2}N^{-2}\).
The original ordinary-color perturbation and stationary phase give a
holomorphic local color germ; each fixed ordinary derivative has
leading multiplier
\(N^j[-\tan(\pi u_*)/(4\pi)]^j\), which is nonzero.

Equation (21) describes only this horizontal current. The constant-mode
deformation has twenty-six additional joining currents, and the exact
three residue formulas also have all their single-, double-, and
triple-index aliases. Height convexity follows from (14), but their
endpoint comparisons have not been established here. The physical
complement includes both original support walls and still requires
uniform finite estimates. Consequently (21) is not an asymptotic for
the retained rectangular sum or the whole polynomial \(\mathcal V_1\).
It supplies an exact source and a common convex domain on which those
remaining comparisons can be formulated without a new critical-point
search or an invalid nested triangle bound.
