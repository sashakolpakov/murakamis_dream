# A full retained-period potential and the exact Fourier boundary cost

Research deduction, 7 November 2026. The established full-period
occupation inequality gives a finite-memory potential on the complete
retained-leg alphabet, including the zero seam and right half. This
extends the earlier half-period construction without a new source
comparison. It does not identify a retained-leg coordinate with a
boundary Fourier coordinate. The exact transform between these two
representations has a separate, explicitly computable weighted norm.
No numerical evaluation is used.

## 1. The literal full-alphabet weights

Fix an original periodic three/four word, its actual geometric
reference, and one permitted collar width \(0<\rho\le10^{-3}\).
Extend the types and reference periodically, but keep target symbols
at different positions independent. A symbol is
\(q_j=(x_j,\sigma_j)\), with \(0\le x_j\le1\) and
\(\sigma_j\in\{0,\epsilon_j\}\). Its target \(z_j\) is
exactly the periodic hybrid graph of
[the split-cutoff theorem](research_mixed_split_cutoff_hybrid_contour.md),
equation (4). In particular its height depends on its own real
coordinate and its two neighboring real coordinates, using its own
selection's cutoff. The seam is not a discontinuous contour reset.

For edge \(j\), retain the complete allocated finite modulus
\[
 \mathcal B_{j,N}=
 |C_{\epsilon_j,N}(X_{j-1},X_j)|
 |d_N(X_{j-1})X_{j-1}^{-N\sigma_{j-1}}|^{\epsilon_{j-1}/2}
 |d_N(X_j)X_j^{-N\sigma_j}|^{\epsilon_j/2},
 \quad X_j=e^{-2\pi iz_j}.
 \tag{1}
\]
Its two halves are modulus allocations, not additional square-root
branches of the source. They restore the original integer powers at
each internal coordinate.

Use precisely the complete upper envelope in
[seam repair, Section 4](research_mixed_seam_raw_exterior_repair.md):
seam-seam edges use their original raw ceiling; other seam-incident
edges use the height-resolved collar profile; remaining right-incident
edges use the complete raw-row envelope; every other edge uses the
original coherent allocated rate. Give the seam priority over the
right label. Keep the original boundary conventions at \(\rho\)
and \(1/2\), and include all Fourier alternatives in each envelope.
Denote this edge rate by \(\mathfrak e_j\), and set
\[
 w_j(q_{j-2},q_{j-1},q_j,q_{j+1})
     =\mathfrak e_j-\Re\Gamma_j(z_{j-1},z_j).
 \tag{2}
\]
Here \(\Gamma_j\) is the original complex tangent plane from
[the open-chain theorem](research_mixed_nonlow_open_chain_boundary.md),
equation (3). It is not replaced by its real-coordinate restriction.
Every target and every source-priority decision in (2) depends only
on these four symbols. Thus (2) remains a finite-range weight.

For fixed \(\rho\), there is a finite local bound
\(K_\rho\) for \(|w_j|\), uniformly in word length. This
can be defined as the supremum over all local types, allowed selections,
real quadruples and enclosing reference rectangles. The coherent
pieces have the original regular compact domains away from the seam;
the collar pieces are bounded height profiles; the raw pieces are
maxima of the continuous integrated logarithmic row rates on compact
physical domains. The logarithmic singularities of individual real
factors are integrable in those row rates. Reference tangents are
bounded on their original compact domains. These observations prove
finiteness; no value of \(K_\rho\) is asserted.

The priority changes need not give a continuous global weight.
All incoming path maxima below are therefore defined as suprema, and no global
continuity or differentiability of the resulting potential is used.
The original source estimates are uniform on their prescribed closed
pieces. In particular, for every fixed \(\tau>0\), their finitely
many local families give constants \(C_\tau,b_\tau\) such that
\[
 \mathcal B_{j,N}\le C_\tau N^{b_\tau}
                    e^{N(\mathfrak e_j+\tau)}.
 \tag{3}
\]
For repetitions of a fixed actual reference these constants and the
level threshold do not depend on the repetition count. This is a
per-edge tolerance; it is not an uncharged total error for a long word.

Put \(a_j=\Re r_j\), let \(y_j\) be the clamp of \(x_j\)
to \([.22,.45]\), and define
\[
 p_j=\min\{1,\sigma_j+400(y_j-a_j)^2\},\qquad
 \omega_j=\frac{p_j}{20000},\qquad \kappa=\frac1{20000}.
 \tag{4}
\]
The actual reference obeys \(.27<a_j<.39\). The baseline
symbol is \((a_j,0)\). Four baseline symbols have weight zero.
Theorem 1 of
[full-period occupation](research_mixed_full_period_occupation.md)
is exactly the pointwise input
\[
                   \sum_jw_j\le-\sum_j\omega_j.
 \tag{5}
\]
It applies to every cyclic target configuration and every positive
integer repetition of the original word with its repeated actual
reference. Stationarity cancels the full complex tangent sum in (2).
Equation (5) is not being inferred from the signed trace asymptotic.

