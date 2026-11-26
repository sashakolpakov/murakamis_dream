# Uniform control of the original moving-root source pole

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The full marked cap function has a uniform boundary layer at the pole
which represents the original Conway root closing. After a factor of
\(N\), its principal part is exactly the original last Newton
coefficient. Its regular part is a holomorphic row operator with norm
bounded independently of the level. A two-end Gamma formula proves
this simultaneously for every physical index.

On a fixed small circle around that pole, negative Fourier projection
therefore selects the original scalar exactly. This projection is made
after the complete boundary packet is assembled. It is not a rule for
deleting regular functions at intermediate crossings.

## 1. The actual cap function and the source pole

Use the complete physical cap model already constructed in
[the full-current connection](research_middle_cap_full_current_connection.md).
Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad F_r=(Q;Q)_r=\prod_{j=1}^r(1-Q^j).
\]
Empty products equal one. Let \(C\) be the faithful cyclic-column
matrix, so \(y=C\alpha\) has the complete Newton coefficient vector
\(\alpha=(\alpha_0,\ldots,\alpha_d)\). Every Casimir normal is retained.
The original packet Frobenius closing is
\(\phi_N(\alpha)=\alpha_d\).

For the literal cap \(m(v_a)=x^{d-a}/N^2\) and diagonal clock
\(Zv_a=Q^av_a\), the full function is
\[
 (\mathcal B_Ny)(t)=m(I-tZ)^{-1}y.
\]
Its exact expansion is
\[
 \mathcal B_N(C\alpha)(t)=\sum_{r=0}^d\alpha_re_{r,N}(t),
 \qquad
 e_{r,N}(t)=\frac{\mu_r}{(t;Q)_{r+1}},\qquad
 \mu_r=\frac{x^d(-q)^rF_r}{N^2}.
 \tag{1}
\]
Here \((t;Q)_{r+1}=\prod_{j=0}^r(1-tQ^j)\).
This is the original marked cap function, not a new source.
Its packet-root closing is
\[
 \phi_N(\alpha)=-N^2Q^{-1}
                  \operatorname{Res}_{t=Q}\mathcal B_N(C\alpha)(t).
 \tag{2}
\]
The literal cap itself is instead the value at \(t=0\).

Put
\[
 h=\frac{2\pi i}{N},\qquad
 t_N(\zeta)=Q^{\,1-\zeta}:=\exp\{h(1-\zeta)\},\qquad
 s(\zeta)=1-e^{-2\pi i\zeta}.
 \tag{3}
\]
This fixes the logarithmic lift. The original root is \(\zeta=0\).
For a radius \(0<\rho<1/2\), set
\[
 \mathcal F_N(\zeta)\alpha
     =N\,\mathcal B_N(C\alpha)(t_N(\zeta)).
 \tag{4}
\]
Only \(r=d\) has a pole in \(|\zeta|<\rho\), and exactly
\[
             N e_{d,N}(t_N(\zeta))=\frac1{s(\zeta)}.
 \tag{5}
\]
Every term with \(r<d\) is holomorphic there. Indeed its possible
poles satisfy \(\zeta=j+1-kN\), \(0\le j\le r\);
none is zero unless \(r=d\).

## 2. One Gamma formula uniform through both ends

Write
\[
 K_{r,N}(\zeta)=
       \frac1{\prod_{j=1}^{r+1}(1-Q^{j-\zeta})}.
\]
Define the positive smooth function
\[
 D(u)=\frac{\sin(\pi u)}{\pi u(1-u)},\qquad
 D(0)=D(1)=1,\qquad 0\le u\le1.
\]
Powers of \(D\) use its real logarithm. Let \(\Gamma\) denote
Euler's Gamma function. All of its arguments below have positive
real part for \(|\zeta|<1/2\). Set
\[
 \begin{split}
 A_{r,N}(\zeta)={}&
 \Gamma(1-\zeta)
 \frac{\Gamma(r+1)}{\Gamma(r+1-\zeta)}
 \frac{\Gamma(N)}{\Gamma(N+\zeta)}
 \frac{\Gamma(N-r+\zeta)}{\Gamma(N-r)}\\
 &\hspace{12mm}\cdot D(r/N)^\zeta e^{\pi i r\zeta/N}.
 \end{split}
 \tag{6}
\]
This is a holomorphic unit and equals one at \(\zeta=0\).

