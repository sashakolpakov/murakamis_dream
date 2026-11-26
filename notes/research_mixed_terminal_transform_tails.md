# Strict tails for the coherently contracted terminal transform

Research deduction, 5 November 2026. The first and last physical-index
tails of the exact terminal transform satisfy the desired supporting-plane
bound on the full real plateau at the actual reference height. The proof
uses coherent cap estimates near zero and exact physical truncation near
one. It leaves the central transform coherent and unresolved. No new
root, parameter cover or word enumeration is used.

## 1. The exact source and its reference

Use the negative-band polynomial from
[reversed-cap assembly, Proposition 1](research_mixed_reversed_cap_assembly.md):
\[
 \mathcal V_{\epsilon,N}(w,X)=
 \sum_{i=0}^{N-1}\frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                       \mathcal U_{\epsilon,N}(w,r^i),
 \quad r=e^{-2\pi i/N},\quad P_i=(r;r)_i,\quad
 p_i(X)=(rX;r)_i .
 \tag{1}
\]
Its own type is \(3+\epsilon\). It sums the original terminal
conditional factor, endpoint polynomial, full terminal diagonal and
terminal Fourier alternative exactly. No parity or forcing term is
deleted.

The original endpoint map is defined on both disks
\[
 D_3=\{|a-(.35-.01i)|\le.09\},\qquad
 D_4=\{|a-(.30-.052i)|\le.064\}.
 \tag{2}
\]
Let its original private, attached and auxiliary coordinates be
\(e(a),t(a),u(a)\). The optimized action is
\[
\begin{split}
 P_\epsilon(a)={}&S(e)+g(t+a)+g(t+e)-(2+\epsilon)g(t)+2\pi iat\\
 &-g(a)-(1+\epsilon)g(e)+J(e),\\
 S(e)={}&F(e,u_c(e)),\qquad g(z)=J(z)+i\pi z(1-z)/2 .
\end{split}
 \tag{3}
\]
These are exactly the branches and allocation of the
[terminal supporting-plane theorem](research_terminal_supporting_plane.md).
The input \(a\) has not yet received its neighboring halfweight.

For the final source statement, \(a_*=A+ic\) is an actual external
reference of an open word of length \(m\ge2\), and \(\nu\) is its
type minus three. The actual ordinary and attached ranges give
\[
 .24\le A\le.433,\quad |c|<.12,\qquad
 .246<\Re t_*<.391,\quad -.108<\Im t_*<.021 .
 \tag{4}
\]
When \(\nu=1\), \(c<0\). These inclusions follow from
[local factor coverage](research_mixed_open_local_factor_coverage.md),
the [ordinary height theorem](research_mixed_cyclic_critical_height_bounds.md)
and the [endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md).
They include the length-two attached input. No private coordinate is
being used as the external leg of this map.

## 2. A reference floor and a reference slope bound

**Lemma 1.** On either entire disk (2),
\[
                         \Re P_\epsilon(a)>107/100 .
 \tag{5}
\]
At every actual reference (4),
\[
                         |\Re P_\epsilon'(a_*)|<21/25 .
 \tag{6}
\]

*Proof of the floor.* Define the original shared action
\[
 W(t,a)=J(t+a)-J(t)-J(a)+i\pi at .
\]
The complete cap action satisfies the exact identity
\[
       P_\epsilon(a)=\mathcal T_\epsilon(t,-2)
                                  +W(t,a)-\epsilon g(t).
 \tag{7}
\]
Substitute the cap definition
\(S(e)+J(e+t)-J(t)-i\pi et-\epsilon g(e)\) and the definition
of \(g\) to verify every quadratic term. There is no additive
phase adjustment.

The [complete cap theorem](research_mixed_complete_first_cap_packet.md)
and its [cut certificate](research_mixed_cap_real_cut_gaps.md)
give \(\Re\mathcal T_\epsilon(t(a),-2)>1\) on every endpoint
image over (2). We claim
\[
 J(x+z)-J(x)-J(z)>1/5
                       \quad(.23\le x,z\le.45).
 \tag{8}
\]
The expression is jointly concave by the
[open pair Hessian estimate](research_mixed_open_word_hessian.md),
so it suffices to check its corners. Elementary integral bounds give
\[
 -J(.23)>17/144,\quad J(.46)>-7/250,\quad
 -J(.45)>3/100,\quad -J(.10)>7/50,\quad -J(.32)>1/12.
 \tag{9}
\]
For the first, integrate over \([1/4,1/3]\) and \([1/3,1/2]\),
using \(\log\sqrt2>1/3\), \(\log\sqrt3>13/24\).
These follow from the first positive terms of the
\(\operatorname{artanh}\) series for \(\log2,\log3\).
The second uses \(\log2<7/10\).
The third uses \(2\sin(.45\pi)>19/10\) and
\(\log(19/10)>18/29>3/5\).
For the fourth integrate \(\log(2\sin\pi x)\le\log(2\pi x)\)
to obtain
\(-J(.1)\ge[1-\log(\pi/5)]/10>7/50\), since
\(\pi/5<2/3\) and \(\log(3/2)>2/5\).
For the last, integrate over \([1/3,1/2]\).
All omitted portions in the lower integrals have positive integrand.

