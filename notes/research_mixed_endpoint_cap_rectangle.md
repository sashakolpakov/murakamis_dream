# The ordinary endpoint coefficient on a rectangle for the outer sum

Research lemma, 5 November 2026. The manuscript is unchanged.

The private critical indices of an open three/four word lie in a region
where the ordinary endpoint coefficient already has a nonzero asymptotic
expansion. That region is too narrow for some proposed contours in the
next, outer summation. We extend the same coefficient to
\[
 E_{\mathrm{cap}}=[27/100,49/100]+i[-11/200,1/25].             \tag{1}
\]
The extension concerns the complete original endpoint coefficient. It
does not yet estimate the outer sum or prove that an open word has a
nonzero leading coefficient.

## 1. The finite function and the statement

We use precisely the function in the
[endpoint extension criterion](research_mixed_endpoint_packet_extension_criterion.md),
with the same sine factorial interpolation \(G_N\) and Newton
polynomials \(e_l(w)\):
\[
 C_N(e,w)=\sum_{l=0}^{N-1}
       \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)},\qquad
 S_l=\prod_{j=1}^l2\sin(\pi j/N).                           \tag{2}
\]
At \(e=j/N\), its terms with \(l>j\) vanish exactly. These
terms remain present when \(e\) is complex. The variable \(w\)
is the original ordinary boundary color, whose complete value is
\(-2\).

Let \(J(0)=0\), \(J'(z)=\Log(2\sin\pi z)\), on the
original branch continued from the real interval \((0,1)\), and set
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 u_c(e)&=\frac1\pi\arctan
          \frac{i+\sqrt{1-2e^{2\pi ie}}}{2},\qquad
 S(e)=F(e,u_c(e)).                                         \tag{3}
 \end{split}
\]
The square root and arctangent are the branches selected by the
original real-index critical point, not new choices made at each
parameter.

**Theorem 1.** On a fixed complex neighborhood of
\(E_{\mathrm{cap}}\times\{-2\}\),
\[
 C_N(e,w)=N^{-3/2}A(e,w)e^{NS(e,w)}(1+O(N^{-1})),
                    \qquad A(e,w)\ne0.                    \tag{4}
\]
Both integer level parities are included. The phase, amplitude and
Gaussian square root are those of the original endpoint theorem;
\(S(e,-2)=S(e)\) in (3). The relative error is holomorphic and
uniform with every fixed joint derivative on smaller neighborhoods.
No numerical width is asserted for the additional neighborhood or
the boundary-color disk.

## 2. The real tails on the enlarged rectangle

Write \(r=\Re e\), \(h=\Im e\),
\(h_+=\max(h,0)\), \(h_-=\max(-h,0)\), and choose the
same two cuts as in the earlier criterion:
\[
                    a=1/20,\qquad b=r-1/100.              \tag{5}
\]
The zero-safe upper exponent for each real row is
\[
 R(e,x)=\mathcal V(x)-J(x)-\Re J_{\mathrm{side}}(e-x)-\pi xh,
 \quad
 \mathcal V(x)=2\int_0^x\log(2|\cos\pi t|)\,dt-2J(x).
                                                                    \tag{6}
\]
Here \(J_{\mathrm{side}}\) is the same reflected reciprocal-factorial
primitive as in the earlier criterion. In particular (6) includes
rows beyond the physical cutoff and their zero limits.

For \(0<x<1/2\), away from a zero, its derivative is
\[
 \partial_xR=
 \log\frac{|\sin\pi(e-x)|\cos^2\pi x}{\sin^3\pi x}-\pi h.
                                                                    \tag{7}
\]
On \(0<x\le a\), the real part of \(e-x\) lies in
\([.22,.49]\). Thus the elementary lower bounds used previously
still apply: the sine modulus exceeds \(1/2\), the cosine square
exceeds \(1/4\), \(\sin\pi x<1/6\), and
\(e^{-\pi h}>1/2\). The exponential of (7) exceeds \(27/2\).

