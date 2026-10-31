# Fractional odd-cycle packing for the original regular-window source

31 October 2026. **Internally reviewed research corollary and conditional
source-rate criterion.** Root and two separate readers completed full
analytical reviews. This refines the internally reviewed
[regular-window phase bound](research_regular_spectral_window_phase_exclusion.md)
on any fixed original incidence graph. It does not assert that regular
windows cover the source or that their positive envelopes have the complete
volume rate. The local analytic constants remain inputs requiring their
stated hypotheses.

## 1. Original face phases and certified local losses

Keep one positive radius \(L_f\) and one phase \(\vartheta_f\) per
original ordinary face, with the unchanged target exponent \(t_f(N)\).
For the original homogeneous source this is \(d=N-1\). Protected
variables are specialized to zero as in that source.

Let \(J\) consist of selected original ports whose literal start/stop
windows satisfy either the four-positive regular-window theorem or the
[one-protected-outer theorem](research_protected_outer_window_phase_exclusion.md).
In the latter case exactly one outer weight is zero and the other three
incident weights are positive. Write \(W_{e,N}\) for the actual window polynomial and
\(E_{e,N}(L)\) for its positive envelope. Every unused row, scalar zero
and raw sign stays in these definitions. At other ports use certified
phase-uniform majorants \(M_{e,N}(L)\) for their actual factors.

Index the supported incidences at a port separately, even if they meet the
same face. A protected zero incidence is omitted and has no phase variable.
The required alignment has the form
\[
 \vartheta_{f(a)}=\varphi_e+\pi\epsilon_a\pmod{2\pi},
 \qquad a\text{ incident to }e,\quad \epsilon_a\in\mathbb F_2,
 \tag{1}
\]
with a free common phase \(\varphi_e\). A straddling LEFT window has
labels \((0,0,1,0)\) in the order \((x,b,c,y)\); full-row windows use
the actual signs at their two endpoints. In a one-protected-outer window
delete the zero incidence from this list; the remaining three labels are
exactly those in its scalar-active theorem.

Let \(|\cdot|_{\mathbb T}\) be circular distance modulo \(2\pi\), and set
\[
 d_e(\vartheta)=\min_{\varphi\in\mathbb T}
   \max_{a\text{ at }e}
       |\vartheta_{f(a)}-\varphi-\pi\epsilon_a|_{\mathbb T}.
 \tag{2}
\]
The minimum exists by compactness. This is precisely distance from the
local alignment in the product supremum metric. To compare with the
relative-phase version of the local theorem, fix one incidence \(a_0\)
and put
\[
 D_e=\max_{a\text{ at }e}
 |(\vartheta_{f(a)}-\pi\epsilon_a)
   -(\vartheta_{f(a_0)}-\pi\epsilon_{a_0})|_{\mathbb T}.
\]
The circular triangle inequality and the choice of \(a_0\) give
\(d_e\le D_e\le2d_e\). Hence, for each fixed \(\eta>0\), the local
theorem supplies \(c_e>0\), \(C_e\ge1\), and \(N_e\) such that
\[
 \begin{aligned}
 |W_{e,N}|&\le C_e e^{-c_eN}E_{e,N}(L)
                  &&\text{if }d_e\ge\eta,\\
 |W_{e,N}|&\le E_{e,N}(L)&&\text{for every phase}.
 \end{aligned}\tag{3}
\]
The second inequality is the original positive-envelope bound. A zero
common scalar makes both sides zero exactly; no local value is divided out.

## 2. Odd cycles force a collection of mismatched ports

Form the bipartite incidence multigraph with ordinary-face vertices,
selected-port vertices, and the labeled incidences (1). Repeated edges
remain distinct. A simple cycle here has no repeated vertices except its
initial/final vertex; two distinct parallel edges are allowed to form a
length-two cycle. Protected zero incidences are absent.

Choose a nonempty finite collection \(\mathcal C\) of cycles for which
the sum of the incidence labels is odd. Let \(r_{\max}\) be the largest
number of port vertices on one of these cycles. Fix
\[
 \eta=\frac{\pi}{4r_{\max}},\qquad
 B(\vartheta)=\{e\in J:d_e(\vartheta)\ge\eta\}.
 \tag{4}
\]
Then \(B(\vartheta)\) meets every cycle in \(\mathcal C\).

Indeed, choose a minimizing \(\varphi_e\) at each port on the cycle
and subtract its two incidence equations. Upon summing around the cycle,
the face phases telescope, while the odd label sum leaves \(\pi\)
modulo \(2\pi\). Applying the circular triangle inequality gives
\[
 \pi\le2\sum_{e\text{ on }C}d_e(\vartheta).
 \tag{5}
\]
If every port of \(C\) were outside \(B\), the right side would be
strictly below \(2r_{\max}\eta=\pi/2\), a contradiction. This uses
only the original incidence multigraph; no white-sphere topology is needed.

