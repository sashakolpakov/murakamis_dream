# Tail-preserving clips for the enlarged contracted-pair box

Research deduction, 7 November 2026. Enlarge the coherent real index
box of the original three-four contraction to
\[
 C'=[1/4,1/2]\times[1/5,9/20]\times[1/5,21/50]^2,
 \qquad T'=\Omega\setminus\operatorname{int}C',
 \tag{1}
\]
in the coordinate order \((s,t,p,q)\). The physical rate \(E\),
three-face support \(\Omega\), original parameter \(K\), and
calibrated action \(M\) are exactly those of
[the contracted source](research_mixed_contracted_pair_rectangle.md).
No source row, phase constant, or failed old comparison is changed.

This note proves the tail reduction for (1). Concavity on the enlarged
complex rectangle and quantitative bounds on its faces are separate
requirements. The new box places the two previously offending real
face neighborhoods inside the coherent integral; it does not improve
a tangent on the old physical complement.

## 1. The global high tails and the low shared index

Section 5 of
[outer-index elimination](research_mixed_contracted_pair_outer_index_elimination.md)
already proves, on the whole original physical region,
\[
             p\ge5/6\quad\Longrightarrow\quad
             E<2261/1500<M-1/200.
 \tag{2}
\]
Its proof first decreases \(s\) to at most \(9/20\), but (2)
is a bound on the original point. No membership in either central
box is needed for that already paid region.

For every remaining point of \(T'\), use the original derivative
barriers in the same note as follows. If \(s>1/2\), decrease it
to \(1/2\), using \(E_s<0\) for \(s\ge9/20\).
If \(q>21/50\), decrease it to \(21/50\), using the original
four-vertex high-index barrier. Decrease \(t>1/2\) to \(1/2\),
and \(1/2<p<5/6\) to \(1/2\), using its equation (13).
All these moves increase or preserve the rate, preserve support,
and retain any changed coordinate on or outside its new central
interval. The resulting point lies in
\[
 R'=[0,1/2]^3\times[0,21/50]\subset\Omega.
 \tag{3}
\]
The two sums \(s+t,t+p\) are at most one, and \(p+q\le.92\).
Continuity handles their boundary faces.

For \(0<t\le1/5\), the literal derivative obeys
\[
 e^{E_t}=
 [\cos\pi s+\cot\pi t\sin\pi s]
 [\cos\pi p+\cot\pi t\sin\pi p]\ge1.
 \tag{4}
\]
Indeed \(\cot\pi t\ge1\), and
\(\cos\pi u+\sin\pi u\ge1\) for \(0\le u\le1/2\).
Raise every low \(t\) to \(1/5\). Both adjacent support sums
remain below one. At \(t=0\), use continuity rather than a
singular logarithmic derivative.

Next decrease any \(p>21/50\) to \(21/50\). The unchanged
estimate \(e^{E_p}<500/729\) on \([21/50,1/2]\) proves that
this increases the rate, independently of the other supported
coordinates. We now have
\(1/5\le t\le1/2\) and \(0\le p,q\le21/50\).

## 2. Raise a low \(p\) without assuming \(t\ge1/4\)

The exact derivative is
\[
 e^{E_p}=
 \frac{\sin\pi(t+p)\sin\pi(p+q)}{2\sin^3\pi p}.
 \tag{5}
\]
For \(0<p\le1/5\), the positive sine is concave in
\(t\in[1/5,1/2]\). Its endpoint values satisfy
\[
 \sin\pi(p+t)\ge
 \min\{\sin\pi(p+1/5),\ \cos\pi p\}
                                      >2\sin^2\pi p.
 \tag{6}
\]
For the first endpoint, \(2p\le p+1/5\le2/5\) gives
\(\sin\pi(p+1/5)\ge\sin(2\pi p)
 =2\sin\pi p\cos\pi p>2\sin^2\pi p\), since \(p<1/4\).
For the second, exactly
\[
 \cos\pi p\ge\cos(\pi/5)=\frac{1+\sqrt5}{4}
 >\frac{5-\sqrt5}{4}=2\sin^2(\pi/5)
 \ge2\sin^2\pi p,
 \tag{7}
\]
where the strict comparison is equivalent to \(\sqrt5>2\).

For every \(0\le q\le21/50\), one has \(q<1-2p\).
Thus \(p+q\in[p,1-p]\) and
\(\sin\pi(p+q)\ge\sin\pi p\). Equations (5)--(7) prove
\[
                 e^{E_p}\ge
                 \frac{\sin\pi(t+p)}{2\sin^2\pi p}>1.
 \tag{8}
\]
Raise every low \(p\) directly to \(1/5\), even when
\(q\) is also low. Continuity includes \(p=0\); a singular
logarithmic derivative is not used at that endpoint. During this
move \(t+p\le7/10\) and \(p+q\le31/50\), so support
is preserved.

Now \(p\in[1/5,21/50]\). The unchanged low-\(q\) barrier
in Section 6 of outer-index elimination raises any \(q<1/5\)
to \(1/5\). That proof uses the original parameter inequalities
of [the four real-complement theorem](research_power_four_real_complement.md)
and has no dependence on \(t\). This last move also preserves
support, including at \(q=0\).

## 3. Finish the clips while retaining the tail label

We now have \(p,q\in[1/5,21/50]\). For
\(9/20\le t\le1/2\), the unchanged high-\(t\) estimate
\[
                 e^{E_t}<2400/2401<1
 \tag{9}
\]
still holds: \(\sin\pi(s+t)\le1\),
\(\sin\pi(t+p)\le\sin(3\pi/5)<24/25\), and
\(\sin\pi t>49/50\). Decrease such \(t\) to \(9/20\).
Finally, for a low \(s\in[0,1/4]\), equation (16) of
outer-index elimination replaces it by either zero or \(1/4\),
without decreasing the rate. Its proof requires only
\(0\le t\le1/2\), so it applies to the new interval.

Every changed coordinate stops at its own boundary in (1), except
for the permitted alternative \(s=0\). No subsequent operation
moves that coordinate off its new boundary. For example a low
\(t\) stops at \(1/5\) and never meets the high-\(t\) test;
a low \(p\) or \(q\) stops at \(1/5\), while each high
one has already stopped at \(21/50\). Thus a point initially
outside \(\operatorname{int}C'\) cannot lose its tail marker.

Define
\[
 F'_0=\{s=0,\ t\in[1/5,9/20],\ p,q\in[1/5,21/50]\}.
\]
The complete conclusion is
\[
 \boxed{\quad
 \max_{T'}E\le
 \max\left\{\frac{2261}{1500},
                  \max_{\partial C'}E,\ \max_{F'_0}E\right\}.
 \quad}
 \tag{10}
\]
The extra face is still strictly concave by its exact decomposition
\(E|_{s=0}=-\log\rho+V(t,p)+V(p,q)-J(p)+L(q)\).
Its unique \(t\)-optimizer remains \((1-p)/2\in[29/100,2/5]\),
strictly inside the enlarged interval. Thus its same two-variable
elimination is available. Concavity of the other eight enlarged
faces is not inferred from the clipping argument.

Equation (10) is an original-source reduction at the same reference.
It neither asserts that its unevaluated face bounds are negative
nor estimates the complex lattice corrections. The earlier failed
physical-tail certificate remains a valid recorded failure for its
smaller coherent box.
