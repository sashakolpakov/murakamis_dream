# A necessary endpoint slope for the complex-symbol weight

Private exact-symbol deduction, 9 November 2026. Near Fourier frequency
\(1/2\), two explicit tests of the full complex symbol give a necessary
linear upper bound on every admissible height. The neighborhood is fixed
but is not quantified. This concerns the direct symbol criterion only:
it neither bounds the signed observation nor rules out a sufficient
weight on the rest of the interval. No mathematical numerical evaluation
or frozen-source edit is used.

## 1. Exact square and a uniform necessary height bound

Keep the symbol and finite Fourier convention of
[the full-shift theorem](research_mixed_next_outer_full_shift_low_frequency_inverse.md)
and [the complex-symbol weight theorem](research_mixed_next_outer_complex_symbol_weights.md):
\[
p(u,t)=(2-2\cos u)^3d(u,-e^{3iu+2\pi it})
        =\sum_{\ell=-11}^{11}p_\ell(t)e^{i\ell u}.
\tag{1}
\]
The direct positivity condition under consideration is
\[
\Re p(u-i\lambda,t)>0\qquad(u\in\mathbb R),\quad\lambda>0.
\tag{2}
\]
No shift sign or original carrier is changed.

Put \(x=u/2\), \(\theta=\pi t\), and
\[
\begin{split}
W(x,\theta)
 &=[4\cos^2x\cos^2(3x+\theta)+\sin^2x]\cos(2x+\theta)\\
 &\hspace{12mm}+2\cos x\cos(3x+\theta)\sin^2x,\\
F(x,\theta)&=\cos x\,W(x,\theta).
\end{split}
\tag{3}
\]
Then the exact entire identity is
\[
\boxed{\quad p(u,t)/256=\sin^6x+F(x,\theta)^2.\quad}
\tag{4}
\]
For a direct source check, set
\[
k=\cot x\cos(3x+\theta),\quad h=-\sin(3x+\theta),\quad
w_1=k-h,\quad w_3=(4k^2+1)w_1+2k.
\]
The original cubic uses
\(\ell=2+4k^2\), \(m=2+4\cos^2x\,w_1^2\).
The identity
\[
\cos^2x\,w_1^2-2\cos^2x\,kw_1=\cos^2x-k^2
\]
reduces it to \(d=4+4\cos^2x\,w_3^2\).
Since \(\sin^3x\,w_3=W(x,\theta)\), multiplication by
\(64\sin^6x\) proves (4). Formula (3) removes the apparent
singularities and licenses complex \(u\).

The highest positive frequency of \(F\) is \(11/2\), occurring only
in \(4\cos^3x\cos^2(3x+\theta)\cos(2x+\theta)\), with coefficient
\(e^{3i\theta}/16\). Hence
\[
                         p_{11}(t)=e^{6\pi it}.
\tag{5}
\]
For real \(u,t\), (3) gives \(|W|\le7\), so
\(0\le p(u,t)\le12800\). If (2) holds, the positive function
\(f(u)=\Re p(u-i\lambda,t)\) has mean \(p_0(t)\) and Fourier
coefficient \(p_{11}(t)\cosh(11\lambda)\). Consequently
\[
\cosh(11\lambda)\le p_0(t)\le12800,\qquad
                  \lambda\le\frac{\log25600}{11}.
\tag{6}
\]
This follows from the integral triangle inequality for the positive
function \(f\). It does not replace the symbol by a coefficient
triangle estimate; it supplies a necessary uniform bound on every
admissible height.

## 2. Endpoint sign and the cubic normal form

At \(t=1/2\), set \(u=-i\lambda\), \(h=\lambda/2>0\).
Then \(\sin x=-i\sinh h\), \(\cos x=\cosh h\),
\(\cos(3x+\pi/2)=i\sinh3h\), and
\(\cos(2x+\pi/2)=i\sinh2h\). Thus \(W=-iV_h\), where
\[
V_h=(4\cosh^2h\,\sinh^23h+\sinh^2h)\sinh2h
                    +2\cosh h\,\sinh3h\,\sinh^2h>0.
\]
Equation (4) gives the exact strict sign
\[
\boxed{\quad
p(-i\lambda,1/2)
=-256\{\sinh^6h+\cosh^2h\,V_h^2\}<0\qquad(\lambda>0).
\quad}
\tag{7}
\]
By (6), compactness, and continuity, admissible heights tend uniformly
to zero as \(t\to1/2\). Otherwise an admissible sequence would have a
subsequence converging to a positive height contradicting (7).

Write
\[
\delta=\pi(1/2-t),\qquad w=(u-i\lambda)/2.
\]
The exact polynomial (3) has the Taylor expansion
\[
F(w,\pi/2-\delta)
 =4\delta^3-32\delta^2w+87\delta w^2-80w^3
                         +O((|w|+|\delta|)^5).
\tag{8}
\]
Indeed its degree-three terms are exactly
\[
[4(\delta-3w)^2+w^2](\delta-2w)+2(\delta-3w)w^2,
\]
using \(\cos(3w+\pi/2-\delta)=\sin(\delta-3w)\) and the
corresponding identity with \(2w\). All omitted terms have degree
at least five. Since \(\sin^3w=w^3+O(|w|^5)\),
\[
\frac{p(u-i\lambda,t)}{256}
 =w^6+\{4\delta^3-32\delta^2w+87\delta w^2-80w^3\}^2
                          +O((|w|+|\delta|)^8).
\tag{9}
\]
This is a uniform ordinary analytic remainder on a fixed complex
neighborhood, with no finite-level approximation.

