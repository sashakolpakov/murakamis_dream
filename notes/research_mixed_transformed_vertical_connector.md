# A height-dependent bound for the complete transformed vertical connector

Research deduction, 7 November 2026. This bounds the literal product
\(U_{0,N}C_{1,N}\) on the incoming line \(\Re a=1/2\), uniformly
between any two nonpositive heights in the stated range. The outgoing
radius gain is retained before maximizing over the transform index.
The result includes all finite rows and does not assume that the
connector has the original pair's height. No numerical evaluation is
used, and no comparison with a following critical action is asserted.

## 1. Exact source and explicit ceiling

Use the unchanged normalization
\[
 \begin{split}
 r&=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)&=\sum_{j<N}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j<N}X^{-j}p_j(X)p_j(Y)/P_j^3.
 \end{split}                                                     \tag{1}
\]
Every \(H_N\) is its whole endpoint polynomial. All indices
\(0\le j<N\), both parities, and every numerator zero remain.
For \(a=1/2+ih\), put
\[
 \delta=-2\pi h,\quad X=-e^{-\delta},\qquad
 0\le\delta\le\Delta\le1/2,\qquad |Y|\le R\le1.
 \tag{2}
\]
Let \(J(t)=\int_0^t\log(2\sin\pi v)\,dv\) on \([0,1]\),
and \(L(t)=-2J((1-t)/2)\). Set
\[
 \begin{split}
 B_0&=1549/1500,\qquad d_0=7/40-3/512+73/125,\\
 \beta(R)&=\tfrac12\log\frac2{1+R^2},\qquad
 u=\Delta/2-\beta(R),\\
 E_\Delta&=\frac{\sqrt3}{2\pi}\sinh^2(\Delta/2),\\
 \mathcal V_\Delta(R)&=B_0+\max\left\{
 d_0+\frac u4+\frac{\max\{u^2,(u-1/10)^2\}}{20}+E_\Delta,
                   \Delta+\frac13\right\}.
 \end{split}                                                     \tag{3}
\]
The definitions include \(R=0\) and \(\Delta=0\) by their literal
continuous values.

**Theorem 1.** For every \(\tau>0\), fixed ordinary and outgoing
derivative orders \(k,\ell\), and fixed \(\Delta,R\) as in (2),
\[
 \sup_{\substack{-\Delta/(2\pi)\le h\le0\\
                  w\in[-2,2],\ |Y|\le R}}
 \left|\partial_w^k\partial_Y^\ell
       [U_{0,N}(w,-e^{2\pi h})C_{1,N}(-e^{2\pi h},Y)]\right|
 \le C_{\tau,k,\ell}N^{B_{k,\ell}}
                      e^{N(\mathcal V_\Delta(R)+\tau)}.
 \tag{4}
\]
It holds at every sufficiently large level of either parity. A
sufficiently small fixed complex ordinary-color disk about \(-2\)
has the same assertion, with a smaller disk for derivatives. Constants
and color disks can be chosen uniformly when \((\Delta,R)\) ranges
over a fixed compact subrectangle of \([0,1/2]\times(0,1]\).
The value assertion is also uniform down to \(R=0\).

For any fixed oriented vertical segment \(\gamma\) joining
\(1/2+ih_1\) to \(1/2+ih_2\), with both heights in the interval
in (4), the exact retained-leg source
\[
 N\int_\gamma U_{0,N}(w,e^{-2\pi ia})
                        C_{1,N}(e^{-2\pi ia},Y)\,da
 \tag{5}
\]
has the same bound after enlarging its polynomial factor. No final
Gram, \(\kappa_N\), factorial halfweight or selected sector is
inserted in (5).

## 2. The whole cap has no nonpositive-height debit here

The [far-half radial cap theorem](research_mixed_three_four_far_half_cap_radial_extension.md),
Equation (9), proves for every \(0\le\rho\le1\),
\(1/2\le x\le1\), and \(0\le e\le1\),
\[
 I_{x,\rho}(e):=\int_0^e\log|1-\rho e^{-2\pi i(x+v)}|\,dv
 \le\begin{cases}
       -J(1/2-e),&e\le1/2,\\
       J(e),&e\ge1/2.
     \end{cases}
 \tag{6}
\]
In particular it applies to the full negative radial interval
\(X=-e^{-\delta}\). Combined with the original compact-index
whole-coefficient rate \(J(e)+\lambda(e)\), it gives the row rate
\(\lambda(e)+I_{1/2,e^{-\delta}}(e)\). The already proved ceilings
\[
 \lambda(e)<433/500\ (e<1/2),\qquad
 \max(-J)<1/6,\qquad
 \max(\lambda+J)<101/125
 \tag{7}
\]
therefore bound the compact private rows by \(B_0\).

