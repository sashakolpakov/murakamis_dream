# The complete low physical tail beside the first cap

Research deduction, 7 November 2026. On the actual enlarged early
taper, the low rows of the adjoining ordinary conditional factor
increase geometrically up to index \(1/5\). Consequently their entire
absolute sum costs less than 201 times one original physical row.
This is an exact finite-source bound, valid at every level and for
both own types; it does not require a moving critical point or a
complex-neighborhood packet. The central and high-index parts remain
separate.

## 1. Original source and actual target domain

Let the first attached target and its next ordinary outgoing target be
\[
 a=x+ih_a,\qquad b=z+ih_b,
 \qquad .1\le x\le .22,\quad .1\le z\le .5,
 \tag{1}
\]
with
\[
 -.108\le h_a\le .021,\qquad
 -.102\le h_b\le .068.
 \tag{2}
\]
These are containing bounds for all four actual unselected first/second
type combinations in
[the first-attached eligibility theorem](research_mixed_first_attached_taper_root_eligibility.md),
Section 3. In particular they contain the correlated minimum-cutoff
targets, including the quadratic upper cutoff and any additional
attenuation in \([0,1]\). If the first moving real coordinate is a
minimum in \([.1,.22]\), its next coordinate automatically satisfies
the lower real bound in (1). No estimate for a next coordinate below
\(.1\) is inferred here.

For \(N\ge2\), put
\[
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib}.
\]
The literal conditional source is
\[
 C_{\epsilon,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b),\qquad
 R_{j,N}=X^{-j}\frac{p_j(X)p_j(Y)}{P_j^{\,2+\epsilon}},
 \qquad \epsilon\in\{0,1\}.
 \tag{3}
\]
This is the original normalization used in
[finite source transport](research_mixed_three_first_source_transport.md),
equation (3). The first chirp, all physical rows, and all rows that
revive off the grid remain present. No factorial or Fourier factor
is inserted into or divided out of (3).

## 2. A uniform exact ratio

**Lemma 1.** For \(0<u\le1/5\),
\[
 \begin{split}
 D_\epsilon(u;a,b):={}&
 \log\left|\frac{\sin\pi(a+u)}{\sin\pi u}\right|
 +\log\left|\frac{\sin\pi(b+u)}{\sin\pi u}\right|\\
 &-\epsilon\log(2\sin\pi u)+\pi(h_b-h_a)
 >\frac1{200}.
 \end{split}
 \tag{4}
\]

*Proof.* For any \(v\in[.1,.5]\), positivity and concavity of sine
on the interval \([u+.1,u+.5]\subset(0,1)\) give
\[
 \frac{\sin\pi(u+v)}{\sin\pi u}
 \ge \min\left\{
 \cos(\pi/10)+\cot\pi u\sin(\pi/10),\ \cot\pi u
 \right\}
 \ge\cot(\pi/5)>\frac43.
 \tag{5}
\]
For the first entry, decrease \(\cot\pi u\) to \(\cot(\pi/5)\)
and use \(\sin(3\pi/10)=\cos(\pi/5)\). The second entry has
the same endpoint bound. An imaginary shift only increases the
sine modulus, since
\[
 |\sin\pi(v+u+ih)|^2
       =\sin^2\pi(v+u)+\sinh^2\pi h.
\]
The strict numerical comparisons in (5) and below are elementary
pentagon identities:
\[
 \cot^2(\pi/5)=1+\frac2{\sqrt5}>\frac{16}{9},
 \qquad
 \sin^2(\pi/5)=\frac{5-\sqrt5}{8}<\frac9{25}.
 \tag{6}
\]
They reduce respectively to \(324>245\) and \(3125>2809\).
Thus \(2\sin\pi u<6/5\). For either value of \(\epsilon\),
\[
 -\epsilon\log(2\sin\pi u)>-\log(6/5).
\]
Since \(h_b-h_a\ge-123/1000\), equations (5)--(6) give
\[
 D_\epsilon>
       \log(40/27)-\frac{123\pi}{1000}>\frac1{200}.
 \tag{7}
\]
For completeness, the last strict comparison needs no logarithm
evaluation. The positive atanh series and \(\pi<22/7\) give
\[
 \begin{split}
 \log(40/27)&>
       2\left\{\frac{13}{67}+
                      \frac13\left(\frac{13}{67}\right)^3\right\}
       =\frac{354536}{902289},\\
 \frac{354536}{902289}-\frac{123}{1000}\frac{22}{7}
                       -\frac1{200}
       &=\frac{8577851}{6316023000}>0.
 \end{split}
 \tag{8}
\]
This proves (4). \(\square\)

