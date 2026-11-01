# Framing and the exact scalar in the main-meridian profile

1 November 2026.

Moving the main meridian changes the physical crossing matrices, the maps that bend strands, and the scalar used to correct the diagram to zero framing. These changes must be kept together. A factor that is harmless for the exponential volume rate can still contribute to the first correction of order \(1/N\).

This note computes the scalar retained in [the filled main-meridian profile](actual_main_meridian_filled_volume.md). The answer is a single quadratic phase. Its exponent is determined by the actual crossing powers and the oriented writhe of the diagram. The proof uses the physical duality maps and crossing normalization; the preferred cusp shape is identified by a separate geometric calculation.

## 1. Statement and convention

Fix an oriented Conway knot diagram \(D\), built from ordered products, physical quarter-turns and two-strand crossing boxes. The order of its endpoints and its original reduced cut are retained. A product stacks compatible two-strand operators; a quarter-turn bends one incoming strand into an outgoing strand and one outgoing strand into an incoming strand.

The crossing boxes contain the integral words \(R^{n_i}\). Here \(n_i\) is the signed exponent of the actual checked crossing: the crossing matrix followed by the interchange of its two tensor factors. For example, if another diagram convention calls a pretzel integer \(a_i\) but inserts \(R^{-a_i}\), then \(n_i=-a_i\) in the formulas below. Let \(w(D)\) be the oriented writhe, the sum of the oriented crossing signs in the one-component diagram. It is the linking number of the knot with its blackboard parallel. Planar joining arcs and quarter-turns add no crossings or curls. Any additional framing curl must be included in both the physical word and its writhe.

Put
\[
 N\ge2,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad d=N-1,\qquad
 \alpha=d+s,\qquad M=-q\,q^\alpha=q^s.
 \tag{1}
\]
The reduced ADO invariant \(F_N(M)\) is the scalar of the actual cut \((1,1)\)-tangle, corrected to zero framing and normalized so that the unknot has value one. It is the full modified-trace invariant divided by its modified dimension. The coordinate \(M\) in (1) is the marked meridian; \(s=0\) is its complete value \(M=1\). This is the normalization fixed by [the ADO comparison](kashaev_ado_pointing.md).

The \(N\)-dimensional highest-weight module with weight \(d+s\) is denoted by \(V_+\), and its actual dual, with weight \(d-s\), by \(V_-\). Their highest-root coordinates are \(x=-q^{-1}q^s\) and \(y=-q^{-1}q^{-s}\). The two opposite-color ordered objects are
\[
 A=V_+\otimes V_-,\qquad B=V_-\otimes V_+.
 \tag{2}
\]
A change of order from \(A\) to \(B\) is represented by an actual invertible intertwiner. To express all such maps as polynomials in a Casimir operator, the [Newton compiler](actual_main_meridian_newton_compiler.md), Section 4, fixes the following reference maps:
\[
 G_A=I,\qquad G_B=\check R_{+,-}r_0(\Omega_A)^{-1},
 \qquad C_{D,C}=G_DG_C^{-1}.
 \tag{3}
\]
Here \(\Omega_A\) is the total quantum Casimir acting on \(A\). Every intertwiner of this type is a polynomial in the Casimir after its reference map is removed. The polynomial \(r_0\) is the full complete crossing, including its Cartan scalar. Its values are nonzero at every spectral root, so it is invertible in the finite Casimir algebra. This algebra also retains the first derivatives at repeated roots; these data are not replaced by values alone. Formula (3) uses the full polynomial inverse in that algebra.

The remaining factors that depend on a wire index are
\[
 H_N(s)=\frac{\sin\pi s}{N\sin(\pi s/N)},\qquad H_N(0)=1,
 \qquad
 W_k(s)=\prod_{r=1}^k
 \left(1-\frac{\sin^2(\pi s/N)}{\sin^2(\pi r/N)}\right),
 \quad 0\le k<N.
 \tag{3a}
\]
The factor \(H_N\) comes from the actual reduced cut. The ratios \(H_N/W_k\) occur on physical turn edges. They are kept separately because their dependence on the internal label \(k\) contributes to the first asymptotic correction.

