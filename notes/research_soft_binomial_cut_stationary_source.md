# The actual soft-binomial cut: cycle, action and midpoint critical scheme

Private written proof, 18 November 2026.

The binomial cut has an exact finite-source cycle and a definite
principal boundary action. The latter changes one cut-gluing equation.
Conservation of the full classical coproduct then identifies its
regular principal critical scheme with the braid fixed-point scheme
at the midpoint. This scheme contains the complete geometric
representation for every fixed finite braid of a hyperbolic knot.
The residual geometric centralizer remains.

The complete proof sources are S (the binomial cut), C (the compact
finite coherent calculus), M (the literal braid/holonomy correspondence),
and G (the regular midpoint frame). Their pins are below.
The stationary statement concerns the principal logarithmic equations
of the actual weighted occupation-state array on its regular charts.
Its critical scheme uses the exponentiated rows, retaining their
logarithmic sheets; it does not select an additive Fourier charge.
It does not assert a uniform phase expansion for a growing full
coherent kernel, a sum-to-integral deformation, or a thimble coefficient.

## 1. The full finite array and retained current

Keep the actual braid word, crossing signs, tail pivots and framing.
Put \(d=N-1\), \(c_0=2\pi i\), \(h=c_0/N\), \(Q=e^h\),
\(q=e^{h/2}\), and \(M=-qx\). The letter \(u\) below denotes a
logarithmic occupation, distinct from the quantum square root \(q\).

Let \(C_N(M)\) be the one-cut endomorphism in M's factorial basis.
Its literal state array with cut occupation \(a\), internal states
\(\mathcal I_N(a)\), and full weights \(W_N\) gives
\[
 Z_N(M)=\sum_{a=0}^{d}\pi_{N,a}
       \sum_{\mathbf k\in\mathcal I_N(a)}W_N(a,\mathbf k;M),
 \qquad \pi_{N,a}=2^{-d}\binom da.
 \tag{1}
\]
The inner support, head and transfer inequalities, and every zero
factor are unchanged. S proves the exact whole-meridian identity
\[
 Z_N=\operatorname{Tr}(P_N^{\rm cut}C_N)=F_N,\qquad
 P_N^{\rm cut}=\sum_a\pi_{N,a}T_a.
 \tag{2}
\]
For an arbitrary marked endomorphism \(C\), the comparison is instead
\[
 \operatorname{Tr}((P_N^{\rm cut}-T_0)C)
   =\operatorname{Tr}(B_N^{\rm cut}[C,\mathcal E]),\qquad
 B_N^{\rm cut}=-\sum_{r=0}^{d-1}
    \frac{\Pr(A>r)}{M Q^{-r-1}-M^{-1}}E_{r+1,r}.
 \tag{3}
\]
The marked word, its tail pivot, and all meridian derivatives are
retained on the right. It is not declared zero for arbitrary marks.
The displayed denominators are units on S's shrinking meridian disk.

Both signed crossings conserve integer total occupation. Closing
the other strands forces the cut input and output occupations to
agree in every surviving term, also with diagonal occupation and
transfer marks. Thus (1) has one cut occupation, not two independent
endpoint positions.

## 2. An exact finite cycle and an exactly removable gauge angle

Use C's kernels
\[
 K_A(w,z)=\sum_{i,j=0}^{d}w^iA_{ij}\binom{d}{j}z^j,\qquad
 \sigma_A=K_A/(1+wz)^d.
 \tag{4}
\]
C proves the exact compact sphere composition
\[
 K_{AB}(w,z)=\frac N\pi\int_{\mathbb C}
  \frac{K_A(w,\bar v)K_B(v,z)}{(1+|v|^2)^{N+1}}\,d^2v.
 \tag{5}
\]
The sphere is \(\Gamma=\{w=v,z=\bar v\}\), including infinity,
with C's orientation. Insert (5) between all actual local matrices
and its trace version on closed strands. All factors \(N\), pivots,
head projectors, clocks and framing stay inside the finite network.
S gives the cut functional
\[
 Z_N=\frac1{2\pi i}\oint_{|v|=1}
                     \sigma_{C_N}(v,v^{-1})\,\frac{dv}{v}.
 \tag{6}
\]
Equations (5)--(6) specify the complete finite compact cycle: the
cut latitude circle times the intermediate and closing spheres.
Its resolution measures avoid their coherent pole divisors.
Expanding the finite kernels, the angle and beta integrations in C
recover exactly (1), including every support condition. This is a
whole-array identity before stationarity.

