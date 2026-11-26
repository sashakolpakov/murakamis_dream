# The even-level radical at a complete endpoint

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The full ordinary Newton kernel at the complete endpoint can have
different exponential rates along odd and even levels. The distinction
comes from its literal high-index radical. At odd levels that radical
vanishes at the complete endpoint. At even levels it has an explicit,
nonzero leading term. We prove this term uniformly away from the real
axis, and give an exact algebraic example where it dominates the
low-index kernel.

This is a statement about a bare kernel evaluated at a complex free
color. It is not a parity assertion about a knot invariant. The example
is the homogeneous positive power-three stationary point; no claim
that it is a complete-ended two-vertex solution is needed.

## 1. Exact reflection with one complete endpoint

Use the original polynomials
\[
 \begin{gathered}
 N=2m,\qquad D=N-1,\qquad \theta=\pi/N,\\
 c_j=2\cos((2j+1)\theta),\qquad
 s_j=2\sin(j\theta),\qquad S_j=\prod_{a=1}^j s_a,\\
 e_j(w)=S_j^{-2}\prod_{a=0}^{j-1}(c_a-w),\qquad
 P_N(w)=2T_N(w/2)+2 .
 \end{gathered}
 \tag{1}
\]
All kernels below are ordinary polynomials before quotient reduction.
Separate the complete-end kernel into
\[
 \begin{split}
 K_N(-2,w)&=L_N(w)+H_N(w),\\
 L_N(w)&=\sum_{j=0}^{m-1}e_j(-2)e_j(w),\\
 H_N(w)&=\sum_{r=0}^{m-1}e_{D-r}(-2)e_{D-r}(w).
 \end{split}
 \tag{2}
\]
The [exact Newton reflection](research_bare_kernel_power_three_obstruction.md#1-exact-reflection-and-a-high-half-estimate)
is
\[
 e_D(w)=\frac{P_N(w)}{N^2(c_0-w)},\qquad
 \frac{e_{D-r}(w)}{e_D(w)}
       =\frac{S_r^2}{\prod_{a=1}^r(c_a-w)}.
 \tag{3}
\]
It follows directly from \(S_rS_{D-r}=N\) and \(c_{D-a}=c_a\).
At even levels \(P_N(-2)=4\). Consequently
\[
 \frac{N^4H_N(w)}{P_N(w)}
 =4\sum_{r=0}^{m-1}A_{r,N}(w),\qquad
 A_{r,N}(w)=
 \frac{S_r^4}{\prod_{a=0}^r(c_a+2)(c_a-w)}.
 \tag{4}
\]
Equivalently the denominator in \(A_{r,N}\) is
\((c_r+2)(c_r-w)e_r(-2)e_r(w)\). Formula (4) is exact.
There are no zeros of \(P_N\) off the real axis.

**Theorem 1.** On every compact subset of \(\{|\Im w|>1\}\),
as \(N\) tends to infinity through even values,
\[
 \frac{N^4H_N(w)}{P_N(w)}
   =\frac{4}{(c_0+2)(c_0-w)}+O(N^{-4})
   =\frac{1}{2-w}+O(N^{-2}).
 \tag{5}
\]
Every fixed derivative of both remainders satisfies the same
respective bound on compact subsets.

*Proof.* Choose \(b>1\) such that \(|\Im w|\ge b\) on a slightly
larger compact neighborhood. Each summand in (4) satisfies
\[
 |A_{r,N}(w)|\le
 T_r:=\frac{S_r^4}{b^{r+1}\prod_{a=0}^r(c_a+2)} .
 \tag{6}
\]
For \(1\le r<m\),
\[
 \frac{T_r}{T_{r-1}}=\frac{s_r^4}{b(c_r+2)}.
 \tag{7}
\]
These ratios increase with \(r\): the sine increases on this range
and \(c_r+2=4\cos^2((r+1/2)\theta)\) decreases. Thus \(T_r\) is
log-convex, and on any consecutive range its maximum is attained
at an endpoint.

Put \(R=\lfloor N/6\rfloor\). For sufficiently large \(N\), and
\(1\le r\le R\), one has \(s_r\le1\) and \(c_r\ge0\). Hence
\[
 T_r\le T_1(2b)^{1-r},\qquad T_1=O(N^{-4}).
 \tag{8}
\]
The second estimate follows from \(s_1\le2\pi/N\) and
\(c_0+2,c_1+2\ge2\). At the other end, the exact sine and
Chebyshev products give
\[
 S_{m-1}^2=N/2,\qquad
 \prod_{a=0}^{m-1}(c_a+2)=2,\qquad
 T_{m-1}=\frac{N^2}{8b^m}.
 \tag{9}
\]
For the middle product, evaluate the monic polynomial
\(2T_m(w/2)=\prod_{a=0}^{m-1}(w-c_a)\) at \(w=-2\).
Log-convexity on \(R\le r<m\), together with (8)--(9), gives
\[
 \sum_{r=1}^{m-1}T_r
 \le\frac{T_1}{1-(2b)^{-1}}
       +N T_1(2b)^{1-R}+\frac{N^3}{8b^m}
 =O(N^{-4}).
 \tag{10}
\]
Keeping the \(r=0\) term proves the first equality in (5).
Since \(c_0=2+O(N^{-2})\), the second follows. All normalized
expressions are holomorphic off the real axis. Applying the uniform
argument on a larger neighborhood and then Cauchy's formula proves
the derivative assertions. \(\square\)

At odd levels every radical polynomial contains the simple physical
root \(-2\), so \(H_N(w)=0\) identically. This exact vanishing is why
Theorem 1 has even-level scope.

## 2. An algebraic point with a strict separation of rates

Set
\[
 w_*=\frac{1-3\sqrt3\,i}{2},\qquad
 t_*=\arccos(-w_*/2)=a-iH,\qquad 0<a<\pi,\ H>0.
 \tag{11}
\]
The [homogeneous power-three calculation](research_bare_kernel_power_three_obstruction.md#2-an-exact-positive-point-with-the-original-unit-charge)
proves, on the original branches,
\[
 3t_*+4i\operatorname{asinh}(\sin(t_*/2))=2\pi .
 \tag{12}
\]
In particular this is an actual positive homogeneous edge geometry,
not merely a root of its exponentiated relation. We use only its
explicit color and branches here.

The [last physical-row theorem](research_last_physical_row_riccati.md),
together with the [even low-index comparison](research_even_complete_low_kernel.md),
fixes the low-index exponential phase on \(\Re w<2\):
\[
 \begin{split}
 \Psi(w)&=\frac{2}{\pi}\int_0^{\pi/2}
        \operatorname{asinh}\left(\frac{\sqrt{2-w}}2\cot y\right)\,dy,\\
 L_N(w)&=\exp\{N\Psi(w)+E_N(w)\},\qquad E_N(w)=O(\log N).
 \end{split}
 \tag{13}
\]
The square root has positive real part, the inverse hyperbolic sine
is continued from real \(w<2\), and the logarithmic endpoint is
integrable. The phase is \(\psi(t,0)\) when \(w=-2\cos t\).
At odd levels \(L_N\) in (13) denotes the low part through index
\((N-1)/2\), which equals the full complete-end kernel.

**Proposition 2.** At (11),
\[
       \Re\Psi(w_*)<\frac{170}{157}
           <\frac{13}{12}<H,\qquad
       H-\Re\Psi(w_*)>\frac1{1884}.
 \tag{14}
\]

*Proof.* Put \(c=\sqrt{2-w_*}/2=(3+i\sqrt3)/4\), so
\(|c|=\sqrt3/2<1\). If \(\operatorname{asinh}z=k+ig\)
has \(k\ge0\), then
\[
 |z|^2=\sinh^2k+\sin^2g\ge\sinh^2k.
 \]
Thus \(\Re\operatorname{asinh}(c\cot y)
\le\operatorname{asinh}(|c|\cot y)\).
For a real variable \(v>0\), the function
\(\operatorname{asinh}(v\cot y)\) is concave in \(v\).
Its tangent at \(v=1\) gives, after integration,
\[
 \Re\Psi(w_*)\le\frac{4G+\sqrt3-2}{\pi},
 \qquad
 G=\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^2}.
 \tag{15}
\]
Here \(\Psi(-2)=4G/\pi\), and the derivative of the real
integral at \(v=1\) is \(2/\pi\).

The alternating partial sum through index \(14\) gives
\(G<11/12\), while \(\sqrt3<26/15\) and \(\pi>157/50\).
The numerator in (15) is positive, so
\[
          \Re\Psi(w_*)<\frac{17/5}{157/50}
                          =\frac{170}{157}.
 \tag{16}
\]
One rational proof of the bound on \(\pi\) uses Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) and the alternating
series bounds
\[
 \pi>16(1/5-1/375)-4/239>157/50.
 \]

