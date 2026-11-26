# Exact complex-degree interpolation of the actual two-tail Gauss kernel

18 November 2026. Private written proof.

The actual normalized Gauss kernels at physical integer degrees have
an exact holomorphic interpolant on any prescribed bounded-height
rectangle strictly above the half-degree wall. Its error from the
exact low-logarithm surrogate is exponentially small, with any
prescribed exponent after shrinking the activity variables. This
uses the full finite cap, not analytic continuation of an \(O(N^{-1})\)
error known only at physical degrees.

The ordinary-binomial input, the marked factorial vacuum scalar,
and the homogeneous degree are retained. A literal finite-degree
residue contour and its two external connectors are specified.
The interpolant is a chosen analytic representation of exact nodal
data. It is not a physical matrix at a noninteger occupation, nor
does its existence deform the original closed source to a geometric
cycle. The result is fixed-root and fixed-meridian.

Complete directs are K, B, F and R, pinned below. The earlier
physical-row analytic-degree interpolation note was read for
coverage; no estimate for its different rows is imported.

## 1. Physical data and the complex rectangle

Use
\[
 c_0=2\pi i,\quad Q=e^{c_0/N},\quad q=e^{c_0/(2N)},\quad
 d=N-1,\quad x=-q^{-1},\quad f_j=(Q;Q)_j.
\]
In the upper chamber below, K's actual two-tail Gauss block has normalized
monomial kernel
\[
 \mathcal K_{N,T}(\rho,\zeta)=
 \sum_{a,b=0}^{T}x^{-a-b}\frac{(A_N)_{ab}}{a_{00,T}}\rho^a\zeta^b,
 \qquad a_{00,T}=(-1)^d Q^{-(T+1)d}f_T^2.                 \tag{1}
\]
The vacuum formula applies in the strict upper chamber used below.
Fix
\[
 \tfrac12<a<b<1,\qquad H<\infty,\qquad
 \mathscr R=\{\sigma:a\le\Re\sigma\le b,\ |\Im\sigma|\le H\}.
                                                               \tag{2}
\]
Use a slightly larger rectangle \(\mathscr R^+\) with real part
still strictly between \(1/2\) and \(1\). All holomorphic estimates
are first proved on a larger rectangle and activity disk and then
restricted. Put
\[
 C=e^{-c_0\sigma},\quad \tau=\sigma-N^{-1},\qquad
 \mathcal T_N=\{T\in\mathbb Z:0\le T\le d,\
                  a\le (T+1)/N\le b\},\quad \sigma_T=(T+1)/N.
                                                               \tag{3}
\]
At the physical nodes these are exactly K's \(C,\tau_N\).
Neither \(C-1\) nor \(C+1\) vanishes on \(\mathscr R^+\).

**Theorem.** For every \(L>0\) there is a fixed activity radius
\(r_L>0\) and an explicitly constructed holomorphic
\(\mathfrak K_N(\sigma;\rho,\zeta)\) such that
\[
 \mathfrak K_N(\sigma_T;\rho,\zeta)=\mathcal K_{N,T}(\rho,\zeta)
                 \quad(T\in\mathcal T_N),                       \tag{4}
\]
and, uniformly on \(\mathscr R\) and
\(|\rho|,|\zeta|\le r_L\),
\[
 \mathfrak K_N=e^{N V_N^{[k]}}\{1+O(e^{-LN})\}
             =e^{NS(\rho,\zeta;C)}
                \mathcal A(\rho,\zeta;C)\{1+O(N^{-1})\}.          \tag{5}
\]
Here \(V_N^{[k]}\) is the finite exact low logarithm defined below;
\(S,\mathcal A\) are K's initialized Goursat phase and amplitude,
continued as the analytic germs at \(\rho=\zeta=0\).
The same relative estimates hold with every fixed derivative on
smaller rectangles and disks. Both kernels in (5) are units for
large \(N\). This assertion concerns the monomial kernel. Its
ordinary-binomial input has the exact contour and selected-sector
estimate in §4, not a zero-free full input disk.

## 2. Exact low coefficients before asymptotic expansion

Choose \(\delta>0\) so small that \(k_N=\lfloor\delta N\rfloor\)
is less than both \(T\) and \(d-T\) at every physical node in a
slightly enlarged real interval. It can also be chosen so that
\[
 |CQ^n-1|\ge c,\qquad c n\le
 |N(Q^n-1)(CQ^n-1)|\le C_1n,\qquad 1\le n\le k_N,              \tag{6}
\]
throughout \(\mathscr R^+\). Indeed
\(CQ^n=e^{-c_0(\sigma-n/N)}\); the real part of
\(\sigma-n/N\) remains in a compact subinterval of \((0,1)\).
Its angle is separated from zero modulo \(2\pi\), independently
of the allowed bounded imaginary part. Its modulus is also bounded
above and below on the rectangle.