## 3. Fractional cycle capacities give an additive loss

Take every \(c_e\) in (3) at the same threshold (4). Define
\[
 \kappa_{\mathcal C}=\max_{\lambda_C\ge0}
 \left\{\sum_{C\in\mathcal C}\lambda_C:
       \sum_{C\ni e}\lambda_C\le c_e
                         \text{ for all }e\in J\right\}.
 \tag{6}
\]
This finite linear program has a finite attained positive value. Every
cycle contains a port, so its variable is bounded by that port's finite
capacity. The feasible set is therefore compact. A sufficiently small
positive weight on any single odd cycle proves positivity.

For any feasible packing, (5) implies
\[
 \begin{aligned}
 \sum_{e\in B(\vartheta)}c_e
 &\ge\sum_{C\in\mathcal C}\lambda_C
                      |B(\vartheta)\cap C|\\
 &\ge\sum_{C\in\mathcal C}\lambda_C.
 \end{aligned}\tag{7}
\]
Consequently every phase point has total certified loss at least
\(\kappa_{\mathcal C}\). For a port-disjoint collection one obtains
the simple lower bound
\[
 \kappa_{\mathcal C}\ge
       \sum_{C\in\mathcal C}\min_{e\in C}c_e.
 \tag{8}
\]
Overlapping cycles can improve the packing value; their phases are not
assumed independent.

The capacities are analytic inputs, not automatically known numerical
constants. If a different cycle collection changes \(r_{\max}\), the
threshold and its certified \(c_e\)'s must be checked again. Alternatively
one may fix the smaller threshold \(\pi/(4|J|)\) once and then compare
cycle collections using that common set of capacities.

## 4. The unchanged Cauchy coefficient

At selected ports set \(P_{e,N}=W_{e,N}\). Multiply (3) over the bad
ports, use the envelope bounds elsewhere, and then apply (7). Uniformly on
the one original phase torus, for \(N\ge\max_eN_e\),
\[
 \left|\prod_eP_{e,N}\right|
 \le C e^{-\kappa_{\mathcal C}N}
       \prod_{e\in J}E_{e,N}(L)
       \prod_{e\notin J}M_{e,N}(L),
 \qquad C=\prod_{e\in J}C_e.
 \tag{9}
\]
Use formal face variables \(z_f\), distinct from their radii \(L_f\).
The original Cauchy formula gives
\[
 \boxed{\displaystyle
 \left|\left[\prod_f z_f^{t_f(N)}\right]\prod_eP_{e,N}(z)\right|
 \le C e^{-\kappa_{\mathcal C}N}
 \frac{\prod_{e\in J}E_{e,N}(L)
       \prod_{e\notin J}M_{e,N}(L)}
      {\prod_fL_f^{t_f(N)}}.}
 \tag{10}
\]
All protected specializations, source target exponents and scalar modes
remain unchanged. There is one radius per original face, not one per
incidence. Any external source character or prefactor retains its actual
modulus separately; no such factor is silently discarded in (10).

## 5. A conditional strict source-rate certificate

Let
\[
 B_L=\limsup_{N\to\infty}\frac1N\log
 \frac{\prod_{e\in J}E_{e,N}(L)
       \prod_{e\notin J}M_{e,N}(L)}
      {\prod_fL_f^{t_f(N)}},
 \tag{11}
\]
with \(\log0=-\infty\). Then (10) bounds the actual window coefficient's
normalized logarithmic limsup by \(B_L-\kappa_{\mathcal C}\).
For a diagram with certified complete rate
\(\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)\),
\[
 B_L-\kappa_{\mathcal C}<\Phi_D,\tag{12}
\]
is a sufficient strict-rate certificate for this original window piece.
It strengthens merely recording that some positive phase loss exists.
It does not establish (12) without quantitative envelope and local-loss
inputs.

A polynomial-size family of pieces can be summed only with uniform
estimates. Precisely, it suffices that the positive quotient for each piece
\(p\) be at most \(\exp\{N(B_p+\omega_N)\}\), where
\(\omega_N\to0\) uniformly, that the multiplicative constants have
uniformly subexponential growth, that the bounds apply from one common
level onward, and that
\(B_p-\kappa_p\le\Phi_D-\varepsilon\) with one \(\varepsilon>0\).
The polynomial number of pieces then costs only \(o(N)\) in the logarithm.
Uncovered source configurations require their own estimates.

No claim is made that compatible phase systems are negligible, that
arbitrary boundary windows satisfy (3), or that the packing capacities
overcome every diagram's envelope excess. This is a general fixed-graph
criterion available at arbitrary fixed width, not universal diagram
coverage or the volume conjecture.
