# The whole unselected plateau for every fixed mixed open word

Research theorem, 5 November 2026. Both the first-cap and terminal-four
coupled authors and their complete 320-bit saved replays have passed.
This deduction uses those completed finite-source comparisons and
the existing ordinary source theorems. No new numerical execution
is used here.

Every fixed open word of length at least two in types three and four
has its original nonzero
Gaussian asymptotic on the **entire retained unselected plateau**,
with either terminal type. The exact leading power is \(N^{-3/2}\).
This is a contour-sector theorem. Other retained Fourier alternatives
and nonplateau regions remain outside its conclusion.

## 1. Completed comparisons on the actual reference sets

The two complete author records are:

| Factor | Complete author | SHA256 |
|---|---|---|
| First cap | [coupled first-cap author](../repro/results/research-mixed-first-cap-coupled-plateau-attempt01.json), all 21,032 jobs | 1e7ecb710244d417de75d794688e8786153fa82355b3d73b6811621130e1c54c |
| Terminal four | [coupled terminal author](../repro/results/research-mixed-terminal-four-source-stage4-attempt01.json), all 40,131 jobs | e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3 |

The first-cap
[320-bit saved replay](../repro/results/research-mixed-first-cap-coupled-plateau-replay.json),
SHA256
d1cc89d4ff8c249f2b4bc4b72e79842ca6151450518d99f00f28498d3edd912e,
has passed all 21,032 jobs, including every inherited source leaf
and every coupled exclusion, without proposals or refinement.

The terminal-four
[320-bit saved replay](../repro/results/research-mixed-terminal-four-source-replay.json),
SHA256
3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79,
has passed all 40,131 jobs and binds the displayed terminal author
hash. It rechecks 82,806 source leaves under their original rules
and both saved length-case reasons at all 253 coupled exclusions.
Both replay records report no proposals or refinements and verify
all final input bindings.

The two source conclusions are used on the necessary actual-reference
sets of the [cap continuation](research_mixed_first_cap_coupled_plateau_certificate.md)
and [terminal continuation](research_mixed_terminal_four_coupled_source_continuation.md).
These sets contain every required actual reference at every fixed
length \(m\ge2\). For a four/four adjacent pair, they use
the oriented real bound and the union of:

* the two-endpoint fixed-point condition when \(m=2\);
* the necessary adjacent ordinary-block inverse conditions when
  \(m\ge3\), including the other attached endpoint at \(m=3\).

Both cases must be excluded before a coupled box is discarded.
The filter acts on the original reference, never on an independently
moving integration target. It neither inserts private legs into
ordinary input domains nor asserts that every feasible auxiliary
point is realized by a word.

Accordingly the source proofs give their comparisons at every actual
reference. This replaces the stronger auxiliary-domain hypothesis in
[the earlier first-cap assembly](research_mixed_terminal_three_full_plateau.md)
and Condition C of
[whole terminal-four completion](research_mixed_terminal_four_full_completion.md).
The latter proof uses its twenty-one comparisons at the actual
reference and thus applies with this replacement. It does not require
their validity at the unused independent inputs discarded by the
necessary filter. The old larger-domain first-cap claim was false;
it is not recovered here.

For each fixed actual reference, the finitely many closed coupled
exclusion boxes avoid that point. The strict source margins on the
remaining leaves and the original holomorphic interpolants therefore
retain the small incoming-variable and ordinary-color neighborhoods
used by the local packets. This does not provide a packet or moving
critical point at every independent plateau target.

## 2. Literal contraction and the complete-source upper planes

Fix a word \(n_j=3+\epsilon_j\), \(1\le j\le m\),
with \(m\ge2\), and put
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 \epsilon=\epsilon_m,\qquad
 X_j=e^{-2\pi iz_j},\qquad r_j=a_j+ic_j.
 \tag{1}
\]
The \(r_j\) are its actual retained critical legs. Every
\(a_j\) lies strictly inside \(P=[.22,.45]\); every retained
type-four height is negative. The actual ordinary and attached
image bounds, rather than narrower cyclic height bounds, are used.

Equation (13) of
[the exact terminal contraction](research_mixed_reversed_cap_assembly.md)
has scalar \(\kappa_N^{m+k_4}N^{m+k_4-1}\). Its retained
unselected integrand is exactly
\[
 \mathscr J_N(\mathbf z;w_L,w_R)=
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
 \tag{2}
\]
Every terminal finite row, its entire diagonal weight, its selected
alternative and its ordinary-color dependence have already been
summed exactly inside \(\mathcal V_\epsilon\). For the
remaining coordinates, (2) selects the factor 1 from
\(1+X_j^{-N}\). It does not select a term from inside
\(\mathcal V_\epsilon\). For \(m=2\), the conditional
product is empty and both endpoint factors share one coordinate.

