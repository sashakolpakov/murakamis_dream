# The actual ordinary-binomial boundary of the complementary Gauss factor

Private written proof, 19 November 2026.

The complementary Gauss factor has a nonzero ordinary-binomial
boundary on a specified input sector at every fixed width. The
proof sums the entire physical input first and estimates its
original coefficient circles. Both endpoint characters, including
the possibly cancelling vacuum, are retained on the whole outer
circle. The nonzero coefficient comes from a proved strict gap.

This is a vacuum-output boundary estimate. It does not propagate
the complementary kernel to nonzero output, differentiate a root
identity in the meridian, or identify a geometric relative cycle.
The two complete directs are B and O, pinned below.

## 1. The exact complementary row and its physical input

Use
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1},\quad c_0=2\pi i,\quad f_j=(Q;Q)_j.
 \tag{1}
\]
Fix \(r\ge2\) tails, \(s=r-1\), \(p=r-2\), and physical integer
degree \(T=d-H\), where
\[
 0<\alpha_-\le H/N\le\alpha_+<1/2,\qquad H\ge p+1.
 \tag{2}
\]
All statements are at the root meridian \(M=1\). Retain the exact
parameters and nonzero scalar
\[
 \begin{split}
 K&=x^rQ^{-T},\quad C=Q^H,\quad h=H-p,\quad C'=Q^h,\quad
 \tau=T/N,\quad \chi=Q^{-H^2},\\
 P_p&=f_{2H-p-1}/f_H^2,\qquad
 \mathfrak P_N=(-1)^dN K^{-d}P_p,\\
 b_p&=(-1)^pQ^{pH-p(p+1)/2}f_H/f_h .
 \end{split}                                                   \tag{3}
\]
Neither \(C'\) nor \(\tau\) is replaced by its limiting value.
We take \(N\) sufficiently large that \(\tau\) lies in a fixed
compact subinterval of \((1/2,1)\), as follows from (2).

B defines the actual complementary operator
\[
 A^\vee=A_N(K^{-1},\Omega)|_{U_T}
   =(-1)^dN\sum_{n=0}^{d}
       {Q^{n(n-1)/2}x^{-n}\over f_n^2}
                         E^nF^nK^{-d+n}|_{U_T}.                \tag{4}
\]
It is the conjugate of the high-degree Gauss factor by the
literal turnover/degree coupon. It is not a scalar inverse of a
previous asymptotic kernel.

The operator (4) is symmetric in the original bilinear basis.
For one head the exact root actions give
\(E^t=x^{-1}KF\), \(F^t=xEK^{-1}\), and \(K^t=K\).
The ordered coproduct gives these same equations for the totals:
for example the term \(E_iK_{>i}\) transposes to
\(x^{-1}K_iF_iK_{>i}\), which is the corresponding term of
\(x^{-1}K_{\rm total}F_{\rm total}\).
Consequently
\[
 (E^nF^n)^t=(xEK^{-1})^n(x^{-1}KF)^n=E^nF^n .
 \tag{5}
\]
The two opposite commutation powers cancel. The remaining Cartan
factor commutes with this product and is diagonal. Every endpoint
arrow is included in this finite identity.

Let
\[
 |\beta\rangle=|\beta_1,\ldots,\beta_s,T-|\beta|\rangle,
 \qquad \beta_i\ge0,\quad |\beta|\le T,\qquad c_i=x^{r-i}.
 \]
B's exact first column and (5) give the full first row
\[
 A^\vee_{\mathbf0,\beta}
    =\mathfrak P_N\,g_{p,|\beta|}
                            \prod_{i=1}^{s}c_i^{\beta_i},
 \qquad G_{p,T}(t)=\sum_{a=0}^Tg_{p,a}t^a.                     \tag{6}
\]
This uses the same physical basis as the original source.
There is no positivity or orthogonality assertion.

On \(z_r\ne0\), retain the original ordinary-binomial input
\[
 c_T(z)=\sum_{|\beta|\le T}
    \binom d{T-|\beta|}\prod_{i=1}^s\binom d{\beta_i}
       z_r^{T-|\beta|}\prod_i z_i^{\beta_i}|\beta\rangle,
 \qquad \xi_i=c_i z_i/z_r .
 \tag{7}
\]
Set
\[
 \mathcal C^\vee_{r,N,T}(\xi)=
       {\langle\mathbf0|A^\vee c_T(z)\rangle
                    \over\mathfrak P_N z_r^T\binom dT}.
 \tag{8}
\]
The denominator is nonzero. It is not the vacuum entry:
\(\mathcal C^\vee(0)=G_{p,T}(0)\) can vanish at infinitely
many levels already in two tails, as B proves.

Define the exact finite polynomial
\[
 \mathcal B_{r,N,T}(v)=
   \binom dT^{-1}[u^T](1+u)^d\prod_{i=1}^s(1+uv_i)^d.
 \tag{9}
\]
Comparison of coefficients in (6),(7) proves the literal
two-circle identity
\[
 \boxed{\quad
 \mathcal C^\vee_{r,N,T}(\xi)
    =\operatorname{CT}_t\,
        G_{p,T}(t)\mathcal B_{r,N,T}(\xi_1/t,\ldots,\xi_s/t).
 \quad}                                                       \tag{10}
\]
Both coefficient circles are positively oriented about zero.
Every head cap and the total cap \(T\) are present. The outer
integrand is a finite Laurent polynomial, so its circle may be
changed to any nonzero complex radius without crossing another
pole. Equation (10) is obtained before any asymptotic substitution.

## 2. Complete local inputs and a bound for both complementary terms

We use O only for its ordinary-binomial polynomial (9), not for
its other Gauss operator. On a fixed small polydisk, O proves
\[
 \mathcal B_{r,N,T}(v)
       =e^{NS_B(v;\tau)}A_B(v;\tau)(1+O(N^{-1})),\qquad
 |\mathcal B_{r,N,T}(v)|\le C e^{N\Re S_B(v;\tau)}.              \tag{11}
\]
The errors are holomorphic with fixed derivatives on smaller
polydisks. Explicitly \(u(v)\) is the solution near
\(b=\tau/(1-\tau)>1\) of
\[
 {u\over1+u}+\sum_i{uv_i\over1+uv_i}=\tau .
 \]
With branches continued from \(v=0\),
\[
 \begin{split}
 S_B&=\Log(1+u)+\sum_i\Log(1+uv_i)-\tau\Log u
                     +\tau\Log\tau+(1-\tau)\Log(1-\tau),\\
 D_B&={u\over(1+u)^2}+\sum_i{uv_i\over(1+uv_i)^2},\\
 A_B&={\sqrt{\tau/(1-\tau)}
                \over(1+u)\prod_i(1+uv_i)\sqrt{D_B}}.
 \end{split}                                                   \tag{12}
\]
In particular \(S_B(0)=0\), \(\partial_{v_i}S_B(0)=b\), and
\(A_B(0)=1\). O's proof estimates the entire actual \(u\)-circle,
including its complement, and retains the \(d=N-1\) factors
displayed in (12).

For the complementary factor define, with the marks analytic at zero,
\[
 \psi(t;C')={\operatorname{Li}_2(t)
                  -\operatorname{Li}_2(C'^{-1}t)\over c_0},
 \qquad
 a_2(t;C')={1-C'\over1-C'+t}
                      \sqrt{{1-C'^{-1}t\over1-t}},
 \qquad a=\psi'(0;C')={1-C'^{-1}\over c_0}.
 \tag{13}
\]
The constant \(a\) is bounded above and away from zero under (2).
Its real part is positive for all sufficiently large \(N\).

Here the whole-circle bound follows from B's exact finite
connection, not just its selected-sector asymptotic. Recall that
\[
 G_{p,T}
   =\left[\delta_{p,N}\mathfrak g_T(Ct)
       -\chi b_p t^{-p}
          \big(F_h(t)-[F_h]_{<p}(t)\big)\right]_{\le T},
 \tag{14}
\]
where
\[
 F_h(t)=\mathfrak g_{T+p}^{\,C'}(t)/(Q^{1-h}t;Q)_h,\qquad
 \mathfrak g_{T+p}^{\,C'}(t)
       =\sum_{j=0}^{T+p}
          {(-1)^jQ^{j(j+1)/2}\over(C'Q;Q)_j}t^j .
 \]
Both auxiliary polynomials stop immediately before their first
zero denominator. B proves
\[
 |\delta_{p,N}|\le C N^p,\quad
 [t^j]F_h=O(N^j)\ (j\text{ fixed}),\quad
 F_h=e^{N\psi}a_2(1+\epsilon_N),\quad \|\epsilon_N\|\le C/N ,
 \tag{15}
\]
and the actual truncation error in (14) is \(O(e^{-\gamma N})\)
on a sufficiently small disk, for any fixed requested \(\gamma\).
The error in (15) is holomorphic on that disk. The normalized
\(\mathfrak g_T(Ct)\) is uniformly bounded there.

Consequently on every compact annulus within that disk the
literal finite polynomial has the decomposition
\[
 G_{p,T}(t)=-\chi b_p t^{-p}e^{N\psi(t;C')}
                     a_2(t;C')(1+\epsilon_N(t))
                     +\mathcal V_N(t),
 \qquad |\mathcal V_N(t)|\le C_{\rm ann}N^p .                   \tag{16}
\]
The Taylor subtractions, the other endpoint, and the cap error
are all included in \(\mathcal V_N\). In particular
\[
 |G_{p,T}(t)|
       \le C_{\rm ann}N^p\big(1+e^{N\Re\psi(t;C')}\big).        \tag{17}
\]
There is no assertion that the first term dominates on the
whole annulus. The poles \(t^{-p}\) in this separated description
cancel in the exact finite expression (14) at zero.

## 3. The original outer circle selects a nonzero coefficient

Choose a bounded open set of shapes \(\vartheta_i\) with
\(\sum_i\vartheta_i=1\), and work on compact subsets of that
affine shape domain. Fix \(0<\theta_0<\pi/3\) and use the
physical input sector
\[
 \xi_i={\vartheta_i a_*^2\over a b},\qquad
          0<|a_*|<a_0,\qquad |\arg a_*|<\theta_0 .
 \tag{18}
\]
The branch \(a_*\) is retained. These are open input coordinates
where \(\sum_i\xi_i\ne0\); individual \(\vartheta_i\) may vanish.
All estimates below are uniform on compact subsets of this
punctured sector. They are not uniform in a regime
\(N|a_*|=O(1)\).

Put
\[
 \Phi(t)=\psi(t;C')+S_B(\xi_1/t,\ldots,\xi_s/t;\tau).
 \tag{19}
\]
With \(t=(a_*/a)v\), the complete phase is
\(a_*(v+v^{-1})+O(a_*^2)\). Thus the exact saddle equation
\(D_t\Phi=0\), divided by \(a_*\), has its unique analytic
solution near \(v=1\):
\[
 t_*=(a_*/a)(1+O(a_*)),\qquad
 \Psi^\vee=\Phi(t_*)=2a_*+O(a_*^2),\qquad
 \mathcal H^\vee=D_t^2\Phi(t_*)=2a_*+O(a_*^2).
 \tag{20}
\]
The implicit derivative is \(2\) at \(v=1,a_*=0\).
The functions here are analytic for the stated physical
parameters and shape bundle; \(C'\) and \(\tau\) remain exact.

Use the actual outer circle \(t=t_*e^{i\theta}\).
For sufficiently small \(a_0\), its entire range lies in the
disk of (14)--(17), and all \(\xi_i/t\) lie in the polydisk
of (11). On a compact subset of (18) this circle stays a
positive distance from \(t=0\), so the annular constants in
(16),(17) are uniform. All phase and square-root marks are
the continuations from zero in (12),(13).

There are two independent whole-circle estimates. The combined
phase satisfies
\[
 \Re[\Phi(t_*e^{i\theta})-\Phi(t_*)]
 \le-[2\Re a_*-C|a_*|^2](1-\cos\theta),
                           \qquad -\pi\le\theta\le\pi.         \tag{21}
\]
Indeed its leading part is \(2a_*\cos\theta\); the periodic
analytic remainder has second derivative \(O(|a_*|^2)\).
Its first derivative at zero is zero by the exact saddle
equation. Integrating that bound gives (21), using comparability
of \(\theta^2\) and \(1-\cos\theta\) on this interval.

The entire phase-zero term in (16) instead has the bound
\[
 \max_\theta\Re S_B(\xi/t_*e^{-i\theta};\tau)
                         \le |a_*|+C|a_*|^2 .
 \tag{22}
\]
This follows directly from the linear term in (12), since
\(b\sum_i\xi_i/t_*=a_*(1+O(a_*))\).
Equations (18),(20),(22) give the strict gap
\[
 \Re\Psi^\vee-\max_\theta\Re S_B(\xi/t_*e^{-i\theta};\tau)
       \ge \tfrac12(2\cos\theta_0-1)|a_*|>0                    \tag{23}
\]
after decreasing \(a_0\). Thus every phase-zero endpoint and
Taylor subtraction is exponentially smaller than the selected
saddle, despite its possible \(N^p\) coefficient.

Choose a fixed small central arc. On its complement, (11),
(16),(21),(23) bound the whole original integrand by exponentials
with a strict gap below \(\Re\Psi^\vee\). This includes the
finite-cap error, whose prescribed exponent \(\gamma\) is
chosen first and whose activity disk is then used in (18).
On the central arc, \(\Re\psi(t_*e^{i\theta};C')>0\), and (16)
has the nonzero leading amplitude
\(-\chi b_pt^{-p}a_2\), with holomorphic relative error
\(O(N^{-1})\). These facts estimate the full original circle,
not just a formally chosen local saddle.

## 4. The actual boundary formula

Taylor expansion at the central saddle in (10), followed by
(21)--(23), now yields
\[
 \boxed{\quad
 \mathcal C^\vee_{r,N,T}(\xi)=
 {-\,\chi b_p\,e^{N\Psi^\vee}\over
                       \sqrt{2\pi N\mathcal H^\vee}}\,
    t_*^{-p}a_2(t_*;C')A_B(\xi/t_*;\tau)
                  (1+O(N^{-1})).
 \quad}                                                       \tag{24}
\]
The Gaussian square root is
\(\sqrt{2a_*}\sqrt{\mathcal H^\vee/(2a_*)}\), with the first
factor positive on positive real \(a_*\) and the second
continued from its value one at zero.
Its coefficient is one: (10) is the positively oriented original
constant-term circle, it passes once through the selected saddle,
and its whole complement has just been bounded.
All displayed amplitude factors are nonzero on the stated
compact sectors. The character \(-\chi b_p\) has not been put
into an unspecified normalization.

For clarity, one may take a central arc of width \(N^{-2/5}\).
The cubic and higher Taylor terms, together with the analytic
amplitude, have their usual integrated relative \(O(N^{-1})\)
error; the odd Gaussian terms cancel. The remaining central
neighborhood is \(O(e^{-cN^{1/5}})\), and the fixed complementary
arcs have the strict exponential gaps above. Holomorphic
parameter errors and fixed input derivatives follow on smaller
compact sectors by Cauchy.

Restoring the exact original factors, the result is
\[
 \boxed{\begin{split}
 \langle\mathbf0|A^\vee c_T(z)\rangle
 ={}&\mathfrak P_N z_r^T\binom dT\,
 {-\,\chi b_p\,e^{N\Psi^\vee}\over
                       \sqrt{2\pi N\mathcal H^\vee}}\,
       t_*^{-p}a_2(t_*;C')A_B(\xi/t_*;\tau)\\
 &\hspace{40mm}\cdot(1+O(N^{-1})).
 \end{split}}                                                 \tag{25}
\]
The normalization is defined even when the vacuum entry is zero.
The ordinary-binomial factors, \(d=N-1\), the physical phases
\(c_i=x^{r-i}\), the homogeneous character \(z_r^T\), the exact
shift \(C'=Q^{H-p}\), and both original endpoint characters
were retained before the selected estimate was taken.

The normalized phase is calibrated by
\(\Psi^\vee\to0\) as \(a_*\to0\); the asymptotic (24) is only
on the punctured sector. The exact two-circle polynomial (10)
continues to describe the microscopic region and its cancellations.
Neither (24) nor the separable monomial endpoint phase implies
a full complementary canonical graph or its failure. Nonzero
output propagation and the original exterior/routing convolution
are separate tasks.

This result is at fixed root \(q_N\), \(M=1\), and physical integer
degree \(T\). No meridian normal, complex-degree contour transport,
geometric-sector occurrence, or closed-source lower bound is inferred.

## Complete directs and author protocol

* B: notes/research_complementary_gauss_boundary_branches.md,
  862 lines, SHA256
  61c8b8cb82843e90611cbb1bde882273f3f751fd8a31d6a604aab6d74f43624e.
* O: notes/research_fixed_width_gauss_coherent_boundary.md,
  383 lines, SHA256
  03e0969c7b7c80d80b6cdb728661f125c15fee33b806dbd81f100bbb89b417c4.

Both complete matching directs were freshly wholly read,
nontruncated, in this active author sequence. Every used
implication was checked. The new transpose, exact full-input
pairing and two-term outer-circle estimates are proved here.
The entire matching final was freshly reread nontruncated and
all three hashes renewed. Independent matching peer review
and root adoption remain separate. Only written mathematics
and text/hash operations were used; frozen and public files
were unchanged.
