# The exact scalar in the filled main-meridian profile

Private derivation, 1 November 2026. This file does not change a published source. It computes the scalar left explicit in `notes/actual_main_meridian_filled_volume.md`, Sections 1–2, from the actual ribbon, duality and reference-map formulas. The calculation is independent of a geometric cusp-shape identification.

## 1. Statement and convention

Fix one actual oriented Conway knot diagram, with the original ordered products, physical quarter-turns, cylindrical cut and transported mark. Its physical crossing boxes are the integral words \(R^{n_i}\), where the signed integer is the exponent of the actual checked crossing used by the compiler. In a note that calls a geometric pretzel integer \(a_i\) but inserts \(R^{-a_i}\), the integer in this report is \(n_i=-a_i\). Let \(w(D)\) be the oriented blackboard self-writhe of the resulting one-component diagram. Planar joining arcs and quarter-turns add no crossings or curls. If a different drawing introduces a framing curl, its crossing and writhe must both be included.

Put
\[
 q=e^{\pi i/N},\qquad d=N-1,\qquad
 \alpha=d+s,\qquad M=-q\,q^\alpha=q^s.
 \tag{1}
\]
The module with parameter \(s\) is denoted by \(V_+\), and its actual dual, with parameter \(-s\), by \(V_-\). The two opposite-color ordered objects will be denoted by
\[
 A=V_+\otimes V_-,\qquad B=V_-\otimes V_+.
 \tag{2}
\]
Use precisely the coherent carriers in the actual Newton compiler:
\[
 G_A=I,\qquad G_B=\check R_{+,-}r_0(\Omega_A)^{-1},
 \qquad C_{D,C}=G_DG_C^{-1}.
 \tag{3}
\]
Here \(r_0\) is the full complete crossing polynomial, including its Cartan scalar and its coefficients at repeated spectral roots. No scalar normalization of this polynomial is made.

Let \(A_N(s)\) be the scalar in the filled profile, excluding the single reduced-cut factor \(H_N(s)\) and excluding the edge insertions \(H_N/W_k\). Then, in this fixed compiler,
\[
 \boxed{\displaystyle
 A_N(s)=q^{\,a(D)s^2/2},\qquad
 a(D)=-w(D)-\sum_i n_i.}
 \tag{4}
\]
This is an equality of the explicitly defined scalar ledger, not an exact equality of the whole invariant with its leading asymptotic. In particular there is no surviving term linear in \(s\), no scalar \(M^{cN}\), and no additional meridian-dependent cup or mark factor in \(A_N\).

For the standard positive checked braid convention, let \(o_i=+1\) when the two oriented strands in the original crossing disk are parallel and \(o_i=-1\) when they are antiparallel. These signs refer to the actual knot orientation, before any artificial reinterpretation of a dual strand as an upward vector-space factor. Reversing one tangent reverses the oriented crossing sign; reversing both preserves it. Hence
\[
 w(D)=\sum_i o_i n_i,\qquad
 \boxed{\displaystyle a(D)=-2\sum_{i:\,o_i=+1}n_i.}
 \tag{5}
\]
Formula (4) is the convention-safe form if a diagram uses a different name for a positive box. Formula (5) follows after translating its box integers into the actual \(R\)-exponents. It does not identify \(a(D)\), by itself, with a knot invariant or a geometric longitude. In particular \(a(D)\) is an even integer. Every power of \(q\) in this report means its actual exponential with \(\log q=\pi i/N\), as fixed by the unrolled source; no logarithmic branch is chosen afterward.

## 2. Closing, the mark, and the absence of another monomial

The actual unrolled twist is
\[
 \theta_\alpha=q^{(\alpha^2+2(1-N)\alpha)/2}.
 \tag{6}
\]
At \(\alpha=d+s\), its exponent completes the square:
\[
 \theta_{d+s}=q^{(s^2-d^2)/2},\qquad
 \frac{\theta_{d+s}^{-w}}{\theta_d^{-w}}
                         =q^{-ws^2/2}.
 \tag{7}
\]
The same formula holds for the dual color \(d-s\). Thus the actual zero-framing correction is already a purely quadratic scalar. The linear term in the common crossing Cartan factor must not be separately retained after this substitution and after the exact shifted-grid calculation below.