B's exact initialized column is the truncation at \(T\) of the
product of a reciprocal finite Euler factor and a terminating
hypergeometric polynomial. Through degree \(k_N\), its coefficients
therefore extend by the literal formulas
\[
 \mathcal E_N(\rho)=
   \sum_{j<N}\frac{(-1)^jQ^{j(j+1)/2}}{f_j}\rho^j,\qquad
 b_j(C)=\frac{(C^{-1};Q)_j(QC)^j}{f_j(QC;Q)_j}.
                                                               \tag{7}
\]
Only \(j\le k_N\) is used in the second expression. Its
denominators are units by (6). At each physical node it is
exactly the \(j\)-th coefficient of B's \(B_{d-T}\).
This is an algebraic continuation of finitely many known
coefficients, with the physical high cap still to be compared.

For completeness the uniform complex-parameter bound follows
from the same finite Riccati equation, not from a real-node
bound. Let \(R_N(0)=1\) be its formal ratio. Through degree \(k_N\),
\[
 CR_N(\rho)R_N(Q\rho)-(1+C-Q\rho)R_N(\rho)+1-CQ\rho=0.           \tag{8}
\]
Writing \(u=R_N-1\), its exact linear coefficient inverse is
\((CQ^n-1)^{-1}\). The remaining row is
\[
 (C T_Q-1)u=-Q\rho(1-C)-Q\rho u-CuT_Qu.
\]
The positive majorant \(cU=C_2\rho(1+U)+C_2U^2\),
\(U(0)=0\), bounds all these low coefficients. It is analytic
on a uniform disk and is less than \(1/2\) after shrinking it.
Thus \(\log R_N\) has the same kind of bound. Dividing its
\(n\)-th coefficient by \(N(Q^n-1)\) gives a uniformly bounded
low logarithm. The reciprocal Euler logarithm contributes exactly
\[
 \frac1N\sum_{n\le k_N}\frac{Q^n\rho^n}{n(Q^n-1)}.               \tag{9}
\]
Consequently the continued initialized low logarithm has
coefficients bounded by \(C_3R_0^{-n}\), uniformly on
\(\mathscr R^+\), and value bounded by \(C_4|\rho|\).

Now continue the exact Goursat logarithmic recursion. K proves,
for the actual polynomial, the identity
\[
 \zeta\mathscr D_\rho^0\mathcal K
   -\rho\mathscr D_\zeta^0\mathcal K=0,\qquad
 \mathscr D_t^0L=
 C(1-Qt)(1-Q^2t)L(Q^2t)
 -(1+C)(1-Qt)^2L(Qt)+(1+Qt^2)L(t).                 \tag{10}
\]
For \(V=N^{-1}\log\mathcal K\), the only new total-degree
\(i+j+1\) coefficients in the row divided by \(\rho\zeta\) are
\[
 Nm_{i+1}v_{i+1,j}-Nm_{j+1}v_{i,j+1},
 \qquad m_n=(Q^n-1)(CQ^n-1).                                  \tag{11}
\]
The known first axis and (11) define successively every
coefficient of total degree at most \(k_N\), as a holomorphic
function of \(\sigma\). Call their polynomial \(V_N^{[k]}\).
At every node it is the exact truncated logarithm of (1).

Here is the uniform bound needed for this continuation. Write
\(M_0>0\) for an enlarged positive majorant constant, distinct
from the clock \(C\). After
the linear terms (11) are removed, the exponentiated increments
have majorant
\[
 M_0(\rho+\zeta)+F(\rho,U_\rho)+F(\zeta,U_\zeta),\qquad
 F(t,p)=M_0(1+t)^2\frac{e^{M_0tp}-1-M_0tp}{t}+M_0(t+t^2)p.
\]
Thus
\[
 U_\zeta=M_0 U_\rho+M_0(\rho+\zeta)+F(\rho,U_\rho)+F(\zeta,U_\zeta),
 \qquad U(\rho,0)=M_0\rho/(R_0-\rho)                            \tag{12}
\]
dominates the finite coefficient induction, by (6).
The derivative of its last term in \(U_\zeta\) is \(O(\zeta)\);
solve for \(U_\zeta=\mathcal H(\rho,\zeta,U_\rho)\) by contraction.
The analytic characteristic equations
\(\dot\rho=-\mathcal H_p,\ \dot p=\mathcal H_\rho,\
\dot U=\mathcal H-p\mathcal H_p\) have bounded coefficients on
a fixed polydisk. Their convergent Picard iteration and the
projection derivative \(1+O(\zeta)\) give an analytic solution.
Positive coefficient induction then proves
\[
 |[\,\rho^i\zeta^j\,]V_N^{[k]}|\le C_5R_1^{-i-j},
 \qquad |V_N^{[k]}|\le C_6r\quad (|\rho|,|\zeta|\le r).           \tag{13}
\]
Only low indices were inverted. These arguments are uniform on
the entire prescribed complex rectangle.

