# A supporting plane for the complete Fourier right cap

Research consequence, 7 November 2026. The completed outgoing-contour
estimates give a supporting-plane bound for the **whole** literal
Fourier right cap across its incoming original-height plateau.
The result is an allocated modulus bound and permits zeros of the
finite incoming weight. It is distinct from the nonzero packet at
the actual reference.

The output remains \(y=x_0\). No selected incoming height, taper
state, full incoming period, ordinary closing functional or
parameter-neighborhood estimate is added here.

## 1. Exact source, reference and domain

Fix the original correlated reference of
[the bare inner-source completion](research_mixed_fourier_right_cap_bare_inner_completion.md),
\[
 \eta\in\{0,1\},\qquad a_*\in K_{3+\eta},\qquad
 (s_*,q_*)\in O_4^2,\qquad y=x_0 .
 \tag{1}
\]
Put \(h_a=\Im a_*\), \(h_s=\Im s_*\), \(h_q=\Im q_*\).
The exact domain is
\[
 P=[11/50,9/20],\qquad a=x+ih_a,\quad x\in P,\qquad
 |h_a|\le.108,\quad -.102\le h_s,h_q\le-.001.
 \tag{2}
\]
For \(\eta=1\), \(h_a\) is its actual negative unselected height.
The reference is fixed while its incoming real target \(x\) varies.
All references and branches are the actual correlated ones; an
independent exterior disk is not substituted.

With \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), \(X=e^{-2\pi ia}\) and \(Y=e^{2\pi iy}\),
the source is exactly
\[
 \begin{split}
 V_N^{\rm F}(y,X)
 &=\sum_{\substack{j,l\ge0\\j+l<N}}
       \frac{X^{-j}p_j(X)P_{j+l}}{P_j^3P_l}\,f_l(y),\\
 f_l(y)&=\frac{e^{-\pi i(N-1)y}}N
       Y^l\prod_{k=l+1}^{N-1}(1-Yr^k).
 \end{split}
 \tag{3}
\]
This is also the exact last-node contraction in equation (5) of
[Fourier-ended boundary windows](research_mixed_fourier_ended_boundary_windows.md).
Its last type-four Fourier alternatives have already been
contracted. No crossing scalar or additional outside \(N\) is
inserted in (3).

Retain the original allocated phase
\[
 \begin{split}
 F_\eta(s,a,q;y)
 &=g(s+a)+g(s+q)-3g(s)-(1+\eta/2)g(a)-g(q)
                         +2\pi ias+\ell_q(y),\\
 \ell_q(y)&=2\pi iy(q-\tfrac12)
   -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})
                         -\operatorname{Li}_2(Y)}{2\pi i},\\
 M_\eta&=\Re F_\eta(s_*,a_*,q_*;x_0),\qquad
 p_\eta=\Re F_{\eta,a}(s_*,a_*,q_*;x_0),\\
 B_\eta(x)&=M_\eta+p_\eta(x-\Re a_*)
                       -\kappa(x-\Re a_*)^2,\qquad
 \kappa=1/2500000 .
 \end{split}
 \tag{4}
\]
The lifted constant \(-\pi iy\), original incoming marginal
and both halfweight allocations are unchanged.

**Theorem 1.** For every \(\tau>0\), there are constants
\(C_\tau,A_\tau,N_\tau\) such that, uniformly on (1)--(2),
for all \(N\ge N_\tau\) of either parity,
\[
 \boxed{\quad
 |d_N(e^{-2\pi ia})|^{\eta/2}
          |V_N^{\rm F}(x_0,e^{-2\pi ia})|
 \le C_\tau N^{A_\tau}
                      e^{N\{B_\eta(x)+\tau\}} .
 \quad}
 \tag{5}
\]
The allocation in (5) is in modulus. No holomorphic square
root of \(d_N\), or division by its value, is used.

## 2. Direct estimate of the low retained source on the plateau

