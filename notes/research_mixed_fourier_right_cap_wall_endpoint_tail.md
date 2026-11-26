# An exact endpoint-tail bound after coherent outgoing contraction

Research deduction, 7 November 2026. The initialized Wall theorem
controls a genuine part of the original two-index finite source.
After its outgoing index is summed exactly, the highest retained-index
rows increase geometrically. Their complete absolute sum is therefore
bounded by twice the explicit final row. Zeros of the incoming finite
polynomial remain present; no division by a possibly vanished row is
used.

The result holds on a fixed positive-width endpoint strip for all
sufficiently large levels, of both parities. It does not require the
half-degree separation certificate. Comparison of the resulting true
endpoint rate with the full-cap reference plane remains open.

## 1. The exact remaining rows

Use the notation and lifted normalization of the
[Wall contraction](research_mixed_fourier_right_cap_wall_operator.md).
Let \(D=N-1\), \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and
\[
 X=e^{-2\pi ia},\qquad Y=e^{2\pi iy},\qquad
 a=x+ih,\quad x\in[.22,.45].
 \tag{1}
\]
The incoming height lies in its original compact interval; in
particular \(-.108\le h\le.068\) suffices for both actual types.
Keep \(y\) in the small neighborhood of \(x_0\) allowed by the
[initialized endpoint-strip theorem](research_mixed_fourier_right_cap_wall_endpoint_strip.md).
Define
\[
 c_N(y)=\frac{e^{-\pi iDy}(1-Y^N)}{N(1-Y)},\qquad
 T_{j,N}(a,y)=
       \frac{X^{-j}(rX;r)_j}{P_j^2}\,W_{N-j-1,N}(Y;Y).
 \tag{2}
\]
The literal cap is exactly
\[
                    V_N^{\rm F}(y,X)=c_N(y)\sum_{j=0}^D T_{j,N}.
 \tag{3}
\]
Each row in (2) already contains its *entire* original outgoing
sum over \(0\le l\le N-j-1\). In particular the outgoing
physical complement has not been bounded term by term.

There exist a fixed \(\delta>0\) and \(N_0\), after harmless
shrinking of the strip in the initialized theorem, such that
\[
 \delta\le\frac1{100},\qquad
 0<\left|\mathcal R_{n,N}(Y)\right|<8,
 \quad
 \mathcal R_{n,N}(Y)=\frac{W_{n,N}(Y;Y)}{W_{n-1,N}(Y;Y)},
 \quad 1\le n\le\delta N,\quad N\ge N_0.
 \tag{4}
\]
This is a consequence of that proved finite-solution theorem,
not an additional premise. Indeed
\[
 \left|\frac{1-2Y}{1-Y}\right|
       <\frac{1+2(123/200)}{1-123/200}
       =\frac{446}{77}<6.
\]
Continuity makes the local fixed ratio less than 7 in modulus;
its uniform \(O(1/N)\) error is less than 1 for large enough
\(N\). Nonvanishing is already part of the same theorem.

## 2. A zero-safe exact geometric increase

For \(j<D\), put \(n=N-j-1\). The original product recurrences
give the exact identity
\[
 T_{j+1,N}=
 \frac{X^{-1}-r^{j+1}}
      {(1-r^{j+1})^2\mathcal R_{n,N}(Y)}\,T_{j,N}.
 \tag{5}
\]
Within (4), its denominators are nonzero. The identity follows by
multiplying the polynomial \((rX;r)_j\) by \(1-Xr^{j+1}\),
not by dividing one value of that polynomial by another. Thus (5)
also holds when one or every row vanishes.

For all incoming heights in (1),
\[
                 |X^{-1}-1|\ge\sin(.44\pi)>\frac9{10}.
 \tag{6}
\]
To see this, write \(X^{-1}=Re^{2\pi ix}\), \(R>0\).
If \(.22\le x\le.25\), minimize the distance over \(R\ge0\)
to obtain \(\sin(2\pi x)\ge\sin(.44\pi)\). If
\(.25\le x\le.45\), the distance is at least 1.
Finally \(\sin(.44\pi)=\cos(.06\pi)>9/10\) follows from
\(\cos u\ge1-u^2/2\) and \(\pi<22/7\).

