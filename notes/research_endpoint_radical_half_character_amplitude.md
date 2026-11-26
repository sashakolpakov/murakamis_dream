# The actual endpoint radical has a regular half-grid character amplitude

Private research note, 16 November 2026. Written proof only.

This note groups the entire radical part of the original endpoint
coupon before estimating it. Near the complete physical color its
alternating weights have an exact analytic interpolation, with the
parity required for a full-grid Fourier argument. The interpolation
also handles endpoint heights of order \(N^{-1}\). The low part of the
coupon and the original spectator remain present; no filled-source
rate or integration-cycle assertion is made.

Half-charge sampling contours are already used for the distinct-node
Cauchy observation in
[the odd-level observation note](research_odd_half_charge_observation.md),
Sections 1--2, and its
[even-level counterpart](research_complete_source_pick_observation.md),
Section 5. Those sections were checked for coverage. The new input here
is the exact analytic amplitude of the actual endpoint's entire high
coupon, including its microscopic-height normalization and terminating
physical-row interpolation. Section 5 derives its own contour formula;
the older observation theorems are coverage references, not additional
proof dependencies or assertions about this different coupon.

## 1. Original coupon and surviving normal

Use
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad k_0=N-m,\quad
 \eta=(-1)^D,\quad\theta=\pi/N,\qquad N\ge2,
\]
\[
 s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^j s_h,\quad
 c_a=2\cos((2a+1)\theta),\quad
 e_k(z)=S_k^{-2}\prod_{h<k}(c_h-z).
 \tag{1}
\]
The original algebra and closing are
\[
 \mathcal A_N=\mathbb C[z]/(P_N),\quad P_N(z)=2T_N(z/2)+2,
 \qquad\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
At the microscopic endpoint put
\[
 w_N(\alpha)=2\cosh(\alpha/N),\qquad
 B_{N,\alpha}(z)=K_N(w_N(\alpha),z)
                  =\sum_{k=0}^D e_k(w_N(\alpha))e_k(z).
 \tag{3}
\]
Its high part is
\[
 B^{\rm high}_{N,\alpha}
   =\sum_{r=0}^{m-1}e_{D-r}(w_N(\alpha))e_{D-r}(z),
 \qquad B^{\rm low}_{N,\alpha}=B_{N,\alpha}-B^{\rm high}_{N,\alpha}.
 \tag{4}
\]
The two complete direct sources, read at the versions listed below,
are the full-radical contraction theorem and the coherent endpoint
kernel theorem. In particular the first gives, for every original
spectator \(f\in\mathcal A_N\),
\[
 \phi_N(e_{D-r}f)=\sum_{a=0}^r b_{ra}f(c_a),\qquad
 b_{ra}=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}}.
 \tag{5}
\]
This is the actual first-normal residue: the radical vanishes at
every physical value, its normal consumes the local derivative, and
the derivative of the spectator drops out by the product rule. At
odd levels the extra simple node \(c_m=-2\) contributes zero. Thus
(5) is not a values-only replacement for the original trace.

For \(0\le a<m\) define the even entire function of \(\alpha\)
\[
 \gamma_{a,N}(\alpha)=
  \sum_{r=a}^{m-1}(-1)^{D-r}e_{D-r}(w_N(\alpha))\,|b_{ra}|.
 \tag{6}
\]
Absolute values in (6) apply only to the fixed real numbers \(b_{ra}\).
The endpoint factor is its displayed signed polynomial, so complex
continuation of (6) is unambiguous. For real \(\alpha\), all its
summands are strictly positive. Equation (5) gives the exact identity
\[
 \boxed{\displaystyle
 \phi_N(B^{\rm high}_{N,\alpha}f)
       =\eta\sum_{a=0}^{m-1}(-1)^a
                      \gamma_{a,N}(\alpha)f(c_a).}
 \tag{7}
\]
It is coefficientwise in arbitrary joint spectators and ordinary
free-boundary variables. Original crossings of any power for which
their physical class is specified can be included in \(f\).

The source of (5) states \(N\ge3\); at \(N=2\), \(e_1=-z/4\),
\(b_{00}=1\), and the same identity follows directly from (2).

