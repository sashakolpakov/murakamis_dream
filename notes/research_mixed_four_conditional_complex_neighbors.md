# A full-sum complex continuation of the four-vertex conditional

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The physical-neighbor theorem has a specified holomorphic continuation
to a fixed neighborhood of the entire real neighbor square. The
continuation is a fixed \(N\)-term sum of the original finite products.
Rows beyond the physical support can revive off the grid; their
absolute rate is bounded explicitly below the selected action.
This is a conditional transfer theorem, not a whole mixed-word
or ordinary-boundary coefficient assertion.

## 1. One canonical finite continuation

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and let \(G_N\)
be the original sine-factorial interpolation. Define its marked
version for the negative root by
\[
 \widehat P_N(v)=
 \exp\!\left(\frac{\pi iv}{2}
             -\frac{\pi iv(v+1)}{2N}\right)G_N(v).
 \tag{1}
\]
It satisfies, meromorphically and with the original normalization,
\[
 \widehat P_N(0)=1,\qquad
 \widehat P_N(v+j)=\widehat P_N(v)
                   (r^{v+1};r)_j\quad(j\ge0).
 \tag{2}
\]
For \(0\le j<N\), \(\widehat P_N(j)=P_j\).
The only noninteger powers in (2) use the fixed exponential
\(r^v=e^{-2\pi iv/N}\).

For complex \(\alpha,\beta\) near
\(K=[1/5,9/20]^2\), set
\[
 \begin{split}
 \mathcal L_{1,N}(\alpha,\beta)
  ={}&\widehat P_N(N\alpha)\widehat P_N(N\beta)
       \sum_{j=0}^{N-1}
        \frac{e^{2\pi i\alpha j}
          (r^{N\alpha+1};r)_j
          (r^{N\beta+1};r)_j}{P_j^3}.
 \end{split}
 \tag{3}
\]
This is holomorphic on a fixed complex neighborhood of \(K\).
The two prefactors lie in their nonzero regular factorial strips,
and the remaining factors are finite polynomials in
\(e^{-2\pi i\alpha},e^{-2\pi i\beta}\).
At every physical pair \(\alpha=a/N,\beta=b/N\in K\),
\[
                     \mathcal L_{1,N}(a/N,b/N)=L_1(a,b).
 \tag{4}
\]
Indeed (2) identifies each surviving summand, and a Pochhammer
factor is exactly zero when \(j+a\ge N\) or \(j+b\ge N\).
Thus the rows beyond \(N-1-\max(a,b)\) vanish at physical
neighbors. They are present in (3) at nonphysical neighbors.

We retain the phase \(Q_4\), the coefficient \(A_4\), and the
classical root \(s_*\) from the
[full physical packet](research_mixed_four_conditional_packet.md).

**Theorem 1.** On a fixed complex neighborhood of \(K\), after
shrinking once if necessary,
\[
 \mathcal L_{1,N}(\alpha,\beta)
 =\frac{\sqrt{2\pi}\,A_4(s_*;\alpha,\beta)}
        {\sqrt{-Q_{4,ss}(s_*;\alpha,\beta)}}
       e^{NQ_4(s_*;\alpha,\beta)}\{1+O(N^{-1})\}.
 \tag{5}
\]
The coefficient and selected phase are holomorphic, the coefficient
is nonzero, and the normalized remainder is uniform with every
fixed complex-neighbor derivative on smaller neighborhoods.
Both level parities and every row of the fixed sum (3) are retained.

## 2. Uniform upper control of finite products near a real wall

Let
\[
 J_{\mathrm{per}}(t)=J(t-\lfloor t\rfloor),\qquad t\in\mathbb R,
 \quad J(0)=J(1)=0.
 \tag{6}
\]
This is continuous. Its derivative away from the integers is
\(\log|1-e^{-2\pi it}|\).

**Lemma 2.** Uniformly for real \(\alpha_0,\beta_0\in K\),
\(0\le j<N\), \(s=j/N\), and
\(|\alpha-\alpha_0|,|\beta-\beta_0|\le\delta\), each summand
of (3) has absolute value at most
\[
 C_\delta N^C\exp N\left[
 H_{\mathrm{per}}(s;\alpha_0,\beta_0)
                  +C_0\delta(1+|\log\delta|)\right],
 \tag{7}
\]
where
\[
 H_{\mathrm{per}}=
 J_{\mathrm{per}}(s+\alpha_0)+J_{\mathrm{per}}(s+\beta_0)
                                             -3J(s).
 \tag{8}
\]
The constants \(C,C_0\) are uniform; \(C_\delta\) may depend on
the fixed positive neighborhood size.

*Proof.* On a fixed compact parameter region,
\[
 |1-e^{-2\pi i(\alpha+h/N)}|
 \le |1-e^{-2\pi i(\alpha_0+h/N)}|+C_1\delta.
 \tag{9}
\]
The logarithm of the right side is a periodic Lipschitz function
with Lipschitz constant \(O(\delta^{-1})\). Its Riemann sum over
any initial interval has error \(O_\delta(1)\), uniformly in the
shift \(\alpha_0\) and the endpoint \(j/N\). Its integral exceeds
the integral of \(\log|1-e^{-2\pi it}|\) by at most
\(C_2\delta(1+|\log\delta|)\).
To check the latter estimate at a zero, split the distance \(d\)
from that zero into \(d\le C_1\delta\) and
\(C_1\delta<d\le1/2\). The first integral is \(O(\delta)\);
on the second, \(\log(1+C\delta/d)\le C\delta/d\).
Away from zeros the estimate is immediate.

