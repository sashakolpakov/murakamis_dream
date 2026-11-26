# Nine concave face comparisons for the complete contracted physical tail

Research deduction, 7 November 2026. The full physical-index
complement of the contracted three-four source is bounded by one
already small far tail and nine strictly concave face maxima.
There is no parameter grid and no new reference family in this
reduction. The nine maxima have not been evaluated here.

Retain \(E,\Omega,T,K,\rho,M\) from
[the original contracted source](research_mixed_contracted_pair_rectangle.md)
and [outer-index elimination](research_mixed_contracted_pair_outer_index_elimination.md).
In particular \(X=Y=K\), and all cardinal terms and three
physical support faces remain part of the source. Define
\[
 C=[1/4,9/20]^2\times[1/5,21/50]^2,
 \quad
 R=[0,9/20]\times[0,1/2]^2\times[0,21/50],
 \tag{1}
\]
in the coordinate order \((s,t,p,q)\).

## 1. Move internal tails to their original central faces

The preceding reduction proves
\[
 \max_T E\le
 \max\{2261/1500,\ \max_{R\setminus\operatorname{int}C}E\},
 \qquad 2261/1500<M-1/200.
 \tag{2}
\]
Its outer clips stop at \(s=9/20,q=21/50\); its internal
clips stop at \(t=p=1/2\). These points remain on or outside
the original central-box faces. We now work entirely in \(R\).

If \(0<t\le1/4\), the exact derivative satisfies
\[
 e^{E_t}=
 [\cos\pi s+\cot\pi t\sin\pi s]
 [\cos\pi p+\cot\pi t\sin\pi p]\ge1.
 \tag{3}
\]
Indeed \(\cot\pi t\ge1\), and \(\cos\pi u+\sin\pi u\ge1\)
for \(0\le u\le1/2\). Hence increasing a low \(t\) to
\(1/4\) does not decrease \(E\). Both adjacent support sums
remain below one. Continuity handles \(t=0\).

Next suppose \(0<p\le1/5\), now with \(1/4\le t\le1/2\).
Since \(q\le21/50<1-2p\),
\(\sin\pi(p+q)\ge\sin\pi p\). Also
\(p+t\in[1/4,7/10]\), so
\[
 e^{E_p}=
 \frac{\sin\pi(t+p)\sin\pi(p+q)}{2\sin^3\pi p}
 \ge\frac{\sin(\pi/4)}{2\sin^2(\pi/5)}>1.
 \tag{4}
\]
The last inequality is \(2\sqrt2+\sqrt5>5\), which follows
from \(\sqrt2>7/5\) and \(\sqrt5>11/5\).
Increasing \(p\) to \(1/5\) therefore increases the rate
and preserves support. Again the zero endpoint follows by continuity.

For \(9/20\le t\le1/2\), with \(1/5\le p\le1/2\),
the numerator sines in the first line of equation (13) of the
preceding reduction satisfy
\(\sin\pi(s+t)\le1\) and
\(\sin\pi(t+p)\le\sin(3\pi/5)<24/25\).
Moreover \(\sin\pi t\ge\cos(\pi/20)>49/50\). Thus
\[
                          e^{E_t}<\frac{2400}{2401}<1.
 \tag{5}
\]
For completeness, \(\sin^2(3\pi/5)=(5+\sqrt5)/8<(24/25)^2\)
follows already from \(\sqrt5<9/4\); the cosine bound follows
from \(\cos x\ge1-x^2/2\) and \(\pi<22/7\).
Decrease any high \(t\) to \(9/20\).

Finally, for \(21/50\le p\le1/2\),
\(\sin\pi p\ge\cos(2\pi/25)>9/10\), by the same
elementary cosine bound. Therefore
\[
                          e^{E_p}\le\frac1{2\sin^3\pi p}
                                             <\frac{500}{729}<1.
 \tag{6}
\]
Decrease any high \(p\) to \(21/50\). These upper clips
also preserve support. Each changed coordinate stops at its
original central boundary, and subsequent steps do not move it
off that boundary. Thus every point of the tail still carries
at least one tail label after these operations.

