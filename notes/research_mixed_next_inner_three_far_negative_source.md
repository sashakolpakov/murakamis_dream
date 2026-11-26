# A finite-source bound on the far negative inner horizontal

Private source theorem, 8 November 2026. No mathematical numerical
evaluation, saved-value calculation, or frozen-source edit is used.

The original complete first edge and shortened second edge admit a
coarse mixed-height bound that is sufficient on the far negative
inner arc. Its proof uses a full real-period kernel estimate and
two exact polynomial continuations. It does not assume a Gaussian
packet for a mixed-height second edge.

## 1. Original source and statement

Keep the exact conventions of
[the low-edge reduction](research_mixed_next_outer_exact_low_edge_reduction.md)
and [the complete inner boundary theorem](research_mixed_next_inner_three_far_samples_and_verticals.md):
\[
\begin{gathered}
 N\ge3,\quad D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 q=e^{\pi i/N},\quad \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\\
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),\qquad
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 f_N(t,u)=K_N(t,0)K_N^<(t,u),\\
 \widetilde g_N(t,u)=\sin t\,f_N(t,u)e^{3iNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2}.
\end{gathered}                                                     \tag{1}
\]
In particular the first edge is full. The second cutoff is exactly
\(U\), including the odd-level middle-row deletion already proved
inside the original outer functional.

