# Moving right-hand angles to the half-period endpoint in the complete row bound

Research proof, 5 November 2026. The neighboring target may be complex.
The comparison retains every row of the original finite sum. It reduces
the absolute row bound on the right half-period to a maximization over
the lower half of the row interval, with the right angle fixed at
\(1/2\). It does not replace an absolute row bound by a conditional
critical value.

## 1. The scalar comparison

Use the continuous, periodic real primitive
\[
 J(t)=\Re\frac{\operatorname{Li}_2(e^{-2\pi it})-\pi^2/6}{2\pi i},
 \qquad
 G_H(t)=\Re\frac{\operatorname{Li}_2(e^{-2\pi H-2\pi it})-\pi^2/6}{2\pi i},
 \qquad H\ge0.
 \tag{1}
\]
Thus \(G_0=J\), both functions are odd and one-periodic, and
\(J(1/2)=0\). Put
\[
 H_*=57/1000,\qquad c_*=-J(1/4)>0.
 \tag{2}
\]
Let \(x\in[1/2,1]\) be the real right-hand target, and let
\(y+ih\) be its other target, with \(0\le y\le1/2\) and
\(|h|\le H_*\). For a row fraction \(u\in[0,1]\), write
\[
 \begin{split}
 I_h(u,y)&=\int_0^u\log|1-e^{2\pi h-2\pi i(y+t)}|\,dt,\\
 R_{\epsilon,d}(u;x,y,h)
   &=I_0(u,x)+I_h(u,y)-(2+\epsilon)J(u)-2\pi d h u,
       \qquad \epsilon,d\in\{0,1\}.
 \end{split}
 \tag{3}
\]
Here \(d=1\) when the complex target is the first argument of the
original kernel. It records that kernel's chirp. The Fourier factors
and selected monomials at the fixed complex target are independent
of \(x,u\). The real right target has Fourier upper rate zero.
Consequently these factors do not affect the comparison below.

**Theorem 1.** Every upper row satisfies
\[
 R_{\epsilon,d}(u;x,y,h)
 <R_{\epsilon,d}(1/4;1/2,y,h)-3/50,
             \qquad 1/2\le u\le1.
 \tag{4}
\]
Moreover,
\[
 \max_{\substack{1/2\le x\le1\\0\le u\le1}}
          R_{\epsilon,d}(u;x,y,h)
 =\max_{0\le u\le1/2}R_{\epsilon,d}(u;1/2,y,h).
 \tag{5}
\]
The maxima and the bound include \(y=0\), zero height, and the
endpoint rows. Equation (5) concerns the complete absolute row
envelope. It asserts no lower bound for an oscillatory finite sum.

## 2. Three elementary estimates prove the upper-row loss

The [real right-angle calculation](research_mixed_right_pair_raw_reduction.md),
equation (4), gives
\[
 I_0(u,x)\le
 \begin{cases}
 J(u+1/2),&0\le u\le1/2,\\
 J(u),&1/2\le u\le1.
 \end{cases}
 \tag{6}
\]
The first line is attained at \(x=1/2\). To treat the second
line, put \(v=1-u\in[0,1/2]\), \(H=|h|\), and
\(\lambda=2\pi(h_+-dh)\). The exact modulus identity gives
\[
 I_h(u,y)=G_H(y+u)-G_H(y)+2\pi h_+u,
             \qquad 0\le\lambda\le2\pi H.
 \tag{7}
\]
Subtracting the value at \((u,x)=(1/4,1/2)\) from the upper
bound supplied by (6) therefore gives
\[
 G_H(y-v)-G_H(y+1/4)+(1+\epsilon)J(v)
       +\lambda(3/4-v)-(3+\epsilon)c_*.
 \tag{8}
\]
Since \(J(v)\le0\), it suffices to bound
\[
 D(y,v,H)=G_H(y-v)-G_H(y+1/4)+J(v)
                         +2\pi H(3/4-v)-3c_*.
 \tag{9}
\]

