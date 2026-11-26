# The absolute geometric value of the adjacent three-crossing action

Research proof, 3 November 2026.

The selected action in the remaining double contraction has the
absolute volume normalization of the original two filled circles.
This identifies its value; it does not assert that the original
remaining contour has a nonzero contribution from that point.

The proof uses the already identified primitive boundary period and
a degeneration on the same algebraic curve. The boundary correction
is retained at that degeneration. In particular, logarithms are not
reset to principal values along the comparison path.

## 1. The two local actions

Use the positive source \(JM^3JM^3\mathbf e_0\). Its geometric
configuration is the reflected complex conjugate of the negative
\((-3,-3)\) configuration in
[the marked branch note](research_three_crossing_pendant_geometric_branch.md).
The two selected original degrees are \(1,2\); the last circle
remains free, with angle \(u\).

Write
\[
 \begin{split}
 r(\tau)&=\tau^2-3\tau+3,&
 z(\tau)&=4-5\tau+4\tau^2-\tau^3,\\
 v(\tau)&=(\tau-2)^2(\tau^2-2\tau+2),&
 X&=1/r(\tau),\qquad
 Y=\frac{r(\tau)}{z(\tau)r(\tau)-1}.
 \end{split}                                                     \tag{1}
\]
The selected point \(\tau_*\) is the root near
\(0.944-1.303i\) of \(v(\tau)=-2i\). On its free-boundary germ,
\[
 v(\tau(u))=-2i\cos(u/2),\qquad
 x=\frac{\operatorname{Log}r(\tau)}{2\pi i},\qquad
 y=\frac{\operatorname{Log}Y}{2\pi i}.                            \tag{2}
\]
The logarithms at \(u=0\) are exactly those fixed in
[the remaining-saddle dictionary](research_three_crossing_geometric_remaining_saddle.md).
In particular
\[
 x_*\in(3/10,1/3)+i(-1/10,0),\qquad
 y_*\in(1/5,1/4)+i(0,1/10).
\]

