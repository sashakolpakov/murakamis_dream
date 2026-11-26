# Return prisms, their boundary signs, and real face gluing

Private geometric calculation, 1 November 2026. No repository source is changed.

This identifies a precise obstacle to applying the original real Casson–Rivin argument directly to an absolute maximizing return state. The continued local potential is the same periodic trigonometric expression, but its three ordered face cross-ratios are negative. The exact alternating coefficient sign supplies those negative signs. An absolute stationary return-to-complete interface therefore need not be an isometry of the original ordered gluing faces.

The inputs are the original ordered prism formulas in notes/actual_newton_ideal_prism_and_associativity.md and the exact return tensor in /private/tmp/md-fixed-newton-return-gates-and-contracted-tensor.md.

## 1. The original product coordinates in a return sector

Use ordinary multiplication coordinates \(x,y\) for the two input indices and \(b\) for the output. In the strict complete sector,
\[
p=b-x>0,\quad q=b-y>0,\quad r=x+y-b>0,\quad w=1-x-y>0.
\tag{1}
\]
The original prism gluing faces have the ordered cross-ratios
\[
\begin{aligned}
\kappa_x&=\frac{\sin(\pi x)\sin(\pi r)}
                  {\sin(\pi w)\sin(\pi p)},\\
\kappa_y&=\frac{\sin(\pi y)\sin(\pi r)}
                  {\sin(\pi w)\sin(\pi q)},\\
\kappa_b&=\frac{\sin(\pi p)\sin(\pi q)}
                  {\sin(\pi b)\sin(\pi r)}.
\end{aligned}
\tag{2}
\]
Their vertex orders are part of the literal tangle gluing. With those orders, all three ratios are positive in the complete sector and satisfy \(\log\kappa_u=-\partial_u m\).

In the interior of a return sector,
\[
0<x,y,b<1,\qquad b<x+y-1.
\tag{3}
\]
The exact finite support has \(k\le i+j-N\); (3) is its strict scaled form. It implies \(x,y>b\), and therefore
\[
-1<p,q,w<0,\qquad 1<r<2.
\tag{4}
\]
Both numerator and denominator signs in (2) are now determined. Since the sines of \(x,y,b\) are positive and those of \(p,q,w,r\) are negative,
\[
\boxed{\ \kappa_x<0,\qquad\kappa_y<0,\qquad\kappa_b<0.\ }
\tag{5}
\]
There is no limiting argument or square-root choice in this sign statement.

The rational six-vertex formulas remain meaningful away from collisions. What fails is the positive cyclic order that made each listed quadruple a supported gluing face of the original convex prism. A negative ratio cannot be made positive by applying a common Möbius transformation to the same ordered quadruple. Permuting its vertices can change its sign, but would change the prescribed tangle face map and must not be inserted silently.

## 2. The absolute return potential is the periodic continuation

Let \(J(u)=\int_0^u\log(2\sin\pi v)\,dv\) for \(0\le u\le1\), and extend it to the real line by
\[
\overline J(u)=\int_0^u\log|2\sin\pi v|\,dv.
\tag{6}
\]
Because \(J(1)=0\), this extension is one-periodic. It also satisfies \(J(1-u)=-J(u)\). Form
\[
\overline m(x,y,b)
 =\overline J(x+y)+J(b)-J(x)-J(y)
  -\overline J(b-x)-\overline J(b-y)-\overline J(x+y-b).
\tag{7}
\]
In the return sector, put \(a=1-x\), \(c=1-y\). Then \(a,c,b>0\) and \(a+c+b<1\). Periodicity and reflection give the exact identity
\[
\overline m(x,y,b)
 =J(a)+J(c)+J(b)+J(a+c+b)
  -J(a+c)-J(a+b)-J(c+b)
 =\mathcal R(a,c,b).
\tag{8}
\]
For example, \(\overline J(x+y)=-J(a+c)\),
\(\overline J(b-x)=J(a+b)\), and
\(\overline J(x+y-b)=-J(a+c+b)\).

Differentiating away from the integral endpoints gives
\[
\log|\kappa_x|=-\partial_x\overline m,\qquad
\log|\kappa_y|=-\partial_y\overline m,\qquad
\log|\kappa_b|=-\partial_b\overline m.
\tag{9}
\]
Thus the absolute return action controls the magnitudes of the original rational face metrics. It does not supply their signs.

