# What the strict Conway proof controls before a main-meridian deformation

Private analytical audit, 31 October 2026. No repository files are changed by this report.

The question is whether the existing strict-tree proof supplies the bounded total variation required by §2 of [the paired-factor profile theorem](/Users/sasha/volume-conjecture/notes/actual_paired_factor_meridian_profile.md), for the actual deformation of the main meridian. The answer has three parts.

* A bounded condition number can be proved for the exact finite **complete-color augmented wire sum**, after its local half-twist coefficients have already been contracted.
* The exact real Fourier-charge representation of the filled scalar does **not** have finite total variation before pairing and deforming its endpoint currents. The selected deformed local cycles do have a bounded condition number, by a Gaussian estimate proved below.
* Neither statement supplies an insertion-compatible representation of the actual main-meridian deformation of an arbitrary strict filled tree. That is the first missing source assertion. A global regrouped-cycle bound at the single complete scalar is not claimed here as an already established main-meridian theorem.

The word “complete” below refers to the main color \(V_{N-1}\), unless an auxiliary color is explicitly specified. All trees, signs, and sufficiently long filling integers are fixed before \(N\) grows.

## 1. Which variables the available theorem actually varies

Write \(d=N-1\), \(q_N=e^{\pi i/N}\), and \(Q_N=q_N^2\). The filled knot has reduced scalar \(K_N(\mathbf p)\). Before filling, let
\[
 A_N(\mathbf h)
   =Z_N^\epsilon(N-h_1,\ldots,N-h_b)
\tag{1}
\]

be its exact augmented source. The \(h_i\) are auxiliary crossing-circle color deficits. The main strands in (1) still have complete color \(V_d\). The strict-tree theorem gives a finite holomorphic corridor packet \(C_N(\chi)\), where \(\chi_i=h_i/N\), and a global comparison

\[
\begin{aligned}
 A_N(\mathbf h)&=\eta_N C_N(\mathbf h/N)
                  +O\!\left(N^C e^{N(F_0-\gamma)}\right),\\
 C_N(\chi)&=N^{3/2}a(\chi)e^{N\Phi(\chi)}
                  (1+O(N^{-1})).
\end{aligned}
\tag{2}
\]

The first line is an assertion on the physical color grid; the second is uniform on a specified fixed complex neighborhood. Here \(a(0)\ne0\), \(\Phi(0)=F_0\), and the color Hessian has negative-definite real part. These are equations (25)–(26) of [the all-strict theorem](/Users/sasha/volume-conjecture/notes/actual_conway_all_strict_tree_long_twist_volume.md). Its §§3–5 separately establish the global whole-source color losses.

The main-meridian question instead varies

\[
 M=e^{z/(2N)}=q_N^s,\qquad z=2\pi i s,
 \qquad \alpha=d+s,
\tag{3}
\]

with \(z\) in a fixed complex disk. Neither \(\chi\) in (2), nor the primitive wire variables used to construct \(C_N\), is \(s\). The old marked white-face maps keep the main meridian parabolic throughout their auxiliary-color deformation. Consequently the uniformity in (2) is not main-meridian uniformity.

## 2. A bounded condition number that really follows: the complete augmented wire sum

Consider a fixed strict tree and a sign pattern covered by the general core theorem: any strict knot pattern, in particular; for two leaves the excluded both-odd pattern has two main components. At auxiliary colors all equal to \(N\), the alias term is exactly zero at each leaf:

\[
 h_N^\epsilon=C_N^\epsilon+(-1)^N h_0^\epsilon=C_N^\epsilon.
\tag{4}
\]

Use the exact primitive wire compiler, with its forced coefficient-one closing gate removed and its complementary wire relation retained. It gives a finite sum

\[
 \eta_N^{-1} A_N(\mathbf0)=\sum_{k\in\Lambda_N}w_{N,k}.
\tag{5}
\]

