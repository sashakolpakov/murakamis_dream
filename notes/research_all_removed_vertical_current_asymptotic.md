# The actual all-removed vertical current

Private written proof, 16 November 2026.

Integrating adjacent removed vertices together does not eliminate the
exponential cost of their internal kernels. For every fixed graph
without isolated vertices and with nonzero signed powers, the complete
all-removed vertical integral has a nonzero endpoint asymptotic. The
coefficient below retains the original crossing phases and paired
current normalization. It is a statement about one term of the exact
current expansion, not about the sum of horizontal and vertical terms.

## 1. Original source and statement

Let \(\Gamma=(V,E)\) be a fixed nonempty finite loopless simple graph,
with every vertex selected and no outside vertex. Each undirected edge
is counted once. Write
\[
 v_0=|V|,\qquad e_0=|E|,\qquad
 d_v=\#\{e\in E:v\in e\}\ge1 .
 \tag{1}
\]
Fix signed integer powers \(n_v\ne0\) and heights \(H_v>0\).
There are no additional coupons in the theorem. Disconnected graphs
are allowed. No geometric parent is assumed.

Use the original full physical algebra and Newton kernel:
\[
 \begin{gathered}
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 s_j=2\sin(\pi j/N),\qquad S_k=\prod_{j=1}^k s_j,\\
 e_k(C)=S_k^{-2}\prod_{j=0}^{k-1}(c_j-C),\qquad
 K_N(C,C')=\sum_{k=0}^{D}e_k(C)e_k(C').
 \end{gathered}                                                   \tag{2}
\]
Here \(S_0=e_0(C)=1\); the symbol \(e_0\) without an argument in
(1) denotes the number of graph edges.

Put
\[
 C_{N,n}=\exp\!\left(\frac{\pi i nD^2}{4N}\right),\qquad
 \Omega_{N,n}=C_{N,n}e^{inN\pi/4},\qquad w_h=2\cosh h .
 \tag{3}
\]
The original crossing \(R^n\) retains the values and first spectral
normals of \(C_{N,n}e^{inNt^2/(4\pi)}\) at \(C=-2\cos t\), and
the simple-node value at odd levels. Write
\(L_{n,1}[f]=\phi_N(R^nf)\).
The original unit-charge full-period vertical density is
\[
 \rho_{N,n,1}(h)=
 \frac{2i\eta N^2\Omega_{N,n}}{\pi}
 \frac{\sinh h\,e^{-inNh^2/(4\pi)}\sinh(nNh/2)}
      {P_N(w_h)},\qquad
 P_N(w_h)=e^{Nh}(1+e^{-Nh})^2 .
 \tag{4}
\]
The complete all-removed term, before its inclusion--exclusion sign,
is the ordinary integral
\[
 \mathcal I_{\Gamma,N}(\mathbf H)=
 \int_{\prod_{v\in V}[0,H_v]}
       \prod_{v\in V}\rho_{N,n_v,1}(h_v)
       \prod_{\{v,w\}\in E}K_N(w_{h_v},w_{h_w})
       \prod_{v\in V}dh_v .
 \tag{5}
\]
No quotient reduction is performed in the integrand. In particular,
every internal removed edge in (5) retains the full kernel.

Define
\[
 \begin{split}
 \kappa_v&=d_v-1+\frac{|n_v|}{2}>0,\\
 \Psi_v(h)&=\kappa_v h-\frac{in_vh^2}{4\pi},\qquad
 \Psi_v'(h)=\kappa_v-\frac{in_vh}{2\pi},\\
 b_d(h)&=\frac{\sinh h}{(2\cosh h-2)^d}\quad(h>0).
 \end{split}                                                     \tag{6}
\]

