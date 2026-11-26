# Full-period vertical currents as charge convolutions of reduced sources

Private written proof, 16 November 2026.

The full angular trace rectangle admits an exact inclusion–exclusion
expansion in which every surviving vertex keeps its full original
trace. Pairing the two ends of each vertical side then gives an integral
of reduced graph sources with explicit endpoint kernel coupons.
Multiplying all coupons at a shared surviving vertex before expanding
them turns those insertions into finite symmetric charge convolutions.
The resulting bound uses actual reduced sources, with their signed
powers and full normals, instead of an absolute unfilled spectator norm.

This is the full-\(\pi\) vertical current of the original trace rectangle.
It is not the older [one-step Ward current](research_even_twist_ward_source_reduction.md).
The decorated Ward identities
and the [classical saturated-face factorization](research_saturated_angle_face_energy.md)
remain distinct. The formula below does not assume their face gap is
a bound for this current, and proves no source noncancellation.

## 1. Original full trace and charge convention

Let \(N\ge2\), \(D=N-1\), \(\eta=(-1)^D\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N),\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
Use the original full Newton kernel
\[
 K_N(z,w)=\sum_{j=0}^{D}e_j(z)e_j(w),\qquad z(t)=-2\cos t.
 \tag{2}
\]
The double physical roots have positive angular lifts
\[
 c_a=-2\cos\tau_a,\qquad
 \tau_a=\pi(D-2a)/N>0,\qquad 0\le a<\lfloor N/2\rfloor.
 \tag{3}
\]
At odd levels \(-2\) is an additional simple root.

Keep the full crossing scalar
\[
 C_{N,n}=\exp\{\pi i nD^2/(4N)\}.
 \tag{4}
\]
For an integer signed power \(n\), the original crossing \(R^n\)
has the same full physical data as
\(C_{N,n}\exp(inNt^2/(4\pi))\). The same data define the canonical
entire real-power extension \(R_n\). We use this extension when \(n\)
is not integral, without changing the integer crossing convention.

The original entire cosine coupon \(\mathcal C_{N,\chi}\) is the
unique class with the value and spectral derivative of
\(\cos(N(1-\chi)t)\) at every double node and value \(1\) at the
odd simple node. Put
\[
 L_{n,\chi}[f]=\phi_N(R_n\mathcal C_{N,\chi}f),\qquad
 \ell=N(1-\chi).
 \tag{5}
\]
For an arbitrary ordinary polynomial \(f(z)\), define
\[
 g_{n,\chi,f}(t)=
  \sin t\,f(-2\cos t)\exp(inNt^2/(4\pi))\cos(\ell t),
 \qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
 \tag{6}
\]
For every fixed \(H>0\), the exact trace contour is
\[
 \begin{split}
 L_{n,\chi}[f]&=H_{n,\chi}^{H}[f]+V_{n,\chi}^{H}[f],\\
 H_{n,\chi}^{H}[f]&=
 -\frac{N^2C_{N,n}}{\pi i}
       \int_{-\pi-iH}^{\pi-iH}g_{n,\chi,f}(t)W_N(t)\,dt,\\
 V_{n,\chi}^{H}[f]&=
 \frac{\eta N^2C_{N,n}}{\pi}
       \int_{-H}^{H}
       \frac{g_{n,\chi,f}(\pi+ih)}{4\cosh^2(Nh/2)}\,dh .
 \end{split}
 \tag{7}
\]
All local functionals are extended coefficientwise in any other
variables. Heights are fixed, rather than differentiated with respect
to powers or charges.