The weight \(w_{N,k}\) is a product of the **exact contracted** complete leaf coefficients and the exact positive Newton multiplication coefficients. It does not mean an expansion of each signed leaf coefficient into all of its internal recurrence or crossing paths.

**Proposition.** For this finite sum there is a constant \(C\), independent of \(N\), such that

\[
 \sum_{k\in\Lambda_N}|w_{N,k}|
       \le C|A_N(\mathbf0)|.
\tag{6}
\]

For every fixed neighborhood \(B\) of its complete maximizing state, after making \(B\) small enough to lie in the strict polytope, there are \(C_B,c_B>0\) with

\[
 \sum_{k/N\notin B}|w_{N,k}|
       \le C_B e^{-c_BN}|A_N(\mathbf0)|.
\tag{7}
\]

Here the constants may depend on the fixed tree and its sign pattern.

**Proof.** The exact complete action is

\[
 \mathcal A(y)=\sum_i g(a_i(y))+
               \sum_{\text{retained gates}}m(x_v(y),y_v(y),z_v(y)).
\tag{8}
\]

It has a unique strict maximum \(F_0\) and a negative-definite Hessian on the primitive \(K=2H-3\) wire space. Every complete leaf index is at least \(1/4\) and less than \(1/2\). These assertions and the closed outside-window absolute bound are proved in §§2–5 of [the general core theorem](/Users/sasha/volume-conjecture/notes/actual_conway_general_core_packet_and_gap.md).

Inside a fixed small strict window, the high-index and quarter-index local source theorems give an exact leaf coefficient bounded by
\(C N^{1/2}e^{Ng(a_i)}\). This is stronger than invoking a nonzero scalar saddle. It follows from the uniform local coefficient interpolation and from the exact identity \(f_\epsilon(x,0)=g(x)\), with a bounded nonzero complete amplitude. See (9), (11), and (17) of [the signed color packet](/Users/sasha/volume-conjecture/notes/actual_odd_conway_complex_color_packet.md) and the corresponding extension in [the quarter-index packet](/Users/sasha/volume-conjecture/notes/actual_conway_quarter_index_color_packet.md). Every strict gate has its local bound \(C N^{-3/2}e^{Nm}\). The fixed integer offsets only multiply the local density by a bounded factor on this compact window. Thus

\[
 |w_{N,k}|
 \le C N^{3-H}
       e^{NF_0-cN|k/N-y_*|^2}.
\tag{9}
\]

The primitive lattice Gaussian satisfies

\[
 \sum_{k\in\mathbb Z^K}e^{-c|k-Ny_*|^2/N}
       \le C N^{K/2}.
\tag{10}
\]

The shift \(Ny_*\) is arbitrary, so this bound has no divisibility or parity restriction. Equations (9)–(10) give an absolute window mass at most
\[
 C N^{3-H+K/2}e^{NF_0}=C N^{3/2}e^{NF_0}.
\]
Outside the window, the closed global core coefficient estimate and the strict compact action gap give an absolute sum \(N^C e^{N(F_0-\gamma)}\), as explicitly stated in equation (6) of the general core theorem. That statement is about absolute wire weights, not just their signed contraction.

Finally the exact packet gives
\[
 |A_N(\mathbf0)|=N^{3/2}|a(0)|e^{NF_0}(1+O(N^{-1})),
 \qquad |a(0)|>0.
\tag{11}
\]
Combining the explicit absolute bounds with this lower bound proves (6) and (7). The scalar lower bound is used only after the absolute wire mass has been estimated. \(\square\)

This proposition is a genuine finite-source conditioning result for arbitrary fixed strict trees. Its limit is also precise: the known local half-twist contractions are already inside \(w_{N,k}\). An insertion depending on their internal summation variable cannot be moved outside those contractions merely because (6) holds.

Moreover, \(A_N(\mathbf0)\) is the complete augmented source, not the fully filled knot scalar \(K_N(\mathbf p)\). The paired-factor theorem cannot use (6) with the latter denominator without another exact transport.