The real and imaginary parts of \(\cos t_*=-1/4+3\sqrt3\,i/4\)
give
\[
             \cosh^2H=\frac{11+3\sqrt{13}}8 .
 \tag{17}
\]
Since \(\sqrt{13}>18/5\), this is greater than
\(109/40>(33/20)^2\). On the other hand,
\(\cosh(13/12)<33/20\). To verify the last comparison without
decimal evaluation, set \(x=13/12\), retain the terms through
\(x^6/6!\) in the positive Taylor series, and bound its tail by
\[
 \cosh x\le\sum_{j=0}^3\frac{x^{2j}}{(2j)!}
           +\frac{x^8/8!}{1-x^2/(9\cdot10)}<\frac{33}{20}.
 \tag{18}
\]
Strict increase of \(\cosh\) proves \(H>13/12\).
Finally \(13/12-170/157=1/1884\), proving (14).
\(\square\)

## 3. The two subsequential kernel rates

**Corollary 3.** The full ordinary kernel at the fixed color (11)
satisfies
\[
 \begin{split}
 \lim_{\substack{N\to\infty\\N\ {\rm odd}}}
       \frac1N\log|K_N(-2,w_*)|&=\Re\Psi(w_*),\\
 K_N(-2,w_*)&=
       \frac{e^{iNt_*}}{N^4(2-w_*)}(1+O(N^{-2}))
                 \qquad(N\ {\rm even}),\\
 \lim_{\substack{N\to\infty\\N\ {\rm even}}}
       \frac1N\log|K_N(-2,w_*)|&=H .
 \end{split}
 \tag{19}
\]
In particular the full kernel has no single exponential rate
along all levels at this free color.