The sector is
\[
             z_j=x_j+ic_j,\qquad \mathbf x\in P^h.
 \tag{3}
\]
All original height cutoff factors are one on this plateau, so its
literal contour heights are the fixed reference heights in (3),
independent of the other real coordinates.

Write \(g(z)=J(z)+i\pi z(1-z)/2\), and allocate one half of
each retained type-four diagonal weight to either incidence:
\[
 L(z)=\mathcal T_{\epsilon_1}(z,-2)-\epsilon_1g(z)/2,
 \qquad
 \Pi(z)=\mathcal P_{\epsilon}(z)-\epsilon_hg(z)/2.
 \tag{4}
\]
Let \(\phi_j\) be the original allocated ordinary phase, with
left flag \(\epsilon_{j-1}\) and own flag \(\epsilon_j\).
The [completed first-cap plateau theorem](research_mixed_first_cap_plateau_completion.md),
the [ordinary source planes](research_mixed_three_row_source_assembly.md),
and the whole [type-three](research_mixed_terminal_three_full_completion.md)
or [type-four](research_mixed_terminal_four_full_completion.md)
terminal theorem give, for any prescribed positive tolerances,
their respective upper rates
\[
 \begin{split}
 B_U(x_1)&=\Re L(r_1)+\Re L'(r_1)d_1-\kappa_*d_1^2,\\
 B_j(x_{j-1},x_j)&=\Re\phi_j(r_{j-1},r_j)
    +\Re\nabla\phi_j(r_{j-1},r_j)\cdot(d_{j-1},d_j)
                       -\kappa_*(d_{j-1}^2+d_j^2),\\
 B_V(x_h)&=\Re\Pi(r_h)+\Re\Pi'(r_h)d_h-\kappa_*d_h^2,
 \qquad d_j=x_j-a_j,\quad\kappa_*=1/2500000.
 \end{split}
 \tag{5}
\]
These bound the literal complete factors multiplied by their actual
unselected Fourier halfweights. For every positive tolerance, the
bounds have a polynomial prefactor and a sufficiently small fixed
ordinary-color disk. They retain all finite rows, revived products,
physical endpoints, contour joins and aliases, at both level parities.
There is no division by a Fourier polynomial, including at a zero.

The two halves at a retained coordinate multiply to exactly its
integer diagonal power in (2). At \(h=1\), the first cap and
terminal transform supply the two halves directly. In particular
the terminal own flag \(\epsilon_m\) belongs inside
\(\mathcal V_{\epsilon_m}\); it is not an additional retained
diagonal exponent.

## 3. Uniform suppression away from the original critical point

Near the actual reference define the original reduced action
\[
 \Phi(\mathbf z)=L(z_1)+
     \sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h).
 \tag{6}
\]
It is the original open action after eliminating the variables
hidden in (2), with its original logarithmic lifts and additive
constant. Hence
\[
 \Phi(\mathbf r)=\mathcal F_m(z_*),\qquad
 \nabla\Phi(\mathbf r)=0,\qquad
 M_{\mathrm{open}}=\Re\mathcal F_m(z_*).
 \tag{7}
\]
No merely exponentiated critical equation or unknown phase constant
is used in this equality.

**Theorem 1.** For every fixed mixed word above and
every \(\tau>0\), there are fixed small ordinary-color disks
and polynomial prefactors such that, uniformly on (3),
\[
 |\mathscr J_N|
 \le C_{m,\tau}N^{A_{m,\tau}}
       \exp N\left\{M_{\mathrm{open}}+\tau
                   -2\kappa_*\sum_{j=1}^{h}(x_j-a_j)^2\right\}.
 \tag{8}
\]
This holds for every sufficiently large integer \(N\), of either
parity. Fixed ordinary-color derivatives satisfy the same upper
rate, with their corresponding polynomial prefactors.

*Proof.* Multiply the complete-source bounds in (5), retaining
their exact halfweights. Equation (7) adds the constant terms and
cancels every linear term. The quadratic losses satisfy
\[
 \kappa_*d_1^2+
 \kappa_*\sum_{j=2}^{h}(d_{j-1}^2+d_j^2)+
 \kappa_*d_h^2=2\kappa_*\sum_{j=1}^{h}d_j^2.
 \tag{9}
\]
The identity includes \(h=1\), with an empty sum. For the fixed
word choose the individual source tolerances to sum to \(\tau\).
No fixed positive error is charged at each edge. The threshold,
color disks and polynomial prefactors may depend on this word.
Cauchy's formula on smaller color disks gives the derivative upper
bounds. \(\square\)

For every fixed \(\eta>0\), the part of (3) with
\(\sum_jd_j^2\ge\eta^2\) is exponentially suppressed by
\(\kappa_*\eta^2\), after choosing the total tolerance and
then \(N\). The exact external scalar is polynomial in modulus
and does not alter this separation.