The claim that no other scalar remains at the closing cut uses the actual matrices, rather than a convention about the size of a normalization. In `relative_pivotal_duality.md`, Section 2, the standard-frame dualities satisfy
\[
 (J_x^{-1})^t J_y=K^{1-N}=g,\qquad y=x^{-1}Q^{-1}.
 \tag{8}
\]
with no scalar. The displayed left and right evaluation/coevaluation maps obey all four snake identities exactly. Their powers of \(x\), including the powers of order \(N\), are part of these maps. They are therefore present in the physical turns, not available for an additional multiplication outside the compiler.

The original cut projector also fixes its normalization exactly. In the balanced basis it is \(e=\psi\varphi\), where \(\psi_a=1\), \(\varphi_a=1/N\), and \(\operatorname{Tr}e=1\). With the marked defect \(D=g^{-1}e\),
\[
 \operatorname{Tr}(gDC)=\operatorname{Tr}(eC).
 \tag{9}
\]
For the actual cut operator \(C=cI\), this is \(c\). Moving the mark requires transporting the whole defect, so (9) still computes the same scalar. It does not permit a new factor obtained by replacing the transported defect by a fresh local matrix. These are the identities in `quantum_bridge_cap_source.md`, Sections 1–2. In particular its \(N^kN^{-(k-1)}N^{-2}=N^{-1}\) cap count is independent of the color; the remaining color monomials have not been discarded.

There is an equivalent direct two-string closure calculation. For the complete normalization \(s_0=(-1)^dN^2\), the actual partial pivotal moment is
\[
 \operatorname{ptr}_{g_2}\Omega^r=0\quad(r<d),\qquad
 \operatorname{ptr}_{g_2}\Omega^d=s_xI,\qquad
 \frac{s_x}{s_0}
 =\frac{\sin\pi s}{N\sin(\pi s/N)}=:H_N(s).
 \tag{10}
\]
Both left and right closings, and either choice of the surviving dual color, have the same ratio. If \(f_D\) is the polynomial of the whole unframed physical operator after the actual closing turn has been retained, then
\[
 F_{D,\mathrm{raw}}(q^s)=H_N(s)\phi_\sigma(f_D).
 \tag{11}
\]
This is compiler Section 5, equations (21)–(23), applied before the zero-framing scalar. The polynomial \(f_D\) contains every physical crossing and physical turn. Its normalization contains no independent boundary monomial. An alternative cap closure first performs its actual closing turn and then uses (11).

Consequently, if all crossing powers and turn scalars are assigned to their local entries, the remaining closing scalar of the filled theorem has the exact complete-value ratio
\[
 \frac{\zeta_{\mathrm{closing},N}(s)}
      {\zeta_{\mathrm{closing},N}(0)}
                         =q^{-w(D)s^2/2}.
 \tag{12}
\]
Constants depending only on \(N\), such as a fixed Fourier or complete balancing convention, cancel from this ratio. An explicitly relocated reference factor must of course be returned to its local entry before using (12). No such relocation changes the total in (4).

There is a different, legitimate intermediate normalization in the rationality proof of `kashaev_ado_pointing.md`, Section 1. It strips the common factor \(q^{\alpha^2/2}\) from each crossing of a same-color braid. In that stripped convention the combined Cartan and framing ratio is
\[
 q^{w(ds+s^2/2)}q^{-ws^2/2}=q^{wds}.
 \tag{12a}
\]
Thus a linear term appears in that intermediate gauge. The filled compiler uses the full physical crossings, whose Cartan factors are already included in (24); its remaining closing factor is (12), not (12a). Multiplying a full-crossing computation by the stripped convention's monomial would count the Cartan normalization twice. The fact that an intermediate formula contains a linear term therefore supplies no additional factor for the ledger here.


## 3. The four mixed generators, including negative odd words

