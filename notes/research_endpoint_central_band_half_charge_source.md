# The original central high band is an exact half-charge source

Private research note, 16 November 2026. Written proof only.

The controlled endpoint amplitude is the factor of a literal band
of the original Newton kernel. Thus it can be inserted into a coupled
graph before any remaining trace is estimated. At even levels the
band is a half-charge coupon times one polynomial amplitude. At odd
levels it is the difference of the two neighboring lattice half-charge
coupons times that same amplitude. The omitted high band has explicit
macroscopic physical support and polynomial coefficient cost.
The low endpoint coupon remains separate.

## 1. Original conventions and the ordinary polynomial identity

For \(N\ge2\), put \(D=N-1\), \(m=\lfloor N/2\rfloor\), \(k_0=N-m\),
\(\eta=(-1)^D\), and \(\theta=\pi/N\). Retain
\[
 s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^j s_h,\quad
 c_a=2\cos((2a+1)\theta),\quad
 e_k(z)=S_k^{-2}\prod_{h<k}(c_h-z),
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f,\qquad
 w_N(\alpha)=2\cosh(\alpha/N).
 \tag{1}
\]
The source charge coupon \(\mathcal C_{N,\chi}\) has the full
Hermite data of \(\cos(N(1-\chi)t)\) under \(z=-2\cos t\).
For an integer \(j=N(1-\chi)\) with \(0\le j\le D\), it is the
ordinary polynomial \(T_j(-z/2)\). Values and normals both agree,
and the odd simple node has value one.

For \(0\le L\le m-1\), define the original central high band
\[
 B^{[L]}_{N,\alpha}(z)=
      \sum_{l=0}^L e_{k_0+l}(w_N(\alpha))e_{k_0+l}(z).
 \tag{2}
\]
Use the exact ratios and polynomial amplitude
\[
 (A_l,B_l)=
 \begin{cases}
 ((l+\tfrac12)\theta,(l+1)\theta),&N\ {\rm even},\\
 ((l+1)\theta,(l+\tfrac32)\theta),&N\ {\rm odd},
 \end{cases}
\]
\[
 \rho_{l,N}(\alpha,t)=
 \frac{[\cos^2 A_l+\sinh^2(\alpha/(2N))]
       [\sin^2(t/2)-\sin^2 A_l]}{\cos^4 B_l},
 \quad
 H_{N,L}(\alpha,t)=
      \sum_{l=0}^L\prod_{j=0}^{l-1}\rho_{j,N}(\alpha,t).
 \tag{3}
\]
Because \(\sin^2(t/2)=(z+2)/4\), this is an ordinary polynomial
of degree at most \(L\) in \(z\); denote it by
\(\mathcal H_{N,L,\alpha}(z)\). Its denominators are nonzero
for all ratios actually used in (3).

**Theorem 1 (ordinary band factorization).** Exactly as ordinary
polynomials, before any physical quotient,
\[
 B^{[L]}_{N,\alpha}=
 \begin{cases}
 \displaystyle d_{N,\alpha}\,
       \mathcal C_{N,1/2}\mathcal H_{N,L,\alpha},
                          &N=2m,\\[3pt]
 \displaystyle d_{N,\alpha}
       \bigl(\mathcal C_{N,(m+1)/N}
                    -\mathcal C_{N,m/N}\bigr)
                         \mathcal H_{N,L,\alpha},&N=2m+1,
 \end{cases}
 \tag{4}
\]
where
\[
 d_{N,\alpha}=
 \begin{cases}
 \displaystyle\frac{(-1)^m\cosh(\alpha/2)}{N^2},&N=2m,\\[3pt]
 \displaystyle\frac{(-1)^m\cosh(\alpha/2)\cosh(\alpha/(2N))}
                         {2N^2\cos^4(\theta/2)},&N=2m+1.
 \end{cases}
 \tag{5}
\]

*Proof.* Consecutive Newton products give
\[
 \frac{e_{k_0+l+1}(w)e_{k_0+l+1}(z)}
      {e_{k_0+l}(w)e_{k_0+l}(z)}
       =\frac{(c_{k_0+l}-w)(c_{k_0+l}-z)}
                    {s_{k_0+l+1}^4}.
 \tag{6}
\]
The two minus signs multiply to plus. Put \(r=m-1-l\).
Then \(c_{k_0+l}=c_r\) and \(s_{k_0+l+1}=s_r\).
Substitution of \(w=w_N(\alpha)\), \(z=-2\cos t\) turns
(6) into (3). Ratio statements are polynomial multiplicative
identities, including at zeros.

