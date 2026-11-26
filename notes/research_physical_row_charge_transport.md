# Positive physical-row charge transport and endpoint-window stability

Private written proof, 16 November 2026.

An original kernel evaluated at a physical color of index \(a\)
has a positive Fourier law supported on \([-a,a]\). Inside a
surviving full trace, this is an exact positive convolution of
the original charge parameter. Its coefficient mass costs
\(O(a\log(N/a))\), and its charge shifts cost \(a/N\).
This gives a quantitative endpoint-window stability lemma for
any supplied uniform charged descendant estimate. It does not
supply that estimate or an arbitrary-short-filling theorem.

## 1. The actual physical row and its positive law

Put \(D=N-1\), \(J=\lfloor D/2\rfloor\), \(\theta=\pi/N\),
\(\eta=(-1)^D\), and
\[
 c_a=2\cos((2a+1)\theta),\quad
 s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^j s_h,\quad
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z).
 \tag{1}
\]
Retain the ordinary kernel \(K_N(w,z)=\sum_{j=0}^D e_j(w)e_j(z)\)
and the original physical row
\[
 F_{a,N}(z)=K_N(c_a,z),\qquad 0\le a\le J.
\]
The endpoint source proves the exact formula and root location
\[
 F_{a,N}(z)=
 \sum_{k=0}^a
   \frac{S_{a+k}}{S_{a-k}S_k^4}\prod_{h<k}(c_h-z)
 =\prod_{\nu=1}^a
       \frac{r_{a,\nu}-z}{r_{a,\nu}-c_0},
 \qquad r_{a,\nu}>2.
 \tag{2}
\]
An empty product is one. Define \(M_{a,N}=F_{a,N}(-2)\).
For independent variables \(X_\nu\in\{-1,0,1\}\) with
\[
 \Pr(X_\nu=0)=\frac{r_{a,\nu}}{r_{a,\nu}+2},\qquad
 \Pr(X_\nu=1)=\Pr(X_\nu=-1)=\frac1{r_{a,\nu}+2},
 \quad K_a=\sum_{\nu=1}^aX_\nu,
 \tag{3}
\]
one has the exact entire angular identity
\[
 \boxed{\quad
 F_{a,N}(-2\cos t)=M_{a,N}\,\mathbb E(e^{iK_at})
                 =M_{a,N}\,\mathbb E(\cos K_at).
 \quad}
 \tag{4}
\]
Indeed each normalized factor in (2) is
\((r_{a,\nu}+e^{it}+e^{-it})/(r_{a,\nu}+2)\).
This is a finite probability law, not a new inner product or
a probabilistic assumption on the quantum source. It is symmetric,
supported on \([-a,a]\), and
\[
 \mathbb E K_a=0,\qquad
        \operatorname{Var}K_a
            =\sum_{\nu=1}^a\frac2{r_{a,\nu}+2}\le a/2.
 \tag{5}
\]
Equivalently \(F_{a,N}(-2\cos t)=\sum_{k=0}^a\beta_{a,k}\cos(kt)\)
with \(\beta_{a,k}\ge0\) and \(\sum_k\beta_{a,k}=M_{a,N}\).
Products of physical rows convolve these laws; their masses
multiply and their support bounds add.

Let \(\mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)\).
Its original closing is
\(\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{\,2T_N(z/2)+2}f\).
The canonical coupon \(\mathcal C_{N,\chi}\) has the full
Hermite data of \(\cos(N(1-\chi)t)\) at
\(z=-2\cos t\), with value one at the odd simple node.
Equation (4) implies, in this full physical algebra,
\[
 \boxed{\quad
 F_{a,N}\mathcal C_{N,\chi}
          =M_{a,N}\,\mathbb E\mathcal C_{N,\chi-K_a/N}.
 \quad}
 \tag{6}
\]
To verify every normal, multiply (4) by
\(\cos(N(1-\chi)t)\). Symmetry of \(K_a\) turns the product
into \(\mathbb E\cos((N(1-\chi)+K_a)t)\).
This entire angular identity can be differentiated and divided
by \(2\sin t\) at every positive physical angle. At the odd
simple node \(t=0\), both sides have value \(M_{a,N}\).
These are all the physical data. Thus (6) holds for every
complex \(\chi\), retaining the original full normal.
It is not asserted as an ordinary polynomial identity for
arbitrary complex charge.