For all real ordinary colors, the two physical private-end layers use
[complementary real colors](research_mixed_three_four_complementary_real_colors.md),
Equations (4)--(6). Their coefficientwise finite proof is valid on the
whole closed unit disk and gives rate \(3/5<B_0\). Thus no compact
endpoint packet is extrapolated to the true ends. The bulk argument
(6)--(7) works at every \(0<e^{-\delta}\le1\), so the restriction to
the old pair's particular height is unnecessary. On the present compact
radial interval the uniform zero-safe product estimates give
\[
 |U_{0,N}(w,-e^{-\delta})|
       \le C_\tau N^B e^{N(B_0+\tau)},
          \qquad 0\le\delta\le1/2,\quad w\in[-2,2].
 \tag{8}
\]
This is a bound for the whole signed cap, proved using complete
coefficient majorants. It is not monotonicity of its signed value.
The angular scope of (8) is the far half, in particular the negative
radius used here. Only the physical-end estimates were asserted on the
entire unit disk; no whole-cap \(B_0\) bound at all disk angles is used.

## 3. Retain the radius term in the lower-row maximization

Define the conditional row rate, with its first-argument chirp, by
\[
 F_{\delta,Y}(t)=I_Y(t)-3J(t)
             +I_{1/2,e^{-\delta}}(t)+\delta t,
 \qquad I_Y(t)=\int_0^t\log|1-Ye^{-2\pi iv}|\,dv.
 \tag{9}
\]
The [outgoing-radius theorem](research_mixed_transformed_following_four_radial_majorant.md),
Equation (6), gives
\[
 I_Y(t)\le L(t)-\beta(R)t,\qquad 0\le t\le1/2,\quad |Y|\le R.
 \tag{10}
\]
Its centered-arc proof includes \(R=0\) and numerator zeros.
Put
\[
 D(t)=L(t)-J(1/2-t)-3J(t),\qquad
 D_\delta(t)=L(t)-3J(t)
                   +\int_0^t\log|e^\delta+e^{-2\pi iv}|\,dv.
 \tag{11}
\]
The exact radial identity, for \(0\le t<1/2\), is
\[
 D_\delta(t)=D(t)+\frac{\delta t}{2}
  +\frac12\int_0^t
       \log\left(1+\sinh^2(\delta/2)\sec^2\pi v\right)dv.
 \tag{12}
\]
It follows by squaring
\(|e^\delta+e^{-2\pi iv}|\). Both the \(\delta t/2\) term and
the remaining integral are required; the original \(X^{-j}\) chirp
has already been included in (9).