The phase and transport comparison also works there. The
initialized algebraic root \(Y_B(0)=1\) has derivative \(C-1\);
K's characteristic has
\(\Lambda_p(0,p)=c_0(C-1)\). Their analytic existence radii
are uniform on this compact \(C\)-set. Substitution of
\(S+N^{-1}\log\mathcal A\) in (10) has \(O(N^{-2})\) residual,
uniformly analytic. The boundary residual follows directly from
(8),(9), with B's retained half-logarithms. Subtracting equations,
the exact linear row remains (11); all other error multipliers
have a factor \(\rho\) or \(\zeta\). The linear positive version
of (12), with \(O(N^{-2})\) forcing, bounds the coefficient
error by \(N^{-2}C_7R_2^{-i-j}\). Summing on a smaller disk gives
\[
 V_N^{[k]}=S+N^{-1}\log\mathcal A+O(N^{-2})+O(e^{-cN}).          \tag{14}
\]
The exponential term is the tail of the uniformly analytic
approximate solution above degree \(k_N\). This repeats the
finite stability argument on a complex parameter rectangle;
it does not continue an error from isolated real nodes.

## 3. Full cap and exact cardinal correction

At physical nodes K's original finite coefficient estimate is
\[
 \left|x^{-a-b}(A_N)_{ab}/a_{00,T}\right|\le e^{C_8N},
                       \qquad0\le a,b\le T.                    \tag{15}
\]
Its proof uses the actual finite operator formula and the global
sine-factorial bounds. The constant is uniform over the enlarged
real interval. Fix a comparison bidisk of radius \(R_3<1\).
The actual polynomial and
\(\widehat{\mathcal K}_N=\exp(NV_N^{[k]})\) agree through
total degree \(k_N\), and both are bounded by \(e^{C_9N}\)
on that bidisk. Cauchy therefore gives, at the physical nodes,
\[
 \left|\mathcal K_{N,T}-\widehat{\mathcal K}_N(\sigma_T)\right|
 \le C(k_N+2)e^{C_9N}
       \frac{(r/R_3)^{k_N+1}}{(1-r/R_3)^2}.                    \tag{16}
\]
By (13), the inverse surrogate costs at most \(e^{C_6Nr}\).
After \(\delta,\mathscr R^+,R_3\) have been fixed, shrinking
\(r\) makes
\(\delta\log(R_3/r)-C_9-C_6r\) arbitrarily large.
Thus for any chosen \(\gamma>0\) the full nodal relative
error in (16) is at most \(e^{-\gamma N}\), for large \(N\).
This is where the original high coefficients and every cap
are paid.

Let \(\operatorname{sinc}z=\sin(\pi z)/(\pi z)\), with its
removable value at zero, and set
\[
 \boxed{\quad
 \mathfrak K_N(\sigma)=\widehat{\mathcal K}_N(\sigma)
 +\sum_{T\in\mathcal T_N}
   \left[\mathcal K_{N,T}-\widehat{\mathcal K}_N(\sigma_T)\right]
                         \operatorname{sinc}(N\sigma-T-1).
 \quad}                                                       \tag{17}
\]
All activity variables in the bracket are unchanged.
This finite formula is holomorphic and proves (4) exactly.
Since
\[
 |\operatorname{sinc}z|\le e^{\pi|\Im z|},
 \qquad
 |\widehat{\mathcal K}_N(\sigma_T)/
                  \widehat{\mathcal K}_N(\sigma)|\le e^{2C_6Nr},
\]
(16),(17) imply
\[
 \left|\frac{\mathfrak K_N}{\widehat{\mathcal K}_N}-1\right|
 \le C N e^{-N(\gamma-\pi H-2C_6r)}.                            \tag{18}
\]
Take \(\gamma>L+\pi H+2C_6r+1\), also on a buffered rectangle,
by shrinking \(r\). This proves the first equality in (5);
(14) gives the second and Cauchy proves all fixed derivatives.

