# What a strict complete-reference attachment gap extends to

Private source-matched deduction, 9 November 2026. A strict gap in the
present complete-color attachment comparison extends the exact right
physical contribution to a fixed complex neighborhood of its outgoing
coordinate. This uses the already proved uniform finite outgoing
formula, not holomorphy at one point alone. An incoming ordinary-color
neighborhood requires an additional uniform source estimate. A real
ordinary-color interval would suffice, by the exact polynomial degree.

The strict attachment gap remains a hypothesis. No new numerical
evaluation, saved-value arithmetic, import, compilation, or change to
a frozen source is used. Nothing here asserts a whole new prefix,
an ordinary two-boundary closing, or stability under short fillings.

## 1. Exact source and the two different boundary coordinates

Fix one eligible actual complete \(343\) reference of length at least
five. Put \(Z_*=e^{-2\pi iz_*}\), and retain the original action
\[
 P(w,z)=\mathcal P_0^+(w,z),\qquad
 \Lambda_*=\Re P(-2,z_*).
 \tag{1}
\]
The local source theorem supplies this holomorphic action near
\((-2,z_*)\), with its absolute normalization.

Use \(D=N-1\), \(M=\lceil N/2\rceil\), \(U=D-M\),
\(q=e^{\pi i/N}\), \(r=q^{-2}\), and
\(\kappa_N=q^{D^2/2}\), with \(P_b=(r;r)_b\).
The original complete transfer is the polynomial
\[
 \begin{split}
 \mathcal T_N(w,Z)
 &=N[Y^0](F_{34,N}(w,Y)d_N(Y)C_{0,N}(Y,Z))\\
 &\quad+N[Y^N](F_{34,N}(w,Y)d_N(Y)C_{0,N}(Y,Z))\\
 &=\sum_{b=0}^{D}\frac{F_{34,N}(w,r^b)}{P_b}
                                  C_{0,N}(r^b,Z).
 \end{split}
 \tag{2}
\]
Its degree in each of \(w,Z\) is at most \(D\), by the exact
attachment theorem, (3)--(4). Both Fourier sectors and the forced
polynomial \(d_N\) occur in (2).

For every ordinary color \(w\), define the full inner polynomial and
the radical functional
\[
 Q_{N,w}^{\rm full}(X)
   =\phi_N^{(t)}[R_N(t)^3K_N(w,t)K_N(X,t)],\qquad
 \mathcal L_{N,w}(F)
   =\phi_N[R_N^3e_M Q_{N,w}^{\rm full}F].
 \tag{3}
\]
The full Hermite functionals, including their first normals and odd
simple node, are unchanged. Put
\[
 \begin{split}
 C_{b,N}(Z)&=C_{0,N}(r^b,Z),\\
 F_N^+(X,Z)
   &=\sum_{b=M}^{D}(-q)^b C_{b,N}(Z)\frac{e_b(X)}{e_M(X)}
     =\sum_{k=0}^{U}f_{k,N}(Z)T_k(-X/2),\\
 \mathcal R_N^+(w,Z)
   &=\frac{1}{\kappa_N^2N}\mathcal L_{N,w}(F_N^+(\cdot,Z)).
 \end{split}
 \tag{4}
\]
Each radical quotient is an ordinary polynomial. The lowered-word
identity in the complete-transfer reduction, (11), and the full
radical contraction give exactly
\[
 \mathcal R_N^+(w,Z)
 =\frac{1}{\kappa_N^2N}
       \sum_{b=M}^{D}(-q)^b\ell_b(w)C_{b,N}(Z)
 =\sum_{b=M}^{D}\frac{F_{34,N}(w,r^b)}{P_b}C_{b,N}(Z),
 \qquad
 \ell_b(w)=\phi_N(R_N^3e_bQ_{N,w}^{\rm full}).
 \tag{5}
\]
These are polynomial identities in \(w,Z\); their validity is not
restricted to complete color. Their estimates need not have that
same scope. The sharp mode theorem currently bounds (3) at \(w=-2\).