The upper tail now starts at \(b\ge.26\), below the old
\(.3\) cutoff. On the additional interval \(b\le x\le.3\),
one has \(-.03\le r-x\le.01\). The weaker bounds
\(|r-x|\le.05\), \(|h|\le.09\), and \(x\ge.24\)
are convenient. They give
\[
 \begin{split}
 |\sin\pi(e-x)|^2
     &\le\sin^2(.05\pi)+\sinh^2(.09\pi)<1/9,\\
 \frac{\cos^2\pi x}{\sin^3\pi x}
     &\le\frac{\cos^2(.24\pi)}{\sin^3(.24\pi)}<5/3,
 \qquad e^{-\pi h}<4/3.
 \end{split}
\]
The trigonometric quotient decreases on \((0,1/2)\), as follows
by differentiating its logarithm. Hence the exponential of (7) is
less than \(20/27<1\) on this extra interval. For
\(.3\le x\le1/2\), the former bound \(14/15<1\) applies
unchanged. The two inequalities also cover the case \(b>.3\).
At real zeros, integrate on both sides and use continuity.

The reflection argument for \(x\ge1/2\) also remains valid:
\(1/6<r<1/2\) and \(r+1/2<1\) throughout (1). Consequently
\[
 \begin{array}{ll}
 R(e,x)\le\Re F(e,a),&0\le x\le a,\\
 R(e,x)\le\Re F(e,b),&b\le x\le1/2,\\
 R(e,x)\le-\Re J(e)+2\pi h_-+(\pi/2)h_+,&1/2\le x\le1.
 \end{array}                                                     \tag{8}
\]
These are upper bounds for all the original finite rows, not only
for their values at integer indices.

## 3. Critical point, currents and the three gaps

The outward certificate accompanying this note proves, on the whole
rectangle (1),
\[
 .17<\Re u_c<.28,\qquad .001<\Im u_c<.1,
 \qquad a<\Re u_c<b,
 \qquad 0<\Re(e-u_c)<1/2.                                  \tag{9}
\]
The discriminant in (3) has real part greater than one. The exact
critical cubic, its quadratic factor, and the enclosure
\(-\pi<\Im F_u(e,u_c)<\pi\) prove the original equation
\(F_u(e,u_c)=0\), with zero logarithmic lift.

The same certificate proves
\[
 \begin{split}
 \Re S(e)-\Re F(e,a)&>1/5,\\
 \Re S(e)-\Re F(e,b)&>1/50,\\
 \Re S(e)+\Re J(e)-2\pi h_--(\pi/2)h_+&>1/3.
 \end{split}                                                  \tag{10}
\]
These are whole-rectangle inequalities. The proof uses the explicit
critical branch and interval bounds for the exact derivatives of
each difference, rather than values on a mesh alone.

For completeness, the contour argument of the earlier criterion does
not require its former numerical rectangle. It requires only (8)--(10)
and \(0<a<b<r<1/2\). On \(a\le\Re u\le b\),
\[
 -\Re F_{uu}=
 \pi\Re(2\tan\pi u+3\cot\pi u+\cot\pi(e-u))>0.
\]
The horizontal segment through \(u_c\) therefore has a unique
nondegenerate maximum. Vertical convexity bounds its two connecting
sides by their endpoints. The original lower-alias comparison is
\[
 \Re F(e,x-iy)-2\pi y
 \le\Re F(e,x+iy)-2\pi(1/2-r)y.                            \tag{11}
\]
Its coefficient is now at least \(\pi/50\), still positive.
The upper alias loses \(2\pi y\). Thus (9)--(11) retain every
piece of the same exact residue contour, while (8) and (10) control
all discarded real rows. Perturbing the cuts to half-grid positions
preserves the strict margins. The original Gaussian calculation and
the zero-safe ordinary-color bound then prove (4), with no change to
its scalar normalization. This proves Theorem 1.

## 4. Reproduction and scope

Run

```sh
python3 experiments/certify_mixed_endpoint_cap_rectangle.py
```

The checker binds the original endpoint certificate and its dependencies,
verifies the additional elementary upper-tail inequalities, and covers
the two rectangles obtained by splitting (1) at \(h=0\). Every
accepted cell checks (9), the zero lift and all three gaps. A saved
replay traverses the identical subdivision trees and cannot refine a
failed cell.

This rectangle permits an outer contour to extend left of the private
critical-index rectangle. The outer sum has its own tails, additional
Fourier terms and connecting contours. Theorem 1 supplies the inner
factor needed there; it does not bound those remaining contributions.