## 4. The nonzero coefficient and the original power of \(N\)

The original local packets give
\[
 \begin{split}
 U_{\epsilon_1,N}
   &=N^{-1-\epsilon_1/2}b_U
                   e^{N\mathcal T_{\epsilon_1}}(1+O(N^{-1})),\\
 C_{\epsilon_j,N}
   &=N^{-(1+\epsilon_j)/2}b_{C,j}
                   e^{N\varphi_j}(1+O(N^{-1})),\\
 \mathcal V_{\epsilon,N}
   &=N^{-1-\epsilon}b_{V,\epsilon}
                   e^{N\mathcal P_\epsilon}(1+O(N^{-1})),\\
 d_N(e^{-2\pi iz})
   &=N^{-1/2}a_0(z)^{-1}e^{-Ng(z)}(1+O(N^{-1})),\\
 a_0(z)&=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}.
 \end{split}
 \tag{10}
\]
The bare conditional phase is \(\varphi_j\); adding its
two diagonal halves gives \(\phi_j\). All leading symbols
in (10) are nonzero on their original branches. The first-cap
packet and ordinary local packets were already established; the
whole-terminal proofs supply the local incoming-variable and color
germs as well as pointwise asymptotics. Their strict bare discarded
current gaps persist locally, so these germs are not inferred from
a value at one incoming coordinate.

At complete colors the terminal coefficient is, for either type,
\[
 b_{V,\epsilon}(r_h,-2)=
       \frac{2\pi A_\epsilon^{\mathrm{red}}}
            {\sqrt{\det H_{\epsilon}^{\mathrm{red}}}}.
 \tag{11}
\]
For \(\epsilon=0\), these are the original double-source
amplitude and its two-dimensional critical Hessian. For
\(\epsilon=1\), they are the reduced amplitude \(\widehat A_1\)
and \(H_{2,*}\) of whole-terminal-four completion, equations
(6)--(8). In the latter case \(\widehat A_1\) already contains
the original inner endpoint Gaussian; its Schur determinant
identity agrees with the unreduced three-dimensional coefficient.
Thus no terminal \(2\pi\), square root or inner Gaussian is
inserted again below.

Set
\[
 \begin{split}
 b(\mathbf r)&=b_U(r_1,-2)b_{V,\epsilon}(r_h,-2)
       \prod_{j=2}^{h}b_{C,j}(r_{j-1},r_j)
       \prod_{j=1}^{h}a_0(r_j)^{-\epsilon_j},\\
 H_{\mathrm{eff}}&=-\Phi''(\mathbf r),\qquad
 A_m=\frac{(2\pi)^{h/2}b(\mathbf r)}
                            {\sqrt{\det H_{\mathrm{eff}}}}.
 \end{split}
 \tag{12}
\]
The [original open Hessian theorem](research_mixed_open_word_hessian.md)
and the complex Schur identity give
\(\Re H_{\mathrm{eff}}\succ0\).
All Gaussian roots are the accretive roots with the original
contour orientation. Hence \(A_m\ne0\).

Let \(\mathcal Z_N^P\) denote the exact scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\) times the integral of
(2) over (3), with the inherited angular orientation.
In increasing real coordinates its measure is
\(dx_1\cdots dx_h\): the sign in
\(dX_j/(2\pi iX_j)=-dz_j\) is canceled by reversing the
clockwise \(X_j=e^{-2\pi iz_j}\) parametrization of each
positively oriented circle.

**Theorem 2.** For every fixed word of length
\(m\ge2\), with either terminal type,
\[
 \mathcal Z_N^P(-2,-2)=
       \kappa_N^{m+k_4}N^{-3/2}A_m
       e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
                    \qquad A_m\ne0.
 \tag{13}
\]
Both level parities are included.

*Proof.* A fixed small box around the real reference lies inside
\(P^h\). The original packets give its nonzero accretive Gaussian
with phase (6) and coefficient (12). Theorem 1 makes the rest of
the entire plateau exponentially smaller. Extending this local
integral to (3) therefore preserves its coefficient and relative
\(O(N^{-1})\) error.

The literal contraction, all local source powers and the remaining
\(h\)-variable Gaussian give exactly
\[
 \begin{split}
 &(m+k_4-1)-(1+\epsilon_1/2)
  -\frac{m-2+k_4-\epsilon_1-\epsilon_m}{2}\\
 &\hspace{12mm}-(1+\epsilon_m)
  -\frac{k_4-\epsilon_m}{2}
  -\frac{m-1}{2}
 =-\frac32 .
 \end{split}
 \tag{14}
\]
The terminal factor contributes \(N^{-1-\epsilon_m}\);
the retained diagonal factors involve only
\(k_4-\epsilon_m\). This is the distinction needed for
a type-four terminal vertex. At \(m=2\), the ordinary-factor
term is zero and the same identity holds. The only Gaussian
constant not already included in (10) is the one in (12).
\(\square\)

