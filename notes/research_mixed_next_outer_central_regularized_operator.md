# The grouped central outer operator and an endpoint-zero analytic probe

Private exact-source proof, 8 November 2026. The constrained conjugated
outer adjoint extends to even analytic angular germs through the
complete-color center. Its limiting multiplier has value \(4096\)
there. On fixed concentric disks the actual finite operator differs
from that multiplier by a Cauchy small-shift error. A finite Neumann
construction consequently gives a local test with the three original
endpoint zeros and an exponentially small residual.

The regularity is that of the grouped operator on even functions.
Individual shift coefficients can still have poles. The construction
uses the actual integer levels and does not assert joint removability
in two independent variables \(u,N^{-1}\). Its residual is measured
against the full analytic norm of the input; no comparison of its
exponential rate with an outer action excess is made.

## 1. The original constrained operator and its exact parity ratios

Keep the ordinary realizations and full Hermite algebra of
[current-free crossing transport](research_current_free_aw_crossing_transport.md)
and [the finite Newton remainder](research_mixed_next_outer_finite_newton_remainder.md):
\[
\begin{gathered}
N\ge6,\quad \theta=\pi/N,\quad q=e^{i\theta},\quad
M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\\
z(u)=-2\cos u,\qquad c_j=2\cos((2j+1)\theta),\\
Q_{3,N}^{\rm rev}(z)=\prod_{\nu=0}^{2}(z-c_{U-\nu}),\\
\mathcal B_N
 =q^{-2}\mathcal L_2(\mathcal L_3^2-I)
   +q^{-3}Z\mathcal L_3-8q^{-2}\mathcal L_3+(8q^{-1}+2)I .
\end{gathered}                                                     \tag{1}
\]
Here \(Z\) is multiplication by \(z\). In the original full quotient,
\[
               \mathcal B_N=R^{-3}\mathcal D_{3,N}^{\rm t}R^3.
                                                                    \tag{2}
\]
The order of the factors in (1) is part of this identity.

For an even angular function \(g\), initially away from all displayed
denominators, define
\[
(\mathcal C_Ng)(u)
 =\frac{\mathcal B_N\!
       \left(e_M(z(u))Q_{3,N}^{\rm rev}(z(u))g(u)\right)}
             {e_M(z(u))}.
                                                                    \tag{3}
\]
The meaning of (3) at its apparent poles will be proved below.

The exact radical formulas from
[far angles and verticals, equation (28)](research_mixed_next_outer_far_angles_and_verticals.md)
are
\[
E_N(u):=e_M(z(u))=
\begin{cases}
\cos(Nu/2)/N,&N\text{ even},\\[1mm]
-\sin(u/2)\sin(Nu/2)/
             \{N\cos^2(\pi/(2N))\},&N\text{ odd}.
\end{cases}                                                       \tag{4}
\]
Consequently, for every integer \(r\),
\[
\frac{E_N(u+2r\theta)}{E_N(u)}
=(-1)^r
\begin{cases}
1,&N\text{ even},\\[1mm]
\displaystyle\frac{\sin((u+2r\theta)/2)}{\sin(u/2)},
                                      &N\text{ odd}.
\end{cases}                                                       \tag{5}
\]
These are meromorphic identities, including continuation across
zeros of the original denominator. The factor with frequency \(N\)
has canceled exactly; it is not bounded by a separate absolute
estimate.

The three reversed endpoint factors are exactly
\[
Q_{3,N}^{\rm rev}(z(u))
 =\prod_{\nu=1}^{3}2\{\cos(\lambda_{\nu,p}\theta)-\cos u\},
\qquad
\lambda_{\nu,p}=
\begin{cases}
2\nu-1,&p=\mathrm{even},\\
2\nu,&p=\mathrm{odd}.
\end{cases}                                                       \tag{6}
\]
Thus the last three positive double angles are
\(\theta,3\theta,5\theta\) at even levels and
\(2\theta,4\theta,6\theta\) at odd levels.