The full monodromy identity from the turn comparison, Section 3, equations (41)–(42), is
\[
 \check R_{-,+}\check R_{+,-}
                       =q^{-s^2}r_0(\Omega_A)^2.
 \tag{13}
\]
Its proof separates the channels by a generic perturbation of the sum of the highest weights and then continues the full polynomial identity. Thus (13) retains derivatives at repeated roots; a nodal-only statement would not suffice.

Removing the coherent carrier (3) gives:

| Starting order | Physical generator | Extracted polynomial |
| --- | --- | --- |
| \(A\) | \(\check R_{+,-}\) | \(r_0\) |
| \(B\) | \(\check R_{-,+}\) | \(q^{-s^2}r_0\) |
| \(A\) | \(\check R_{-,+}^{-1}\) | \(q^{s^2}r_0^{-1}\) |
| \(B\) | \(\check R_{+,-}^{-1}\) | \(r_0^{-1}\) |

Every crossing swaps the order, regardless of its sign. For a word of length \(L\), signs \(\delta_j\in\{1,-1\}\), and net exponent \(n=\sum_j\delta_j\), the exponent of \(q^{s^2}\) starting at \(A\) is
\[
 \frac{L-n}{2}-\left\lfloor\frac L2\right\rfloor
                         =-\left\lfloor\frac n2\right\rfloor.
 \tag{14}
\]
Starting at \(B\) replaces the floor of \(L/2\) by its ceiling, giving \(-\lceil n/2\rceil\). Therefore
\[
 f_{n,A}=q^{-\lfloor n/2\rfloor s^2}r_0^n,\qquad
 f_{n,B}=q^{-\lceil n/2\rceil s^2}r_0^n.
 \tag{15}
\]
These formulas apply to negative integers and to alternating positive and negative odd blocks. For example \(n=-1\) starting at \(A\) has factor \(q^{s^2}\), whereas starting at \(B\) it has factor one. Replacing a negative odd reference by the coherent carrier is done once; adding its conversion again to (15) would be a double count.

For later use, write \(\delta(n)\in\{0,1\}\) for the parity of \(n\), using Euclidean division even when \(n<0\). In units of \(s^2/2\), (15) has scalar exponent
\[
 -2\lfloor n/2\rfloor=-n+\delta(n),\qquad
 -2\lceil n/2\rceil=-n-\delta(n).
 \tag{16}
\]
The two parity terms will cancel against the turns. This is why treating every mixed word as a scalar \(q^{-ns^2/2}\) before retaining the reference maps would be incorrect locally, even though that scalar is the final global result.

## 4. A boundary grading makes all turn phases telescope

Assign an integer \(\chi\) to the six actual spaces of polynomial morphisms:
\[
 \begin{array}{c|c}
 \text{space}&\chi\\ \hline
 \operatorname{End}(V_+\otimes V_+),\
 \operatorname{End}(V_-\otimes V_-)&0\\
 \operatorname{End}(A),\ \operatorname{End}(B)&0\\
 \operatorname{Hom}(A,B)&1\\
 \operatorname{Hom}(B,A)&-1 .
 \end{array}
 \tag{17}
\]
This is an integer assigned to an ordered boundary type, not a scalar extracted from an unknown invariant. On the opposite-color category it is \(h(\text{target})-h(\text{source})\), with \(h(A)=0,h(B)=1\). Consequently \(\chi(YX)=\chi(Y)+\chi(X)\) for every compatible product.

The exact six-type table in `actual_main_meridian_turn_comparison.md`, Section 3, has scalar
\[
 \gamma_{\mathscr T}(s)
                  =q^{(\chi_{\mathrm{out}}-\chi_{\mathrm{in}})s^2/2}.
 \tag{18}
\]
Indeed the four successive types have \(\chi\)-values \(0,-1,0,1,0\), so their exponents are \(-1,+1,+1,-1\); the opposite-color endomorphism turns have exponent zero. The paired operator \(H_N^{-1}\mathcal R\operatorname{diag}W\) is separate from this scalar.

