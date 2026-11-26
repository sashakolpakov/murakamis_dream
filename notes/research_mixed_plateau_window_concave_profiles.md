# Concave finite profiles for mixed plateau windows

Research deduction, 6 November 2026. On a plateau with constant
heights, every ordinary finite kernel has a finite alphabet of
concave target profiles. The four possible last-row rates have
affine holomorphic representatives. Consequently any fixed ordinary
window, with its literal Fourier weights, admits a finite family
of rigorous tangent upper bounds on the original real products.
Compatible first-cap profiles can be included by the same argument.
This is a target-concavity and finite-source reduction theorem;
it supplies no new negative comparison or nonzero contribution.
No numerical evaluation is used.

## 1. Source and one allocation of each weight

Use the original kernels and primitive of the
[exact torus composition](research_mixed_conditional_torus_composition.md):
\[
\begin{split}
C_{\epsilon,N}(X,Y)
 &=\sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)p_i(Y)}{P_i^{2+\epsilon}},
 \qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\\
Q_\epsilon(s;a,b)
 &=g(s+a)+g(s+b)-(2+\epsilon)g(s)-g(a)-g(b)+2\pi ias.
\end{split}
\tag{1}
\]
Thus the incoming chirp is retained, with its original sign. All
primitives and logarithmic lifts below are those of this source.
Put \(P=[.22,.45]\), \(\ell_0=.15\), and \(\ell_1=.125\).

Consider ordinary vertices \(p,\ldots,q\), where
\(2\le p\le q\le m-1\), with retained variables
\(z_{p-1},\ldots,z_q\). Their real parts lie in \(P\) and their
heights are constant in the target variables. For the finite contour
reduction suppose \(|\Im z_j|\le.108\); main-index heights lie
in \([-.108,.068]\). These contain the actual ordinary and attached
reference heights and the selected heights used below.

Write \(\epsilon_j\in\{0,1\}\) for the original vertex flag and
\(\sigma_j\in\{0,1\}\), \(\sigma_j\le\epsilon_j\), for a selection.
Unselected type-four heights are their actual negative heights;
selected heights are fixed \(0\le H_j\le.014\). Define
\[
\theta_{p-1}=\theta_q=\tfrac12,\qquad
\theta_j=1\quad(p\le j<q).
\tag{2}
\]
The allocated modulus is exactly
\[
\prod_{j=p}^q|C_{\epsilon_j,N}(X_{j-1},X_j)|
\prod_{j=p-1}^q
 \left|d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}\right|^{\theta_j}.
\tag{3}
\]
The half-powers in (3) are moduli, not holomorphic square roots.
Each internal diagonal and each internal selected monomial occurs
once. Adjacent windows restore the full boundary factor by combining
their two half-allocations.

For an unselected coordinate put \(m_j=1\). At each selected
coordinate choose \(\nu_j\in\{0,1\}\) and put \(m_j=\nu_j\).
The two alternatives for its complete selected weight are
\[
-\Re g(z_j)-2\pi H_j,\qquad 0.
\tag{4}
\]
They are upper-rate alternatives, not a decomposition into two
independently continued source polynomials. The node contribution
to a labeled holomorphic target phase is
\[
W_{\boldsymbol\nu}(z)=
 -\sum_{j=p-1}^q\theta_j\epsilon_jm_jg(z_j)
 +2\pi i\sum_{j=p-1}^q\theta_j\sigma_j\nu_jz_j.
\tag{5}
\]
The ordinary unselected type-four estimate and the complete selected
Fourier bound justify (5), including their polynomial factors and
arbitrarily small rate tolerances. No factorial-dominance restriction
on a selected real target is needed here. When adjoining windows,
choose one \(\nu_j\) for the complete weight first and use that same
choice in both half-allocations.

## 2. A seven-label ordinary alphabet