The distinct-root products of \(P_N\) and the sine products
\(S_m^2=2N\) (even), \(S_m^2=N\) (odd), give
\[
 e_{k_0}(-2\cos t)=
 \begin{cases}
 \cos(Nt/2)/N,&N=2m,\\
 -[\cos(mt)-\cos((m+1)t)]/[2N\cos^2(\theta/2)],
                                      &N=2m+1,
 \end{cases}
 \tag{7}
\]
and
\[
 (-1)^{k_0}e_{k_0}(w_N(\alpha))=
 \begin{cases}
 \cosh(\alpha/2)/N,&N=2m,\\
 \cosh(\alpha/2)\cosh(\alpha/(2N))
                  /[N\cos^2(\theta/2)],&N=2m+1.
 \end{cases}
 \tag{8}
\]
For the odd identity use
\(\cos(mt)-\cos((m+1)t)=2\sin(Nt/2)\sin(t/2)\);
it includes the simple root at \(t=0\). Equations (6)--(8)
prove (4). Its degree is at most \(k_0+L\le D\), so no
hidden reduction or discarded normal occurs. \(\square\)

## 2. The omitted band has only macroscopic physical support

The full high coupon and its omitted band are
\[
 B^{\rm high}_{N,\alpha}
       =\sum_{r=0}^{m-1}e_{D-r}(w_N(\alpha))e_{D-r}(z),
 \qquad E^{[L]}_{N,\alpha}
       =B^{\rm high}_{N,\alpha}-B^{[L]}_{N,\alpha}.
 \tag{9}
\]
Set \(r_*=m-L-2\). If \(r_*<0\), \(E^{[L]}=0\).
Otherwise the original radical contraction gives
\[
 \phi_N(R_nE^{[L]}_{N,\alpha}f)
   =\sum_{a=0}^{r_*}\omega_{a,N,L}(\alpha)
                         R_n(c_a)f(c_a),
\]
\[
 \omega_{a,N,L}(\alpha)=
   \sum_{r=a}^{r_*}e_{D-r}(w_N(\alpha))b_{ra},\qquad
 b_{ra}=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}}.
 \tag{10}
\]
Here \(R_n\) is the original crossing at integer powers and its
canonical full-Hermite real-power extension otherwise, with the
original scalar retained. At real \(n\), \(|R_n(c_a)|=1\).
The surviving angles necessarily satisfy
\[
 \tau_a=(D-2a)\theta\ \ge\
 \begin{cases}
 (2L+3)\theta,&N\ {\rm even},\\
 (2L+4)\theta,&N\ {\rm odd}.
 \end{cases}
 \tag{11}
\]
Thus \(L=\lfloor\delta N\rfloor\), \(0<\delta<1/2\), removes
only physical rows at angles tending to at least \(2\pi\delta\).

Uniformly on every bounded complex \(\alpha\)-set,
\[
 |\omega_{a,N,L}(\alpha)|\le C N^{3/2},\qquad
                   \sum_a|\omega_{a,N,L}(\alpha)|
                                     \le C N^{5/2}.
 \tag{12}
\]
Indeed the full-radical source proves \(|b_{ra}|\le2\) and
\[
 |e_{D-r}(-2\cos t)|\le\sqrt{N-1}e^{D|\Im t|}.
 \tag{13}
\]
Take \(t=\pi-i\alpha/N\), and sum at most \(m\) terms in each
coefficient. The finite exceptional level \(N=2\) is immediate;
its omitted band is empty. Every derivative in a free exterior
variable commutes with (10), without a new coefficient cost.

The trace in (10) still includes its original normal. Since the
radical value is zero, that normal differentiates the radical,
and only the spectator value survives. The odd simple value
vanishes. No value-only substitute for a full trace is assumed.

## 3. Exact assembly inside an arbitrary coupled graph

Let \(G=(V,E)\) be a finite original graph, \(S\) its traced
vertices, and \(T\subseteq S\) a set of vertices receiving one
chosen high endpoint coupon each. Set
\[
 F_N(\mathbf z)=A_N(\mathbf z)\prod_{vw\in E}K_N(z_v,z_w),
 \tag{14}
\]
where \(A_N\) is any joint polynomial spectator. It may contain
additional fixed coupons at the same vertices. Every edge is
kept once, and outside variables remain ordinary free variables
or their prescribed values.