For \(0\le t\le1/2\), radial differentiation of (1) gives
\[
 \partial_HG_H(t)=\arg(1-e^{-2\pi H-2\pi it})\ge0,
                 \qquad J(t)\le G_H(t)\le0.
 \tag{10}
\]
The last upper bound follows by letting \(H\) tend to infinity.
Endpoint cases follow by continuity. No logarithm across the unit
circle is needed in this argument.

For fixed \(v,H\), the derivative in \(y\) of the difference
of the two \(G_H\) terms in (9) has the sign of
\[
 \cos 2\pi(y+1/4)-\cos2\pi(y-v)
 =-2\sin\pi(2y+1/4-v)\sin\pi(1/4+v).
 \tag{11}
\]
It follows that its maximum over \(y\in[0,1/2]\) occurs at
\(y=0\) or \(y=1/2\) if \(v\le1/4\). If
\(v\ge1/4\), it occurs at \(y=(v-1/4)/2\).
The derivative argument is initially made for \(H>0\); continuity
gives the same assertion at \(H=0\), including logarithmic zeros.

There are now only three estimates.

* At \(y=0\), \(0\le v\le1/4\), (10) implies
  \[
  D\le-G_H(1/4)+(3\pi/2)H-3c_*
     \le-G_{H_*}(1/4)+(3\pi/2)H_*-3c_*.
  \tag{12}
  \]
  Indeed the derivative in \(H\) of the middle expression is
  \(3\pi/2-\arctan(e^{-2\pi H})>0\).
* At \(y=1/2\), \(0\le v\le1/4\), all three terms
  \(G_H(1/2-v),G_H(1/4),J(v)\) are nonpositive. Hence
  \[
                 D\le(3\pi/2)H_*-3c_*.
  \tag{13}
  \]
* If \(1/4\le v\le1/2\), put \(t=(v+1/4)/2\).
  At the maximizing value of \(y\), (10) gives
  \[
  D\le -2J(t)+J(v)+\pi H_*-3c_*
       \le-2J(3/8)+\pi H_*-3c_*.
  \tag{14}
  \]
  For the second inequality, the derivative of
  \(-2J((v+1/4)/2)+J(v)\) is
  \(\log(2\sin\pi v)-\log(2\sin\pi t)\ge0\), because
  \(1/4\le t\le v\le1/2\).

The three bounds (12)--(14) are respectively approximately
\(-.0626723,-.1687352,-.0915114\). The accompanying scalar
check encloses each strictly below \(-3/50\) using outward
arithmetic. This proves (4). For lower rows (6) bounds the right
angle by \(1/2\); the upper rows have just been bounded by an
included lower row with a strict loss. The reverse inequality in
(5) follows by choosing \(x=1/2\). This proves Theorem 1.

## 3. Several right coordinates can be moved simultaneously

There is a simpler corresponding fact when both targets are right
coordinates. For \(x,y\in[1/2,1]\), (6) gives
\[
 \begin{split}
 I_0(u,x)+I_0(u,y)-(2+\epsilon)J(u)&\le-\epsilon J(u)\le0,
                                                   &&u\ge1/2,\\
 R_{\mathrm{RR}}(1/4;1/2,1/2)&=(4+\epsilon)c_*>0.
 \end{split}
 \tag{15}
\]
For lower rows both individual angular maxima occur at \(1/2\).
Thus the complete RR envelope also attains its maximum with both
right angles equal to \(1/2\) and its row in \([0,1/2]\).

Fix an original cyclic word, a set \(T\) of its right positions,
all the other real coordinates in \([0,1/2]\), and every selection.
On the original periodic hybrid contour, replacing any right real
coordinate by \(1/2\) leaves every other target unchanged: both
coordinates have left cutoff one, and both right heights are zero.
Let \(\mathcal E_{\rm raw}(x)\) be the sum of the complete raw
rates on edges incident to \(T\), plus the unchanged coherent
rates on all other edges where those rates are available. Then
\[
 \mathcal E_{\rm raw}(x)\le\mathcal E_{\rm raw}(x^{1/2}),
       \qquad x^{1/2}_j=1/2\quad(j\in T).
 \tag{16}
\]
One can instead keep any fixed upper bound for an edge outside
\(T\), including its original zero-collar bound: it is unchanged
by this operation. In (16) the edges incident to \(T\) still use
their **raw** rates after the replacement. They are not reclassified
as coherent half-period edges.

