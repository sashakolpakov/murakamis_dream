# Exact one-sided half-charge reduction and its geometric limits

Fix the original matched simple-sphere Morse diagram, its actual cup, cap and unrestricted mark, its crossing-disk frames, and its shared ordinary face targets. The diagram and signed powers are fixed before the level grows. This note is an exact reduction of its LEFT/RIGHT terms. It does not prove that those terms are exponentially smaller than the geometric contribution on every undecorated diagram.

The main conclusions are two finite identities. The omitted-half scalar converts the original integer Fourier lattice at a one-sided port into a half-integer lattice whose smallest modes do not cancel. Independently, the same one-sided port is a compression to a semisimple lower Casimir block. Thus neither an omitted spectral zero nor the first-normal mechanism for complete-channel Morse graphs annihilates it. The final section states precisely which primitive peripheral log would be needed to interpret the half-charge expression geometrically, and why changing that log while keeping the original ordered boundary pair is impossible.

## 1. The source polynomial before applying the crossing functional

Let
\[
 N\ge3,\quad d=N-1,\quad m=\lfloor N/2\rfloor,\quad M=m-1,
 \quad q=e^{\pi i/N},\quad \sigma(\delta)=-2\cos(2\pi\delta).
 \tag{1}
\]
Put \(c_r=2\cos((2r+1)\pi/N)\), \(\alpha_r=c_r-\sigma\), and \(s_r=2\sin(\pi r/N)\). The exact original before/active/after recursion is
\[
 B_r=b\alpha_r B_{r-1},\qquad
 R_r=B_{r-1}+s_r^2(x+y)R_{r-1}
             +s_rs_{r-1}\alpha_{r-1}xyR_{r-2},\qquad
 Z_r=R_r+c\alpha_rZ_{r-1},
 \tag{2}
\]
with \(B_{-1}=1\), \(R_{-1}=R_{-2}=Z_{-1}=0\), and absent endpoint terms zero. In particular
\[
 H_{V,\mathrm L}(x,b,c,y;\sigma)
   =(-1)^d A_N(\delta)\,c^{d-M} Z_M(x,b,c,y;\sigma),
 \tag{3}
\]
where the entire omitted-half product is
\[
 A_N(\delta)=\prod_{r=m}^{d}(c_r-\sigma(\delta))
 =\begin{cases}
 e^{\pi iN\delta}+e^{-\pi iN\delta},&N\text{ even},\\
 2i\sin(\pi\delta)
       (e^{\pi iN\delta}-e^{-\pi iN\delta}),&N\text{ odd}.
 \end{cases}
 \tag{4}
\]
These signs use \(c_r-\sigma\), not its negative. The central odd factor is included. Literal reflection of a decreasing path sends \((i,j)\) to \((d-j,d-i)\). It preserves the unused diagonal factors because \(c_{d-r}=c_r\), the one-step factors because \(s_{N-r}=s_r\), and the two-step factors by reversing their two indices. Hence RIGHT has (3) with \(b,c\) exchanged; no extra scalar or mirror change is needed.

For a fixed assignment of CROSS/LEFT/RIGHT ports let \(J\) be its one-sided set and let \(R\) denote the number of all ports. Coefficient extraction is linear and the factors (4) contain no face variables. The actual shared numerator therefore has the exact factorization
\[
 S_{N,J}(\boldsymbol\delta)
   =(-1)^{d|J|}\prod_{e\in J} A_N(\delta_e)
                      P_{N,J}(\boldsymbol\delta),
 \tag{5}
\]
where \(P_{N,J}\) is obtained using the same shared targets, protected zeros, mark and order as before. It is an even polynomial in each spectral variable \(-2\cos(2\pi\delta_e)\). No independent face radius or phase has been introduced.

## 2. Exact reindexing of the complete Fourier period