At \(T\) start with unit charge; at \(S\setminus T\) retain
arbitrary original charges \(\chi_v\). Write
\[
 Z_{\rm band}=
 \left(\prod_{v\in S}\phi_N^{(z_v)}\right)
 \left[
  F_N\prod_{v\in S}R_{n_v}(z_v)
  \prod_{v\in S\setminus T}\mathcal C_{N,\chi_v}(z_v)
  \prod_{v\in T}B^{[L]}_{N,\alpha_v}(z_v)
 \right].
 \tag{15}
\]
Equation (4) gives an exact source formula. At even levels it
is \(\prod_{v\in T}d_{N,\alpha_v}\) times the same graph source
with charges \(1/2\) at \(T\) and common inserted spectator
\[
                 F_N\prod_{v\in T}\mathcal H_{N,L,\alpha_v}(z_v).
 \tag{16}
\]
At odd levels it is that same scalar times the sum over
\(\epsilon\in\{+,-\}^{T}\), with sign \((-1)^{\#\{v:\epsilon_v=-\}}\),
of the same sources (16), with charges
\[
 \chi_v^+=(m+1)/N=\tfrac12+\tfrac1{2N},\qquad
 \chi_v^-=m/N=\tfrac12-\tfrac1{2N}\quad(v\in T).
 \tag{17}
\]
All remaining charges, full traces, powers, carriers, shared
edges and spectator factors stay exactly as written. Parameters
in \(A_N\) are held fixed when comparing the indicated charges.
No independent-neighbor or product-spectator assumption enters
the identity.

There is also a bound for restoring the entire high coupon
which retains actual coherent reduced sources. Define
\(Z_{\rm high}\) by replacing every band in (15) with its full
high coupon. For \(\varnothing\ne U\subseteq T\), define
\(\mathscr Z_U(\mathbf a)\) by evaluating \(z_v=c_{a_v}\)
for \(v\in U\) in (14), retaining every resulting kernel and
shared spectator, and taking all original traces over \(S\setminus U\).
Those traces keep the original powers and charges and the
band coupons at \(T\setminus U\). The factors \(R_{n_v}(c_{a_v})\)
for \(v\in U\) are kept outside this definition.
Expansion of (9), followed by (10), gives exactly
\[
 Z_{\rm high}-Z_{\rm band}
  =\sum_{\varnothing\ne U\subseteq T}\ \sum_{0\le a_v\le r_*}
      \left[\prod_{v\in U}
       \omega_{a_v,N,L}(\alpha_v)R_{n_v}(c_{a_v})\right]
                           \mathscr Z_U(\mathbf a).
 \tag{18}
\]
Consequently, for real powers and bounded microscopic
parameters,
\[
 |Z_{\rm high}-Z_{\rm band}|
 \le\sum_{\varnothing\ne U\subseteq T}
       (C N^{5/2})^{|U|}
           \max_{0\le a_v\le r_*}|\mathscr Z_U(\mathbf a)|.
 \tag{19}
\]
An empty tail contributes zero. Fixed ordinary outside
derivatives satisfy the identical statement with the
corresponding derivatives of \(\mathscr Z_U\).
In particular edges joining two evaluated vertices remain
\(K_N(c_{a_v},c_{a_w})\); edges to surviving traces remain
their original physical-boundary kernels. Equation (19)
does not replace them by an unfilled absolute spectator.

## 4. Analytic use and its precise remaining scope

For \(L=\lfloor\delta N\rfloor\), the adopted general-domain
theorem gives, uniformly with all fixed derivatives on compact
subsets of
\[
 |\cos t-\cos(2\pi\delta)|<1+\cos(2\pi\delta),
 \qquad
 H_{N,L}(\alpha,t)=\sec^2(t/2)+O_{\rm hol}(N^{-2}).
 \tag{20}
\]
The normalized polynomial amplitude is therefore a unit there
for large \(N\). The scalar (5) also is a unit after its \(N^{-2}\)
factor is removed on compact \(\alpha\)-sets avoiding
\(\cosh(\alpha/2)=0\). For \(\delta=1/8\), the entire closed
rectangle \(|\Re t|\le\pi/4,\ |\Im t|\le\log3\) lies in this
domain.

Thus (15)--(17) put the band into actual original near-half-charge
sources with a common controlled local multiplier. This is stronger
than identifying a formal off-grid phase or merely matching central
physical values. At odd levels the difference in (17) must remain
coherent. Its cosine factor is exactly
\(2\sin(Nt/2)\sin(t/2)\); at even levels the factor is
\(\cos(Nt/2)\). Their insertion in the original double-pole
horizontal trace cancels one denominator factor, giving the same
simple-pole half-charge kernel as in the amplitude theorem.
All original vertical terms are still present.

The theorem does not bound the full near-half-charge sources,
prove a gap for the physical sources in (19), or compare their
combined rate with the filled action. It also does not factor
the low part of \(K_N(w_N(\alpha),z)\) through a radical charge
coupon. Combining that low part with (18), and controlling the
remaining full graph source, are separate tasks.

## 5. Direct source versions

All three complete direct proofs were read at the following
versions; the implications used above and their hashes were checked.

* [Full high Newton radical](research_high_newton_radical_contraction.md),
  SHA256 1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03:
  original Newton data, full trace, coefficients (5)--(6), bounds
  (12), and the full Fourier estimate (34)--(36).
* [Endpoint general domain](research_endpoint_radical_general_domain.md),
  SHA256 600ae0d78f29946272ed54b600cb1f5fdf170965985a08d6e3d9201303722074:
  exact lowering amplitude, its compact-domain symbol and the
  rectangle used in (20).
* [Full-period current charge convolution](research_full_period_current_charge_convolution.md),
  SHA256 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595:
  original cosine coupons and real-power carriers, full-Hermite
  charge substitution, and full-survivor source placement.
