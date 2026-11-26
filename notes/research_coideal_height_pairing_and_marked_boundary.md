# A signed height pairing gives a positive metric with polynomial source costs

24 November 2026. Written research proof.

The actual tensor Krein form, after an explicit half-Cartan twist,
is diagonal in the complete nested coideal frame. Its diagonal
entries are signed cosecants independent of neighboring heights.
Taking the absolute values of this coordinate diagonal gives a
specified positive metric. In that metric the actual crossing
coefficients have their sewn volume rate without additional graph
weight corrections, and both original boundary packets have
polynomial norms.

An original marked cap followed by a crossing between its two legs has a
further exact all-channel formula: a known quadratic phase times
a positive weight between polynomial bounds. This is a boundary
coefficient estimate, not a lower bound for its contraction with
an arbitrary coherent exterior.

## 1. Complete physical conventions and the conserved source channel

Keep the conventions of [S], [T], [K] and [G]:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad c=1+q,\quad F_a=(Q;Q)_a,\quad F_d=N.
 \tag{1}
\]
All fractional powers below mean the displayed exponential branch.
The physical heads \(e_a\), \(0\le a\le d\), are orthonormal. Put
\[
 Ke_a=xQ^{-a}e_a,\quad
 Ee_a=(Q^{-a}-1)e_{a-1},\quad
 Fe_a=(1-Q^{a+1})e_{a+1}.
 \tag{2}
\]
Missing endpoint arrows are zero. The coproducts are
\(\Delta E=E_1K_2+E_2\), \(\Delta F=F_1+K_1^{-1}F_2\).
On any ordered suffix use the actual operator
\[
 B_c^{(b)}=F_*-(E_*-cI)K_*^{-1},\qquad B_c^{(0)}=c.
 \tag{3}
\]
Its roots are simple at this corrected auxiliary parameter:
\[
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)),\quad
 \lambda_r=2\sqrt q\cos\alpha_r,\quad
 \alpha_r=(r+\tfrac12)\pi/N,\quad0\le r<N.
\]
Here \(p_N(B_c^{(b)})=0\), and
\[
 p_N'(\lambda_r)=Nq^{d/2}(-1)^r/\sin\alpha_r.
 \tag{4}
\]
Every actual signed braid commutes with its total coideal.

Write \(\theta=\pi/(2N)\), so \(c=\lambda_0\).
For \(b=2k\) heads, \(k\ge1\), the original source is
\[
 u_0=p^{\otimes k},\quad
 p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\quad
 \ell_{ab}=x^a\mathbf1_{a+b=d}/N,\quad m_{ab}=x^b/N^2,
\]
\[
 \mathcal K_N=\chi_N\ell_0R u_0,\qquad
 \ell_0=\ell_{12}\cdots\ell_{2k-3,2k-2}m_{2k-1,2k}.
 \tag{5}
\]
The marked row has no degree delta. All original exterior factors
remain in \(\chi_N\). Direct endpoint substitution gives
\(E_*u_0=F_*u_0=0\), \(K_*u_0=u_0\), hence \(B_cu_0=cu_0\).
We may therefore restrict the whole word and its observation to
\(\mathcal E_c=\ker(B_c^{(2k)}-cI)\). This is one globally
conserved channel; no projector is inserted between crossings.
All subsequent boundary norms are on this full source channel.
Their dual norms use the restriction of the specified positive form.

## 2. A physical half-Cartan twist of the known Krein form