## 2. A uniform coefficient-mass bound

For \(a=0\), \(M_{0,N}=1\). For \(1\le a\le J\),
\[
 \boxed{\quad
 1\le M_{a,N}
 \le(a+1)\left[\frac{\pi^2e^4}{4}
                       \left(\frac Na\right)^2\right]^a .
 \quad}
 \tag{7}
\]
In particular, if \(C_0=\pi e^2/2\),
\[
 \log M_{a,N}\le\log(a+1)+2a\log(C_0N/a).
 \tag{8}
\]

*Proof.* The terms of (2) at \(-2\) are nonnegative.
For \(k\le a\le N/2\), use
\[
 S_{a+k}/S_{a-k}
       \le(2\pi/N)^{2k}\frac{(a+k)!}{(a-k)!},
 \quad S_k\ge(4/N)^k k!,\quad
              \prod_{h<k}(c_h+2)\le4^k.
\]
The \(k\)-th term is at most
\[
 \left(\frac{\pi^2N^2}{16}\right)^k
       \frac{(a+k)!}{(a-k)!(k!)^4}
 \le \frac{[(\pi^2/4)N^2a^2]^k}{(k!)^4}.
 \tag{9}
\]
The final upper sequence increases for \(0\le k\le a\):
the ratio of consecutive terms is at least
\(\pi^2N^2/(4a^2)\ge\pi^2>1\).
The inequality \(a!\ge(a/e)^a\), obtained by integrating
\(\log x\), bounds its last term by the power in (7).
Summing \(a+1\) terms proves the result. The lower bound follows
already from the \(k=0\) term. \(\square\)

The root product also gives
\[
 \sup_{z\in[-2,2]}|F_{a,N}(z)|=M_{a,N}.
 \tag{10}
\]
All fixed spectral derivatives on this interval cost at most
a fixed power of \(a+1\), by the polynomial Markov estimate
used in the endpoint source. This is consistent with (6),
which already retains the normals exactly.

For \(0<\varepsilon<1/2\) and \(a\le\varepsilon N\), monotonicity
of \(x\log(C_0/x)\) on this interval gives
\[
 M_{a,N}\le N\exp\{N h(\varepsilon)\},\qquad
 h(\varepsilon)=2\varepsilon\log(C_0/\varepsilon)
                          \longrightarrow0.
 \tag{11}
\]
Consequently any uniform \(a=o(N)\) window has subexponential
mass and charge support \(o(1)\). A statement at one descendant
charge alone is not made uniform by this observation.

## 3. Exact transport of a shared graph source

Fix a finite original circle tree, a nonempty traced set \(S\), and a
set \(U\subseteq S\) of evaluated physical vertices.
Let \(Y=S\setminus U\). Set \(z_v=c_{a_v}\) for \(v\in U\).
Every original edge is retained. Every untraced outside color
is complete, \(z_b=-2\), for the estimates below.
The algebraic formula also permits free outside colors, with
their literal row polynomials left unevaluated.

Let \(A_N(\mathbf z)\) be any joint polynomial spectator,
including any additional fixed coupons. Write \(A_{N,\mathbf a}\)
for its evaluation at \(U\). Keep the original crossing
elements \(R_{n_w}\), their scalar carriers, and the original
full trace at every \(w\in Y\).
At a survivor define the entire shared cut-row product
\[
 p_w(z)=\prod_{\substack{v\in U\\vw\in E}}F_{a_v,N}(z),
 \quad M_w=p_w(-2),\quad
 A_w=\sum_{\substack{v\in U\\vw\in E}}a_v.
 \tag{12}
\]
By (4), \(p_w(-2\cos t)=M_w\mathbb E(e^{iK_wt})\), with a
symmetric law supported on \([-A_w,A_w]\).
These finite auxiliary laws may be taken independent for
different surviving vertices.