The original ordinary operators used in (1) are
\[
\begin{split}
(\mathcal L_nf)(u)
={}&(c_0+A_N(u)+C_N(u))f(u)\\
 &-q^nA_N(u)e^{-inu}f(u-2\theta)
  -q^nC_N(u)e^{inu}f(u+2\theta),\\
A_N(u)&=\frac{4\cos^4((u-\theta)/2)}
                    {\sin u\sin(u-\theta)},\qquad
C_N(u)=A_N(-u),\qquad c_0=2\cos\theta .
\end{split}                                                       \tag{7}
\]
Expanding their finite composition and using (5) gives an exact
seven-shift realization of (3):
\[
(\mathcal C_Ng)(u)
 =\sum_{r=-3}^{3}a_{r,p}(u,N^{-1})g(u+2\pi r/N).
                                                                    \tag{8}
\]
Equations (1),(5)--(7) specify every coefficient, including its
phase, without introducing a different finite source.

For a sufficiently small fixed angular disk, the only possible
poles in these raw coefficients are at \(u=k\theta\),
\(|k|\le5\), and the additional odd-level denominator
\(\sin(u/2)\) at zero. Indeed the three occurrences of (7) have
coefficient arguments \(u,u\pm2\theta,u\pm4\theta\).
All shifted evaluations in (8) have distance at most \(6\theta\).
On a fixed annulus separated from zero the coefficients are jointly
analytic in \(u,\epsilon\) for small \(\epsilon\), using
\(\theta=\pi\epsilon\) and the appropriate parity formula.

This does not make each \(a_{r,p}\) holomorphic at zero. For example,
at an even level the extreme positive shift in
\(\mathcal L_2\mathcal L_3^2\) contains
\(C_N(u)C_N(u+2\theta)C_N(u+4\theta)\).
Its pole at zero is not canceled by
\(Q_{3,N}^{\rm rev}(z(6\theta))\), whose three zeros have odd
angular indices. The cancellation with the reflected shift uses
evenness of the test. We therefore retain the full sum (8).

## 2. Grouped removability for every even analytic test

The ordinary divisibility proved in
[the finite Newton remainder, equation (5)](research_mixed_next_outer_finite_newton_remainder.md)
states that, for every ordinary polynomial \(P\),
\[
\frac{\mathcal B_N(e_M Q_{3,N}^{\rm rev}P)}{e_M}
                         \in\mathbb C[z].
                                                                    \tag{9}
\]
Its source is the full grouped endpoint theorem, including the odd
simple node and every required first normal. In particular (9) is
ordinary divisibility before taking a remainder in the physical
algebra.

