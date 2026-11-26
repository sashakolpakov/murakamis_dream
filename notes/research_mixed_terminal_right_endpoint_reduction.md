# Reducing the terminal real right sector to its half endpoint

Research deduction, 5 November 2026. At complete ordinary color, the
entire original terminal polynomial has its largest right-half
exponential rate at the real angle \(1/2\). The endpoint near one
is controlled directly from finite products. Combining this with the
proved raw conditional-row comparison reduces the terminal right
sector to one half-endpoint boundary comparison. It does not prove
that remaining comparison or whole-source dominance.

## 1. The actual terminal rate on real compact intervals

Use the exact polynomial \(H_N\) in
[torus composition, equation (21)](research_mixed_conditional_torus_composition.md).
The exact identity
\[
 H_N(w,e^{2\pi ie})=G_N(Ne)\mathcal C_N(e,w)              \tag{1}
\]
and [the full-index endpoint theorem](research_complete_boundary_full_index_interval.md)
give its complete-color packet on every compact real interval in
\((0,1)\). Write
\[
 h(e)=J(e)+\Re S(e),\qquad S(e)=F(e,u_c(e)),
\]
\[
 F(e,u)=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,
 \quad
 u_c(e)=\frac1\pi\arctan\frac{i+\sqrt{1-2e^{2\pi ie}}}{2}.
                                                               \tag{2}
\]
These are the original continued branches. Uniformly on such a
compact interval, \(H_N(-2,e^{2\pi ie})\) has rate \(h(e)\),
power \(N^{-1}\), and nonzero symbol. Every fixed ordinary
\(w\)-derivative at \(w=-2\) has the same exponential upper
rate, with its original polynomial power. No assertion about an
off-grid polynomial is inferred merely from physical-node values;
(1) is the exact identity of the prescribed finite functions.

For \(1/2<e<1\), write
\(\sqrt{1-2e^{2\pi ie}}=a+ib\). Then \(0<b<1\), and the
original endpoint calculation in
[outer cap real tails, equation (7)](research_mixed_outer_cap_real_tails.md)
proves
\[
 \Re S'(e)-J'(e)=-2\log(1+\sqrt{1-b^2}+b)\le-\log4.
                                                               \tag{3}
\]
Consequently
\[
 h'(e)\le2\log(\sin\pi e)<0\qquad(1/2<e<1).             \tag{4}
\]
This is a monotonicity statement for the complete-color rate, not
for each finite polynomial or for a moving-color phase.

## 2. A strict bound at the missing end of the period

The [literal endpoint collar bound](research_mixed_endpoint_seam_majorants.md),
equation (8), gives at every real ordinary color and every fixed
ordinary derivative
\[
 |\partial_w^k H_N(w,Y)|\le C_kN^{A_k}e^{.589N}
                              \quad(|Y-1|\le1/1000).     \tag{5}
\]
It retains every finite row, including revived off-grid rows. The
exact value \(H_N(w,1)=1\) is not used as a continuity estimate.
In particular (5) applies whenever \(9999/10000\le e\le1\),
since \(|e^{2\pi ie}-1|\le2\pi(1-e)<1/1000\).

There is a simple analytic lower bound for the reference rate at the
half endpoint:
\[
                              h(1/2)>7/10.               \tag{6}
\]
Indeed
\(u_c(1/2)=1/4+i\log3/(4\pi)\). Along this vertical segment,
\(-\Re F_{uu}>0\), directly from the two positive cotangents
in (2); hence \(y\mapsto\Re F(1/2,1/4+iy)\) is convex.
Its value at zero is \(-6J(1/4)=3b_2/2\), where
\(b_2=2G_{\rm Cat}/\pi\), and its derivative there is
\(-\pi/2\). Its tangent lower bound gives
\[
 h(1/2)\ge\frac32b_2-\frac18\log3
      >\frac{28}{33}-\frac9{64}=\frac{1495}{2112}>\frac7{10}.
                                                               \tag{7}
\]
Here the alternating Catalan series gives \(G_{\rm Cat}>8/9\),
\(\pi<22/7\), and \(\log3<9/8\). The last logarithmic
bound follows by truncating the positive exponential series at
\(9/8\). Thus (5) has a strict gap from the half-endpoint rate.

