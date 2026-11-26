# A geometric coordinate from a ratio of the original half-charge sums

Fix \(r\ge1\), \(n\in\mathbb Z\), \(r+|n|>1\), and use the
literal complete-outside sources
\[
 C_N=\phi_N[R^n e_L K_N(\,\cdot\,,-2)^r],\qquad
 D_N=\phi_N[R^n e_{L+1}K_N(\,\cdot\,,-2)^r],
 \qquad L=N-1-\lfloor N/2\rfloor .
\]
All normalizations, physical derivatives and signed crossing
powers are those of [A,B]. No factor is removed from either sum.

Let \(t_*\) be their selected complete half-charge saddle:
\[
 nt_*+2ir\operatorname{asinh}\tan(t_*/2)=\pi,\qquad
 |\Re t_*|<\pi,\quad\Im t_*<0 .
\]
Write \(z_*=-2\cos t_*\).

**Proposition.** The ratio is defined at all sufficiently large
integer levels, through both parities, and
\[
 \lim_{N\to\infty}\frac{D_N}{C_N}
 =\rho_*=\frac{\cos t_*-1}{2}
 =-\sin^2(t_*/2),\qquad z_*=-2-4\rho_* .
 \tag{1}
\]
This limit is algebraic over \(\mathbb Q\). In particular, the
selected critical coordinate can be recovered from actual finite
source observations, including their phases.

## Proof from the two complete source asymptotics

Put \(m=\lfloor N/2\rfloor\), \(s_m=2\sin(m\pi/N)\), and
\[
 p_N(z)=\frac{c_L-z}{s_m^2}.
\]
The original Newton polynomials obey \(e_{L+1}=p_Ne_L\).
The two proved asymptotics [A, (7)] and [B, (6)] have the
same nonzero carrier, exponential, logarithmic error, Gaussian
normalization and square-root branch. Their amplitudes satisfy
the exact relation
\[
 b^B_N(t_*)=p_N(z_*)b^A_N(t_*).
\]
Both are nonzero for all sufficiently large levels. Dividing
the asymptotics therefore gives
\[
 D_N/C_N=p_N(z_*)(1+o(1)).
\]
At odd levels \(c_L=-2\); at even levels
\(c_L=-2\cos(\pi/N)\). At both parities \(s_m^2\to4\).
Hence the ratio tends to \((-2-z_*)/4\), which proves (1).
The possibly oscillating carrier and the level-dependent
logarithmic error cancel before taking the limit.

## An explicit polynomial for the selected algebraic point

Set \(w_*=\exp(it_*/2)\). Then \(|w_*|>1\), so
\(w_*\notin\{0,i,-i\}\). On the branches continued from zero,
\[
 u_*=\exp(\operatorname{asinh}\tan(t_*/2))
     =\sec(t_*/2)+\tan(t_*/2)
     =-i\,\frac{w_*+i}{w_*-i}.
\]
Multiplying the critical equation by \(i/2\) and exponentiating
gives \(w_*^n u_*^{-r}=i\). Consequently
\[
 w_*^n(w_*-i)^r=i(-i)^r(w_*+i)^r .
 \tag{2}
\]
For \(n\ge0\), this is a polynomial equation over \(\mathbb Q(i)\).
For \(n<0\), multiply it by \(w_*^{-n}\) to obtain
\[
 (w_*-i)^r-i(-i)^r w_*^{-n}(w_*+i)^r=0 .
\]
In either case the displayed polynomial is not identically zero:
its value at \(w=i\) is nonzero. Thus \(w_*\) is algebraic.
Finally,
\[
 4\rho_* w_*^2=(w_*^2-1)^2 ,
\]
so \(\rho_*\) is algebraic over \(\mathbb Q(i)\), and hence
over \(\mathbb Q\).

Equation (2) can have additional roots. The actual saddle branch
and the original source asymptotics select the root used in (1);
exponentiation alone does not make that selection.

## Scope and direct sources

This is a local source-period identity. It does not identify (2)
with a knot's \(A\)-polynomial, evaluate a closed knot invariant,
or prove noncancellation after arbitrary tangle assembly.
Its nonzero denominator is proved by the full source contour,
rather than assumed from a formal stationary equation.

- A: [The original multi-leg half-charge source](research_multileg_half_charge_source_bound.md),
  SHA256 df85063947dc52c876d1cb810208e4da725517b7556661e3ddb21a3de7f0f8d2.
- B: [Mixed low and radical half-charge sources](research_mixed_low_radical_coupon_trace_bound.md),
  SHA256 5e347ad0b8fb1a31415344eac6c2c3dea3b4b4d8b39dc0d76b1eb47a62d382e6.

Both entire direct proof texts and every implication used here
were read at these matching pins. Only written mathematics and
text operations were used.