For \(t\le1/3\), use \(\log(1+x)\le x\) and integrate the
secant square to obtain
\[
 D_\delta(t)\le D(t)+\delta t/2
                       +\frac{\sqrt3}{2\pi}\sinh^2(\delta/2).
 \tag{13}
\]
The original scalar bounds, stated with their proof in
[the calibrated transformed remainder](research_mixed_three_four_transformed_complement_calibration.md),
Equation (11), are
\[
 D''\le-2\pi\sqrt3<-10,\quad
 -1/10<D'(1/4)<0,\quad D(1/4)<d_0.
 \tag{14}
\]
In particular the tangent-quadratic bound at \(1/4\) gives, for any
real \(v\),
\[
 D(t)+vt\le
 d_0+\frac v4+\frac{\max\{v^2,(v-1/10)^2\}}{20}.
 \tag{15}
\]
Indeed after writing \(t=1/4+s\), maximize
\((D'(1/4)+v)s-5s^2\) on the real line. The maximum of the
square of its linear coefficient over \(D'(1/4)\in[-1/10,0]\)
is exactly the maximum of the two endpoint squares in (15).
Taking \(v=\delta/2-\beta(R)\) in (13)--(15) retains the outgoing
radius improvement before the maximization.

The rest of the lower half has no larger value. For
\(1/3\le t\le1/2\) and \(0\le\delta\le1/2\),
\[
 |e^\delta+e^{-2\pi it}|<3/2,\qquad
 2\sin\pi t\ge\sqrt3,
 \tag{16}
\]
because \(e^{1/2}<5/3\) and \(\cos2\pi t\le-1/2\).
More explicitly \(q^2-q+1\le19/9<9/4\) for
\(1\le q=e^\delta<5/3\). The exponential guard follows from
\(e<25/9\): the exponential series gives
\(e<8/3+(1/24)/(1-1/5)=87/32<11/4<25/9\).
Also \(L'(t)=\log(2\cos(\pi t/2))\le\log2\).
Thus, wherever its derivative is finite,
\[
 (D_\delta(t)-\beta(R)t)'
   <\log\frac{3}{3\sqrt3}-\beta(R)
   <\log(3/5)<0.
 \tag{17}
\]
The same conclusion follows directly for (9) using
\(|1-Ye^{-2\pi it}|\le2\). All logarithmic singularities are
integrable; continuity of these primitives gives the endpoint and
zero limits. Consequently the maximum on \([1/3,1/2]\) is at
\(1/3\), which was already included in (13)--(15).

Finally \(D_\delta(t)\) increases with \(\delta\ge0\): the
\(\delta\)-derivative of its integral is
\((e^{2\delta}+e^\delta\cos2\pi v)/
 |e^\delta+e^{-2\pi iv}|^2\ge0\), with integrated limits at the
single possible zero. Therefore every lower row for
\(0\le\delta\le\Delta\) is bounded by the lower expression in (3),
using \(\Delta\) before the same maximization. No separate crude
\(\delta/6\) debit is added.

## 4. Every upper row, including the last one

For \(0\le\rho\le1\) the function
\(f(v)=\log|1+\rho e^{-2\pi iv}|\) is symmetric under
\(v\mapsto1-v\) and has zero period and half-period integrals.
For \(t\in[1/2,1]\),
\[
 I_{1/2,\rho}(t)=-I_{1/2,\rho}(1-t)\le0.
 \tag{18}
\]
Here the integral on \([0,1-t]\subset[0,1/2]\) is nonnegative:
its integrand decreases on this half interval, so its primitive is
concave with zero endpoint values. The assertions at \(\rho=1\)
use integrability of the half-period logarithmic zero.

The whole-disk centered-arc bound gives \(I_Y(t)\le L(t)<1/3\),
while \(J(t)\ge0\) on \([1/2,1]\). Thus (9) yields
\[
 F_{\delta,Y}(t)\le\Delta+1/3,
                        \qquad 1/2\le t\le1.
 \tag{19}
\]
There is no terminating-support assumption on either free numerator.
In particular every row revived by a nonphysical outgoing \(Y\) is
included in (19).

## 5. Finite-level passage and the actual connector scope

Uniform zero-safe finite-product upper bounds apply to both numerator
products for all \(j/N\in[0,1]\), \(0\le\delta\le\Delta\), and
\(|Y|\le R\). Together with
\(\log|P_j|=NJ(j/N)+O(\log N)\), they bound every literal row in
(1) by a polynomial times \(e^{N(F_{\delta,Y}(j/N)+\tau)}\).
This keeps \(j=0,N-1\), both parities and all zeros; only the nonzero
physical denominators are divided. Summing the original \(N\) rows
and multiplying by (8) proves the value bound (4), after assigning one
aggregate tolerance. It does not divide a bound for a signed terminal
sum or expand a coherent \(H_N\) into uncontrolled partial terms.

Fixed ordinary derivatives follow by Markov applied to the complete
cap bound on \([-2,2]\). The compact-index endpoint theorem and
polynomial growth supply its small fixed complex-color version,
with any prescribed additional tolerance. For \(R>0\), outgoing
Cauchy estimates at radius \(R/N\), with the polynomial degree
\(N-1\), cost only polynomial factors: growth from \(R\) to
\(R(1+1/N)\) costs at most \(e\). At \(R=0\), take a fixed
sufficiently small outgoing disk and use continuity of (3) to absorb
its rate change in the prescribed tolerance. This proves the stated
jets without logarithmic differentiation at a finite zero. Integrating
over the fixed bounded-length segment proves (5).

The formula generalizes the vertical part of the existing radial and
angular estimates; those earlier theorems retain their original fixed
\(\Gamma_+\). It makes no numerical claim that (3) is below the
pre-Gram action at a following reference. Using it for a moving-height
join still requires proof that both endpoint heights are nonpositive,
that their \(\Delta\) lies in \([0,1/2]\), and that the explicit ceiling
is below the correct absolute action with a strict margin. The pointwise
bound is uniform for such endpoint choices; derivatives of a
reference-varying path are not asserted by the fixed-path statement (5).
None of those new comparisons is evaluated here.