The corner values in (8) therefore exceed respectively
\(17/72-7/250\), \(7/50+6/100\), and
\(1/12+17/144+3/100\), each at least \(1/5\), strictly.
Here \(J(.9)=-J(.1)\) and \(J(.68)=-J(.32)\).

Both \(a\) and \(t(a)\) lie in
\(Q=[.23,.45]+i[-.12,.12]\). Vertical convexity of \(\Re W\)
and its real-height imaginary marginals \((\pi\Re a,\pi\Re t)\)
give
\[
 \Re W(t,a)>
  \frac15-\pi\{\Re t\,\Im a+\Re a\,\Im t\}
 \ge\frac15-\frac{4073\pi}{100000}>\frac7{100}.
 \tag{10}
\]
We used \(\Re t\le.391,\Im t\le.021,\Im a\le.08\)
from the entire endpoint images; negative heights only improve this
lower bound. The last rational comparison uses \(\pi<22/7\).
For type four, \(\Im t<0\), \(0<\Re t<1/2\), and
\(-\Re g(t)>0\). One direct proof uses
\[
 \partial_R\Im\operatorname{Li}_2(Re^{-i\theta})
   =-\arg(1-Re^{-i\theta})/R<0
       \quad(0<R\le1,\ 0<\theta<\pi),
\]
and
\(\Re g(t)=\Im\operatorname{Li}_2(e^{-2\pi it})/(2\pi)\).
Thus (7) proves (5) for both types.

*Proof of the slope.* Original stationarity cancels the responses
of \(e,t,u\), giving
\[
 P_\epsilon'(a)=g'(a+t)-g'(a)+2\pi it.
 \tag{11}
\]
At an actual reference put \(R=e^{2\pi c}\),
\(u=e^{-2\pi\Im t_*}\), \(\theta=2\pi A\), and
\(\psi=2\pi\Re(a_*+t_*)\). The original logarithms give
\[
 \Re P_\epsilon'(a_*)=
        \log\frac{|u-Re^{-i\psi}|}{|1-Re^{-i\theta}|}.
 \tag{12}
\]
By (4),
\[
 \cos\theta<63/1000,\quad \cos\psi<9/20,\quad
 e^{-.084\pi}<u^2<e^{.432\pi}.
 \tag{13}
\]
For \(\psi\), use \(.486<\Re(a_*+t_*)<.824\).
The upper cosine bound follows, for example, from the alternating
degree-eight Taylor upper polynomial at
\((44/125)(157/50)\); it is strictly less than \(9/20\).
For \(\theta\), use
\(\cos(.48\pi)=\sin(.02\pi)<.02\pi<63/1000\).

Elementary Taylor bounds give
\[
       u^2<389/100,\qquad u>217/250.
 \tag{14}
\]
For the upper bound, put \(x=1188/875=(54/125)(22/7)\).
The rational expression
\(\sum_{j=0}^{20}x^j/j!+x^{21}/[21!(1-x/22)]\)
is less than \(389/100\) and bounds \(e^{.432\pi}\).
For the lower bound use
\(e^{-.042\pi}>1-.042\pi>217/250\).