**Lemma 1.** For every \(0<\rho<1/2\), there are holomorphic
functions \(E_{r,N}\), for all \(N\ge2\) and \(0\le r<N\),
such that
\[
 \boxed{\quad
 F_r(1-Q^{r+1-\zeta})K_{r,N}(\zeta)
       =A_{r,N}(\zeta)e^{E_{r,N}(\zeta)},\qquad
 |E_{r,N}(\zeta)|\le C_\rho\frac{|\zeta|}{N}.
 \quad}
 \tag{7}
\]
The left side is interpreted by its removable value at the one
source pole. In particular the statement is uniform even for \(r=d\).
Fixed \(\zeta\)-derivatives of \(E_{r,N}\) are \(O(N^{-1})\)
on smaller disks.

**Proof.** Define
\[
 g(z)=\frac{1-e^{2\pi iz}}{z(1-z)}.
\]
Its apparent singularities at zero and one are removable. It is
nonzero on a fixed complex neighborhood of \([0,1]\). Choose a
holomorphic logarithm there. Along the real interval,
\[
 \log g(u)-\log g(0)=\log D(u)+\pi iu.
 \tag{8}
\]
Factor each term of the product with \(1\le j\le r\) as
\[
 \frac{1-Q^j}{1-Q^{j-\zeta}}
 =\frac{j}{j-\zeta}
  \frac{N-j}{N-j+\zeta}
  \frac{g(j/N)}{g((j-\zeta)/N)}.
 \tag{9}
\]
The first two products are exactly the four Gamma ratios and
\(\Gamma(1-\zeta)\) in (6), by the Gamma recurrence.
They have no zero or pole in the stated disk.

Put \(\ell=\log g\). Bounded first two derivatives on a fixed
neighborhood give
\[
 \begin{split}
 \sum_{j=1}^r
 [\ell(j/N)-\ell((j-\zeta)/N)]
 &=\frac{\zeta}{N}\sum_{j=1}^r\ell'(j/N)
                       +O_\rho(|\zeta|^2/N)\\
 &=\zeta[\ell(r/N)-\ell(0)]
                       +O_\rho(|\zeta|/N).
 \end{split}
 \tag{10}
\]
These are uniform Taylor and Riemann-sum estimates, including
\(r=0,N-1\). They define a holomorphic error which vanishes at
zero. Equations (8)--(10) prove (7), because
\[
 F_r(1-Q^{r+1-\zeta})K_{r,N}
                 =\prod_{j=1}^r\frac{1-Q^j}{1-Q^{j-\zeta}}.
 \]
Cauchy's formula on nested disks proves the derivative statement.
\(\square\)

The Gamma products here are not a new Gamma-function identity.
Their role is to keep both endpoint factors at once, rather than
using an interior approximation at the original source pole.
For example the top kernel is exactly
\[
                         K_{d,N}(\zeta)=s(\zeta)^{-1},
 \tag{11}
\]
whereas every lower kernel has its pole canceled. Formula (7)
retains that difference.

## 3. A level-independent bound for the regular source row

For \(0\le r<d\), put
\[
                      k_r=\min(r+1,N-r-1)\ge1.
\]

**Theorem 2.** The exact family (4) has the decomposition
\[
 \boxed{\quad
 \mathcal F_N(\zeta)\alpha
   =\frac{\alpha_d}{s(\zeta)}
      +L_N(\zeta)\alpha_\perp,\qquad
 \sup_{|\zeta|\le\rho}\|L_N(\zeta)\|_{2\to\mathbb C}
                                                    \le C_\rho,
 \quad}
 \tag{12}
\]
where \(\alpha_\perp=(\alpha_0,\ldots,\alpha_{d-1})\).
The row \(L_N\) is holomorphic, and all fixed derivatives have
level-independent bounds on smaller disks. More precisely,
\[
       |N e_{r,N}(t_N(\zeta))|
                      \le C_\rho k_r^{\,\rho-1}\qquad(r<d).
 \tag{13}
\]

