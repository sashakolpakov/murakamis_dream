# Mixed-phase concavity without height ordering

Research note, 3 November 2026. The complete-end-compensated mixed
phase has a larger proved concavity domain than originally stated:
its nonnegative heights need not be ordered. Two of the domain
conditions follow directly from the new geometric half-plane bound.
The real wire-order condition does not follow from the half-plane,
height and sector bounds alone. The example below demonstrates that
limitation. The separate
[coupled period proof](research_positive_path_real_wire_order.md)
now establishes this condition for every actual positive path with
integer powers at least three. The counterexample below does not
satisfy any asserted integer filling system.

## 1. Removing the height-order hypothesis

Use the phase and variables of
[the mixed-wire note](research_mixed_wire_phase_concavity.md):
\[
 \mathcal F_n(x,t)=b(x,t)+\psi(t,0)+\frac{int^2}{4\pi}-it,
 \quad x=a+iY,\quad s=\frac12-\frac{t}{2\pi}=b+iS,
 \quad
 \alpha(h)=\frac{\arccos(\operatorname{sech}(2\pi h))}{2\pi}.
 \tag{1}
\]
The scalar \(b=\Re s\) is distinct from \(b(x,t)\).

**Proposition 1.** Theorem 1 and Corollaries 2--3 of that note
remain valid with the height conditions replaced by
\[
                  Y,S\ge0,
 \quad\hbox{or, for the pair,}\quad Y,S_1,S_2\ge0,
 \tag{2}
\]
with no comparison between them. The real-domain conditions remain
exactly
\[
              \alpha(Y)<a<b<\frac12,\qquad \alpha(S)<b.
 \tag{3}
\]
For the pair, impose (3) for both \(b_i,S_i\).

*Proof.* The original factorial arguments have real parts in
\((0,1)\) under \(0<a<b<1/2\), independently of their imaginary
parts. Thus the original strip identities used in the Hessian
calculation do not require \(S-Y\ge0\).
Keep the exact quantities
\[
 u=\Re\cot\pi(s+x),\quad v=\Re\cot\pi(s-x),\quad
 w=\Re\cot\pi x,\quad d=\Re\csc\pi s .
 \tag{4}
\]
One has \(v,w,d>0\) regardless of the sign of \(S-Y\).
When \(a+b\ge1/2\), \(u\le0\), and the positive rank-one
decomposition in the original proof applies without any height
ordering. When \(a+b<1/2\), write
\[
 C(r,h)=\frac{\sin(2\pi r)}
                  {\cosh(2\pi h)-\cos(2\pi r)}.
 \tag{5}
\]
It decreases in \(h\ge0\), and decreases in \(r\in(0,1/2)\)
once \(r>\alpha(h)\). Starting from \((a,Y)\), increase the
real coordinate to \(a+b\) and the height to \(Y+S\);
this gives \(u<w\). Starting from \((b,S)\) gives
\(u<\Re\cot\pi s<d\). Only \(Y+S\ge Y,S\) was used.
The negative real Hessian is therefore
\[
 \pi(v+u)\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
           +2\pi\operatorname{diag}(w-u,d-u)>0.
 \tag{6}
\]
The same lower bound, segment integration, and addition of the
two vertex contributions prove all the cited quantitative
conclusions. \(\square\)

The [unsummed-network incidence theorem](research_unsummed_network_phase_coercivity.md)
already removes height ordering on its different domain
\(b\ge1/4\). Proposition 1 concerns the complete-end contribution
\(\psi(t,0)\) and retains the larger domain (3), which can have
\(b<1/4\). It does not add that complete-end contribution at a
general interior vertex.

## 2. Conditions supplied by the geometric spectral half-plane

Let \(t,u\) have real parts in \([0,\pi)\) and nonpositive imaginary
parts. Write
\[
 A=\cos^2(t/2),\qquad B=\cos^2(u/2),\qquad
               k=\frac{AB}{A+B}=\sin^2(\pi x).
 \tag{7}
\]
Suppose \(\Re A,\Re B>0\) and \(\Im A,\Im B\ge0\).
The selected algebraic wire branch is obtained by continuation
from \(A=B=1,\ x=1/4\). When at least one imaginary part is
positive, \(1/A+1/B\) has positive real and negative imaginary
parts. Hence \(k\) has positive real and positive imaginary parts.
The corresponding branch \(x=\pi^{-1}\arcsin\sqrt{k}\) satisfies
\(0<\Re x<1/2,\ \Im x>0\), and
\[
 \cos(2\pi\Re x)\cosh(2\pi\Im x)
       =\Re(1-2k)<1.
 \tag{8}
\]
Thus \(a>\alpha(Y)\). The real boundary case follows directly
whenever the selected wire remains in \(0<x<1/2\).

