# The actual marked Borel minor from the soft endpoint source

Private written proof, 18 November 2026.

This note reconstructs the Borel transform of the original marked
source from its one-variable endpoint moments. It uses the common-disk
factorial estimate for the regular hard contractions. The resulting
function has an actual nonzero square-root minor, and its leading
clock character is the one calculated from the analytic principal
phase. Every primitive starts at the original Borel origin.

The theorem is local under the same simple two-branch node hypotheses
as the soft reduction. It does not identify the branch as the
hyperbolic component or determine its coefficient in the physical
root-of-unity evaluation.

## 1. Source and assertion

Use the actual marked highest-cut source and its exact formal moment
reduction [B]:
\[
 \mathscr W_m(h,\alpha+z)
   =r(z)\mathfrak L_z
       \left[\exp\left(\sum_{j\ge1}h^jU_j(z,m;t)\right)\right],
 \qquad
       \mathfrak L_z[t^d]=d!\,z^{-d-1}.
 \tag{1}
\]
Here \(z=Y-\alpha\), \(\alpha\ne0,1\), the source normalization
satisfies \(r(0)\ne0\), and the calibrated quadratic coefficient
\(\sigma\ne0\). Keep precisely the original clocks \(m\), original
highest-cut projector, pivots and framing. The clock vector is a
fixed specialization of independent stage marks, as in [B] and [D].

Let \(\Psi_a(z,x,\mathbf t)\) be the logarithmic coefficients after
the regular hard contractions in [D, (28a)]:
\[
 \log\mathcal H_{\rm scaled}
    =\sum_{a\ge0}h^{a-1}\Psi_a(z,x,\mathbf t),\qquad
                  \|\Psi_a\|\le MC^a a!.
 \tag{2}
\]
The estimate holds on fixed common disks in \(z,x,\mathbf t\).
The scaling is \(x=ht\), where the scalar \(t\) in (1) is distinct
from the independent stage-mark vector \(\mathbf t\).
Put
\[
 \begin{split}
 \Phi(z,x)&=-zx+\Psi_0(z,x,0),&
 f(z,x)&=-\Phi(z,x),\\
 x_g(z)&:\ \partial_x\Phi(z,x_g(z))=0,&
 \xi_g(z)&=f(z,x_g(z)),\\
 A_0(z,x)&=\Psi_1(z,x,0),&
 \Theta(z,x)&=\partial_{\mathbf t}\Psi_0(z,x,0).
 \end{split}
 \tag{3}
\]
These are the analytic germs of [P], not newly chosen phases.
In particular
\[
 \xi_g(z)=\frac{z^2}{4\sigma}+O(z^3),\qquad
 x_g(z)=\frac{z}{2\sigma}+O(z^2),\qquad
               \Theta_g(z):=\Theta(z,x_g(z))
                         =\frac{\mu z}{2\sigma}+O(z^2).
 \tag{4}
\]

**Theorem.** For each prescribed compact set of clock values, the
canonical Borel transform
\[
 b_m(z,\xi)=\mathcal B_h\mathscr W_m(\alpha+z,\xi),
       \qquad \mathcal B_h(h^N)=\xi^N/N!,
 \tag{5}
\]
has continuation from its original \(\xi=0\) germ, for small
\(z\ne0\), to the local twofold cover
\[
                         v^2=\xi-\xi_g(z).
 \tag{6}
\]
On one common neighborhood in \((z,v)\) it has the form
\[
 b_m(z,\xi)=E_m(z,\rho)+\rho^{-1/2}A_m(z,\rho),
             \qquad \rho=\xi-\xi_g(z),
 \tag{7}
\]
where \(E_m,A_m\) are holomorphic jointly in \(z,\rho\) and in
clock values on a neighborhood of the prescribed compact.
The coefficient is nonzero:
\[
 A_m(z,0)=\frac{r(z)}2\,
       e^{A_0(z,x_g(z))+m\cdot\Theta_g(z)}
                          \,\partial_vx(z,0)\ne0 .
 \tag{8}
\]
The inverse Morse coordinate \(x(z,v)\) used here is fixed below;
changing its sign changes both square-root conventions consistently.
Consequently the actual leading marked/unmarked minor ratio is
\[
                         \frac{A_m(z,0)}{A_{m=0}(z,0)}
                              =e^{m\cdot\Theta_g(z)}.
 \tag{9}
\]
This is a statement about the analytically continued source in
(5), not only its formal stationary expansion.

