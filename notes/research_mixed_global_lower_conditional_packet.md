# The complete conditional source at nonpositive selected height

Research proof, 4 November 2026. This assembles the new global real-root,
full-period phase and lower-half factorial lemmas. Its analytic inputs and
the present contour assembly require independent review before promotion.
Completed source artifacts and frozen manuscripts are unchanged.

The assertion is for a single original conditional sum. It does not
evaluate the remaining coherent mixed-word sum or assert a knot theorem.

## 1. One fixed finite source

Let \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\), and let \(P_N(w)\)
be the original marked interpolation in
[the lower-half factorial theorem](research_lower_half_factorial_continuation.md).
For real \(0<a,b<1/2\) define
\[
 \begin{split}
 \mathcal L_{\epsilon,N}(a,b)
 &=P_N(Na)P_N(Nb)\sum_{j=0}^{N-1}
   \frac{e^{2\pi iaj}(r^{Na+1};r)_j(r^{Nb+1};r)_j}
        {P_j^{2+\epsilon}},\qquad\epsilon\in\{0,1\},\\
 T_N(s;a,b)
 &=e^{2\pi iNa s}
   \frac{P_N(N(s+a))P_N(N(s+b))}{P_N(Ns)^{2+\epsilon}}.
 \end{split}                                                     \tag{1}
\]
The factorial recurrence gives the exact identity
\(\mathcal L_{\epsilon,N}=\sum_{j=0}^{N-1}T_N(j/N)\), for all
these real parameters, without any physical-grid assumption. When
\(Na,Nb\) are integers, the rows beyond the original triangle support
vanish exactly; all other rows are the original conditional sum.

Use the normalized phase
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad Q_\epsilon(s)=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias.
                                                                    \tag{2}
\]
The selected original zero-lift root \(s_*=x_*+ih_*\) is the one in
[the global cotangent theorem](research_mixed_global_cotangent_roots.md).
Let \(K\Subset(0,1/2)^2\) be any compact set on which \(h_*\le0\).

**Theorem 1.** Uniformly for \((a,b)\in K\), along all integer levels,
\[
 \mathcal L_{\epsilon,N}(a,b)=
 N^{(1-\epsilon)/2}
 \frac{\sqrt{2\pi}\,A_\epsilon(s_*;a,b)}
      {\sqrt{-Q_{\epsilon,ss}(s_*;a,b)}}
 e^{NQ_\epsilon(s_*;a,b)}\{1+O_K(N^{-1})\},                   \tag{3}
\]
where
\[
 A_\epsilon(s;a,b)=e^{i\pi(\epsilon s-a-b)/2}
 \frac{\sqrt{2\sin\pi(s+a)}\sqrt{2\sin\pi(s+b)}}
      {\{\sqrt{2\sin\pi s}\}^{2+\epsilon}}.                 \tag{4}
\]
The sine roots continue their positive real values on the original
strip, and the Gaussian root has positive real part. The coefficient
is nonzero and uniformly bounded above and away from zero on \(K\).
Thus this complete finite source is nonzero for all sufficiently large
levels, uniformly on \(K\). Both parities and every original row remain.

## 2. The whole analytic phase, including height zero

The [full-period reflection theorem](research_mixed_negative_height_full_period.md)
proves that \(x_*\) is the unique nondegenerate global maximum of
\(\Re Q_\epsilon(x+ih_*)\) on \([0,1]\), using the continuous
lower-boundary phase when \(h_*=0\). Write \(M=\Re Q_\epsilon(s_*)\).
Its high-half comparison is a strict circular second-difference
inequality; it does not assume that this half has only one turning point.

Choose a fixed small \(d>0\) so that
\([x_*-2d,x_*+2d]\Subset(0,1/2)\) for every parameter in \(K\),
all its shifted arguments are in the original regular strip, and
\(-\Re Q_{ss}>c_K>0\) near the resulting root segments. Compactness
gives a strict phase gap off \((x_*-d,x_*+d)\). These statements
are uniform even when some selected heights are zero.