## 3. Filling introduces a second, essential cancellation

At complete main color, [the general source filling transfer](/Users/sasha/volume-conjecture/notes/general_original_source_long_filling_transfer.md), equation (1), is the exact finite identity

\[
 K_N(\mathbf p)=
 \chi_N\kappa^{-2\sum_i p_i}
 \sum_{\mathbf j}
   \left(\prod_i\beta_{j_i-1}^{(-p_i)}\right)
   A_N(\mathbf N-\mathbf j).
\tag{12}
\]

Each circle-basis coefficient family has mass at most \(2N(1+|p_i|)\). This is polynomial for fixed slopes, but gives only the augmented exponential envelope \(e^{NF_0}\) when combined with the source bound. The filled critical exponent is
\[
 F_{\mathbf p}=\Re T_{\mathbf1}(z_*),
\tag{13}
\]
not \(F_0\). The analytic filling action has a negative quadratic real correction for nonzero reciprocal slopes. Therefore an \(e^{NF_0}\) upper bound, even with no polynomial loss, cannot be read as \(O(|K_N(\mathbf p)|)\). The circle-basis note itself makes this distinction in its §4.

There is a more exact obstruction to calling the raw Fourier representation a bounded-variation cycle. In one coordinate its exact form, with harmless unit constants suppressed, is

\[
 \sum_{m\ne0}\sigma_{m,N}\,m
 \int_{-1/2}^{1/2}
 e^{2\pi iN(Px^2-mx)}
 \sinh(2\pi i x)\,\mathcal F_N(x)\,dx,
 \qquad |\sigma_{m,N}|=1.
\tag{14}
\]

Here \(P\) is a fixed real integer and \(\mathcal F_N\) is the exact finite Fourier polynomial of the even color corridor. Equation (14) is equation (11) of [the full-normal endpoint theorem](/Users/sasha/volume-conjecture/notes/actual_filling_source_fourier_endpoint_gap.md).

**Lemma.** If \(\mathcal F_N\) is not identically zero, the disjoint union of the real cycles in (14), with their displayed densities, has infinite total variation for each \(N\).

Indeed, putting
\[
 c_N=\int_{-1/2}^{1/2}
       |\sinh(2\pi i x)\mathcal F_N(x)|\,dx,
\]
analyticity and nonvanishing give \(c_N>0\). The absolute integral on its \(m\)-th real cycle is \(|m|c_N\), since both exponential phases have modulus one. Hence their sum is infinite. This does not contradict absolute convergence of the **integrated charge coefficients**: cancellation inside each oscillatory integral is what makes those coefficients summable.

