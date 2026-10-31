# An endpoint-conditioned energy for the original shared source

31 October 2026. **Conditional general theorem.** The finite shared-coefficient
identities and local coefficient bounds below are proved. Sections 5–6 give
an explicit compact shared-flow criterion: keep the endpoint entropy and
relative-energy bound on the **same** flow, optionally taking their minimum
with the older one-sided envelope. A strict score gap proves the full
long-filling limit. The universal geometric inequality for that score
remains open; no independent local norm or endpoint concentration supplies it.

## 1. Actual coefficients and both parity supports

Fix the original certified flat plat \(D\), with \(R\) coupons, degree
\(d=N-1\), ordinary face targets \(d\), and two protected targets zero.
Keep the [actual homogeneous source](actual_homogeneous_casimir_face_source.md)
and its full polynomial resolvent numerator

$$
V_N(\sigma)=\chi_N(\sigma)(\sigma-\Omega_N)^{-1},
\qquad \chi_N(\sigma)=2T_N(\sigma/2)+2.
$$

The [positive reference at both parities](actual_fejer_odd_regularized_full_numerator.md)
is

$$
F_N=
\begin{cases}
-V_N(-2),&N\ \text{even},\\
V_N(-2)-N^{-2}\partial_\sigma V_N(-2),&N\ \text{odd}.
\end{cases}\tag{1}
$$

For a four-incidence exponent \(v=(v_x,v_b,v_c,v_y)\ge0\) with
\(|v|=d\), define

$$
p_N(v)=[x^{v_x}b^{v_b}c^{v_c}y^{v_y}]H_{F_N},
\qquad
a_N(v;\sigma)=[x^{v_x}b^{v_b}c^{v_c}y^{v_y}]H_{V_N(\sigma)}.
\tag{2}
$$

The reference satisfies \(p_N(v)>0\) for every such exponent, at both
parities. In particular none of the inverses below divides by zero.
Protected targets remove every array with positive degree at a protected
incidence; they are never replaced by positive marked radii.

Let \(\Gamma_N\) be the exact original shared array set: an element
\(\boldsymbol v=(v_e)\) satisfies all original face targets. Separate
incidences retain their original quartet labels. The path endpoints are
\(i=v_b\) and \(j=d-v_c\), so the original classes are determined by each
monomial:

$$
\begin{array}{c|c|c|c}
&\mathrm{CROSS}&\mathrm{LEFT}&\mathrm{RIGHT}\\ \hline
N=2m&v_b,v_c\le m-1&v_c\ge m&v_b\ge m\\
N=2m+1&v_b,v_c\le m&v_c\ge m+1&v_b\ge m+1
\end{array}\tag{3}
$$

They are disjoint and exhaustive. The odd central zero-step monomial is
CROSS in this convention. The odd reference derivative retains the same
endpoints, so the same partition applies to \(F_N\).

For a subset \(A_N\subseteq\Gamma_N\) specified by these supports, put

$$
\begin{aligned}
W(\boldsymbol v)&=\prod_e p_N(v_e),&
\mathcal R(\boldsymbol v;\boldsymbol\sigma)
 &=\prod_e\frac{a_N(v_e;\sigma_e)}{p_N(v_e)},\\
Z_A&=\sum_{\boldsymbol v\in A_N}W(\boldsymbol v),&
S_A(\boldsymbol\sigma)
 &=\sum_{\boldsymbol v\in A_N}W(\boldsymbol v)
                        \mathcal R(\boldsymbol v;\boldsymbol\sigma).
\end{aligned}\tag{4}
$$

\(S_A\) is exactly the raw original shared numerator with this support
restriction. There is no additional \(N^R\), pivot, or independently
normalized face contraction. The sign-adjusted convention differs by a
common unit sign and gives the same inequalities. The original external
character and Fourier-period factors remain outside the numerator.

## 2. The finite shared Cauchy inequality

Define