To prove (16), apply (5) to each AR or RA edge and (15) to each RR
edge. Their maximizing right angles agree, and the independent row
maxima are compatible. All Fourier factors at A positions are
unchanged; those at real R positions have upper rate zero, including
their selected monomials. The argument keeps the literal edges of
one- and two-cycles, so diagonal or parallel incidences pose no
exception.

If the rate is written relative to the original complex tangent
planes, the same conclusion holds after summing the incident edges.
The coefficient of each right coordinate in that sum is the sum of
its two critical derivatives, which is zero. The other target
coordinates remain fixed. Individual tangent-subtracted edge bounds
need not be maximized at \(1/2\); stationarity is used on their
complete sum.

## 4. The remaining row maximum is strictly concave

For fixed \(y,h\), the part of the reduced rate that depends on
the row is
\[
 E(u)=J(u+1/2)+G_H(y+u)-(2+\epsilon)J(u)+\lambda u,
       \qquad 0<u<1/2.
 \tag{17}
\]
**Proposition 2.** This function has exactly one maximum on
\([0,1/2]\), attained in its interior, and
\[
 E''(u)\le-2\pi,\qquad
 \max_{[0,1/2]}E
       \le E(u_0)+\frac{E'(u_0)^2}{4\pi}
                  \quad(0<u_0<1/2).
 \tag{18}
\]
In particular any interior trial row gives a certified upper bound
once its value and derivative have been enclosed. No row grid or
claim that the trial row is stationary is required.

Indeed
\[
 G_H''(t)=\frac{\pi\sin(2\pi t)}
                    {\cosh(2\pi H)-\cos(2\pi t)}.
 \tag{19}
\]
If \(t=u+y\le1/2\), this is at most
\(\pi\cot(\pi t)\le\pi\cot(\pi u)=J''(u)\).
If \(t\ge1/2\), it is nonpositive, whereas \(J''(u)>0\).
These cases exhaust \(0<t<1\). Therefore
\[
 E''(u)\le-\pi\tan(\pi u)-(1+\epsilon)\pi\cot(\pi u)
                                      \le-2\pi.
 \tag{20}
\]
The derivative tends to \(+\infty\) at zero and \(-\infty\)
at \(1/2\). When \(H=0,y=0\) or \(y=1/2\), the extra
logarithmic term has the same conclusion after its multiplicity is
combined with the other terms. Thus the maximum is unique and
interior. Taylor's inequality bounds \(E\) by
\(E(u_0)+E'(u_0)(u-u_0)-\pi(u-u_0)^2\); maximizing this
quadratic on the whole real line proves (18).

This argument concerns concavity in the row alone, with the other
target fixed. It does not require joint concavity in the target and
row, or a bound relating height to angle. The Fourier terms omitted
from (17) are constant in the row and can be restored unchanged.

## 5. What this leaves to prove

The original finite-product and absolute Fourier estimates turn these
raw rates into upper bounds with a polynomial prefactor and any fixed
positive exponential tolerance. They include all rows and both
parities, as proved in the
[whole-source reduction](research_mixed_right_half_source_reduction.md).
The scalar row \(u=1/4\) in the proof is a comparison value of a
continuous upper envelope; no finite coefficient at that row is used
as a lower bound, and no divisibility condition on \(N\) is needed.

The remaining right-interface comparison can therefore fix every
right real angle at \(1/2\) and bound its unique lower-row maximum
by (18). This removes the right angular variables and the need for
a row grid. It does not remove the gap between raw
row bounds and coherent conditional actions: that distinction is
essential even at the half-period endpoint. The full-period
asymptotic and the short-filling stability theorem remain open.

```sh
python3 experiments/check_mixed_complex_right_row_reduction.py
```