For a vertex angle \(t=\vartheta-iH\), put
\(s=b+iS=1/2-t/(2\pi)\) and \(w_t=-2\cos t\).
Then
\[
 \cos(2\pi b)\cosh(2\pi S)=\frac{\Re w_t}{2}.
 \tag{9}
\]
Consequently \(\Re w_t<2\) implies \(b>\alpha(S)\).
In particular the
[proved path bound](research_geometric_spectral_half_plane.md)
\(\Re w_t<7/4\) implies both this condition and
\(\Re A=(2-\Re w_t)/4>1/16\).

These deductions alone leave precisely
\[
                         \Re x<\min(\Re s_t,\Re s_u)
 \tag{10}
\]
to be checked. For the actual positive integer-power paths, the
linked coupled period proof supplies (10), so their critical points
do lie in (3). The following example explains why the coupled
equations are needed in addition to the separate bounds above.

## 3. An exact obstruction to deriving (10) from those bounds alone

Take
\[
          A=1,\qquad B=\frac3{10}+\frac35i,\qquad
          t=0,\quad u=2\arccos\sqrt B ,
 \tag{11}
\]
with \(0<\Re u<\pi\), \(\Im u<0\). Put \(u=\vartheta-iH\).
The selected wire is \(x=\pi^{-1}\arctan\sqrt B=a+iY\), since
\[
                  k=\frac{B}{1+B}=\frac{15+12i}{41}.
 \tag{12}
\]
All these branches are continued from the complete positive
branch in the upper right \(B\)-quadrant.

The explicit angular data are
\[
 \cosh H=\frac{3\sqrt5+\sqrt{85}}{10}<\frac85,\qquad
 \cos\vartheta=\frac{3\sqrt5-\sqrt{85}}{10},\qquad
 \left(\frac{\sinh H}{\sin\vartheta}\right)^2
                                      =\frac{9+\sqrt{17}}8<3.
 \tag{13}
\]
Thus \(0<H<23/20\), because
\(\cosh(23/20)>1+(23/20)^2/2>8/5\).
The color is \(w_u=4/5-12i/5\), so
\(\Re w_u<7/4\). The complete endpoint satisfies the corresponding
zero-height conditions. Both \(A,B\) have real part greater than
\(1/16\), and (8)--(9) hold.

Nevertheless (10) fails. For \(z=\sin^2(v+ih)\),
\[
                     \cos(2v)=|1-z|-|z|.
 \tag{14}
\]
Applying this to (12), and to
\(\pi s_u=\pi/2-u/2=\arcsin\sqrt B\), gives
\[
 \cos(2\pi a)=\frac{2\sqrt5-3}{\sqrt{41}}<\frac{15}{64},
 \qquad
 \cos(2\pi\Re s_u)=\frac{\sqrt{85}-3\sqrt5}{10}>\frac14.
 \tag{15}
\]
The first rational bound uses \(\sqrt5<9/4\) and
\(\sqrt{41}>32/5\).
For the second, squaring
\(\sqrt{85}>5/2+3\sqrt5\) reduces again to
\(\sqrt5<9/4\). Since both real angles in (15) belong to
\((0,\pi)\), strict decrease of cosine proves
\[
                 a>\Re s_u,\qquad
                 a-\Re s_u>\frac1{128\pi}.
 \tag{16}
\]
The last bound follows from the cosine gap \(>1/64\) and
\(|\cos'|\le1\). The elementary bounds
\(\sqrt5<9/4,\sqrt{85}<37/4\) also prove the upper bound
on \(\cosh H\) in (13). No approximate root calculation is used.

The violation is strict. Perturbing \(A=1\) a sufficiently small
distance into the upper right quadrant preserves it and all the
strict bounds, and gives a second angle with positive real part
and negative imaginary part. This is still only a counterexample
to an inference from the displayed angle bounds.
No integer powers or filling charges have been imposed in (11).
In particular it is not a counterexample to (10) for an actual
positive integer-filled path. The subsequent
[wire-order theorem](research_positive_path_real_wire_order.md)
proves (10) on that actual family by using its coupled original period
equations, together with a new maximum principle for the cosine moduli.

The phase extension in Proposition 1 likewise supplies no
finite-source coefficient or global contour estimate. Its use
still requires locating the actual saddle in its real domain
and retaining the other original cycle contributions.