$$
E_A(\boldsymbol\sigma)
 =\sum_{\boldsymbol v\in A_N}W(\boldsymbol v)
                |\mathcal R(\boldsymbol v;\boldsymbol\sigma)|^2
 =\sum_{\boldsymbol v\in A_N}
                \prod_e\frac{|a_N(v_e;\sigma_e)|^2}{p_N(v_e)}.
\tag{5}
$$

Cauchy on this one shared array set proves

$$
|S_A(\boldsymbol\sigma)|^2
 \le Z_AE_A(\boldsymbol\sigma)
 \le Z_AE_{\Gamma_N}(\boldsymbol\sigma).\tag{6}
$$

The full energy is a concrete positive shared coefficient:

$$
\begin{aligned}
E_{\Gamma_N}(\boldsymbol\sigma)
 &=[\text{original targets}]\prod_e
             K_N(\sigma_e;x_e,b_e,c_e,y_e),\\
K_N(\sigma;l)&=\sum_{|v|=d}\frac{|a_N(v;\sigma)|^2}{p_N(v)}l^v.
\end{aligned}\tag{7}
$$

Equation (7) by itself supplies no domination by the endpoint source. It
retains every original face demand and does not replace extraction
by a product of independent local norms.

Equivalently, for \(Z=Z_{\Gamma_N}\) and
\(\mu_N(\boldsymbol v)=W(\boldsymbol v)/Z\),

$$
\frac{S_A}{Z}=\mathbb E_{\mu_N}[\mathcal R\,1_A],\qquad
\frac{E_{\Gamma_N}}Z=\mathbb E_{\mu_N}[|\mathcal R|^2],\qquad
\frac{|S_A|}Z
\le\sqrt{\mu_N(A)\,\mathbb E_{\mu_N}[|\mathcal R|^2]}.\tag{8}
$$

Endpoint concentration does not control an exponentially large ratio
on a rare array. The new input is a second-moment bound on this same
distribution.

Shared face rescaling does not improve (6). Multiplying each reference
coefficient by the same face monomials multiplies \(W\), on every feasible
array, by the fixed scalar \(\prod_f L_f^d\). It scales \(Z_A\) and \(E_A\)
reciprocally, leaving their product unchanged.

## 3. The sufficient rate and its filling consequence

Write \(\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)\). The
[endpoint source theorem](general_fejer_endpoint_source_volume.md) gives
\(N^{-1}\log Z\to\Phi_D\). Let \(\mathrm{NC}_N\) contain every array with
at least one noncross port. Its [unique-maximizer concentration](actual_fejer_spectral_polydisk_complement.md)
gives

$$
\limsup_N\frac1N\log Z_{\mathrm{NC}}
       \le\Phi_D-\gamma_D,\qquad\gamma_D>0.\tag{9}
$$

If this support is empty, its original remainder is zero. Otherwise a
sufficient new estimate is

$$
\limsup_N\frac1N\log
 \sup_{\boldsymbol\sigma\in[-2,2]^R}E_{\mathrm{NC}}(\boldsymbol\sigma)
 \le\Phi_D+\gamma_D-\varepsilon
\quad\text{for some }\varepsilon>0.\tag{10}
$$

Using the full energy in (10) is stronger. Equations (6) and (9) then give

$$
\limsup_N\frac1N\log
 \sup_{\boldsymbol\sigma\in[-2,2]^R}|S_{\mathrm{NC}}(\boldsymbol\sigma)|
 \le\Phi_D-\frac{\varepsilon}{2}.\tag{11}
$$

Thus an energy rate at most \(\Phi_D\) would suffice, but is not necessary:
the endpoint mass gap leaves the additional budget \(\gamma_D\) in (10).
For individual sectors with endpoint rate \(z_s\) and energy rate \(e_s\),
the sufficient condition is \(z_s+e_s<2\Phi_D\). The two optimizations must
retain their own shared constraints; their maximizing flows need not agree.