## 2. The common-disk quantum amplitude

Specialize the independent marks in (2) to \(\mathbf t=hm\).
For \(m\) in a prescribed compact, Cauchy estimates in the mark
disk, followed by finite coefficient comparison, give
\[
 \log\mathcal H_{\rm scaled}
  =\frac{\Psi_0(z,x,0)}h+A_0(z,x)+m\cdot\Theta(z,x)
                                 +\sum_{n\ge1}h^n B_n(z,x,m),
 \tag{10}
\]
with
\[
                     \|B_n\|\le M_1C_1^n n!
 \tag{11}
\]
on fixed smaller \(z,x\) disks. The constants can depend on the
clock compact, but not on \(n\).

Here are the bounds for this specialization explicitly. A term
\(h^{a-1}\mathbf t^\gamma\) contributes to \(h^n\) exactly when
\(a+|\gamma|=n+1\). Its norm is bounded by
\(MC^a a!R^{-|\gamma|}\sup|m^\gamma|\), where \(R\) is a
buffered mark radius. The number of multiindices at each total
degree, and the sum over \(0\le a\le n+1\), cost an exponential
in \(n\). Also
\((n+1)!\le2^n n!\) for \(n\ge1\). This proves (11).
At order \(h^0\), the only possibilities are \((a,|\gamma|)=(1,0)\)
and \((0,1)\), giving the two displayed terms in (10).

Exponentiate the nonprincipal part:
\[
 a(h,z,x,m)=\sum_{j\ge0}h^j a_j(z,x,m)
    =e^{A_0+m\cdot\Theta}
                  \exp\left(\sum_{n\ge1}h^nB_n\right).
 \tag{12}
\]
All \(a_j\) are holomorphic on common disks and
\[
 \|a_j\|\le M_2 C_2^j j!,\qquad
                  a_0=e^{A_0+m\cdot\Theta}\ne0.
 \tag{13}
\]
Indeed a term with positive indices \(n_1+\cdots+n_k=j\)
has \(\prod n_i!\le j!\). The number of ordered compositions
of \(j\) is at most \(2^j\); the exponential's \(1/k!\) only
improves the estimate. Enlarging the exponential constant
absorbs the vertex constants and proves (13).

Equation (12) does not assert convergence of the series in \(h\).
It supplies analytic coefficients in \(x,z,m\) and a uniform
Gevrey bound. These are the properties used below.

## 3. An exact formula for the original Borel germ

Fix \(z\ne0\) sufficiently small. Since
\(\Psi_0(z,x,0)=O(x^2)\), \(f(z,0)=0\) and \(f_x(z,0)=z\).
Let \(x=x(z,\xi)\) denote its inverse at \(x=\xi=0\), only in
this section. Define
\[
 g_j(z,\xi,m)
       =\frac{a_j(z,x(z,\xi),m)}{f_x(z,x(z,\xi))}.
 \tag{14}
\]
Let \(I_\xi\) be the primitive starting at the original
\(\xi=0\). Then
\[
                 b_m(z,\xi)
                     =r(z)\sum_{j\ge0}I_\xi^j g_j(z,\xi,m)
 \tag{15}
\]
as actual convergent germs.

First check convergence. On a fixed sufficiently small inverse
disk, with \(z\ne0\) fixed, the functions in (14) satisfy
\(\|g_j\|\le M_z C_2^j j!\). Thus
\(\|I_\xi^j g_j\|\le M_z(C_2|\xi|)^j\), on a smaller star-shaped
disk. The series converges normally there.

