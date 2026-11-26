# Exponentially accurate analytic transport of the full matching source

The original radical matching unit admits a holomorphic lift that is
exponentially close to one on any prescribed fixed complex compact,
provided its exact physical data are imposed on sufficiently short
windows bounded away from the endpoint \(c=2\). The lift and its genuine
analytic reciprocal retain every mixed normal. They therefore give
exact original multiwindow trace identities for arbitrary attachments.
A supplied nonzero local Morse period has the same leading coefficient
after this transport. No occurrence of that local cycle in the original
global period is asserted.

## 1. The original unit and its exponentially small interior data

Use the full physical algebra, original kernels and trace of [M].
Thus \(N\ge2\), \(d=N-1\), \(m=\lfloor N/2\rfloor\),
\(\eta=(-1)^d\), \(P_N(z)=2T_N(z/2)+2\), and
\[
 c_a=2\cos((2a+1)\pi/N),\quad
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z),\quad
 S_j=\prod_{h=1}^j2\sin(h\pi/N).
 \tag{1}
\]
There are \(m\) double nodes and, at odd levels, the additional simple
node \(-2\). Put \(D_a=\eta(4-c_a^2)\) at double nodes. The normalized
normal coupon \(\delta_a\) has derivative \(D_a^{-1}\) at its own node,
zero values everywhere and all other first derivatives zero.

Let \(I\) be the vertices actually subjected to the original traces,
and \(\mathcal E\) a fixed finite multigraph of chosen same-index
connections with distinct endpoints in \(I\). The other original
kernels and all ordinary free variables remain in the attachment.
The exact unit of [M] is
\[
 U=\prod_{e=vw\in\mathcal E}(1+V_e),\qquad
 V_e=\sum_{a,b<m}J_{ab}\delta_a^{(v)}\delta_b^{(w)},\qquad
 J_{ab}=\frac{W_{ab}}{G_{ab}},
 \tag{2}
\]
where
\[
 G_{ab}=\sum_{r=0}^{m-1}e_r(c_a)e_r(c_b)\ge1,\qquad
 W=G^{-1},\qquad |W_{ab}|\le4m\le2N.
 \tag{3}
\]
The quotient in (2) is entrywise. All its nonzero Newton summands
in (3) are positive.

Fix \(0<\varepsilon<4\). Set
\[
 \alpha=\min(1/8,\sqrt{\varepsilon}/(4\pi)),\quad
 k=\lfloor\alpha N\rfloor,\quad \kappa=\alpha\log2.
\]
For sufficiently large \(N\), \(1\le k<m\). If \(h<k\) and \(1\le j\le k\),
\[
 c_h\ge2-4\pi^2\alpha^2\ge2-\varepsilon/4,\qquad
 4\sin^2(j\pi/N)\le4\pi^2\alpha^2\le\varepsilon/4.
 \tag{4}
\]
Consequently, whenever \(c_a\le2-\varepsilon\), none of its first
\(k\) Newton factors vanishes and \(e_k(c_a)\ge2^k\).
For two such double nodes, (3) gives
\[
 G_{ab}\ge2^{2k},\qquad
 |J_{ab}|\le2N e^{-\kappa N}\quad(N\ge2/\alpha).
 \tag{5}
\]
This proof uses the actual positive physical Newton values; it does
not posit a complex continuation of \(G^{-1}\).

At every double node, including those approaching \(-2\),
\[
 |D_a|=4\sin^2((2a+1)\pi/N)\ge16/N^2.
 \tag{6}
\]
Thus the ordinary mixed derivative of \(V_e\) at a physical pair,
\(J_{ab}/(D_aD_b)\), is bounded by a polynomial in \(N\) times
\(e^{-\kappa N}\). Its other value/first-normal data are zero.
At an odd simple endpoint no derivative is imposed.

## 2. Explicit holomorphic lift and genuine reciprocal