**Proof.** First, uniformly for integers \(m\ge1\) and
\(|\zeta|\le\rho\),
\[
 \left|\frac{\Gamma(m+\zeta)}{\Gamma(m)}\right|
       \asymp_\rho m^{\operatorname{Re}\zeta}.
 \tag{14}
\]
One elementary proof uses the Gamma recurrence to write the ratio
as \(\Gamma(1+\zeta)\prod_{j=1}^{m-1}(1+\zeta/j)\).
The sum of \(\log(1+\zeta/j)-\zeta/j\) is uniformly bounded
by a convergent multiple of \(\sum j^{-2}\), and
\(H_{m-1}-\log m\) is bounded. The compact Gamma factor and
its reciprocal are bounded too. The corresponding inverse ratios
follow by replacing \(\zeta\) with \(-\zeta\).

Applying (14) in (6), and using the bounded function \(D\), gives
\[
 |A_{r,N}(\zeta)|
 \le C_\rho
   \left(\frac{(r+1)(N-r)}{N}\right)^{\operatorname{Re}\zeta}
 \le C_\rho k_r^\rho\qquad(r<d).
 \tag{15}
\]
For the last inequality, the positive quantity in parentheses lies
between \(k_r/2\) and \(2k_r\).

There is also a uniform denominator bound
\[
 |1-Q^{r+1-\zeta}|\ge c_\rho k_r/N.
 \tag{16}
\]
Indeed \(|\sin(a+ib)|\ge|\sin a|\). The real part of
\(r+1-\zeta\) is at distance at least \(k_r-\rho\)
from \(N\mathbb Z\), and \(k_r-\rho\ge(1-\rho)k_r\).
Use \(\sin(\pi u/N)\ge2\min(u,N-u)/N\) for
\(0\le u\le N\), and retain the bounded exponential factor
in \(1-e^{2iz}=-2ie^{iz}\sin z\). This proves (16).

Combining (7), (15), and (16) with
\(|\mu_r/F_r|=N^{-2}\) proves (13). There are at most two
indices for each positive value of \(k_r\), so
\[
 \|L_N(\zeta)\|^2
   =\sum_{r<d}|N e_{r,N}(t_N(\zeta))|^2
   \le2C_\rho^2\sum_{k=1}^\infty k^{2\rho-2}<\infty.
 \tag{17}
\]
The exponent is summable precisely in the stated range
\(\rho<1/2\). This proves the uniform operator bound. The entries
are holomorphic; vector-valued Cauchy estimates prove the derivative
bounds without a dimension-dependent loss. \(\square\)

At the root the regular coefficients are known exactly:
\[
       N e_{r,N}(Q)=
        \frac{x^d(-q)^r}{N(1-Q^{r+1})}\qquad(r<d).
 \tag{18}
\]
There is also a uniform two-end approximation. Restricting \(L_N\)
to indices with \(k_r\ge R\) gives
\[
                    \|L_N|_{\{k_r\ge R\}}\|
                              \le C_\rho R^{\rho-1/2}.
 \tag{19}
\]
This follows by comparing the tail in (17) with its integral.
It concerns the regular part only; the original top source mode
in (12) is kept separately.

## 4. The original root as a pointed value and a Fourier mode

Multiplication by the exact central factor removes the source pole:
\[
 \mathcal S_N(\zeta)=s(\zeta)\mathcal F_N(\zeta).
 \]
This is a holomorphic row operator with
\[
 \boxed{\quad
 \mathcal S_N(0)=e_d^{\mathsf T},\qquad
 \|\mathcal S_N(\zeta)-e_d^{\mathsf T}\|
                                     \le C_\rho|\zeta|.
 \quad}
 \tag{20}
\]
It is a uniform actual-source statement on the complete Newton
Hilbert space. No closed knot scalar defines the metric.

