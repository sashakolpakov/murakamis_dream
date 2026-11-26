# The canonical origin jet and its original cap connector

Written research proof, 22 November 2026.

The canonical Gamma section has an explicit expansion at zero activity.
Its first possible nonanalytic term is of order \(C^N\log C\).
Its first \(N\) asymptotic Taylor coefficients and those of the
original polynomial therefore admit an exact comparison. A marked
Cauchy formula retains the additional radial connector at every finite
radius. The original cap improves the connector bound by \(N^{-1/2}\).

The two coefficient packets below describe one variable at fixed
remaining arguments. They are not a rank-two physical boundary space.
No lower bound for their closing, or for a general Conway scalar, follows.

## 1. The original section and its marks

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 p=Q^{-1},\quad \eta=(-1)^d,\quad \kappa=q^{d^2/2}.
 \tag{1}
\]
Use the full algebra and centered basis of [P], with
\(\phi(f_i f_j)=\delta_{ij}\) and \(U_t=\sum_{j=0}^d t^jf_j\).
The original source and its exact equation [S] are
\[
 \begin{split}
 \Phi(C,H,K)&=\phi(f_0U_{-C}U_{-H}U_{-K}),\\
 (1-C/q)^2\Phi(pC)-(1-CH)(1-CK)\Phi(C)&=CJ(C),\\
 J(C)&=\frac{\eta}{N}
       [2+H^N+K^N+C^N(1-(HK)^N)] .
 \end{split}
 \tag{2}
\]
The variables \(H,K\) are held fixed in a shift of \(C\).
Write \(C=e^{-2\pi ic},H=e^{-2\pi ih},K=e^{-2\pi ik}\).
The canonical section of [G] is
\[
 \Gamma(C)=\frac{\kappa^2}{N^2}
 \frac{\prod_{a\in\{c,h,k\}}
       \mathfrak F_N(N(1-a)-1/2)^2}
      {\prod_{\{a,b\}}\mathfrak F_N(N(1-a-b))}.
 \tag{3}
\]
Here \(\mathfrak F_N\) is exactly [E]'s marked factorial; the
pairs are labelled. Initially take real \(h,k>0,h+k<1\), and a
chosen bounded-argument branch of \(\Log C\) with \(0<|C|<1\).
All formulas extend on their stated zero-free marked domains.

## 2. An exact upper-half-plane formula for the factorial