There are constants \(C_K,\tau_0>0\) such that for
\(0<\tau\le\tau_0\), putting \(Y=-h_*+\tau\),
\[
 \max_{0\le x\le1}\Re Q_\epsilon(x-iY)\le M+C_K\tau^2.
                                                                    \tag{5}
\]
Near the root, this is the analytic Taylor estimate at \(s_*\),
whose gradient vanishes, followed by completion of the real quadratic.
Away from the root use its strict compact gap and uniform continuity
of the lower-boundary dilogarithm, including its continuous values at
integer arguments. The high-half reflection inequality is valid at
every negative height and preserves the bound. Slight extensions of
the real interval by \(O(N^{-1})\) cost only \(O(N^{-1})\) in (5),
since the line \(\Im s=-Y\le-\tau\) stays below the axis.

The left-vertical lemma in
[the real-contour theorem](research_mixed_real_conditional_contour_geometry.md)
gives a strict uniform gap on \(s=iy\), \(h_*\le y\le0\).
After reducing \(\tau_0\) if necessary, it also gives
\[
 \max_{-Y\le y\le0}\Re Q_\epsilon(iy+0^+)<M-c'_K.           \tag{6}
\]
This follows from monotonicity away from zero and continuity at the
extended lower endpoint, not from a stationary-phase approximation
at a moving factorial endpoint.

## 3. A literal full residue rectangle

Set \(l_N=-1/(2N)\), \(r_N=1-1/(2N)\), and let \(\mathcal R_N\)
be the counterclockwise rectangle with these real sides and heights
\(\pm Y\). For all large \(N\), the two numerator interpolations in
(1) are holomorphic on a neighborhood of this rectangle and its
interior. Indeed their unscaled real arguments exceed \(-1\);
the Gamma product has no poles there, while its reciprocal-Gamma
zeros beyond one period are retained. The denominator is holomorphic
and nonzero because \(-1<\Re(Ns)<N\). Thus the only poles in
the residue formula are the original cotangent poles, and exactly
the integers \(0,\ldots,N-1\) are enclosed:
\[
 \mathcal L_{\epsilon,N}
 =\frac{N}{2i}\oint_{\partial\mathcal R_N}
                     T_N(s)\cot(\pi Ns)\,ds.               \tag{7}
\]

On the upper part of the boundary write \(\cot=-i+R_+\), and
on the lower part write \(\cot=i+R_-\). Applying Cauchy's theorem
separately to the upper and lower half-rectangles shows that their
two constant contributions are exactly
\[
                         +N\int_{l_N}^{r_N}T_N(x)\,dx.       \tag{8}
\]
In particular the constant mode is not \(N/2\), and no endpoint
current is dropped when combining it.

The horizontal remainders satisfy
\(|R_\pm|\le C e^{-2\pi NY}\). On either midpoint vertical side,
the exact tangent-hyperbolic formula gives
\[
                 |R_\pm(x+iy)|\le2e^{-2\pi N|y|}.            \tag{9}
\]
It is bounded even at \(y=0\). These are the two original aliases.

## 4. Both aliases and every vertical side

The lower-half factorial theorem gives a uniform polynomial-times-
exponential bound with phase (2) on the whole lower horizontal side,
including all shifted arguments beyond one. Combining it with (5)
and (9) bounds the lower horizontal remainder below the rate
\(M+C_K\tau^2-2\pi Y\).

For real \(a,b\), the exact Schwarz identity is
\[
 \frac{|T_N(x-iy)|}{|T_N(x+iy)|}
 =\exp\left[2\pi Ny\{a-b+\epsilon(x-1/2)\}
                         +\epsilon\pi y\right].             \tag{10}
\]
It holds across every shifted factorial wall, as a multiplicative
modulus identity at zeros. On \(K\) and \(0\le x\le1\), the
absolute value in braces is at most a fixed \(\Lambda_K<1\).
The \(O(N^{-1})\) extension to the actual real endpoints changes
the estimates only by a bounded factor. Therefore the upper horizontal
remainder has rate at most
\[
                   M+C_K\tau^2-2\pi(1-\Lambda_K)Y.           \tag{11}
\]
Choose \(\tau\) small enough that
\(C_K\tau<\pi(1-\Lambda_K)\). Since \(Y\ge\tau\), both
horizontal aliases have a strict uniform gap, also at \(h_*=0\).
No upper-half Stirling estimate is used.