Set \(S_ce_a=c^{-a}e_a\). Integer conservation and the diagonal
physical pivots imply
\[
 [R^\pm,S_c\otimes S_c]=0,\qquad
 [\text{pivot},S_c]=0,\qquad
 \sigma_{S_cAS_c^{-1}}(w,z)=\sigma_A(w/c,cz).
 \tag{7}
\]
Position-preserving marks obey the same rule. For \(|c|=1\), this
rotation preserves each sphere and its measure. In (6), use \(c=v\)
and rotate every intermediate coherent coordinate. The cut becomes
\((1,1)\); all internal gauges cancel by (7). This is an exact
change of variables, and the normalized angle integral is one.
Equivalently, diagonality gives
\[
 \sigma_{C_N}(v,v^{-1})
       =2^{-d}\sum_a\binom da(C_N)_{aa}=\sigma_{C_N}(1,1).
 \tag{8}
\]
For charged Ward insertions the circle and defect (3) remain.
This angle is the common diagonal momentum gauge, not the
geometric centralizer coordinate \(r\).

No geometric-centralizer relative interval has been specified by
(5)--(6). In S's alternative normal-residue presentation the full
normal pole packet, south affine clutch and endpoint current remain.
Equal density endpoint values do not erase its derivative current.

## 3. The principal binomial action from the exact coefficients

The consecutive ratio is exactly
\[
 \frac{\pi_{N,a+1}}{\pi_{N,a}}
       =\frac{d-a}{a+1}
       =\frac{c_0-h-u}{u+h},\qquad u=ha.
 \tag{9}
\]
Near \(u=c_0/2\), choose logarithms by continuation from
\(u/c_0\in(0,1)\), avoiding \(0,c_0\). Its principal logarithm
and normalized primitive are
\[
 g'(u)=\log\frac{c_0-u}{u},\qquad
 g(u)=c_0\left[-\frac u{c_0}\log\frac u{c_0}
 -(1-u/c_0)\log(1-u/c_0)-\log2\right].
 \tag{10}
\]
In particular
\[
 g(c_0/2)=g'(c_0/2)=0,\qquad g''(c_0/2)=-4/c_0\ne0.
 \tag{11}
\]
The constant in (10) is fixed by the original cut normalization.
Indeed a maximal binomial probability lies between \(1/N\) and
one, so its logarithm divided by \(N\) tends to zero. Summing
the logarithms of (9) between that central occupation and any
\(a_N/N\to t\in(0,1)\) gives, on compact subintervals, the Riemann
integral \(\int_{1/2}^t\log((1-y)/y)\,dy\). Hence
\(h\log\pi_{N,a_N}\to g(c_0t)\). The rational ratio fixes its
holomorphic principal continuation on the stated logarithmic chart.
No deformation of the finite state sum was used.

The exact finite mean is \(d/2\), with coordinate \(c_0/2-h/2\).
At even \(N\) the two maximal integer weights flank it. These
finite shifts, parity and all normal corrections remain in (9);
only the principal position is \(c_0/2\).

## 4. The modified cut row and the full localized critical ideal

Work in a regular logarithmic chart of M's literal generating
correspondence. Let \(S_0\) be its leading expression, including
the original Cartan, pivotal and framing contributions. For either
signed crossing M's identities read
\[
 dS_{\rm crossing}
 =\sum_{\rm out}\log p_{\rm out}\,d\log A_{\rm out}
  -\sum_{\rm in}\log p_{\rm in}\,d\log A_{\rm in}
  +\text{external-meridian terms}.
 \tag{12}
\]
For the positive transfer \(C\), the outputs are \(BC,A/C\).
Consequently (12) gives M's derivatives
\(S_a=\log(p_{{\rm out},2}/p_{{\rm in},1})\),
\(S_b=\log(p_{{\rm out},1}/p_{{\rm in},2})\), and
\(S_C=\log(p_{{\rm out},1}/p_{{\rm out},2})\).
The negative crossing has the inverse identities.
M first derives these identities in the old basis. Its exact
factorial change adds the corresponding endpoint primitives to
the generating expression and changes momentum to
\(p_{\rm new}=(1-A)p_{\rm old}\). Thus (12) has the same canonical
form in the factorial basis used in (1). From here on \(p\)
means this new-basis momentum.