**Theorem 1.** For every fixed nonnegative integer \(k\), there
are constants \(C_k,A_k\) such that
\[
 \sup_{1/2\le e\le1}
 |\partial_w^k H_N(-2,e^{2\pi ie})|
                 \le C_kN^{A_k}e^{Nh(1/2)}.              \tag{8}
\]
For each fixed \(\eta>0\), restricting the supremum to
\([1/2+\eta,1]\) gives a strictly smaller rate.

Apply the original compact packet on \([1/2,9999/10000]\),
and use (4) there. Apply (5)--(7) to the remaining interval. For
the strict version, take the minimum of the positive compact
monotonicity gap and the collar gap; if the interval lies wholly
in the collar, use that gap alone. Finitely many small levels are
absorbed into the constants. No new row or root cover is needed.

The compact packet is holomorphic for sufficiently small moving
ordinary colors, and the collar estimate has its quantified complex
color extension. Therefore any fixed strict discarded-sector gap
persists on a sufficiently small fixed color neighborhood, after a
chosen small rate tolerance. This statement uses continuity and
compactness; it does not claim that (4) holds for the moving-color
phase or that the complete-color exponent in (8) remains unchanged
on that neighborhood. Fixed derivatives there require smaller
neighborhoods and the corresponding Cauchy cost.

## 3. The adjacent edge and Fourier factors remain present

For an open word of length at least two, its last source portion is
exactly
\[
 C_{\epsilon,N}(X_a,X_e)\,
 H_N(w_R,X_e^{-1})\,
 d_N(X_e)^\epsilon X_e^{-N\sigma},
 \quad X_e=e^{-2\pi ie},\quad \sigma\in\{0,\epsilon\}.
                                                               \tag{9}
\]
Other allocated Fourier halves and adjacent factors remain unchanged.
If the last real coordinate is \(e\in[1/2,1]\), its physical
hybrid height is zero. Both it and the replacement \(e=1/2\)
have every neighboring left cutoff equal to one. Thus no neighboring
height changes in this replacement.

The [complete right-row reduction](research_mixed_complex_right_row_reduction.md)
states that the full raw envelope of the conditional factor in (9)
is largest at \(e=1/2\), whenever its other target lies in that
theorem's admitted domain. In particular it applies to a complex
nonlow neighbor of real part in \([0,1/2]\) and height
\(|h|\le.057\). It also applies with a fixed real right neighbor:
put \(c_*=-J(1/4)=b_2/4\). The right-row theorem's two real
upper-row bounds give a raw rate at most \(-\epsilon J(u)\le0\)
for \(u\ge1/2\). At the replaced terminal angle \(e=1/2\),
the quarter row has rate at least
\((3+\epsilon)c_*-c>0\), for any unchanged real right neighbor,
because its other integral \(I_0(1/4,y)\) is at least
\(-c\), where \(c=\max J-\min J\).
Here \(3c_*>c\) follows already from \(b_2>56/99\) and
\(c<1/3\). All upper rows are therefore dominated at the replaced
point; the existing lower-row comparison clamps the terminal angle
with the neighboring angle fixed. This supplies the fixed-neighbor
claim rather than inferring it from a simultaneous RR maximum.
Larger unrefined
open-end height ranges are not included merely by analogy. On the
real right half the complete Fourier upper rate of \(d_N\) is
zero, as in the same established mixed source allocation; the
selected monomial has unit modulus. Zeros or forcing ties cause no
problem for this upper bound.

Under those explicit adjacent-source hypotheses, Theorem 1 therefore
reduces the complete-color upper envelope of (9) to \(e=1/2\).
Both original Fourier choices are retained, and one finite-source
tolerance can be kept until the full product is assembled. In a
tangent-subtracted formulation, use the allocated phases: the endpoint
phase is \(S+J-\epsilon g/2\), and the conditional phase contains
the matching \(-\epsilon g/2\) half. Their last-coordinate
tangents cancel by the actual open critical equation. The bare
\(H\) and bare \(C\) phases alone would not be stationary for
\(\epsilon=1\). The surviving tangent in the other variable
is still part of the boundary comparison.

This is a reduction of a terminal right sector, not its comparison
with the critical action. In particular the remaining factor at
\(e=1/2\), its adjacent interior loss, and any unrefined neighboring
height domain still require their actual boundary estimate. The
one-vertex word has no last conditional edge; only the standalone
factor theorem (8) applies to it here. No global open-source or
short-filling theorem is asserted.