Write \(\epsilon_N=(-1)^{N+1}\). Apart from the unchanged exterior framing/component character, the original Fourier-Hermite functional is
\[
 I_{N,J}=C_{N,\boldsymbol n}
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
 \prod_e\ell_e\epsilon_N^{\ell_e}
 \int_{[-1/2,1/2]^R}
 S_{N,J}(\boldsymbol\delta)\prod_e\sin(2\pi\delta_e)
 e^{N\sum_e(\pi in_e\delta_e^2+2\pi i\ell_e\delta_e)}
 \,d\boldsymbol\delta,
 \tag{6}
\]
\[
 C_{N,\boldsymbol n}=q^{d^2\sum_en_e/4}(-i)^R.
 \tag{7}
\]
The complete source normalization, including all root normals, is already in (6). There is no new power of \(N\) in the following change of indices.

At an even level, write \(k=a+1/2\), \(a\in\mathbb Z\). The two modes in (4) receive original weights
\[
 (k-\tfrac12)(-1)^{k-1/2}
 +(k+\tfrac12)(-1)^{k+1/2}
       =-(-1)^a.
 \tag{8}
\]
Terms with original \(\ell=0\) have weight zero, so no missing endpoint term must be added when \(k=\pm1/2\). At an odd level the corresponding calculation is
\[
 2i\bigl[(k-\tfrac12)-(k+\tfrac12)\bigr]=-2i,
 \tag{9}
\]
and the retained slow factor is \(\sin(\pi\delta)\).

Define for a one-sided port
\[
 w_N(k)=\begin{cases}-(-1)^{k-1/2},&N\text{ even},\\-2i,&N\text{ odd},\end{cases}
 \qquad
 b_N(\delta)=\begin{cases}\sin(2\pi\delta),&N\text{ even},\\
 \sin(2\pi\delta)\sin(\pi\delta),&N\text{ odd}.
 \end{cases}
 \tag{10}
\]
Then (6) is exactly
\[
 \begin{split}
 I_{N,J}={}&C_{N,\boldsymbol n}(-1)^{d|J|}
 \sum_{\substack{k_e\in\mathbb Z+1/2\ (e\in J)\\
                  k_e\in\mathbb Z\setminus\{0\}\ (e\notin J)}}
 \left(\prod_{e\in J}w_N(k_e)\right)
 \left(\prod_{e\notin J}k_e\epsilon_N^{k_e}\right)\\
 &\quad\times\int_{[-1/2,1/2]^R}
 P_{N,J}(\boldsymbol\delta)
 \left(\prod_{e\in J}b_N(\delta_e)\right)
 \left(\prod_{e\notin J}\sin(2\pi\delta_e)\right)
 e^{N\sum_e(\pi in_e\delta_e^2+2\pi ik_e\delta_e)}
 \,d\boldsymbol\delta.
 \end{split}
 \tag{11}
\]
This keeps the actual full crossing powers \(n_e=\epsilon_e-2p_e\), including negative powers and the original square-root lift in (7). It is valid separately for every original sector assignment, before any absolute estimate.

### Endpoint currents and convergence

Reindexing is legitimate at fixed \(N,\boldsymbol n\). For an ordinary integer-charge variable the original sine amplitude vanishes at both endpoints; its first derivatives match after multiplication by the endpoint character. Three integrations by parts retain the second-derivative boundary difference and give the usual \(O(|k|^{-3})\) integral and \(O(|k|^{-2})\) weighted term.

For an even-level half-charge variable, the sine amplitude is odd, its first derivatives at \(\pm1/2\) agree, and \(Nk\) is an integer. Thus the same first-derivative cancellation holds. For an odd-level half-charge variable, \(b_N\) is even, its endpoint first derivatives are opposite, and \(Nk\) is a half-integer. The endpoint exponential values are then opposite too. Their two products agree, giving the same cancellation. All spectral polynomials and the quadratic chirp have equal endpoint values; derivatives of these factors do not affect the first derivative because the sine vanishes there.