Fix any target compact in \(\mathbb C^I\), and a larger buffered
polydisk containing it and all the physical nodes. These choices
precede \(N\). At each \(v\in I\), take a consecutive nonempty window
\(\mathcal I_{v,N}\) of at most \(\rho N\) distinct physical nodes,
all satisfying \(c\le2-\varepsilon\). Keep their original multiplicities.
The number \(\rho>0\) will be chosen after the compact and \(\kappa\).

Let \(H_{v,a,1}(z)\) be the ordinary spectral Hermite cardinal
polynomial whose first derivative is one at the double node \(c_a\)
in that window and whose other required window jets vanish.
Source [S], Lemma 2, proves uniformly over the window location that
the full interpolation operator on a fixed disk obeys
\[
 \|\mathscr L_{\mathcal I}d\|
 \le C N^B \exp\!\left\{C_R s(1+\log(N/s))\right\}\max|d|,
 \qquad s=|\mathcal I|.
 \tag{7}
\]
This includes the fold endpoint. Its proof uses the actual bound
\(|c_a-c_b|\ge16|a-b|^2/N^2\), not an assumed spacing of order \(N^{-1}\).
For \(s\le\rho N\), write the exponential cost as
\(\omega_R(\rho)N\), where
\(\omega_R(\rho)=C_R\rho(1+|\log\rho|)\to0\).