If \(1\le n\le\delta N\), then \(r^{j+1}=r^{-n}\) and
\[
 |1-r^{j+1}|\le2\pi\delta<\frac{11}{175},\qquad
 |X^{-1}-r^{j+1}|>
           \frac9{10}-\frac{11}{175}
           =\frac{293}{350}>\frac45.
 \tag{7}
\]
Together with (4),
\[
 |(1-r^{j+1})^2\mathcal R_{n,N}|
       <8\left(\frac{11}{175}\right)^2<\frac25.
 \tag{8}
\]
Equations (5)--(8) prove
\[
                       |T_{j+1,N}|\ge2|T_{j,N}|,
 \tag{9}
\]
with a strict inequality whenever \(T_{j,N}\ne0\).

Let
\[
 M_N=\lfloor\delta N\rfloor,\qquad J_N=N-1-M_N.
\]
All rounding is now explicit: the row degrees range from
\(n=M_N\) to zero. If \(M_N=0\), the following result is
immediate. Otherwise apply (9) successively to obtain
\[
 \left|c_N(y)\sum_{j=J_N}^D T_{j,N}\right|
       \le |c_N(y)|\sum_{j=J_N}^D|T_{j,N}|
       \le 2|c_N(y)T_{D,N}|.
 \tag{10}
\]
The final inequality is strict if the final row is nonzero.
If that row is zero, (9) proves that every row in this strip is
zero, so (10) still holds without qualification.

## 3. The exact endpoint and its surviving rate

Since \(W_{0,N}=1\), \(P_D=N\), and
\((rX;r)_D=(1-X^N)/(1-X)\), the endpoint in (10) is exactly
\[
 \boxed{\quad
 c_N(y)T_{D,N}=
 \frac{e^{-\pi i(N-1)y}(1-Y^N)
                 X^{-(N-1)}(1-X^N)}
      {N^3(1-Y)(1-X)}.
 \quad}
 \tag{11}
\]
Here \(X\ne1\) by (1), and \(|Y|<1\). The numerator
\(1-X^N\) is retained even at its zeros. This is the original
finite scalar and both original parity conventions, with no added
crossing scalar or power of \(N\).

On compact incoming heights and the fixed output neighborhood,
(10)--(11) imply the uniform bound
\[
 \left|c_N(y)\sum_{j=J_N}^D T_{j,N}\right|
       \le C N^{-3}
        \exp\left\{N\left[2\pi(-h)_++\pi\Im y\right]\right\}.
 \tag{12}
\]
Indeed \(|1-Y^N|\le2\), the two denominator factors in (11)
stay uniformly nonzero, and
\[
 |X^{-(N-1)}(1-X^N)|
          \le |X|^{-(N-1)}+|X|
          \le C_1e^{2\pi N(-h)_+}.
\]
The lifted Fourier exponential contributes the stated
\(\pi\Im y\) rate. Multiplication by any other exact factor
independent of \(j,l\) preserves (10), including at its zeros.
When the original admissible incoming halfweight is allocated,
its existing rate contribution is
\(-\eta\Re g(a)/2\), \(\eta=0,1\); no new allocation or
division by that finite factor is used here.

Thus (10) controls an actual positive-width portion of the original
high-inner-index, low-outgoing-index physical wedge. It sums the
outgoing index coherently first and only then takes the remaining
absolute row sum. It does not control the middle part of that wedge,
the other retained-index currents, or the comparison of
\(2\pi(-h)_++\pi\Im y-\eta\Re g(a)/2\) with the calibrated
right-cap plane. These are the remaining source obligations; no
whole-cap or knot-invariant lower bound is inferred.