*Proof.* At odd levels the radical vanishes, so (13) applies to the
full kernel. At even levels,
\[
 P_N(w_*)=e^{iNt_*}+e^{-iNt_*}+2
            =e^{iNt_*}(1+O(e^{-NH})).
 \tag{20}
\]
Theorem 1 gives the stated leading term for \(H_N\).
Equation (13) and the strict gap (14) make \(L_N/H_N\)
exponentially small, up to a fixed polynomial factor. This proves
the even asymptotic and both limits. \(\square\)

The low-index theorem therefore cannot be changed into a theorem
for the full even complete-end kernel on the same complex domain.
Actual complete-ended internal pairs satisfy stronger bounds:
their selected angles lie in \(0\le\Re t\le\pi/2\),
\(0\le-\Im t<107/100\), where the
[complete-edge gap theorem](research_internal_pair_complete_edge_gap.md)
proves \(\Re\psi(t,0)-|\Im t|>1/500\).
Their full kernels consequently do have the low-sector asymptotic
at both parities. The point (11) has \(\Re t_*>\pi/2\) and lies
outside that region.

The [local internal-pair preparation](research_internal_pair_local_gaussian.md)
also bounds the radical outside-edge terms after the original
traces. Corollary 3 concerns evaluation of the bare polynomial at
one complex color before any such trace; it does not contradict
either of these pair-specific results.

## 4. Reproduction

The [focused checker](../experiments/check_even_complete_radical_asymptotic.py)
verifies the rational and Taylor comparisons in Proposition 2.
It also constructs the original Newton polynomials directly and
checks the exact reflection identity (4) at finite even levels.
Its high-precision kernel-rate entries are numerical illustrations
of the theorem, not premises of its proof.
The [saved record](../repro/results/research-even-complete-radical-asymptotic.json)
records precision, comparisons, and dependency hashes.