**Theorem 1.** Along both level parities,
\[
 \boxed{\quad
 \mathcal I_{\Gamma,N}=
 \mathcal A_{\Gamma,N}(\mathbf H)\,
 N^{\,v_0-4e_0}
 \exp\!\left(N\sum_{v\in V}\Psi_v(H_v)\right)
 \bigl(1+O(N^{-1})\bigr),
 \quad}                                                         \tag{7}
\]
where the actual coefficient is
\[
 \mathcal A_{\Gamma,N}(\mathbf H)=
 \left(\frac{i\eta}{\pi}\right)^{v_0}
 \prod_{v\in V}
 \frac{\operatorname{sgn}(n_v)\Omega_{N,n_v}\,
       b_{d_v}(H_v)}
      {\kappa_v-in_vH_v/(2\pi)} .
 \tag{8}
\]
Its modulus is bounded above and below by positive constants when
the heights range over any fixed compact subset of \((0,\infty)^V\).
The relative error is uniform on such compacts. Consequently
\[
 \lim_{N\to\infty}\frac1N\log|\mathcal I_{\Gamma,N}|
       =\sum_{v\in V}
          \left(d_v-1+\frac{|n_v|}{2}\right)H_v .
 \tag{9}
\]
The heights and powers are fixed before taking this limit. No
shrinking-height assertion is made.

For the single edge with powers \(n,p\ne0\), (7) reads
\[
 \begin{split}
 \mathcal I_{\mathrm{edge},N}
 ={}&-\frac{\operatorname{sgn}(np)\Omega_{N,n}\Omega_{N,p}}
                {\pi^2N^2}\,
 \frac{b_1(H_1)b_1(H_2)}
 {(|n|/2-inH_1/(2\pi))(|p|/2-ipH_2/(2\pi))}\\
 &\quad\cdot
 \exp N\left\{\frac{|n|H_1+|p|H_2}{2}
             -\frac{i(nH_1^2+pH_2^2)}{4\pi}\right\}
 \bigl(1+O(N^{-1})\bigr).
 \end{split}                                                     \tag{10}
\]
Thus even this actual joint integral has the internal-edge cost
\(H_1+H_2\), in addition to the two density rates
\((|n|/2-1)H_1+(|p|/2-1)H_2\).

## 2. A kernel bound including every small-height face

Two elementary Newton estimates will distinguish the whole box from
its positive-height corner. The exact top polynomial is
\[
 e_D(w)=\frac{\eta P_N(w)}{N^2(w-c_0)} .
 \tag{11}
\]
Indeed \(S_D=N\), \(c_D=c_0\), and the monic polynomial \(P_N\)
has the listed \(N\) roots with their original multiplicities.