Next check that its coefficients are those of (1). Since
\(g_j\,d\xi=a_j\,dx\), its order-\(h^N\) coefficient is
\[
 r(z)\sum_{j=0}^N (N-j)!
    \operatorname{Res}_{x=0}
         a_j(z,x,m)f(z,x)^{-(N-j+1)}\,dx .
 \tag{16}
\]
This follows by Cauchy coefficient extraction and the exact
coefficient shift of \(I_\xi^j\).
Expand \(f=zx-\Psi_0\). The term with power \(\ell\) of
\(\Psi_0/(zx)\) in (16) is
\[
 \frac{r(z)(N-j+\ell)!}
               {\ell!\,z^{N-j+\ell+1}}\,
             [x^{N-j+\ell}]\,a_j(z,x,m)\Psi_0(z,x,0)^\ell .
 \tag{17}
\]
Since \(\Psi_0=O(x^2)\), only \(\ell\le N-j\) can contribute.
Thus (16)--(17) are finite coefficient calculations.

The same expression is obtained from (1) after \(x=ht\):
use \(h^j a_j\), the term \(\Psi_0^\ell/(\ell!h^\ell)\)
of the phase exponential, and the exact moment
\[
      h^{-1}\int_0^\infty e^{-zx/h}x^d\,dx
                    =d!\,h^d z^{-d-1}
 \tag{18}
\]
as notation for \(\mathfrak L_z\), with \(d=N-j+\ell\).
At fixed \(N\) this is the same finite regrouping of the exact
formal hard-Wick reduction, not an analytic integral assumption.
Consequently (15) is the canonical Borel transform of the
original source. No other formal solution or cycle was selected.

## 4. A parameter-dependent Morse coordinate with its original base

The critical point in (3) is analytic and
\(f_{xx}(0,0)=-2\sigma\ne0\). Define the holomorphic nonzero factor
\[
 H(z,x)=\int_0^1(1-s)
    f_{xx}\bigl(z,x_g(z)+s(x-x_g(z))\bigr)\,ds .
 \tag{19}
\]
Taylor's formula gives
\(f(z,x)-\xi_g(z)=(x-x_g(z))^2H(z,x)\), and
\(H(0,0)=-\sigma\).
Choose one analytic square root of \(H\) and put
\[
             v=(x-x_g(z))\sqrt{H(z,x)}.
 \tag{20}
\]
This has a holomorphic inverse \(x=x(z,v)\) on fixed small disks.
In particular
\[
 f(z,x(z,v))=\xi_g(z)+v^2,\qquad
 v_0(z):=v(z,0),\qquad v_0(z)^2=-\xi_g(z).
 \tag{21}
\]
The base \(v_0(z)\) is holomorphic, is \(O(z)\), and is nonzero
for small \(z\ne0\). It is the image of the original endpoint
\(x=0,\xi=0\), not a new origin placed at the fold.