## 2. Exact last term and lowering ratios

Write the positive physical angle as
\[
 \tau_a=(D-2a)\theta,\qquad c_a=-2\cos\tau_a,
 \qquad p_a=m-1-a.
 \tag{8}
\]
The sum in (6) is most useful in the order \(r=m-1-l\),
\(0\le l\le p_a\). Let its summand be \(T_l(\alpha,\tau_a)\).
The first summand is exactly
\[
 T_0(\alpha,\tau)=
 \begin{cases}
 \displaystyle \frac{\cosh(\alpha/2)}{N}\sin\tau,
       &N=2m,\\[4pt]
 \displaystyle \frac{\cosh(\alpha/2)\cosh(\alpha/(2N))}
                       {N\cos^4(\theta/2)}
                        \sin\tau\sin(\tau/2),&N=2m+1.
 \end{cases}
 \tag{9}
\]
Here is a direct normalization check. The sine products give
\(S_m^2=2N\) at even levels and \(S_m^2=N\) at odd levels.
Also \(P_N(w_N(\alpha))=4\cosh^2(\alpha/2)\). Factoring its
double roots, and its odd simple root when present, yields
\[
 (-1)^{k_0}e_{k_0}(w_N(\alpha))=
 \begin{cases}
 \cosh(\alpha/2)/N,&N=2m,\\
 \cosh(\alpha/2)\cosh(\alpha/(2N))
                      /(N\cos^2(\theta/2)),&N=2m+1.
 \end{cases}
 \tag{10}
\]
These are polynomial identities after substitution, fixed by their
positive values at \(\alpha=0\), rather than a choice of a square-root
branch. The same sine products in (5) give
\[
 |b_{m-1,a}|=
 \begin{cases}
 \sin\tau_a,&N=2m,\\
 \sin\tau_a\sin(\tau_a/2)/\cos^2(\theta/2),&N=2m+1,
 \end{cases}
 \tag{11}
\]
proving (9). In particular the even central endpoint coefficient is
exactly \(1/N\), not merely of polynomial size.

Define
\[
 (A_l,B_l)=
 \begin{cases}
 ((l+\tfrac12)\theta,(l+1)\theta),&N=2m,\\
 ((l+1)\theta,(l+\tfrac32)\theta),&N=2m+1,
 \end{cases}
\]
\[
 \rho_{l,N}(\alpha,\tau)=
 \frac{[\cos^2 A_l+\sinh^2(\alpha/(2N))]
       [\sin^2(\tau/2)-\sin^2 A_l]}{\cos^4 B_l}.
 \tag{12}
\]
For \(l<p_a\), the next summand satisfies
\[
                    T_{l+1}=\rho_{l,N}T_l.
 \tag{13}
\]
Indeed, in the original \(r\) notation the ratio is simply
\[
 \frac{T_{r-1}}{T_r}
       =\frac{(w_N(\alpha)-c_r)(c_a-c_r)}{s_r^4}.
 \tag{14}
\]
The first factor follows by adding one Newton factor; the second
follows by dividing (5) at consecutive \(r\). Substitution of
\(r=m-1-l\) gives (12). At \(l=p_a\), its numerator has the exact
factor \(\sin^2(\tau_a/2)-\sin^2 A_{p_a}=0\).
At a zero of a summand, the ratio statements mean their multiplicative
identities, obtained first for real \(\alpha\) and then by analytic
continuation.

The ratios are even entire functions of each of \(\alpha,\tau\)
where their constant denominators are nonzero. These denominators
become small late in the full lowering process; the next section
avoids that part of the continuation.

## 3. Exact local interpolation and its nonzero symbol

For \(N\ge100\), put \(L_N=\lfloor N/20\rfloor\) and define
\[
 H_N(\alpha,\tau)=
       \sum_{l=0}^{L_N}\prod_{j=0}^{l-1}\rho_{j,N}(\alpha,\tau),
 \qquad
 \Gamma_N(\alpha,\tau)=T_0(\alpha,\tau)H_N(\alpha,\tau).
 \tag{15}
\]
An empty product is one. Formula (15) is a finite analytic
interpolant, not an asymptotic substitution for the summands.