For an edge \(e=vw\), define the polynomial
\[
 v_{e,N}^{\sharp}(z_v,z_w)=
 \sum_{\substack{a\in\mathcal I_{v,N},\,b\in\mathcal I_{w,N}\\
                         a,b\ {\rm double}}}
 \frac{J_{ab}}{D_aD_b}
       H_{v,a,1}(z_v)H_{w,b,1}(z_w).
 \tag{8}
\]
This is the tensor interpolation of precisely the full physical jets
of \(V_e\). Equations (5)--(7) give, on the larger polydisk,
\[
 \|v_{e,N}^{\sharp}\|
 \le C N^{B'}e^{[-\kappa+2\omega_R(\rho)]N}.
 \tag{9}
\]
Choose the fixed window density so that \(2\omega_R(\rho)<\kappa/4\).
Absorbing the polynomial factor leaves a fixed positive exponential
gap. Put
\[
 \boxed{\quad
 \mathcal U_N=\prod_{e\in\mathcal E}(1+v_{e,N}^{\sharp}),
 \qquad \mathcal V_N=\frac1{\mathcal U_N}.
 \quad}
 \tag{10}
\]
For all sufficiently large levels, \(\mathcal U_N\) is nonzero
throughout the buffered polydisk, and, for some \(\gamma>0\),
\[
 \mathcal U_N=1+O(e^{-\gamma N}),\qquad
 \mathcal V_N=1+O(e^{-\gamma N}).
 \tag{11}
\]
Every fixed derivative has the same conclusion on the smaller target
compact by Cauchy's formula. The constants are uniform over the allowed
window locations. Parallel edges are included literally. A selected
loop can be omitted because its radical correction is zero.

Evaluation of all mixed jets, with derivative order less than the
original multiplicity at each node, is an algebra homomorphism.
Equation (8) therefore proves
\[
 \operatorname{jet}_{\boldsymbol{\mathcal I}}\mathcal U_N
       =\operatorname{jet}_{\boldsymbol{\mathcal I}}U,\qquad
 \operatorname{jet}_{\boldsymbol{\mathcal I}}\mathcal V_N
       =\operatorname{jet}_{\boldsymbol{\mathcal I}}U^{-1}.
 \tag{12}
\]
The second equality follows from the genuine analytic inverse in (10).
One must not replace that inverse by the finite matching polynomial
off the physical jets: products of the interpolating polynomials need
not be square-zero as ordinary functions.

## 3. Exact original traces, attachments and signed powers

Keep any original joint attachment \(A_N\), including all untouched
kernels and ordinary free-boundary variables, and any signed integers
\(n_v\). In the selected variables use the original physical crossing
powers, with all their first normals. Set
\[
 F_{<,N}=A_N\prod_{v\in I}R(z_v)^{n_v}
                   \prod_{e\in\mathcal E}K_{<,e},\qquad
 F_N=A_N\prod_{v\in I}R(z_v)^{n_v}
                   \prod_{e\in\mathcal E}K_e .
 \tag{13}
\]
Negative powers may be represented by their original polynomial
multiplication classes in the traced variables. Free variables are
not reduced. Source [M] gives \(F_N=UF_{<,N}\) in the full tensor
algebra, including all mixed normal coordinates.

For contours \(\Gamma_v\) enclosing exactly \(\mathcal I_{v,N}\)
inside the common holomorphy domain, define the original partial trace
\[
 \Phi_{\boldsymbol{\mathcal I},N}(B)=
 \frac{(\eta N^2)^{|I|}}{(2\pi i)^{|I|}}
 \int_{\prod_v\Gamma_v} B(\mathbf z)
                       \prod_v\frac{dz_v}{P_N(z_v)}.
 \tag{14}
\]
It is the sum of the original local value/normal rows on precisely
those assignments, with one value at every odd simple node.
The full residue product rule and (12) give the exact identities
\[
 \boxed{\quad
 \Phi_{\boldsymbol{\mathcal I},N}(F_N)
   =\Phi_{\boldsymbol{\mathcal I},N}(\mathcal U_NF_{<,N}),\qquad
 \Phi_{\boldsymbol{\mathcal I},N}(F_{<,N})
   =\Phi_{\boldsymbol{\mathcal I},N}(\mathcal V_NF_N).
 \quad}
 \tag{15}
\]
These hold for arbitrary attachments, without positivity or
factorization, coefficientwise in every ordinary free variable and
its derivatives. Either source in (15) may also be replaced by a
holomorphic representative with exactly its full window jets.
Every crossing carrier, spectator normal and original trace factor
then remains part of the integrand.

## 4. A supplied local Morse contribution and the global remainder

Suppose a specified local descent chain in the target compact carries
an original low-source differential \(\omega_N\) with a supplied
nonzero Morse packet. In precise terms, let \(I_N=\int_{\Gamma}\omega_N\)
have its nonzero local Gaussian asymptotic, with the corresponding
absolute descent estimate
\[
                  \int_\Gamma|\omega_N|/|I_N|=e^{o(N)}.
 \tag{16}
\]
A uniform holomorphic Morse expansion with nonzero normalized leading
amplitude supplies (16); a nonzero Hessian alone does not.
Then (11) proves directly
\[
 \int_\Gamma\mathcal U_N\omega_N
       =I_N(1+O(e^{-\gamma' N})),\qquad
 \int_\Gamma\mathcal V_N\omega_N
       =I_N(1+O(e^{-\gamma' N}))
 \tag{17}
\]
for any fixed \(0<\gamma'<\gamma\), after increasing the starting level.
Thus the given local leading coefficient and its orientation are
preserved. The error bound follows by multiplying (16) by the uniform
error in (11); it does not exchange the bilinear observation for a norm.
These are periods of the lifted representatives in (15), without an
off-grid equality to the canonical polynomial \(F_N\).

The original full trace also has all assignments outside the selected
product of windows. Equation (15) does not estimate or delete them.
Deforming its closed contours still retains every midpoint connector,
endpoint current and remaining chain. The lift introduces no new pole,
but it does not prove that a chosen Morse chain occurs with nonzero
coefficient in that deformation. Neither arbitrary short-filling
noncancellation nor a new geometric-cycle occurrence follows from
(17). The endpoint region \(c\to2\), excluded from (5), also remains
outside this uniform exponential estimate.

## Direct sources

* [M: Full radical matching unit transport](research_full_radical_matching_unit_transport.md),
  SHA256 437867f73282cf09d7bd7b7e9b03759401cf6e96733f9e6116854dc867e40112.
* [S: Short spectral window repair](research_short_spectral_window_repair.md),
  SHA256 581ccd3ec9232a6aa1f42172fcff856f94a6d76efccc001bd411cf2243de2550.