For completeness, the derivative sampling identity behind (7) is
\[
 L_{n,\chi}[f]=\eta C_{N,n}
       \sum_{j=0}^{N-1}g_{n,\chi,f}'\bigl(\pi(D-2j)/N\bigr).
 \tag{8}
\]
At each double node the two opposite angles give exactly the value
and first-normal terms of \(\phi_N\); at the odd angle zero the term
is \(C_{N,n}f(-2)\). This verifies (8), including \(N=2\), from the
full physical data. The residue proof of (7) then applies without
change: \(g\) is odd and entire, and the double-pole grid kernel has
no boundary pole on the rectangle. It does not require \(\cos(\ell t)\)
to be periodic. Thus (7) holds for all complex \(\chi,n\) as an identity
of entire parameter families, and for the actual integer-power source.

## 2. The paired vertical current

Write
\[
 w_h=2\cosh h,\qquad b=nNh/2,\qquad
 E_n(h)=\exp\{inN(\pi^2-h^2)/(4\pi)\}.
 \tag{9}
\]
The polynomial spectator takes the same value \(f(w_h)\) at
\(t=\pi+ih\) and \(t=\pi-ih\). Directly pairing these two terms gives
\[
 V_{n,\chi}^{H}[f]=\int_0^H \rho_{N,n,\chi}(h)f(w_h)\,dh,
 \tag{10}
\]
where the entire parameter-dependent scalar is
\[
 \begin{split}
 \rho_{N,n,\chi}(h)
 ={}&\frac{2\eta N^2C_{N,n}}{\pi}
       \frac{\sinh h\,E_n(h)}{4\cosh^2(Nh/2)}\\
 &\quad\cdot
 \left\{i\cos(\pi\ell)\cosh(\ell h)\sinh b
             -\sin(\pi\ell)\sinh(\ell h)\cosh b\right\}.
 \end{split}
 \tag{11}
\]
Indeed \(\sin(\pi\pm ih)=\mp i\sinh h\), the Gaussian
multipliers are \(E_n(h)e^{\mp b}\), and
\(\cos(\ell(\pi\pm ih))=\cos(\pi\ell)\cosh(\ell h)
 \mp i\sin(\pi\ell)\sinh(\ell h)\). These identities give both
signs and the factor two in (11).

At a lattice charge \(\chi=J/N\), \(J\in\mathbb Z\), this simplifies to
\[
 \rho_{N,n,J/N}(h)=
 \frac{2i\eta(-1)^{N-J}N^2C_{N,n}}{\pi}
 \frac{\sinh h\,E_n(h)\cosh((N-J)h)\sinh(nNh/2)}
      {4\cosh^2(Nh/2)}.
 \tag{12}
\]
In particular the unit-charge formula has no cosine sign or hyperbolic
charge factor. Also
\[
                 V_{0,J/N}^{H}=0\quad(J\in\mathbb Z).
 \tag{13}
\]
This is an exact full-current identity, not a bound or a value-only
observation. Off the lattice the second term of (11) need not vanish.

For bounded real \(n,\chi\), the direct estimate of (11) gives
\[
 |\rho_{N,n,\chi}(h)|
 \le C N^2\sinh H\,
       \exp\{N(|n|/2+|1-\chi|-1)h\}\quad(0\le h\le H).
 \tag{14}
\]
The constant is uniform in such real parameter boxes. It uses the full
\(4\cosh^2(Nh/2)\) denominator, rather than its first Fourier alias.

## 3. Full traces at all surviving vertices

Let \(G=(V,E)\) be a fixed finite original graph, \(S\subseteq V\)
its selected vertices, and \(B=V\setminus S\) the outside vertices.
There is no restriction on the selected degrees or on the size of
\(S\). The algebra below works for any finite graph with the original
same-index kernel (2), in particular every original circle tree.
Include each edge once. Outside variables remain prescribed or free.