Each \(S_A\) has degree at most \(d\) in each spectral coordinate. Under
\(\sigma_e=-2\cos(2\pi\delta_e)\), Bernstein's bound extends (11) to a
sufficiently thin fixed complex strip, with cost at most
\(\exp(2\pi d\sum_e|\operatorname{Im}\delta_e|)\). Shrink the strip to
retain a positive gap and apply Cauchy for fixed derivatives. The
[whole-domain current argument](actual_global_diagonal_spectral_sector_gap.md)
then bounds the entire summable charge series, retaining second-derivative
endpoint currents. It uses no infinite sharp-cube localization.

Together with the [ALL-CROSS long-filling theorem](general_all_cross_long_filling_volume.md),
(10) therefore implies the full invariant's volume limit for \(D\) and
independently sufficiently long, fixed signed twists. The filled action
approaches \(\Phi_D\), so its loss can be made smaller than the fixed
remainder gap. This is a conditional implication, not an established
universal energy estimate.

## 4. Exact reduction to spectral coefficient suprema

Define

$$
k_N^*(v)=\frac1N\log\max_{\sigma\in[-2,2]}|a_N(v;\sigma)|,
\qquad h_N(v)=\frac1N\log p_N(v).\tag{12}
$$

The coefficient polynomial is nonzero: (1) excludes simultaneous
vanishing of its endpoint value and first derivative. For nonempty \(A_N\),
put

$$
J_{A,N}=\max_{\boldsymbol v\in A_N}
                   \sum_e\bigl(2k_N^*(v_e)-h_N(v_e)\bigr).
$$

Then, exactly,

$$
e^{NJ_{A,N}}
 \le \sup_{\boldsymbol\sigma\in[-2,2]^R}E_A(\boldsymbol\sigma)
 \le |A_N|e^{NJ_{A,N}}.\tag{13}
$$

The upper bound treats each positive summand. For the lower bound choose a
maximizing **shared** array, then maximize each of its coefficient
polynomials in its independent spectral coordinate. All these choices
occur in the same source. No shared face radius is separately optimized.

Since \(|A_N|\le\binom{d+3}{3}^R\), the logarithmic error in (13) is
\(O_D(\log N/N)\). The [uniform reference entropy](actual_fejer_full_kernel_entropy_identity_reduction.md)
replaces \(h_N(v)\) by \(h(v/d)\) with uniform \(o(1)\) error. Thus the
energy question is exactly the finite shared-flow condition

$$
\limsup_N\max_{\boldsymbol v\in\mathrm{NC}_N}
          \sum_e\bigl(2k_N^*(v_e)-h(v_e/d)\bigr)
       <\Phi_D+\gamma_D.\tag{14}
$$

No continuous limit for \(k_N^*\) is assumed. A feasible array sequence
exceeding this budget would disprove this sufficient route; a large local
ratio without the remaining original targets would not.

## 5. A joint variational criterion on the original shared flow

Let \(\mathcal P_D\) be the compact polytope of nonnegative original
four-incidence loads \(q_e\), with \(\sum_vq_{e,v}=1\) at every port,
ordinary face sums one, and protected face sums zero. Repeated incidences,
when present in an allowed source, are counted with their actual labels.
Write \(h(q)\) for the proved continuous full reference entropy. In the
closed CROSS region \(q_b,q_c\le1/2\), it is the two-triangle entropy
\(h_C(q)\), including the constrained split of the outer loads.

The [one-sided relative-energy theorem](actual_one_sided_relative_spectral_energy.md)
and the CROSS interpolation bound give, uniformly on the actual finite
supports and on the whole real spectral interval,

$$
\frac1N\log\frac{|a_N(v;\sigma)|^2}{p_N(v)}
\le g(v/d)+o(1),\qquad
g(q)=
\begin{cases}
h_C(q),&q_b,q_c\le\tfrac12,\\
C(q_x,q_y,\tfrac12-q_x-q_y),&q_c\ge\tfrac12
                       \text{ or }q_b\ge\tfrac12.
\end{cases}\tag{15}
$$

