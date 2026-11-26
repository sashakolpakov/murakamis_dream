# The midpoint Fourier and normal pairing of the retained leaf interface

Private written proof, 16 November 2026.

The real interface in the weighted leaf construction is an exact
finite-frequency pairing with the original remaining source.
Its midpoint endpoints eliminate the boundary terms when the
derivative is transferred to that source. Both outer exterior
half-boundaries of the original construction remain.

The identity identifies a specific coherent estimate still needed.
A separate convex diagnostic shows why replacing that pairing by
its absolute real profile cannot supply a general parent-action
comparison. It makes no lower claim for the actual interface.

## 1. Exact interface and its midpoint transform

Use one fixed bulk window and all the conventions of the weighted
window theorem. In particular
\[
 u_j=j/N,\quad j_0\le j\le j_1,\quad
 a_N=(j_0-\tfrac12)/N,\quad b_N=(j_1+\tfrac12)/N,
 \quad \nu_N(x)=2\pi x+\pi/N.
 \tag{1}
\]
The actual leaf is \(F_N=T(R^nB_N)\), with its original microscopic
endpoint product, and \(\mathcal S_N\) is its fixed signed phase
weight. Write its normalized full physical jets as
\[
 a_j=e^{-N\mathcal S_N(u_j)}F_N(c_N(u_j)),\quad
 b_j=e^{-N\mathcal S_N(u_j)}
  [\partial_uF_N(c_N(u_j))
                 -N\mathcal S_N'(u_j)F_N(c_N(u_j))],
 \tag{2}
\]
where \(c_N(x)=2\cos\nu_N(x)\) and the derivative denotes the
ordinary composed derivative before evaluation. Their uniform bound is
\[
 |a_j|+|b_j|/N\le M_N,\qquad \log M_N=o(N),
 \tag{3}
\]
on larger fixed bounded microscopic parameter sets.

Keep the entire original spectator \(p_N\), including any receiving
crossing, other kernels, free boundary variables and remaining traces.
With \(f_N(x)=p_N(c_N(x))\), put
\[
 A_N(x)=e^{N\mathcal S_N(x)}\sin\nu_N(x)f_N(x),\qquad
 K_{j,N}(x)=\frac{\sin(2\pi N(x-u_j))}{x-u_j}.
 \tag{4}
\]
The apparent singularity of \(K_{j,N}\) is removable. None of
these quantities is replaced by its absolute value below.

Let \(\mathfrak I_N\) denote the unnormalized real interface in
the weighted theorem, namely the integral of
\(D_N(g_+-g_-)\) along \([a_N,b_N]\). Its explicit formula is
\[
 \mathfrak I_N
 =2i\sum_j\int_{a_N}^{b_N}
                  [-a_j K_{j,N}'(x)+b_jK_{j,N}(x)]A_N(x)\,dx .
 \tag{5}
\]
Indeed
\(-K_{j,N}'=(\sin(2\pi Nd)-2\pi Nd\cos(2\pi Nd))/d^2\),
where \(d=x-u_j\). This is the original removable double-pole
interface, including its normal coefficient.

**Theorem 1.** Exactly
\[
 \boxed{\quad
 \frac{\mathfrak I_N}{2i}
 =\mathfrak P_N
 :=\sum_j\left\{
       a_j\int_{a_N}^{b_N}K_{j,N}(x)A_N'(x)\,dx
       +b_j\int_{a_N}^{b_N}K_{j,N}(x)A_N(x)\,dx\right\}.
 \quad}
 \tag{6}
\]
There is no endpoint term in (6). Equivalently, define the finite
normal Fourier combination and the actual weighted spectator transform
\[
 \begin{split}
 \mathfrak c_N(\xi)
   &=\sum_{j=j_0}^{j_1}
            (b_j-2\pi iN\xi a_j)e^{-2\pi i\xi j},\\
 \widehat A_N(\xi)
   &=\int_{a_N}^{b_N}A_N(x)e^{2\pi iN\xi x}\,dx .
 \end{split}
 \tag{7}
\]
Then
\[
 \boxed{\qquad
 \mathfrak P_N=\pi N\int_{-1}^{1}
                    \mathfrak c_N(\xi)\widehat A_N(\xi)\,d\xi .
 \qquad}
 \tag{8}
\]
These formulas hold coefficientwise in all remaining variables
and after their fixed ordinary derivatives.

*Proof.* For every window index,
\[
 K_{j,N}(a_N)=K_{j,N}(b_N)=0,
 \tag{9}
\]
because \(N(a_N-u_j)\) and \(N(b_N-u_j)\) are half integers.
The real endpoints differ from every \(u_j\), so no removable-value
exception occurs in (9). Integration by parts in (5) now gives (6).
The derivative in \(A_N'\) includes the phase, sine factor and the
full derivative of the original spectator.

The exact elementary Fourier identity
\[
 K_{j,N}(x)=\pi N\int_{-1}^{1}
                       e^{2\pi iN\xi(x-u_j)}\,d\xi
 \tag{10}
\]
holds also at \(x=u_j\). Differentiate (10), substitute in (5),
and interchange finite sums and compact integrals. This proves
(8) with the sign and normal combination in (7).
Alternatively integrating \(A_N'\) in (6) inside the Fourier
integral produces boundary terms for each individual \(\xi\);
their complete integral vanishes by (9). They must not be
deleted separately at each frequency. \(\square\)

## 2. Original closing, shared colors and the required estimate

Let \(\Lambda_N\) be the original remaining closing functional:
all other prescribed traces, coupons and ordinary outside
evaluations are retained with their original order. If some
microscopic endpoint parameters are shared with this remaining
source, they remain inside \(\Lambda_N\).
Linearity and finite trace sampling commute with (5)--(8), so
the actual closed contribution of this real interface is
\[
 \boxed{\quad
 Z_{N,\mathrm{int}}
 =-\frac{\eta}{\pi^2}\Lambda_N(\mathfrak P_N)
 =-\frac{\eta N}{\pi}
     \int_{-1}^{1}
          \Lambda_N\bigl(\mathfrak c_N(\xi)\widehat A_N(\xi)\bigr)
           \,d\xi .
 \quad}
 \tag{11}
\]
The scalar factor is exactly the factor
\(-\eta/(2\pi^2i)\) of the original double-pole trace multiplied
by \(2i\) in (6). There is no new trace normalization.
In particular one cannot replace the shared closing in (11)
by the product of two separately closed factors.

For several leaf messages at the same receiving color, apply the
weighted construction directly to their ordinary product. If their
separate normalized jets are \(a_{i,j},b_{i,j}\), the joint ones are
\[
 a_j=\prod_i a_{i,j},\qquad
 b_j=\sum_i b_{i,j}\prod_{k\ne i}a_{k,j},
 \qquad \mathcal S_N=\sum_i\mathcal S_{i,N}.
 \tag{12}
\]
This preserves every shared-color product normal. The same
subexponential bound (3), with a larger polynomial factor, holds
for any fixed number of messages. Formulas (5)--(11) then use
these joint jets. The representatives so chosen are the direct
joint Hermite representatives; no off-grid equality with products
of separately chosen representatives is asserted.

Denote by \(Z_{N,\mathrm{ext}}\) the two exterior half-boundary
integrals, after the same original closing and with their original
normalization. The exact window identity is
\[
                         Z_{N,\mathrm{win}}
                 =Z_{N,\mathrm{ext}}
                             -\eta\pi^{-2}\Lambda_N(\mathfrak P_N).
 \tag{13}
\]
Both outer vertical sides and their intersections with other current
faces remain in \(Z_{N,\mathrm{ext}}\). Formula (9) removes only
the integration-by-parts terms in the real interface; it does not
remove those exterior sides.

Thus, once those exterior contributions are controlled at a desired
rate \(B\), the precise additional estimate is
\[
                  |\Lambda_N(\mathfrak P_N)|
                                   \le e^{NB+o(N)} .
 \tag{14}
\]
For a strict parent boundary gap one would need \(B<M_G\).
This is a requirement on the actual joint Fourier/normal pairing
(7)--(11), not a bound on each factor or each frequency separately.
If cancellation between the exterior and interface is to be used
instead, the full combination (13) must be estimated.

A second joined contour in another color applies its original
functional inside (11); it is not an automatic cancellation of
this expression. Opposite orientations do cancel artificial common
sides when one global representative is used on adjacent windows.
They do not supply a second copy with the opposite sign of (11).
An additional operator or current identity would be needed for that.

The frequency interval in (8) includes zero. In particular (3)
only gives the polynomial-times-subexponential coefficient bound
\[
                   \sup_{-1\le\xi\le1}|\mathfrak c_N(\xi)|
                                      \le C N^2M_N.
 \tag{15}
\]
It supplies no uniform nonzero-frequency penalty for
\(\widehat A_N\). All original oscillation and normal compensation
in their product remain available in (11).

## 3. A general positive reference-energy diagnostic

Here is a precise limitation of an absolute real-profile argument,
without assigning a growth lower bound to any quantum current.
Use an original included circle-tree graph with complete outside
vertices, ambient positive angle body \(X\), raw edge energy
\(\mathcal E\), edge count \(e_G\), and a supplied positive
unit-charge parent \(z_0\).

Let \(L\) be a nonempty set of selected vertices of degree one in this
included graph, and let \(E_L\) be their incident edge set.
Require that their incident edges are distinct,
their neighbors lie in \(R=S\setminus L\), \(R\ne\varnothing\),
and \(|n_\ell|\ge2\) for every \(\ell\in L\).
No chosen leaf is adjacent to another chosen leaf.
All other powers are the original fixed powers. These are genuine
terminal leaves here; no additional saturated cut edges or cut
incidence constraints are being silently dropped.

Construct \(z_*\) by putting every vertex in \(R\) and every
outside vertex at its complete angle, using the selected
complete-neighbor terminal solution at each chosen leaf, and
putting every remaining edge at the complete solution.
The terminal reference is strictly positive, including for
\(|n_\ell|=2\). Its opposite endpoint has both \(k_w=h_w=0\)
and \(s_w=G_w=0\). Consequently these edge assignments match at
every shared retained vertex and give \(z_*\in X\).
Their selected rows and energy are
\[
 \rho_\ell(z_*)=-\pi\quad(\ell\in L),\qquad
 \rho_v(z_*)=0\quad(v\in R),\qquad
 \mathcal E(z_*)=\sum_{\ell\in L}
                       \pi(M_\infty-\mathcal I_{n_\ell}).
 \tag{16}
\]
The full ambient differential is
\[
                    d\mathcal E(z_*)
                       =-\sum_{\ell\in L}H_\ell^*\,d\rho_\ell .
 \tag{17}
\]
Indeed this is the terminal edge differential on each chosen
leaf edge, and every coefficient on every other complete edge
is zero. The neighboring differential coefficients are zero,
so they introduce no missing shared work.

**Proposition 2.** With
\[
 M_*=(e_G-|L|)M_\infty+\sum_{\ell\in L}\mathcal I_{n_\ell},
 \tag{18}
\]
the actual positive parent satisfies
\[
                 \boxed{\qquad M_*-M_G=D_*(z_0)/\pi>0,\qquad}
 \tag{19}
\]
where \(D_*\) is the raw-energy Bregman remainder at \(z_*\).

*Proof.* The parent and reference have the same rows at \(L\),
so (17) vanishes on \(z_0-z_*\). Strict convexity gives
\(\mathcal E(z_0)-\mathcal E(z_*)=D_*(z_0)\).
They are distinct because every retained selected parent row is
\(-\pi\), whereas its row at \(z_*\) is zero and \(R\ne\varnothing\).
The segment from the positive reference is inside the ambient
convex body, hence its Bregman remainder is strictly positive.
Use \(M_G=e_GM_\infty-\mathcal E(z_0)/\pi\) and (16).
\(\square\)

The corresponding reduced real phase, after eliminating only the
chosen leaf variables, is
\[
 \Psi_{\mathrm{red}}(\mathbf t_R)
 =\sum_{\ell\in L}S_{n_\ell}(t_{w(\ell)})
   +\sum_{e\notin E_L}\psi(t_v,t_w)
   +\frac{i}{4\pi}\sum_{v\in R}n_vt_v^2
   -i\sum_{v\in R}t_v ,
 \tag{20}
\]
with the outside angles still zero. The regular positive terminal
continuation exists near \(\mathbf t_R=0\), and all other edges
there are positive. By the original constants,
\[
                    \Re\Psi_{\mathrm{red}}(0)=M_*>M_G.
 \tag{21}
\]
Continuity therefore leaves a neighborhood of small nonzero real
retained angles on which this real phase weight exceeds \(M_G\).
Such angles can be chosen in fixed bulk windows, however near the
complete end of those windows needs to be.

For fixed real retained angles, minimizing the leaf incidence
variables on this regular locus gives exactly these
\(\Re S_{n_\ell}\), by the retained-boundary Legendre identity
at height zero. Thus that minimization alone does not remove the
excess in (21). The retained receiving unit rows and their original
oscillation have not been imposed by taking an absolute real
interface bound. If every vertex of \(R\) receives at least one
chosen leaf message, the corresponding candidate absolute phase
weight for the tensor real-interface term is precisely
\(\Re\Psi_{\mathrm{red}}\). This identifies the classical budget
that fails; it supplies neither an estimate for the remaining
quantum edge amplitudes nor a nonzero interface coefficient.

This diagnostic covers a general marked network with shared
retained colors. It is not a new individual filling example.
It does not claim that the interface itself grows at \(M_*\),
that its cancellation is impossible, or that a saturated deletion
face has the same capacity domain as this positive reference.

## 4. Coverage and direct sources

The continuous-frequency character of one-sided interfaces is
already explicit in the two-half-plane endpoint-source theorem
\(985fa\), §3. The new calculation is the phase-weighted finite-window
normal combination (7), its exact midpoint integration by parts,
and its placement inside the unchanged joint closing.
The final diagnostic uses the existing terminal Bregman reference;
it does not propose a new abstract convexity theorem.

Complete direct sources were read at the following unchanged pins,
with their directly used implications and hashes checked:

* [Weighted window and original interface](research_filled_leaf_weighted_window_current.md),
  SHA256 d1b533a14265451d31fb33870787f8f5145c7971f4cfc2d912b1c6652b523188:
  complete final author read retained; exact jets, interface,
  full residue normalization, all exterior sides and aliases.
* [Retained-boundary leaf energy](research_retained_boundary_leaf_energy_profile.md),
  SHA256 e6d91b27e4c87e573e1f3cd471ea759a39ebff37f3f0e90622678cc5ed3579e7:
  complete fresh read retained from this sequence; strict terminal
  references, full differential and regular Legendre identity.
* [Fixed-parent ambient calibration](research_fixed_parent_height_global_calibration.md),
  SHA256 268da098a6650065dc2abada9ce7c1bd8029abc33feb59783a67f03cd25a7bf0:
  complete fresh read; the original positive angle body,
  strict energy convexity, complete-edge constant and parent action.

Only written mathematics and source-text/hash reads were used.
No mathematical program, test, numerical experiment or compilation
was run. Adopted notes and public manuscripts remain unchanged.