Let \(L_N=\lfloor N/5\rfloor\). Every factor in the numerator
of \(R_{j,N}\), for \(0\le j\le L_N\), is nonzero: the real
parts of its two sine arguments lie in \([.1,.42]\) and
\([.1,.7]\), respectively, strictly between consecutive integer
zeros. Also \(P_j\ne0\) for \(j<N\). The exact product recurrence
therefore gives
\[
 \frac{|R_{j+1,N}(a,b)|}{|R_{j,N}(a,b)|}
 =\exp D_\epsilon((j+1)/N;a,b)>e^{1/200},
               \qquad 0\le j<L_N.
 \tag{9}
\]
The chirp in (3) is essential: it is precisely what changes the
exponential height contribution to \(\pi(h_b-h_a)\) in (4).

**Theorem 2.** Uniformly on (1)--(2), for both types and every
integer \(N\ge2\),
\[
 \boxed{\quad
 \left|\sum_{j=0}^{L_N}R_{j,N}(a,b)\right|
 \le\sum_{j=0}^{L_N}|R_{j,N}(a,b)|
 <201\,|R_{L_N,N}(a,b)|.
 \quad}
 \tag{10}
\]

Indeed (9) bounds the sum by
\(|R_{L_N,N}|\sum_{k\ge0}e^{-k/200}\).
Since \(e^{1/200}>201/200\), the infinite geometric sum is
strictly less than 201. If \(L_N=0\), (10) is immediate.
No asymptotic approximation, parity restriction, or cancellation
assumption enters (10).

## 3. The joint first-cap source and the surviving obligations

For fixed retained \(a,b\), the entire first-cap factor and every
allocated exterior Fourier factor are independent of the ordinary
index \(j\). Multiply (10) by the modulus of their exact product,
or by their original nonnegative halfweight allocations. The resulting
non-strict bound with constant 201 holds with every factor and
allocation unchanged, and is strict when the common multiplier is
positive. Thus it also holds when a finite factor vanishes; no division
by its value is involved. The complete joint first-cap/ordinary low
physical tail is controlled by one literal row at a constant cost.

Its exponential-rate form is also explicit. Define the complete
bare real-row rate
\[
 \begin{split}
 E_\epsilon(u;a,b)={}&
 \int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt
 +\int_0^u\log|1-e^{-2\pi i(b+t)}|\,dt\\
 &-(2+\epsilon)J(u)-2\pi h_a u,
 \qquad J(u)=\Re g(u).
 \end{split}
 \tag{11}
\]
The original uniform factorial/product estimates give
\(|R_{L_N,N}|\le C N^A e^{N E_\epsilon(1/5;a,b)}\), after
changing the constant for the \(O(1/N)\) rounding. The numerator
arguments remain in the fixed regular intervals just listed, and
the denominator retains its usual endpoint \(O(\log N)\) error.
In particular no integrable-zero or revived-row issue is hidden
in this inference. Equation (4) also proves directly that the
continuous low-tail maximum is its value at \(u=1/5\).

One may therefore put the left half-grid cut just after \(L_N\)
in a subsequent exact contour decomposition. All rows below that
cut are already exhausted by (10). Their multiplication with the
new [complete early-cap envelope](research_mixed_cap_early_taper_envelope_transport.md)
uses the same actual target \(a\), including its true endpoint
branch and original first weight.

This result does not place the cut rate (11) below the calibrated
joint reference plane. Nor does it bound the central ordinary
current or the high physical rows. Those obligations must retain
the actual adjacent target, original marginals, middle compensation
and relative pinning fee. The previously proved conditional-root
eligibility supplies none of these missing finite-source signs.
There is no whole left-boundary or whole-word conclusion here.