For the lower vertical sides use the exact midpoint identities and
Lemma 2 of the lower-half factorial theorem:
\[
 \begin{split}
 |P_N(-1/2+iNy)|^2&=\frac{N}{1+e^{2\pi Ny}},\\
 \frac{|T_N(r_N+iy)|}{|T_N(l_N+iy)|}
 &\le(1+e^{2\pi Ny})^{-\epsilon}\le1,\\
 |T_N(l_N+iy)|&\le C_K N^{-\epsilon/2}
       e^{N\Re Q_\epsilon(iy+0^+)}\quad(-Y\le y\le0).
 \end{split}                                                     \tag{12}
\]
The second inequality holds for all real neighbors, including those
off the physical grid: each full-period numerator multiplier has
modulus at most \(1+e^{2\pi Ny}\). Equations (6), (9) and (12)
control both lower vertical remainders. Reflecting their rows by (10)
and retaining the penalty in (9) controls both upper vertical
remainders, with at least the same strict gap. This includes their
corners and their intersections with the real axis.

## 5. The complete zero mode and its nonzero coefficient

Deform the exact real integral (8) to the following left-to-right path:
the two exterior intervals have height \(-Y=h_*-\tau\); the interval
\([x_*-d,x_*+d]\) has height \(h_*\); and two vertical segments join
these pieces. Retain also the two vertical end joins from real height
zero to \(-Y\). Holomorphy established before (7) makes this an exact
deformation of the same finite function.

The two end joins have the strict gap (6), (12). On the exterior
horizontal intervals the selected-height global phase gap persists
when the height is lowered by the fixed sufficiently small \(\tau\).
They lie below \(-\tau\), so the lower-half factorial expansion
applies uniformly across all shifted walls. On the short interior
vertical segments, the same compact gap persists by continuity in
the original regular strips. These arguments also apply when
\(h_*=0\): only the central regular-strip segment touches the axis;
all potentially shifted-wall exterior pieces stay strictly below it.

On the central segment the original regular-strip expansion is
\[
 T_N(s)=N^{-\epsilon/2}A_\epsilon(s;a,b)
                      e^{NQ_\epsilon(s;a,b)}\{1+O_K(N^{-1})\}.
                                                                    \tag{13}
\]
All factors in (4) are regular and nonzero there. The exact original
critical equation holds, and \(-\Re Q_{ss}>0\). The ordinary analytic
Gaussian along this left-to-right segment gives
\(\sqrt{2\pi}/\sqrt{-Q_{ss}}\). Its first cubic correction is odd
on the symmetric interval, so the relative error is \(O_K(N^{-1})\).
The three powers are
\[
                 N\cdot N^{-\epsilon/2}\cdot N^{-1/2}
                          =N^{(1-\epsilon)/2}.               \tag{14}
\]
All the other portions of the zero-mode path and both aliases are
exponentially smaller by Sections 4--5. This proves (3), including
its original carrier, its nonzero coefficient and the full-level
normalization. No unshifted high-row tail has been estimated termwise
at a rate that exceeds the saddle; those rows are part of the exact
coherent residue rectangle throughout.

## 6. Scope and reproduction

This theorem concerns the fixed canonical finite source (1), for real
neighbors in compact subsets of the nonpositive-selected-height region.
It includes every physical conditional sum in that region and both
parities. It does not assert that a given complex taper pair lies in
a source neighborhood of such a real set. The global cotangent root
alone does not supply that further complex-parameter statement.
It also gives no lower bound for an outer cyclic or ordinary-boundary
observation after further summation.

Run

    python3 experiments/check_mixed_global_lower_conditional_packet.py

The [focused checker](../experiments/check_mixed_global_lower_conditional_packet.py)
passes ten exact identities and 180 exact finite-source comparisons
at levels 2, 3, 4, 5 and 6. It checks the all-row canonical-to-physical
reduction, full-period and reflection algebra, the cotangent residue
coefficient and the powers in (14). It also validates the current
proof, checker and record bindings of all four analytic inputs.
The global phase gaps and compact contour argument are written proofs,
not finite-level extrapolations.