It follows that the logarithm of the first finite product is
bounded above by
\[
 N\{J_{\mathrm{per}}(s+\alpha_0)-J(\alpha_0)
                  +C_2\delta(1+|\log\delta|)\}+O_\delta(1),
 \tag{10}
\]
and likewise for the second product. The original bulk factorial
expansion gives
\(\log|\widehat P_N(N\alpha)|\le NJ(\alpha_0)+O(N\delta)+O(\log N)\).
The phase \(e^{2\pi i\alpha j}\) costs at most \(2\pi N\delta\).
Finally, \(\log|P_j|=NJ(s)+O(\log N)\), uniformly through
both physical endpoints. Combining these estimates proves (7).
No logarithmic derivative is taken through a revived zero.
\(\square\)

## 3. The revived rows have a strict rate gap

Put \(U_0=1-\max(\alpha_0,\beta_0)\ge11/20\).
For \(s\ge U_0\), at least one numerator argument in (8)
has crossed one. Its fractional part lies in \([0,9/20]\),
where \(J\le0\). The other numerator contributes at most
\(\max_{[0,1]}J=J(5/6)<1/6\). Also \(s\ge11/20\)
implies \(J(s)\ge0\). Therefore
\[
              H_{\mathrm{per}}(s;\alpha_0,\beta_0)<\frac16
                           \quad(U_0\le s<1).
 \tag{11}
\]
At an exact wall use continuity.

The physical root certificate gives
\[
 \begin{split}
 M(\alpha_0,\beta_0)
   &>\Re F(1/10;\alpha_0,\beta_0)+1/50\\
   &\ge 2J(3/10)-3J(1/10)+1/50>\frac15.
 \end{split}
 \tag{12}
\]
The middle inequality uses the increase of \(J\) on
\([3/10,11/20]\). The two strict scalar estimates
\(J(5/6)<1/6\) and the final inequality in (12) are checked
outward. Thus the revived rows have a uniform real-reference
gap greater than \(1/30\).

For \(s<U_0\), (8) is the real entropy of the original physical
conditional. Its two tails outside \([1/10,9/20]\) already
have the gap \(1/50\) in the physical theorem. Applying Lemma 2
and summing at most \(N\) terms shows that every tail of the
fixed sum (3), including all revived rows, retains a strict
gap on a sufficiently small fixed complex neighbor neighborhood.
Continuity of the selected critical action is included when
choosing that neighborhood.

## 4. The same central source and the original Gaussian

Fix a real reference in \(K\). Its physical proof uses half-grid
real cuts, a cotangent rectangle with strictly separated alias
currents, and a horizontal zero mode through its selected saddle.
Keep this rectangle fixed while the neighboring parameters vary.
Its height exceeds the reference critical height in modulus by
\(10^{-5}\), so a sufficiently small fixed parameter neighborhood
also keeps the moving critical point inside the rectangle.

At every central integer \(j\), identity (2) identifies (3) with
exactly the marked-factorial summand used in the physical proof.
The same interpolation in \(s=j/N\) is therefore an exact
interpolant for the central part of (3) at complex neighbors.
All its factorial arguments remain in their regular strips.
The full symbol (22) of the physical theorem holds there,
uniformly and holomorphically in both neighbors.

Every reference endpoint, side and alias inequality is strict
on a fixed compact set. Continuity of the actual phase preserves
these inequalities after shrinking the complex parameter patch.
No reflection identity for complex parameters is assumed: it
established the real-reference gap, which is now strict on the
entire fixed contour. The zero-mode integral is deformed to the
moving critical height with its two endpoint currents retained.
The negative real Hessian remains positive, so the same Gaussian
calculation gives (5) with the exact coefficient \(+N\).
Lemma 2 and Section 3 control the remaining finite rows.

The real square is compact, so finitely many such patches give
a fixed complex neighborhood. The root branches agree on
overlaps by strict complex-gradient injectivity on the common
middle rectangle, which persists under sufficiently small
parameter changes. The original sine and Hessian branches fix
the coefficients on these overlaps as well. The source (3) is
the same finite function on every patch. Cauchy's formula on
smaller patches gives the normalized derivative estimates in (5).

This continuation retains the complete conditional sum and its
specified scalar. It supplies an exact interpolant for later
neighbor-index contour work. It does not by itself control the
remaining coherent mixed-word contraction or an ordinary
boundary observation.

Reproduce the focused checks with:

    python3 experiments/check_mixed_four_conditional_complex_neighbors.py --precision 256

The [record](../repro/results/research-mixed-four-conditional-complex-neighbors.json)
verifies the current physical author/replay dependencies, three
outward scalar margins, and 380 exact finite comparisons at levels
\(2,3,4,6\). The finite comparisons include every term of (3),
its physical zero rows, and the full original conditional sums.
The all-level interpolation identity and the uniform tail extension
are the written proofs above.