**Theorem 1.** At every physical double-node angle
\(0<\tau_a\le1/10\),
\[
                     \Gamma_N(\alpha,\tau_a)=\gamma_{a,N}(\alpha)
 \tag{16}
\]
for all complex \(\alpha\). On the fixed bidisk
\(|\alpha|\le1, |\tau|\le1/5\),
\[
 |\rho_{j,N}|<\tfrac14\quad(0\le j<L_N),\qquad
 |H_N-1|\le\tfrac13,
 \tag{17}
\]
and
\[
             H_N(\alpha,\tau)=\sec^2(\tau/2)+O_{\rm hol}(N^{-2}).
 \tag{18}
\]
Here \(O_{\rm hol}\) means a holomorphic function with the indicated
uniform bound on this bidisk; every fixed derivative has the same
bound on a strictly smaller bidisk. Consequently
\[
 \Gamma_N(\alpha,\tau)=
 \begin{cases}
 \displaystyle\frac{\cosh(\alpha/2)}{N}\sin\tau
           [\sec^2(\tau/2)+O_{\rm hol}(N^{-2})],&N\ {\rm even},\\[4pt]
 \displaystyle\frac{\cosh(\alpha/2)}{N}\sin\tau\sin(\tau/2)
           [\sec^2(\tau/2)+O_{\rm hol}(N^{-2})],&N\ {\rm odd}.
 \end{cases}
 \tag{19}
\]
The bracketed factors are nonzero for all sufficiently large \(N\).
More directly, the exact factors \(H_N\) in (15) are nonzero by (17).
The interpolation is odd in \(\tau\) at even levels and even in
\(\tau\) at odd levels. The latter has its prescribed double zero
at \(\tau=0\); this is not a lost normal at an odd simple node.

*Proof.* From (8), \(p_a=(N\tau_a/\pi-1)/2\) at even levels and
\(p_a=N\tau_a/(2\pi)-1\) at odd levels. Thus
\(0\le p_a<L_N\) in (16). The factor at \(j=p_a\) in (12)
annuls every later product in (15), so (13) proves the exact identity.

For \(j<L_N\), \(0\le A_j<1/6\) and \(0<B_j<1/5\).
Hence \(\cos^4 B_j>(49/50)^4>9/10\).
For the complex arguments in the stated bidisk,
\(|\sin(\tau/2)|\le\sinh(1/10)<1/9\), and
\(|\sinh(\alpha/(2N))|<1/100\). Inserting these bounds and
\(\sin^2 A_j<1/36\) in (12) proves the first inequality in
(17), with room to spare. Summing the geometric majorant proves
the second. These elementary bounds also apply on a slightly
larger open neighborhood of the closed bidisk for each level.

Put \(z=\sin^2(\tau/2)\). On the same bidisk, Taylor estimates
for the real numbers \(A_j,B_j\), whose denominators stay away
from zero, give
\[
        |\rho_{j,N}-z|\le C(j+1)^2N^{-2},\qquad |z|<1/4.
 \tag{20}
\]
Telescoping the product, using (17) for all its other factors,
gives
\[
 \left|\prod_{j<l}\rho_{j,N}-z^l\right|
       \le C N^{-2}l^3(1/4)^{l-1}.
 \tag{21}
\]
The sum over \(l\) is \(O(N^{-2})\); the omitted geometric tail
\(\sum_{l>L_N}z^l\) is \(O(e^{-cN})\). Since
\((1-z)^{-1}=\sec^2(\tau/2)\), this proves (18).
Cauchy's formula on smaller bidisks proves the derivative assertion.
The odd extra factor in (9) satisfies
\(\cosh(\alpha/(2N))/\cos^4(\theta/2)=1+O_{\rm hol}(N^{-2})\),
which proves (19) and its parity statements. \(\square\)

