# An actual coherent chart for each capped Euler coproduct factor

Private written proof, 18 November 2026.

The finite operator \(E_N(\lambda E_iK_{>i})\) has a regular,
nonzero coherent generating kernel for small complex \(\lambda\)
on every fixed compact set away from incidence. Its exact recurrence
retains the tail Cartan shifts and their finite coherent caps. A
coefficient majorant controls low activity degrees; the actual matrix
norm controls every remaining degree. Together these prove a relative
\(O(N^{-1})\) asymptotic, including the Cartan half-step and the
\(N-1\) endpoint correction.

This is a theorem about one actual coproduct factor. Composition into
a full source still requires its original resolutions, interfaces,
normals, and cycle. No such source contribution is inferred here.

The complete directs A and C are pinned below. A supplies the actual
one-head convention; C supplies the root coproduct and its original-
metric estimate. The coupled recurrence and analytic proof are below.

## 1. The literal capped recurrence

Fix \(N\ge2\), \(d=N-1\), \(h=N^{-1}\), \(c=2\pi i\),
\(Q=e^{ch}\), \(q_-=Q^{-1}\), and \(f_n=(Q;Q)_n\).
There are one donor and \(s\ge0\) later heads. The complete meridian
is fixed. Their actual matrices have
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\qquad
 Kw_a=xQ^{-a}w_a,\qquad x=-e^{-ch/2},
 \tag{1}
\]
with the original missing arrow at zero. Set
\[
 X=E_iK_{>i},\qquad
 U_N(\lambda)=E_N(\lambda X)
 =\sum_{n=0}^d\frac{\lambda^nX^n}{f_n},\qquad X^N=0.
 \tag{2}
\]
All kernels use evaluation rows and the original binomial columns.
For each head let \(I_a=w_{a,0}z_{a,0}+w_{a,1}z_{a,1}\ne0\).
For the donor and tails respectively put
\[
 \theta=\frac{w_{i,1}z_{i,1}}{I_i},\qquad
 t=\lambda\frac{w_{i,0}z_{i,1}}{I_i},\qquad
 \Theta_l=\frac{w_{l,1}z_{l,1}}{I_l}\quad(l>i).
 \tag{3}
\]
These are regular homogeneous ratios on the complements of incidence.

Let \(g_{j,n}(\theta)\) be the coefficient of \(t^n\) in A's
one-head polynomial
\[
 g_j(\theta,t)=\sum_{a=0}^j\binom ja(1-\theta)^{j-a}
                              \prod_{k=1}^a(\theta+q_-^kt).
\]
For the artificial donor slot number \(0\le j\le d\), keep the
tail degrees equal to \(d\) and define the exact normalized kernel
\[
 G_j(\theta,t,\boldsymbol\Theta)
 =\sum_{n=0}^j g_{j,n}(\theta)t^n c_n(\boldsymbol\Theta),\qquad
 c_n=x^{sn}\prod_{l>i}[1+(q_-^n-1)\Theta_l]^d.
 \tag{4}
\]
At \(j=d\) this is exactly
\(K_{U_N}/\prod_{a\ge i}I_a^d\). Indeed the donor coefficient
is A's finite \(E^n/f_n\) coefficient, while \(K_{>i}^n\)
has precisely the shifted finite binomial kernels in \(c_n\).
No tail occupation or projector has been continued or removed.

Define
\[
 \psi_h(\Theta)=\frac{q_-\Theta}{1+(q_--1)\Theta},\qquad
 C_h(\boldsymbol\Theta)=x^s\prod_{l>i}[1+(q_--1)\Theta_l]^d.
 \tag{5}
\]
On any fixed compact \(\boldsymbol\Theta\)-set these are holomorphic
for sufficiently small \(h\). Since
\(c_n=C_h\,c_{n-1}\circ\psi_h\), the one-head recurrence gives
\[
 \boxed{\begin{split}
 G_{j+1}(t,\boldsymbol\Theta)
 ={}&(1-\theta)G_j(t,\boldsymbol\Theta)
       +\theta G_j(q_-t,\boldsymbol\Theta)\\
 &+q_-t C_h(\boldsymbol\Theta)
                    G_j(q_-t,\psi_h\boldsymbol\Theta),\qquad G_0=1.
 \end{split}}\tag{6}
\]
For example its coefficient of \(t^n\) is
\((1-\theta+\theta q_-^n)g_{j,n}c_n+q_-^ng_{j,n-1}c_n\),
exactly (4). Although the separated terms of (6) use rational
coordinates, their sum is the finite polynomial (4).