An equivalent algebraic proof removes all turn phases at once. In a space of type \(\chi\), replace a coordinate polynomial \(f\) by
\[
                         \widetilde f=q^{-\chi s^2/2}f.
 \tag{19}
\]
Compatible products remain ordinary multiplication because \(\chi\) adds. Every turn loses precisely its scalar (18). The final true endomorphism has \(\chi=0\), so the root scalar is unchanged. This is only a proof of scalar cancellation; it is not a change to the actual definition of the invariant.

At an opposite-color word \(R^n\), its input-output type has \(\chi=\delta(n)\) if it starts at \(A\), and \(\chi=-\delta(n)\) if it starts at \(B\). Equations (16) and (19) therefore leave the scalar
\[
                              q^{-ns^2/2}.
 \tag{20}
\]
In the original coordinates the same statement is
\[
 \sum_{\text{actual turns}}(\chi_{\mathrm{out}}-\chi_{\mathrm{in}})
                    =-\sum_{\text{crossing leaves}}\chi_i,
 \tag{21}
\]
since products add \(\chi\) and the closing endomorphism has \(\chi=0\). Thus every floor/ceiling parity term cancels, for either starting order and any signs of the powers.

The argument must be performed on the original typed expression. Lowering its vertices with compatible reverse Hom spaces closes their carriers to the identity. Reassociating that finite contraction retains each original edge tensor and its scalar. If an edge is subsequently described using a different forward turn, its already determined scalar ratio must be kept. One cannot apply (21) to a new untyped physical word inferred from commutativity.

## 5. Equal-color crossings and the global result

At an equal-color vertex with \(\sigma=s\) or \(-s\), the full crossing eigenvalue has common Cartan scalar
\[
 \kappa_\sigma=q^{(d+\sigma)^2/2}.
 \tag{22}
\]
Writing its actual grid as
\[
 \tau_j=\frac{2\pi}{N}\left(\frac d2+\sigma-j\right)
 \tag{23}
\]
gives the exact identity, including the finite sign \((-1)^j\),
\[
 \kappa_\sigma(-1)^j q^{j(j+1)-2\sigma j}
       =q^{d^2/4-\sigma^2/2}
                       \exp\left(\frac{iN\tau_j^2}{4\pi}\right).
 \tag{24}
\]
For an integer crossing power \(n\), all factors are raised with their actual integer powers. Hence the complete-value ratio of its explicit chirp scalar is exactly \(q^{-n\sigma^2/2}=q^{-ns^2/2}\). This is the factor used in the regular-circle and direct-crossing trace theorems. In particular the apparent linear term \(d\sigma\) in (22) has not been omitted: it is absorbed by the actual translated grid (23), as the equality (24) shows.

Equal-color crossing leaves have \(\chi=0\). Combining (20), (21) and (24), the product of all edge and crossing/reference factors in the filled profile is therefore
\[
 \boxed{\displaystyle
 \left(\prod_e\gamma_e(s)\right)
 \left(\prod_{i\text{ equal}}q^{-n_i\sigma_i^2/2}\right)
 \left(\prod_{i\text{ opposite}}\rho_i^{(n_i)}(s)\right)
                         =q^{-(\sum_i n_i)s^2/2}.}
 \tag{25}
\]
Multiplication by the remaining zero-framing ratio (12) proves (4). This proof includes the original root closing turn. It also includes any pure leaf as the case \(n_i=0\).

There is a useful filling form of the answer. Retain the original parity representatives \(n_i=\epsilon_i-2p_i\). Even twists do not change the oriented pairing, so the signs \(o_i\) are unchanged. If \(w_\epsilon=\sum_i o_i\epsilon_i\) is the writhe of the retained half-twist diagram, then
\[
 \begin{aligned}
 a(D)
  &= -w_\epsilon-\sum_i\epsilon_i
                            +2\sum_i(o_i+1)p_i\\
  &= -w_\epsilon-\sum_i\epsilon_i
                            +4\sum_{i:\,o_i=+1}p_i.
 \end{aligned}
 \tag{26}
\]
In particular pure parallel fillings contribute \(4p_i\), whereas antiparallel fillings contribute zero to this integer. The same quantities occur in the independent geometric surgery bookkeeping through the squared linking number of a crossing circle, but that interpretation is not used in the proof.