On either seam the retained triangle has middle load
\(1/2-q_x-q_y\), so the formulas agree. At
\((q_b,q_c)=(1/2,1/2)\) both are zero. Thus \(g\) is a well-defined
continuous function on the full simplex. It does not reassign either
middle load. A zero actual coefficient satisfies (15) with logarithm
minus infinity.

Define on the **same** original feasible flow

$$
H(\boldsymbol q)=\sum_eh(q_e),\qquad
G(\boldsymbol q)=\sum_eg(q_e),\qquad
\mathcal P_D^{\mathrm{NC}}
 =\left\{\boldsymbol q\in\mathcal P_D:
        \max_e\max(q_{e,b},q_{e,c})\ge\tfrac12\right\}.
\tag{16}
$$

The exact finite noncross set is contained in this closed set after
scaling by \(d\). The set may also contain limiting boundary flows of
patterns that are eventually infeasible; keeping them enlarges the
maximum and is safe for this upper criterion. Empty maxima are minus
infinity.

For **each** feasible finite array, uniform reference entropy and (15)
give

$$
\prod_e|a_N(v_e;\sigma_e)|
\le\exp\left\{\frac N2
       [H(\boldsymbol v/d)+G(\boldsymbol v/d)]+o(N)\right\}.
\tag{17}
$$

The error is uniform over all arrays and real spectral coordinates. Sum
(17) over the original noncross arrays. Their number is polynomial in
\(N\), and compactness and continuity then prove

$$
\limsup_N\frac1N\log
 \sup_{\boldsymbol\sigma\in[-2,2]^R}|S_{\mathrm{NC}}|
\le\frac12\max_{\boldsymbol q\in\mathcal P_D^{\mathrm{NC}}}
                 [H(\boldsymbol q)+G(\boldsymbol q)].\tag{18}
$$

This is an arraywise inequality. It is stronger than replacing the right
side by \(\tfrac12(\max H+\max G)\), whose two maximizers may differ.
It requires neither an unknown limiting spectral coefficient function
\(k^*\) nor a minimax exchange.

**Joint criterion.** For the fixed certified diagram, the explicit condition

$$
\boxed{\displaystyle
\max_{\boldsymbol q\in\mathcal P_D^{\mathrm{NC}}}
       [H(\boldsymbol q)+G(\boldsymbol q)]<2\Phi_D}
\tag{19}
$$

implies a fixed real spectral gap for the entire noncross numerator.
The polynomial strip extension and whole-domain current argument of
section 3 then prove the full invariant's filled-volume limit for
independently sufficiently long fixed signed twists, with its original
mark, characters, and normalization. The ALL-CROSS relative asymptotic
remains the leading term. Condition (19) is a proved sufficient reduction;
its validity for every certified diagram is open.

## 6. Combining the energy bound with the earlier envelope

One can retain both available local estimates without comparing them.
On the closed LEFT simplex let \(t=2(1-q_c)\) and define

$$
h_{\mathrm{env},L}(q)=
\begin{cases}
t\,C(q_x/t,q_b/t,q_y/t),&t>0,\\
0,&q=e_c.
\end{cases}\tag{20}
$$

RIGHT is the literal interchange of \(b,c\). This continuous perspective
is the exact concave conjugate of the
[proved weighted upper envelope](actual_global_left_weighted_spectral_envelope.md)
\(\max\{\log c,Q(x,b,y)+\tfrac12\log c\}\): its two atoms have
loads \(e_c\) and \(\alpha+e_c/2\), respectively. Finite positive
outer and middle tilts, followed by a finite compact covering as in the
local energy theorem, therefore give a uniform **coefficient upper bound**
\(N^{-1}\log|a_N|\le h_{\mathrm{env},L}(q)+o(1)\).
This does not decompose the finite source into the two atoms or exchange
an infimum over shared radii with their maximum. Protected faces continue
to impose exponent zero; a sector with protected overloaded middle is
identically absent.

