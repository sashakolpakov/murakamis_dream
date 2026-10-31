# A global color gap for the actual coherent low core

29 October 2026. The literal mixed-source recurrence has a global
two-branch upper envelope no larger than the complete-color envelope.
Every macroscopic nonzero color deficit gives a STRICT contraction
on a fixed high-index interval, uniformly even at the repeated-root
color. Together with the proved coherent circle profile, this yields
a strict circle and original-source gap for the low cores at all
colors \(0\leq h\leq\lfloor(N-1)/2\rfloor\) outside a fixed
complete-color corridor.

This is a theorem about the **actual low core**. The original
nonzero crossing-times-short-polynomial band \(RP_{N,h}\) remains
separate. Its global macroscopic-color bound is not supplied here.
Thus the theorem does not yet bound the full mixed-color filling sum.

## 1. Exact recurrence and a bounded source at its literal wall

Use the notation of
[the selected mixed-inner source theorem](actual_pretzel_mixed_inner_source_wkb.md).
Put \(M=\lfloor(N-1)/2\rfloor\), \(H=Q^h\),
\(\chi=\pi h/N\), and normalize by the COMPLETE diagonal:

\[
 V_{h,r}=q^{h^2}A_{h,r}/D_{0,r},\qquad0\leq r\leq M.
\]

The exact selected Ward identity gives, with \(Z=Q^{r+1}\),

\[
 V_{h,r}=p_{h,N}(r)V_{h,r+1}+q_N(r)V_{h,r+2},
\]
\[
 p_{h,N}=-\frac{Z^{-1}[(H+H^{-1})Z^2+1+Q^{-1}]}{(1-Z)^2},
\quad
 q_N=-\frac{Q^{-2}Z^{-2}(1-QZ^2)(1+QZ)}
                         {(1-Z)^2(1-QZ)}.             \tag{1}
\]

This holds at EVERY physical \(r\), including \(r<h\). At
\(r=M-1\), \(q_N=0\) at both parities. Thus one may start the
recurrence at the actual \(V_{h,M}\), assigning the auxiliary
\(V_{h,M+1}=0\); no nonexistent factorial is divided out.

The terminal source is especially well controlled:

\[
 |V_{h,M}|=\frac{s_M^2}{s_{M-h}s_{M+h}}
 =\begin{cases}1,&N\text{ odd},\\
                 \cos\chi,&N\text{ even}.
   \end{cases}                                      \tag{2}
\]

For odd \(N=2M+1\), complement the two denominator factorials.
For even \(N=2m\), \(M=m-1\), one has
\(s_M^2=N/2\) and
\(s_{M-h}s_{M+h}=N/(2\cos\chi)\). This proves (2)
uniformly for all physical colors \(0\leq h\leq M\).
The endpoint is the original finite source, not a chosen solution
of an annihilator.

## 2. An elementary spectral ellipse controls all colors

Freeze \(u=(r+1)\pi/N\) and let \(Q\to1\) in (1), keeping
\(Z=e^{2iu}\) and \(H=e^{2i\chi}\). Write
\(T_0(u,\chi)\) for its \(2\times2\) companion. Its eigenvalues
are \(Z^{-1}v\), where

\[
 v^2-bv-c=0,\qquad c=\cot^2u,
\quad b=(c-1)\cos^2\chi-2i\sqrt c\sin^2\chi.
 \tag{3}
\]

For every \(0<u\leq\pi/2\), \(0\leq\chi\leq\pi/2\),

\[
 \boxed{\qquad \rho(T_0(u,\chi))
                    \leq\rho_0(u):=\max(1,\cot^2u).\qquad}
 \tag{4}
\]

Moreover the inequality is strict when \(\chi>0\) and
\(u\ne\pi/4\); it also holds strictly at \(u=\pi/2\).

Here is a direct proof, including collisions. For \(0<c<1\),
a root on the unit circle gives
\(b=v-c/v\), the ellipse

\[
 \left(\frac{\Re b}{1-c}\right)^2+
 \left(\frac{\Im b}{1+c}\right)^2=1.
\]

The displayed \(b\) has the left side

\[
 \cos^4\chi+\frac{4c}{(1+c)^2}\sin^4\chi\leq1,
 \tag{5}
\]

strict for \(\chi>0\). Both roots at \(b=0\) have modulus
\(\sqrt c<1\). The segment from zero to an interior point of
this convex ellipse cannot cross the unit-root locus. Continuity
therefore puts both roots inside the disk; limiting boundary
points give the non-strict assertion. For \(c>1\), apply exactly
this argument to \(v/c\), with parameter \(1/c\).
At \(c=1\), the roots of
\(v^2+2i\sin^2\chi\,v-1\) lie on the unit circle.
At \(c=0\), the roots are \(0,-\cos^2\chi\).
These computations prove (4), with no root-label selection.