## 2. Entry, exit and a full-alphabet relative estimate

Fix \(0<\theta<1\) and write
\[
 t_i=w_i+\frac\theta2(\omega_{i-1}+\omega_i),\quad
 K_\theta=K_\rho+\theta\kappa,\quad a=1-\theta.
 \tag{6}
\]
Thus \(|t_i|\le K_\theta\) and every cycle has total
\(t\)-weight at most \(-a\sum\omega_j\).
A state at layer \(i\) is the last three symbols
\(v_i=(q_{i-2},q_{i-1},q_i)\); appending \(q_{i+1}\)
has weight \(t_i\). Set
\(\Psi_i(v_i)=\omega_{i-2}+\omega_{i-1}+\omega_i\).

Let \(A_i^{[h]}(v)\) be the supremum of length-\(h\)
incoming weights from the baseline at layer \(i-h\) to \(v\).
Let \(H_i(v)\) be the supremum of all incoming paths from the
baseline at layer zero, with terminal layer \(i\) modulo the
original period. Baseline padding aligns these definitions.
Let \(E_i^{[3]}(v)\) be the weight of appending three baseline
symbols. The original three-symbol entry and exit construction gives
\[
 A_i^{[3]}(v)\le H_i(v)\le-E_i^{[3]}(v),\qquad
 |H_i(v)|\le3K_\theta,
 \quad A_i^{[h]}\le A_i^{[h+1]}\le H_i\quad(h\ge3).
 \tag{7}
\]
Indeed close an incoming path by the three baseline exit steps and
then enough zero-weight baseline steps to restore its layer. Apply
(5)--(6). Conversely a baseline path followed by the three entry
steps reaches any prescribed triple. All these functions vanish at
baseline states. This argument uses no continuity or attained supremum.

Define
\[
 D_i(v)=-A_i^{[3]}(v)-E_i^{[3]}(v),\qquad
 C=\max\{1000,120000K_\theta\}.
 \tag{8}
\]
Then
\[
                    a\Psi_i(v)\le D_i(v)\le C\Psi_i(v).
 \tag{9}
\]
The lower bound follows by closing the three-step entry by the
three-step exit and baseline padding. Each prescribed symbol's
occupation is counted once.

For the upper bound, first suppose \(\Psi_i<\kappa\).
Every prescribed symbol is unselected and strictly inside the plateau:
a selected or nonplateau symbol has \(\omega=\kappa\).
Write \(d_j=x_j-a_j\). Then \(\omega_j=d_j^2/50\), and
every affected target retains its full original reference height.
The same complete plateau Hessian bound used in
[the relative-depth proof](research_mixed_finite_depth_subaction.md),
equation (9), gives
\[
 A_i^{[3]}\ge-10(2d_{i-2}^2+d_{i-1}^2),\qquad
 E_i^{[3]}\ge-10(d_{i-1}^2+2d_i^2).
 \tag{10}
\]
The added occupation in (6) is nonnegative, so it cannot spoil these
lower bounds. Hence \(D_i\le20\sum d_j^2=1000\Psi_i\).
If \(\Psi_i\ge\kappa\), the six local bounds give
\(D_i\le6K_\theta\le120000K_\theta\Psi_i\). This proves
(9), including the baseline case.

**Theorem 1.** Put \(\lambda=1-a/C\). For every \(k\ge0\),
\[
 0\le H_i(v)-A_i^{[3k+3]}(v)
               \le\frac{C^2}{a}\lambda^k\Psi_i(v).
 \tag{11}
\]
The constants are independent of the word length and terminal state.
They may depend on the fixed collar and the specified local bounds.

*Proof.* Take an incoming path with total weight within
\(\varepsilon>0\) of its terminal supremum. Every prefix is
within \(\varepsilon\) of its own supremum: otherwise replace
that prefix and retain the identical remaining symbols, contradicting
terminal near-optimality. Different path lengths are permitted because
the layer and actual reference are aligned modulo the original period.