Let \(A_N(s)\) be the product of the remaining normalized scalar factors: the zero-framing scalar, the six-type turn scalars, the equal-color crossing phases, and the reference factors of opposite-color crossing words. Every factor is divided by its value at \(s=0\). The single reduced-cut factor \(H_N\) and the index-dependent edge ratios \(H_N/W_k\) are excluded. Then
\[
 \boxed{\displaystyle
 A_N(s)=q^{\,a(D)s^2/2},\qquad
 a(D)=-w(D)-\sum_i n_i.}
 \tag{4}
\]
This is an exact identity for the scalar just defined. An asymptotic statement about the whole invariant requires the separate estimates of its finite sum. The identity shows that \(A_N\) has no surviving term linear in \(s\) and no additional meridian-dependent cup or cut factor.

For the standard positive checked braid convention, let \(o_i=+1\) when the two oriented strands in the original crossing disk are parallel and \(o_i=-1\) when they are antiparallel. These signs refer to the actual knot orientation, before any artificial reinterpretation of a dual strand as an upward vector-space factor. Reversing one tangent reverses the oriented crossing sign; reversing both preserves it. Hence
\[
 w(D)=\sum_i o_i n_i,\qquad
 \boxed{\displaystyle a(D)=-2\sum_{i:\,o_i=+1}n_i.}
 \tag{5}
\]
Formula (4) retains the actual writhe and the actual \(R\)-exponents. Formula (5) is its form in the standard positive-braid convention. The integer \(a(D)\) is even and depends on this diagrammatic decomposition; it is not, by itself, a knot invariant. Every power of \(q\) means the exponential with \(\log q=\pi i/N\) fixed by the unrolled source.

The scalar identity holds for every oriented Conway knot diagram to which the typed compiler applies. The moving-meridian asymptotic in Section 6 has narrower hypotheses. In particular the broader complete-value volume theorem for strict Conway trees does not, by itself, supply that moving profile.

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

The closing calculation uses the actual evaluation maps. In [the pivotal duality calculation](relative_pivotal_duality.md), Section 2, the Cartan generator acts by \(Kv_a=xQ^{-a}v_a\). If \(\varphi_a\) is the dual basis, the selected module duality is
\[
 J_xw_a=c_a(x)\varphi_{d-a},\qquad
 c_a(x)=(-x)^aQ^{a(a+1)/2}.
 \tag{8a}
\]
Its double dual is exactly
\[
 (J_x^{-1})^t J_y=K^{1-N}=g,\qquad y=x^{-1}Q^{-1}.
 \tag{8}
\]
Here the superscript \(t\) is matrix transpose. Indeed the \(a\)-th diagonal entry on the left of (8) is \(c_a(y)/c_{d-a}(x)=x^{1-N}Q^{a(N-1)}\), the corresponding entry of \(g\). This includes both parities of \(N\).

The left and right evaluation/coevaluation maps obey the four snake identities: bending a strand out and back returns the identity. Their powers of \(x\), including those of order \(N\), are already part of the physical turns. They do not leave an additional scalar outside those maps.

The original cut projector also fixes its normalization exactly. In the balanced basis it is \(e=\psi\varphi\), where \(\psi_a=1\), \(\varphi_a=1/N\), and \(\operatorname{Tr}e=1\). With the marked defect \(\mathcal{D}=g^{-1}e\),
\[
 \operatorname{Tr}(g\mathcal{D}C)=\operatorname{Tr}(eC).
 \tag{9}
\]
For the actual cut operator \(C=cI\), this is \(c\). Moving the mark transports the whole defect, so (9) computes the same scalar. The [explicit cap and marked-cut formulas](quantum_bridge_cap_source.md), Sections 1–2, give \(N^kN^{-(k-1)}N^{-2}=N^{-1}\) for a presentation with \(k\) cups, \(k-1\) ordinary caps and one marked cap. This count is independent of the color; all remaining color monomials stay in the evaluation maps.