In particular, for fixed \(\chi_0>0\) and any fixed interval
\(I\subset(\pi/4,\pi/2)\), compactness gives

\[
 \sup_{u\in I,\ \chi_0\leq\chi\leq\pi/2}
                           \rho(T_0(u,\chi))\leq\theta<1.
 \tag{6}
\]

At \(\chi=\pi/2\) the two roots coalesce throughout this interval.
Their common modulus is \(\sqrt c<1\). No eigenbasis or gap
between the two roots will be used.

## 3. Frozen blocks turn the spectral bound into a uniform source bound

Define

\[
 E(u)=\begin{cases}
 \displaystyle\frac2\pi\int_u^{\pi/4}\log\cot v\,dv,
                         &0\leq u<\pi/4,\\
 0,&\pi/4\leq u\leq\pi/2.
 \end{cases}
\]

The following are actual uniform estimates, not an adiabatic
assumption:

\[
 \limsup_{N\to\infty}\ 
 \max_{0\leq h,r\leq M}
 \left\{\frac1N\log|V_{h,r}|-E(\pi r/N)\right\}\leq0,
 \tag{7}
\]

and for every fixed \(\delta>0\), \(0<\beta<1/2\), there
is \(\gamma=\gamma(\delta,\beta)>0\) such that

\[
 \limsup_{N\to\infty}\ 
 \max_{\delta N\leq h\leq M,\ 0\leq r\leq\beta N}
 \left\{\frac1N\log|V_{h,r}|-E(\pi r/N)\right\}
                           \leq-\gamma.
 \tag{8}
\]

We take \(\log0=-\infty\). If \(\delta\geq1/2\), the range
is eventually empty, so only \(0<\delta<1/2\) matters.

Proof. First fix a small lower cutoff \(a>0\). On
\(a\leq u\leq\pi/2\), all coefficients of (1), and their
first \(u\) derivatives, are uniformly bounded, independently
of \(h,N\). The normalized exact matrix
\(B_N(r)=T_N(r)/\rho_0(u_r)\), \(u_r=(r+1)\pi/N\),
differs from the Lipschitz family
\(B(u_r,\chi)=T_0(u_r,\chi)/\rho_0(u_r)\) by \(O_a(1/N)\).

For a bounded \(2\times2\) matrix \(B\) with both eigenvalues
in the closed unit disk, Cayley--Hamilton gives directly

\[
 \|B^L\|\leq L\|B\|+L-1\leq C_a L.
 \tag{9}
\]

Indeed its divided-power coefficient is
\(\sum_{k=0}^{L-1}\lambda_1^{L-1-k}\lambda_2^k\), whose
modulus is at most \(L\); this formula also covers the repeated
root. If both roots instead have modulus at most \(\theta<1\),
the same proof gives \(C_aL\theta^{L-1}\).

Choose a fixed block length \(L\). A telescoping expansion of a
block of adjacent exact normalized matrices differs from the frozen
\(B(u_r,\chi)^L\) by \(O_{a,L}(1/N)\), uniformly in \(\chi\).
For any prescribed \(\varepsilon>0\), choose \(L\) so large
that \(C_aL<e^{\varepsilon L}\), and then choose \(N\) large.
Partition the product into such blocks. Two incomplete end blocks
cost a constant. This bounds the normalized product by
\(C_{a,\varepsilon}e^{2\varepsilon N}\).

For (8), choose a fixed closed interval
\(I\subset(\max(\pi\beta,\pi/4),\pi/2)\).
Every source propagation from the terminal point to \(r\leq\beta N\)
crosses all of \(I\). By (6), choose the same \(L\) sufficiently
large that each full block inside \(I\) has norm at most
\(e^{-\gamma_0 L}\), with \(\gamma_0>0\). There are
\(N|I|/(\pi L)+O(1)\) such blocks. Make the ordinary-block
\(\varepsilon\) smaller than, for example,
\(\gamma_0|I|/(8\pi)\). The negative block budget therefore
remains a fixed negative multiple of \(N\).

Near the only singular coefficient endpoint, direct use of (1)
gives a universal constant \(C\) with

\[
 \|T_N(r)\|\leq C\frac{N^2}{(r+1)^2},
                         \quad0\leq u_r\leq a<\pi/8.
 \tag{10}
\]