Let \(A_N(\mathbf z)\) be any joint polynomial spectator, independent
of the charges on which the shift operators below act. Parameters
of that spectator can instead be held fixed during the shifts.
Define
\[
 F_G(\mathbf z)=A_N(\mathbf z)\prod_{e=vw\in E}K_N(z_v,z_w),
 \qquad
 Z_{G,N}(\mathbf n,\boldsymbol\chi;\mathbf z_B)
       =\left(\prod_{v\in S}L_{n_v,\chi_v}^{(z_v)}\right)F_G .
 \tag{15}
\]
Choose fixed heights \(H_v>0\) and abbreviate the functionals in (7)
by \(L_v,H_v^{\rm op},V_v^{\rm op}\); the superscript distinguishes
operators from their height parameters.

**Theorem 1 (full-survivor current expansion).** Exactly,
\[
 \prod_{v\in S}L_v
 =\prod_{v\in S}H_v^{\rm op}
   +\sum_{\varnothing\ne C\subseteq S}(-1)^{|C|+1}
       \left(\prod_{v\in C}V_v^{\rm op}\right)
       \left(\prod_{w\in S\setminus C}L_w\right).
 \tag{16}
\]
Consequently every correction to the product of full lower horizontal
contours is an integral with full original traces at every surviving
vertex.

**Proof.** Expand
\(\prod H_v^{\rm op}=\prod(L_v-V_v^{\rm op})\) and rearrange.
Operators in distinct variables commute, even when their common input
contains shared edges and a nonfactorized spectator. Finite integrals
and finite Hermite functionals may be interchanged directly.
\(\square\)