There is an equivalent direct two-string closure calculation. The normalized functional \(\phi_\sigma\) on the finite Casimir algebra is
\[
 \phi_\sigma(f)=s_0[z^d]f,\qquad s_0=(-1)^dN^2.
 \tag{9a}
\]
The polynomial is first reduced to degree less than \(N\) in the actual algebra. Here \(\sigma=s\) or \(-s\) for equal colors and \(\sigma=0\) for opposite colors. The symbol \([z^d]\) means the coefficient of \(z^d\). Thus \(\phi_\sigma\) keeps the whole polynomial, including its repeated-root coefficients. The actual partial pivotal moments are
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
This is [the compiler's primitive closing formula](actual_main_meridian_newton_compiler.md), Section 5, equations (21)–(23), applied before the zero-framing correction. The polynomial \(f_D\) contains every physical crossing and physical turn. An alternative cap closure first performs its actual closing turn and then uses (11).

Consequently, if all crossing powers and turn scalars are assigned to their local entries, the remaining closing scalar of the filled theorem has the exact complete-value ratio
\[
 \frac{\zeta_{\mathrm{closing},N}(s)}
      {\zeta_{\mathrm{closing},N}(0)}
                         =q^{-w(D)s^2/2}.
 \tag{12}
\]
Constants depending only on \(N\), such as a fixed Fourier or complete balancing convention, cancel from this ratio. An explicitly relocated reference factor must of course be returned to its local entry before using (12). No such relocation changes the total in (4).

The rationality proof in [the ADO normalization](kashaev_ado_pointing.md), Section 1, uses a different intermediate normalization: it strips the common factor \(q^{\alpha^2/2}\) from each crossing of a same-color braid. In that convention the combined Cartan and framing ratio is
\[
 q^{w(ds+s^2/2)}q^{-ws^2/2}=q^{wds}.
 \tag{12a}
\]
Thus a linear term appears in that intermediate gauge. The filled compiler uses the full physical crossings, whose Cartan factors are already included in (24); its remaining closing factor is (12), not (12a). Multiplying a full-crossing computation by the stripped convention's monomial would count the Cartan normalization twice. The fact that an intermediate formula contains a linear term therefore supplies no additional factor for the ledger here.


## 3. The four mixed generators, including negative odd words

The full monodromy identity from [the turn comparison](actual_main_meridian_turn_comparison.md), Section 3, equations (41)–(42), is
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

We denote the scalar multiplying \(r_0^n\) in (15) by \(\rho_N^{(n)}(s)\), with the starting order retained. Its complete value is one. This is the opposite-color factor used in the global product below.

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

The six forward physical turns have the following scalar exponents. An entry \(a\) means multiplication by \(q^{as^2/2}\), in addition to the paired sine-product operator.

| Input space | Output space | \(a\) |
| --- | --- | ---: |
| \(\operatorname{End}(V_+\otimes V_+)\) | \(\operatorname{Hom}(B,A)\) | \(-1\) |
| \(\operatorname{Hom}(B,A)\) | \(\operatorname{End}(V_-\otimes V_-)\) | \(1\) |
| \(\operatorname{End}(V_-\otimes V_-)\) | \(\operatorname{Hom}(A,B)\) | \(1\) |
| \(\operatorname{Hom}(A,B)\) | \(\operatorname{End}(V_+\otimes V_+)\) | \(-1\) |
| \(\operatorname{End}(A)\) | \(\operatorname{End}(B)\) | \(0\) |
| \(\operatorname{End}(B)\) | \(\operatorname{End}(A)\) | \(0\) |

These are the actual maps of [the six-type turn theorem](actual_main_meridian_turn_comparison.md), Section 3. In each row the exponent is \(\chi_{\mathrm{out}}-\chi_{\mathrm{in}}\). Thus its scalar is
\[
 \gamma_{\mathscr T}(s)
                  =q^{(\chi_{\mathrm{out}}-\chi_{\mathrm{in}})s^2/2}.
 \tag{18}
\]
Indeed the four successive types have \(\chi\)-values \(0,-1,0,1,0\), so their exponents are \(-1,+1,+1,-1\); the opposite-color endomorphism turns have exponent zero. The remaining operator is \(H_N^{-1}\mathcal R\operatorname{diag}W\), where \(\operatorname{diag}W\) multiplies Newton coefficient \(k\) by \(W_k\) and \(\mathcal R\) reverses the \(N\) coefficients, sending index \(k\) to \(d-k\). It is separate from this scalar.

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

The argument is performed on the expression with its actual ordered input and output spaces. To rewrite it as a contraction with all indices incoming, pair each output with the compatible reverse morphism space. The reference maps around each resulting vertex compose to the identity. Reassociating this finite contraction retains every original edge tensor and its scalar. If an edge is described using a different forward turn, the known ratio of the two turn scalars is kept. No interchange of physical tangles is used.

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
gives the exact quadratic-exponential identity, including the finite sign \((-1)^j\),
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

There is a useful filling form of the answer. Let \(\epsilon_i\in\{0,\pm1\}\) be the retained half twist at auxiliary crossing circle \(i\), and let \(p_i\in\mathbb Z\) be its integer filling coefficient in the original primitive slope \(\mu_i+p_i\lambda_i\). The resulting crossing power is \(n_i=\epsilon_i-2p_i\). Even twists do not change the oriented pairing, so the signs \(o_i\) are unchanged. If \(w_\epsilon=\sum_i o_i\epsilon_i\) is the writhe of the retained half-twist diagram, then
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

## 6. The moving profile and the preferred cusp

The scalar identity above requires no strict geometric saddle or long-twist assumption. To apply it to an asymptotic, impose the hypotheses of [the filled main-meridian theorem](actual_main_meridian_filled_volume.md), Section 1.

Here is the distinction in terms of the tangle operations. Combine consecutive multiplications with no intervening turn into a product junction. A junction is marked if it contains an original crossing-circle operator and bare if it does not. The moving theorem includes strict trees with no adjacent bare junctions, and the larger class satisfying the explicit finite component-path inequality in that theorem. The knot pattern and its retained parity choices are fixed. The two-leaf case retains its stated pure-leaf qualification.

For this class there is one presentation-dependent threshold \(B\) such that the theorem holds for all fixed signed crossing powers \(n_i=\epsilon_i-2p_i\) with \(|n_i|\ge B\). The signs and magnitudes are independent; no ratio between the magnitudes is bounded. They are fixed before \(N\) tends to infinity. The threshold is independent of the subsequent fixed disk \(0\le R<1\). Both even and odd levels are included.

Substitution of (4) into that theorem's second-order insertion formula gives
\[
 \frac{F_N(q^s)}{F_N(1)}
   =H_N(s)q^{a(D)s^2/2}
       \left(1-\frac{\pi s^2}{N}
                    \sum_e\cot(\pi x_e^{\mathrm{fill}})
                      +O(N^{-2})\right).
 \tag{27}
\]
All estimates are uniform on a fixed disk \(|s|\le R<1\). The integers \(n_i\), the orientation pattern and the presentation are fixed before \(N\) tends to infinity. The edge sum is the same filled complex saddle sum as in that theorem.

The exact bound \( |\log A_N(s)|\le \pi|a(D)|R^2/(2N) \), using the specified exponential, shows that the scalar tends to one uniformly. Moreover, \(H_N(s)=\sin(\pi s)/(\pi s)+O_R(N^{-2})\). Consequently the reduced invariant has the limit
\[
 \frac{F_N(q^s)}{F_N(1)}
       \longrightarrow\frac{\sin\pi s}{\pi s}
 \tag{28}
\]
locally uniformly before the first ordinary resonance. The quotient at \(s=0\) is assigned its removable value one.

For clarity, the full modified-trace invariant is
\[
 \mathcal N_N(M)=d_N(M)F_N(M),\qquad
 d_N(M)=i^{N+3}\frac{M-M^{-1}}{M^N-M^{-N}},
 \qquad
 \frac{d_N(q^s)}{d_N(1)}=\frac1{H_N(s)}.
 \tag{28a}
\]
The whole germ gives \(d_N(1)=i^{N+3}/N\). Thus its normalized profile tends to one. These profile limits use the proved filled packet, not scalar bookkeeping alone. No continuation of these uniform estimates across \(s=\pm1\) is asserted.

More precisely, without dividing out the scalar,
\[
 \frac{F_N(q^s)}{F_N(1)H_N(s)}
  =1+\frac{s^2}{N}
       \left(\frac{i\pi a(D)}2
                   -\pi\sum_e\cot(\pi x_e^{\mathrm{fill}})\right)
           +O(N^{-2}).
 \tag{29}
\]
Thus omitting \(A_N\) can change the first correction even though it changes neither the leading disk profile nor the logarithmic volume. Set \(z=2\pi i s\), so that the marked meridian is \(M=e^{z/(2N)}\) and its squared coordinate is \(M^2=e^{z/N}\). Equation (29) becomes
\[
 1+\frac{z^2}{8\pi iN}
       \left(a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}})\right)
          +O(N^{-2}).
 \tag{30}