Let
\[
 D=t\partial_t,\qquad
 L=\sum_{l>i}\Theta_l(1-\Theta_l)\partial_{\Theta_l}.
\]
Then \(\psi_h\) is exactly the time-\(h\) flow of \(-cL\).
The half-step \(x=-e^{-ch/2}\) gives the expansions
\[
 C_0=(-1)^s e^{-c\sum_l\Theta_l},\qquad
 C_h=C_0(1+h a_C+O(h^2)),
 \tag{7}
\]
\[
 a_C=c\sum_l(\Theta_l-\tfrac12)
                  +\frac{c^2}{2}\sum_l\Theta_l(1-\Theta_l).
 \tag{8}
\]
To check them, expand
\(\log[1+(e^{-ch}-1)\Theta]
=-ch\Theta+c^2h^2\Theta(1-\Theta)/2+O(h^3)\),
multiply by \(d=h^{-1}-1\), and include \(-chs/2\).
These expansions and fixed derivatives are uniform on enlarged compact
sets. The sign in \(C_0\) and every term of (8) remain.

## 2. Low-degree logarithms with a controlled tail neighborhood

Fix compact sets of donor \(\theta\) and tail \(\boldsymbol\Theta\).
Work first near one tail point in a slightly larger polydisk, and use
a finite cover at the end. Write
\(V_j=h\log G_j\) as a formal power series in \(t\), with zero
constant coefficient. Its coefficients are entire polynomials in
\(\boldsymbol\Theta\), since the coefficients in (4) are such
polynomials and a fixed logarithmic coefficient uses only finitely
many of them. Put
\[
 \delta_0V=\frac{V(q_-t,\boldsymbol\Theta)-V(t,\boldsymbol\Theta)}h,
 \qquad
 \delta_1V=\frac{V(q_-t,\psi_h\boldsymbol\Theta)-V(t,\boldsymbol\Theta)}h.
\]
The exact formal evolution is
\[
 V_{j+1}=V_j+h\mathcal F_h(V_j),\qquad
 \mathcal F_h(V)=
 \log\{1-\theta+\theta e^{\delta_0V}
                         +q_-t C_h e^{\delta_1V}\}.
 \tag{9}
\]
Its coefficient of \(v_n=[t^n]V_j\) is again exactly
\[
                     r_n=1-\theta+\theta q_-^n,
                             \qquad |r_n|\le e^{Cnh}.
 \tag{10}
\]
All tail shifts occur in the term with the extra activity \(t\).
This fact is essential to the following estimate.

We give the needed analytic majorant in detail. Expand holomorphic
tail functions about the chosen center. Absolute Taylor coefficients
in all tail variables are collapsed to one variable \(y\), by
replacing every tail deviation by \(y\). On a fixed small disk these
series converge. A positive vector field
\[
                         \mathcal L=a(y)\partial_y,
                  \qquad a(y)=C(1+y)^2
 \tag{11}
\]
majorizes the absolute coefficients of the actual tail vector field
\(-cL\), including its constant displacement at the center. Increase
\(C\) to absorb the fixed number of tails. Let \(\phi_u\) be its
positive analytic flow. For positive small \(u\), substitution by
the actual tail flow is majorized by \(e^{u\mathcal L}\), namely
substitution \(y\mapsto\phi_u(y)\). This follows by expanding both
flows into their convergent differential series, or their Picard
iterations, and taking absolute coefficients term by term. Also
\[
 \frac{e^{h\mathcal L}-1}{h}A
                          \preceq e^{h\mathcal L}\mathcal L A
 \tag{12}
\]
for a positive series \(A\). Here \(\preceq\) means coefficientwise
majorization.