Set \(L_N=\lceil N/8\rceil\), \(M_N=\lceil N/2\rceil-1\).
Use the specified global factorial cardinal, and define
\[
 S_N^<(q)=\widehat f_N(q;y)
       \sum_{j=0}^{M_N}
            \frac{X^{-j}p_j(X)p_j(e^{-2\pi iq})}{P_j^3}.
 \tag{6}
\]
For \(q=z+ih_q\), \(z\in P\), put
\[
 \mathcal L_\eta(x,z)
       =B_\eta(x)-\kappa(z-\Re q_*)^2 .
 \tag{7}
\]
We claim, for every prescribed \(\varepsilon>0\),
\[
 |d_N(X)|^{\eta/2}|S_N^<(z+ih_q)|
 \le C_\varepsilon N^{A_\varepsilon}
                e^{N\{\mathcal L_\eta(x,z)+\varepsilon\}} .
 \tag{8}
\]
This follows directly from the original retained-index decomposition;
it is not an inference about a truncated sum from an upper bound
for the modulus of the complete conditional polynomial.

For \(0\le j<L_N\), the physical left-tail monotonicity in
Section 4 of
[the bare inner-contour proof](research_mixed_fourier_right_cap_bare_inner_contour.md)
bounds each allocated row rate by its real-cut value at \(s=1/8\).
Equation (6) of the inner-source completion puts that value below
\(\mathcal L_\eta(x,z)-1/35000\).
The original uniform product upper bounds include \(j=0\),
factorial endpoint errors of \(O(\log N)\), and any zeros.
The last such index satisfies \((L_N-1)/N<1/8\).

For the indices \(L_N\le j\le M_N\), apply the exact cotangent
residue identity with the original half-grid cuts
\[
             \sigma_-=(L_N-1/2)/N,\qquad
             \sigma_+=(M_N+1/2)/N .
 \tag{9}
\]
Its main current has retained height \(h_s\).
The original bare sheet inequality (15) bounds its phase by
\(\mathcal L_\eta(x,z)-\kappa(\Re s-\Re s_*)^2\).
The lower and upper aliases keep their full denominators and
have the original additional reserves \(1893\pi/25000\) and
\(7/50\), respectively. Every penalized vertical part is
bounded by its corresponding real-cut rate, with gap \(1/35000\).
For the unpenalized negative-height joins, vertical convexity
bounds the rate by the larger of its real-cut and critical-height
cut rates. The latter has gap at least
\[
                       \delta_s=\kappa(23/200)^2>0.
 \tag{10}
\]
These are the individual current bounds in Sections 2--3 of
the bare inner-contour proof and the completed cut comparisons.
They include both side orientations, the zero-mode coefficient
\(+N\), and both parity choices in (9).

The cardinal is independent of the retained index. On this
fixed negative-height outgoing strip, the factorial cardinal
and the original root-Pochhammer cardinal have the same
calibrated phase and nonzero symbol, with proved ratio
\(1+O(N^{-1})\); see equation (8a) of the inner-source completion.
Thus these same current estimates apply to (6).
Their exact off-grid equality is not assumed.
The source bounds, the \(O(1/N)\) half-grid shifts and all finite
polynomial factors are uniform on the stated compact domains.
Allocate one aggregate rate tolerance \(\varepsilon\).
Adding the small physical rows and the complete central
decomposition proves (8), without deleting any part of the
truncated source.

## 3. The whole terminal factor

Define the original central outgoing integral
\[
               I_N^P=N\int_{11/50}^{9/20}S_N^<(z+ih_q)\,dz .
 \tag{11}
\]
The coefficient \(N\) is the outgoing zero-mode density;
the cardinal \(1/N\) is already in (6).
Equation (8), integrated with (7), gives
\[
 |d_N(X)|^{\eta/2}|I_N^P|
 \le C_\varepsilon' N^{A_\varepsilon'}
                            e^{N\{B_\eta(x)+\varepsilon\}} .
 \tag{12}
