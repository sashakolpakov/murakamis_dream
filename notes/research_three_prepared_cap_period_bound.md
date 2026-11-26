# A whole-period entrance bound for the original prepared cap

Research proof, 4 November 2026. Completed source artifacts and frozen
manuscripts are unchanged.

This supplies a quantitative whole-period bound for the actual prepared
source, rather than an arbitrary function with the same local phase.
Together with its proved disk packet, it gives an initial capped
Gaussian source envelope. Propagation of that envelope through further
attachments requires the corresponding retained-kernel estimates.

## 1. Actual source and statement

Use the exact conventions of
[the quantified prepared-cap theorem](research_three_prepared_cap_quantified_source.md):
\[
 A=JM^3,\qquad x_h=\frac16+iY_h,\qquad
 Y_h=\frac{\log2}{2\pi},\qquad
 B_N(y,w)=v(w)^TA^2h(y).
 \tag{1}
\]
The complete outside color is \(w=-2\). In particular (1) is the
undeleted original source with its full boundary polynomial, at both
level parities.

**Theorem 1.** Uniformly over the entire real outgoing period,
\[
 \sup_{\eta\in\mathbb R}
       |B_N(\eta+iY_h,-2)|\le C N^A e^{47791N/25000}
                                  =C N^A e^{1.91164N}.
 \tag{2}
\]
Every fixed ordinary derivative at the complete outside color and
every fixed Fourier-endpoint derivative have the same exponential
bound. On a sufficiently small fixed complex ordinary-color
neighborhood of \(-2\), the uniform upper rate can be chosen as
\(1.91165\), including every fixed derivative on a smaller neighborhood.

## 2. Two global supporting planes

Keep the same fixed central wire and angular heights as in the
prepared source proof, with the following harmless interval overcover:
\[
 \begin{split}
 h_c&\in[.10135867,.10135871],\\
 H_c&\in[.97895508,.97895512],\qquad
 x=\xi+ih_c,\quad t=\tau-iH_c,\\
 &\hspace{10mm}7/50\le\xi\le1/5,\quad0\le\tau\le9/5.
 \end{split}
 \tag{3}
\]
The actual central cap bottom has the real phase
\[
 R(\xi,\tau)=\Re\{b(x,t)+\Psi(t)\}
                         +\frac{3\tau H_c}{2\pi}-H_c.
 \tag{4}
\]
All factorial arguments in (4) are in their original regular strips.
The joint cap Hessian in
[the concavity theorem](research_three_vertex_joint_concavity.md),
Lemma 3, proves that (4) is strictly concave in \((\xi,\tau)\)
on this whole rectangle, uniformly over (3). Therefore, at any
interior rational point \(z\),
\[
 \sup_{q\in\mathcal B}R(q)
 \le R(z)+\sum_j\max\{\partial_jR(z)(a_j-z_j),
                           \partial_jR(z)(b_j-z_j)\},
 \qquad \mathcal B=\prod_j[a_j,b_j].
 \tag{5}
\]
At
\(z=(.180461985434,1.522032732790)\), outward evaluation of this
single plane gives
\[
                             R<1.26465.
 \tag{6}
\]
This is a global concavity certificate, not a sampled maximization.
The value and both derivatives are evaluated with the complete height
intervals (3). The exact real derivative formulas are (10) of
[the original central-source proof](research_three_cap_central_source.md).
All other pieces of that same original cap decomposition have rate
below \(1.26\), or below \(2/3\) for its removed radical, by its
Lemma 2. Thus (6) bounds the entire actual cap, including its physical
tails, folded currents, odd simple node, and all original normals.

For the retained vertex, delete the L40 corner and put
\(r=e^{-2\pi h_c}\), so \(1/2<r<53/100\). Minimize each
denominator interval over its real wire phase. Its complete summand
envelope, with the cardinal factors retained, is
\[
 \mathscr E_r(s,t)=-\tfrac12\log(r/2)+\mathcal J(s+t)
       +s\log r-t\log2-\ell_r(s)-\ell_{1/2}(t),
 \quad
 \ell_r(s)=\int_{-s/2}^{s/2}\log|1-r e^{2\pi iu}|\,du.
 \tag{7}
\]
Section 6 of
[the global-wire theorem](research_three_vertex_global_wire_bound.md)
proves, for every radius in \([1/2,53/100]\), that the global
maximum of (7) on the larger L50 retained domain is attained inside
\([3/10,37/100]^2\). Its proof excludes all low-sum regions and
all boundary faces before using strict index concavity. This applies
in particular to the L40 subset; the central maximizing square remains
retained.

On this square use the concave support plane at the rational point
\((.35320055,.32326893)\). Its value and gradient are evaluated
outward for the entire interval of radii coming from (3). The result is
\[
                 \sup_{\mathcal D_{40}}\mathscr E_r<.64699.
 \tag{8}
\]
This is an absolute real-index bound, valid for every real phase of
both wires and every subset of the original summands.

The same bound holds if the first height runs from \(h_c\) to
\(Y_h\). Indeed, for each fixed pair of indices the height second
derivative of (7) is \(4d_1\ge0\), with \(d_1\) defined in
equation (31) of the global-wire theorem. The maximum envelope is
therefore convex in the height. At its first endpoint use (8), and
at the homogeneous endpoint use
\(2c<2(161533/500000)<.64699\). This proves the bound on the whole
joining height interval without assuming a quadratic approximation.