Let
\[
 \mathcal U_+=\{u=b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\}.
                                                                    \tag{2}
\]
Write the original inner critical point and action as
\[
 t_*(u)=a_*(u)-iH_*(u),\quad
 S(u)=\Phi(t_*(u),u),\quad
 \Phi(t,u)=\psi(t,0)+\psi(t,u)+\frac{3it^2}{4\pi}-it .
                                                                    \tag{3}
\]
The [original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
and [upper terminal-region guards](research_mixed_next_shortened_edge_upper_terminal_regions.md)
give, on this closed actual family,
\[
                  0<a_*<\pi/2,\qquad 1/2<H_*<1 .
                                                                    \tag{4}
\]
All phase constants and logarithmic lifts below are those of
the original edge primitive.

**Theorem.** Uniformly for \(u\in\mathcal U_+\), at both level
parities and all sufficiently large \(N\),
\[
 \boxed{\quad
 \sup_{5\pi/12\le a\le\pi/2}
 |\widetilde g_N(-a-iH_*(u),u)W_N(-a-iH_*(u))|
       \le C e^{N(\Re S(u)-1/10)} .
 \quad}                                                           \tag{5}
\]
The absolute integral on this interval, including the original
trace factor \(N^2|C_{N,3}|/\pi\), satisfies the same estimate
after changing \(C\). Every original angular Fourier charge is
retained in \(W_N\).

This is a pointwise source theorem and an absolute integral
consequence. It makes no derivative claim. It does not estimate
the remaining negative middle interval or the angular connections
to the far endpoints.

## 2. A real-period bound with the exact shortened cutoff

Set \(a_L=5\pi/12\), and first fix any \(a_R\) with
\(a_L<a_R<\pi/2\). Put \(H=H_*(u)\) and \(t_+=a-iH\).
For \(a_L\le a\le a_R\),
\[
 |\cos(t_+/2)|^2=\frac{\cosh H+\cos a}{2}
       <\frac{8/5+3/10}{2}=\frac{19}{20}<1 .
                                                                    \tag{6}
\]
Here \(\cos a_L=\sin(\pi/12)<\pi/12<11/42<3/10\);
the written bound \(\cosh1<8/5\) is the same one used in
[horizontal concavity](research_mixed_next_inner_three_horizontal_concavity.md).
Compactness and (4) therefore place this entire \(t_+\)-family
inside the domain of
[the free-pair kernel, Theorem 4](research_pair_free_boundary_kernel.md).
Dropping its favorable real-angle decay gives
\[
 \sup_{v\in[-\pi,\pi]}|K_N(t_+,v)|
        \le C N^A e^{N\Re\psi(t_+,0)} .
                                                                    \tag{7}
\]
This is a bound for the complete finite kernel, including its
original factorial currents and radical.

The low kernel in that source is
\[
 L_N(t,v)=\sum_{j=0}^{N-1-\lfloor N/2\rfloor}
                       e_j(-2\cos t)e_j(-2\cos v).
                                                                    \tag{8}
\]
Its exact radical comparison, equation (22) there, gives
\[
 |K_N(t_+,v)-L_N(t_+,v)|\le N^2e^{(N-1)H}
                      \qquad(v\in\mathbb R).
                                                                    \tag{9}
\]
By [the complete-edge gap, Theorem 2](research_internal_pair_complete_edge_gap.md),
\[
                    \Re\psi(t_+,0)>H+1/500 .
                                                                    \tag{10}
\]
Thus (7) also bounds \(L_N\).

If \(N=2m\), the cutoff in (8) is \(m-1=U\). If \(N=2m+1\),
it is \(m=U+1\), so the literal term
\(e_m(-2\cos t_+)e_m(-2\cos v)\) must be subtracted. We bound
that term directly.

For any angle \(z=\theta+ih\) in a fixed bounded-height strip,
the original finite Newton product has the zero-safe upper bound
\[
 \begin{split}
 |e_j(-2\cos z)|&\le C N^A e^{N V_z(j/N)},\\
 V_z(y)&=\int_0^y\log|2\cos(2\pi s)+2\cos z|\,ds-2J(y),\\
 J(y)&=\int_0^y\log(2\sin\pi s)\,ds .
 \end{split}                                                       \tag{11}
\]
For the present use the strip is \(|\theta|\le\pi,\ |h|\le1\).
This is the same midpoint-product argument as
[real-period Newton, Lemma 1](research_three_crossing_real_period_newton_bound.md)
and [the complex finite-product proof, Section 2](research_mixed_next_physical_three_kernel_fourier_bound.md),
with a larger fixed height bound. To check that enlargement,
factor the numerator into its two shifted cosine factors. Outside
the bounded number of closest cells to a zero, the logarithmic
derivative is at most a constant times inverse distance, giving
total midpoint error \(O(\log N)\). In a closest cell with height
at least \(N^{-1}\), the same bound holds. At a smaller height,
rescale the cell: the sampled logarithm is at most
\(-\log N+C\), while its integral average is at least
\(-\log N-C\). Exact sampled zeros only lower the product.
The sine-factorial denominator has its original \(O(\log N)\)
error. All constants are uniform on the stated compact strip.

Factoring the full-circle logarithm and using its symmetry about
\(s=1/2\) gives
\[
 \int_0^1\log|2\cos(2\pi s)+2\cos z|\,ds=|h|,
 \qquad V_z(1/2)=|h|/2.
                                                                    \tag{12}
\]
Here \(J(1/2)=0\). The same local logarithm estimate gives a
uniform \(O(N^{-1}\log N)\) integral error on an interval of
length \(1/(2N)\), including moving zeros. Since, at odd levels,
\(m/N=1/2-1/(2N)\), equations (11)--(12) prove
\[
 |e_m(-2\cos t_+)|\le C N^A e^{NH/2},\qquad
 \sup_{v\in[-\pi,\pi]}|e_m(-2\cos v)|\le C N^A .
                                                                    \tag{13}
\]
Thus the subtracted odd row is also below the rate in (7).
We have proved, with the exact cutoff at both parities,
\[
 \boxed{\quad
 \sup_{v\in[-\pi,\pi]}|K_N^<(t_+,v)|
             \le C N^A e^{N\Re\psi(t_+,0)} .
 \quad}                                                           \tag{14}
\]
No individual low-row estimate was inferred from a coherent sum.

## 3. Exact outside-degree continuation

For fixed \(t_+\), the kernel in (14) is a polynomial of degree
at most \(U\) in the ordinary variable \(-2\cos v\). Its real
period covers the whole interval \([-2,2]\). Expansion in
Chebyshev polynomials bounds each coefficient by twice the
supremum in (14), while
\(|T_j(\cos(b+iK))|\le e^{jK}\). Consequently
\[
 |K_N^<(t_+,b+iK)|
       \le C N^A e^{N\Re\psi(t_+,0)+UK}.
                                                                    \tag{15}
\]
This step retains the entire exact polynomial; it does not
continue a saddle expansion to the mixed-height domain.

The Newton polynomials have real coefficients, and both angular
arguments are even. Therefore
\[
 |K_N^<(-a-iH,b-iK)|
       =|K_N^<(a+iH,b-iK)|
       =|K_N^<(a-iH,b+iK)|.
                                                                    \tag{16}
\]
The full first edge satisfies, by
[complete-edge gap, Corollary 3](research_internal_pair_complete_edge_gap.md)
and the same real-coefficient symmetry,
\[
 |K_N(-a-iH,0)|
                  \le C N^A e^{N\Re\psi(a-iH,0)} .
                                                                    \tag{17}
\]
Since \(U<N/2\), (15)--(17) give the finite-source bound
\[
 |f_N(-a-iH,u)|
       \le C N^A
          e^{N\{2\Re\psi(a-iH,0)+K/2\}},
                \qquad a_L\le a\le a_R .
                                                                    \tag{18}
\]

## 4. Comparison with the actual inner action

We now estimate the slack in (18) using only the original phase.
On the cut-safe box of
[negative-horizontal phase, Section 1](research_mixed_next_inner_three_negative_horizontal_phase.md),
\[
 \psi_u(t,u)=-\frac1\pi
          \operatorname{arsinh}\{\tan(u/2)\cos(t/2)\}.
                                                                    \tag{19}
\]
Write \(c=\cos(t_+/2)\). By (6), \(|c|<1\). For real
\(0\le v\le b\), the principal return at \(c\tan(v/2)\)
has nonnegative real part, and
\[
 \Re\operatorname{arsinh}\{c\tan(v/2)\}
        \le\operatorname{arsinh}\{|c|\tan(v/2)\}
        \le\operatorname{arsinh}\{\tan(v/2)\}.
                                                                    \tag{20}
\]
Indeed, for a return \(\xi+i\nu\), the identity
\(|\sinh(\xi+i\nu)|^2=\sinh^2\xi+\sin^2\nu\) proves the
first inequality. Integrating (19)--(20), using the same
primitive at \(t=0\), yields
\[
 \begin{split}
 \Re\psi(t_+,0)-\Re\psi(t_+,b)
 &\le\psi(0,0)-\psi(0,b)\\
 &\le\psi(0,0)-\psi(0,\pi/2)
 <\frac{263}{1250}.
 \end{split}                                                       \tag{21}
\]
The last strict comparison uses the written source constants
\[
 \psi(0,0)=2b_2,\qquad
 b_2<729/1250,\qquad \psi(0,\pi/2)>239/250,
                                                                    \tag{22}
\]
from [real-period Newton](research_three_crossing_real_period_newton_bound.md)
and [complete-edge gap, equation (14)](research_internal_pair_complete_edge_gap.md).

For the downward continuation \(b-ik,\ 0\le k\le K\),
\[
 0<\arg c
   =\arctan\{\tan(a/2)\tanh(H/2)\}<H/2.
                                                                    \tag{23}
\]
The argument of \(\tan((b-ik)/2)\) is nonpositive.
Their product has nonnegative real part on the original
cut-safe box. If its imaginary part is nonpositive, so is that
of its principal return. Otherwise, writing the return as
\(\xi+i\nu\), with \(\xi>0,\ 0<\nu<\pi/2\), gives
\[
 \arg\sinh(\xi+i\nu)=\arctan(\coth\xi\tan\nu)>\nu .
 \tag{24}
\]
Thus in both cases the return's imaginary part is less than
\(H/2\). Since the downward height derivative in (19) is
minus that imaginary part divided by \(\pi\),
\[
 \Re\psi(t_+,b)-\Re\psi(t_+,b-iK)\le\frac{HK}{2\pi}.
                                                                    \tag{25}
\]
Combining the real and height comparisons,
\[
 \Re\psi(t_+,0)-\Re\psi(t_+,u)
                  <\frac{263}{1250}+\frac{HK}{2\pi}.
                                                                    \tag{26}
\]

Put \(s(u)=\Re S(u)\). The actual-height supporting inequality
in [horizontal concavity](research_mixed_next_inner_three_horizontal_concavity.md)
gives
\[
 s(u)\ge
 \Re\psi(t_+,0)+\Re\psi(t_+,u)
                    -H+\frac{3aH}{2\pi}.
                                                                    \tag{27}
\]
On the negative horizontal, the exact crossing factor has
modulus \(e^{-3NaH/(2\pi)}\). Also, uniformly by (4),
\[
 |W_N(-a-iH)|
       \le \frac{e^{-NH}}{(1-e^{-NH})^2}\le C e^{-NH}.
                                                                    \tag{28}
\]
Hence (18) gives the complete angular source rate
\[
        2\Re\psi(t_+,0)+K/2-H-\frac{3aH}{2\pi}.
                                                                    \tag{29}
\]
The difference between (27) and (29) is, by (26), larger than
\[
 \begin{split}
 \frac{3aH}{\pi}-\frac{263}{1250}
                  -\frac K2-\frac{HK}{2\pi}
 &> H\left(\frac54-\frac1{12}\right)
                      -\frac{263}{1250}-\frac14\\
 &>\frac13-\frac{263}{1250}
   =\frac{461}{3750}=:\Delta .
 \end{split}                                                       \tag{30}
\]
Here \(a\ge5\pi/12\), \(H>1/2\), \(K\le1/2\), and
\(\pi>3\). The factor \(\sin t\) is uniformly bounded.
We have proved the polynomial-prefactor version of (5), with
gap \(\Delta>1/10\), on every fixed \([a_L,a_R]\).

## 5. Include the end \(a=\pi/2\) by finite-degree continuation

This last step avoids using the free-pair theorem on the boundary
\(\Re t=\pi/2\) of its stated domain.
For each fixed \(u\), write \(f_N(t,u)=F_N(-2\cos t,u)\).
The polynomial \(F_N(\cdot,u)\) has degree at most
\[
                     d_N=D+U<3N/2.
                                                                    \tag{31}
\]
With \(x=\tan(a/2)\) and \(t=-a-iH\),
\[
 \zeta_H^-(x)=-2\cos(-a-iH)
      =-2\frac{\cosh H(1-x^2)-2i\sinh H\,x}{1+x^2}.
                                                                    \tag{32}
\]
Thus
\[
 P_N(x)=(1+x^2)^{d_N}F_N(\zeta_H^-(x),u)
                                                                    \tag{33}
\]
is an ordinary polynomial of degree at most \(2d_N<3N\).
Set \(x_L=\tan(a_L/2)\), \(x_R=\tan(a_R/2)\).
The raw-source version of (27)--(30) on \([a_L,a_R]\) is
\[
 |f_N(-a-iH,u)|
 \le C N^A
       e^{N\{s(u)+H+3a_RH/(2\pi)-\Delta\}}.
                                                                    \tag{34}
\]
Consequently the supremum of \(P_N\) on \([x_L,x_R]\)
has the same bound multiplied by \((1+x_R^2)^{d_N}\).

Affine Chebyshev continuation from \([x_L,x_R]\) to
\([x_R,1]\) costs at most a polynomial factor times
\(e^{2d_N\rho_R}\), where
\[
 \rho_R=\operatorname{arcosh}
       \left(1+\frac{2(1-x_R)}{x_R-x_L}\right).
                                                                    \tag{35}
\]
For completeness, the Chebyshev coefficients on the input
interval are bounded by twice its supremum, and each
degree-\(j\) term at the enlarged real argument is at most
\(e^{j\rho_R}\). Summing the at most \(2d_N+1\) terms
gives the asserted polynomial factor.

Choose the fixed \(a_R<\pi/2\) sufficiently close to \(\pi/2\)
that
\[
                          3\rho_R<1/100 .
                                                                    \tag{36}
\]
This is possible because \(x_R\to1\) and \(\rho_R\to0\).
All constants from Sections 2--4 then concern this one fixed
compact interval; no limiting uniformity of those constants
is assumed.

For \(x\in[x_R,1]\), dividing (33) by \((1+x^2)^{d_N}\)
cancels the entire input clearing-factor cost, since
\((1+x^2)^{d_N}\ge(1+x_R^2)^{d_N}\). It follows that
\[
 |f_N(-a-iH,u)|
 \le C N^A e^{N\{s(u)+H+3a_RH/(2\pi)-\Delta+1/100\}},
                    \qquad a_R\le a\le\pi/2.
                                                                    \tag{37}
\]
The negative crossing decay for \(a\ge a_R\) is at least its
value at \(a_R\). Restoring (28) and the bounded sine therefore
leaves rate at most \(s(u)-\Delta+1/100\).
There is a fixed reserve beyond the claimed gap:
\[
               \Delta-\frac1{100}-\frac1{10}
                           =\frac{97}{7500}>0 .
                                                                    \tag{38}
\]
Absorb every polynomial factor, including the original \(N^2/\pi\)
in the absolute integral, into this reserve. Equations
(30) and (37)--(38) prove (5).

The proof has preserved the full first edge, every retained
second-edge row, the separate odd cutoff correction, the exact
trace denominator and both level parities. It establishes no
mixed-height saddle expansion and supplies no estimate for the
intervening negative angular interval.
