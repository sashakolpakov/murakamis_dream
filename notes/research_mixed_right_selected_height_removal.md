# Removing a selected height in the right transition interval

Research proof, 5 November 2026. The analytic implication below reduces
a comparison between two Fourier choices to two bounds for an imaginary
derivative. The accompanying outward certificate is required for those
bounds. This is not a monotonicity assertion for the selected contour:
that stronger assertion has a counterexample.

## 1. The two incident phases

Use the original allocated block phase
\[
 \phi_{\eta\epsilon}(a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
       +2\pi ias-(1+\eta/2)g(a)-(1+\epsilon/2)g(b),
 \qquad
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
\]
Here \(\eta,\epsilon\in\{0,1\}\) specify types three and four,
respectively. The inner variable \(s\) is the unique original
logarithmic critical point of the block. Its branch is the one fixed in
the [conditional source theorem](research_mixed_transition_whole_period_source.md),
not an arbitrary root of the exponentiated equation.

The center has type four. With its neighbors fixed, write
\[
 F(a,b,c)=\phi_{\eta,1}(a,b)+\phi_{1,\gamma}(b,c),
 \qquad \eta,\gamma\in\{0,1\}.
\]
The subscript \(b\) denotes differentiation in the center variable.
The two neighbor variables need not be distinct in the original cycle;
allowing them to vary independently only enlarges the domain.

Define the following closed convex polygons:
\[
\begin{split}
 \Omega_3={}&\operatorname{conv}\{.1,.22-.03i,.45-.03i,.5,
                                   .45+.02i,.22+.02i\},\\
 \Omega_4={}&\operatorname{conv}\{.1,.22-.057i,.45-.057i,.5,
                                   .45+.014i,.12+.014i\},\\
 W_4={}&\operatorname{conv}\{.45-.057i,.5,.45+.014i\}.
\end{split}                                                    \tag{1}
\]
Put \(\Omega_j^{\ge .16}=\Omega_j\cap\{\Re z\ge .16\}\).
The early, plateau and right-transition conditional source theorems,
including the [left/right interface theorem](research_mixed_left_right_interface_source.md),
give the same holomorphic critical branch on these products. The
closed-cotangent uniqueness theorem identifies the branches on overlaps.
Thus the following boundary argument concerns a holomorphic function on
a neighborhood of the complete product, not just on its boundary.

**Derivative bounds.** For all four choices of \((\eta,\gamma)\),
\[
\begin{array}{ll}
 \Im F_b(a,b,c)>-3/5,&
 (a,b,c)\in\Omega_{3+\eta}\times W_4\times\Omega_{3+\gamma},\\[2mm]
 \Im F_b(a,b,c)>-9/20,&
 (a,b,c)\in\Omega_{3+\eta}^{\ge .16}\times W_4
                       \times\Omega_{3+\gamma}^{\ge .16}.
\end{array}                                                     \tag{2}
\]
These are the two numerical inequalities to be certified. For fixed
values of the other variables, \(\Im F_b\) is harmonic. Three
successive minimum principles reduce (2) to products of polygon edges.
There are 432 products in the first line and 507 in the second: clipping
\(\Omega_3\) creates seven edges, whereas the clipped \(\Omega_4\)
has six. None of those edges may be discarded.

## 2. The actual hybrid heights

Let \(t\in[.45,.5]\), put \(d=.5-t\), and set
\[
 R=400d^2,\qquad H=.014,\qquad
 s=\min\{L(x_-),L(x_+)\},\qquad f=\min\{6s,1\},
 \quad L(x)=\min\{1,(x-.1)/.12\}.
\]
The neighboring real coordinates \(x_-,x_+\) lie in \([.1,.5]\).
They carry their actual hybrid heights, hence
\(a\in\Omega_{3+\eta}\), \(c\in\Omega_{3+\gamma}\).
Let \(c_*\in[-.057,0]\) be the original unselected center height.
The two center targets are
\[
 b_u=t+i c_*sR,\qquad b_s=t+iHfR.                            \tag{3}
\]
Changing the center's selection does not change either neighboring
height: each cutoff is chosen by its own row. Every point of the vertical
segment joining (3) is in \(W_4\), because
\(R\le20d\). If \(s\ge1/2\), both neighboring real parts are
at least \(.1+.12/2=.16\). Consequently the appropriate line of
(2) applies to that entire vertical segment.

The full selected correction for the center is
\[
               \max\{\Re g(b_s),-2\pi\Im b_s\}.              \tag{4}
\]
It includes both alternatives in the actual Fourier-polynomial bound.
The neighbors' corrections agree on both sides of the proposed comparison
and cancel. No positivity of the quantum sum is assumed.

## 3. Comparison at the same real coordinate

Assume (2). Write \(h_u=c_*sR\), \(h_s=HfR\), and let
\(k=3/5\) when \(s\le1/2\), and \(k=9/20\) otherwise.
Since \(\partial_h\Re F(a,t+ih,c)=-\Im F_b(a,t+ih,c)\),
\[
 \Re F(a,b_s,c)-\Re F(a,b_u,c)
       \le k(h_s-h_u)\le k(Hf+.057s)R.                      \tag{5}
\]
For the branch \(-2\pi h_s\), use \(s\le f\) and \(k\le3/5\):
\[
 \Re F(a,b_s,c)-2\pi h_s-\Re F(a,b_u,c)
 \le-\kappa_F fR,
 \qquad \kappa_F=.028\pi-.0426>0.                           \tag{6}
\]

For the other branch put \(J(t)=\Re g(t)\) and
\(\lambda=\log(2\sin(.45\pi))\). On this real interval,
\(J(.5)=0\) and \(J'(t)=\log(2\sin\pi t)\ge\lambda\), so
\(J(t)\le-\lambda d\). Also \(\Im g'(t+ih)\ge0\) for
\(.45\le t\le.5\) and \(h\ge0\). Integrating vertically gives
\(\Re g(b_s)\le J(t)\). In the two cases of (2), respectively,
\[
\begin{split}
 k(Hf+.057s)R&\le (3/5)(.014+.057/2)\,400d^2
                                     \le .51d,\\
 k(Hf+.057s)R&\le (9/20)(.014+.057)\,400d^2
                                     \le .639d.
\end{split}
\]
Therefore
\[
 \Re F(a,b_s,c)+\Re g(b_s)-\Re F(a,b_u,c)
       \le-\kappa_G d,\qquad \kappa_G=\lambda-.639>0.        \tag{7}
\]
Combining (6)--(7) proves
\[
 \boxed{\quad
 \Re F(a,b_s,c)+\max\{\Re g(b_s),-2\pi h_s\}
 \le\Re F(a,b_u,c)-\min\{\kappa_F fR,\kappa_Gd\}.
 \quad}                                                     \tag{8}
\]
This holds with equality permitted at \(s=0\) or \(t=.5\).
It compares the two selections at the same real coordinate. A separate
unselected transport estimate is needed to move that coordinate down to
.45. Neither (8) nor a lower bound for an imaginary derivative proves a
whole-period asymptotic by itself.

For a cycle of length two, the two neighbors coincide but remain fixed,
so the argument applies directly. A cycle of length one requires a
different reading of its incidences. Its action is
\(G(b)=\phi_{11}(b,b)\), with one original edge, and
\(G'(b)=F_b(b,b,b)\). Along the vertical change of that one variable,
all three arguments lie in \(W_4\subset\Omega_4^{\ge .16}\).
Use the second bound in (2) and integrate \(-\Im G'\), with
\(s=f=1\). Equations (5)--(8) then hold with \(G\) in place of
\(F(a,\cdot,c)\). This counts the loop once and does not assert that
its neighboring incidences stay fixed.

## 4. What the certificate checks

The script below covers every edge product in (2) by exact dyadic
rectangles. On each rectangle it encloses both original logarithmic
critical points by affine Newton self-maps. It evaluates \(F_b\) at
the exact parameter midpoint and bounds its variation with the complete
Schur Hessians on the rectangle. A leaf is accepted only when this
outward lower bound exceeds the required value in (2). Floating roots
only propose centers; they do not decide acceptance. The saved binary
trees retain every subdivision and every root witness for a fresh replay.
The two scalar reserves in (6)--(7) are also checked outward.

```sh
python3 experiments/certify_mixed_right_selected_height_removal.py
```

The theorem depends on completion of that cover. A finite sample of
target parameters, including a successful optimization on each boundary
product, is insufficient.