Equivalently the leading profiles in (19) are
\[
 \frac{2\cosh(\alpha/2)}N\tan(\tau/2),\qquad
 \frac{2\cosh(\alpha/2)}N
                 \frac{\sin^2(\tau/2)}{\cos(\tau/2)},
 \tag{22}
\]
respectively. At \(\alpha=0\), these start as \(\tau/N\) and
\(\tau^2/(2N)\). All fixed angular and microscopic-height
derivatives are controlled by (19) after the displayed zeros are
factored out. Since every factor is even in \(\alpha\), the same
interpolant descends analytically to \(\alpha^2\). Moreover
\(N^2(w_N(\alpha)-2)=\alpha^2+O(\alpha^4/N^2)\) is a uniformly
invertible local coordinate in \(\alpha^2\). On smaller fixed
disks, each fixed ordinary derivative in the endpoint color \(w\)
therefore costs at most \(C_aN^{2a}\), including at \(w=2\).

## 4. The actual character, both parities, and the retained low part

At a physical angle one has exactly
\[
               (-1)^a=i^{-D}e^{iN\tau_a/2}.
 \tag{23}
\]
Thus the portion of (7) with \(\tau_a\le1/10\) is
\[
 \eta i^{-D}\sum_{\tau_a\le1/10}
            e^{iN\tau_a/2}\Gamma_N(\alpha,\tau_a)f(c_a).
 \tag{24}
\]
For an even angular spectator \(F(\tau)=f(-2\cos\tau)\), the
central summand has an exact even holomorphic continuation obtained
by replacing its character-amplitude product by
\[
 \begin{cases}
 i\sin(N\tau/2)\Gamma_N(\alpha,\tau)F(\tau),&N\ {\rm even},\\
 \cos(N\tau/2)\Gamma_N(\alpha,\tau)F(\tau),&N\ {\rm odd}.
 \end{cases}
 \tag{25}
\]
It agrees with the product in (24) at every positive physical
angle in the window. Both expressions in (25) are even; their
values at the reflected grid points consequently agree too. The
odd-level zero angle contributes zero because \(\Gamma_N(\alpha,0)=0\).
The sum (24) can therefore be written as half its symmetric central
grid sum, with no unaccounted half-grid endpoint at zero.

The trigonometric factors in (25), before multiplication by \(F\),
are in fact polynomials in \(\cos\tau\). At even levels this follows
from \(\sin(m\tau)\sin\tau=(1-\cos^2\tau)U_{m-1}(\cos\tau)\).
At odd levels use
\(2\cos(\tau/2)\cos((m+1/2)\tau)
 =\cos(m\tau)+\cos((m+1)\tau)\), together with the factor
\(\sin\tau\sin(\tau/2)\) in (9). The remaining factor \(H_N\)
is a polynomial in \(\sin^2(\tau/2)\).

This parity is essential. A half-charge cosine alone vanishes on
the even physical grid; its normal data cannot simply be dropped.
Equations (7) and (25) instead start with the full original trace,
consume the radical normal exactly, and only then express its
surviving values as a half-grid character. They do not assert an
identity between full Hermite coupons by matching values alone.

For completeness the noncentral part has only a polynomial weight
cost. The radical source proves
\(|e_{D-r}(-2\cos t)|\le\sqrt{N-1}e^{D|\Im t|}\).
At \(t=\pi-i\alpha/N\), this and \(|b_{ra}|\le2\) imply,
uniformly for \(|\alpha|\le1\),
\[
 |\gamma_{a,N}(\alpha)|\le C N^{3/2}.
 \tag{26}
\]
Hence the complete exact decomposition is
\[
 \begin{split}
 \phi_N(B_{N,\alpha}f)
  ={}&\phi_N(B^{\rm low}_{N,\alpha}f)
    +\eta i^{-D}\sum_{\tau_a\le1/10}
         e^{iN\tau_a/2}\Gamma_N(\alpha,\tau_a)f(c_a)
    +\mathcal R_N(f),\\
 |\mathcal R_N(f)|\le{}& C N^{5/2}
                     \max_{\tau_a>1/10}|f(c_a)|.
 \end{split}
 \tag{27}
\]
An empty maximum has value zero. Joint exterior variables and their
ordinary derivatives remain in \(f\) throughout these identities.

The local amplitude in (24) is controlled and carries an actual
nonzero Fourier frequency. This removes the artificial zero-frequency
description obtained by replacing the endpoint radical with an
arbitrary positive radical weight. The following exact contour formula
makes that frequency explicit without suppressing its side currents.