Writing the squared ratio in (12) as \(R_*\), (13)--(14) imply
\[
 L:=\frac{11}{40}\left(\frac{217}{250}\right)^2
                    <R_*<\frac{4890}{937}.
 \tag{15}
\]
Indeed its denominator is at least
\((937/1000)(1+R^2)\) and at most \(2(1+R^2)\).
Its numerator is at least
\((11/20)(u^2+R^2)>(11/20)(217/250)^2(1+R^2)\),
and at most
\((u+R)^2\le(1+u^2)(1+R^2)<(489/100)(1+R^2)\).
The following are exact rational inequalities:
\[
 \sum_{j=0}^{16}\frac{(42/25)^j}{j!}>\frac{4890}{937},
 \qquad
 L\sum_{j=0}^{16}\frac{(8/5)^j}{j!}>1.
\]
Each Taylor sum is a lower bound for its exponential. Thus
\(-4/5<\Re P_\epsilon'(a_*)<21/25\), proving (6).
\(\square\)

Only the derivative at the actual reference was used. Neither (11)
nor (12) asserts that the moving target has an endpoint critical point
outside the input disks.

## 3. Both terminal-transform end tails have small finite rate

For \(0<\delta<1/2\), retain the sum (1) only over
\(i/N\le\delta\) or \(i/N\ge1-\delta\), and denote it by
\(\mathcal V_{\epsilon,N}^{\,{\rm end}}\).
The positive outer-row majorant is obtained by taking the modulus
of each coefficient and of the entire coherent cap value
\(\mathcal U_{\epsilon,N}(w,r^i)\).

**Lemma 2.** There are fixed \(\delta,\rho>0\) such that, for
\(a=y+ih\in[.22,.45]+i[-.12,.12]\), \(|w+2|\le\rho\),
both own types and both level parities, this majorant is bounded by
\[
                         C N^A e^{217N/250}.
 \tag{16}
\]
Each fixed ordinary derivative has the same bound on a smaller
fixed color disk. The two tails can also be bounded separately.

*Proof.* The outer coefficient in (1) has the zero-safe upper rate
\[
 \chi_\epsilon(t,a)=I_a(t)-(1+\epsilon)J(t)-2\pi t\Im a,
 \qquad
 I_a(t)=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds .
 \tag{17}
\]
The original uniform sine-product estimates apply to every finite
row and its zeros, with an arbitrary prescribed tolerance.
The function \(\chi_\epsilon\) is continuous on the compact
target rectangle times \([0,1]\), including its integrated
real-height zeros. Jensen's identity gives
\[
 \chi_\epsilon(0,a)=0,\qquad
 \chi_\epsilon(1,a)=2\pi\max(-h,0)\le.24\pi<132/175.
 \tag{18}
\]

For \(t\le\delta\), the
[coherent cap seam theorem](research_mixed_cap_seam_source_bounds.md)
gives the finite upper rate
\[
 b_\epsilon+\Delta_\delta+\eta,\qquad
 b_0=101/125,\quad b_1=433/500,\quad
 \Delta_\delta=\delta\log2-J(\delta)\longrightarrow0.
 \tag{19}
\]
It is used only on its actual outgoing collar, \(\delta\le.001\).

For \(t=i/N\ge1-\delta\), the exact physical identity is
\[
 \mathcal U_{\epsilon,N}(w,r^i)=
   \sum_{j=0}^{N-1-i}
      \frac{\mathcal H_N(w,r^{-j})p_j(r^i)}{P_j^{1+\epsilon}}.
 \tag{20}
\]
The deleted terms vanish exactly, independently of color.
The coherent endpoint coefficient and its zero-safe endpoint bound
give the physical cap upper profile from
[reversed-cap assembly, equation (17)](research_mixed_reversed_cap_assembly.md):
\[
 \mathfrak U_\epsilon(t)=
  \max_{0\le s\le1-t}
       \{\lambda(s)+J(s+t)-J(t)-\epsilon J(s)\}.
 \tag{21}
\]
It is continuous, and \(\mathfrak U_\epsilon(1)=0\).
To see this at the moving endpoint put \(s=(1-t)v\),
\(0\le v\le1\), and use the continuous endpoint values of
\(J,\lambda\). Thus (20) has upper rate tending uniformly
to zero as \(t\uparrow1\). No cap packet is extrapolated there.

Choose \(\delta\le.001\) so small that each of
\(\Delta_\delta\), \(\sup_{t\le\delta,a}|\chi_\epsilon(t,a)|\),
\(\sup_{t\ge1-\delta}\mathfrak U_\epsilon(t)\), and
\(\sup_{t\ge1-\delta,a}|\chi_\epsilon(t,a)-\chi_\epsilon(1,a)|\)
is less than \(1/2000\). Spend less than \(1/1000\) in total
on all finite-source and color tolerances. The first tail then has
rate less than
\(433/500+1/500=217/250\); the second has rate less than
\(132/175+1/500<217/250\). At most \(N\) rows only change
the polynomial prefactor. This proves (16).
Cauchy's formula gives the fixed ordinary derivatives. \(\square\)

## 4. The full-plateau supporting-plane inequality for these tails

Let \(a_*=A+ic\) be an actual reference as in (4), let
\(a=y+ic\) with arbitrary \(y\in P=[.22,.45]\), and put
\(d=y-A\), \(\kappa_*=1/2500000\). Allocate the neighboring
unselected halfweight with
\[
             \Pi_{\epsilon,\nu}(a_*)=
                      P_\epsilon(a_*)-\frac{\nu}{2}g(a_*).
 \tag{22}
\]

**Theorem 3.** For the fixed tails in Lemma 2, a sufficiently small
fixed ordinary-color neighborhood and every fixed color derivative
satisfy
\[
\begin{split}
 &|\partial_w^j\mathcal V_{\epsilon,N}^{\,{\rm end}}
                 (w,e^{-2\pi ia})|
            |d_N(e^{-2\pi ia})|^{\nu/2}\\
 &\quad\le C_jN^{A_j}
  \exp N\left\{
   \Re\Pi_{\epsilon,\nu}(a_*)+
   \Re\Pi_{\epsilon,\nu}'(a_*)d
              -\kappa_*d^2-\frac1{50}\right\}.
\end{split}
 \tag{23}
\]
The same bound holds for the positive outer-row majorant before
color differentiation. The moving \(a\) may be outside (2).
No moving endpoint branch at \(a\) is assumed.

*Proof.* By (4), \(|d|\le213/1000\). Lemma 1 gives
\[
 \Re P_\epsilon(a_*)+\Re P_\epsilon'(a_*)d-\kappa_*d^2
 >\frac{107}{100}-\frac{21}{25}\frac{213}{1000}
       -\kappa_*\left(\frac{213}{1000}\right)^2
 =\frac{2227699954631}{2500000000000}>\frac{89}{100}.
 \tag{24}
\]
Subtracting the tail rate \(217/250\) leaves more than \(11/500\).
In particular the unweighted estimate (23) retains \(1/50\),
with positive room for any further smaller-neighborhood tolerance.

There is no neighboring weight when \(\nu=0\). When \(\nu=1\),
the actual height \(c<0\). For every \(y\in P\), the radial
argument in Lemma 1 gives
\(G_c(y):=\Re g(y+ic)<0\). Its strict positive minimum after
negation on the compact actual-height range and \(P\) permits
the [original relative Fourier theorem](research_mixed_fourier_weight_continuation.md):
the halfweight has rate \(-G_c(y)/2\), with only polynomial
prefactors. Moreover
\[
                   G_c''(y)=\pi\Re\cot\pi(y+ic)>0 .
\]
Its real supporting-line inequality therefore gives
\[
 -\frac12G_c(y)\le
     -\frac12G_c(A)-\frac12G_c'(A)d .
 \tag{25}
\]
Adding (25) to the unweighted estimate produces exactly the two
terms of \(\Pi\) in (23). Only the actual reference derivative
is evaluated; the Fourier halfweight at the new target is kept.
This proves the full-plateau statement. \(\square\)

The end-row source bound is uniform on a slightly larger complex
target neighborhood by the same zero-safe product bounds and strict
reserve. Apply the
[horizontal complex-extension theorem](research_mixed_horizontal_complex_extension.md)
to the squared holomorphic allocated product
\((\mathcal V_{\epsilon,N}^{\,{\rm end}})^2d_N^\nu\).
Its integral Fourier powers require no square root of \(d_N\).
Fixed target derivatives of this squared product have bounds on
smaller fixed neighborhoods with a slightly smaller gap. The ordinary
color derivatives in (23) already have their separately stated scope.

Theorem 3 discharges precisely the end-index portion of equation (15)
of reversed-cap assembly, including its actual tangent, halfweight
and full real plateau. In the exact contracted source one may write
\(\mathcal V=\mathcal V^{\,{\rm end}}+\mathcal V^{\,{\rm central}}\).
The central part \(\delta<i/N<1-\delta\) is left coherent.
It is not bounded by this theorem; the nested triangle obstruction
remains relevant there. No ordinary-closure asymptotic, selected-neighbor
extension, or stability under arbitrary short fillings is inferred.

## 5. Exact scalar reproduction

The [rational-constants script](../experiments/check_mixed_terminal_transform_tail_constants.py)
checks the corner floors, the vertical cost, the degree-eight cosine
bound, the exponential Taylor upper bound through degree twenty with
its geometric remainder, the positive Taylor lower bounds through
degree sixteen, the full-plateau plane in (24), and both tail budgets.
Run it from the repository root:

    python3 experiments/check_mixed_terminal_transform_tail_constants.py

Every arithmetic comparison uses exact rational numbers. The script
does not solve a root, evaluate a source, or cover a parameter domain;
its checks supplement the analytic source and contour arguments above.