Let \(J'(\xi)=\operatorname{Log}(2\sin\pi\xi)\), with the original
positive-strip normalization \(J(0)=0\), and set
\[
 \begin{split}
 b(y,u)={}&J(1/2+u/(2\pi))+J(1/2-u/(2\pi))\\
 &-J(1/2-y+u/(2\pi))-J(1/2-y-u/(2\pi))-2J(y).
 \end{split}                                                     \tag{3}
\]
These are the original Newton evaluation factors. The normalization
of the actual complex column, including its retained chirp, is
proved in Section 7 of
[the complex next-step theorem](research_three_crossing_complex_next_step.md).
It gives
\[
 \begin{split}
 \mathcal W(x,y;u)={}&I(x)+J(x+y)-4J(x)-2J(y)+b(y,u)\\
 &+\frac{i\pi}{2}\{(x-y)^2-x+y\},\\
 I'(x)&=\operatorname{Log}\lambda(x),\qquad I(0)=0,\qquad
 \lambda=-\frac{(\tau-2)^3}{r(\tau)} .
 \end{split}                                                     \tag{4}
\]
At \(u=0\), \(b(y,0)=J(2y)-4J(y)\), so (4) is exactly
the phase of the certified remaining saddle.

The original angular action is
\[
 \mathcal G(u)=\operatorname{stat}_{\alpha,\beta}
 \left\{\psi(\alpha,\beta)+\psi(\beta,u)
       +\frac{3i}{4\pi}(\alpha^2+\beta^2)-i(\alpha+\beta)\right\}.
                                                                    \tag{5}
\]
Its full primitive equations, rather than only their exponentials,
are
\[
 r_{\alpha,\beta}=\frac{3i}{2}\alpha-\pi i,\qquad
 r_{\beta,\alpha}+r_{\beta,u}=\frac{3i}{2}\beta-\pi i .
                                                                    \tag{6}
\]
Here \(r_{s,t}=\operatorname{arsinh}(\tan(s/2)\cos(t/2))\)
on the original continued branch, and
\(\psi_s=-r_{s,t}/\pi\).

**Theorem 1.** On the selected complex neighborhood of \(u=0\),
\[
 \operatorname{stat}_{x,y}\mathcal W(x,y;u)
                      =\mathcal G(u)+i c_0
                  \quad\hbox{for some }c_0\in\mathbb R.             \tag{7}
\]
Consequently, at the complete free boundary,
\[
 \boxed{\quad
  2\pi\Re\mathcal W(x_*,y_*;0)
       =\operatorname{Vol}(M_{3,3})
       =\operatorname{Vol}(M_{-3,-3}).
 \quad}                                                          \tag{8}
\]
The manifolds in (8) are the original partially filled exteriors,
with their main cusps and the remaining auxiliary cusp complete.
Reflection accounts for the last equality. No closing filling,
new boundary framing, or extra carrier is included in (8).

## 2. The already marked boundary differential

Put \(w=e^{iu}\). Direct differentiation of (3) gives
\[
 b_u(y,u)=\frac1{2\pi}
       \operatorname{Log}\frac{1+Yw}{Y+w}.                         \tag{9}
\]
At \(u=0\) this logarithm is zero. The source stationarity equations
on (1)--(2) can be checked before taking logarithms:
\[
 e^{\mathcal W_x}
       =\frac{\lambda X(X-Y)}{Y(1-X)^4}=1,\qquad
 e^{\mathcal W_y}
       =\frac{Y(Y-X)(Y+w)(Y+w^{-1})}{(1-Y)^4}=1.                  \tag{10}
\]
The first identity holds identically in \(\tau\); the second is
the trace identity \(w+w^{-1}=-2-v(\tau)^2\).
The full logarithmic equations at \(u=0\) were calibrated in the
remaining-saddle note. Thus they remain zero on the selected germ
and on every regular continuation of it.

Conjugating the original negative-clock period identity in the
marked branch note, with the corresponding reflection of angles,
gives the positive-source identity
\[
 e^{2r_{u,\beta}}=\frac{Y+w}{1+wY},\qquad r_{0,\beta}=0.
                                                                    \tag{11}
\]
This uses the original ordered interface and primitive curves,
not an unmarked trace comparison. Equations (9)--(11) therefore
give the equality of full logarithms
\[
 b_u=-\frac1\pi r_{u,\beta}=\mathcal G'(u).                         \tag{12}
\]
The envelope derivative of the stationary value of (4) is \(b_u\).
Hence the difference in (7) is a complex constant. It remains
to prove that its real part is zero.

## 3. A useful fact about the factorial primitive

We will use limits on continued branches, not merely principal
branches.

**Lemma 2.** Let \(m\in\mathbb Z\).

1. Every finite continuation of \(J(\xi)\) toward \(\xi=m\)
   has a finite, purely imaginary limit.
2. If \(u\) stays near a fixed value for which
   \(1/2\pm u/(2\pi)\notin\mathbb Z\), then on any fixed continued
   branch, as \(y\to m\),
   \[
    b(y,u)=i\ell u+i c+o(1),\qquad b_u(y,u)=i\ell+o(1),
       \qquad \ell,c\in\mathbb R.                                \tag{13}
   \]
   The errors are locally uniform in \(u\).

**Proof.** The only zeros of \(2\sin\pi\xi\) are the simple
zeros at integers. A circuit changes a branch of \(J\) by
\[
                  2\pi i(k\xi-l),\qquad k,l\in\mathbb Z.           \tag{14}
\]
This follows either by integrating the changed logarithm or by
integrating \((\xi-n)^{-1}\) at each integer \(n\).
On a reference path along the real axis, with small detours around
integers, the real integral across each unit interval is
\(\int_0^1\log(2\sin\pi s)\,ds=0\).
Thus its limit at every integer is purely imaginary. Formula (14)
proves the same assertion on any continued branch. The logarithmic
singularity is integrable.

For integer \(m\), periodicity of sine gives, on arbitrary
fixed branches,
\[
                 J(a)-J(a-m)=i d\,a+i e,\qquad d,e\in\mathbb R.
                                                                    \tag{15}
\]
Indeed the derivative is a purely imaginary constant; its
integration constant is purely imaginary by evaluating at a
regular real \(a\). Apply (15) to
\(a_\pm=1/2\pm u/(2\pi)\) in (3), and use the first assertion
for \(J(m)\). This proves the first limit in (13).
All four shifted arguments stay away from integers; differentiation
there proves the second limit, locally uniformly. \(\square\)

## 4. Continue to a zero-volume degeneration

The normalization of \(I\) has a particularly simple continuation.
In the simply connected region
\[
                  \Re\tau<3/2,\qquad \Im\tau<0,                   \tag{16}
\]
neither \(r(\tau)\) nor \(\lambda(\tau)\) vanishes. The two zeros
of \(r\) lie on the line \(\Re\tau=3/2\), and the only zero of
the numerator of \(\lambda\) is \(2\).
Choose their logarithms by continuation from \(\tau=1\), where
both are \(1\). The one-form
\[
              \frac{\operatorname{Log}\lambda}{2\pi i}
                         \,d\operatorname{Log}r                  \tag{17}
\]
has a single-valued primitive in (16), extending near \(1\)
with value zero. It is the function \(I\) in (4): the selected
characteristic branch and its endpoint normalization are the
ones proved in the complex next-step theorem.
Explicitly, the real-\(x\) segment followed by the downward
complex-\(x\) segment used there has
\(\tau=(3-\sqrt{4/X-3})/2\); its selected square root has
positive real and positive imaginary parts away from \(x=0\).
Thus that defining continuation stays in (16).

Continue from \(\tau_*\) toward \(1\) within (16).
All angle multipliers and all original shape parameters are
algebraic functions of \(\tau\). Their nonconstant zero, pole and
chart-divisor sets are finite. They are regular at the selected
point. A path can consequently be chosen to avoid them before
its endpoint; lift it to the algebraic cover carrying the selected
half-angle signs and \(w\). All original logarithms and all
factorial logarithms are continued along that same path.
No positivity is required along this comparison path.

The limiting source coordinates are
\[
            r\longrightarrow1,\qquad Y\longrightarrow1,\qquad
            x\longrightarrow0,\qquad y\longrightarrow m
                              \quad(m\in\mathbb Z),\qquad I\to0.
                                                                    \tag{18}
\]
The integer \(m\) allows the actual winding of \(Y\); it is
not silently replaced by zero. Since \(v(1)=1\),
\[
                 \cos(u/2)\longrightarrow i/2.                  \tag{19}
\]
Thus the continued \(u\) has a finite limit, with nonzero cosine;
the shifted factorial arguments in Lemma 2 are not integers.
The path can be taken to be a finite regular path followed by
a short algebraic approach to \(1\), so all the logarithmic
windings mentioned here are finite.

For the original geometry write
\[
 c=\cos(\alpha/2),\qquad d=\cos(\beta/2).
 \]
The full geometric dictionary gives
\[
 c^2=\frac{2-\tau}{4},\qquad
 d=-i(1-\tau)c,\qquad
 \mathfrak q_{\alpha,\beta}=-i\frac{\tau+1}{\tau-1}.               \tag{20}
\]
It follows that \(c\to\pm1/2\), \(d\to0\).
The first tangent stays finite, while
\(\tan(\beta/2)\to\infty\). The outside tangent remains finite
by (19). More explicitly, the squares of these two finite
tangents tend to \(3\) and \(-5\), respectively; neither finite
tangent tends to \(i\) or \(-i\).

Here this also proves that the signed cell volume tends to zero,
rather than merely asserting that some angle degenerates.
For an edge with tangents \(a,b\), its eight original shapes are
\[
 \left(A,B,-1/A,-1/B,C,D,-1/C,-1/D\right),
 \]
\[
 A=\frac{\mathfrak q+a}{b-i},\quad
 C=\frac{\mathfrak q-a}{b-i},\quad
 B=-\frac{\mathfrak q-b}{a+i},\quad
 D=-\frac{\mathfrak q+b}{a+i},\qquad
 \mathfrak q^2=1+a^2+b^2.                                      \tag{21}
\]
If just \(b\to\infty\) and \(a\) has a finite limit different
from \(\pm i\), then \(\mathfrak q/b\to\pm1\);
the two sums \(\mathfrak q\pm b\) tend respectively to
infinity and zero. Every shape in (21) therefore tends to
one of \(0,1,-1,\infty\). The same conclusion holds with
the endpoints interchanged. These conditions apply to both
original edges here. The Bloch--Wigner function is continuous
and zero at those limiting values. Consequently
\[
                         V_{\rm cells}^{\rm sgn}\longrightarrow0.
                                                                    \tag{22}
\]

## 5. The boundary correction fixes the real constant

The signed continuation of the
[original edge-volume identity](research_positive_edge_volume_identity.md),
Section 9, applies to this path. Summing its two edges and using
the continued full equations (6) cancels the selected-vertex
corrections against the quadratic and linear terms in (5).
Only the outside correction remains:
\[
 V_{\rm cells}^{\rm sgn}
      =2\pi\Re\mathcal G-2\Im u\,\Im r_{u,\beta}.                 \tag{23}
\]
This calculation retains both original cells, both primitive
unit charges and the free boundary.

By Lemma 2 and (18), all the terms of (4) except \(b(y,u)\)
have purely imaginary limits. The polynomial in (4) has this
property because \(x\to0\) and \(y\to m\in\mathbb Z\).
Using (12), (13), (22) and (23), we obtain
\[
 \begin{split}
 2\pi\Re(\mathcal W-\mathcal G)
 &=2\pi\Re\mathcal W
       -V_{\rm cells}^{\rm sgn}-2\Im u\,\Im r_{u,\beta}\\
 &\longrightarrow
   2\pi\{\Re(i\ell u+i c)+\Im u\,\Im(i\ell)\}=0 .
 \end{split}                                                     \tag{24}
\]
The left side is constant by (12), so it is identically zero.
This proves (7).

At \(u=0\), the original geometry is positive and has the
original primitive filling periods. The accepted marked
completion theorem therefore identifies the sum of the sixteen
cell volumes with the volume of the actual partial exterior.
The outside correction vanishes. Equation (8) follows.

The proof determines the real constant, which is what the
volume comparison needs. It does not determine the remaining
purely imaginary constant \(i c_0\), or a finite-level unit
scalar from it.

For later attachment, the original boundary periods are therefore
\[
 U_0=-2\pi\,\frac{d}{du}\operatorname{stat}\mathcal W,
 \qquad V=2iu.
\]
An original outside carrier \(\eta_b\), when present, changes this
to \(U=U_0-i\eta_bu\), exactly as in the marked branch note.
Its quadratic action term is inserted once, after combining the
incident pieces. The comparison above requires no change of the
original meridian, disk longitude or carrier.

## 6. Consequences for the local boundary theorem

The exact outward
[selected-action certificate](../experiments/verify_three_crossing_closing_action.py)
and its [saved result](../repro/results/research-three-crossing-closing-action.json)
give
\[
 1.53735693993859
       <\Re\mathcal W(x_*,y_*;0)
       <1.53735694249979 .
 \]
The certificate alone was an action computation; Theorem 1 is
the separate proof of its geometric interpretation.

The
[whole preparation-error theorem](research_three_crossing_global_preparation_error.md)
is therefore below the geometric rate by more than \(3/100\)
on a fixed sufficiently small complex boundary neighborhood.
The separate
[full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
now proves that the selected contribution has a nonzero coefficient
in the original finite source, with all remaining contours and real
tails below its rate. That coefficient follows from the exact
contour identity and its bounds; it is not inferred from the
geometric character or the action normalization.