## 3. Exact wire deformation and restoration of the original source

The exact half-band reconstruction gives the retained attachment as
\[
 v(w)^TA(A-E_{40})h(y)
       =N\int_{-1/8+iY_h}^{7/8+iY_h}
                     W_N(x,w)\widetilde V_N^{(40)}(x,y)\,dx.
 \tag{9}
\]
Both factors are the original entire finite Fourier functions of
\(x\); their product is periodic. Move only the central segment
\(.14\le\Re x\le.20\) down to the fixed height in (3), retaining
both wire verticals. For every real outgoing phase \(\eta\), at
\(y=\eta+iY_h\), the resulting pieces have the following bounds:

| Original piece | Cap rate | Retained-vertex rate | Combined upper rate |
| --- | ---: | ---: | ---: |
| Central horizontal interval | \(1.26465\) | \(.64699\) | \(1.91164\) |
| Exterior real wire intervals at \(Y_h\) | \(1.264\) | \(2c<.646132\) | \(1.910132\) |
| Both wire verticals | \(1.2638\) | \(.64699\) | \(1.91079\) |

The sharper exterior bound is the proved bound in Section 2 of
the quantified prepared-cap theorem. The two actual cap vertical
bounds are Proposition 2 of the original cap-wire-complement proof;
their individual rates are \(1.261\) and \(1.2638\). Their source
scope includes the entire indicated height interval and the original
outside ordinary normals. The retained factor is bounded by its
absolute summands before taking any cap absolute value. Thus this
argument retains every angular current inside the exact cap and
uses no local cap packet on a complementary contour.

All lengths and the reconstruction factor \(N\) cost only a polynomial.
Finally, the separate
[Fourier corner-transfer theorem](research_three_chain_fourier_corner_transfer.md)
gives, on the full outgoing real period at height \(Y_h\),
\[
 |v(-2)^TAE_{40}h(y)|\le CN^A e^{1.715N}.
 \tag{10}
\]
It also retains the original outside normals. Adding (10) restores
exactly the undeleted source (1) and proves (2). The same cited
source bounds have arbitrarily small rate increases on sufficiently
small complex ordinary-color neighborhoods. Their strict margins
permit the rate \(1.91165\). Fixed ordinary derivatives follow
there by Cauchy; the already proved complete-point derivative bounds
give the sharper complete-point rate in (2). Fourier derivatives
cost powers of \(N\), either directly in the finite factors or by
the exact finite Fourier degree after the integration. \(\square\)

## 4. An initial capped Gaussian source envelope

Let \(S_1(y)\) be the actual prepared phase at complete outside
color, and set
\[
 M_1=\Re S_1(x_h)>1.9113,\quad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i),\quad
 v(t)=\min\{d_{\mathbb T}(t,0),1/100\}.
 \tag{11}
\]
The proved analytic seed class has
\(|S_1'(x_h)|\le|k_0|(3/100)\) and
\(-\Re S_1''>8\) on the complex disk of radius \(1/200\).
The quantified source theorem supplies the actual nonzero packet
on this entire disk.

**Corollary 2.** The original prepared source satisfies
\[
 |B_N(x_h+t,-2)|\le CN^A
  \exp N\left[M_1+|k_0|\frac3{100}v(t)
                         -\frac{29}{20}v(t)^2\right]
 \qquad(t\in\mathbb R).
 \tag{12}
\]
Every fixed ordinary derivative at the complete outside color and
fixed Fourier derivative has the same bound with polynomial cost.

*Proof.* On \(|t|\le1/200\), integrate the seed's real Hessian
bound to obtain
\(\Re S_1(x_h+t)\le M_1+|k_0|(3/100)|t|-4t^2\).
The actual source packet proves (12) there. For all remaining
phases, \(v\in[1/200,1/100]\). Since
\[
 |k_0|=4\pi/\sqrt{21}>125/46,
 \quad
 1.9113+\frac{125}{46}\frac3{100}\frac1{200}
        -\frac{29}{20}\left(\frac1{200}\right)^2>1.91165,
 \tag{13}
\]
and the quadratic on the left increases over this interval,
the whole-period estimate (2) is strictly smaller than the desired
right side. This includes the entire annulus between radii
\(.005\) and \(.01\), not only the far complement. Locally,
fixed derivatives of the true holomorphic packet give polynomial
factors; on the complement use Theorem 1. \(\square\)

This is an entrance theorem for the prescribed original source.
It does not assert that three or arbitrarily many additional quantum
attachments already preserve (12).

## 5. Reproduction

```sh
python3 experiments/check_three_prepared_cap_period_bound.py --precision 192
```

The [checker](../experiments/check_three_prepared_cap_period_bound.py)
and [record](../repro/results/research-three-prepared-cap-period-bound.json)
contain both rational supporting points, their exact boxes, outward
phase/gradient enclosures and all scalar budgets. The positive-strip
primitive is evaluated directly by its convergent dilogarithm branch.
No optimization routine or sampled critical point is used in acceptance.