## 5. An exact central block with all aliases and both side currents

For \(N\ge100\), choose a positive grid midpoint \(b\le1/10\), so
\(e^{iNb}=-\eta\), and \(0<H\le1/10\). Suppose \(F(t)\) is even
and holomorphic on a neighborhood of the closed rectangle
\([-b,b]+i[-H,H]\). An original physical spectator, including a
real-power chirp, may use any such representative with its exact
physical values; its normal has already been consumed in (5).
Put
\[
 A_N(t)=\Gamma_N(\alpha,t)F(t),\qquad
 \mathcal S_N=\eta i^{-D}
       \sum_{0<\tau_a<b}A_N(\tau_a)e^{iN\tau_a/2}.
 \tag{28}
\]
Then
\[
 \boxed{\begin{split}
 \mathcal S_N={}&\frac{N i^{-D}}{2\pi}
       \int_{-b-iH}^{b-iH}
       \frac{A_N(t)e^{-iNt/2}}{1-\eta e^{-iNt}}\,dt\\
 &+\frac{\eta N i^{-D}e^{iNb/2}}{4\pi i}
       \int_{-H}^{H}\frac{A_N(b+ih)}{\cosh(Nh/2)}\,dh.
 \end{split}}
 \tag{29}
\]
Both the midpoint phase and the second integral are part of the
identity. No endpoint or vertical term has been discarded.

To prove it, use the residue-one grid kernel
\[
 J_N(t)=\frac{iN\eta}{e^{iNt}-\eta},\qquad
                    J_N(-t)=-J_N(t)-iN.
 \tag{30}
\]
The residue theorem on the counterclockwise rectangle sums all
physical grid points inside. The full sum is twice the sum in (28),
because \(A_N(-t)=\eta A_N(t)\) and
\(e^{-iN\tau/2}=\eta e^{iN\tau/2}\) on the grid. The odd-level
zero point has zero residue since \(A_N(0)=0\).
Reflecting the top side onto the bottom, and the left side onto the
right, gives in each case the same paired integrand
\[
 J_N(t)A_N(t)e^{iNt/2}
     -J_N(-t)A_N(-t)e^{-iNt/2}
       =\frac{2iN\eta A_N(t)e^{-iNt/2}}
                    {1-\eta e^{-iNt}}.
 \tag{31}
\]
On the right side \(t=b+ih\), the midpoint relation changes (31)
times \(dt=i\,dh\) into
\(N e^{iNb/2}A_N(b+ih)\,dh/\cosh(Nh/2)\).
Multiplying the whole residue formula by \(\eta i^{-D}/2\)
proves (29), including its orientation and normalization.

On the lower side the denominator in (29) has its absolutely
convergent expansion
\[
 \frac{e^{-iNt/2}}{1-\eta e^{-iNt}}
       =\sum_{j\ge0}\eta^j e^{-iN(j+1/2)t}.
 \tag{32}
\]
Thus the first effective charge is exactly \(1/2\), and every
alias is retained. The formula has no zero-charge horizontal term.
It does not establish an exponential bound on its vertical integral,
or combine the result with the low term in (27). In particular no
rate below the selected filled action follows without estimating
those terms and the actual spectator. The theorem concerns an exact
central block of the original high coupon, not a substitute closing.

## 6. Direct source versions

Both files below were read in full for this proof; the directly used
identities and their original trace normalization were checked.

* [Exact full-radical contraction](research_high_newton_radical_contraction.md),
  SHA256 `1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03`.
  Equations (2)--(6), (10)--(12), (17), and (34)--(36) give the
  original algebra, surviving normal, signs, parity split and Fourier
  bound used here.
* [Coherent endpoint kernel bounds](research_full_period_endpoint_kernel_reduction.md),
  SHA256 `a1d67ac803c0160bbfdacaa96a6fde9dc1ffae06fc39eb94f0416dcf2ecef76e`.
  Equations (1)--(6) and (15) fix the actual endpoint coupon and
  distinguish its low interpolation from its full normal data.
  Its polynomial bounds do not already provide the local amplitude
  or character in (19)--(25).