Small ordinary-color perturbations continue the critical point,
action and coefficient holomorphically. A local contour deformation
follows that germ, and the strict plateau-complement gap persists
on smaller fixed color disks. For fixed ordinary derivative orders
\(p,q\ge0\), Cauchy's formula gives the leading power
\(N^{p+q-3/2}\) and nonzero multiplier
\[
       \left(-\frac{\tan\pi u_L}{4\pi}\right)^p
       \left(-\frac{\tan\pi u_R}{4\pi}\right)^q.
 \tag{15}
\]
Signed jets retain their signs from the original torus identity.
The integrated source (2) uses integer diagonal powers; no
holomorphic halfpower of a finite Fourier polynomial is required.

The [geometric/source identification](research_mixed_geometric_source_identification.md)
gives \(2\pi\Re\mathcal F_m(z_*)=V_{\mathrm{cells}}\), with
the original marking and normalization. Since
\(|\kappa_N|=1\), equation (13) consequently gives the
volume rate \(V_{\mathrm{cells}}\) for this entire plateau
sector, and likewise for its fixed ordinary jets.

## 5. Completion of the entire type-four terminal factor

The completed terminal comparisons also discharge the entire
factor theorem used in (10), not merely its contribution to the
plateau integral.

**Corollary 3.** Let \(a_*\) be the actual incoming nonprivate
leg of a type-four terminal vertex in any fixed word of length
\(m\ge2\). The whole literal polynomial satisfies
\[
 \mathcal V_{1,N}(-2,e^{-2\pi ia_*})
   =\frac{2\pi}{N^2}
       \frac{\widehat A_1(a_*,e_*,t_*)}
            {\sqrt{\det H_{2,*}}}
       e^{N\mathcal P_1(a_*)}(1+O(N^{-1})).
 \tag{16}
\]
Its coefficient is nonzero, with the original phase, branches and
orientation. For every fixed ordinary derivative order \(j\ge0\),
\[
 \left.\partial_w^j\mathcal V_{1,N}(w,e^{-2\pi ia_*})
                                                     \right|_{w=-2}
   =2\pi N^{j-2}
       \frac{\widehat A_1(a_*,e_*,t_*)}
            {\sqrt{\det H_{2,*}}}
       \left(-\frac{\tan\pi u_*}{4\pi}\right)^j
       e^{N\mathcal P_1(a_*)}(1+O(N^{-1})).
 \tag{17}
\]
These are holomorphic local packets on fixed smaller ordinary-color
disks, through both integer-level parities.

*Proof.* The completed twenty-one comparisons hold at every such
actual reference by Section 1. The exact source partition and
Gaussian proof in
[whole terminal-four completion](research_mixed_terminal_four_full_completion.md),
Sections 2--3, therefore apply with Condition C restricted to this
necessary actual-reference set. The entire end-index sector is removed
before any inner restriction; the private tails retain the complete
inner endpoint polynomial; the upper physical triangle includes
the even half row. Thus no finite row, revived term or alias is
omitted. The proof there yields exactly (16)--(17), with its one
combined source/color tolerance.

Its normalization is \(N^2N^{-3}(2\pi/N)=2\pi N^{-2}\)
for the reduced double source. The identity
\(\det H_{3,*}=h_{u,*}\det H_{2,*}\) and the original inner
Gaussian already contained in \(\widehat A_1\) match the
unreduced triple source. This is the same nonzero coefficient used
in (11); it is not an additional factor in Theorem 2. \(\square\)

The allocated full independent-plateau upper bound for this whole
terminal factor is likewise unconditional: it is the terminal
entry of (5), with any prescribed tolerance and ordinary-color
derivatives. It still concerns the incoming reference height and
the unselected neighboring halfweight.

## 6. Remaining scope

This extends the previously conditional ending-three plateau
assembly to both terminal types and removes the remaining
first-coordinate locality on the unselected plateau. It includes
lengths two and three with their literal incidence counts and
normalizations, without a word-by-word numerical calculation.

The exact open source also contains selected alternatives at the
retained coordinates and regions outside the plateau where contour
heights change. Their possible contribution cannot be discarded by
(8). A nonzero coefficient of \(\mathcal Z_N^P\) therefore
does not yet identify the leading coefficient of the entire ordinary
closure. One-vertex words, general selected and nonplateau sectors,
branching, and arbitrary short partial fillings retain their separate
proof obligations. No cofinite per-template theorem is inferred
from this sector assembly alone.