Put \(\widetilde h=(h+g)/2\) and

$$
h_{\mathrm{sharp}}(q)=
\begin{cases}
h_C(q),&q_b,q_c\le\tfrac12,\\
\min\{h_{\mathrm{env},L}(q),\widetilde h(q)\},
       &q_c\ge\tfrac12,\\
\min\{h_{\mathrm{env},R}(q),\widetilde h(q)\},
       &q_b\ge\tfrac12.
\end{cases}\tag{21}
$$

The formulas agree on their seams. Taking the minimum of two uniform
bounds is valid; no assertion that \(\widetilde h\le h_{\mathrm{env}}\)
is needed. Repeating the same finite-array sum proves

$$
\limsup_N\frac1N\log
 \sup_{\boldsymbol\sigma\in[-2,2]^R}|S_{\mathrm{NC}}|
\le\max_{\boldsymbol q\in\mathcal P_D^{\mathrm{NC}}}
                       \sum_e h_{\mathrm{sharp}}(q_e).\tag{22}
$$

**Combined criterion.** The compact, original-incidence condition

$$
\boxed{\displaystyle
\max_{\boldsymbol q\in\mathcal P_D^{\mathrm{NC}}}
                 \sum_e h_{\mathrm{sharp}}(q_e)<\Phi_D}
\tag{23}
$$

has the same full signed long-filling consequence. It is sufficient
whenever (19) holds. It also retains every previously established genuine
sector or branch-cover certificate based on the one-sided perspective
envelope: (21) only lowers that comparison on each covered original
sector. To handle the closed-set convention, a flow with a strict overload
is approximated by the proved full-support integer flow rounding while
retaining that overload; a subsequence fixes its actual finite sector.
Continuity then extends the corresponding certificate. At flows with only
terminal seams, the score equals the endpoint entropy, whose strict gap
on this closed noncross boundary is already proved. This is an implication
between criteria, not a claim of a newly verified strict enlargement of
the diagram classes.

No concavity of (21) is asserted or required. Equations (18) and (22) use direct
compact maximization of the original flows, not unproved convexity or an
independent optimization at each face. Proving (23) universally, or finding
a feasible original flow that obstructs it, is the remaining geometric
entropy problem.

## 7. Proved inputs and remaining limits

The [CROSS cofactor interpolation theorem](actual_cross_cofactor_factorization.md)
already gives coefficientwise \(O(\log^2N)\) domination by the CROSS
endpoint polynomial. That polynomial is at most \(H_{F_N}\) at both
parities. CROSS factors therefore have polynomial energy cost. The
[support-preserving endpoint estimates](actual_fejer_spectral_polydisk_complement.md)
also bound (7) on small spectral polydisks. The general one-sided theorem now supplies the local triangle bound (15).
The unresolved step is the global comparison (19) or (23) on the original
shared-flow polytope.

A new [protected-outer theorem](actual_protected_outer_spectral_energy.md)
computes \(k_N^*\) and its relative-energy limit there, with uniform closed
boundary control. It is a local input to (14), not a shared-flow estimate.

Earlier metrics do not supply (10). The
[complete-circle positive quotient](actual_complete_circle_reflection_positive.md)
bounds transmission on an already inserted \(L_N\), not replacement by
\(V_N\) or overlapping coupons. The
[full Fourier–Hermite Gram](actual_filling_fourier_hermite_gram.md) has an
actual whole-source excess-energy example on a redundant normalization
insertion, but is not the energy (7). The
[Newton-turn Gram](actual_newton_turn_positive_gram.md) keeps turns and
coherent reflected circuits; it does not bound arbitrary source energies.
The [length-normalized star](actual_length_normalized_star_gram.md) retains
both coefficient and dual weights, which cannot be dropped.

The new joint and combined-score reductions use the proved uniform local theorem; their global strict inequalities remain hypotheses, not general volume comparison theorems.

Sections 5–6 prove conditional reductions; their universal strict entropy hypotheses remain open.