Let \(G'\) retain only edges with neither endpoint in \(U\).
Denote its actual full traced source with spectator
\(A_{N,\mathbf a}\) by
\(Z_{G',N}^{A_{N,\mathbf a}}(\mathbf n_Y,\boldsymbol\chi_Y)\).
This includes all original surviving kernels and other insertions.
Define the literal evaluated-edge factor
\[
 D_U(\mathbf a)=
 \prod_{\substack{vw\in E\\v,w\in U}}K_N(c_{a_v},c_{a_w})
 \prod_{\substack{vb\in E\\v\in U,\ b\notin S}}F_{a_v,N}(-2).
 \tag{13}
\]
For free outside colors, replace the corresponding factors
in the second product by \(F_{a_v,N}(z_b)\); do not assign
them a charge or a trace.

Let \(\mathscr R_U(\mathbf a)\) be the original surviving
contraction with these evaluated colors, including all factors
(12)--(13), but with the evaluated vertices' crossing values
kept separately. Applying (6) at each survivor gives exactly
\[
 \boxed{\quad
 \mathscr R_U(\mathbf a)=D_U(\mathbf a)
       \left(\prod_{w\in Y}M_w\right)
       \mathbb E\!\left[
          Z_{G',N}^{A_{N,\mathbf a}}
           (\mathbf n_Y,\boldsymbol\chi_Y-\mathbf K/N)\right].
 \quad}
 \tag{14}
\]
There is no independence assumption on the graph spectator.
Only the finite coefficient laws are independent; every shared
edge and all coherent sums remain inside the descendant source.
In particular internal \(U\)-edges remain the factors in (13),
and no normal at a surviving vertex is removed.

For complete outside colors every factor outside the expectation
is positive. If \(d_v\) is the original degree of \(v\), then
\[
 D_U(\mathbf a)\prod_wM_w
                         \le\prod_{v\in U}M_{a_v,N}^{d_v}.
 \tag{15}
\]
Indeed a cut or outside incidence contributes precisely \(M_{a_v,N}\).
An internal \(U\)-edge obeys
\(0<K_N(c_a,c_b)\le\min(M_{a,N},M_{b,N})
 \le M_{a,N}M_{b,N}\), by (2) and (10).
Counting both original endpoints proves (15).
With \(d_U=\sum_{v\in U}d_v\), (11) yields
\[
 D_U\prod_wM_w\le N^{d_U}e^{Nd_Uh(\varepsilon)}
                    \quad\hbox{if all }a_v\le\varepsilon N.
 \tag{16}
\]
The charge shifts in (14) satisfy
\[
 |K_w|/N\le A_w/N\le d\,\varepsilon,\qquad
                      d=\max_{v\in S}d_v.
 \tag{17}
\]
At unit readout one can say more without an estimate.
The exact full-Hermite identity
\(\mathcal C_{N,1+u}=\mathcal C_{N,1-u}\) implies that (14)
is unchanged if \(1-K_w/N\) is replaced by \(1-|K_w|/N\)
in each descendant coordinate. Thus only below-unit lattice
charges in \([1-d\varepsilon,1]\) are used.

## 4. A usable endpoint-window lemma

Consider the omitted-row source of the adopted outer-row theorem.
At each \(v\in U\) its exact weight is \(\Omega_{v,a_v}\), allowing
a fixed number of shared microscopic endpoint coupons with
\(|\alpha|\le A<\pi\). All the other original factors are as
in (14). In particular
\[
 |\Omega_{v,a_v}|\le C N^{3/2}.
 \tag{18}
\]
Start with unit charge at every traced vertex, and retain
the original integer powers. Restrict the exact row sum to
\(0\le a_v\le\varepsilon N\), also respecting its original
tail support. Call that restricted contribution \(T_{U,N}^\varepsilon\).

**Endpoint-window lemma.** Suppose there are \(r_0,\Delta>0\),
a reference rate \(M\), and constants \(C,p\) such that the
actual descendant sources in (14) satisfy
\[
 \left|Z_{G',N}^{A_{N,\mathbf a}}
       (\mathbf n_Y,\boldsymbol\chi)\right|
       \le C N^p e^{N(M-\Delta)}
 \quad\text{for }\chi_w\in(1+N^{-1}\mathbb Z)\cap[1-r_0,1],
 \tag{19}
\]
uniformly over all physical parameters \(\mathbf a\) in the
indicated window and all retained insertions. Then, whenever
\(d\varepsilon\le r_0\),
\[
 |T_{U,N}^\varepsilon|
    \le C' N^{p+d_U+(5/2)|U|}
           e^{N[M-\Delta+d_Uh(\varepsilon)]}.
 \tag{20}
\]
In particular a fixed sufficiently small \(\varepsilon>0\)
preserves half the supplied margin:
\[
 d_Uh(\varepsilon)\le\Delta/2
 \quad\Longrightarrow\quad
 |T_{U,N}^\varepsilon|\le C' N^{p'}
                                      e^{N(M-\Delta/2)}.
 \tag{21}
\]
The same choice can serve the finitely many evaluated subsets
of a fixed graph, if (19) holds uniformly for them.

*Proof.* Apply the exact unit-charge reflection after (17).
Equation (14) then evaluates the source only at the lattice
charge window in (19). The expectation has total mass one, so (19)
bounds it without replacing the descendant by a physical norm.
Apply (16), multiply by (18), and sum at most \(N^{|U|}\)
physical assignments. The original evaluated crossing values
have modulus one at real, in particular integer, powers.
This proves (20); \(h(\varepsilon)\to0\) proves (21).
\(\square\)

This is a stability input for an induction whose descendant
estimates are already available uniformly in charge. It does
not infer (19) from a bound known only at \(\boldsymbol\chi=\mathbf1\),
from classical action concavity, or from a nonzero boundary state.
Other endpoint windows and vertical currents remain.

## 5. The retained integer phase and the limit of absolute estimates

The original crossing convention is
\[
 R_n(c_a)=C_{N,n}\exp\{inN\tau_a^2/(4\pi)\},\qquad
 C_{N,n}=\exp\{\pi inD^2/(4N)\},\quad
 \tau_a=\pi-\frac{2\pi(a+1/2)}N.
 \tag{22}
\]
Combining its value with the exact tail character gives
\[
 (-1)^aR_n(c_a)
   =\kappa_{N,n}
       \exp\{i\pi(1-n)a+i\pi n(a+1/2)^2/N\},\qquad
 \kappa_{N,n}=C_{N,n}e^{i\pi n(N-2)/4}.
 \tag{23}
\]
The scalar has modulus one for real \(n\). For odd integer \(n\)
the linear character is one; for even integer \(n\) it is
\((-1)^a\). The quadratic phase remains in both cases.
For a shared product, each summand of its exact weight retains
this character; its other physical row factors are unchanged.
No integer-only identity has been differentiated in \(n\).

The coefficient cost cannot generally be made subexponential
on a fixed macroscopic endpoint window by using the Gaussian
tail penalty alone. Here is an actual-kernel verification.
Fix \(0<\delta<1/2\), take \(\alpha=0\),
\(L=\lfloor\delta N\rfloor\), and let
\(a_N/N\to x\in(0,1/2-\delta)\). The exact tail products in the
outer-row source have a common sign and give
\[
 \lim_{N\to\infty}\frac1N\log|\omega_{a_N,N,L}(0)|
       =-J_\delta(x),\qquad
 J_\delta(x)=
 -\int_0^\delta
       \log\left(1-\frac{\sin^2(\pi x)}{\cos^2(\pi u)}\right)du.
 \tag{24}
\]
To prove the limit, the first retained product has length \(L+1\).
Its logarithm divided by \(N\) converges to the displayed integral:
all factors on that interval are strictly positive and bounded
away from zero. Through physical termination, every subsequent
ratio is at most some \(q_x<1\) for all large \(N\), because its
limit is
\((\cos^2(\pi x)-v)/(1-v)\le\cos^2(\pi x)<1\).
Its denominators stay away from zero since \(x>0\).
Thus the whole tail is between its first positive term and
a constant times that term. The nonzero base factor contributes
only \(O(\log N)\) to its logarithm. This proves (24) at both parities.
Expansion at \(x=0\), uniformly on the fixed \(u\)-interval, yields
\[
                 J_\delta(x)=\pi\tan(\pi\delta)x^2+O(x^4).
 \tag{25}
\]

In contrast, the positive \(k=a\) term of the actual row (2) gives
\[
 \liminf_{N\to\infty}\frac1N\log M_{a_N,N}\ge m(x),
\]
\[
 m(x)=
 \int_0^{2x}\log(2\sin\pi u)\,du
 -4\int_0^x\log(2\sin\pi u)\,du
 +\int_0^x\log(4\cos^2\pi u)\,du.
 \tag{26}
\]
These Riemann-sum limits follow by separating the integrable
\(\log u\) singularity at zero; its factorial sum has
\(O(\log N)\) error. The cosine product uses its literal
midpoint arguments. In particular
\[
                         m(x)=2x\log(1/x)+O(x).
 \tag{27}
\]
Equations (25)--(27) show that, for sufficiently small fixed
\(x>0\),
\[
 \liminf_{N\to\infty}N^{-1}
       \log\bigl(|\omega_{a_N,N,L}(0)|F_{a_N,N}(-2)\bigr)>0.
 \tag{28}
\]
The second factor is a literal complete outside incidence,
not an arbitrary test polynomial.
Thus this positive coefficient expansion is not a uniformly
subexponential absolute contraction to an undeformed deleted rate
on fixed macroscopic windows. Equation (28) does not rule out
coherent cancellation in the row sum, a sufficiently large
supplied action gap, or every possible filled-action estimate.
The small-window lemma explicitly shows how a positive margin
can absorb the cost. The original phase (23) and paired
vertical currents remain relevant beyond that argument.

## 6. Coverage and direct sources

The following earlier constructions were checked for overlap:
[the complete-source Pick observation](research_complete_source_pick_observation.md)
treats a Cauchy observation of the complete row;
[the entropy Fourier embedding](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_entropy_circle_fourier_embedding.md)
represents a classical entropy defect;
[the shared-cycle Fourier compiler](actual_matching_graph_shared_cycle_fourier_compiler.md)
uses positive magnetic-polynomial coefficients with matching flows
and the original cycle characters.
They are different objects from (3)--(6). General charge convolution
itself is already in the full-period current source below.
The present additional input is the positive physical-row law,
its support and coefficient-mass control, and the resulting
endpoint-window stability estimate. These coverage pointers
are not additional proof dependencies.

The complete direct sources were read at the following versions,
their used implications checked, and hashes verified:

* [Coherent endpoint kernel reduction](research_full_period_endpoint_kernel_reduction.md),
  SHA256 a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e:
  exact physical-row formula, roots above \(2\), and original
  ordinary-polynomial/normal conventions.
* [Actual outer-row decay](research_endpoint_outer_row_decay.md),
  SHA256 85e708606a44cbbbc45a82db0685fcb1d35215c89470ccdc7408790305e55e30:
  exact tail products, parity character, shared endpoint weights,
  and their coefficientwise full-source placement.
* [Full-period current charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  original charge/crossing conventions and full-Hermite cosine
  multiplication inside arbitrary shared surviving traces.

Only written mathematics, text reads and hashes were used. No
mathematical program, numerical experiment, test or compilation was
run. Adopted notes and public manuscripts are unchanged.