For each of these variables the exact formula remains
\[
 \int_{-1/2}^{1/2}B(\delta)e^{2\pi iNk\delta}\,d\delta
 =(2\pi iNk)^{-3}
 \left\{[B''(\delta)e^{2\pi iNk\delta}]_{-1/2}^{1/2}
       -\int_{-1/2}^{1/2}B'''(\delta)e^{2\pi iNk\delta}\,d\delta\right\}.
 \tag{12}
\]
The boundary term in (12) is not set to zero. Applying it in all variables proves absolute summability: half-charge weights are bounded and give \(|k|^{-3}\), while ordinary weights give \(|k|^{-2}\). The constants at this point may grow exponentially with \(N\); (12) is a finite-source identity, not a uniform volume estimate. The finite shift and grouping producing (11) are therefore valid, with all currents retained.

### The smallest modes reinforce

At an even level, \(w_N(-k)=-w_N(k)\) and changing \(\delta\) to \(-\delta\) changes the integral by a minus sign. At an odd level both \(w_N\) and the full one-sided amplitude are even. Ordinary coordinates also have two cancelling sign changes. Therefore every sign choice of a fixed positive magnitude vector gives exactly the same contribution. The smallest vector has \(k_e=1/2\) at one-sided ports and \(k_e=1\) elsewhere; its \(2^R\) sign copies reinforce. This proves neither that its integral is nonzero nor that it dominates other magnitudes. It proves that the omitted-half scalar supplies no automatic sign cancellation of those copies.

## 3. The same reduction as a semisimple block

The original source-normalized Casimir acts on the polynomial basis \(z^0,\ldots,z^d\), with outer face variables retained, by
\[
 \Omega z^j=c_jz^j-s_j^2(x+y)z^{j-1}-s_js_{j-1}xy z^{j-2}.
 \tag{13}
\]
The endpoint terms vanish with the actual sine factors. Let \(P_-\) project to \(z^0,\ldots,z^M\). This subspace is invariant. Its block \(\Omega_-\) has distinct diagonal eigenvalues \(c_0,\ldots,c_M\); hence it is semisimple over the rational function field of the outer variables. Its full spectral decomposition is the finite identity
\[
 f(\Omega_-)=\sum_{a=0}^{M} f(c_a)
       \prod_{\substack{0\le b\le M\\b\ne a}}
                    \frac{\Omega_--c_bI}{c_a-c_b}.
 \tag{14}
\]
The denominator scalars are nonzero. Their conditioning as \(N\) grows is not being bounded.

The LEFT numerator in (3) is exactly the face-generating polynomial of
\(P_-V_N(\sigma;\Omega)P_-\), extended by zero outside this block. Applying the original full-Hermite crossing functional commutes with this finite compression and gives \(P_-R^nP_-\). In its lower block (14) uses
\[
 f(c_a)=\kappa^n(-1)^{an}q^{na(a+1)},
                    \qquad\kappa=q^{d^2/2}.
 \tag{15}
\]
Thus the one-sided contribution is a coherent semisimple spectral sum with all its original face coefficients, not a complete-circle nilpotent source.

### The full-Hermite derivative becomes a value functional

Write \(\mathcal L_N^f\) for the actual local full-Hermite functional which sends the numerator \(V_N(\sigma;\Omega)\) to \(f(\Omega)\). Its exact paired-node formula, for any scalar entry \(H(\sigma)\) of the original numerator, is
\[
 \mathcal L_N^f H
 =\sum_{a=0}^{M}\frac{(4-c_a^2)(fH)'(c_a)-c_af(c_a)H(c_a)}{N^2}
   +\mathbf1_{N\text{ odd}}\frac{f(-2)H(-2)}{N^2}.
 \tag{15a}
\]
There is one summand per distinct double node. The last summand is the actual simple node and uses \(\chi_N'(-2)=N^2\). This is the derivative identity of the full source, not an ordinary-value interpolation assumed in advance.

Every entry of the LEFT numerator is divisible by
\(\chi_N(\sigma)/D_-(\sigma)\), where
\(D_-(\sigma)=\prod_{a=0}^{M}(\sigma-c_a)\). Since
\(\chi_N=D_-^2\) at even levels and
\(\chi_N=(\sigma+2)D_-^2\) at odd levels, all its values at all full spectral nodes are zero. Therefore (15a) becomes
\[
 \boxed{\displaystyle
 \mathcal L_N^f H_{V,\mathrm L}
   =\sum_{a=0}^{M} f(c_a)\,
       \frac{4-c_a^2}{N^2}\,
                       \partial_\sigma H_{V,\mathrm L}(c_a).}
 \tag{15b}
\]
No derivative of \(f\) survives. The numerator derivatives in (15b) are retained: they are the exact Lagrange projector polynomials in (14), not a discarded normal or an unknown new source. Indeed on the lower block
\(V_N=\sum_a\chi_N(\sigma)(\sigma-c_a)^{-1}\Pi_a^-\), and
\(\chi_N(\sigma)/(\sigma-c_a)^2\) at \(c_a\) is
\(N^2/(4-c_a^2)\). This proves the identification with (14) directly.

The same calculation applies to RIGHT, using the upper triangular quotient block and the literal row reflection. It also applies with any actual exterior attached: perform the fixed linear face extraction after (15b). With several one-sided ports, apply the corresponding partial derivatives separately to their original shared numerator. Their ordinary values of \(f\) replace only those local spectral normals; the other ports and the one physical cut retain their original full functionals.

For clarity there is also an exact finite grid form of (11). Put
\[
 \mathcal G_N=\begin{cases}
 \{(j+1/2)/N:j\in\mathbb Z,\ |j+1/2|<N/2\},&N\text{ even},\\
 \{j/N:j\in\mathbb Z,\ |j|<N/2\},&N\text{ odd}.
 \end{cases}
 \tag{15c}
\]
At one-sided coordinate, the half-charge sum and its integral equal
\[
 \begin{cases}
 -\dfrac1N\displaystyle\sum_{\delta\in\mathcal G_N}
 e^{\pi iN\delta}\sin(2\pi\delta)\,
 P(\delta)e^{\pi inN\delta^2},&N\text{ even},\\[6pt]
 -\dfrac{2i}{N}\displaystyle\sum_{\delta\in\mathcal G_N}
 e^{\pi iN\delta}\sin(2\pi\delta)\sin(\pi\delta)\,
 P(\delta)e^{\pi inN\delta^2},&N\text{ odd}.
 \end{cases}
 \tag{15d}
\]
The outside scalar \((-1)^d q^{nd^2/4}(-i)\) from (5)–(7) is still outside (15d). For multiple one-sided coordinates use the product of these finite functionals and leave the other original charge integrals unchanged. The odd central grid point has weight zero, exactly as the missing simple-node term in (15b).

Here is a classical Fourier-series proof rather than a formal delta-comb argument. At even levels set
\(G(\delta)=e^{\pi iN\delta}\sin(2\pi\delta)P(\delta)e^{\pi inN\delta^2}\). Its endpoint values and first derivatives match, so its periodic extension has an absolutely convergent Fourier series with coefficient decay of order three. Sampling that series on the half-shifted grid in (15c) selects frequencies \(Na\) with multiplier \((-1)^a\); integrating its Fourier coefficients gives the even formula in (15d). At odd levels use
\(G(\delta)=e^{\pi iN\delta}\sin(2\pi\delta)\sin(\pi\delta)P(\delta)e^{\pi inN\delta^2}\). Its endpoint first derivatives again match: both exponential and unweighted first derivative change sign. Sampling on the unshifted grid selects the required frequencies with multiplier one. Formula (12) retains all second-derivative currents in both arguments. The grid has no endpoint at \(\pm1/2\), so no endpoint half-weight has been silently assigned.

This is a genuine drop from the full-Hermite derivative functional to an ordinary value functional on the compressed block. It does not make that block an ordinary Hopf representation. Nor does it bound the original projector coefficients in (14)–(15b) polynomially in \(N\). There is nevertheless a useful exact norm reduction, uniform in the signed crossing power. For a polynomial of degree at most \(d\) on \([-2,2]\), the usual polynomial derivative bound is \(\|H'\|_\infty\le(d^2/2)\|H\|_\infty\). Applying (15b) gives
\[
 |\mathcal L_N^f H|
 \le 2m\frac{d^2}{N^2}
       \max_{0\le a\le M}|f(c_a)|\,
                    \sup_{-2\le\sigma\le2}|H(\sigma)|
 \le N\max_a|f(c_a)|\,\|H\|_\infty.
 \tag{15e}
\]
This applies to each complex scalar entry and to the already extracted shared coefficient: rotate its derivative to a real part to use the real polynomial inequality. For \(f=R^n\), (15) makes \(\max_a|f(c_a)|=1\), for every signed integer \(n\). Iteration over a one-sided set \(J\) gives at most \(N^{|J|}\) times the same whole shared spectral supremum, uniformly in those powers. The other spectral parameters remain fixed spectators. Thus every one-sided Fourier charge sum can be eliminated by a finite value functional before treating the remaining variables; it needs no derivative of the crossing phase and no infinite-charge tail estimate of its own. This improves the exact functional interface, but it does not improve the numerator's exponential rate. The missing shared geometric bound is still substantive.

This yields an exact boundary obstruction to a source-independent local suppression theorem. In the original four-face polynomial,
\[
 [c^d]H_{V,\mathrm L}(\sigma)
       =\frac{\chi_N(\sigma)}{\sigma-c_0},
       \qquad \chi_N(z)=\mathcal T_N(z)+2.
 \tag{16}
\]
It is the literal diagonal path \(i=j=0\). Its values vanish at every complete spectral node, including the simple odd endpoint; at \(c_0\) its first derivative is nonzero. Applying the physical crossing functional gives
\[
 [c^d]H_{R^n,\mathrm L}=\kappa^n,
                         \qquad |\kappa^n|=1
 \tag{17}
\]
for every signed integer \(n\). The reflected statement holds for \([b^d]H_{R^n,\mathrm R}\). Thus the full charge and normal calculation does not kill every one-sided endpoint, even for arbitrarily long fixed powers. Equations (16)–(17) concern an actual local source coefficient. They make no claim that this endpoint can independently maximize an admissible whole marked coefficient.

## 4. Why the complete-channel first normal does not remove these terms

The first-normal theorem for original NC Morse graphs uses “NC” for *noncrossing Morse wiring*. Its edge coupons are the full-normal complete sectors \(R^eL_j\), factored through the stated ordinary objects with all source constants retained. This is different from the LEFT/RIGHT split of a general resolvent numerator.

In particular the projector just used is not itself a Casimir intertwiner. From (13),
\[
 [\Omega,P_-]z^{M+1}
   =s_{M+1}^2(x+y)z^M+s_{M+1}s_Mxy z^{M-1},
 \tag{18}
\]
which is nonzero when \(x+y>0\). Terms with negative index are absent. One therefore cannot replace a one-sided truncated coupon by an invariant ordinary vertex and invoke generic scalarity or its first-normal zero. The original full polynomial coupon is covariant; its source path partition need not preserve that property term by term.

Even where the complete-channel normal theorem applies, its equation is
\(Z=\nu_N^{-1}\partial_t(D_N(t)Z(t))|_{t=0}=Z(0)\), with the actual local source and exterior network currents kept. The zero \(D_N(0)=0\) alone gives no exponential bound on \(Z(0)\). The exposed six-port pruning theorem supplies an additional exact support vanishing for its closed complete-circle configuration; it is not a theorem deleting arbitrary semisimple one-sided currents.

## 5. Exact charge marks versus a primitive peripheral interpretation

On a regular chamber, suppose a local residual exponential action is \(A_0(\delta)\), after removing the oscillatory mode in (4) but not its slow prefactor. Before grouping modes the two full branches are
\[
 A_{\pm}(\delta)=A_0(\delta)\pm\pi i\delta.
 \tag{19}
\]
The original longitude polarization is \(V=-4\pi i\delta\). If the *full* physical derivative is \(U_\pm=\partial_\delta A_\pm\), then the retained half twist gives \(U_{\pm,\epsilon}=U_\pm-\epsilon V/2\). The original integer-charge critical equation is
\[
 U_{\pm,\epsilon}+pV=-2\pi i\ell,
               \qquad n=\epsilon-2p.
 \tag{20}
\]
The reindexed half-charge equation is instead
\[
 U_{0,\epsilon}+pV=-2\pi ik,\qquad
 U_0=\partial_\delta A_0,\qquad k=\ell\pm\tfrac12.
 \tag{21}
\]
Equations (20) and (21) are the same derivative identity. The latter gives a trace-zero image for the primitive filling word only if \(U_0\), rather than \(U_\pm\), is independently proved to be the marked log of an actual globally sewn representation. Reindexing (6) does not prove this new adapter.

There is a simple obstruction to making that change in the same fixed boundary frame. Let \(A,B\) be an irreducible ordered pair of determinant-one matrices. If \(C\) and \(C_0\) both transport this pair to the same ordered output pair, then \(C_0^{-1}C\) centralizes both \(A\) and \(B\). Their common centralizer is scalar, so the two projective transports agree. A change of peripheral ratio by \(-1\), as in (19), is noncentral and cannot be made while retaining that tuple. A centralizer half-turn of \(BA\) is not a centralizer of the ordered pair in general. Removing it requires changed output flags or gluing data, and those changes must be checked around the whole original graph.

The existing regular signed-circle construction retains the omitted-half mode, the shared face-character repair, all ordered heads and the original mark. At a free real spectral critical point \(\partial_\delta\operatorname{Re}A_0=0\), where the remaining residual action and its spectral derivative are real, it gives \(U_\pm=\pm\pi i\). Its actual untwisted auxiliary meridian therefore has trace squared zero. With the retained half twist the fixed word \(m_\epsilon^2\lambda^\epsilon\) is killed projectively, with its recorded central sign. The already proved marked peripheral-volume gap applies once this is a globally sewn actual representation whose canonical volume equals the original sharp action.

This last conclusion is not new from the charge grouping; it is the established conditional regular spectral argument. Formula (11) identifies exactly how its half-integer mark appears in the original finite period. It does not erase the global face-character condition. At a competing positive-value non-CROSS sharp maximum, the existing MAIN-cycle theorem supplies an odd character cycle, so that particular real coherent construction is unavailable there. A general complex saddle may have further phases that compensate the cycle; neither the real odd-cycle test nor (11) constructs or excludes it.

## 6. The reduced remaining problem

The new exact reduction leaves three specific routes, none supplied by normality alone.

First, one can estimate the coherent semisimple blocks (14) after the original shared coefficient extraction. Their eigenvalues have unit modulus, but the finite diagonalizing matrices may have exponential conditioning; the written proof must retain the original face-dependent norm or prove cancellation of that conditioning after sewing. Bounding separate spectral rank-one projectors would lose that information.

Second, a complex source saddle construction could retain all half-charge branches of (11), solve the original shared phase equations, and identify the original primitive group and canonical regulator. For an upper bound it must cover every contributing saddle and all boundary currents, including protected flat caps. It cannot infer an actual orbifold from (21) without an adapter for its residual log.

Third, one can use the proved regular-window phase exclusion quantitatively. It supplies a strict loss relative to a positive window envelope at every mismatched port. To obtain the desired absolute geometric bound, that loss must exceed the envelope's excess over the complete action. The odd MAIN-cycle theorem supplies inconsistency, not the required numerical comparison. The explicit flat-cap polynomial shows that even a fixed phase mismatch can leave only polynomial cancellation at an endpoint; no uniform exponential window theorem extends there by the sign table alone.

Consequently this calculation neither proves nor disproves a full undeformed simple-sphere volume theorem. It gives an exact all-parity change of Fourier lattice, a semisimple finite-block realization, and a fixed-frame obstruction to replacing its actual peripheral marks by half-cone marks without further geometry. Every statement concerns the original source; no sample knot or numerical saddle is used.

## Source references

The authoritative source for this calculation is publication commit `bb6d98a0e523dc0ee622398c4d10d439ff9af57b`. The formulas used above are in `research_original_one_sided_four_state_transfer.md` §§1–3, `actual_homogeneous_casimir_face_source.md` §§1–4, `actual_cross_cofactor_factorization.md` §§1–3, `actual_spectral_total_derivative_source.md`, and `actual_balanced_terminal_fan_volume.md` §§5,7–9. The ordinary normal and its scope are in `actual_nc_morse_graph_first_normal_source_reduction.md` §§1–6 and `actual_exposed_six_port_complete_circle_pruning.md`. The geometric qualifications use `research_spectral_face_sign_cocycle.md`, `research_stationary_noncross_main_cycle_obstruction.md`, `research_regular_signed_spectral_group_sewing.md`, `research_critical_circle_fan_fundamental_chain.md`, and `general_representation_volume_peripheral_gap.md`. Regular switching and the endpoint limitation are in `research_regular_spectral_window_phase_exclusion.md` and `research_flat_cap_no_local_exponential_angular_gap.md`.