\]
The independent calculation of [the preferred main cusp](actual_main_meridian_preferred_cusp.md) identifies
\[
 \tau_{\mathrm{main}}
       =a(D)+2i\sum_e\cot(\pi x_e^{\mathrm{fill}}).
 \tag{31}
\]
Here the meridian translates by one and the longitude is the primitive preferred longitude, with linking number zero after the auxiliary fillings. That calculation follows the original face maps and the homology of the filled auxiliary slopes. It does not infer the longitude from (30).

Combining the two results gives the geometric form of the first correction:
\[
 \boxed{\displaystyle
 \frac{F_N(q^s)}{F_N(1)H_N(s)}
 =\frac{\mathcal N_N(q^s)}{\mathcal N_N(1)}
 =1+\frac{\tau_{\mathrm{main}}\,z^2}{8\pi iN}
                         +O_{D,\mathbf{n},R}(N^{-2}).}
 \tag{32}
\]
The equality between the two ratios is exact; their common asymptotic is uniform on the fixed disk. The filled theorem already identifies the uniform logarithmic rate there with the actual volume of the resulting knot complement. Only the auxiliary crossing-circle cusps are filled; the main knot cusp stays unfilled.

## 7. Scope of the calculation

The exact scalar calculation uses the ribbon twist, actual duality and marked cut, six-type turns, mixed monodromy and the full shifted-grid crossing identity. The latter is derived in detail in [the regular circle trace](actual_main_meridian_regular_circle_trace.md), Sections 1–3, and [the direct crossing trace](actual_main_meridian_direct_crossing_trace.md). The argument is finite-level algebra and applies at both parities.