## 6. Consequences for the profile and its first correction

For the class and independently long fixed slopes in the filled-volume theorem, substitute (4) into its already established asymptotic:
\[
 \frac{F_N(q^s)}{F_N(1)}
   =H_N(s)q^{a(D)s^2/2}
       \left(1-\frac{\pi s^2}{N}
                    \sum_e\cot(\pi x_e^{\mathrm{fill}})
                      +O(N^{-2})\right).
 \tag{27}
\]
All estimates are uniform on a fixed disk \(|s|\le R<1\). The integers \(n_i\), the orientation pattern and the presentation are fixed before \(N\) tends to infinity. The edge sum is the same filled complex saddle sum as in that theorem.

The exact bound \( |\log A_N(s)|\le \pi|a(D)|R^2/(2N) \), using the specified exponential, shows that the scalar tends to one uniformly. Moreover, \(H_N(s)=\sin(\pi s)/(\pi s)+O_R(N^{-2})\). Consequently
\[
 \frac{F_N(q^s)}{F_N(1)}
       \longrightarrow\frac{\sin\pi s}{\pi s}
 \tag{28}
\]
locally uniformly before the first ordinary resonance. This conclusion uses the proved filled packet, not scalar bookkeeping alone. The full modified-trace invariant has dimension ratio exactly \(1/H_N\), so its normalized profile tends to one. Neither statement asserts a uniform profile across \(s=\pm1\).

More precisely, without dividing out the scalar,
\[
 \frac{F_N(q^s)}{F_N(1)H_N(s)}
  =1+\frac{s^2}{N}
       \left(\frac{i\pi a(D)}2
                   -\pi\sum_e\cot(\pi x_e^{\mathrm{fill}})\right)
           +O(N^{-2}).
 \tag{29}
\]
Thus omitting \(A_N\) can change the first correction even though it changes neither the leading disk profile nor the logarithmic volume. With \(z=2\pi i s\), (29) becomes
\[
 1+\frac{z^2}{8\pi iN}
       \left(a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}})\right)
          +O(N^{-2}).
 \tag{30}
\]
The parenthesis is the precise quantity to compare with the actual preferred main longitude. No such geometric identification is inferred here.

## 7. Exact scope and proof dependencies

The scalar calculation uses no positive-pressure estimate, no quantum volume conjecture and no expected cusp shape. Its inputs are the fixed unrolled ribbon twist and reduced ADO normalization; exact duality, pivot and marked cut; the actual six-type turn table; full mixed monodromy; and the exact equal-color shifted-grid identity.

The relevant repository sources are:

- `notes/kashaev_ado_pointing.md`, Sections 1–2: the zero-framed reduced family, its twist, and its all-parity complete specialization.
- `notes/relative_pivotal_duality.md`, Sections 1–2, and `notes/quantum_bridge_cap_source.md`, Sections 1–2: the exact dual lift, double dual, four caps/cups and marked projector.
- `notes/actual_main_meridian_newton_compiler.md`, Sections 4–5: coherent carriers, physical currying and primitive closing trace.
- `notes/actual_main_meridian_turn_comparison.md`, Section 3, equations (41)–(43) and its six-type table.
- `notes/actual_main_meridian_regular_circle_trace.md`, Sections 1–3, and `notes/actual_main_meridian_direct_crossing_trace.md`: the actual shifted grid, full chirp constant and its integer powers.
- `notes/actual_main_meridian_filled_volume.md`, Sections 1–2 and 7: the filled profile and the edge insertion correction to which the explicit scalar is applied.

A different coherent carrier gauge can redistribute the integer phases among edges and odd vertices, but the compatible product and closing identities prove that their total is unchanged. A different framing changes the explicit twist factor and must be recorded. A different reduced cut normalization would define a different scalar; it is not permitted under the conventions above. No equality between generic quantum operators or classical geometric factors is asserted.