Let \(P_j\) be its cumulative appended occupation, so for \(j\ge3\)
one has \(\Psi_j=P_j-P_{j-3}\). Close the prefix by its baseline
exit. Equations (7)--(9) give
\[
 aP_j\le D_j(v_j)+\varepsilon
              \le C(P_j-P_{j-3})+\varepsilon,
 \quad P_{j-3}\le\lambda P_j+\varepsilon/C.
 \tag{12}
\]
At the terminal state \(v_T\), this also gives
\(P_T\le(C/a)\Psi_T+\varepsilon/a\). Iterating (12) yields
\[
 P_{T-3k}\le(C/a)\lambda^k\Psi_T+\varepsilon/a.
 \tag{13}
\]
Prepend baseline periods so that \(T\ge3k+3\). Replace
the prefix through layer \(T-3k\) by its literal three-step
entry, retaining that state and the entire suffix exactly. Its lost
weight is at most \(D_{T-3k}\le C\Psi_{T-3k}\le CP_{T-3k}\).
The resulting path has length \(3k+3\), with the correct layer.
Use (13) and let \(\varepsilon\downarrow0\), proving (11).
\(\square\)

Primitive periods one and two cause no exception. The long paths have
independent target symbols; only their type and reference coefficients
repeat. The three occupation incidences are not three copies of a
physical block.

## 3. An exact finite-memory inequality on the entire retained period