Changing coherent reference maps can redistribute scalar phases among edges and odd vertices. Compatible composition and the actual closing cut preserve their total. Changing the framing changes the recorded twist factor. Changing the reduced cut normalization changes the invariant, so that change must be stated separately.

The complete-value volume theorem has broader coverage. In particular [the strict-tree theorem](actual_conway_all_strict_tree_long_twist_volume.md) establishes the long-twist volume equality at \(M=1\) without the additional product-junction restriction used by the moving theorem. The profile and first correction in Section 6 are asserted only for the moving theorem's stated class. Exact knowledge of a framing factor does not supply the remaining estimates for other trees.

The geometric comparison in (31) uses the preferred peripheral curves of the same knot. It does not identify a classical geometric factor of a quantum annihilator, nor does it give a profile on a fixed nonshrinking disk in \(M\). The microscopic coordinate and the exclusion of ordinary resonances remain part of the statement.


## 8. Reproducing the finite identities

The [exact scalar script](../experiments/audit_main_meridian_exact_scalar.py) starts from the two mixed positive crossings, obtains the inverse crossings, and composes signed words with their actual starting and ending orders. It also derives the integer grading from the six turn phases, checks compatible products and turns on finite expression trees, and compares the shifted-grid exponents as rational polynomials. Its [recorded results](../experiments/main_meridian_exact_scalar_results.json) list the inputs and the scope of the checks.

To run the scalar checks together with the geometric matrix identities, use the repository runner:

```sh
python3 repro/run_research_checks.py meridian-cusp
```

The scalar script uses Python's standard library; the geometric script also requires SymPy. These computations check local algebra. The physical tensor formulas, the longitude's topology, and the uniform asymptotic estimates are supplied by the proofs, rather than by a finite list of examples.