The published proof repairs this representation by contour deformation and an exact pairing of endpoint currents. If
\[
 U_N(x)=e^{2\pi iPNx^2}\sinh(2\pi i x)\mathcal F_N(x),
\]
then the paired vertical density is
\[
 V_N(v)=U_N(1/2-iv)-U_N(-1/2-iv).
\tag{15}
\]
The exact integer Fourier periodicity and the two sinh zeros give
\(V_N(0)=V_N'(0)=0\). The source bounds then give
\[
 |V_N(v)|\le
 N^C v^2 e^{N(F_0-\gamma)+2\pi|P|Nv}.
\tag{16}
\]
Consequently the total variation of this **paired** vertical contribution is bounded by
\[
 |m|\int_0^\sigma e^{-2\pi|m|Nv}|V_N(v)|\,dv
 \le
 \frac{N^C |m|}{N^3(|m|-|P|)^3}
 e^{N(F_0-\gamma)}.
\tag{17}
\]
It is summable over the high charges. The horizontal pieces have a geometric tail. In several variables, equation (14a) of the endpoint theorem removes one tail at a time while all spectator chirps remain on real grids or real finite integrals. This prevents a new exponential cost from another filling slope.

Thus a summable deformed remainder exists at the complete scalar after the indicated pairings. Equation (17) does not hold for either separate vertical current, nor for an arbitrary multiplier inserted differently on the two sides.

## 4. The selected local filled cycle is well conditioned

There is a second proved bounded-variation statement, this time for the selected local part of the filled contour. It follows from the full complex packet, not merely from the existence of a nonzero saddle.

Let \(b\) auxiliary circles be filled. On its fixed central neighborhood, the exact finite color Fourier polynomial satisfies

\[
 \mathcal F_N(\zeta)=
 N^{\mu+b/2}B(\zeta)e^{N\Psi(\zeta)}(1+O(N^{-1})),
 \qquad \mu=3/2.
\tag{18}
\]

This is a uniform holomorphic statement about the exact finite Fourier sum; its derivation uses the original cotangent rectangles and their exponentially bounded currents. For a minimal charge \(m_i=\pm1\), take the translated real contour through its filled critical point \(\zeta_m\). On a fixed small neighborhood of that point,

\[
 \Re\{T_m(\zeta_m+u)-T_m(\zeta_m)\}
       \le-c|u|^2,\qquad u\in\mathbb R^b.
\tag{19}
\]

The real part of the translated Hessian is negative definite and the amplitude, including \(\prod_i m_i\sinh(2\pi i\zeta_i)\), is bounded and nonzero at the critical point. Hence the total variation of the exact density on this local contour is at most

\[
 C N^{\mu+b/2}e^{NF_{\mathbf p}}
       \int_{\mathbb R^b}e^{-cN|u|^2}\,du
 \le C N^\mu e^{NF_{\mathbf p}}.
\tag{20}
\]

The fixed slope tuple is important: its nonzero sinh factors and Gaussian constants may depend on those slopes. The asymptotic of the same integral has a nonzero coefficient of \(N^\mu e^{NT_m(\zeta_m)}\). The minimal sign choices add by exact reflection; they do not cancel. The full-source filling theorem therefore also implies that (20) is \(O(|K_N(\mathbf p)|)\), after restoring the same common normalization on both sides.

This proves bounded variation for the selected local cycles. It does **not** identify the actual main-meridian insertion on these cycles.

For the remaining global pieces, the proof provides absolute estimates for the paired high-charge currents and many contour complements, and estimates on grouped scalar source errors. It is reasonable to reconstruct a complete regrouped cycle from these steps. This report has not promoted that reconstruction to an insertion-compatible global measure theorem. In particular, replacing a residual scalar by a single atom with its already-small value would provide no information about an independently deformed residual. Such a packaging is not a solution of the signed-sum criterion.

## 5. The earliest new source identity is before the old contour motion

The complete-color source compiler uses one algebra
\[
 \mathcal H_N=\mathbb C[\omega]/(\mathcal T_N(\omega)+2),
 \quad T e_r=e_{d-r},
 \quad \phi(e_re_t)=\mathbf1_{r+t=d}.
\tag{21}
\]
Its circle coefficients, normal terms, core/alias split, and filling coefficients are compiled in that algebra. These identities retain the full double-node information at \(M=1\).

Under (3), an oriented main strand has highest-root parameter
\[
 x_+=-q_N^{-1}M,
 \qquad x_-=-q_N^{-1}M^{-1}
\tag{22}
\]
on its dual. Equal-color tensor sectors have the moving Casimir relation
\[
 \mathcal T_N(\omega)+M^{2N}+M^{-2N}=0,
\tag{23}
\]
whereas opposite-color sectors retain \(\mathcal T_N(\omega)+2=0\). The local turn is consequently a typed linear map between different intertwiner spaces, with the actual duality, braiding carrier and pivot retained. It is not the same scalar reversal in (21) on every sector.

The exact local constructions now available privately make this distinction constructive: the physical currying map is regular on bounded microscopic disks, while a same-color polynomial interpolation chart can become singular at the first ordinary resonance. Neither fact is a spectral norm estimate for a whole strict tree. The old complete-source positive multiplication, coefficient reversal and Fourier endpoint identities cannot therefore simply be reused with \(M\) substituted in their nodes.

This is the earliest missing equality: an exact oriented compiler for \(f_N(e^{z/N})\), valid as a whole holomorphic function on the prescribed \(z\)-disk, together with the map of that compiler to the **same** grouped variables and cycles used in §§2–4. Even a bounded physical matrix multiplier does not prove a bounded multiplier on those contracted coefficients or cycles.

In particular, the paired-product form
\[
 f_N(e^{z/N})=\sum_\sigma w_{N,\sigma}
               \prod_{\ell=1}^{m}P_{N,n_\ell(\sigma)}(z)
\tag{24}
\]
has not been supplied for arbitrary strict trees by the cited complete-source theorem. Nor is there an established equivalent of (24) on its deformed contours. The figure-eight whole-source elimination proves such an identity for that knot; its proof cannot be replaced by the strict-tree auxiliary-color packet.

## 6. A precise contour stability target

The following sufficient condition isolates what a useful next lemma would establish. It is not asserted for the general source.

Suppose there is an exact, main-meridian-uniform decomposition
\[
 f_N(e^{z/N})=\int_{\Gamma_N}
                  I_N(z,\xi)\,d\mu_N(\xi)+r_N(z),
 \qquad K_N=\int_{\Gamma_N}d\mu_N+r_N(0),
\tag{25}
\]
with every current and discrete residual specified independently of its unknown contraction. Assume
\[
 \|\mu_N\|_{\mathrm{TV}}\le C|K_N|,
 \qquad |r_N(z)|\le C_R e^{-cN}|K_N|
\tag{26}
\]
on each fixed \(z\)-disk, and a measurable bulk \(\Gamma_N^{\mathrm{bulk}}\) with exponentially small complementary variation. If, as whole holomorphic functions,
\[
 \sup_{\Gamma_N^{\mathrm{bulk}}}
 |I_N(z,\xi)-H_N(z)^m|\le C_R/N,
 \qquad \sup_{\Gamma_N}|I_N(z,\xi)|\le C_R,
\tag{27}
\]
then the signed-sum proof applies verbatim, giving
\(f_N(e^{z/N})/K_N=H_N(z)^m+O_R(N^{-1})\), with every fixed derivative. A condition number \(o(N)\), with corresponding tail control, suffices for convergence without the stated rate.

For the existing filling cycles, two concrete obligations cannot be omitted.

First, the bulk insertion must have a holomorphic continuation to the actual complex wire and Fourier contours. Bounds on its integer samples alone do not permit the old contour deformation. Exponential interpolation errors must be controlled before summation, including the shifted Newton and normal coefficients.

Second, the insertion must preserve the paired endpoint conditions. If the two deformed side densities no longer agree to first order at their common endpoint, (17) changes: a nonzero constant difference gives a nondecaying charge contribution after the Laplace integral, while a linear difference gives an \(m^{-1}\) bound. Neither is summable in total variation. The double zero is therefore an exact source-matching condition, not a consequence of a bounded multiplier or of the local saddle.

The most concrete available starting points are (6) for the complete augmented wire sum and (20) for the selected filled cycles. The next broad analytic work is to transport the **actual typed main-meridian source** to one of those representations, retaining its endpoint matching, and to bound the complementary deformed source before taking absolute values. The present strict-tree volume proof establishes the scalar volume limit; it does not by itself establish that transport or the general microscopic profile.

## Source coverage checked

This audit read the actual all-strict assembly §§1–8; the general core estimate §§1–6; the signed and quarter local coefficient packets; the complete crossing-circle and filling identity §§1–4; the general source filling transfer §§1–5; the full-normal Fourier endpoint theorem §§1–6, including its multiport telescoping formula; the local charge selection proof; and the decorated-character and root-character source interfaces. The conclusions above use their equations and contour bounds, rather than prior review labels. The private typed-turn and moving-Casimir calculations are mentioned only to identify the first unsupplied global adapter, not as a completed replacement for it.