No uniqueness off the grid is asserted. Another function
vanishing at the same nodes changes the interpolant, and its
contour must be changed consistently. Formula (17), not an
unmarked substitution of \(C\) into a high-degree matrix, is
the chosen representation.

## 4. Exact ordinary-binomial input at complex degree

The actual binomial interface has a particularly simple exact
continuation. With \(\tau=\sigma-N^{-1}\), define the finite
polynomial of degree at most \(d\)
\[
 \mathcal B_N(t;\tau)=
 \sum_{j=0}^{d}\frac{(1-N)_j(-N\tau)_j}
                         {j!\,[N(1-\tau)]_j}t^j.                \tag{19}
\]
Pochhammer symbols here are ordinary rising products.
The denominators are units on the rectangle, since
\(\Re(1-\tau)>0\). At \(\sigma_T\) its numerator stops at \(T\),
and exactly
\[
 \mathcal B_N(t;T/N)=\binom dT^{-1}
               \sum_{j=0}^{T}\binom dj\binom d{T-j}t^j.         \tag{20}
\]
Thus neither the binomial dual nor its top cap is suppressed.

We give the complex-parameter estimate used in its composition.
Its coefficient recurrence proves
\[
 t(1-t)\mathcal B_N''+
 [N(1-\tau)+(N(1+\tau)-2)t]\mathcal B_N'
                  -(N-1)N\tau\,\mathcal B_N=0.                 \tag{21}
\]
Let \(p(t)\) be the analytic root at \(p(0)=\tau/(1-\tau)\) of
\[
 t(1-t)p^2+[(1-\tau)+(1+\tau)t]p-\tau=0,
 \quad S_B(t)=\int_0^t p(v)\,dv,                                \tag{22}
\]
and define \(\mathcal A_B(0)=1\) by
\[
 [2t(1-t)p+(1-\tau)+(1+\tau)t]\,\partial_t\log\mathcal A_B
             =-t(1-t)p'+2tp-\tau.                              \tag{23}
\]
Both are analytic on a common disk; the relevant denominator at
zero is \(1-\tau\). They retain \(d=N-1\) and \(\tau\) exactly.