\]
Discarding the nonnegative outgoing quadratic loss suffices
for (12); no stationary point for the varying target \(x\)
is needed.

Equation (12) of
[the whole-right completion](research_mixed_fourier_right_horizontal_completion.md)
has already retained and bounded the remaining original
physical rows, outgoing currents, joins and the coherently
transported positive retained group. Uniformly on (1)--(2),
\[
 |d_N(X)|^{\eta/2}|V_N^{\rm F}-I_N^P|
       \le e^{N\{B_\eta(x)-\delta_c/16\}},
                   \qquad \delta_c=\kappa/2500 .
 \tag{13}
\]
Choose \(\varepsilon<\tau\), use the triangle inequality
with (12)--(13), and enlarge the finite polynomial prefactor.
This proves (5). If the incoming weight vanishes, all
displayed allocated inequalities remain valid with left
side zero; the proof has nowhere divided by that weight.

At the actual target \(a=a_*\), the separate
[full-cap asymptotic](research_mixed_fourier_right_cap_full_asymptotic.md)
supplies the nonzero coefficient, original phase and
\(N^{-3/2}\) power. The upper estimate (5) neither proves
nor requires a nonzero packet at every other target in \(P\).

## 4. The exact boundary obligation this supplies

In equation (12) of Fourier-ended boundary windows, the
right product contains the literal \(V_N^{\rm F}(y,X_h)\),
where \(h=m-1\). At an unselected last retained node
on its original-height plateau, (5) supplies exactly its
terminal allocation
\[
                |V_N^{\rm F}(x_0,X_h)|
                         |d_N(X_h)|^{\epsilon_h/2}.
 \tag{14}
\]
In the full source product the other half of that node's factor
belongs to the adjacent ordinary block. When the right window's
cut is itself \(h\), (14) is exactly its displayed halfweight
allocation; no further half is inserted into that window.
The action in (4) is
\(\Re\Pi_{\epsilon_h}^{\rm F}(r_h;x_0)\) from that note's
equation (9), and \(p_\eta\) is its original real marginal.
Consequently (5) replaces the terminal term in the local
unselected plateau comparison by a bound for its **complete
finite source**, with the original tangent and a quadratic
loss. Together with a proved holomorphic packet on a local
reference neighborhood, it may also be used as an actual
nonzero terminal symbol in local stationary contractions.

This does not discharge the supremum of the right compensated
bracket
\[
                 B_{R,N}^{\rm F}-D_R+a_d\delta_R^2
 \tag{15}
\]
in equations (18)--(19) of that reduction. Its domain includes
selected retained factors, taper heights, nonplateau physical
states and the whole neighboring boundary window. In particular
(5) changes neither the height to a selected positive height
nor the incoming real target to its full period.
The left compensated bracket and the relative-pinning fee
also remain. The last type-four sectors were contracted
exactly in (3); selections at the surviving node \(h\)
were not thereby contracted or paid.

Likewise a local Fourier endpoint is not the ordinary closing
vector. Section 2, equations (4)--(5) and (8), of the
[whole-message Schur criterion](research_mixed_paired_whole_message_schur_criterion.md)
still needs its complete input-contour norm and complementary-source
bounds. Section 6, equations (27)--(29), of the
[localized retained-current theorem](research_mixed_localized_current_remainder_transport.md)
still has its actual exterior term. Neither can be inferred
from (5) by a change of coordinates or from a local nonzero
amplitude.
Thus this corollary supplies a complete terminal-factor
estimate on its stated plateau. It asserts no new knot-family
theorem, arbitrary short-filling stability, or finite-exception
conclusion. The distinct whole ordinary-color source and outside-color
gap required by Sections 2--3 of
[open-source stability](research_mixed_open_source_stability_reduction.md)
are not supplied. The per-template finite-branching implication
still requires the actual short partial-filling statements of
Sections 3--4 of
[the finite-exception reduction](research_finite_exceptions_under_partial_fillings.md).