For each vertex take one of the following labeled expressions:
\[
\begin{array}{c|c|c}
\text{label}&\text{holomorphic expression}&\text{index target}\\ \hline
0&Q_\epsilon(s;a,b)&
 s=x+ih_s,\quad x\in[\ell_\epsilon,.5]\\
L&Q_\epsilon(\ell_\epsilon;a,b)&s=\ell_\epsilon\ \text{real}\\
R&Q_\epsilon(.5;a,b)&s=.5\ \text{real}\\
1_{\kappa,\lambda}&2\pi i(\kappa a-\lambda b)&
 \kappa,\lambda\in\{0,1\}.
\end{array}
\tag{6}
\]
The last line has four labels and no active index variable. Its
maximum is the literal full last-row rate, because
\[
\max_{\kappa,\lambda}\Re[2\pi i(\kappa a-\lambda b)]
 =2\pi(-\Im a)_++2\pi(\Im b)_+.
\tag{7}
\]
This rate is not obtained by substituting \(s=1\) into a central-strip
logarithmic phase. Formula (7) retains all four sign choices even
when the particular constant heights make some redundant.

**Proposition 1.** On the stated height domain, the complete finite
ordinary kernel is bounded, up to a polynomial factor and any
positive rate tolerance, by the maximum of the seven profiles (6).
This includes both level parities and all physical rows.

*Proof.* The bare index comparisons in the
[asymmetric contour proof](research_mixed_horizontal_asymmetric_contour.md),
the [half-index extension](research_mixed_half_index_contour.md),
and the [own-four smaller cut](research_mixed_four_left_cut_extension.md)
place both horizontal aliases below the main line. They bound vertical
aliases by their real cuts and zero-mode joins by their endpoint
profiles. These comparisons are pointwise in the outer arguments
on \(P+i[-.12,.12]\); row-independent outer weights cancel.
The tall ordinary aliases themselves are not being assigned a
concavity theorem. They are removed before (6).

The left real tail increases to \(\ell_\epsilon\). The
[full right-tail theorem](research_mixed_right_tail_endpoint_bound.md)
places the entire real interval \([.5,1]\) below its half-row and
full last-row endpoints when both outer height moduli are at most
.108. It includes the wrapped and zero-safe physical rows.
Its full last-row formula is (7). These bare comparisons are
unchanged by adding (5), which is independent of the index. This
is the same transport of pointwise comparisons used explicitly in
Section 2 of the
[selected own-four finite reduction](research_mixed_selected_four_four_finite_reduction.md).
It does not transport an old unselected affine supporting plane to
new heights. \(\square\)

For fixed \(\boldsymbol\rho\in
\{0,L,R,1_{00},1_{01},1_{10},1_{11}\}^{q-p+1}\) and Fourier choices,
let
\[
\Phi_{\boldsymbol\rho,\boldsymbol\nu}
 =\sum_{j=p}^q Q_{\epsilon_j}^{\rho_j}
                   (s_j;z_{j-1},z_j)+W_{\boldsymbol\nu}(z).
\tag{8}
\]
Only main indices are optimized; fixed or absent indices have formal
zero rows and columns. The maximum over the finite labels in (8)
is a complete upper-rate bound for (3).

## 3. Concavity and a rigorous tangent bound

**Theorem 2.** Every labeled phase (8) is horizontally concave on its
full real product. Subtracting any fixed original reference action
and its original complex boundary affine terms preserves this
concavity. Strictness is not claimed for a direction incident only
to last-row carriers with no remaining node curvature.

*Proof.* Section 2 of the
[second-selection concavity proof](research_mixed_second_selected_horizontal_concavity.md)
establishes the bare estimate
\[
-\Re Q_\epsilon''\succ\mu I_3,\qquad
\mu=1/1250000,
\tag{9}
\]
on \([\ell_\epsilon,.5]+i[-.108,.068]\) for the index and
\(P+i[-.12,.12]\) for both outer arguments. In the own-four
small-index interval, its extra index factorial is essential;
one cannot replace (9) by separate unweighted pair positivity.
The two real cuts use the same theorem at index height zero and
then its principal active submatrix. Each last-row carrier is
affine and has zero Hessian.