Let \(I_N(w,z)\) be the exact fixed-path local integral in the next
local-source theorem, (15), based at \(y_*\). Its endpoints do not
move with \(w,z\). That theorem proves on a fixed complex bidisk
\[
 I_N(w,z)=N^{-2}A(w,z)e^{NP(w,z)}
                       (1+O_{\rm hol}(N^{-1})),\qquad A(w,z)\ne0.
 \tag{6}
\]
In particular this is already an actual local finite integral,
not an asymptotic definition of one. Before composition with
\(Z=e^{-2\pi iz}\), it is a polynomial of degree at most \(D\)
in each \(w,Z\): integration of its fixed path preserves the degree
bounds of its exact integrand. Thus
\[
 \begin{split}
 E_N^-(w,z)
 &:=\mathcal T_N(w,e^{-2\pi iz})-I_N(w,z)
                    -\mathcal R_N^+(w,e^{-2\pi iz})\\
 &=\sum_{b=0}^{M-1}\frac{F_{34,N}(w,r^b)}{P_b}
                     C_{b,N}(e^{-2\pi iz})-I_N(w,z)
 \end{split}
 \tag{7}
\]
is holomorphic on the local chart and polynomial of degree at most
\(D\) in \(w\). Equation (7) identifies the exact other remainder
that a whole-transfer extension must retain.

## 2. The right contribution does extend in the outgoing coordinate

Let \(\mathcal D(t,Z_*)\), \(E_0(Z_*)\), \(M_3\), and
\(\Gamma(\delta)\) be precisely the original rates of the positive
transition and selected-action theorems. Assume a uniform strict gap
\[
 \mathcal D(t,Z_*)+\Gamma(1/2-t)
       \le\Lambda_*-\gamma
          \quad(0\le t\le1/2),\qquad \gamma>0.
 \tag{8}
\]
No assertion that (8) holds is made here.
For example, the adopted combined-action inequality makes
\[
 M_3+E_0(Z_*)-\Lambda_*
       \le \frac{5\pi}{226}-\gamma
 \tag{8a}
\]
a sufficient condition for (8). The proposition does not require
(8a): any source-valid proof of the full envelope gap (8) is eligible.

**Proposition 1.** Under (8), there is a fixed disk \(V\) about
\(z_*\) such that, for both parities and all sufficiently large \(N\),
\[
 \sup_{z\in V}
 \left|e^{-NP(-2,z)}
       \mathcal R_N^+(-2,e^{-2\pi iz})\right|
       \le C e^{-\gamma N/2}.
 \tag{9}
\]
Every fixed \(z\)-derivative of the normalized expression has the
same bound on a smaller disk, with its own constant.

*Proof.* First, for any fixed \(\varepsilon>0\), the complete
outgoing-amplitude theorem gives on a sufficiently small disk about
\(Z_*\), uniformly for every \(M\le b\le D\),
\[
 |C_{b,N}(Z)|\le C_\varepsilon N^{A_\varepsilon}
              e^{N\{\mathcal E(b/N,Z_*)+\varepsilon\}}.
 \tag{10}
\]
Here is why its endpoint-uniform complex scope supplies (10).
Its exact formula retains the factor \(S_b/N\) and the original
nonzero symbol \(\mathcal B(a,Z)\), and its other exponential is
\(\exp\{-N\int_a^1\log h(v,Z)\,dv\}\). The function \(h\) is
nonzero and holomorphic on a common neighborhood, including \(a=1\).
Choose its original logarithm there. Uniform continuity of
\(\log h\) makes
\[
 \sup_{1/2\le a\le1}
 \left|\int_a^1\{\log h(v,Z)-\log h(v,Z_*)\}\,dv\right|
 <\varepsilon
 \tag{11}
\]
on a fixed smaller disk. The symbol ratios and relative finite
errors are uniformly bounded. The sine factors are unchanged and
cancel in this comparison, including at the last physical row
\(b=D\). This proves (10), using the adopted complete row ceiling
at \(Z_*\). No pointwise relative error is dropped inside a sum.

The exact transition formula
\[
 f_{k,N}(Z)=(-1)^{M+k}\sum_{d=k}^{U}
                     q^{M+d}\beta_{d,k,N}C_{M+d,N}(Z),
 \qquad \beta_{d,k,N}>0,
 \tag{12}
\]
and its uniform sine-product bounds therefore imply
\[
 |f_{k,N}(Z)|\le C_\varepsilon N^{B_\varepsilon}
       e^{N\{\mathcal D(k/N,Z_*)+\varepsilon\}},
                    \qquad0\le k\le U.
 \tag{13}
\]
This is the proof of the original coefficient ceiling with (10)
inserted. At odd levels use the same monotonicity of the original
reference action to remove \(M/N-1/2\). All weights, stops, and
phases in (12) are retained before taking the eligible absolute
upper bound.