The new principal expression is precisely \(S_0+g(u)\).
All internal rows are unchanged. For the single matching cut
position \(A=e^u\), cancellation in (12) gives
\(\partial_uS_0=\log(p_{\rm out}/p_{\rm in})\), with its retained
logarithm branches. Thus the changed exponentiated cut equation is
\[
 \boxed{\displaystyle
       \frac{p_{\rm out}}{p_{\rm in}}
                  =e^{-g'(u)}=\frac{u}{c_0-u}.}
 \tag{13}
\]
The physical pivot on a closed strand is \(x^{1-N}Q^{a(N-1)}\).
Its leading expression is \(c_0(\log A-\log x)\), so its
exponentiated momentum multiplier is one. The writhe term depends
on \(x\). These facts explain why they do not alter (13);
they are not dropped from the source or its meridian derivatives.

It is important to use the entire internal correspondence, not
(13) alone. The ordered classical coproduct has
\[
 K_*=K_1K_{\rm tail},\qquad
 E_*=e_1K_{\rm tail}+E_{\rm tail},\qquad
 F_*=f_1+K_1^{-1}F_{\rm tail}.
 \tag{14}
\]
Both signed maps of M preserve these functions. Direct substitution
in its positive rational map gives
\(K_1'K_2'=K_1K_2\),
\(e_1'K_2'+e_2'=e_1K_2+e_2\), and
\(f_1'+(K_1')^{-1}f_2'=f_1+K_1^{-1}f_2\).
Its negative map is the inverse, proving the same identities.
Iteration gives (14) in the original tensor ordering.

In the canonical-graph ring impose the internal stationary rows,
including closure of the positions and momenta at tensor positions
\(2,\ldots,b\). Their \(K,e,f\) close. Since \(K_{\rm tail}\)
is a unit, (14) first gives \(K_1'=K_1\), then \(e_1'=e_1\),
and finally \(f_1'=f_1\). Hence also \(A_1'=A_1\).
On any chart where either \(1-A_1\) or \(1-x^2/A_1\) is a unit,
the literal formulas
\[
 f_1=(1-A_1)/p_1,\qquad
 e_1=(1-x^2/A_1)p_1/x
 \tag{15}
\]
force \(p_1'=p_1\). The argument is an ideal calculation in the
localized graph ring, not merely a statement about closed points.
Its unit condition holds near \(A_1=-1,M=1\).

Modulo those internal rows, (13) is equivalent to
\(1-u/(c_0-u)=0\). As \(c_0-u\) is a unit, its ideal is
exactly \((u-c_0/2)\). Conversely a full braid fixed point at
\(u=c_0/2\) satisfies every internal row and (13). Therefore
the localized principal stationary ideal equals the full braid
fixed-point ideal plus \((u-c_0/2)\). This conclusion is on the
chosen logarithmic sheet and unit chart. Endpoint/nonunit strata,
for example the simultaneous vanishing at \(A=1,M=1\), are not
included by this localization.

The common momentum remains free. A local classical diagonal gauge
may set \(p_1=p_1'=1\); this is a frame choice, not another equation
forced by (13). M identifies the resulting scheme with the actual
selected-flag knot representation scheme. G gives a regular complete
geometric point for every fixed finite braid of a hyperbolic knot:
\[
 A_{\rm cut}=-1,\qquad p_{\rm in}=p_{\rm out}=1,\qquad
 \mu_{\rm cut}=\begin{pmatrix}-1&2\\-2&3\end{pmatrix}.
 \tag{16}
\]
Thus the actual weighted principal state presentation has this
geometric stationary point, with nondegenerate local five-shape
coordinates. This does not put it on a contributing deformation of
the compact cycle (5)--(6).

## 5. Latitude calibration and the surviving centralizer

C's exact clock symbols are
\(R_\pm(T)=[1+(Q^{\pm1}-1)T]^d\), with \(T=wz/(1+wz)\).
At \(T=1/2\), put \(c_N=\cos(\pi/N)^{N-1}\). Direct substitution
in C's complete finite generator formulas gives
\[
 R_+=-q^{-1}c_N,\quad R_-=-q c_N,\quad \sigma_K=M c_N,
\]
\[
 \sigma_{\mathcal E}
   =v^{-1}[-M q c_N-M^{-1}-(M-M^{-1})2^{-d}],
 \qquad \sigma_F=v(1+q c_N).
 \tag{17}
\]
The vacuum term is explicit. The root upper wall is zero only
after its prescribed specialization; off-root normals must be
taken in C's full formula before that specialization.
As \(N\to\infty\), (17) gives the actual Gauss coordinates
\[
 A=-1,\qquad p=v^{-1},\qquad
 K=M,\quad e=-(M+M^{-1})p,\quad f=2/p.
 \tag{18}
\]
This calibrates the latitude and occupation at principal order.
It is not equality of finite coordinate operators, or a uniform
star-symbol theorem for an arbitrary growing full-word kernel.
Section 4 used M's signed generating correspondence, not the latter.

At completion and \(p=1\), the actual framing is
\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 F^{-1}J_1F=\begin{pmatrix}1+s&-s\\s&1-s\end{pmatrix},
 \qquad A=(1+s)^{-1}.
 \tag{19}
\]
It is independent of \(r\). Left multiplication by
\(J_b=\begin{pmatrix}1&b\\0&1\end{pmatrix}\) changes \(r\) to
\(r+bs\), preserving \(s\). At the midpoint \(s=-2\), this is
a nonzero additive centralizer direction. Common momentum instead
conjugates (19) by \(\operatorname{diag}(p,1)\); it does not
change \(r\). The latitude angle in (17) is this latter gauge.

On the old framed geometric family,
\(u=-\log(1+s)\), so \(du=-ds/(1+s)\) is independent of \(r\).
At the midpoint \(g'=0\), the Hessian changes by
\[
                         g''(c_0/2)\,du\otimes du.
 \tag{20}
\]
The \(r\) direction remains in the full kernel because it is
tangent to the unchanged critical family with \(s=-2\).
After fixing the common momentum, if the old Hessian has exactly
its two framing null directions, (20) removes exactly the one
on which \(du\ne0\). Indeed projection of the new null-vector
equation to the old cokernel first forces \(du=0\), and then
the vector is in the old kernel. The exact corank assertion uses
that old transverse-regularity premise; survival of \(r\) does not.

There is no identification of the latitude circle with an
\(r\)-centralizer relative contour here. The former has the
exact normalized gauge integral one in (8). A nonzero universal
integral along the latter requires a separate relative source map,
including (3), not concentration of (1) or a normal residue.

## 6. Scope and complete proof-source pins

The finite cycle, literal principal boundary action and regular
principal critical scheme are now fixed. The geometric midpoint
is present without an alternating or long-twist hypothesis.
All source walls, pivots, framing and marked currents remain.
Analytic phase/amplitude control of the full coherent network,
the geometric centralizer reduction, its relative cycle and a
nonzero physical geometric coefficient remain unproved.

* S: notes/research_binomial_cut_framing_density.md, SHA256
  4bc6efc595fd6d59c0bc572d83495fb779cff230ff1cb9c14429a0b7c6a2a1b0.
* C: notes/compact_coherent_source_period.md, SHA256
  8c6c3277367a4aa6c69269da635139d5f881f3d3d0d894e04dd97028d76537e4.
* M: notes/marked_braid_holonomy.md, SHA256
  eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.
* G: notes/research_midpoint_geometric_braid_frame.md, SHA256
  9b9756929ac16b9413744ab376ac74718ecbaac645ab0440e3e3a835349b8e30.

All four complete sources were read nontruncated in the author
sequence and their used implications checked. The coefficient action,
conserved-coproduct ideal, finite angle change and framing calculation
are proved above. No external proof is imported from coverage links.
Only written mathematics and text/hash operations were used.
Frozen and public files are unchanged.