[R] proves that the actual full crossings preserve the tensor form
\[
 H_Ne_a=qQ^ae_{d-a},\qquad H_N^\dagger=H_N,\quad H_N^2=I.
\]
Use the explicit unrolled square root and its twist
\[
 K^{1/2}e_a=q^{d/2-a}e_a,\qquad
 H'_N=H_NK^{1/2},\qquad
 H'_Ne_a=q^{1+d/2+a}e_{d-a}.
 \tag{6}
\]
Thus \(H'_N\) too is a Hermitian unitary involution.
Write \(A^{\sharp'}=H'_NA^\dagger H'_N\) on one head.
This does not choose a square root separately at each clock node.
The original crossings preserve integer total degree, so commute
with \(K^{1/2}\otimes K^{1/2}\). Consequently every signed word obeys
\[
 R^\dagger(H'_N)^{\otimes b}R=(H'_N)^{\otimes b}.
 \tag{7}
\]
This is an explicit consequence of the already known physical
Krein conservation, not a first conserved-form construction.

At completeness [R]'s raising generator is \(e_x=qE\).
Its head adjoints therefore give
\(E^\sharp=QE\), \(F^\sharp=Q^{-1}F\), \(K^\sharp=K\).
Conjugation by the displayed \(K^{1/2}\) changes these to
\[
 F^{\sharp'}=q^{-1}F,\quad
 E^{\sharp'}=qE,\quad
 (EK^{-1})^{\sharp'}=q^{-1}EK^{-1}.
\]
For any root \(\sigma\), \(\bar\sigma=q^{-1}\sigma\). Thus the
one-head conditional operator satisfies
\[
 (B_\sigma^{(1)})^{\sharp'}=q^{-1}B_\sigma^{(1)}.
 \tag{8}
\]
All these identities include the bottom and top zero arrows.

## 3. Exact signed orthogonality of every height

Use the leading continuants and their eigenvectors
\[
 D_{-1}=0,\quad D_0=1,\quad
 D_{a+1}(\lambda;\sigma)
   =(\lambda+qQ^a\sigma)D_a-q(1-Q^a)^2D_{a-1},
\]
\[
 u_\lambda(\sigma)_a=q^{-a}D_a(\lambda;\sigma)/F_a,\quad
 M_\lambda(\sigma)_a=D_a(\lambda;\sigma)/F_a.
 \tag{9}
\]
The first component of every \(u_\lambda\) is one. Let \(E_d\)
denote the trailing continuant, and
\(L_\lambda=D_d(\lambda;\sigma)/N\). [K] and [S] give
\[
 M_\lambda u_\lambda
    ={p_N'(\lambda)L_\lambda\over q^dN},\quad
 E_d=q^d\overline{D_d},\quad |L_\lambda|=1.
 \tag{10}
\]
The finite polynomial
\(\Phi_{\lambda,\sigma}(z)=\sum_aD_a(\lambda;\sigma)z^a/F_a\)
has degree \(d\), constant term one and all its roots on the
unit circle. Self-inversivity therefore gives, with
\(\varphi_a=D_a(\lambda;\sigma)/F_a\),
\(\bar\varphi_{d-a}=\bar L_\lambda\varphi_a\). Direct multiplication yields
\[
 u_\lambda^\dagger H'_N
     =q^{1+3d/2}\bar L_\lambda M_\lambda.
\]
Equation (8) makes distinct eigenvectors orthogonal; (10) now gives
\[
 \boxed{\quad
 u_{\lambda_r}(\sigma)^\dagger H'_N u_{\lambda_t}(\sigma)
   =\delta_{rt}\,w_r,\qquad
 w_r=(-1)^{r+1}\csc\alpha_r .
 \quad}
 \tag{11}
\]
Indeed the diagonal is \(q^{1+d/2}p_N'(\lambda_r)/N\);
substitute (4) and \(q^{d+1}=-1\).
The signed norm is independent of \(\sigma\).
Write \(U_\sigma\) for the invertible matrix with columns \(u_\lambda(\sigma)\).
This calculation uses every physical coordinate, rather than a
reduced value-only Casimir quotient.

For a width \(b\) choose successive suffix roots
\(\nu_0,\ldots,\nu_{b-1}\), and set \(\nu_b=c\). The exact path vector is
\[
 v_{\boldsymbol\nu}=
   \bigotimes_{j=1}^b u_{\nu_{j-1}}(\nu_j).
 \tag{12}
\]
Tail-up graph elimination gives a basis of all \(N^b\) physical
states, as in [S]. For two different paths choose their deepest
differing height; the next heights agree, so (11) makes that tensor
factor orthogonal. Hence, if \(\Psi\) has these columns,
\[
 \Psi^\dagger(H'_N)^{\otimes b}\Psi
    =\mathcal W,\qquad
 \mathcal W_{\boldsymbol\nu}
    =\prod_{j=0}^{b-1}w_{r_j},\quad \nu_j=\lambda_{r_j}.
 \tag{13}
\]
The external factor \(w_{r_0}\) is included.
On the integer-degree \(kd\) source,
\((K^{1/2})^{\otimes 2k}=1\). Thus this is the old tensor
Krein form there, not a new positive flux for invariant states.
For example the ordinary cup still has signed square zero.

## 4. The specified positive metric and its crossing normalization

Define the positive form by the absolute coordinate diagonal:
\[
 \mathcal D_{\boldsymbol\nu}
      =|\mathcal W_{\boldsymbol\nu}|
      =\prod_{j=0}^{b-1}\csc\alpha_{r_j},\qquad
 G_{\rm ht}=\Psi^{-\dagger}\mathcal D\Psi^{-1}.
 \tag{14}
\]
Thus the paths are orthogonal with the displayed positive norms.
This is not the physical spectral absolute value of
\((H'_N)^{\otimes b}\), which is \(I\). The basis \(\Psi\) is
nonunitary, and its specific coideal definition is part of (14).
It uses no completed-word value or unknown closing coefficient.

This positive metric is admissible in the exponential window.
Indeed \(\|u_\lambda(\sigma)\|_{\rm ph}^2=h_N(\lambda,\sigma)
\le4^d\), so \(\|\Psi\|\le N^{b/2}2^{bd}\).
Since \(|\mathcal W_{\boldsymbol\nu}|\ge1\), (13) gives
\[
 \Psi^{-1}=\mathcal W^{-1}\Psi^\dagger(H'_N)^{\otimes b},
 \qquad \|\Psi^{-1}\|\le\|\Psi\| .
\]
Also \(\|\mathcal D\|\le\csc^b\theta=O_b(N^b)\).
Consequently
\[
 \|G_{\rm ht}^{\pm1}\|\le e^{C_bN},\qquad
                         \|\log G_{\rm ht}\|=O_b(N).
 \tag{15}
\]
Operator norms here are induced physical norms.
The same bounds hold on the conserved external channel.

Let \(R_i\) change only the middle height \(\lambda_r\) to
\(\lambda_{r'}\), with neighboring heights \(\lambda_v,\lambda_s\).
[S] gives the exact phases and, on its explicit compact signed
chambers, one positive amplitude:
\[
 B^+_{r',r}=(-1)^{r'}\sin\alpha_{r'}
       {f_vf_s\over f_{r'}f_r}J_N,\qquad
 B^-_{r',r}=\overline{B^+_{r',r}},\qquad
 f_r=e^{i\pi r(r+1)/(4N)}.
\]
Here \(J_N>0\) eventually and
\(\log J_N=NV_{\rm sew}/\pi+O(\log N)\).
The full original Cartan scalar is included:
\(\kappa q^{d/2}i^{-d}=1\).
Normalizing (12) in (14) multiplies an entry only by
\(\sqrt{\sin\alpha_r/\sin\alpha_{r'}}\). Therefore
\[
 \boxed{\quad
 \widetilde B^+_{r',r}
   =(-1)^{r'}\sqrt{\sin\alpha_r\sin\alpha_{r'}}
           {f_vf_s\over f_{r'}f_r}J_N,\quad
 \widetilde B^-=\overline{\widetilde B^+},\quad
 \log|\widetilde B^\pm|=NV_{\rm sew}/\pi+O(\log N).
 \quad}
 \tag{16}
\]
There are no neighboring \(h_N\)-volume corrections in this metric.
Those in [S]'s physical joint Haar metric were correct for that
different metric; no physical comparison of subexponential size is claimed.

## 5. General ordinary boundary tensors, with their phases

For any actual tail vector \(z_\sigma\) of height \(\sigma\), put
\[
 A_\lambda={N^2q^dx^{-d}\over p_N'(\lambda)}.
\]
The original cup is a Hopf invariant. Its first-head zero coordinate
is \(Nx^{-d}e_d\otimes z_\sigma\). The inverse row from [K] has endpoint
\[
 (U_\sigma^{-1})_{\lambda,d}
   ={E_d(\lambda;\sigma)D_d(\lambda;\sigma)\over Np_N'(\lambda)}
   ={q^dN\over p_N'(\lambda)}.
\]
Graph reconstruction therefore proves
\[
 p_{12}\otimes z_\sigma
   =\sum_\lambda A_\lambda
        u_\sigma(\lambda)\otimes u_\lambda(\sigma)\otimes z_\sigma.
 \tag{17}
\]
This is valid at every tail height; \(|A_{\lambda_r}|=N\sin\alpha_r\).

The ordinary cap coefficient is
\[
 t_{\eta,\lambda,\sigma}
 =\ell[u_\eta(\lambda)\otimes u_\lambda(\sigma)]
 ={q^{-d}\over N}\sum_{a=0}^d
 {x^aD_a(\eta;\lambda)D_{d-a}(\lambda;\sigma)\over F_aF_{d-a}}.
\]
As a polynomial in \(\eta\), it has degree at most \(d\) and
leading coefficient \(q^{-d}x^d/N^2\), independent of \(\lambda,\sigma\).
Hopf intertwining annihilates it at every root \(\eta\ne\sigma\).
Lagrange uniqueness, without dividing an ordinary bubble, gives
\[
 \boxed{\quad t_{\eta,\lambda,\sigma}
      =\delta_{\eta,\sigma}\,{q^{-d}x^dp_N'(\sigma)\over N^2}
      =\delta_{\eta,\sigma}/A_\sigma .\quad}
 \tag{18}
\]
These identities include \(N=2\) and every level parity.
They retain the actual pivot and the full finite support.
In particular an ordinary cup-cap bubble can vanish by the sum
of the \(A_\lambda\); it has not been normalized to one.

These general formulas also control genuine ordinary turns on
arbitrary tail sectors. Inserting a cup adds the two weights
\(\csc\alpha_\sigma\csc\alpha_\lambda\) to the old tail weight.
The exact sector map norms are therefore
\[
 \|\operatorname{Cup}_\sigma\|^2
       =N^2\csc\theta\csc\alpha_\sigma,\qquad
 \|\operatorname{Cap}_\sigma\|^2
       =N^{-2}\csc\theta\csc\alpha_\sigma .
 \tag{18a}
\]
The sine sum used below proves both identities directly from (17)--(18).
Uniformly the ordinary cup has norm at most \(N\csc\theta=O(N^2)\),
and the cap at most \(\csc\theta/N=O(1)\).
The rank-one middle-height factor of their cup-cap composition has norm
\(\csc\theta\csc\alpha_\sigma\); no positive bubble is substituted.

## 6. The full marked tensor and the original boundary norms

The unrestricted original marked row factors exactly:
\[
 m[u_\eta(\lambda)\otimes u_\lambda(\sigma)]
   ={1\over N^2}\Phi_{\eta,\lambda}(q^{-1})
                         \Phi_{\lambda,\sigma}(-q^{-2}).
 \tag{19}
\]
Write \(m_{\eta,\lambda,\sigma}\) for this coefficient.
There is no height delta in this formula.
For outer and deeper height \(c\), [G] instead gives the useful
full graph-row identity \(mL_c=h/N\), \(h_a=x^a\).
Directly \(hB_c^{(1)}=\mu_*h\), where
\[
 \mu_*=-q^{-1}-q^2=\lambda_{N-2},\qquad
 \alpha_*=\pi-3\theta,\quad s_*=\sin\alpha_*=\sin3\theta.
\]
The recurrence or reciprocity gives
\(D_a(\mu_*;c)/F_a=x^a\). Hence
\[
 m_{c,\lambda,c}=\delta_{\lambda,\mu_*}\,T_*,
 \qquad
 T_*={2\over N(1-q^{-3})}
     ={x^dp_N'(\mu_*)\over q^dN^2}.
 \tag{20}
\]
For example \(h u_{\mu_*}(c)=\sum_{a=0}^dq^{-3a}
=2/(1-q^{-3})\). No denominator vanishes for \(N\ge2\).

On the external channel \(\nu_0=c\), (17) expands the actual
\(u_0\) with even heights \(\nu_{2j}=c\) and odd coefficients
\(\prod_{j=1}^k A_{\nu_{2j-1}}\).
The literal LAST-mark row in (5), by repeated (18) and then (20), is
\[
 \ell_0(v_{\boldsymbol\nu})
  =A_c^{-(k-1)}T_*
       \prod_{j=1}^{k-1}\delta_{\nu_{2j},c}\,
                         \delta_{\nu_{2k-1},\mu_*}.
 \tag{21}
\]
This proves the original ordering directly. It needs no mark relocation.
Other individual marked rows need not agree on arbitrary channels;
the already proved relocation on actual regular invariant sources
retains precisely that narrower scope.

Use \(\sum_{r=0}^d\sin\alpha_r=\csc\theta\), obtained by summing
the finite geometric progression. The outer \(c\) factor in (14)
is retained. Equations (17)--(21) give the exact source norms
\[
 \boxed{\quad
 \|u_0\|_{G_{\rm ht}}^2=(N^2\csc^2\theta)^k,\qquad
 \|\ell_0|_{\mathcal E_c}\|_{G_{\rm ht}^{-1}}^2
   ={1\over(N^2\sin^2\theta)^{k-1}}\,
                      {\sin\theta\over N^2s_*}.
 \quad}
 \tag{22}
\]
For the second formula the reciprocal path weight on its support is
\(\sin^k\theta\,s_*\prod_{j<k}\sin\alpha_{\nu_{2j-1}}\).
Sum the \(k-1\) free odd heights and use the displayed sine sum.
The remaining factors are \(|A_c|^{-2k+2}|T_*|^2\), proving (22).
Since \(\sin\theta\le s_*\le3\sin\theta\), these are polynomial
at every fixed width, and \(\|\ell_0|_{\mathcal E_c}\|=\Theta_k(N^{-1})\).
Multiplying by \(|\chi_N|\) restores any external scalar in the row.
The claim is not a bound for the unrestricted marked row on all
external heights of the full physical tensor space.

## 7. One signed crossing between the legs of the marked pair

The following is an all-channel row identity, before estimating
any adjoining coherent exterior. The crossing is between the two
legs of the marked pair, with outer and deeper heights \(c\). Put
\[
 b^\pm_\lambda=(mR^\pm)
       [u_c(\lambda)\otimes u_\lambda(c)].
\]
The phase-exact reduced crossing sends
\(u_\lambda(c)\) to \(\kappa\,\overline{D_a(\lambda;c)/F_a}\)
in coordinate \(a\). The graph row \(h/N\) thus gives
\[
 b^+_\lambda={\kappa\over N}
                     \overline{\Phi_{\lambda,c}(-q)}.
 \tag{23}
\]
For \(\lambda=\mu_j\), (4) of [S] gives
\[
 \Phi_{\lambda,c}(-q)=(Q;Q)_A(q^3;Q)_B,\quad B=d-A,\quad
 A=\begin{cases}[\lfloor N/2\rfloor-j]_N,&N\ {\rm even},\\
                 [\lfloor N/2\rfloor+j]_N,&N\ {\rm odd}.
   \end{cases}
\]
Every sine half-angle in this product is in \((0,\pi)\).
Its exact phase and positive magnitude are therefore
\[
 b^+_\lambda=\eta_{N,A}W_{N,A},\quad
 \eta_{N,A}=\kappa i^dq^{-[A(A+1)+B(B+2)]/2},\quad
 W_{N,A}={R_A\over N\sin\theta},\quad
 R_A=\prod_{h=1}^A{\sin(h\pi/N)\over\sin((h-\tfrac12)\pi/N)}.
 \tag{24}
\]
The half-grid sine product is \(2\); reflection of its omitted
last \(A\) factors proves the formula for \(W\).
The ratio \(R_A/R_{A-1}\) crosses one only once, so \(R_A\)
is unimodal. Its endpoints are \(1\) and \(N\sin\theta\ge1\).
Moreover \(\sin t/t\) decreases on \((0,\pi)\), so
\[
 R_A\le\prod_{h=1}^A{h\over h-\tfrac12}
       \le C\sqrt{A+1}\le C\sqrt N .
\]
The middle inequality follows by taking logarithms and using
\(\sum_{h=1}^A(2h-1)^{-1}\le\tfrac12\log(A+1)+C\).
Thus, with universal constants,
\[
                       2/\pi\le W_{N,A}\le C\sqrt N .
 \tag{25}
\]
This lower bound is for every actual channel, not just a largest mode.

The boundary phase is the same height chirp already present in [S].
For sorted \(\lambda=\lambda_r\), its physical root permutation gives
\(2A=N-\tfrac12+(-1)^{N+r}(r+\tfrac12)\).
Substitute this in the quadratic exponent of (24):
\[
 \eta_{N,A}=\zeta_N f_r^{-1},\qquad
 \zeta_N=i^dq^{d(N-4)/4}.
 \tag{26}
\]
All quarter powers are the stated exponential branches.
For \(r=N-2\), \(A=d\), \(W=1\), and \(b^+=\kappa\).

The graph eigen-row \(h/N\) annihilates all but \(\mu_*\) before the
crossing. Since [S] proves \(B^-=\overline{B^+}\) entrywise in
this same frame, (20) gives the exact negative row
\[
 b^-_\lambda={T_*\over\bar T_*}\,\overline{b^+_\lambda}
             =-q^3\overline{b^+_\lambda}.
 \tag{27}
\]
No free flip or reversal of the original marked ordering is used.

In the positive metric the two-head path norm is
\(\csc\theta\,\csc\alpha_r\), not \(h_N(c,\lambda)^2\).
Its normalized boundary coefficient is therefore
\[
 \widehat b^\pm_r=b^\pm_r\sqrt{\sin\theta\sin\alpha_r},
 \qquad
 \boxed{\quad c_0/N\le|\widehat b^\pm_r|\le C_0
                 \quad(N\ge2,\ 0\le r<N).\quad}
 \tag{28}
\]
Use (25), \(\sin\alpha_r\ge\sin\theta\ge1/N\), and
\(\sin\theta\le\pi/(2N)\). The constants are universal.
Ordinary caps on the other pairs multiply the exact tensor (21).
In particular the same statement applies to a crossing on the
literal final marked pair, retaining all earlier ordinary caps.
It is not necessary to move that mark across an arbitrary exterior.
There is also an actual row-norm bound, with that crossing included:
\[
 \|\ell_0R_{2k-1}^{\pm}|_{\mathcal E_c}\|_{G_{\rm ht}^{-1}}^2
  ={\,\sin\theta\sum_r W_{N,A(r)}^2\sin\alpha_r\over
                              (N^2\sin^2\theta)^{k-1}},
 \qquad
 c_k\le\|\ell_0R_{2k-1}^{\pm}|_{\mathcal E_c}\|_{G_{\rm ht}^{-1}}
                                                    \le C_k\sqrt N .
 \tag{29}
\]
For the lower bound use \(W\ge2/\pi\), and for the upper use
\(W^2\le CN\); the same exact sine sum proves both.
These are norms of the unscaled original row. An included
\(\chi_N\) multiplies them by \(|\chi_N|\), which is not declared polynomial.

## 8. What has been simplified

This explicit positive path metric has polynomial original input
and marked-output costs on the globally conserved source channel.
Its local signed crossing rate is the sewn-cell volume itself,
without the neighboring graph-weight corrections of the physical
joint Haar metric. The marked cap followed by a crossing between its two legs
has nonzero polynomially bounded coefficients in every channel,
with an explicit single-height quadratic phase. These are actual
source-dependent normalization and boundary estimates.
The boundary statement is a row on all graph exteriors in
\(\mathcal E_c\), not a new terminal-curl survival statement on
saturated regular invariant sources.

They do not make the original observation positive. The signed
pairing (13) is still indefinite; the ordinary cup source and its
actual braid images remain isotropic. Taking its absolute coordinate
diagonal changes the norm, not that algebraic fact.
A row with all nonzero coefficients
can annihilate a coherent exterior vector. The phases in (16),
(24) and (27), unselected height channels, and the full marked
functional remain in a whole component.
No arbitrary short-word scalar lower bound or finite-exception
volume theorem follows.

The construction is on the full \(N^b\)-dimensional physical head
space and its complete external channel. It does not silently reuse
the \(N\)-dimensional Conway packet budgets in another compiler.
Any quartic or capacity implementation must retain these actual
spaces, measures, positive metrics and known normalization factors.

[G] already supplies polynomial marked-row bounds in a different
graph metric and retains the source-selected reduction. [R] already
proves physical Krein conservation and its meridian-jet extensions.
[P] already proves coherent ordinary-cap simplifications and keeps
the unrestricted marked packet. The additions here are the exact
height diagonal of a specified physical Krein twist, its explicit
positive absolute-diagonal metric with both original boundary norms,
and the all-channel marked-cap/crossing product and bounds.
No first polynomial boundary frame or new general positivity
principle is claimed.

## Complete proof inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| S | [Signed coideal chamber](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| T | [Exact crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| G | [Graph Gram and local volume](research_coideal_graph_gram_and_octahedral_volume.md) | 398 | 35ca803fb3262b1f85a08c3aa9b9112bcc2823ce380ce82362ef18bd382d6766 |
| R | [Physical real-meridian Krein form](research_real_meridian_krein_transport.md) | 310 | caf18090cb75a0527ffccdf4a3217fe422876d683271eda8e3e6d591259e92dc |
| P | [Ordinary and marked cap reassociation](actual_pivotal_cap_reassociation_angle_packet.md) | 243 | c822bbcc34b86c600f291f7e66c210253f341319a9d92007fcc51e6633424b14 |

Only written mathematics and text/hash operations were used.
Earlier final notes, the progress ledger and public manuscripts
remain unchanged.