There is also a useful consequence of the two finite outer-mode
theorems:
\[
 |\mathcal O_{N,k}|
 :=|\mathcal L_{N,-2}(T_k(-\,\cdot/2))|
 \le C_\varepsilon N^{B_\varepsilon}
        e^{N\{\Gamma(1/2-k/N)+\varepsilon\}},
                       \qquad0\le k\le U.
 \tag{14}
\]
Indeed \(\Gamma\) is continuous at zero with \(\Gamma(0)=M_3\).
Choose a fixed \(\delta_1>0\) such that
\(M_3-\Gamma(\delta)<\varepsilon\) for \(0\le\delta<\delta_1\).
The whole-frequency bound gives \(CN^B e^{NM_3}\) on this
last interval. On \([\delta_1,1/2]\), use the adopted whole
outer asymptotic and its uniform coefficient upper bound.
This proves (14), without claiming a relative asymptotic near
\(\delta=0\). The constants may depend on \(\varepsilon\).

Combining (4), (13), (14), and the assumed envelope gap (8) gives
\[
 |\mathcal R_N^+(-2,Z)|
 \le C_\varepsilon N^{B_\varepsilon}
                  \exp N\{\Lambda_*-\gamma+2\varepsilon\}.
 \tag{15}
\]
The factor \(1/(\kappa_N^2N)\), of modulus \(1/N\), and the
at most \(N\) frequencies only affect the displayed polynomial
factor. Set \(\varepsilon=\gamma/8\). Shrink \(V\) so that it
maps into the disk used above and
\[
                  \Re P(-2,z)\ge\Lambda_*-\gamma/8.
 \tag{16}
\]
Equations (15)--(16) give normalized rate at most
\(-5\gamma/8\). Absorb the fixed polynomial factor into
\(\gamma/8\), proving (9). The exact normalized expression is
holomorphic; fixed-radius Cauchy estimates prove its derivative
assertion. \(\square\)

The proof works for a compact family of references if (8) has one
positive margin and the cited source neighborhoods and local
action charts have uniform compact scope. A pointwise collection
of positive margins is not itself such a uniform assertion.

## 3. Precisely what is needed for a whole local packet

**Lemma 2.** Suppose, on a fixed neighborhood \(B\times V\) of
\((-2,z_*)\), the exact remainder
\[
 R_N(w,z):=\mathcal T_N(w,e^{-2\pi iz})-I_N(w,z)
 \tag{17}
\]
obeys
\[
 |e^{-NP(w,z)}R_N(w,z)|\le C N^B e^{-\eta N},
                          \qquad \eta>0.
 \tag{18}
\]
Then the whole transfer has the same nonzero holomorphic packet
as (6) on every fixed smaller bidisk, with all fixed normalized
mixed derivatives. At \(w=-2\) its fixed incoming ordinary
derivatives have the leading coefficient in the local-source
theorem, (21b).

*Proof.* The local coefficient \(A\) is bounded away from zero
after shrinking. Divide (17) by
\(N^{-2}A(w,z)e^{NP(w,z)}\). The additional relative error is
holomorphic and bounded by \(CN^{B+2}e^{-\eta N}\), which is
absorbed in the existing \(O_{\rm hol}(N^{-1})\) error in (6).
Cauchy's formula on nested fixed bidisks gives every fixed
normalized derivative. The original phase derivative
\[
 P_w(-2,z)=-\frac{\tan(\pi u_L(z))}{4\pi}\ne0
 \tag{19}
\]
is already proved in that source. Differentiating the resulting
packet therefore gives its same actual incoming ordinary-jet
formula. These are derivatives of the original polynomial (2).
\(\square\)

At the fixed ordinary color \(w=-2\), Proposition 1 supplies the
right-hand part of (18). To obtain the entire outgoing local
packet there, one must additionally have the same local
normalized gap for the exact \(E_N^-(-2,z)\) in (7). To obtain
an independent ordinary-color disk, both parts in (7) must
be controlled there, or their sum must be controlled as in (18).

The base-reference complete-transfer reduction explicitly
restricts its conclusion to \(w=-2,z=z_*\) and does not assert
outside jets. Its algebraic identities remain valid near that
point, but this alone does not enlarge their error estimates.
One must either reapply its finite component estimates on fixed
parameter neighborhoods or prove a whole remainder bound of
the form (18). The present proposition does not silently make
that source audit.

## 4. A real ordinary-color interval would suffice