For \(x\in P\) at any real height,
\(\Re g''(x+ih)=\pi\Re\cot\pi(x+ih)>0\). All coefficients
of \(-g\) in (5) are nonnegative, so these node terms add
nonnegative negative real Hessians. The original chirps and
selected affine monomials have zero real horizontal Hessian.
Summing the pulled-back forms proves the assertion. \(\square\)

Let \(f=\Re(\Phi-F_*-p_L(z_{p-1}-r_{p-1})
-p_R(z_q-r_q))\) be a labeled defect, where \(F_*,p_L,p_R\)
come from the original all-main reference phase with the allocation
(2), not from a cut or last-row replacement. Its internal
reference derivatives vanish by the original stationarity equations;
the two boundary marginals remain. For any exact trial
\(y\in K=\prod_i[l_i,u_i]\) on the active real product,
\[
\sup_K f\le f(y)+
 \sum_i\max\{\partial_i f(y)(l_i-y_i),
                    \partial_i f(y)(u_i-y_i)\}.
\tag{10}
\]
If an outward enclosure on a whole reference cell gives
\(f(y)\le A\) and \(\partial_i f(y)\in[d_i^-,d_i^+]\),
the rigorous replacement is
\[
A+\sum_i\max\{d_i^-(l_i-y_i),d_i^+(u_i-y_i)\}.
\tag{11}
\]
This follows directly from the supporting affine function of a
concave function. No target-root solve, optimizer stationarity or
lower Hessian inversion is required. Different exact trials may
be used for different labels or cells; no derivative of that
choice enters (10). Each trial and gradient must use the same
original reference, action and boundary marginals.

The maximum of the labeled phases need not be concave. Equations
(10)--(11) are applied separately before taking a finite maximum.
For a fixed window, a common strict negative bound on all the
labeled defects gives a corresponding finite-source upper gap
after spending tolerance on the polynomial factors. Concavity
alone gives neither that sign nor a nonzero coefficient.

## 4. Adding the first cap and locating the reference window

The original bare cap is
\[
\Psi_\alpha(e,a)=S(e)+J(e+a)-J(a)-i\pi ea-\alpha g(e).
\tag{12}
\]
The [cap Hessian theorem](research_mixed_first_cap_plateau_phase.md),
Lemma 1, gives \(-\Re\Psi_\alpha''\succ\pi I_2/200\) on
\[
e\in[.27,.49]+i[-.055,.04],\qquad
a\in P+i[-.108,.021].
\tag{13}
\]
Consequently the main private line, either real cut, and either
horizontal alias at heights \(-.055,.04\), with its original
constant penalty \(-.11\pi,-.08\pi\), are concave labeled profiles.
Any separately proved constant endpoint ceiling is concave too.
Use their existing complete-source bounds only on their proved
height/color domains; (13) does not enlarge a finite packet theorem.
In particular the selected-first-four source at \(H\le.014\)
is covered by the existing finite cap reduction.

For a prefix consisting of this cap and ordinary vertices
\(2,\ldots,q\), use weight one at retained coordinates
\(1,\ldots,q-1\) and weight one half at \(q\). Formula (5)
with these coefficients counts every internal diagonal once.
The reference has only the original right boundary marginal.
Theorem 2 and (10)--(11) extend to every such admitted cap/profile
choice without altering \(S\), its original chirps or color dependence.