Put
\[
                H_j(z,v,m)
                  =a_j(z,x(z,v),m)\,\partial_vx(z,v).
 \tag{22}
\]
On fixed smaller disks these satisfy
\[
                         \|H_j\|\le M_3 C_3^j j!.
 \tag{23}
\]
On the initial inverse branch, \(g_j=H_j/(2v)\).
For \(j\ge1\), the exact original primitive in (15) is
\[
 I_\xi^j g_j
   =\frac1{(j-1)!}
       \int_{v_0(z)}^v
              (v^2-t^2)^{j-1}H_j(z,t,m)\,dt.
 \tag{24}
\]
Indeed the repeated-primitive kernel is
\((\xi-\xi')^{j-1}/(j-1)!\); use
\(\xi'=\xi_g+t^2\) and \(g_j\,d\xi'=H_j\,dt\).
This also proves that every primitive retains its original base
and continuation history. The integrand of (24) is holomorphic
through \(t=0\). Its integral is path-independent inside this
Morse disk. Continued paths remaining in this local twofold
domain therefore give precisely (24), including those exchanging
the two sheets.

## 5. Convergence through the fold and the actual leading minor

Choose \(r>0\) so that the inverse coordinate and bounds above hold
on \(|v|<r\), and shrink the \(z\)-disk so that \(|v_0(z)|<r\).
For endpoints in smaller closed disks the straight path in (24)
stays inside \(|t|<r\). Its length is at most \(2r\), and
\(|v^2-t^2|\le2r^2\). Hence
\[
 |I_\xi^j g_j|
       \le 2r M_3\,j\,C_3^j(2r^2)^{j-1}
                                    \qquad(j\ge1).
 \tag{25}
\]
Decrease \(r\) until \(2C_3r^2<1\). The sum of (24) then converges
normally and is jointly holomorphic in \(z,v,m\), including
\(z=v=0\). Equations (15) and (24) give the actual continuation
\[
 b_m=r(z)\left[
       \frac{H_0(z,v,m)}{2v}
       +\sum_{j\ge1}\frac1{(j-1)!}
        \int_{v_0(z)}^v
            (v^2-t^2)^{j-1}H_j(z,t,m)\,dt\right].
 \tag{26}
\]
The sole possible pole in this local cover is the explicit
simple pole in the first term.

Multiply (26) by \(v\), and split its analytic Taylor series in
\(v\) into even and odd powers. This gives exactly (7), with
\[
 A_m(z,0)=\frac{r(z)}2 H_0(z,0,m).
 \tag{27}
\]
Every \(j\ge1\) term is holomorphic in \(v\), and hence contributes
nothing to this residue. Substituting (13) and (22) proves (8).
The factors \(r\), \(\partial_vx\) and \(a_0\) are nonzero on
smaller neighborhoods. The fold is therefore genuinely present.
Its leading coefficient cannot disappear by cancellation with
the higher quantum corrections.

For completeness the odd part of (24) also has an explicit
description:
\[
 \frac{1}{2(j-1)!}\int_{-v}^{v}
                  (v^2-t^2)^{j-1}H_j(z,t,m)\,dt.
 \tag{28}
\]
The moving lower endpoint cancels here, after the actual
primitives have been formed. Expression (28) is
\(v^{2j-1}\) times a function holomorphic in \(v^2\).
Thus higher primitives contribute \(O(\rho)\) to \(A_m\),
consistent with (27). They have not been discarded from the
whole source (26).

Finally the factors common to \(m\) and \(m=0\) in (8) cancel,
giving (9). This is an identity of actual leading minors.
The neighborhood can shrink with the chosen clock compact;
no single uniform neighborhood for arbitrarily large clocks
is asserted by this proof.

## 6. Scope on the route to the volume identity

The factorial estimate does more than give a candidate phase:
it constructs the local analytic Borel source and proves the
nonvanishing of its marked fold coefficient. The leading
character \(e^{m\cdot\Theta_g}\) is consequently selected by the
original highest-cut source itself.

The selection here is local at a simple two-branch Alexander node.
It does not say that this local branch belongs to the geometric
component of a hyperbolic knot, or that it can be transported to
complete holonomy with all requisite source domains available.
It also does not compute the coefficient with which this minor
occurs in the original root-of-unity evaluation. Other periods
and endpoint currents of that evaluation remain present.

Thus the actual local minor/clock-character question is settled
under the stated hypotheses, whereas the arbitrary-short-partial-
filling and finite-exception assertions remain open.

## 7. Complete written proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| B | notes/research_actual_hard_wick_soft_reduction.md | b528230f79ceea7a9a812ac600bcb55e9ba7819a465218761e0f81fdd317002b |
| P | notes/research_actual_analytic_principal_phase.md | 9ae7b5df2dbd955ee6ac4580590d9f21d1b1750bcdd6c5085e7322251ab70bcb |
| D | notes/research_actual_symbol_factorial_deficiency.md | a757e1ac8f6e62268cd7c2d681758a0258394661181026aace2cd516f4ca3359 |

B supplies the actual formal moment identity and retained clocks.
P supplies the analytic principal phase, its calibration and critical
germ. D supplies the common-disk factorial estimate for all regular
hard logarithmic coefficients. The amplitude estimate, exact Borel
coefficient reconstruction, moving-base Morse formula, convergence
through the cover and nonzero actual minor are proved above.

Only written mathematics, source-text reads and hash checks were used.
Frozen manuscripts and public documentation are unchanged.