We first record the precise approximation needed to extend (9).
There is a fixed \(R_0>0\), chosen smaller than one, such that an
even function holomorphic on \(D_t=\{|u|<t\}\), \(t\le R_0\),
can be approximated uniformly on every smaller closed disk by
polynomials in \(z(u)\). To see this, put
\[
                         w=z(u)+2=2-2\cos u.
                                                                    \tag{10}
\]
As a function of \(v=u^2\), the right side is analytic with
derivative one at zero. It has an analytic local inverse
\(v=F(w)\). Choose a fixed inverse disk \(|w|<\rho\), and
then \(R_0\) so that the image of \(\overline{D_{R_0}}\) lies
in a strictly smaller disk \(|w|\le\rho'<\rho\).
The even Taylor polynomials in \(u\) approximate the given function
on every smaller closed \(u\)-disk. Each such polynomial is a
polynomial in \(u^2=F(w)\), and its Taylor polynomials in \(w\)
approximate it uniformly on \(|w|\le\rho'\).
A diagonal choice proves the assertion.
This argument does not require the original analytic function to
extend to the entire spectral disk \(|w|<\rho\).

Fix \(0<r<R<R_0\). For all sufficiently large physical \(N\),
let
\[
r\le s<s+\delta\le R,\qquad
              12\pi/N\le\delta\le1,
                                                                    \tag{11}
\]
and let \(g\) be even and holomorphic on \(D_{s+\delta}\).
All shifted evaluations from \(|u|\le s\) lie in
\(\overline{D_{s+\delta/2}}\), strictly inside its domain.
Apply the preceding approximation on that closed disk and write
the approximants as \(P_\ell(z(u))\).
By (9), every \(\mathcal C_N[P_\ell(z(u))]\) is an even
holomorphic function on the full disk.

For large \(N\), all raw coefficient poles lie in \(D_{r/2}\);
on \(|u|=s\) the finite coefficients in (8) are bounded.
Uniform convergence of the shifted inputs therefore gives uniform
convergence of their outputs on this circle. By the maximum
principle these outputs converge uniformly on the closed disk
\(\overline{D_s}\). On every compact subset avoiding the finitely
many raw poles, their limit is exactly (8). The limit hence supplies
its unique holomorphic continuation through all those poles.
It is even, since every polynomial output is even.

We have proved grouped removability at every sufficiently large
integer level, at both parities. No continuation of physical
divisibility to arbitrary complex \(\epsilon\) was used.

## 3. The actual central principal multiplier

On a fixed punctured disk let \(\epsilon\to0\) in the raw
coefficients of (8). The factor (6) tends to
\((2-2\cos u)^3\), and each ratio (5) tends to \((-1)^r\).
Set
\[
\begin{gathered}
x=\cos u,\quad a=\cot^2(u/2),\\
\ell=2+4a\cos^2(3u/2),\qquad
m=2+4a\cos^2u .
\end{gathered}                                                     \tag{12}
\]
The resulting multiplication operator is
\[
m_0(u)
 =(2-2\cos u)^3
       \{(\ell^2-1)m-(8+2x)\ell+10\}
 =\sum_{r=-3}^{3}a_{r,p}(u,0).
                                                                    \tag{13}
\]
In the convention of
[the all-character source, equation (3)](research_mixed_next_outer_all_character_symbol.md),
this is \((2-2\cos u)^3d(u,-e^{3iu})\).
It is the same at both parities. The sign in this character comes
from the exact factor \((-1)^r\) in (5).

The apparent central singularity of (13) can be removed explicitly.
Write
\[
\sigma=\sin^2(u/2),\qquad
A=\cos^2(u/2)\cos^2(3u/2),\qquad
B=\cos^2(u/2)\cos^2u .
\]
Then direct expansion of \(\ell=2+4A/\sigma\) and
\(m=2+4B/\sigma\) gives
\[
\boxed{\quad
m_0(u)=64\left[
64A^2B+(32A^2+64AB)\sigma
 +(12B-8xA)\sigma^2-4x\sigma^3
\right].
\quad}                                                            \tag{14}
\]
This is an even entire trigonometric expression, and
\[
                             m_0(0)=4096.
                                                                    \tag{15}
\]
Shrink \(R_0\), still retaining the approximation margin above,
so that
\[
                         |m_0(u)|\ge2048
                      \quad (|u|\le R_0).
                                                                    \tag{16}
\]
This is a fixed neighborhood assertion from (14)--(15), not a
quantitative claim about a large central contour.

A further exact principal fact will be useful for possible
continuation. Put \(t=u/2\) and, away from \(\sin t=0\), set
\[
k=\cot t\cos3t,\qquad h=-\sin3t,\qquad
w_1=k-h=\frac{\cos2t}{\sin t},\qquad
w_3=(4k^2+1)w_1+2k.
\]
The trigonometric identity
\(\cos^2t\,w_1^2-2\cos^2t\,kw_1=\cos^2t-k^2\)
and expansion of (13) give
\[
d(u,-e^{3iu})=4+4\cos^2t\,w_3^2.
                                                                    \tag{16a}
\]
For \(u=-2ix\), \(x>0\), write
\[
k=iK,\quad w_1=iW,\quad
K=\coth x\cosh3x>1,\quad
W=\frac{\cosh2x}{\sinh x}
  =\frac1{\sinh x}+2\sinh x>2.
\]
The last inequality follows from \(1+2s^2>2s\) for \(s>0\).
Then \(w_3=-iV\), where
\[
V=(4K^2-1)W-2K>8K^2-2K-2>4.
\]
Consequently (16a) is negative, whereas
\((2-2\cosh2x)^3<0\). Thus
\[
                    m_0(iy)>0\qquad(y\in\mathbb R).
                                                                    \tag{16b}
\]
Evenness gives the opposite half-axis, and (15) supplies its
central value. On every fixed bounded imaginary segment, continuity
therefore gives some thin complex neighborhood without a zero of
the principal multiplier. This is a principal assertion only;
the finite operator and inverse below are still proved on the
small disks specified in (11),(16).

## 4. Uniform small-shift control across the center

Use the supremum norm \(\|\cdot\|_s\) on \(D_s\).
For each fixed \(0<r<R<R_0\), there is a finite constant
\(C_{r,R}\), common to both parities, such that
\[
\boxed{\quad
\|(\mathcal C_N-m_0)g\|_s
 \le \frac{C_{r,R}}{N\delta}\|g\|_{s+\delta}
\quad}                                                            \tag{17}
\]
for all sufficiently large \(N\), all radii in (11), and every
bounded even analytic \(g\) on \(D_{s+\delta}\).

For the proof, first work on \(|u|=s\). The exact coefficient
expressions have a fixed jointly analytic neighborhood of the
compact annulus \(r\le|u|\le R\) at \(\epsilon=0\). Thus,
uniformly for these circles,
\[
|a_{r',p}(u,N^{-1})|\le C,\qquad
|a_{r',p}(u,N^{-1})-a_{r',p}(u,0)|\le C/N .
                                                                    \tag{18}
\]
Use (13) and subtract \(g(u)\) in each shifted term of (8).
The shift length is at most \(6\pi/N\), at most \(\delta/2\)
by (11). Cauchy's derivative estimate along the shifted segment
therefore gives
\[
|g(u+2\pi r'/N)-g(u)|
       \le \frac{4\pi |r'|}{N\delta}\|g\|_{s+\delta}
       \le \frac{12\pi}{N\delta}\|g\|_{s+\delta}.
                                                                    \tag{19}
\]
The first bound uses the derivative cost \(2/\delta\);
the last inequality uses \(|r'|\le3\).
Equations (18)--(19), summed over seven shifts, prove the boundary
estimate (17), increasing the constant to absorb \(1/N\) since
\(\delta\le1\). Section 2 makes its left side holomorphic on
the full disk. The maximum principle proves (17) there.

The estimate is thus uniform through the moving central poles,
although it was obtained on fixed circles avoiding them.
It does not bound the separate pole-bearing terms of (8).

## 5. A finite endpoint-zero analytic parametrix

The construction now follows the finite Neumann method in
[the adopted local probe](research_mixed_next_outer_local_adjoint_probe.md),
with the new central operator and its even analytic domain.
Fix \(0<r<R<R_0\), put \(\Delta=R-r\), and choose
\[
M_{r,R}\ge\max\{1,C_{r,R}/2048,12\pi\},\qquad
k_N=\left\lfloor\frac{\Delta N}{4M_{r,R}}\right\rfloor,\qquad
t_N=\Delta/k_N .
                                                                    \tag{20}
\]
For sufficiently large \(N\), \(k_N\ge1\). Each nested disk
loss \(t_N\) is at least \(12\pi/N\), so that (17) applies
at every step.

Multiplication by the inverse is performed first in
\[
                 \mathcal T_N=(\mathcal C_N-m_0)m_0^{-1}.
                                                                    \tag{21}
\]
This order retains its analytic variation under all shifts.
Equations (16)--(17) show that each application with disk loss
\(t_N\) has norm at most \(1/4\). All functions remain even.

For any bounded even analytic input \(F_N\) on \(D_R\), define
\[
g_N=m_0^{-1}\sum_{\ell=0}^{k_N-1}(-\mathcal T_N)^\ell F_N,
\qquad
\rho_N=(-\mathcal T_N)^{k_N}F_N .
                                                                    \tag{22}
\]
The finite sum defining \(g_N\) is analytic on \(D_{r+t_N}\);
the last remaining disk layer accommodates every shift in its
application on \(D_r\). Exact telescoping gives
\[
\boxed{\quad
\mathcal C_Ng_N=F_N-\rho_N,\qquad
\|g_N\|_r\le\frac1{1536}\|F_N\|_R,\qquad
\|\rho_N\|_r\le e^{-c_{r,R}N}\|F_N\|_R,
\quad}                                                            \tag{23}
\]
where one permissible fixed positive rate is
\[
                   c_{r,R}=\frac{\Delta\log4}{8M_{r,R}}.
                                                                    \tag{24}
\]
Indeed \(\mathcal C_Nm_0^{-1}=I+\mathcal T_N\).
The finite geometric identity yields precisely the residual
in (22). Nested disk estimates give successive norms \(4^{-\ell}\);
their sum times \(1/2048\) is \(1/1536\).
Finally \(k_N\ge\Delta N/(8M_{r,R})\) for all sufficiently
large \(N\), proving (24).

Set
\[
                  h_N(u)=Q_{3,N}^{\rm rev}(z(u))g_N(u).
                                                                    \tag{25}
\]
At all sufficiently large levels the last three positive double
angles lie in \(D_r\), so \(h_N\) vanishes there exactly.
The local identity, with all factors restored, is
\[
\mathcal B_N(E_Nh_N)
                 =E_N(F_N-\rho_N)\qquad\hbox{on }D_r .
                                                                    \tag{26}
\]
Both sides are interpreted by their proved holomorphic
continuations. No separate division at a physical zero occurs.
The three zeros in (25) are exactly those of the original endpoint
theorem, including its odd simple-node implication. They have not
been replaced by vanishing conditions on the target \(F_N\).

## 6. Source scope and the remaining global obligation

In particular, \(F_N(u)=H_N(-2\cos u)\), for the actual outgoing
polynomial, is an eligible even input. Equation (23) retains
its entire analytic norm on the chosen disk. If an independent
source estimate gives \(\|F_N\|_R\le C N^A e^{NE}\), the
residual bound is exactly
\[
                  \|\rho_N\|_r
                    \le C N^A e^{N(E-c_{r,R})}.
                                                                    \tag{27}
\]
Neither the radius choice nor \(C_{r,R}\) has been compared with
the required outer action budget. No sufficient residual rate is
inferred.

The test (25) is a local analytic germ, not a global polynomial
test in the full Frobenius pairing. Applying it to the entire
outer observation still requires a global completion or a justified
matching to other test regions, with every resulting boundary
term retained. The original crossing scalar, trace normalization,
and forcing are unchanged; no new full trace identity is asserted
by the local equation (26).

Finally, a single character \(e^{ibu}\) is generally not even.
The grouped removability proof cannot be applied to that character
alone. Actual Chebyshev modes occur with their two reflected
characters and are covered as even inputs, with their full analytic
norm kept in (23). No separate uniform carrier inverse follows
from this note.

## Source versions

The frozen source versions used here are:

- current_free_aw_crossing_transport:
  f81b9fc3edc2504c5250ad283bf0ceff191a1fc3a310c00fdb57602362f0bf4a.
- outer_adjoint_radical_endpoint_conditions:
  9cde443d65bfdc41104ffe9e78ce4e4540ec998b53681923f99fd42a5d436d71.
- outer_finite_newton_remainder:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.
- outer_far_angles_and_verticals:
  5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d.
- outer_all_character_symbol:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- outer_local_adjoint_probe:
  81acea1bc5255eaa72b6ac031d6b8b692ed1c40421c6beaf19e34b4118d7ec07.

No mathematical numerical evaluation, replay, or frozen-source edit
is used.
