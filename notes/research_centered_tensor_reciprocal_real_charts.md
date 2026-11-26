# Reciprocal real charts for the original centered tensor

21 November 2026. Research note. Earlier finals and public
manuscripts remain unchanged.

The generating polynomial of the centered Conway tensor has exact
reciprocal charts. Moving a leg outside the unit disk changes the
crossing power in its original Frobenius source. This change matters:
the two charts with all legs on the same side have the oscillatory
packet already proved on the real cube, whereas every mixed real
chart has an endpoint packet of order \(N^{-3/2}\), after its explicit
exterior monomial has been removed. Its coefficient is nonzero.

These are statements about the whole initialized tensor, including
its original closing and repeated-root coordinates. They do not assert
a volume identity or move a geometric coefficient cycle. The final
section locates a real negative hyperbolic trace in this atlas and
explains a limitation of the cleared critical equation.

## 1. Exact reciprocal identities in the full boundary algebra

Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\quad
 \chi_N=q^{d^2/4},\quad D_N(t)=1-\eta t^N .
 \tag{1}
\]
Every power \(q^a\) means \(e^{\pi ia/N}\). Work in the entire
original algebra
\[
 H_N=\mathbb C[z]/P_N(z),\qquad P_N(z)=2T_N(z/2)+2,
\]
with its original Frobenius row \(\phi\), positive crossing \(R\),
and centered basis
\[
 f_a=N^{-1/2}R p_a(z),\qquad
 G_N(t;z)=\sum_{a=0}^d p_a(z)t^a .
 \tag{2}
\]
All derivatives at double roots of \(P_N\) are part of this algebra.
For a polynomial \(g(z)\), let
\(g^\sharp(z)=\overline{g(\bar z)}\). This conjugates its
coefficients, rather than its argument. Extend the same operation
coefficientwise to a series in \(t\), and write
\[
 G_N^+(t;z)=G_N(t;z),\qquad
 G_N^-(t;z)=G_N(t;z)^\sharp .
\]
In particular, for real \(s,z\), \(G_N^-(s;z)\) is the complex
conjugate of \(G_N(s;z)\).

**Lemma 1.** The following are exact identities in \(H_N[t]\):
\[
 p_{d-a}=R^{-2}p_a^\sharp,\qquad
 \boxed{\quad t^dG_N(1/t;z)=R^{-2}G_N^-(t;z).\quad}
 \tag{3}
\]

**Proof.** The centered compiler proves
\(f_a^\sharp=f_{d-a}\) and \(R^\sharp=R^{-1}\).
Apply \(\sharp\) to (2) and multiply by \(R^{-1}\). This gives
the first identity in (3). Reindexing the finite sum proves the
second. These are full algebra identities, not just equalities at
the distinct Casimir roots. They are not asserted as ordinary
polynomial identities at an arbitrary off-spectrum \(z\).
\(\square\)

The original three-boundary polynomial is
\[
 \mathcal C_N(\mathbf t)
   =N^{-3/2}\phi\!\left(R^3\prod_{i=1}^3G_N(t_i;z)\right).
 \tag{4}
\]
Choose signs \(\varepsilon_i\in\{+1,-1\}\). An inside leg has
\(\varepsilon_i=1,t_i=s_i\); an exterior leg has
\(\varepsilon_i=-1,t_i=1/s_i\). Initially an exterior \(s_i\)
is nonzero. Set
\[
 m=\#\{i:\varepsilon_i=-1\},\quad k=3-2m=\sum_i\varepsilon_i,
 \qquad
 F_{\varepsilon,N}(\mathbf s)
    =N^{-3/2}\phi\!\left(R^k
                       \prod_iG_N^{\varepsilon_i}(s_i;z)\right).
 \tag{5}
\]
Here \(G_N^{\varepsilon_i}\) denotes \(G_N^+\) or \(G_N^-\),
not a multiplicative power. Formula (3) gives exactly
\[
 \boxed{\quad
 \mathcal C_N(\mathbf t)=
       \left(\prod_{\varepsilon_i=-1}t_i^d\right)
                              F_{\varepsilon,N}(\mathbf s).
 \quad}
 \tag{6}
\]
The polynomial \(F_{\varepsilon,N}\) is also defined at exterior
\(s_i=0\). Thus (6) has a regular interpretation at infinity after
the displayed monomial is removed. No original source factor was
discarded. In particular the effective crossing powers are \(3,1,-1,-3\),
not always \(3\).