## 3. The finite alternating sign supplies the missing phase

In fixed Newton coordinates the return coefficient of output \(k\) in \(e_i*_se_j\) has sign
\[
(-1)^{i+j-k},
\tag{10}
\]
apart from the common scalar \(-\Delta_s\). The corresponding scaled phase is
\[
i\pi(x+y-b).
\tag{11}
\]
If
\(\mathcal M_{\mathrm{ret}}=\overline m+i\pi(x+y-b)\),
then its three exponentiated negative derivatives are
\[
e^{-\partial_x\mathcal M_{\mathrm{ret}}}
 =-e^{-\partial_x\overline m},\quad
e^{-\partial_y\mathcal M_{\mathrm{ret}}}
 =-e^{-\partial_y\overline m},\quad
e^{-\partial_b\mathcal M_{\mathrm{ret}}}
 =-e^{-\partial_b\overline m}.
\tag{12}
\]
Equations (5), (9), and (12) agree exactly. This matches the actual coefficient sign with the ordered rational face ratios; it is stronger than a statement about their moduli.

The ordinary complete gluing map requires
\[
\kappa_{\mathrm{child}}\kappa_{\mathrm{parent}}=1.
\tag{13}
\]
A positive complete face and an interior return face have opposite signs. Even if stationarity of the absolute action gives equality of their metric magnitudes, their product is \(-1\), not \(1\). Such a real absolute stationary state therefore does not give the original ordered face isometry.

This conclusion is local and exact. It does not assert that the full signed contraction has a real saddle there, or that a complex stationary state cannot define a representation. It explains why the real absolute maximum cannot simply be assigned the original representation volume.

## 4. Boundary parity of an arbitrary connected return region

The sign localization does not require all internal edges to be turns. In covariant cubic coordinates a return vertex contributes
\[
(-1)^{i+j+r-d},\qquad d=N-1.
\tag{14}
\]
Let \(\mathcal C\) be any connected set of return vertices in a fixed cubic resolution. On each internal edge, either the two incident labels are equal, when a turn is present, or their sum is \(d\), for an unturned contraction. Let \(v(\mathcal C)\) be its number of vertices and \(u(\mathcal C)\) its number of internal unturned edges. Multiplying (14) over the region gives
\[
\boxed{\quad
\prod_{v\in\mathcal C}(-1)^{\sum_{e\ni v}i_{v,e}-d}
 =(-1)^{d(u(\mathcal C)-v(\mathcal C))}
       (-1)^{\sum_{e\in\partial\mathcal C}i_e}.
\quad}
\tag{15}
\]
Each turned internal edge contributes an even integer \(2i\), and each unturned one contributes \(d\). This proves the formula directly, including all endpoint indices. The remaining factors \((-\Delta_s)^{v(\mathcal C)}\) and the bounded paired turn weights are separate.

Hence every internal parity dependence cancels; the nonconstant alternating sign is on the boundary of the region. If the boundary label is expressed from the outside component instead, an unturned boundary identification changes it to \(d-i\), altering only the overall constant sign.

For positive old branches at these interfaces, the parity cannot be ignored when looking for a saddle of the signed sum. At an interior real critical point of the absolute branch action, a single return/complete boundary has an additional \(i\pi\) derivative, whereas an integer Fourier charge changes it by \(2\pi i\). This is the analytic counterpart of (13)'s sign failure. No uniform contour deformation or endpoint estimate follows from this observation alone.

## 5. Consequence for a whole-component geometric comparison

The one-cluster clamping result uses an actual alternative complete state and therefore avoids assigning a geometric representation to an absolute return maximizer. For a general component, the direct real representation-volume argument needs additional data: either a signed complex deformation that restores the original ordered metric equations, or a separate global action comparison that retains all boundary constraints.

The rational prism maps continue algebraically, but their continuation alone is not a degree-one geometric chain for the original exterior. In particular, absolute stationarity only proves (9), while the original face matching requires the signed equations (12)–(13). A volume bound for representations cannot be invoked until that distinction and any degenerate boundary configurations have been resolved.