The degree-three polynomial factors exactly:
\[
Q(z)=4-32z+87z^2-80z^3
                   =-(5z-2)(16z^2-11z+2).
\tag{10}
\]
It retains the full correlated complex-symbol degeneration.

## 3. Two explicit negative tests

For \(\delta>0\), set \(y=\lambda/(2\delta)\). At the real
observation \(u=\delta/2\), one has \(w=\delta(1/4-iy)\).
The real leading term in (9), divided by \(\delta^6\), is
\[
f_{1/4}(y)
 =\frac{145}{4096}-\frac{5743}{256}y^2
                     +\frac{20639}{16}y^4-6401y^6.
\tag{11}
\]
For example
\(Q(1/4-iy)=3/16-27y^2+i(7y/2-80y^3)\) verifies all
coefficients directly. As a polynomial in \(X=y^2\), its second
derivative is \(20639/8-38406X>0\) on \(0\le X\le1/64\).
At \(y=1/23\), drop the negative last term and use
\[
\frac{145}{4096}<\frac{37}{1024},\quad
\frac{5743}{256\cdot529}>\frac{43}{1024},\quad
\frac{20639}{16\cdot529^2}<\frac5{1024}.
\]
The latter two follow by replacing \(529\) respectively with \(530\)
and \(528\), and comparing \(22972>22790\) and \(20639<21780\).
At the other endpoint the exact value is
\[
f_{1/4}(1/8)=-\frac{6453}{262144}<-\frac1{1024}.
\]
Convexity therefore proves
\[
             f_{1/4}(y)<-\frac1{1024}
                          \qquad(1/23\le y\le1/8).
\tag{12}
\]

For larger \(y\), use \(u=2\delta/3\). Now the real leading
polynomial is
\[
f_{1/3}(y)
 =\frac2{729}-\frac{31}{27}y^2+\frac{472}{3}y^4-6401y^6.
\tag{13}
\]
Here \(Q(1/3-iy)=1/27-7y^2+i(2y/3-80y^3)\).
Writing (13) as \(G(X)\), \(X=y^2\), gives
\[
G'(X)=-31/27+(944/3)X-19203X^2,\quad
G''(X)=944/3-38406X.
\]
For \(X\ge1/64\), \(G''<0\), and
\(G'(1/64)<-31/27+5-4=-4/27<0\).
The exact initial value is
\[
f_{1/3}(1/8)=-\frac{229849}{729\cdot262144}<0.
\]
Thus \(f_{1/3}(y)<0\) for all \(y\ge1/8\). Continuity and its
negative leading coefficient also give a fixed \(c_1>0\) with
\[
f_{1/3}(y)\le-c_1(1+y^6)\qquad(y\ge1/8):
\tag{14}
\]
the quotient is strictly negative and tends to \(-6401\).

## 4. Necessary slope and the remaining accumulated weight

**Theorem.** There is a fixed \(\delta_0>0\) such that, for
\(0<\delta=\pi(1/2-t)<\delta_0\), condition (2) implies
\[
\boxed{\qquad
\lambda<\frac{2\delta}{23}
                  =\frac{2\pi}{23}(1/2-t).
\qquad}
\tag{15}
\]

*Proof.* Every admissible height tends uniformly to zero by (6)--(7).
Suppose \(\lambda\ge2\delta/23\). If
\(1/23\le y\le1/8\), use (11)--(12) at \(u=\delta/2\):
the leading real term is at most \(-\delta^6/1024\), whereas
the error in (9) is \(O(\delta^8)\). It is negative for small
\(\delta\). If \(y\ge1/8\), use (13)--(14) at
\(u=2\delta/3\). For a fixed \(c_2>0\), the leading real term
is at most
\[
-c_1\delta^6(1+y^6)\le-c_2(\delta+\lambda)^6,
\]
while the error is \(O((\delta+\lambda)^8)\). It too is negative
as the admissible \(\delta,\lambda\) tend to zero. Both cases
contradict (2), with one uniform sufficiently small \(\delta_0\).
\(\square\)

Therefore every positive Lipschitz weight satisfying the direct
symbol condition on \([a,\alpha]\), contained sufficiently near
\(1/2\), obeys
\[
\boxed{\quad
\int_a^\alpha\lambda(t)\,dt
 <\frac{\pi}{23}
       \{(1/2-a)^2-(1/2-\alpha)^2\}.
\quad}
\tag{16}
\]
If positivity is imposed up to the open endpoint, the remaining
contribution is at most \(\pi(1/2-a)^2/23\).

This is a necessary local restriction on the specific sufficient
complex-symbol criterion. No explicit size of its endpoint
neighborhood is supplied. A height below (15) is not thereby
certified admissible. In particular, the result neither limits the
accumulated gain on the rest of the interval nor proves an obstruction
to the actual action budget or signed functional.

## Frozen source bindings

- Full finite-shift convention and Fourier degree:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
- Direct complex-symbol criterion and accumulated weight:
  858546c9a2762175c32c1ef7b6dd62385051335a613665c9ff1848e0af711ff1.
- Original all-character cubic symbol:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Original odd square and endpoint regularization:
  244a089f0046f1a8b81f55941c17c32304eb3fd679aa933361ebacbfa416f9a8.