For the second coefficient use
\(|1-QZ^2|/|1-QZ|\leq C\),
\(|1+QZ|\leq2\), and \(|1-Z|\geq4(r+1)/N\).
The first coefficient has the same bound because \(|H+H^{-1}|\leq2\).
Thus all steps with \(r+1\leq aN/\pi\) cost at most
\(\exp\{O(Na\log(1/a))+O(\log N)\}\), by the elementary
factorial bound. This tends to rate zero as \(a\downarrow0\).
It does not grow like \(N^{O(N)}\).

Finally the scalar envelope product is bounded by the exact
right-endpoint Riemann sum

\[
 \sum_{j=r}^{M-1}\log\rho_0((j+1)\pi/N)
                         \leq N E(\pi r/N).
 \tag{11}
\]

Together with the source bound (2), these estimates prove (7).
For (8), first fix the strictly contracting interval and its budget,
then make \(a\log(1/a)\) small enough, and finally make
\(\varepsilon\) small enough. The loss from (10) and all ordinary
blocks is then strictly smaller than that budget. This proves (8)
uniformly in every indicated physical color and index.

The proof supplies exponential-rate bounds. It does not assert a
polynomial prefactor uniform through every spectral collision.

## 4. Strict circle and original-source core gaps

Interchange the two original finite sums as in the mixed source
theorem. In the complete Newton basis
\(B_r(w)=\prod_{a<r}(c_a-w-w^{-1})\), the exact mixed low-core
coefficient has magnitude

\[
 |b_{h,r}|=\frac{s_{2r}}{s_r^6}|V_{h,r}|.
 \tag{12}
\]

All marked phases remain in the equality defining that coefficient;
(12) is used only for its upper bound. The uniform factorial and
Newton-factor estimates in
[the coherent complete-base theorem](actual_pretzel_coherent_circle_and_period_asymptotic.md)
therefore imply, for every fixed \(R>1\),

\[
 \limsup_N\frac1N\log
   \max_{0\leq h\leq M}\|c_{N,h}\|_R\leq j(\log R).
 \tag{13}
\]

For every fixed \(0<\delta<1/2\), there is
\(\varepsilon_R(\delta)>0\) such that

\[
 \boxed{\quad\limsup_N\frac1N\log
  \max_{\delta N\leq h\leq M}\|c_{N,h}\|_R
                   \leq j(\log R)-\varepsilon_R(\delta).\quad}
 \tag{14}
\]

To prove strictness, let \(u_*\in(\pi/4,\pi/2)\) be the
unique maximum of the complete profile \(J_R\). Choose
\(u_*/\pi<\beta<1/2\). For \(r\leq\beta N\), use (8).
For \(r>\beta N\), use (7): that interval lies strictly above
the complete maximum, so its continuous profile
\(J_R+E=J_R\) has a fixed gap below \(j\).
Both assertions are uniform around the entire \(|w|=R\) circle;
the already proved arc inequality bounds each Newton factor by its
negative-axis value up to a constant. The finite \(r\) sum costs
only a factor \(N\).

There is also a direct original-source consequence. For each fixed
odd \(s\geq3\), choose its complete geometric radius
\(R_s=\exp[2\operatorname{arsinh}(\tan(\pi/s))]\).
If every color deficit is \(0\leq h_i\leq M\) and at least one
has \(h_i\geq\delta N\), then

\[
 \boxed{\quad\limsup_N\frac1N\log
  \left|\Phi_2\left(\prod_{i=1}^s c_{N,h_i}\right)\right|
              \leq \frac{V_s}{2\pi}-\varepsilon_{R_s}(\delta).
              \quad}                                  \tag{15}
\]

Indeed the exact full-Hermite source residue has the circle bound

\[
 |\Phi_2(F)|\leq
 \frac{N^2(R+R^{-1})}{(1-R^{-N})^2}R^{-N}
                      \max_{|w|=R}|F(w+w^{-1})|.
\]

Apply (13)--(14) to its factors, and use
\(s j(\log R_s)-\log R_s=V_s/(2\pi)\).
This step retains the actual derivative source and every finite
winding. It does not replace it by a semisimple trace.

The global alias terms \(RP_{N,h_i}\) are not covered by
(13)--(15). In the small cusp corridor they have the separate
[proved source gap](actual_pretzel_mixed_alias_source_gap.md) for odd
\(s\geq5\). At macroscopic deficits, their old \(56^{h_i}\)
bound may be too large. No claim about the full colored cube or
fixed long fillings is made without resolving those terms.