Choose \(e=\theta/6\), and, for example, take
\[
 k=\left\lceil\frac Ca\max\left\{0,
                    \log\frac{C^2}{ae}\right\}\right\rceil,
 \quad h=3k+3,
 \quad B_i(v)=\theta(\omega_{i-1}/6+\omega_i/3),
 \quad V_i=A_i^{[h]}+B_i.
 \tag{14}
\]
Then every full-alphabet transition satisfies
\[
             w_i(v,v')\le V_{i+1}(v')-V_i(v)
                                   -\frac\theta6\Psi_{i+1}(v').
 \tag{15}
\]
To prove this, use the exact supremum Bellman identity
\(A_{i+1}^{[h+1]}=\sup_{v\to v'}(A_i^{[h]}+t_i)\).
Its depth increment is nonnegative and, by (11), at most
\(e\Psi_{i+1}\). Directly,
\[
 t_i+B_{i+1}-B_i=w_i+\frac\theta3\Psi_{i+1}.
 \tag{16}
\]
Substitution proves (15). No optimizing path or new values of a
potential have been evaluated.

For an open path, (15) telescopes with no accumulated approximation
error. Combining it with the literal source bound (3) gives
\[
\begin{split}
 \prod_{j=u}^{v-1}\mathcal B_{j,N}
 \le{}&(C_\tau N^{b_\tau})^{v-u}\exp N\bigg\{
 \sum_{j=u}^{v-1}\Re\Gamma_j
 +V_v(v_v)-V_u(v_u)\\
 &\hspace{25mm}-\frac\theta6\sum_{j=u}^{v-1}\Psi_{j+1}
 +(v-u)\tau\bigg\}.
\end{split}
 \tag{17}
\]
Internal original complex tangents cancel; the two cut tangents remain
exactly as in the open-chain theorem, equation (16). This is a bound
for the conditional source on its actual hybrid graph, with its
endpoint halves displayed. It does not assert an independent
one-coordinate contour formula for a newly appended factor.
The bounded graph Jacobian changes fixed-length prefactors only.

Unlike the earlier half-period subaction, (15)--(17) retain all seam,
right-half and selected symbols of the full graph. They do not compare
the surviving boundary functions with a cap, a Fourier observation, or
an arbitrary incoming message.

## 4. The exact norm of the conditional-to-Fourier transform

Keep the notation of
[the exact Fourier bridge](research_mixed_conditional_fourier_message_bridge.md):
\[
\begin{split}
 r&=e^{-2\pi i/N},\quad P_a=(r;r)_a,\quad X=e^{2\pi ix},\\
 f_a(x)&=\frac{e^{-\pi i(N-1)x}}N
            X^a\prod_{j=a+1}^{N-1}(1-Xr^j),\\
 (\mathcal E_\alpha F)(x)&=
           \sum_{a<N}P_a^{1-\alpha}F(r^a)f_a(x),
                         \qquad\alpha\in\{0,1\}.
\end{split}
 \tag{18}
\]
At every integer level \(N\ge2\), the domain is the entire space
of polynomials of degree less than \(N\). Let \(\omega_a>0\),
and let \(\nu_N(x)>0\) be a weight bounded above and below on
a compact Fourier domain \(\Lambda\), for each fixed \(N\).
In particular \(\nu_N=e^{NW}\) is allowed for a bounded real \(W\).
Define
\[
 \|F\|_\omega=\max_{a<N}|F(r^a)|/\omega_a,
 \qquad \|G\|_\nu=\sup_{x\in\Lambda}|G(x)|/\nu_N(x).
\]

**Proposition 2.** The exact finite-dimensional operator norm is
\[
 \boxed{\quad
 \|\mathcal E_\alpha\|_{\omega\to\nu}
 =\sup_{x\in\Lambda}\frac1{\nu_N(x)}
       \sum_{a<N}|P_a|^{1-\alpha}\omega_a|f_a(x)|.
 \quad}
 \tag{19}
\]
The triangle inequality proves the upper bound. For each fixed output
\(x\), prescribe \(F(r^a)\) with magnitude \(\omega_a\)
and phase opposite to that of \(P_a^{1-\alpha}f_a(x)\), with
arbitrary phase at zero coefficients. Interpolation at the \(N\)
distinct nodes realizes these data by a degree-less-than-\(N\)
polynomial of norm one. Its output attains the sum in (19). Taking
the supremum over outputs proves equality, whether or not that
supremum is attained. Both level parities and the full original
normalization in (18) are retained.

For a rate version suppose \(\omega_a=e^{NV(a/N)}\), with
\(V\) continuous on \([0,1]\), and let \(x\) range over a
fixed compact set with \(0<|X|<1\). Write
\(J(u)=\int_0^u\log(2\sin\pi t)\,dt\) with its original
continuous endpoint values. Then, uniformly on that set,
\[
\begin{split}
 \lim_{N\to\infty}\frac1N\log
   \sum_{a<N}|P_a|^{1-\alpha}\omega_a|f_a(x)|
 &=\max_{0\le u\le1}
       \{V(u)+(1-\alpha)J(u)+\Re\ell_u(x)\},\\
 \ell_u(x)&=2\pi ixu-I_X(u)-\pi ix,\\
 I_X(u)&=\frac{\operatorname{Li}_2(Xe^{-2\pi iu})-
                         \operatorname{Li}_2(X)}{2\pi i}.
\end{split}
 \tag{20}
\]
All constants in \(\ell\) are the original incidence constants.
Indeed the original uniform sine-factorial estimate, also used in
[the full physical-row bound](research_mixed_contracted_pair_rectangle.md),
Section 4, is
\(\log|P_a|=NJ(a/N)+O(\log N)\), including its endpoint
ranges. The other product in (18) is uniformly smooth because
\(|X|\) stays below one. Its Riemann sum gives
\[
 \frac1N\log|f_a(x)|
 =-\tfrac12\log|X|+u\log|X|
       +\int_u^1\log|1-Xe^{-2\pi it}|\,dt
       +O(\log N/N).
 \tag{21}
\]
The full-circle integral is zero, by the mean-value property of
\(\log|1-Xz|\) for \(|X|<1\). Thus (21) is
\(\Re\ell_u(x)+O(\log N/N)\). The largest positive summand
and at most \(N\) times that summand bound the sum in (20).
Uniform continuity and the dense physical grids finish the proof.
This rate statement is for a separately specified continuous
one-coordinate weight \(V\); the triple-state potential of (14)
has not been substituted for it.

## 5. The paired operator still needs a coherent boundary estimate

At a cut following a type-four letter, the exact Fourier attachment
by \(A_3A_4\) obeys
\[
 L_N\mathcal E_1
       =\kappa_N^3N\,\mathcal E_1\mathcal T_{01}\mathcal T_{10}.
 \tag{22}
\]
This is the bridge identity applied first to the next type-three
factor and then to the next type-four factor. The two original
type-four Fourier sectors are combined exactly, not equated
separately. The factor \(\kappa_N^3N\) is retained.

Equations (19)--(22) locate a precise extra operation. A retained-leg
potential is not a scalar Fourier-period weight, and the exact change
of coordinates is not a zero-cost inequality. For an unrestricted
node-magnitude class, the positive sum and real-index maximum in
(19)--(20) are unavoidable. This is the same interpolation mechanism
as the sharp norm in
[the literal-transfer obstruction](research_mixed_literal_transfer_norm_obstruction.md),
Section 2. It does not claim that the actual cap messages realize
these phase-aligned extremizers.

A useful next theorem would control this boundary transform on the
actual coherent phase class, with its global remainder retained,
and compare the resulting weight with the original paired action.
Such a theorem may preserve cancellation by a contour argument
before taking the modulus in (18). The present result neither
establishes that comparison nor rules it out. In particular it does
not supply the full-period Schur estimate or initial whole-envelope
assumption in
[the whole-message criterion](research_mixed_paired_whole_message_schur_criterion.md).
The established signed cyclic asymptotic and the pointwise occupation
inequality have distinct roles; neither is silently converted into
an absolute Fourier-cycle loss. No new knot or partial-filling
conclusion follows from this note.
