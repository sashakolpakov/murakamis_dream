# Independent read of the stable-section cap bound and tilted certificate

This is a bounded independent audit of
[the uniform protected-spectrum proof](md-protected-stable-section-uniform-spectral-gap.md)
and the tilted-pressure verifier. It concerns the exact finite estimate
and its use of the original complete action. It is not an audit of every
other source sector or a new filling theorem.

## 1. Finite spectral metric

The cutoff is \(M=\lfloor N/2\rfloor-1\), with \(d=N-1\). Thus
\(2M=N-2\) at even levels and \(2M=N-3\) at odd levels. The
sine-Cauchy integral has every moment required by a degree-\(M\)
polynomial squared. Its last diagonal entry is exactly one at even
levels and \(1/(2\cos(\pi/N))\le1\) at odd levels, including \(N=3\).

The bidiagonal matrix has distinct real diagonal entries on this
cutoff. The stated relation \(AC=CA^T\) gives self-adjointness in the
\(C^{-1}\) metric. The divided difference is a polynomial also at
spectral nodes; \(\chi_N(A)=0\). Its real-interval norm is bounded by
\(\sup|\chi_N'|\le N^2\). On \([0,1]\), the integral density is at
least \(1/\pi\), and the shifted-Legendre evaluation inequality gives
\((C^{-1})_{00}\le\pi(M+1)^2\). These facts yield the stated
\(\pi^5(M+1)^2/16\) bound after the original \(U_0\) normalization.
This argument uses only the sine-Cauchy metric, not a comparison with
the beta-square measure.

The coefficient pairing is the original one:
\(S_N(\sigma)=\sum_{j\le M}v_j(\sigma)p_j\). Since
\(g_j=(-1)^jv_j/U_0\), its \(C\)-norm partner has coefficients
\((-1)^jp_j\). The alternating polynomial and all original targets
are therefore retained before applying Cauchy–Schwarz.

## 2. Alternating section and the unbounded tail

For a positive stable binary polynomial the coefficient support is
contiguous and log-concave. When \(p_Mp_{M+1}>0\), set
\(t_0=p_M/p_{M+1}\).

* For \(t\le t_0\), log-concavity makes the omitted terms decrease from
  \(M+1\) onward. Their alternating sum has magnitude at most its first
  term, itself at most \(p_Mt^M\).
* For \(t\ge t_0\), the retained terms increase up to \(M\); pairing
  them from the final term bounds their alternating sum by \(p_Mt^M\).
* At \(t_0\), the terms of indices \(M,M+1\) are global maxima of
  the coefficient sequence weighted by \(t_0^j\). Hence
  \(P(t_0)/t_0^M\le(d+1)p_M\).
* On \([\log T,\log t_0]\), the function
  \(\log P(e^z)-Mz\) is convex. Its endpoint bound gives the stated
  tail coefficient \(K_T\). No estimate of the length of that interval
  is needed.

The zero cases are also covered. If support starts above \(M\), the
section is zero. If it ends at or before \(M\), the section is the full
polynomial and \(P(t)/t^M\) is nonincreasing for \(t>0\). Contiguity
excludes any remaining gap case. Thus the proof never divides by a
zero coefficient.

The common-variable squared-factor estimate is applied before taking
the maximum in \(t\). On \([1,T]\) the relevant scalar function is
\(a/t+bt-2k\), which is convex because \(a\ge0\).
The bounded portion of the norm uses
\(t^d/(1+t^N)\le1/t\); the unbounded portion uses \(t^M\), whose
full \(C\)-norm is at most one. Combining these with Minkowski gives
exactly
\[
\|Q_M\|_C\le
\sqrt{1+\log T}\,P(1,1)R_T^{d/2}
\max\{P(T)/T^M,(d+1)p_M\}+p_M.
\]
There is no missing heavy-tail moment or exponential coefficient-ratio
factor.

## 3. Rate and geometry interface

The change from \(T^M\) to \(T^{d/2}\) costs only the fixed factor
\(T^{1/2}\) or \(T\). The coefficient \(p_M\) has normalized load
\(M/d\to1/2\). The closed original triangle coefficient upper bound
therefore applies at that boundary, even though \(M\) lies just below
the first omitted index. The existing strict complete optimizer gives
the required gap at this boundary.

For the recorded source the ordered arguments are
\((x,b,c,y)=(0,50,16,29)\), with \(b,y\) protected. Thus the binary
coordinates are \(A=L_{16},C=L_0\). The verifier uses the correct
spectator rows \((x,b,y)\) and \((x,c,y)\), not a cyclic reinterpretation
of the four source arguments. It removes only region 32, keeps 106
triangle rows, and subtracts exactly the 52 extracted ordinary target
logs. Subtracting \(\frac12\log(17/5)\) implements the original
\(T^{d/2}\) weight; it is not a new target.

The geometric input is the original complete action
\(\Phi=\operatorname{Vol}(Y)/(2\pi)\). The feasible-flow certificate
gives a lower bound for this maximum. Its upper interval endpoint is
not an upper bound for \(\Phi\). The tilted calculation is instead a
positive Cauchy upper bound for the exterior at fixed \(A/C=17/5\);
it needs no stationarity of its rational trial weights.

The resulting conclusion is correctly restricted to one original
signed singleton, at odd levels, with all other spectra fixed at
\(-2\). Markov's inequality controls its first cap derivative, and
the one-variable finite Hermite norm can be applied in that same cap
variable. Neither consequence fills the other regions or establishes
a full-invariant volume equality.

## 4. Independent verifier replay

I read the verifier and its interval routines. The square root uses
integer floor/ceiling bounds. The arctangent uses exact half-angle
reduction and a signed series with an explicit remainder. The
log-sine integral uses the stated positive Euler sine-product series,
outward bounds for the zeta values and a geometric tail. The triangle
loads are the exact maximizing angles
\(\pi^{-1}\arctan(w/\sqrt{ab+ac+bc})\); singleton rows are handled
separately. Thus the evaluated expression is the original normalized
triangle potential at the supplied positive rational weights.

The independent replay wrote
[md-r54-tilted-pressure-geometric-peer-replay.json](md-r54-tilted-pressure-geometric-peer-replay.json).
Its result equals the previously stored tilted result exactly. In
particular the certified upper endpoint is
\[
\frac{676833385214656842525551381309548892359909}{10^{40}}
<67.684,
\]
and the exact lower bound for \(a-Tb\) is \(3/2500\).
The response-result input has unchanged SHA256
\[
\texttt{7f906dddb8395ac88a0fc2ea06a25e6d970f89c800335ad5c854e2346422ac23}.
\]
The response localization was not rerun in this audit; it remains a
separately checked input, as the verifier states.

No correction was found. The accompanying manifest records the hashes
of the proof, verifier, certificate, response input, interval engine,
original source and independent replay. No public file was changed.