There is an equivalent fixed-circle orthogonality statement. Define
\(P_-\) on \(L^2(d\theta/(2\pi))\) to retain the Fourier
frequencies \(-1,-2,\ldots\), and evaluate
\(\zeta=\rho e^{i\theta}\). The function
\[
 \mathcal F_N(\zeta)\alpha-\frac{\alpha_d}{2\pi i\zeta}
 \]
is holomorphic in the disk: the difference between
\(s(\zeta)^{-1}\) and \((2\pi i\zeta)^{-1}\) is holomorphic.
Therefore
\[
 \boxed{\quad
 P_-[\mathcal F_N(\rho e^{i\theta})\alpha]
       =\frac{\alpha_d}{2\pi i\rho}e^{-i\theta},\qquad
 \|P_-\mathcal F_N\alpha\|_{L^2}^2
                           =\frac{|\alpha_d|^2}{4\pi^2\rho^2}.
 \quad}
 \tag{21}
\]
The regular source terms disappear by this exact orthogonal
projection, not by a separate estimate for each of their scalar
contributions. The norm of the full boundary function is different
from the norm of its negative-frequency part.

For a full packet whose original reduced invariant is
\(K_N=\chi_N\alpha_d\), the unchanged external line
\(\chi_N\) multiplies (21) once. Thus the right side becomes
\(|K_N|^2/(4\pi^2\rho^2)\). The coordinate, circle and projection
are fixed from the original source and do not depend on \(K_N\).

## 5. Assembly and geometric limitations

The projection in (21) is applied after the complete original packet
has been assembled. Functions regular at the selected root are not a
submodule for the full physical connection. The exact face-unit action
contains \(f(t)\mapsto Q^{-1}f(t/Q)\), which becomes
\(\zeta\mapsto\zeta+1\). A pole at a neighboring integer can
therefore become the selected source pole. One may not quotient out
the regular part at each intermediate gate.

The parameter \(\zeta\) moves an auxiliary source-resolvent coordinate
at the fixed quantum root. It is neither a peripheral meridian nor a
quantum-parameter normal. The Gamma layer does not identify it with
the different normal parameters in the earlier source-frame results.

The estimates remove a level-dependent analytic loss at the original
moving pole and retain both endpoint ranges. They do not establish
a comparison between the projected norm in (21) and the unprojected
norm of an arbitrary short-component packet. In particular the error
in (20), when paired with \(\alpha\), is controlled by
\(|\zeta|\|\alpha_\perp\|\); this can exceed the original
\(|\alpha_d|\). A volume lower bound still requires control of
the actually assembled geometric packet and its original source.
No new short-filling volume case is proved here.

## Complete proof source and coverage

The complete matching proof source was read:

| Source | SHA-256 |
|---|---|
| [Full marked cap connection](research_middle_cap_full_current_connection.md) | bcd2df76c220524fcd4cc6c14e59dc6b921b21d84a43bb45e7e67c3850975692 |

The complete [whole Gamma profile](whole_gamma_frame_profile.md) and
[full-head Gamma transport](full_head_gamma_source_transport.md) were
read for coverage. They already derive Gamma profiles and preserve
both endpoint source factors in their own normal parameters. The
Gamma function and harmonic-product estimates themselves are classical.
The result here concerns the different moving pole of the actual
physical cap function and its level-independent source operator.

The complete [one-sided angular Hermite note](research_one_sided_hermite_projection.md)
was also read for coverage. It already expresses an original trace as
an angular coefficient and distinguishes its value from the full
Hardy norm. Its \(2N\)-dimensional confluent angular representative
is different from the \(N\)-dimensional physical clock function here.
Fourier projection itself is standard; the complete source, moving-root
layer and uniform bound above are the specific assertions proved here.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical calculation, test, build, git operation
or earlier-final edit was performed.
