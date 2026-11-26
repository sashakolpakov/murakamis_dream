# Conditional assembly of the complete selected terminal kernel

Research deduction, 6 November 2026.

Seven remaining uniform branch comparisons would complete the local
ordinary-plus-terminal selected kernel on the canonical \(K_4\) families.
The other profile comparisons and the finite-source reduction are already
available. This note states the exact implication. It does not assume
those seven signs or assert their numerical verification.

## 1. Reference, target and literal allocation

Let
\[
 K_4=\{|z-(.30-.052i)|\le.060\}
             \cap\{-.108\le\Im z\le-.001\},\qquad
 P=[.22,.45],\qquad H=1/100.
 \tag{1}
\]
Fix a reference parameter \(\zeta\in K_4\), an ordinary vertex of
type four, and a terminal vertex of type \(3+\epsilon\),
\(\epsilon\in\{0,1\}\). Write the original canonical reference as
\[
 b_*=\zeta,\qquad (s_*,a_*,t_*,v_*),
 \tag{2}
\]
where \(v_*=\xi_*\) for terminal type three and \(v_*=e_*\) for type
four. The [all-input reference theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its [refinement](research_mixed_terminal_quadratic_residual_refinement.md)
supply these same original zero-lift branches. The
[canonical source-domain lemma](research_mixed_terminal_canonical_source_domain.md)
supplies the oriented input, inverse-leg, physical-tail and ordinary-color
source hypotheses throughout (1). In particular, its compactness argument
preserves uniform source neighborhoods at retained domain boundaries.
An arbitrary independent point in an image rectangle is not being
declared source-feasible.

Use the exact ordinary phase and original stationary terminal action:
\[
 \begin{split}
 Q_1(s;b,a)&=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,\\
 M_*(\zeta)&=Q_1(s_*;\zeta,a_*)+P_\epsilon(a_*)
                            -g(a_*)-\tfrac12g(\zeta),\\
 p_*(\zeta)&=g'(\zeta+s_*)-\tfrac32g'(\zeta)+2\pi is_*.
 \end{split}
 \tag{3}
\]
All primitives, terminal actions and logarithmic lifts are original.
The full stationary equations give
\(Q_{1,s}=0\), the internal terminal stationarity, and
\[
 Q_{1,a}(s_*;\zeta,a_*)+P_\epsilon'(a_*)-g'(a_*)=0.
 \tag{4}
\]
Thus the shared \(a\)-marginal cancels, while the full complex incoming
marginal \(p_*\) remains.

Let \(X_z=e^{-2\pi iz}\). The allocated finite modulus is exactly
\[
 \mathcal K_{N,\epsilon}(b,a;w)=
 \left|C_{1,N}(X_b,X_a)\mathcal V_{\epsilon,N}(w,X_a)
                      d_N(X_a)X_a^{-N}\right|\,|d_N(X_b)|^{1/2}.
 \tag{5}
\]
The target variables satisfy
\[
 b_R,a_R\in P,\qquad \Im b=\Im\zeta,\qquad \Im a=H.
 \tag{6}
\]
Their real parts are independent; in particular \(b_R\) is not
restricted to the reference disk section. The incoming leg is
unselected. The half-power in (5) allocates a modulus, not a
holomorphic square root. The complete selected diagonal and monomial
occur once.

## 2. The precise seven remaining hypotheses

Use the 27 terminal labels of
[the complete envelope](research_mixed_terminal_concave_profile_envelope.md),
Sections 1--4. Its regular labels are
\(\sigma\in\{0,L,R,-,+\}^2\), with the first coordinate the transform
index; its two further labels are the entropy profile \(R_\epsilon\)
and constant \(C=879/1000\). Main heights are the original reference
heights. A real cut has height zero.

For any such terminal profile \(T_{\epsilon,\sigma}\), define the
ordinary-main joint defect
\[
 D_{\epsilon,\nu,\sigma}
 =\Re Q_1(s;b,a)+T_{\epsilon,\sigma}(a;\mathbf x)
 -\tfrac12\Re g(b)-\nu\Re g(a)-2\pi\nu H
 -\Re\{M_*(\zeta)+p_*(\zeta)(b-\zeta)\}.
 \tag{7}
\]
Here \(\nu=1\) is factorial and \(\nu=0\) is forced. Both alternatives
retain all \(a_R\in P\). The ordinary main index has its full original
interval \([1/8,1/2]+i\Im s_*\). Each terminal label retains its own
original active-index intervals, penalties or entropy domain.

**Hypothesis (S).** There is a number \(\gamma_7>0\) such that
\(\sup D_{\epsilon,\nu,\sigma}\le-\gamma_7\), uniformly over
\(\zeta\in K_4\), (6), and every original active index, for the seven
entries
\[
 \begin{array}{c|c|c}
 \epsilon&\sigma&\nu\\ \hline
 0&(R,0)&1\\
 0&R_0&0,1\\
 1&(L,0)&0,1\\
 1&R_1&0,1 .
 \end{array}
 \tag{8}
\]
In the entropy rows \(R_0,R_1\) denote terminal entropy profiles, not
ordinary labels.

A complete finite source-cell verification of strictly negative
upper bounds supplies such a \(\gamma_7\) by their finite minimum.
It must cover every retained cell, match its own source reserve to
its own reference-plane ceiling, retain closed boundary contacts,
and justify any empty-reference exclusion. The
[source-cell joined-plane protocol](research_mixed_terminal_source_cell_joined_plane.md)
specifies that sufficient mechanism; its proposed calculation is not
assumed to have succeeded here. A positive upper is merely
inconclusive.

All other branch comparisons are already uniform on this same domain:

| Profiles or branches | Existing raw gap |
|---|---:|
| Main, both terminal types and both alternatives | \(1/400\) |
| Sixteen penalized alias endpoint labels, both alternatives | \(1/20\) |
| Constant, both terminal types and both alternatives | \(1/100\) |
| Thirteen real-cut/entropy families paid by the original joined plane, both alternatives | \(>1/225\) |
| Terminal-four private left cut \((0,L)\), both alternatives | \(51/20000\) |
| Terminal-three right transform cut \((R,0)\), forced alternative | \(>171/500000\) |

The dependencies are respectively the
[uniform main comparison](research_mixed_terminal_uniform_main_comparison.md),
[alias completion](research_mixed_terminal_uniform_alias_completion.md),
[height-sensitive constant proof](research_mixed_terminal_uniform_constant_profile.md)
and its [passed result](../repro/results/research-mixed-terminal-uniform-constant-profile.json),
the [exact real-face recombination](research_mixed_terminal_uniform_real_face_outcome.md),
and the [private-left symmetric-cost transfer](research_mixed_terminal_private_left_symmetric_transfer.md).
The constant result has SHA256
5931137b18d3b6d1815ed2cf90569425910882f88e637e35391f575fcab12965.
Its two original-height floors and four joined comparisons passed
without changed inputs.

Consequently, under (S), every terminal label and both alternatives
have the common raw gap
\[
             \delta=\min\{\gamma_7,\ 171/500000\}>0.
 \tag{9}
\]
The smaller explicit floor in (9) only preserves the weakest currently
available old comparison. If a new uniform calculation also strengthens
that already-negative branch, its better proved gap may replace the
old floor. It is not a limitation of the source envelope.

## 3. Restoring every ordinary label and terminal current

The [ordinary-label completion](research_mixed_terminal_ordinary_label_completion.md)
proves that each of the six nonmain ordinary labels lies below the
ordinary main maximum by at least \(1/500\), with the same terminal
profile, target arguments, incoming halfweight and Fourier alternative.
Its hypotheses hold here:
\[
 -.108\le\Im\zeta\le-.001,\qquad
 -.102<\Im s_*<-.001,\qquad b_R,a_R\in P,\qquad \Im a=.01.
 \tag{10}
\]
The first interval also lies in the height domain of the original
seven-label **finite-source** theorem in
[the ordinary compiler](research_mixed_plateau_window_concave_profiles.md),
Proposition 1. Thus the pointwise label domination is being used only
where its separate finite-envelope premise holds.

Adding each unchanged terminal profile and row-independent weight to
that domination reduces the \(7\cdot27\cdot2=378\) comparisons for
each terminal type to (7). The ordinary \(1/500\) gap is added to,
not subtracted from, the terminal gap. It therefore does not impose
another minimum in (9). Ordinary horizontal aliases, their joins,
wrapped rows and last-row carriers remain covered by that compiler.

The terminal envelope is an exact reduction of the complete finite
source. On every sign half of a vertical alias side, the kernel penalty
is linear and the phase is convex in that height. Its endpoints are
an outer penalized alias label and a zero-height real-cut label.
The real-cut hypotheses in (8), together with the completed real cuts,
therefore supply the endpoints previously missing from the alias
completion. Applying the same argument in both index coordinates
controls double aliases and all their sides. Zero-mode joins are
handled by their real-cut and main endpoints.

The entropy profile retains the entire physical right triangle and
the support-wall bounds. The constant profile covers the positive
exterior majorants and whole coherent end rows. The envelope retains
the complete private ordinary polynomial, revived off-grid terms and
the even-level half row. No sector is removed by a bare comparison
with an independently enlarged reference box.

## 4. Conditional complete finite-kernel theorem

**Theorem.** Under (S), for every sufficiently small fixed
\(\tau>0\), there are a fixed ordinary-color neighborhood of the
complete color and constants \(C_\tau,A_\tau,N_\tau\), uniform in
\(\zeta\in K_4\), such that
\[
 \mathcal K_{N,\epsilon}(b,a;w)
 \le C_\tau N^{A_\tau}
 \exp N\!\left\{\Re[M_*(\zeta)+p_*(\zeta)(b-\zeta)]
                                  -\delta+\tau\right\}
 \tag{11}
\]
for both terminal types, all targets (6), and every integer
\(N\ge N_\tau\) of either parity. Every prescribed fixed ordinary-color
jet of the original integer-weighted holomorphic source has the same
rate on a smaller neighborhood, after the incoming modulus allocation.

*Proof.* Choose a branch for the complete selected-weight bound first;
use that same choice in both half-allocations whenever a supporting
plane is used. Its two additive alternatives have the rates appearing
in (7). All 378 profile comparisons have gap at least \(\delta\) by
Sections 2--3. Apply the complete ordinary and terminal finite-source
envelopes, sum their finitely many currents and physical majorants,
and spend one total tolerance \(\tau\). Their compact source
neighborhoods are provided by Section 1's source-domain theorem.
The original holomorphic interpolants and zero-safe finite products
supply Cauchy estimates for the fixed color jets; a modulus halfweight
is never differentiated as a holomorphic function. This proves (11).
Choose \(\tau<\delta/4\) and absorb the polynomial prefactor in a
further \(\delta/4\) reserve. The finite rate then retains gap
\(\delta/2\). \(\square\)

Every actual open-word suffix with \(m\ge3\), types
\((n_{m-2},n_{m-1},n_m)=(4,4,3+\epsilon)\), and an unselected
incoming leg satisfies these local reference hypotheses. For \(m=3\)
the incoming reference is attached to the first endpoint; for \(m>3\)
it is ordinary. The original uniqueness theorem identifies both with
the canonical family, without requiring arbitrary canonical parameters
to be realized by finite words.

The theorem is local to the target product (6). It does not cover an
incoming type-three reference, a selected incoming leg, or a length-two
word whose preceding factor is an endpoint rather than an ordinary
kernel. A selected incoming leg changes both its target height and
complete Fourier weight and requires a larger joint window. The bound
also does not control outer real tails, nonplateau height graphs, or
their reset and joining faces. Its incoming affine marginal must still
be matched to the adjoining original source with the complementary
halfweight. Thus even after (S) is discharged, a whole open-word
asymptotic, nonzero global coefficient, arbitrary short-filling theorem
and cofinite knot-volume conclusion require separate assembly work.