There is a concrete polynomial alternative to proving (18)
directly on a complex disk. Let \(I\) be a fixed nondegenerate
real interval containing \(-2\), possibly as an endpoint.
Suppose the exact polynomial (17), on a fixed outgoing disk \(V\),
satisfies
\[
 \sup_{w\in I,\ z\in V}|R_N(w,z)|
                  \le C N^A e^{N(\Lambda_*-\eta)}.
 \tag{20}
\]
Its degree in \(w\) is at most \(D<N\), because the local path
defining \(I_N\) is fixed. Expand in Chebyshev polynomials after
affinely mapping \(I\) to \([-1,1]\). Every coefficient is at
most twice the norm in (20). On the filled ellipse of height
\(h>0\),
\[
 |R_N(w,z)|\le C(2D+1)N^A
                         e^{N(\Lambda_*-\eta)+Dh}.
 \tag{21}
\]
Choose \(h<\eta/4\), and then a closed ordinary-color disk about
\(-2\) inside the ellipse and the local packet chart. This is
possible even when \(-2\) is an endpoint of \(I\): both real
endpoints lie in the interior of every ellipse of positive
height. Shrink both parameter disks so that
\(\Re P(w,z)\ge\Lambda_*-\eta/4\).
Equation (21) then gives (18), with a smaller positive gap
after polynomial absorption. Lemma 2 applies.

This argument requires the continuum estimate (20), including
its uniform outgoing-coordinate scope. It does not infer (20)
from finitely many nearby physical samples or from its single
value at \(w=-2\). If a source comparison instead gives a
uniform estimate relative to \(\Re P(w,z)\) on a sufficiently
small interval and disk, continuity first converts it to (20)
with a reduced gap.

## 5. Why a pointwise gap cannot supply the missing ordinary jets

The insufficiency of holomorphy and degree alone has an elementary
exact example. Fix a real \(\Lambda_0\), and let
\[
                        R_N(w,Z)=e^{N\Lambda_0}(w+2).
 \tag{22}
\]
It is entire, has ordinary degree one and outgoing degree zero,
and vanishes at \(w=-2\) for every \(N\). It satisfies any
prescribed exponential-gap bound at that point, uniformly in \(Z\).
Nevertheless at every fixed \(w\ne-2\) its rate is
\(\Lambda_0\), and its first ordinary derivative at \(-2\)
is exactly \(e^{N\Lambda_0}\). Even an all-real coarse bound
\(\sup_{[-2,2]}|R_N|\le4e^{N\Lambda_0}\) does not fix this.
In angular coordinates it is
\(2e^{N\Lambda_0}(1-\cos\theta)\), so the usual evenness at
complete color also does not remove the issue.

This is a counterexample to the proposed automatic inference,
not a counterexample for the actual quantum source. The latter
has additional structure that may prove (20), a family of
uniform charged-mode bounds in \(w\), or direct uniform finite
contour estimates. Those are substantive additional source
statements.

Finally, the retained outgoing coordinate \(z\) is not the
ordinary right color \(w_R\). The exact original conversion is
\[
 v(w)^TA_3A_4A_3v(w_R)
   =\kappa_N^4N\sum_{b=0}^{D}
        \mathcal T_N(w,r^b)H_N(w_R,r^{-b}).
 \tag{23}
\]
A local conditional packet near \(z_*\) cannot replace the
whole summand in (23). Its closing contour, complementary
source bounds, and original ordinary derivatives must still
be justified. Neither (9) nor Lemma 2 supplies those
additional estimates or a composition theorem.

## Frozen source bindings

- Exact next attachment, degrees, and ordinary observation:
  d92eed1edd1dabbc7e2b5f10bd1d55aa536215b7212ec93c5cbc11549aa5728a.
- Actual local integral, original action, and nonzero mixed packet:
  f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696.
- Lowered-word identity and complete-reference scope:
  b8e2cf1b901fde9d962fab2d1d3d160dd7871321388750eb462cae7183cb4e46.
- Exact positive transition:
  68aad94365bf6a9f6ff8e3070e74c3e147ccabaf6845118c82adfe89a4fe1fab.
- Endpoint-uniform complex outgoing amplitude:
  1620ac15a7fb61021729aeb3831b85dc6c716f140787f9984ecc29bd3be61840.
- Whole selected outer observation away from the half-frequency end:
  8c0f4853c05443eb76d821bca6d7248f6c00e19177a796e530e4b4cd24d93ac6.
- Complete whole-frequency upper bound:
  24ed707af29a5a15e5f2302210ae492d8256c5b5548145dce31de19dbbd2c489.
- Combined action comparison supplying the sufficient example (8a):
  c4134027f8297321f91363bbf252f55d755596c45ac41c63492212a0c0c23974.