**Lemma 2.** For \(w=2\cosh h\), \(h\ge0\), and every
\(0\le k\le D\),
\[
 |e_k(w)|\le e^{Nh},\qquad
 0<K_N(w_h,w_{h'})\le N e^{N(h+h')}\quad(h,h'\ge0).
 \tag{12}
\]

*Proof.* At \(w=2\) the successive absolute ratios are
\[
 \frac{|e_{k+1}(2)|}{|e_k(2)|}
   =\frac{\sin^2((k+\tfrac12)\pi/N)}
          {\sin^2((k+1)\pi/N)}.
 \tag{13}
\]
They pass from at most one to at least one only once. This follows
by writing the denominator sine minus the numerator sine as
\(2\cos((k+\tfrac34)\pi/N)\sin(\pi/(4N))\).
Hence the maximum of \(|e_k(2)|\) occurs at an end. The first end
equals one, and (11) gives
\[
 |e_D(2)|=\frac{1}{N^2\sin^2(\pi/(2N))}\le1,
 \tag{14}
\]
using \(\sin x\ge2x/\pi\) on \([0,\pi/2]\).

For \(w\ge2\), each factor \((w-c_j)/(2-c_j)\) is at least one.
Extending its partial product to all \(N\) root factors yields
\[
 \frac{|e_k(w)|}{|e_k(2)|}
 \le\prod_{j=0}^{N-1}\frac{w-c_j}{2-c_j}
 =\frac{P_N(w)}{P_N(2)}
 =\cosh^2(Nh/2)\le e^{Nh}.
 \tag{15}
\]
Each \(e_k(w)\) has sign \((-1)^k\). The same-index products in
the kernel are therefore positive, and summing their bounds proves
(12). \(\square\)

The exact density also obeys, uniformly on a fixed height interval,
\[
 |\rho_{N,n,1}(h)|
 \le C_{n,H}N^2
       e^{N(|n|/2-1)h},\qquad 0\le h\le H .
 \tag{16}
\]
This follows directly from (4), keeping its complete denominator.
Multiplying (12) and (16) gives on the whole box
\[
 \left|\prod_v\rho_v\prod_{\{v,w\}}K_N(w_{h_v},w_{h_w})\right|
 \le C N^{2v_0+e_0}
                 \exp\!\left(N\sum_v\kappa_vh_v\right).
 \tag{17}
\]
Since every \(\kappa_v\) is positive, the complement of
\[
                    \mathcal B=\prod_v[H_v/2,H_v]
 \tag{18}
\]
has an absolute integral bounded by
\[
 C N^{2v_0+e_0}
 \exp\!\left\{N\left(\sum_v\kappa_vH_v-\epsilon_0\right)\right\},
 \qquad
 \epsilon_0=\tfrac12\min_v\kappa_vH_v>0 .
 \tag{19}
\]
This includes all axes, all lower-dimensional faces and their
neighborhoods. It is not an estimate obtained by extending a
positive-height asymptotic to \(h=0\).

## 3. Uniform top dominance and the original signed coefficient

**Lemma 3.** On any fixed positive-height compact,
\[
 K_N(w_h,w_{h'})
       =e_D(w_h)e_D(w_{h'})(1+O_{\rm hol}(N^{-4})).
 \tag{20}
\]
The estimate holds on a fixed complex neighborhood of that compact,
and hence for every fixed number of derivatives there.

*Proof.* Choose a complex neighborhood with
\(\Re w_h,\Re w_{h'}\ge2+\delta\) for some fixed \(\delta>0\).
Uniformly in \(0\le j<D\),
\[
 \Re w-c_j-s_{j+1}^2
 \ge\delta-\frac{2\pi}{N}\ge\delta/2
 \tag{21}
\]
for large \(N\). Here the first inequality is the difference of
cosines at angles separated by \(\pi/N\). Since \(s_{j+1}^2\le4\),
each backward ratio has modulus at most
\(\vartheta=(1+\delta/8)^{-1}<1\).
Its last one satisfies the stronger bound
\[
 \left|\frac{e_{D-1}(w)}{e_D(w)}\right|
       =\left|\frac{s_D^2}{c_{D-1}-w}\right|
       \le C_\delta N^{-2}.
 \tag{22}
\]
Consequently
\[
 \sum_{k=0}^{D-1}
 \left|\frac{e_k(w)e_k(w')}{e_D(w)e_D(w')}\right|
 \le C_\delta N^{-4}\sum_{\ell\ge0}\vartheta^{2\ell}
 =O(N^{-4}).
 \tag{23}
\]
The denominators have no zero in this neighborhood. Holomorphic
Cauchy estimates on smaller fixed neighborhoods prove the derivative
claim. \(\square\)

Apply (20) to every edge of (5) on \(\mathcal B\). Its leading
integrand factors by vertex as
\(\prod_v\rho_{N,n_v,1}(h_v)e_D(w_{h_v})^{d_v}\).
Equations (4),(11) give the exact factor
\[
 \begin{split}
 \rho_{N,n,1}(h)e_D(w_h)^d
 ={}&
 \frac{i\eta^{d+1}\operatorname{sgn}(n)\Omega_{N,n}}{\pi}
       N^{2-2d}\,
       \frac{\sinh h}{(2\cosh h-c_0)^d}
       e^{N\{(d-1+|n|/2)h-inh^2/(4\pi)\}}\\
 &\quad\cdot(1+e^{-Nh})^{2d-2}
                  (1-e^{-|n|Nh}) .
 \end{split}                                                     \tag{24}
\]
All current and Newton signs are present here. In particular
\(\sum_vd_v=2e_0\) makes the product of the \(\eta^{d_v+1}\)
factors equal to \(\eta^{v_0}\).

On each interval \([H_v/2,H_v]\), the amplitude in (24), after
its displayed constant and power of \(N\), equals
\[
 b_{d_v}(h)+O(N^{-2})+O(N^b e^{-cN})
 \tag{25}
\]
with bounded fixed derivatives. The \(O(N^{-2})\) term uses
\(c_0=2+O(N^{-2})\); the exponentially small term comes from
the two final factors in (24). The constants are uniform over
compact positive height choices.

For each vertex,
\[
 |\Psi_v'(h)|\ge\Re\Psi_v'(h)=\kappa_v>0 .
 \tag{26}
\]
Integration by parts using
\(e^{N\Psi_v}=(N\Psi_v')^{-1}(e^{N\Psi_v})'\), followed
by the absolute bound \(|e^{N\Psi_v(h)}|=e^{N\kappa_vh}\),
therefore gives
\[
 \int_{H_v/2}^{H_v}
  \left[b_{d_v}(h)+O(N^{-2})+O(N^b e^{-cN})\right]
       e^{N\Psi_v(h)}\,dh
 =
 \frac{b_{d_v}(H_v)e^{N\Psi_v(H_v)}}
      {N\Psi_v'(H_v)}
       (1+O(N^{-1})).
 \tag{27}
\]
The lower endpoint is exponentially smaller, and the derivative
remainder is \(O(N^{-2}e^{N\kappa_vH_v})\). Thus (27) is
a relative complex asymptotic with a nonzero leading coefficient,
not a replacement of the oscillatory integral by its absolute value.

The error from replacing the product of kernels by its top term is
also controlled. By (20),(24) it has absolute integral at most
\[
 C N^{-4}\,N^{2v_0-4e_0}
       \prod_v\int_{H_v/2}^{H_v}e^{N\kappa_vh_v}\,dh_v
 \le C N^{v_0-4e_0-4}e^{N\sum_v\kappa_vH_v}.
 \tag{28}
\]
This is \(O(N^{-4})\) relative to the nonzero leading term of
(27) multiplied over all vertices. Combining (24),(27),(28)
and the exponentially smaller complement (19) proves (7)--(8).
Formula (26) and positivity of every \(b_d(H)\) prove the stated
uniform nonvanishing and the limit (9). \(\square\)

## 4. What the integrated obstruction does and does not imply

The original full trace has the exact decomposition
\[
 L_{n,1}=H_{n,1}^{H}+V_{n,1}^{H}.
 \tag{29}
\]
Tensoring (29), or its full-survivor inclusion--exclusion form,
retains all original value and first-normal data and the odd
simple-node value. Equation (5) is exactly its all-removed term.
Its sign in the full-survivor correction is \((-1)^{v_0+1}\);
that sign does not change its rate or nonvanishing.

Theorem 1 shows that the positive internal-kernel cost survives
the actual oscillatory integrations in this term. The issue is
therefore not repaired merely by replacing a pointwise estimate
with a joint vertical integral over the same removed component.
Any useful bound for that integral must pay its rate (9).

It does not follow that the complete original period has this rate.
Other horizontal and vertical terms in (29) can cancel it. Nor does
the theorem say that a supplied geometric parent cannot absorb the
additional rate in a strict gap. Such a comparison requires its
actual heights and action budget. The theorem assumes no geometric
parent, while the corrected angle-envelope source supplies a
positive-parent one-edge example to which (10) can also be applied.

A zero power makes its exact unit current zero, so nonzero powers
are necessary for the asserted coefficient. An isolated vertex
instead has \(\kappa_v=|n_v|/2-1\); the monotone endpoint proof
need not apply to it. Both exclusions are hypotheses of this theorem,
not deletions from a larger source. Likewise, arbitrary surviving
traces, external kernels or additional coupons require their own
estimates and are not absorbed into (8).

## 5. Coverage and direct-source readback

The full-current source already gives the exact signed density,
the complete trace decomposition and the all-removed integrand.
The corrected angle-envelope source proves the pointwise internal
kernel rate and explains its incompatibility with a proposed
zero-cost pointwise quantum transfer. The additional result here
is the nonzero asymptotic of the actual integrated all-removed term,
uniformly including all omitted small-height regions.

The complete direct sources were read in full, their used implications
checked, and both pins verified:

* [Original full-period currents and graph source](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595.
* [Corrected full-height angle envelope and internal kernel obstruction](research_saturated_current_full_height_angle_envelope.md),
  SHA256 af559ba52a93f87b370d2ce6421b19fa0a3cb4b67a0d1a46816fe0f39cb388b2.

Only written mathematics, text reads and hashes were used. No
mathematical program, numerical experiment, test or build was run.
Previously adopted notes and public manuscripts are unchanged.