The padding rule is the following. If coefficient \(k\) is majorized
by \(u_k(\phi_{kh}(y))\), then \(\delta_0\) on that coefficient
is bounded by \(Ck u_k(\phi_{kh}(y))\). For \(\delta_1\), split
the activity rotation and tail difference, use (12), and commute the
positive flow with its generator. Its bound is
\[
              (Ck+\mathcal L)u_k\bigl(\phi_{(k+1)h}(y)\bigr).
 \tag{13}
\]
Whenever (13) occurs in (9), the output activity degree is at least
\(k+1\). Thus the padding available at output degree \(n\) is
sufficient. For products, every input degree is at most \(n\), and
every shifted input degree is at most \(n-1\). Positivity permits all
their arguments to be increased to the common \(\phi_{nh}(y)\).
This proves the padding rule for every Taylor monomial in (9), not
only for its linearization.

For specificity, the nonlinear remainder after subtracting
\(\theta\delta_0V\) has a positive convergent majorant of the form
\[
 F(t,y,p,q)=C(y)\left[
       \frac{p^2}{1-C(y)p}
       +\frac{t}{1-C(y)(t+p+q)}\right],
                  \qquad C(y)=\frac{C}{1-y/R}.
 \tag{14}
\]
Constants and \(R\) are fixed after shrinking the tail polydisk.
Here \(p=DU\) and \(q=\mathcal L U\). To verify (14), first split
the logarithm in (9) into
\(\log(1-\theta+\theta e^A)\) and
\(\log[1+tq_-C_h e^B/(1-\theta+\theta e^A)]\).
The first minus \(\theta A\) starts in degree two in \(A\);
the second has an explicit \(t\). Expanding on a fixed small
polydisk gives (14). The uniform analytic bound on \(C_h\) follows
from (5),(7). Increasing constants absorbs \(Ck\) in (13).