## 2. The remaining outer exits and strict face concavity

We now have \((t,p)\in[1/4,9/20]\times[1/5,21/50]\).
Section 6 of outer-index elimination proves that a low outer
\(s\in[0,1/4]\) can be replaced, without decreasing \(E\),
by either \(0\) or \(1/4\). It also proves that increasing
any \(q<1/5\) to \(1/5\) increases \(E\).
The upper outer exits were already stopped at \(9/20,21/50\).

Consequently each tail point, except for the far region paid in
(2), is bounded by a point on \(\partial C\), or on
\[
 F_0=\{s=0,\ t\in[1/4,9/20],\ p,q\in[1/5,21/50]\}.
 \tag{7}
\]
If a previous clip supplied the tail label, it remains on its
boundary; if the only label was a low \(s\), the two alternatives
are precisely a central face or \(F_0\). There is no substitution
of an interior point for a lost tail label.

The eight faces of \(C\) are strictly concave for \(E\),
because on real indices \(E=\Re\mathcal F\) and the whole
rectangle theorem gives \(-\Re\mathcal F''\succ0\).
The extra face also has a strictly concave phase. Write
\(V(u,v)=J(u+v)-J(u)-J(v)\) for real arguments and
\(L(q)=q\log\rho-\mathcal I_K(q)\). Then exactly
\[
 E|_{s=0}=-\log\rho+V(t,p)+V(p,q)-J(p)+L(q).
 \tag{8}
\]
Each real ideal-triangle pair has a positive definite negative
Hessian on the displayed ranges, by the triangle criterion.
The own term \(-J(p)\) is concave, and
\[
 L''(q)=\frac{2\pi\Im(Ke^{-2\pi iq})}{|1-Ke^{-2\pi iq}|^2}<0
 \tag{9}
\]
because \(q\ge1/5>\Re x_0\) and \(q-\Re x_0<1/2\).
Thus (8) is strictly concave in its three free coordinates.

Its \(t\)-maximum is explicit:
\[
 t=\frac{1-p}{2}\in[29/100,2/5],\qquad
 \max_tE|_{s=0}=
 -\log\rho-2J((1-p)/2)+J(p+q)-3J(p)-J(q)+L(q).
 \tag{10}
\]
This follows either from the exact supported-fiber theorem or
directly from \(\sin\pi(t+p)=\sin\pi t\).
The resulting two-variable function is strictly concave: its
negative Hessian is the positive Schur complement of that in (8).

## 3. The exact remaining finite comparison

Let \(F_1,\ldots,F_8\) be the eight closed faces of \(C\).
Then
\[
 \boxed{\quad
 \max_T E\le
 \max\left\{\frac{2261}{1500},\
                  \max_{0\le j\le8}\max_{F_j}E\right\}.
 \quad}
 \tag{11}
\]
Every face maximum on the right is a maximum of a smooth strictly
concave function on a fixed closed rectangle. Its exact finite
support is therefore bounded by the tangent at any chosen point
\(y\) of that face:
\[
 \max_{F_j}E\le E(y)+\sum_{i\ {\rm free}}
  \max\{E_i(y)(L_i-y_i),E_i(y)(U_i-y_i)\}.
 \tag{12}
\]
For \(F_0\) one may instead use the two-variable function in
(10). All signed derivative terms and the original cardinal rate
remain in (12). No optimizer existence certificate is needed to
validate such a tangent bound.

Thus nine rigorous tangent comparisons below the original action
would complete the entire physical-index complement, with (2)
already paying its far region. No such tangent values have been
evaluated in this note. The nonmain complex contour currents remain
a separate whole-source obligation even after the physical-tail
comparison succeeds.