For a selected position \(j\), with \(2\le j\le m-2\), exactly
the ordinary factors \(C_j,C_{j+1}\) touch its retained variable.
The smallest incident-factor target block has five variables
\[
(a,u,z,v,b)=(t_{j-1},s_j,t_j,s_{j+1},t_{j+1}).
\tag{14}
\]
Its original reference is supplied by two ordinary vertices
\(j,j+1\) with external legs \(t_{j-1},s_{j+2}\).
The [universal ordinary-window lemma](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2, gives a unique holomorphic zero-lift family on the full
product of those two typed disks. The
[open-window identification](research_mixed_open_word_window_inheritance.md)
identifies every actual restriction with that family, including an
attached external leg. This is a reference family, not a new
target-dependent saddle.

In particular position \(3\), for \(m\ge5\), uses vertices \(3,4\)
and inputs \(t_2,s_5\); \(s_5\) is attached when \(m=5\).
If preserving its correlations with the first endpoint is useful,
one can instead retain the one-ended prefix through vertex \(4\)
with sole external parameter \(s_5\). It has nine original variables:
the three endpoint variables and three ordinary pairs. The same
endpoint/ordinary Brouwer construction and principal Hessian argument
as the [all-word localization](research_mixed_open_word_critical_localization.md)
give its unique holomorphic reference branch. No selected-gap claim
follows from this existence statement.

More generally a selected run \([j,k]\subset[2,m-2]\) needs the
incident ordinary factors \(j,\ldots,k+1\): \(L=k-j+2\) vertices,
\(2L\) original unknown legs with two external inputs, and
\(2L+1\) target variables. A one-ended prefix through \(k+1\)
instead has \(2k+3\) original variables and one external input.
Independent external disks may lose useful actual correlations,
although their coverage is valid. Existing proved
[interior-selection estimates](research_mixed_interior_selected_plateau.md)
remain available and need not be replaced by enumerating these profiles.

## 5. Limits of this reduction

The last incident factor at selection \(j=m-1\) is the complete
terminal transform \(V_{\epsilon_m}\), not an ordinary \(C\).
Its coherent inner source, physical support triangle and additional
currents require their own finite-source reduction. The restricted
central Hessian in the
[terminal joint-source theorem](research_mixed_terminal_four_joint_source.md)
does not establish concavity for every complete terminal profile.
Existing terminal estimates can be retained as a separate boundary
module; transposing a cap does not identify its localized sectors.

Nor does constant-height concavity imply concavity on the actual
nonplateau graph. For a real \(C^2\) graph \(w(x)=x+iH(x)\),
a holomorphic phase \(F\), and a real direction \(v\), the exact rule is
\[
\begin{split}
D^2\Re F(w(x))[v,v]
={}&\Re\{(v+iDH\,v)^T F''(w)(v+iDH\,v)\}\\
 &-\sum_j\Im F_j(w)\,D^2H_j[v,v].
\end{split}
\tag{15}
\]
The first term equals
\[
v^T\Re F''v-(DH\,v)^T\Re F''(DH\,v)
             -2v^T\Im F''(DH\,v).
\tag{16}
\]
Its second term can oppose horizontal concavity, and (15) has an
additional height-curvature term. For the elementary model
\(F(w)=-w^2/2\), \(H(x)=ax\), the resulting second derivative
is \(a^2-1\). This only disproves an implication from horizontal
concavity; it is not a counterexample for an actual source phase.

On a piece of the
[literal split hybrid graph](research_mixed_split_cutoff_hybrid_contour.md)
where neighboring cutoffs are one, its right taper is
\(H_j=400c_j(.5-x_j)^2\). Its derivative has modulus up to
\(40|c_j|\), and \(H_j''=800c_j\). Where a neighbor cutoff
is active, mixed derivatives also occur; the piecewise interfaces
retain their exact graph treatment. Thus no small-slope or favorable
sign hypothesis needed to control (15) has been supplied by
Theorem 2. This applies also when the phase contains the original
selected monomial or chirps.

Finally, the complete
[finite boundary-window criterion](research_mixed_open_finite_boundary_windows.md)
contains occupation debits and positive quadratic pinning fees,
as well as source profiles. Its local reference coercivity pays
those fees in its stated regime; the present theorem does not
declare that entire window objective globally concave. A whole-source
closure still needs the required negative labeled comparisons,
the terminal and nonplateau estimates on their actual contours,
and the original local nonzero packet. The plateau alphabet supplies
a uniform finite target reduction for fixed windows, not those
remaining signs or the cofinite filling theorem.