Consider the positive analytic flow
\[
 U_\tau=C DU+F(t,y,DU,\mathcal L U),\qquad U(0,t,y)=0.
 \tag{15}
\]
It exists on fixed small \(t,y\) disks through time two. Here is
an elementary existence check. Write its right side as
\(H(t,y,p,q)\), with \(p=DU\), \(q=U_y\), substituting
\(a(y)q\) in (14). The characteristic equations are
\[
 \dot t=-tH_p,\quad \dot y=-H_q,\quad
 \dot p=tH_t,\quad \dot q=H_y,\quad
 \dot U=H-pH_p-qH_q.
 \tag{16}
\]
Initially \(p=q=U=0\). At \(t=0\) the solution remains
\(p=q=U=0\), with \(y\) fixed and \(\dot t=-Ct\).
On a small polydisk the nonconstant right sides are bounded by
\(C'(|t|+|p|+|q|)\). Integration and Gronwall keep these quantities
\(O(|t(0)|)\) for time two, while \(y\) moves only
\(O(|t(0)|)\). Picard iteration gives analytic dependence.
The initial-to-final coordinate map has, at \(t=0\), diagonal
Jacobian entries \(e^{-C\tau}\) and one; it is uniformly invertible
on a smaller polydisk. As in A, differentiating the characteristic
equations proves \(p=DU,q=U_y\). This constructs (15) analytically.
Its coefficients are nonnegative: Picard iteration of the positive
coefficient equation has this property on short intervals, and
continuation preserves it. Equivalently one may compare its
coefficient equations successively on such intervals.

The two-half-step comparison from A now applies with the additional
positive derivative \(\mathcal L\). The time-\(h\) flow dominates
\(A+hF(t,y,DA,\mathcal L A)\); a second time \(h\) dominates
\(e^{ChD}\). Combining (10),(13),(14), induction proves
\[
 |[t^n]V_j|_{\rm tail\ coeff}
       \preceq [t^n]U(2jh,t,\phi_{nh}(y)),\qquad j\le d.
 \tag{17}
\]
We use (17) only for \(n\le L_N=\lfloor\delta N\rfloor\).
Choose \(\delta>0\) so that \(\phi_\delta\) maps a smaller
tail disk into the analytic disk of (15). Then Cauchy's estimate
for \(U\) gives fixed constants \(C_1,R_1>0\) such that
\[
          |[t^n]V_j|\le C_1R_1^{-n},
                \qquad 1\le n\le L_N,\quad j\le d,
 \tag{18}
\]
uniformly on that smaller tail neighborhood. Fixed tail derivatives
have the same statement on further smaller neighborhoods.
The proof does not require a full unit-time tail rotation to remain
in this neighborhood. Only the bounded padding \(nh\le\delta\)
has been used.

## 3. Actual high-degree terms and zero-freeness

We now pay the degrees not covered by (18). For the artificial donor
of dimension \(j+1\), use its binomial metric \(\binom ja^{-1}\).
Its lowering norm is at most \(\pi(j+1)/N\le\pi\) for \(j\le d\):
\[
 |Q^{-a}-1|\sqrt{(j+1-a)/a}
 \le(2\pi/N)\sqrt{a(j+1-a)}.
\]
Tail Cartans are unitary in their original metrics. Thus the actual
operator behind (4) has \(\|X\|\le\pi\), \(X^N=0\).
C's finite logarithm estimate gives
\(\|E_N(tX)\|\le e^{C_2N|t|}\) on a fixed small circle.
For a concrete realization of arbitrary bounded normalized parameters,
choose donor homogeneous coordinates
\((w_0,w_1)=(1,\theta)\), \((z_0,z_1)=(1-\theta,1)\),
and the same construction with \(\Theta_l\) on each tail.
All incidence pairings equal one. The exact binomial norms in C
then give, uniformly on a slightly larger tail neighborhood,
\[
                |G_j(\theta,t,\boldsymbol\Theta)|
                      \le e^{\kappa N+C_2N|t|},\qquad j\le d.
 \tag{19}
\]
The fixed constant \(\kappa\) retains the coherent conditioning.

Let \(V_j^{[L]}\) be the Taylor polynomial of the formal logarithm
through degree \(L=L_N\). By (18), on a fixed smaller activity
circle \(|t|=R_2<R_1\),
\(|V_j^{[L]}|\le C_3R_2\). The functions
\(G_j\) and \(\exp(V_j^{[L]}/h)\) have identical Taylor
coefficients through degree \(L\). Cauchy's estimate therefore gives
for \(|t|\le\rho R_2\), \(0<\rho<1\),
\[
 |G_j-e^{V_j^{[L]}/h}|
 \le\frac{2\rho^{L+1}}{1-\rho}
                   e^{N(\kappa+C_4R_2)}.
 \tag{20}
\]
Also \(|e^{V_j^{[L]}/h}|\ge e^{-C_3N\rho R_2}\).
Take \(\rho\) sufficiently small, after fixing \(\delta,R_2\),
so that \(\delta\log\rho+\kappa+C_4R_2+C_3\rho R_2<0\).
It follows that
\[
             G_j=e^{V_j^{[L]}/h}(1+O(e^{-\eta N})),\qquad j\le d,
 \tag{21}
\]
for some \(\eta>0\), uniformly on the resulting nonempty activity
disk. Hence the actual polynomials are zero-free there for all
sufficiently large \(N\). If desired, finitely many smaller levels
are included by reducing the radius, since \(G_j(0)=1\).
All remaining finite coefficients have been estimated, not omitted.

## 4. Analytic phase, half-step, and transport

The limiting equation for the phase is explicit:
\[
 V_\tau=\mathcal F(V)=\log Z,\qquad V(0)=0,
 \tag{22}
\]
\[
 Z=1-\theta+\theta e^{-cDV}
            +tC_0e^{-c(D+L)V}.
\]
It has a unique analytic solution through \(0\le\tau\le1\)
on a sufficiently small activity disk and enlarged tail neighborhood.
Indeed this is a first-order analytic equation in \(t,\boldsymbol\Theta\).
At \(t=0\), all momenta stay zero; its tail characteristic velocity
is zero, while its activity characteristic is \(\dot t=c\theta t\).
The full characteristic vector field differs by \(O(t)\) on a small
neighborhood. The same Picard, Gronwall, and invertible-projection
argument as (16), now for the fixed finite number of tail coordinates,
proves the assertion. The initial projection has determinant
\(e^{c\theta\tau}\ne0\). This fixes the phase by \(V(0)=0\)
and \(V(\tau,t=0)=0\), including its additive constant.

For the first correction put
\[
 P=e^{-cDV},\qquad R=e^{-c(D+L)V}.
\]
Since the two shifts in (9) are exact flows, (7)--(8) give
\[
 \mathcal F_h(V)=\mathcal F(V)+h\mathcal F_1(V)+O(h^2),
 \tag{23}
\]
\[
 \mathcal F_1(V)=\frac1Z\left\{
  \frac{c^2}{2}\theta P D^2V
  +tC_0R\left[a_C-c+\frac{c^2}{2}(D+L)^2V\right]\right\}.
 \tag{24}
\]
The \(-c\) is the literal \(q_-t\) in (6); \(a_C\) includes
the retained Cartan half-step. Define \(A(0)=0\) by the linear
analytic transport equation
\[
 A_\tau=-\frac cZ\{\theta P DA+tC_0R(D+L)A\}
                  +\mathcal F_1(V)-\tfrac12V_{\tau\tau}.
 \tag{25}
\]
Integration along the already proved analytic characteristics defines
an analytic \(A\), with \(A(\tau,0)=0\). Its exponential is a unit.
Equations (22)--(25) are also explicit ways to compute the phase and
coefficient, with no unspecified normalization.

We justify comparison with the actual finite recurrence. Put
\(W_j=V(jh)+hA(jh)\). Taylor's formula and (23)--(25) give
\[
 W_{j+1}-W_j-h\mathcal F_h(W_j)=O(h^3),
 \tag{26}
\]
uniformly on larger fixed analytic neighborhoods, with zero constant
activity coefficient. The low-degree coefficient error obeys the
same padding rule (13). After its exact linear multiplier (10) is
removed, the derivative of the nonlinear remainder has a majorant
\[
                  B_1(t,y)D e+B_2(t,y)\mathcal L e,
 \tag{27}
\]
where the positive analytic functions \(B_1,B_2\) vanish at \(t=0\).
For the \(D\) term this follows from the quadratic remainder in
\(\delta_0V\), whose already bounded inputs are \(O(t)\).
Every \(\mathcal L\) term comes from the explicit \(t\) part
of (9), so consumes the extra padding degree required in (13).
The bounds (17) and the analytic \(V,A\) provide uniform coefficient
majorants for these derivatives. The residual (26) has a majorant
\(h^3 B_0(t,y)\), where \(B_0\) is positive analytic and \(O(t)\).

The positive linear flow
\[
 Z_\tau=C DZ+B_1DZ+B_2\mathcal LZ+B_0,\qquad Z(0)=0,
 \tag{28}
\]
exists analytically through time two on smaller fixed neighborhoods:
its tail velocity is \(O(t)\), and its initial activity velocity
is \(-Ct\). The two-half-step comparison proves, exactly as in
(17),
\[
 |[t^n](V_j-W_j)|_{\rm tail\ coeff}
       \preceq h^2[t^n]Z(2jh,t,\phi_{nh}(y)),
                  \qquad n\le L_N.
 \tag{29}
\]
This pays the discrete stability rather than merely its consistency.
After summing on a smaller activity disk, the analytic tail of \(W_j\)
beyond \(L_N\) is exponentially small. Equations (21),(29) therefore
give
\[
             G_j=e^{N V(jh)+A(jh)}(1+O(N^{-1})),\qquad j\le d.
 \tag{30}
\]
The exponentially small terms can be made smaller than the stated
relative error by the prior choice of the inner radius. Fixed
derivatives follow by Cauchy on nested neighborhoods.

Finally set \(j=d\). The endpoint \(d/N=1-h\) gives
\[
 \boxed{\quad
 G_d=e^{N V(1)}\,a\,(1+O(N^{-1})),\qquad
                  a=\exp\{A(1)-V_\tau(1)\}\ne0.
 \quad}\tag{31}
\]
At zero activity \(V=A=V_\tau=0\), hence \(a=1\).
For no tails this is A's explicit one-head phase and coefficient.

## 5. Actual chart, canonical rows, and retained source scope

A finite cover of the compact tail and donor parameter sets makes
all preceding constants uniform. On any
\(\mathcal K\Subset X^{s+1}\), (3) is bounded. Thus a fixed
small \(\lambda\)-disk gives the actual homogeneous kernel
\[
 \boxed{\quad
 K_{U_N}(\mathbf w,\mathbf z)
 =\prod_{a\ge i}I_a^d\ e^{N V(1,\theta,t,\boldsymbol\Theta)}
                      a(\theta,t,\boldsymbol\Theta)(1+O(N^{-1})).
 \quad}\tag{32}
\]
It is zero-free there for all large \(N\), uniformly on smaller
compacts. The leading amplitude is a holomorphic unit. All fixed
coherent and activity derivatives have the same relative estimate.
The local phase is \(\sum_a\log I_a+V\); its mixed Hessian at
\(\lambda=0\) is the diagonal identity-kernel Hessian, with entries
\((1+w_az_a)^{-2}\) in affine coordinates. Hence it remains
nondegenerate on smaller compact charts for sufficiently small
\(\lambda\). This is an actual regular generating kernel near
identity, including projective coordinate infinities.

The graph is checked by literal finite rows, not used to assume the
asymptotic. For a tail head \(l>i\), direct commutation gives
\[
 E_iU_N=U_NE_i,\qquad K_iU_N=(1-\lambda X)U_NK_i,
 \qquad K_lU_N=U_NK_l,
 \tag{33}
\]
\[
 E_lU_N=(1-Q^{-1}\lambda X)^{-1}U_NE_l,
                  \qquad F_lU_N=(1-\lambda X)U_NF_l.
 \tag{34}
\]
The inverse is finite because \(X^N=0\). These follow from
\(KE=QEK\), \(KF=Q^{-1}FK\), and the exact finite Euler
recurrence; all original arrows remain. Consequently the principal
map of (32) preserves donor \(e_i\) and each tail \(k_l\), sends
\(k_i\) to \((1-\lambda\xi)k_i\), and sends tail
\(e_l,f_l\) to \((1-\lambda\xi)^{-1}e_l,(1-\lambda\xi)f_l\),
respectively, where \(\xi=e_i\prod_{l>i}k_l\).

This result is at the fixed root and complete meridian. It does not
differentiate \(E(M)\), its vacuum row, or denominators such as
\((M^{-2}Q;Q)_n\). C's whole-meridian operator carry estimate is
not being converted into a missing meridian-normal kernel theorem.
All such insertions must still be retained separately.

Nor does (32) justify composing local kernels over a full compact
chain by ignoring its complement or possible cross-pair incidence.
It supplies the local factor needed for such a composition argument.
C retains the high-degree coproduct carry; the opposite-source
quotient, turnover, original cut, pivotal normalization, and relative
window currents remain. No geometric-cycle coefficient or closed
source lower bound is claimed.

## Complete proof directs

* A: notes/research_actual_one_head_euler_coherent_flow.md,
  SHA256 a18a31a9b338a936b1a03a112b091c0da7588e6b88baa502b1378bb004cf3e65.
* C: notes/research_root_capped_euler_coproduct_factorization.md,
  SHA256 e11f5f827f226ee93505e00aed3885a33abdbfc15ee71e023a67c048c9c17720.

Both complete directs were freshly read nontruncated in this active
author/formal-review sequence and retained unchanged. The matching
entire final was read back, every used implication checked, and all
three hashes renewed before freezing. Only written mathematics and
text/hash operations were used. Frozen and public files were unchanged.