## 2. The mixed real-chart theorem

Write
\[
 \Delta_N(\mathbf s)=\prod_{i=1}^3D_N(s_i),\qquad
 A_0(\mathbf s)=\prod_{i=1}^3(1+s_i)^{-1}.
 \tag{7}
\]
For real \(|s_i|<1\), all factors in these expressions are positive.

**Theorem.** Fix \(0<\rho<1\). If the signs are mixed, so that
\(k=1\) or \(k=-1\), then uniformly on \(\mathbf s\in[-\rho,\rho]^3\),
\[
 \boxed{\quad
 F_{\varepsilon,N}(\mathbf s)=
 \kappa^{-k}e^{\,3k\pi i/(4N)}
 \Delta_N(\mathbf s)\,N^{-3/2}A_0(\mathbf s)
                                      (1+O_\rho(N^{-1})).
 \quad}
 \tag{8}
\]
This includes both parities and composite levels. In particular the
whole mixed-chart source is nonzero on every such compact cube for
all sufficiently large \(N\). The error is a value estimate; no
derivative of its relative error is claimed.

For comparison, the all-positive chart is the previously proved
real packet
\[
 F_{+++,N}(\mathbf s)=
 (-1)^N\kappa^3e^{\,i\pi/4-3\pi i/(4N)}
 \Delta_N(\mathbf s) B(\mathbf s)e^{iN\Psi(\mathbf s)}
                                  (1+O_\rho(N^{-1})),
 \tag{9}
\]
where
\[
 \begin{aligned}
 B(\mathbf s)&=\prod_{i<j}(1-s_is_j)^{-1/2},\\
 \Psi(\mathbf s)&=-\frac\pi{12}
  +\frac1{2\pi}\left[
       \sum_i\operatorname{Li}_2(-s_i)
       +\operatorname{Li}_2(-s_1s_2s_3)
       -\sum_{i<j}\operatorname{Li}_2(s_is_j)\right].
 \end{aligned}
 \tag{10}
\]
The roots in \(B\) are positive. Since \(\phi(g^\sharp)=\overline{\phi(g)}\),
the all-negative chart is exactly the complex conjugate of
\(F_{+++,N}(\mathbf s)\) for real \(\mathbf s\).

Consequently these formulas cover every real inside/exterior choice
away from \(t_i=\pm1\), after the exact monomial in (6) is retained.
They make no assertion in a level-dependent transition region at
those walls.

## 3. The physical interpolation and its source

We give the proof of (8), including its endpoint coefficient.
The full-degree generating-section theorem supplies
\[
 U_N(t,z)=\exp\!\left\{\sum_{n=1}^{N-1}
  \frac{(-1)^{n+1}(2T_n(z/2)-2q^{-n})}{n(Q^{-n}-1)}t^n\right\}.
 \tag{11}
\]
On every fixed interior disk this agrees exponentially accurately
with \(G_N\) at all physical values and all required first Casimir
normals. The real-source theorem proves, for every fixed \(j\ge0\),
\[
 U_N(t,2\cos\theta)
       =A(t,2\cos\theta)e^{N\Phi(t,2\cos\theta)}
                                            (1+O_{C^j,\rho}(N^{-1})),
 \tag{12}
\]
for real \(|t|\le\rho\), uniformly on \(0\le\theta\le2\pi\).
Here
\[
 A(t,z)=(1+zt+t^2)^{-1/2},\qquad
 \Phi(t,z)=\frac{
  \operatorname{Li}_2(-wt)+\operatorname{Li}_2(-w^{-1}t)
                          -2\operatorname{Li}_2(-t)}{2\pi i},
 \quad z=w+w^{-1}.
 \tag{13}
\]
All branches are anchored at \(t=0\). For real \(t\) and \(z\in[-2,2]\),
\(A>0\) and \(\Phi\) is purely imaginary. The \(C^j\) norm in
(12) is the real angle norm. Conjugating (11)--(12) gives the
corresponding interpolation for \(G_N^-\), with phase \(-\Phi\)
and the same leading amplitude.