Here is a finite proof, without a real-circle assumption.
For \(W=N^{-1}\log\mathcal B_N\), (21) becomes
\[
 t(1-t)(W'^2+N^{-1}W'')
 +[(1-\tau)+(1+\tau)t-2t/N]W'-\tau+\tau/N=0.
\]
The coefficient of the newly solved \([t^{n+1}]W\) is
\((n+1)(1-\tau+n/N)\); its modulus is at least
\(c(n+1)\) on the entire rectangle. Terms with an additional
\(t\), and the quadratic \(tW'^2\), have a positive analytic
first-order majorant. For \(n\le\delta N\), the remaining
\(N^{-1}t^2W''\) term costs at most a constant times
\(tW'\) in the same majorant. This proves a common analytic
bound for the low logarithm, by scalar coefficient induction.
Also the coefficients in (19) are bounded by \((C N)^j/j!\):
bound its two numerator factors by \(C N\) and its
denominator factors by \(cN\). Hence its complete polynomial
is bounded by \(e^{C N}\) on a fixed comparison disk.
The exact low-log truncation and the whole polynomial agree
through \(\delta N\). The Cauchy tail comparison (16) therefore
applies in one variable, now for every complex \(\tau\).
Substitution of (22),(23) gives \(O(N^{-2})\) logarithmic
residual. The same triangular linear inverse and analytic
majorant give \(O(N^{-2})\) logarithmic error. Consequently
\[
 \mathcal B_N(t;\tau)=e^{NS_B(t;\tau)}
                  \mathcal A_B(t;\tau)(1+O(N^{-1}))              \tag{24}
\]
on a fixed disk, with all fixed derivatives. This is an
actual polynomial estimate throughout the complex rectangle.

Choose a coefficient circle within the \(\zeta\) disk and define
\[
 \mathfrak C_N(\sigma;\rho,\eta)=
 \operatorname{CT}_\zeta\,
       \mathfrak K_N(\sigma;\rho,\zeta)
                       \mathcal B_N(\eta/\zeta;\tau).           \tag{25}
\]
It is holomorphic for sufficiently small \(\eta,\rho\).
At every physical node it is precisely K's normalized
ordinary-binomial coherent kernel. All \(\zeta\)-coefficients
needed by the finite polynomial (19) are extracted; no cap
has been replaced by an infinite state.

There is also a selected actual circle with a unit amplitude.
Put \(c_*=2/c_0,\ c(\rho;C)=S_\zeta(\rho,0;C)\),
\(b_\tau=\tau/(1-\tau)\), and \(a_*^2=b_\tau c_*\eta\).
For a sufficiently small output disk and a compact subset of
\(0<|a_*|<a_0,\ |\arg a_*|<\theta<\pi/2\), the phase
\[
 S(\rho,\zeta;C)+S_B(\eta/\zeta;\tau)
\]
has the saddle
\[
 \zeta_*=\frac{a_*}{\sqrt{c_*c(\rho;C)}}(1+O(a_*)),\quad
 \Psi=S(\rho,\zeta_*;C)+S_B(\eta/\zeta_*;\tau),\quad
 \mathcal H=(\zeta\partial_\zeta)^2
            [S+S_B]_{\zeta_*}.                                 \tag{26}
\]
The square-root marks continue from \(c(0)=c_*\).
On the complete circle \(\zeta=\zeta_*e^{i\theta'}\) the real
phase gap is at most
\[
 -[2\Re(a_*\sqrt{c(\rho)/c_*})-C|a_*|^2](1-\cos\theta').
\]
It is strict after shrinking. This follows by subtracting the
leading cosine and using the exact critical equation to remove
the linear remainder. Both actual factors have (5),(24) on
the entire circle. Taylor's formula and the strict complementary
gap therefore give
\[
 \mathfrak C_N=
 \frac{e^{N\Psi}\mathcal A(\rho,\zeta_*;C)
                    \mathcal A_B(\eta/\zeta_*;\tau)}
             {\sqrt{2\pi N\mathcal H}}\,(1+O(N^{-1})).            \tag{27}
\]
The Gaussian coefficient is one, with its branch continued from
positive real \(a_*\) at \(\rho=0\). The exponential correction
in (18) is negligible in this same paired estimate.
For a given bounded rectangle, a common nonempty fixed
\(\eta\)-sector exists: \(b_\tau\) avoids the negative real axis
and has bounded argument strictly between \(-\pi,\pi\);
take \(c_*\eta\) in a sufficiently narrow sector about the
positive ray. There is no assertion uniform as \(N|a_*|\to0\),
or that an arbitrary geometric input lies in this sector.

## 5. Vacuum, homogeneous and contour marks

F's exact factorial \(\widehat F_N\) is holomorphic and zero-free
on \(-1<\Re z<N\), with \(\widehat F_N(T)=f_T\).
The continued vacuum and ordinary-binomial scalar are
\[
 \mathfrak a_{00,N}(\sigma)=
 (-1)^d e^{-c_0d\sigma}\widehat F_N(N\sigma-1)^2,\qquad
 \mathfrak b_N(\sigma)=
 \frac{\Gamma(N)}
      {\Gamma(N\sigma)\Gamma(N(1-\sigma)+1)}.                    \tag{28}
\]
They are holomorphic units on the rectangle for large \(N\),
and have exactly the values in (1),(20). On \(w_2z_2\ne0\),
choose and retain one logarithm \(\ell=\Log(w_2z_2)\).
The source-marked interpolated kernel is
\[
 \mathfrak P_N(\sigma)=
 \mathfrak a_{00,N}(\sigma)
 e^{(N\sigma-1)\ell}\mathfrak b_N(\sigma)
                  \mathfrak C_N(\sigma;\rho,\eta),\quad
 \rho=xw_1/w_2,\quad \eta=xz_1/z_2.                             \tag{29}
\]
At every node it is the original output evaluation paired with
the original ordinary-binomial input. Changing \(\ell\) by
\(2\pi i h\) multiplies (29) by \(e^{2\pi i hN\sigma}\);
this equals one at the nodes but is an actual contour character
off them. It is not discarded.

For clarity the vacuum's extensive phase is also fixed.
Let \(U=e^{c_0\sigma}\) and
\(I(\sigma)=[\operatorname{Li}_2(1)-\operatorname{Li}_2(U)]/c_0\)
with F's strip marking. Its exact shift and complex expansion give
\[
 \mathfrak a_{00,N}=
 (-1)^d\frac{iNU}{1-U}
       e^{N[2I(\sigma)-c_0\sigma]}(1+O(N^{-1})).
\]
Stirling's formula in the right-half-plane sectors gives
\[
 \mathfrak b_N=
 (2\pi N)^{-1/2}\sqrt{\frac{\sigma}{1-\sigma}}\,
 e^{N[-\sigma\Log\sigma-(1-\sigma)\Log(1-\sigma)]}
 (1+O(N^{-1})).                                                \tag{30}
\]
All logarithms and roots continue from the real interval.
Together with (27), these exhibit the full phase and all
nonzero prefactors of (29); no factorial scalar is called
a bounded unit. Fixed \(\sigma\) derivatives are allowed,
not meridian or moving-root derivatives.

If \(h_N(\sigma)\) is a holomorphic spectator on the same
rectangle, matching its specified physical values, then exactly
\[
 \sum_{T\in\mathcal T_N}\mathfrak P_N(\sigma_T)h_N(\sigma_T)
 =\frac1{2\pi i}\int_{\Gamma_N}
    \frac{c_0N}{e^{c_0N\sigma}-1}\,
             \mathfrak P_N(\sigma)h_N(\sigma)\,d\sigma.           \tag{31}
\]
The positively oriented contour surrounds exactly these nodes;
it lies in the buffered rectangle and no other pole is included.
One may take a rectangle whose vertical sides are the adjacent
half-grid lines. Every displayed kernel pole has residue one.
On such a side its denominator has modulus
\(1+e^{-2\pi N\Im\sigma}\). Thus its vertical bound is explicit:
it is \(O(N)\) above and \(O(Ne^{-2\pi N|\Im\sigma|})\) below.
The top and bottom horizontal pieces and both external
vertical connectors are retained with their orientations.
Artificial interior connectors cancel only when the same
interpolant and spectator are used on both sides.

Replacing \(\mathfrak K_N\) by its surrogate in a *fixed compact
local factor* costs the arbitrarily specified exponential in
(18), including (27)'s selected coefficient circle. This does
not bound an unknown spectator or an exponentially cancelling
closed sum. Formula (31) pays a source-exact contour for these
degree data, not an estimate of its original exterior contractions.

## 6. Nonreal moment reached, and what remains

R's physical two-tail moment is \(T/N\). On a resolved
total-lowering-zero three-head presentation, its principal total
Cartan is \(k_P=-e^{-c_0\sigma}\). Thus this interpolation can
reach a specified marked value
\[
 \sigma_*=-c_0^{-1}\Log(-k_P)
\]
by a vertical path whenever its real part lies in the strict
upper chamber (after its retained integer log choice) and its
imaginary part is finite. The radius of the activity chart
may shrink with that prescribed height. If neither eigenvalue
has real phase in the chamber, this theorem does not cross
the half-degree or endpoint wall. In particular a real
loxodromic eigenvalue puts its reciprocal pair on one of
those real-phase walls. For a nonreal eigenvalue, one of
the reciprocal phases lies in the upper half of a period,
but this alone does not put its actual angular coordinates
in (27)'s small activity sector.

R's radial polynomial sums the original closed degree blocks;
it does not identify them with this single factor. Equations
(17),(29),(31) now remove one specific missing interpolation
step for the actual Gauss kernel. To estimate the radial source,
the remaining braid, turnover, inverse-Jacobian and closing
factors must share a controlled marked continuation, and the
actual angular cycle and the connectors in (31) must be
estimated. Excluded degree blocks remain the exact
complementary part of that source. No geometric coefficient,
noncancellation, filling estimate, meridian normal, or
higher-width kernel follows here.

## Complete proof directs and protocol

* K: notes/research_actual_gauss_coherent_goursat_kernel.md,
  552 lines, SHA256
  37ade960cb7938372b7854b00aebc1df82e648144f850fcd4a356f68a00159e1.
* B: notes/research_actual_gauss_first_column_unit.md,
  415 lines, SHA256
  ebe3b496a739d1734738e4b663c7a7fd6713e44549b72ee2e93ae90314a15047.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  226 lines, SHA256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.
* R: notes/research_reduced_projective_occupation_source.md,
  600 lines, SHA256
  e9563cc9bdacb7a8afd15f1a199fd351ed963dbf8a07d761ecc69e4fa5ae6113.

Only written mathematics and text operations are used. Frozen
and public files are unchanged. The entire matching final and
all four complete directs were freshly read nontruncated in
this author sequence; every used implication was checked and
all five pins renewed. Independent matching peer and root
adoption remain separate.