## 4. A joint comparison without a neighboring-height restriction

There is a stronger joint reduction on every compact right interval,
without first reducing the conditional rows. For a fixed complex
neighbor \(a\), define the original full raw rates
\[
\begin{split}
 I_a(u)&=\int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt,\\
 I_0(u,e)&=\int_0^u\log(2|\sin\pi(e+t)|)\,dt,\\
 R_\epsilon(a,e)&=\max_{0\le u\le1}
  \{I_a(u)+I_0(u,e)-(2+\epsilon)J(u)-2\pi\Im(a)u\},\\
 R_\epsilon^{\rm seam}(a)&=\max_{0\le u\le1}
  \{I_a(u)-(1+\epsilon)J(u)-2\pi\Im(a)u\}.
\end{split}                                                   \tag{10}
\]
The signed chirp in the first argument is retained. These are the
full \(0\le u\le1\) envelopes; no optimizer bracket or upper-row
deletion is used. The usual zero-safe product estimates give their
uniform finite-row upper bounds when \(a\) ranges over any fixed
compact hybrid annulus.

For a fixed row, only \(I_0(u,e)\) changes with the terminal
right angle. Combining (4) with its derivative gives
\[
\begin{split}
 \frac d{de}[h(e)+I_0(u,e)]
 &\le2\log\sin\pi e
       +\log\frac{|\sin\pi(e+u)|}{\sin\pi e}\\
 &\le\log\sin\pi e.
\end{split}                                                   \tag{11}
\]
The functions are continuous and absolutely continuous across their
integrable logarithmic singularities, so integration is legitimate.
Put
\[
 K(e)=-\int_{1/2}^e\log\sin\pi t\,dt
                   \ge\frac{\pi^2}{6}(e-1/2)^3.         \tag{12}
\]
The lower bound follows from
\(-\log\cos v\ge v^2/2\) for \(0\le v<\pi/2\).
Taking the maximum over all rows after integration yields
\[
 h(e)+R_\epsilon(a,e)
       \le h(1/2)+R_\epsilon(a,1/2)-K(e)
                              \quad(1/2\le e<1).        \tag{13}
\]
Thus on every fixed compact subinterval below one, the entire
complete-color \(H\) packet times the complete raw conditional
envelope is reduced jointly to its half endpoint, for arbitrary
fixed complex neighboring height. All fixed complete-color ordinary
derivatives retain this rate. This proves more than separate
monotonicity of either conditional factor.

Uniformity at the missing endpoint requires a separate bound. If
\(|e^{-2\pi ie}-1|\le\delta\), the product collar (2) of the
seam-majorant note gives
\[
 |C_{\epsilon,N}(X_a,e^{-2\pi ie})|
 \le e^{N\omega(\delta)}
          \sum_{j<N}\frac{|X_a|^{-j}|p_j(X_a)|}{S_j^{1+\epsilon}}.
                                                               \tag{14}
\]
Combining this with the actual \(H\) collar gives the joint upper
rate
\[
             b_2+2\omega(\delta)+R_\epsilon^{\rm seam}(a).
                                                               \tag{15}
\]
It is uniform through \(e=1\), for all real ordinary colors and
fixed ordinary derivatives. The exact value at the endpoint can be
smaller. The actual right diagonal weight still has rate zero and
the selected monomial is still unit modulus.

Equations (13) and (15) provide two explicit alternatives covering
the whole terminal right half: use (13) on
\([1/2,9999/10000]\), and (15) with \(\delta=1/1000\)
on the remaining collar. Both include the same unchanged neighboring
Fourier allocations. No neighboring-height restriction is required
for this two-alternative statement.

One must not replace the second alternative by the first without
another comparison. Indeed
\(I_0(u,1/2)-J(u)=V_0(u)/2\), so the generic estimate only gives
\(R_\epsilon^{\rm seam}(a)\le R_\epsilon(a,1/2)+b_2/2\).
Together with (15), this leaves \(3b_2/2\), whereas the actual
\(h(1/2)\) is strictly below \(3b_2/2\). The latter strictness
follows from the strictly convex vertical function used in (7): its
derivative increases from \(-\pi/2\) to zero at the saddle, so
its saddle value is below its real starting value. This identifies
an insufficiency of that coarse bound, not a failure of the actual
joint clamp. The two-alternative reduction, or the restricted full
clamp of Section 3, must retain its stated scope.