Define a reflection-even amplitude \(A_{\varepsilon,N}(\theta)\)
by multiplying the three interpolating sections and removing their
phases \(N\sum_i\varepsilon_i\Phi(s_i,2\cos\theta)\).
For every fixed \(j\),
\[
 A_{\varepsilon,N}(\theta)
  =\prod_i(1+2s_i\cos\theta+s_i^2)^{-1/2}
                                        +O_{C^j,\rho}(N^{-1}).
 \tag{14}
\]
In particular its derivatives are uniformly bounded and
\(A_{\varepsilon,N}(0)=A_0(\mathbf s)+O_\rho(N^{-1})\).

Put
\[
 \begin{aligned}
 \sigma_\varepsilon(\theta)
   &=\frac{k(\theta-\pi)^2}{4\pi}
                  +\frac1i\sum_i\varepsilon_i
                                         \Phi(s_i,2\cos\theta),\\
 a_N(\theta)&=\sin\theta\,A_{\varepsilon,N}(\theta),\qquad
 L_N(\theta)=a_N(\theta)e^{iN\sigma_\varepsilon(\theta)}.
 \end{aligned}
 \tag{15}
\]
This is a real phase. The Gaussian interpolation
\(\chi_N^k e^{ikN(\theta-\pi)^2/(4\pi)}\) has precisely the
values of \(R^k\) at the physical nodes and its first Casimir
derivatives at double nodes. The odd simple node needs only its
value. Negative \(k\) causes no change to this verification because
\(R\) is a unit.