Here is the exact graph content of a term of (16). Put \(Y=S\setminus C\)
and \(G'=G\setminus C\), deleting every edge incident to \(C\), but
retaining every surviving vertex, including isolated selected vertices.
For \(w\in Y\), let \(r_w\) count its edges to \(C\). Set
\[
 \begin{split}
 A_{N,C,\mathbf h}(\mathbf z_{V\setminus C})
       &=A_N(\mathbf w_{\mathbf h},\mathbf z_{V\setminus C}),\\
 Q_{w,N,\mathbf h}(z)
       &=\prod_{\substack{e=vw\\v\in C}}K_N(w_{h_v},z),\\
 D_{C,N}(\mathbf h;\mathbf z_B)
       &=\prod_{\substack{e=vv'\\v,v'\in C}}
                  K_N(w_{h_v},w_{h_{v'}})
          \prod_{\substack{e=vb\\v\in C,\ b\in B}}
                  K_N(w_{h_v},z_b).
 \end{split}
 \tag{17}
\]
Empty products are one. Denote the literal reduced source, with
spectator \(A_{N,C,\mathbf h}\), by \(Z_{G',N}^{A_{C,\mathbf h}}\).
Then the \(C\)-term before its inclusion–exclusion sign is
\[
 \begin{split}
 I_{C,N}={}&
 \int_{\prod_{v\in C}[0,H_v]}
      \left(\prod_{v\in C}\rho_{N,n_v,\chi_v}(h_v)\,dh_v\right)
      D_{C,N}(\mathbf h;\mathbf z_B)\\
 &\quad\cdot
 \left(\prod_{w\in Y}L_{n_w,\chi_w}\right)
 \left[
  A_{N,C,\mathbf h}
  \prod_{e\in E(G')}K_N
  \prod_{w\in Y}Q_{w,N,\mathbf h}(z_w)
 \right].
 \end{split}
 \tag{18}
\]
This follows by (10) in each removed variable. In particular internal
removed edges have not been replaced by one. Several removed vertices
meeting one survivor produce the single product \(Q_w\) at that
survivor; they are not independently traced there. No factorization
of \(A_N\) or of the reduced graph is assumed.

## 4. Exact finite charge convolution

Expand the ordinary polynomial product at each survivor as
\[
 Q_{w,N,\mathbf h}(z)
    =\sum_{k=0}^{r_wD}\beta_{w,k}(\mathbf h)T_k(-z/2).
 \tag{19}
\]
This is an identity before taking any quotient. Define
\[
 (\mathcal S_{w,k}f)(\boldsymbol\chi)
   =\tfrac12\{f(\boldsymbol\chi+(k/N)\mathbf e_w)
                     +f(\boldsymbol\chi-(k/N)\mathbf e_w)\},
 \qquad
 \mathcal B_{w,N,\mathbf h}
    =\sum_{k=0}^{r_wD}\beta_{w,k}(\mathbf h)\mathcal S_{w,k}.
 \tag{20}
\]
For \(r_w=0\) the operator is the identity.

**Theorem 2 (actual reduced-source formula).** The surviving-trace
factor in (18), including all its endpoint coupons, is exactly
\[
             \left(\prod_{w\in Y}\mathcal B_{w,N,\mathbf h}\right)
               Z_{G',N}^{A_{C,\mathbf h}}
                    (\mathbf n_Y,\boldsymbol\chi_Y;\mathbf z_B).
 \tag{21}
\]
All charges here are literal original charge parameters; no source
amplitude is divided out.

**Proof.** In the full physical algebra,
\[
 T_k(-z/2)\mathcal C_{N,\chi}
       =\tfrac12\{\mathcal C_{N,\chi-k/N}
                            +\mathcal C_{N,\chi+k/N}\}.
 \tag{22}
\]
At every positive physical angle this is the cosine product identity.
Differentiating that identity in \(t\), then dividing by \(2\sin t\),
proves the first-normal equality. At the odd simple node both sides
have value one. These are all physical data, proving (22).
Apply (22) to (19) inside the original surviving trace; arbitrary
shared spectators and all other variables stay fixed. Operators in
different charges commute, proving (21). \(\square\)

The identical product identity holds for the finite one-sided coupons
\(Q_{N,\sigma}\), using the two shifted exponentials. It also holds
termwise in any fixed-height angular cosine decomposition because
multiplication by \(\cos(kt)\) gives the same two charge shifts.
These are identities for specified representatives; they do not
remove their connector currents.

In particular lattice charges remain lattice charges throughout
(18)--(21), with no restriction to \(0\le J\le N\). After another
application of (16) in a reduced source, (13) still applies at every
zero-power vertex. The recursion retains the full simple/normal data
even when a shifted charge is zero or leaves the initial unit interval.
An isolated surviving vertex has its actual scalar trace
\(L_{n,\chi}[1]\), or the trace of its retained spectator, rather than
being silently deleted.

## 5. A quantitative estimate in terms of actual reduced sources

We give a bound on real outside colors \(z_b\in[-2,2]\); arbitrary
fixed ordinary outside derivatives obey the same exponential estimate.
The identities (16)--(22) themselves hold for unrestricted free
outside variables.

For \(h_*>0\), define
\[
 \begin{split}
 x_{h_*}&=4-2\cosh h_*,\\
 p(h_*)&=\frac2\pi\int_0^{\pi/2}
     \operatorname{asinh}\!\left(\sinh(h_*/2)\cot y\right)\,dy,\\
 \lambda(h_*)&=\max\{p(h_*),h_*\},\\
 \gamma(h_*)&=\max\{p(h_*)+h_*/2,2h_*\}.
 \end{split}
 \tag{23}
\]
The endpoint theorem proves \(p(h_*)\to0\), indeed
\(p(h_*)=O(h_*\log(1/h_*))\). Its estimates imply, uniformly for
\(0\le h,h'\le h_*\),
\[
 \begin{split}
 \sup_{z\in[-2,2]}|K_N(2\cosh h,z)|
       &\le C_{h_*}N^{a_{h_*}}e^{N\lambda(h_*)},\\
 |K_N(2\cosh h,2\cosh h')|
       &\le C_{h_*}N^{a_{h_*}}e^{N\gamma(h_*)}.
 \end{split}
 \tag{24}
\]
Fixed spectral derivatives on the real outside interval cost only
additional powers of \(N\), by the ordinary polynomial Markov bound.
No fixed-height exponential loss is dropped.

A polynomial \(Q(z)\) of degree at most \(rD\), with real-interval
sup norm \(M\), has Chebyshev coefficients satisfying
\[
       \sum_{k=0}^{rD}|\beta_k|\le(2rD+1)M.
 \tag{25}
\]
This follows from its ordinary cosine coefficient integrals on
\([0,\pi]\), with the constant coefficient counted once. Therefore
(19), with its entire shared product, satisfies
\[
 \sum_k|\beta_{w,k}(\mathbf h)|
       \le C_{G,h_*}N^{a_{G,h_*}}
                    e^{Nr_w\lambda(h_*)}.
 \tag{26}
\]
At the exact height-zero endpoint this sharpens to
\[
 \sum_k|\beta_{w,k}(\mathbf0)|
       \le (2r_wD+1)\{N+m(N-1)\}^{r_w}
       \le C_{r_w}N^{2r_w+1}\quad(r_w>0).
 \tag{27}
\]
There is no exponential loss in (27).

Let \(e_C\) be the number of edges with both endpoints in \(C\), and
\(b_C\) the number with exactly one endpoint in \(C\), including edges
to original outside vertices. For real powers and real charges put
\[
 \begin{split}
 \varepsilon_C(\mathbf H;\mathbf n_C,\boldsymbol\chi_C)
   ={}&e_C\gamma(h_*)+b_C\lambda(h_*)\\
     &+\sum_{v\in C}
       (|n_v|/2+|1-\chi_v|-1)_+H_v,\qquad
               h_*=\max_{v\in C}H_v.
 \end{split}
 \tag{28}
\]
For fixed graph and bounded real power/charge boxes,
\(\varepsilon_C\to0\) as all \(H_v\to0\).

Let \(\mathcal Q_{C,N}\) be the finite set of shifted surviving charges
in (20): in each coordinate with \(r_w>0\) the shift has the form
\(\pm k/N\), \(0\le k\le r_wD\), and the other coordinates are unchanged.
Define the actual reduced-source supremum
\[
 \mathcal M_{C,N}
  =\sup_{\mathbf h\in\prod[0,H_v]}
       \max_{\boldsymbol\chi'\in\mathcal Q_{C,N}}
       |Z_{G',N}^{A_{C,\mathbf h}}
                        (\mathbf n_Y,\boldsymbol\chi';\mathbf z_B)|.
 \tag{29}
\]
When the outside variables vary in a real compact set, take the same
supremum there. For a desired fixed outside derivative, include the
finitely many derivatives of the reduced source up to that order in
(29).

**Theorem 3 (unconditional current reduction bound).** For fixed
positive heights and bounded real powers and charges,
\[
                  |I_{C,N}|
    \le C_{G,\mathbf H}N^{a_{G,\mathbf H}}
       e^{N\varepsilon_C(\mathbf H;\mathbf n_C,\boldsymbol\chi_C)}
                       \mathcal M_{C,N}.
 \tag{30}
\]
The same statement holds for every fixed mixed ordinary outside
derivative with the preceding convention in (29).

**Proof.** The norm of the symmetric shift in (20), relative to the
finite supremum in (29), is at most one. Apply (26) at each survivor.
Its exponent counts the cut edges from \(C\) to \(Y\) once. The second
product in \(D_{C,N}\) contributes the same \(\lambda\) cost on the
remaining cut edges, while its first product contributes \(\gamma\)
on the \(e_C\) internal removed edges. Apply (14) and bound its exponent
on \(0\le h_v\le H_v\) by the positive part in (28). The finite integration
volumes and all prefactors are absorbed in the stated polynomial.
For outside derivatives use the ordinary product rule in (18);
the differentiated cut kernels have the same rate by (24), and the
required surviving-source derivatives were retained in (29).
This proves (30). \(\square\)

This is a bound by actual charged reduced sources, not a bound by the
absolute norm of their unfilled spectators. If \(A_N\) is nonfactorized,
its exact restriction \(A_{C,\mathbf h}\) remains inside those sources.
The constants in (30) may depend on fixed positive heights; no uniform
claim is made when heights shrink with \(N\). The asserted small-height
limit concerns the explicit rate \(\varepsilon_C\).

There is a useful shrinking-height regime with a stronger estimate.
It uses the exact endpoint root disk rather than substituting
\(h_*=O(N^{-1})\) into constants that were proved only at fixed height.

**Corollary 4 (microscopic heights).** Fix \(0<\alpha_0<\pi\), and take
\[
          H_v=\alpha_v/N,\qquad 0<\alpha_v\le\alpha_0.
          \tag{30a}
\]
Let \(q_C=\#\{w\in Y:r_w>0\}\). Uniformly for bounded real powers
and charges, at every level,
\[
 |I_{C,N}|
   \le C_{G,\alpha_0}N^{\,2(e_C+b_C)+q_C}
                 \mathcal M_{C,N}^{\rm mic}.
 \tag{30b}
\]
Here \(\mathcal M_{C,N}^{\rm mic}\) is precisely (29), on the height
box (30a). Constants also depend on the fixed real parameter bounds.
For a fixed outside multi-derivative of order \(|\nu|\), the exponent
of \(N\) in (30b) may be increased by \(2|\nu|\), with the required
reduced-source derivatives included as in (29). No exponential factor
occurs in this bound.

**Proof.** For all sufficiently large \(N\), uniformly in (30a),
\[
 2\cosh h-2\le 2-c_0,\qquad 0\le h\le\alpha_0/N.
 \tag{30c}
\]
Indeed
\(\cosh(\alpha_0/N)+\cos(\pi/N)
=2-(\pi^2-\alpha_0^2)/(2N^2)+O_{\alpha_0}(N^{-4})<2\).
The exact root disk in the endpoint theorem consequently gives
\(|F_{j,N}(2\cosh h)|\le1\). Its cosine interpolation then bounds the
low kernel by \(N\) on the real other color. With that other color
also equal to \(2\cosh h'\), the bound is at most
\(N e^{J h'}\le N e^{\alpha_0/2}\). The full radical estimate gives
\[
 \begin{split}
 \sup_{z\in[-2,2]}|K_N(2\cosh h,z)|&\le C_{\alpha_0}N^2,\\
 |K_N(2\cosh h,2\cosh h')|&\le C_{\alpha_0}N^2
                  \qquad(0\le h,h'\le\alpha_0/N).
 \end{split}
 \tag{30d}
\]
Only finitely many levels were excluded in proving (30c).
Their compact polynomial evaluations can be absorbed into the same
constant in (30d); no root-disk assertion at those levels is needed.

Apply (25) to each whole shared product. For \(r_w>0\),
\[
       \sum_k|\beta_{w,k}(\mathbf h)|
                     \le C_{G,\alpha_0}N^{2r_w+1}.
       \tag{30e}
\]
Each other removed edge in \(D_{C,N}\) costs \(C N^2\) by (30d).
Finally (14), \(\sinh(\alpha_0/N)\le C_{\alpha_0}/N\), and the bounded
real parameter boxes give
\[
        \int_0^{\alpha_v/N}|\rho_{N,n_v,\chi_v}(h)|\,dh\le C
                     \quad(0<\alpha_v\le\alpha_0).
        \tag{30f}
\]
The powers \(N^2\), \(N^{-1}\) from \(\sinh h\), and \(N^{-1}\) from
the integration length cancel. Multiplying (30e), (30d), and (30f)
in (18)--(21) proves (30b). Ordinary outside derivatives of the cut
kernels cost \(N^2\) per derivative by Markov on the whole real
color interval; the other differentiated factors stay in (29).
This proves the derivative statement. \(\square\)

The macroscopic charge shifts in (20) remain in (30b). The improved
height scale removes an exponential operator cost; it does not
replace the shifted reduced sources by their unit-charge value.

## 6. The charge convolution is not local

The shift interval in (20) cannot in general be replaced by an
\(o(1)\) charge interval. This is visible in a coefficient of the
literal original endpoint kernel, rather than in a chosen spectator.

For one cut incidence at height zero write
\[
 B_N(z)=K_N(2,z)=\sum_{k=0}^{D}\beta_kT_k(-z/2).
 \tag{31}
\]
The original sine products satisfy \(S_D=N\) and
\[
 \prod_{a=0}^{N-1}2\sin\frac{(2a+1)\pi}{2N}=2.
\]
Removing the last factor from this product gives
\[
 e_D(2)=\frac{\eta}{N^2\sin^2(\pi/(2N))}.
 \tag{32}
\]
Only the \(e_D(2)e_D(z)\) term contributes to the leading coefficient
of \(B_N\). Since the leading coefficients of \(e_D(z)\) and
\(T_D(-z/2)\) are respectively \(\eta/N^2\) and \(\eta/2\),
\[
                 \beta_D=
             \frac{2\eta}{N^4\sin^2(\pi/(2N))}.
 \tag{33}
\]
At unit charge, (22) therefore includes the two extreme reduced-source
charges
\[
                 \chi=1/N,\qquad \chi=2-1/N,
 \tag{34}
\]
each with the exact coefficient
\[
        \frac{\eta}{N^4\sin^2(\pi/(2N))}
                    \sim\frac{4\eta}{\pi^2N^2}.
 \tag{35}
\]
Thus these shifts have polynomial, not exponential, suppression.
Neither (33) nor (35) asserts that one such contribution dominates;
the coherent sum can cancel them. At the current level the height-zero
density itself vanishes, and no single integration endpoint is being
assigned positive measure. The assertion is the nonlocality of the
exact endpoint operator being integrated.

The classical saturated-face energy identity retains the surviving
charges and imposes a compatibility condition involving the removed
powers and charges. The coupons in (17) do not impose that condition:
at height zero \(B_N(c_j)=K_N(c_j,2)>0\) at every distinct physical node,
so \(B_N\) is a unit in the full physical algebra. Its physical support
is not a projector onto a compatible angle fiber. Consequently neither
(30) nor the polynomial endpoint theorem identifies the shifted
reduced-source maximum with the classical same-charge face action.
The next analytic task is to control this actual coherent convolution,
including its current weights, or prove the needed reduced-source
rate bound on its genuine shifted range.

## 7. Coverage and direct-source readback

The prior one-step Gaussian Ward deletion and its decorated matching
coupons concern a different translated source current. The present
finite inclusion–exclusion identity starts instead from the complete
full-\(\pi\) rectangle (7). It retains its entire vertical weight,
all internal removed edges and all shared boundary products. It
does not invoke square-zero deletion of an off-grid kernel.

All three complete direct sources were read, their used implications
checked, and their hashes verified:

* [Exact complete trace contour](research_exact_complete_trace_contour.md),
  SHA256 a63c66e8078457fa84e8044dc876beca36126348e816de9c6997d2a2610474e8:
  original derivative trace, crossing carrier, full rectangle
  orientation and its exact double-pole vertical kernel.
* [Finite polarized charge source](research_polarized_charge_heat_source.md),
  SHA256 860801dedc3f1093d58c0413f580599512bd2566c00f4a94d0ebf99636343db1:
  original full-Hermite cosine data, canonical real-power extension
  and scalar carrier, and the one-sided coupons used in (22)'s variant.
* [Coherent endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  exact original kernel normalization, full ordinary endpoint/mixed
  derivative bounds, and both-parity small-height estimate with the
  full radical retained.

Only written mathematics, source reads and hashes were used. No
mathematical program, numerical experiment, test or compilation was
run. Adopted notes and public manuscripts are unchanged.