Let \(B\) denote the Barnes function used in [E, equation (8)].
Differentiating that finite product gives the exact identity
\[
 \frac{\mathfrak F_N'(z)}{\mathfrak F_N(z)}
 =\frac{\pi}{N^2}\sum_{r=0}^d(z-r)
           \left[\cot\frac{\pi(z-r)}N+i\right].
 \tag{4}
\]
For completeness the derivative calculation has no asymptotic input.
In [E]'s product set \(w_1=(r-z)/N,w_2=(r+z+1)/N\), and use
\[
 \frac{d}{dw}\log B(1+w)
       =w\psi(1+w)-w-\tfrac12+\tfrac12\log(2\pi).
 \]
The linear terms cancel after \(\psi(1+w)=\psi(w)+1/w\).
Reindexing \(r\mapsto d-r\) pairs \(w_2\) with \(1-w_1\).
The identities
\(\psi(1-w)-\psi(w)=\pi\cot(\pi w)\) and
\(\sum_{r=0}^d\psi((r-z)/N)=N\psi(-z)-N\log N\)
then give
\((\log G_N)'=\pi N^{-2}\sum_r(z-r)\cot(\pi(z-r)/N)\).
The quadratic phase defining \(\mathfrak F_N\) supplies the \(i\)
in (4). Apparent removable points are interpreted by continuation.

In \(\Im z>0\), expansion of \(\cot t+i=-2i e^{2it}/(1-e^{2it})\)
and integration give
\[
 \begin{split}
 \log\frac{\mathfrak F_N(z)}{c_N}
 ={}&\sum_{\substack{n\ge1\\N\nmid n}}
       \frac{Q^{nz}}{n(p^n-1)}
   +\frac{z-d/2}{N}\Log(1-e^{2\pi iz})\\
 &+\frac{\operatorname{Li}_2(e^{2\pi iz})}{2\pi iN},\\
 c_N&=\sqrt N\,
       \exp\left\{\frac{\pi i}{4}
                   -\frac{\pi i(N+N^{-1})}{12}\right\}.
 \end{split}
 \tag{5}
\]
All series and logarithms are anchored at zero exponential argument.
To check the integration, the finite sums of \(Q^{-nr}\) vanish at
nonresonant \(n\), whereas
\(\sum_r rQ^{-nr}=N/(p^n-1)\). At \(n=Nm\) the remaining
sum is \(N(z-d/2)\). These give (5) by direct differentiation.
The derivative decays integrably at the upper end, uniformly on
bounded real intervals, so its integration constant is a single
nonzero constant, not a periodic function.

Its normalization follows from \(\mathfrak F_N(0)=1\). Indeed the
nonresonant exponential in (5), with \(x=Q^z\), is
\[
 (1-x^N)^{d/(2N)}
       \prod_{r=1}^d(1-p^rx)^{-r/N}.
 \]
This identity follows by expanding the finite product's logarithm.
As \(z\to0\) from above, the remaining power is
\((1-x^N)^{z/N}\to1\). Thus
\[
 c_N=e^{\,i\pi/(12N)}
          \prod_{r=1}^d(1-p^r)^{r/N}.
 \tag{6}
\]
The factors have arguments \(\pi/2-\pi r/N\). Pairing \(r,N-r\)
gives modulus \(\sqrt N\); summing their weighted arguments gives
precisely (5). No undetermined unit remains.

## 3. Exact origin factorization and its quantitative central factor

Set \(Z=C^N,x=H^N,y=K^N\), and define
\[
 \begin{split}
 \Gamma_0&=\frac{\kappa^2}{N^2}
 \frac{\mathfrak F_N(N(1-h)-1/2)^2
       \mathfrak F_N(N(1-k)-1/2)^2}
      {\mathfrak F_N(N(1-h-k))},\\
 A_N(C)&=\exp\!\sum_{\substack{n\ge1\\N\nmid n}}
       \frac{2q^{-n}-H^n-K^n}{n(p^n-1)}C^n,\\
 M(Z)&=\frac{(1-xZ)(1-yZ)}{(1+Z)^2}.
 \end{split}
 \tag{7}
\]
The fixed marked factorials in \(\Gamma_0\) are nonzero in the
stated real domain. The series for \(A_N\) converges absolutely
on \(|C|<\min(1,|H|^{-1},|K|^{-1})\) and defines a nonzero unit.
Let \(Z_N\) be the unit with logarithm
\[
 \begin{split}
 \log Z_N(Z)={}&\Log(1+Z)
 -\left(\tfrac12-h+\tfrac1{2N}\right)\Log(1-xZ)
 -\left(\tfrac12-k+\tfrac1{2N}\right)\Log(1-yZ)\\
 &+\frac{2\operatorname{Li}_2(-Z)
           -\operatorname{Li}_2(xZ)-\operatorname{Li}_2(yZ)}
          {2\pi iN}.
 \end{split}
 \tag{8}
\]
Its logarithms and dilogarithms, and \(\Log M\), are their power
series at zero. Substitution of (5) into (3) gives exactly
\[
 \boxed{\quad
 \Gamma(C)=\Gamma_0 A_N(C)\,B_N(C),\qquad
 B_N(C)=Z_N(C^N)
       \exp\left\{-\frac{\Log M(C^N)\Log C}{2\pi i}\right\}.
 \quad}
 \tag{9}
\]
For example the three variable factorial arguments have exponential
arguments \(C/q,CH,CK\). Their coefficients of \(\Log(1-\cdot)\)
are \(1/2-c\), \(1/2-c-h+1/(2N)\), and
\(1/2-c-k+1/(2N)\), respectively. Collecting the \(c\) terms
gives \(c\Log M=-\Log M\Log C/(2\pi i)\).
The constants \(c_N\) cancel two against two, proving the displayed
\(\Gamma_0\) without any limiting-normalization assumption.

Uniformly for \(h,k\) in a fixed compact subset of the real domain,
a fixed \(\rho<1\), and bounded \(\arg C\),
\[
 \log B_N(C)=O_\rho\bigl(|C|^N(1+|\Log C|)\bigr),\qquad
 B_N(C)=1+O_\rho(\rho^N)\quad(0<|C|\le\rho).
 \tag{10}
\]
Indeed \(x,y\) have modulus one and all power-series arguments
have modulus at most \(\rho^N\). Also
\(\sup_{0<r\le\rho}r^N|\log r|\le C_\rho\rho^N\).
This is a relative estimate against \(\Gamma_0A_N\), not against
a Taylor truncation or the physical source.

In particular the finite asymptotic jet is
\[
 \Gamma(C)=\Gamma_0 P_N(C)
            +O_N\bigl(C^N(1+|\Log C|)\bigr),\qquad
 P_N=[A_N]_{<N}.
 \tag{11}
\]
The first logarithmic coefficient is
\(\Gamma_0(2+H^N+K^N)/(2\pi i)\) at \(C^N\Log C\).
Thus jets through degree \(d\) exist, but an ordinary holomorphic
germ to all orders at zero has not been asserted.

## 4. The exact polynomial source has two explicit coefficient packets

Set \(P_{-1}=Q_{-1}=0,P_0=1,Q_0=0\). For \(1\le n<N\)
define their coefficients by
\[
 \begin{split}
 (p^n-1)P_n&=(2q^{-1}p^{n-1}-H-K)P_{n-1}
                    +(HK-p^{n-1})P_{n-2},\\
 (p^n-1)Q_n&=(2q^{-1}p^{n-1}-H-K)Q_{n-1}
                    +(HK-p^{n-1})Q_{n-2}+\delta_{n1}.
 \end{split}
 \tag{12}
\]
Write \(P_N(C)=\sum_{n<N}P_nC^n\) and
\(\mathcal Q_N(C)=\sum_{n<N}Q_nC^n\).
Every denominator \(p^n-1\) is nonzero, including at composite
levels. The first recurrence agrees with (11): from (7),
\[
 \frac{A_N(pC)}{A_N(C)}
 =\frac{(1-CH)(1-CK)}{(1-C/q)^2}\,M(C^N)^{-1/N},
 \tag{13}
\]
with the root equal to one at zero; the last factor has no
nonconstant coefficient below degree \(N\).

Put \(j_0=\eta(2+H^N+K^N)/N\). Coefficient comparison in (2)
through degree \(d\) gives the exact polynomial identity
\[
 \Phi(C)=\Phi_0P_N(C)+j_0\mathcal Q_N(C),\qquad
 \Phi_0=\Phi(0,H,K)
       =\frac{\eta}{N}[C^N]\mathscr S_N(C,H,K).
 \tag{14}
\]
The last expression is the explicit product sum of [S].
No division by \(j_0,\Phi_0\), or a cyclic norm occurs.
Consequently, if \(g_n\) are the jets in (11), then
\[
 \sum_{n<N}\bigl(g_n-[C^n]\Phi\bigr)C^n
       =(\Gamma_0-\Phi_0)P_N(C)-j_0\mathcal Q_N(C).
 \tag{15}
\]
This describes all \(N\) low coefficients in terms of two
specified packets; it does not remove their dependence on \(H,K,N\).

## 5. Marked Cauchy coefficients retain a cut connector

Choose \(0<\arg C<2\pi\), with its continued canonical section.
Let \(\Gamma_+(t)\) be the initial bank on \(0<t<1\).
After one counterclockwise turn its terminal bank is
\(\Gamma_-(t)=M(t^N)^{-1}\Gamma_+(t)\), by (9).
There are no factorial poles on these slit annuli: all
\(C\)-dependent factorial arguments have positive imaginary part.
With
\(\beta(C)=[1-(CH)^N][1-(CK)^N]\), the exact jump is
\[
 W(C):=\Gamma_-(C)-\Gamma_+(C)
   =\frac{N}{\eta}\frac{C^N J(C)\Gamma_+(C)}{\beta(C)}.
 \tag{16}
\]
For \(0\le n<N\) define the integral over one marked circle
\[
 a_n(\rho)=\frac1{2\pi i}
       \int_{|C|=\rho}^{\rm marked}\Gamma(C)C^{-n-1}\,dC .
 \]
The cut-annulus boundary has the outer circle minus the inner
circle and the two radial banks. Its orientation gives
\[
 a_n(\rho_2)-a_n(\rho_1)
   =\frac1{2\pi i}\int_{\rho_1}^{\rho_2}W(t)t^{-n-1}\,dt,
 \quad
 a_n(\rho)=g_n+
       \frac1{2\pi i}\int_0^\rho W(t)t^{-n-1}\,dt .
 \tag{17}
\]
The second identity follows from (11); all radial integrals
converge absolutely. The same jump formula holds for
\(\Gamma-\Phi\), since \(\Phi\) is polynomial.

Let \(x=f_0U_{-H}U_{-K}\) be the actual full output observed by
\(\Phi(C)=\sum_{n<N}(-C)^nx_n\). For any finite co-source row
\(\ell\), including its original corridors, define
\[
 K_\ell(C)=\sum_{n<N}(-1)^n\ell_n C^{-n-1}.
 \]
Summing (17) gives the complete readout identity
\[
 \begin{split}
 \frac1{2\pi i}\int_{|C|=\rho}^{\rm marked}\Gamma K_\ell\,dC
       -\ell(x)
 ={}&\sum_{n<N}(-1)^n\ell_n
              \bigl(g_n-[C^n]\Phi\bigr)\\
 &+\frac1{2\pi i}\int_0^\rho W(C)K_\ell(C)\,dC .
 \end{split}
 \tag{18}
\]
Both the jet block (15) and the connector remain. Neither
is an ordinary Fourier projection of a single-valued whole
Gamma circle.

## 6. Literal caps and quantitative connector bounds

The centered transform in [P] gives the original rows
\[
 \phi(f_n)=\frac{\kappa^{-1}}{\sqrt N}(-q^{-1})^n,\qquad
 m(f_n)=\frac{\kappa}{\sqrt N}(-q)^n .
 \]
Thus their exact co-source kernels are
\[
 K_\phi=\frac{\kappa^{-1}}{\sqrt N}
              \frac{1+C^{-N}}{C-q^{-1}},\qquad
 K_m=\frac{\kappa}{\sqrt N}
              \frac{1+C^{-N}}{C-q}.
 \tag{19}
\]
These are finite Laurent polynomials with their displayed removable
points, not new poles of the original cap. In particular the
\(\phi\)-connector between two radii is exactly
\[
 \Delta_\phi=
 \frac{\sqrt N\kappa^{-1}}{2\pi i\eta}
 \int_{\rho_1}^{\rho_2}
  \frac{(1+C^N)J(C)\Gamma_+(C)}
       {(C-q^{-1})\beta(C)}\,dC .
 \tag{20}
\]
For \(m\), replace \(\kappa^{-1},q^{-1}\) by \(\kappa,q\).
In general \(\Delta_\ell(\rho_1,\rho_2)\) denotes
\((2\pi i)^{-1}\int_{\rho_1}^{\rho_2}W(C)K_\ell(C)\,dC\).

For \(0\le\rho_1<\rho_2\le\rho<1\), Cauchy--Schwarz gives
\(|K_\ell(t)|\le\|\ell\|t^{-N}/\sqrt{1-\rho^2}\).
Also \(|J|\le6/N\) and
\(|\beta|\ge(1-\rho^N)^2\ge(1-\rho^2)^2\). Therefore
\[
 \begin{split}
 |\Delta_\ell|&\le
 \frac{3\|\ell\|}{\pi(1-\rho^2)^{5/2}}
                     \int_{\rho_1}^{\rho_2}|\Gamma_+(t)|\,dt,\\
 |\Delta_\phi|,\ |\Delta_m|&\le
 \frac{6}{\pi\sqrt N(1-\rho)(1-\rho^2)^2}
                     \int_{\rho_1}^{\rho_2}|\Gamma_+(t)|\,dt .
 \end{split}
 \tag{21}
\]
These are absolute Gamma-weighted estimates, without a lower
bound on the original scalar.

There is a source-scaled estimate on shrinking circles. Fix \(c>0\)
and take \(\rho_2\le c/N\), for sufficiently large \(N\).
For unit \(H,K\), \(|p^n-1|\ge4/N\) when \(N\nmid n\).
Consequently (7) gives
\[
 |\log A_N(C)|\le-N\log(1-|C|)\le2c
                         \quad(|C|\le c/N).
 \tag{22}
\]
Equations (9)--(10) bound the remaining factor uniformly, so
\(|\Gamma_+|\le C_c|\Gamma_0|\) and
\(|W(C)|\le C_c|\Gamma_0||C|^N\). Applying the same finite
co-source estimates and integrating a length at most \(c/N\) proves
\[
 |\Delta_\ell|\le C_c|\Gamma_0|\|\ell\|/N,\qquad
 |\Delta_\phi|,\ |\Delta_m|
                         \le C_c|\Gamma_0|N^{-3/2}.
 \tag{23}
\]
Constants are uniform on the fixed compact marked family.
The inner jet block in (18) has not been bounded by these estimates.
In particular (23) is not a relative error for its original cap.

All fixed parameter derivatives on buffered pole-free domains
differentiate the whole identities, including \(\Gamma,J,M\)
and any moving row. A coherent boundary derivative is not
identified with an ordinary main-color quantum normal.

## Complete proof sources and scope

All four complete proof texts were read at these renewed matching pins:

| Label | Complete source | SHA-256 |
|---|---|---|
| E | [Canonical factorial, 226 lines](exact_factorial_interpolation_and_complex_contours.md) | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |
| G | [Canonical Gamma section, 632 lines](research_crossing_exact_gamma_source_extension.md) | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |
| S | [Cleared original source, 248 lines](research_crossing_cleared_cyclic_source.md) | cd157a7ec5947fbddb2d94bb7696726d1714f1089bd93c0ea3aa7a0380cafb46 |
| P | [Full pairwise compiler, 668 lines](research_exact_pairwise_conway_source.md) | 470c9df0384274623a1aa0b6939067021894f2fea41595dfa7440081ca77f1d1 |

Finite cyclic dilogarithmic products and their anchored low jets
already occur in [the cyclic Hardy source](actual_cyclic_hardy_dilog_network.md).
No novelty for that method is claimed. The comparison here uses the
specified canonical factorial, its exact origin normalization, the
actual forced polynomial, and the literal full co-source rows.
The formulas retain all \(N\) coordinates and Hermite directions.
They supply no arbitrary-tree cancellation or finite-exception theorem.

Only written mathematics and text/hash inspection were used. No
mathematical program, numerical experiment, test, build, git action,
or earlier-final file edit was performed.