For an ordinary polynomial \(f\), the original source is exactly
\[
 \phi(f)=(-1)^N\sum_{j=0}^{d}
  \left.\frac d{d\theta}\{\sin\theta\,f(2\cos\theta)\}
                              \right|_{\theta=(2j+1)\pi/N}.
 \tag{16}
\]
Replacing the physical Hermite data by (11) in this identity, and
factoring out \(\Delta_N\), has exponentially small normalized
error \(O_\rho(N^4\rho^N)\), just as in the real-source proof.
Conjugation and the fixed powers \(k=\pm1\) preserve that bound.
The exact midpoint Poisson identity therefore gives
\[
 \frac{F_{\varepsilon,N}}{\Delta_N}
 =\frac{(-1)^N\chi_N^k iN^{1/2}}{2\pi}
      \sum_{\ell\ne0}(-1)^\ell\ell I_{\ell,N}
                                    +O_\rho(N^4\rho^N),
 \quad
 I_{\ell,N}=\int_0^{2\pi}a_N(\theta)
         e^{iN(\sigma_\varepsilon(\theta)-\ell\theta)}d\theta .
 \tag{17}
\]
The zero label is absent exactly: it is the integral of \(L_N'\),
whose endpoint values \(L_N(0)=L_N(2\pi)=0\) agree. This is the
original source cancellation, not a choice to suppress a critical
point. The factors \(N^{1/2}\) and \(\ell\) in (17) are retained.

## 4. Every nonzero Fourier charge is nonstationary

For real \(|s|<1\), let
\[
 h_s(\theta)=\theta-2\arg(1+se^{i\theta}),
 \qquad h_s'(\theta)=\frac{1-s^2}{|1+se^{i\theta}|^2}>0.
 \tag{18}
\]
The argument is continuous from zero. Thus \(h_s(0)=0\),
\(h_s(\pi)=\pi\), and \(0<h_s(\theta)<\pi\) for
\(0<\theta<\pi\). Direct differentiation of (15) gives
\[
 \sigma_\varepsilon'(\theta)
       =\frac{\sum_i\varepsilon_i h_{s_i}(\theta)-k\pi}{2\pi}.
 \tag{19}
\]
When \(k=1\), two signs are positive and one is negative.
On the first half-circle their signed sum lies strictly between
\(-\pi\) and \(2\pi\), so
\(-1<\sigma_\varepsilon'<1/2\). Reflection gives
\(-1/2<\sigma_\varepsilon'<1\) on the other half.
For \(k=-1\), reverse all signs to obtain the same strict
bound \(|\sigma_\varepsilon'|<1\). At the two endpoints the
derivatives are \(-k/2,k/2\), also strictly inside this interval.

Compactness of \([-\rho,\rho]^3\times[0,2\pi]\) now supplies
\(c_\rho>0\) with
\[
 |\sigma_\varepsilon'(\theta)-\ell|
                           \ge c_\rho|\ell|\qquad(\ell\ne0).
 \tag{20}
\]
All fixed higher phase derivatives are uniformly bounded. There is
no stationary nonzero charge to initialize in a mixed real chart.
Additional solutions of a cleared exponential critical equation
must not be assigned such a charge without this check.

## 5. The endpoint coefficient, with its original phase

The exact endpoint data are
\[
 a_N(0)=a_N(2\pi)=0,\quad
 a_N'(0)=a_N'(2\pi)=A_{\varepsilon,N}(0),\quad
 \sigma_\varepsilon(0)=\sigma_\varepsilon(2\pi)=k\pi/4 .
 \tag{21}
\]
Integrate \(I_{\ell,N}\) by parts twice, using
\(v_\ell=\sigma_\varepsilon'-\ell\). A third integration
bounds the remaining integral. Equations (14), (20), and (21)
give uniformly for every nonzero integer \(\ell\),
\[
 \begin{aligned}
 I_{\ell,N}={}&\frac{A_{\varepsilon,N}(0)e^{iNk\pi/4}}{N^2}
   \{(k/2-\ell)^{-2}-(-k/2-\ell)^{-2}\}\\
 &\hspace{25mm}+O_\rho(N^{-3}|\ell|^{-3}).
 \end{aligned}
 \tag{22}
\]
For example the first integration leaves amplitude
\((a_N/v_\ell)'\); the second boundary term is exactly the
first line of (22). The remaining amplitude is
\(((a_N/v_\ell)'/v_\ell)'\). Its next boundary term and
integral have the stated bound after one further integration.
The difference in braces is \(O(|\ell|^{-3})\); its leading
inverse-square endpoint terms cancel. Thus both the main series
and the remainder in (17) are summable with their source weight
\(|\ell|\).

For \(k=\pm1\), the required absolutely convergent endpoint sum is
\[
 S_k=\sum_{\ell\ne0}(-1)^\ell\ell
       \{(k/2-\ell)^{-2}-(-k/2-\ell)^{-2}\}
                                      =-2\pi k .
 \tag{23}
\]
Here is an elementary normalization check. For \(k=1\), shifting
the second summation index by one, first in symmetric partial
sums, gives
\[
 S_1=2\sum_{\ell\in\mathbb Z}
                         \frac{(-1)^\ell}{\ell-1/2}
     =-8\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}=-2\pi .
\]
The shifted tails tend to zero. The final alternating series is
\(\int_0^1(1+x^2)^{-1}dx=\pi/4\), by integrating the
finite geometric sums and bounding their remainder. Reversing
the sign of \(k\) reverses the braces, proving (23).

Substituting (22)--(23) in (17) gives
\[
 F_{\varepsilon,N}
  =(-1)^N(-ik)\chi_N^k e^{iNk\pi/4}
       \Delta_N N^{-3/2}A_0(\mathbf s)
                                         (1+O_\rho(N^{-1})).
 \tag{24}
\]
The leading amplitude is bounded above and away from zero on
the compact cube. Finally, for \(k=\pm1\), the exact scalar identity
\[
 (-1)^N(-ik)\chi_N^k e^{iNk\pi/4}
                         =\kappa^{-k}e^{3k\pi i/(4N)}
 \tag{25}
\]
follows by inserting \(d=N-1\) in (1). This proves (8).

## 6. Where a real negative hyperbolic trace lies

This section concerns the classical critical equation of the
displayed bulk phase. It does not assert its contribution to a
finite coefficient period.

For original finite parameters \(t_i\ne-1\), put
\[
 x_i=\frac{1-t_i}{1+t_i},\qquad
 E_2=x_1x_2+x_1x_3+x_2x_3.
\]
Away from \(1+t_1t_2t_3=0\), clearing the exponential critical
equation gives an endpoint \(w=-1\) and the reciprocal quadratic
\[
 w^2-z_*w+1=0,\qquad
 z_*=1-\frac{\sum_it_i+\sum_{i<j}t_it_j}{1+t_1t_2t_3}
                           =2-\frac4{1+E_2}.
 \tag{26}
\]
For real parameters,
\[
 z_*<-2\quad\Longleftrightarrow\quad -1<E_2<0,
 \qquad z_*=-2\quad\Longleftrightarrow\quad E_2=0.
 \tag{27}
\]
An inside real leg has \(x_i>0\), and an exterior real leg has
\(x_i<0\). In either same-side chart all three \(x_i\) have the
same sign, so \(E_2>0\) and \(-2<z_*<2\). A real negative
hyperbolic trace therefore requires a mixed chart. The actual
mixed-real source there is (8), not the unit-charge packet (9).
This places that trace relative to these generating coordinates;
identifying a prescribed marked geometric trace with these
coordinates remains a separate requirement.

The quadratic in (26) also needs its original divisor exclusions.
Before its denominators are cleared, the equation is
\[
 -\prod_i\frac{w+t_i}{1+t_iw}=1,\qquad
 w\ne0,\qquad \prod_i(1+t_iw)\ne0 .
 \tag{28}
\]
An apparent root on a zero or pole of the ratio can occur only
if \(t_it_j=1\) for some \(i,j\). This is impossible when all
\(|t_i|<1\), but is permitted in mixed charts. Indeed if
\(t_2=t_1^{-1}\), the corresponding two signed Blaschke factors
cancel. Their canceled numerator and denominator can still leave
roots in the cleared quadratic (26). Such a root is not an
ordinary critical point of the reduced logarithmic phase. The
source formula (8) remains uniform through this reciprocal-pair
divisor, since its original finite expression has no singularity
there. The exceptional value \(E_2=-1\) is the degree-changing
divisor \(1+t_1t_2t_3=0\), and was excluded in (26).

There is a simple positive circle interpretation inside the real
cube. Set \(R_i=(1+t_i)/(1-t_i)>0\). At the initialized unit-charge
point, \(w=e^{i\theta_*}\), the three Blaschke angles satisfy
\[
 h_{t_1}(\theta_*)+h_{t_2}(\theta_*)+h_{t_3}(\theta_*)=\pi,
 \qquad
 \tan\frac{h_{t_i}(\theta_*)}{2}
       =\frac{r}{R_i},\qquad
 r^2=\frac{R_1R_2R_3}{R_1+R_2+R_3}.
 \tag{29}
\]
To check this, the Cayley transform gives
\(\tan(h_{t_i}/2)=x_i\tan(\theta_*/2)\), while (26)
gives \(\tan^2(\theta_*/2)=1/E_2=r^2\).
The triangle whose side opposite vertex \(i\) has length
\(R_j+R_k\) has semiperimeter \(R_1+R_2+R_3\), inradius
\(r\), and these same positive half-angle tangents. Its vertices
are the centers of three externally tangent circles of radii
\(R_i\). Thus (29) is an elementary center-triangle identification
for these auxiliary coordinates. It does not identify the
original marked Conway gluing with an arbitrary circle pattern,
nor identify its regulator or volume.

For clarity, the initialized action itself has exact logarithmic
momenta
\[
 \exp\{2\pi t_i\partial_{t_i}\Psi\}
       =\frac{(1-t_it_j)(1-t_it_\ell)}
                    {(1+t_i)(1+t_1t_2t_3)},
       \qquad\{i,j,\ell\}=\{1,2,3\},
 \tag{30}
\]
on the real cube, with removable values at \(t_i=0\).
These ratios and the phase constant in (10) are fixed by the
original source. A geometric generating-function comparison
must match these momenta and the original markings; algebraicity
of (26) alone does not do so.

## 7. Scope and complete proof sources

The reciprocal identities retain full algebra elements. The
asymptotic theorem evaluates the entire original source on a
real generating atlas and keeps its exterior monomials, crossing
powers and first-root normals. No physical boundary direction is
discarded, and no geometric cycle coefficient is assigned.

Real-chart nonvanishing away from the walls does not establish a
complex zero-free domain or control an assembled coefficient
period. In particular the original coefficient cycle cannot be
replaced by arbitrary real evaluations of its vertices. No volume
identity or finite-exception filling theorem follows here.

All three complete proof sources were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Centered original compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Full-degree generating section](research_full_degree_centered_generating_section.md) | 6fbef2085aca79503518745a08d3466ec84cd337ec8131944e2aebb9c95c2f6b |
| [Initialized real source](research_centered_tensor_real_source_packet.md) | 4052f55915ff8d9688de9b714f8209eab4c7ea885467024c864cc9c68e07e654 |

The source Poisson formula and calibrated interpolation are already
proved in the last source. The new assembly is the exact reciprocal
atlas, the absence of nonzero real charges in all mixed charts,
their explicit nonzero endpoint coefficient, and the resulting
geometric placement. No novelty is claimed for reciprocal
polynomials, integration by parts, or tangent-circle triangles.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
