# The actual one-head finite Euler kernel through a small coherent activity

Private written proof, 18 November 2026.

The finite Euler polynomial of the actual root lowering operator has
a nonzero coherent-kernel asymptotic on every compact chart away from
incidence, for sufficiently small complex Euler parameter. This follows
from its exact finite recurrence. A coefficient majorant proves that
the actual logarithm converges uniformly; a second majorant proves the
relative error. Thus the analytic characteristic calculation below is
not being used as a substitute for an asymptotic theorem.

The donor and recipient coordinates remain the original binomial
coherent coordinates. All finite endpoint terms remain. This result
estimates one actual matrix factor; it does not evaluate its contraction
with the opposite-source quotient or identify a geometric contribution
to a closed period.

The sole complete direct S is pinned below. It supplies the literal
root matrices and their coherent convention. All finite identities and
analytic estimates needed here are proved inline.

## 1. The exact finite polynomial and a homogeneous recurrence

Put
\[
 c=2\pi i,\quad N\ge2,\quad d=N-1,\quad h=N^{-1},\quad
 Q=e^{ch},\quad q_-=Q^{-1},\quad f_n=(Q;Q)_n.
 \tag{1}
\]
The actual lowering matrix at the complete meridian is
\[
 E w_a=(Q^{-a}-1)w_{a-1}\quad(a\ge1),\qquad Ew_0=0,
 \qquad E^N=0.
\]
Define the actual finite operator
\[
 U_N(\lambda)=\sum_{n=0}^d\frac{\lambda^n E^n}{f_n}.
 \tag{2}
\]
With evaluation row \(v(w)w_a=w^a\) and binomial column
\(c(z)=\sum_a\binom da z^aw_a\), its exact kernel is
\[
 \boxed{\quad
 v(w)U_N(\lambda)c(z)
   =\sum_{a=0}^d\binom da z^a
                       \prod_{k=1}^a(w+Q^{-k}\lambda).
 \quad}\tag{3}
\]
Indeed, for \(n\le a\), the coefficient of \(w_{a-n}\) in
\(E^nw_a/f_n\) is
\[
 {a\brack n}_Q Q^{-na+n(n-1)/2}.
\]
It is exactly the coefficient of \(w^{a-n}\lambda^n\) in the
product in (3), by the finite binomial product. For \(n>a\)
both sides vanish. No occupation has been continued to a complex index.

Use homogeneous coordinates \(w=(w_0,w_1)\), \(z=(z_0,z_1)\).
On the complement of incidence put
\[
 I=w_0z_0+w_1z_1\ne0,\qquad
 \theta=\frac{w_1z_1}{I},\qquad
 t=\lambda\frac{w_0z_1}{I}.
 \tag{4}
\]
These ratios are regular functions on
\(X=(\mathbb P^1\times\mathbb P^1)\setminus\{I=0\}\).
The homogeneous version of (3), divided by \(I^d\), is
\[
 G_d(\theta,t)=\sum_{a=0}^d\binom da(1-\theta)^{d-a}
                         \prod_{k=1}^a(\theta+q_-^kt).
 \tag{5}
\]
For every integer \(j\ge0\), define the same expression with
\(d\) replaced by \(j\), while keeping the fixed \(Q\) in (1).
Pascal's identity and removal of the first product factor give
\[
 \boxed{\quad
 G_{j+1}(\theta,t)
 =(1-\theta)G_j(\theta,t)
        +(\theta+q_-t)G_j(\theta,q_-t),\qquad G_0=1.
 \quad}\tag{6}
\]
In particular \(G_j(\theta,0)=1\). Equation (6), including its
last step \(j=d-1\), is exact for the physical kernel.

## 2. A uniform analytic logarithm of the actual recurrence

Fix an arbitrary compact set of \(\theta\)-values, enlarged slightly
to an open neighborhood with compact closure. Constants below are
uniform there. Let \(D=t\partial_t\). Initially interpret
\[
 V_j=h\log G_j
\]
as a formal power series with constant coefficient zero. Define
\[
 \delta_h V(t)=\frac{V(q_-t)-V(t)}h,
 \qquad
 \mathcal F_h(V)=
 \log\{1-\theta+(\theta+q_-t)e^{\delta_hV}\}.
 \tag{7}
\]
The logarithm in (7) is its formal series at constant coefficient one.
The exact recurrence is
\[
                         V_{j+1}=V_j+h\mathcal F_h(V_j).
 \tag{8}
\]

We prove convergence uniformly for \(0\le j\le N\), rather than
assuming that the finite \(G_j\) has no zeros. The coefficient of
\(t^n\) in \(\delta_hV\) is
\((q_-^n-1)v_n/h\), whose absolute value is at most
\(|c|n|v_n|\). The part of \(\mathcal F_h\) linear in \(V\)
is \(\theta\delta_hV\). Consequently the coefficient of \(v_n\)
in (8) is exactly
\[
 r_n=1-\theta+\theta q_-^n,
                  \qquad |r_n|\le e^{Cnh}.
 \tag{9}
\]
Every other term of coefficient \(n\) uses only \(v_1,\ldots,v_{n-1}\).
The Taylor series in two variables of
\(\log(1-\theta+(\theta+q_-t)e^w)-\theta w\)
has an absolute coefficient majorant, uniform in \(N,\theta\), of
the form
\[
 F(t,p)=C t+\frac{C(t+p)^2}{1-C(t+p)},\qquad p=D U,
 \tag{10}
\]
after increasing \(C\) to absorb \(|c|\).
This follows directly by expanding the exponential and logarithm on
a fixed small bidisk in \((t,w)\); there is no term linear in \(w\)
left after the subtraction.

Here and below inequalities of formal series with nonnegative
coefficients are coefficientwise. Consider the positive majorant flow
\[
 \partial_\tau U=C D U+F(t,D U),\qquad U(0,t)=0.
 \tag{11}
\]
It has an analytic solution on a fixed small \(t\)-disk for
\(0\le\tau\le2\). The following elementary characteristic argument
also supplies the required uniform radius. Put \(p=D U\). The
characteristic equations are
\[
 \dot t=-t(C+F_p(t,p)),\qquad
 \dot p=t F_t(t,p),\qquad
 \dot U=F(t,p)-pF_p(t,p).
 \tag{12}
\]
At \((t,p)=(0,0)\) all right sides vanish except for the harmless
linear coefficient \(-Ct\). On a sufficiently small bidisk,
\(F_p=O(t+p)\) and \(tF_t=O(t)\). Integration and the elementary
Gronwall inequality therefore keep \(|t|+|p|\le C_1|t(0)|\)
for time two. Picard iteration on a slightly larger bidisk gives
holomorphic dependence on the initial value. Moreover
\(\partial t(\tau)/\partial t(0)=e^{-C\tau}+O(|t(0)|)\).
The inverse-function theorem, uniformly on the compact time interval,
then gives an analytic solution \(U(\tau,t)\) on a fixed disk.
Differentiating (12) verifies \(p=D U\) and (11). Alternatively this
identity follows from its zero initial value and its homogeneous
linear evolution. The coefficient equations of (11) show inductively
that all coefficients of \(U\) are nonnegative.

For clarity, this flow really dominates the discrete recurrence.
If the absolute coefficients of \(V_j\) are bounded by a nonnegative
series \(A\), (9)--(10) bound the next series by
\[
                   e^{ChD}\{A+hF(t,D A)\}.
 \tag{13}
\]
The time-\(h\) flow of (11), starting at \(A\), dominates
\(A+hF(t,D A)\): every coefficient is increasing and the vector
field has nonnegative coefficients. A further time \(h\) dominates
the linear flow \(e^{ChD}\). These statements hold coefficient by
coefficient; the already established analytic solution bounds their
series. Induction gives
\[
              |V_j|_{\rm coeff}\le U(2jh,t),\qquad j\le N.
 \tag{14}
\]
Thus all formal logarithms converge on a fixed disk, uniformly in
\(j,N,\theta\). Their exponentials equal the polynomials \(G_j\)
by equality of Taylor coefficients. In particular
\[
 \boxed{\quad G_j(\theta,t)\ne0\quad(j\le N,\ |t|<\epsilon),\quad}
 \tag{15}
\]
for a fixed \(\epsilon>0\), with the analytic logarithm fixed by
\(G_j(\theta,0)=1\). This is an actual zero-free statement.

## 3. The calibrated analytic flow and its subprincipal transport

The limiting equation suggested by (8) will now be solved analytically
and then compared with the actual recurrence. Put
\[
 \mathcal F(V)=\log Z,\qquad
 Z=1-\theta+(\theta+t)e^{-cDV},\qquad
 \partial_\tau V=\mathcal F(V),\quad V(0,t)=0.
 \tag{16}
\]
Let \(b\) be a small initial activity and define
\[
 \omega(b)=\frac{c(\theta+b)}{1+b},\qquad
 t_\tau=b e^{\tau\omega(b)},\qquad
 \Delta_\tau=1+\frac{c\tau(1-\theta)b}{(1+b)^2}.
 \tag{17}
\]
The map \(b\mapsto t_\tau\) has derivative
\(e^{\tau\omega(b)}\Delta_\tau\), nonzero on a fixed small disk,
uniformly for \(0\le\tau\le1\) and the stated \(\theta\)-set.
It has a unique small analytic inverse. Define
\[
 R_\tau=1+\frac{c\tau b}{1+b}
         \operatorname{exprel}\!\left(\frac{c\tau(\theta+b)}{1+b}\right),
 \qquad p_\tau=\frac1c\Log R_\tau,
 \tag{18}
\]
where \(\operatorname{exprel}(z)=(e^z-1)/z\) with value one at zero.
Equivalently \(R_\tau=(\theta+t_\tau)/(\theta+b)\), but (18)
is the required removable expression when \(\theta+b=0\).
All logarithms are continued from \(b=0\). Finally set
\[
 V(\tau,t_\tau)
 =\tau\log(1+b)+\omega(b)\int_0^\tau p_\sigma\,d\sigma.
 \tag{19}
\]
These are analytic functions on the same small disk.

Here is a direct verification of (16). With
\(W=e^{-cp}\), its characteristic equations are
\[
 \dot t=\frac{c t(\theta+t)W}{Z},\qquad
 \dot p=\frac{tW}{Z},\qquad
 \dot V=\log Z+\frac{c p(\theta+t)W}{Z}.
 \tag{20}
\]
Equations (17)--(18) give
\((\theta+t_\tau)e^{-cp_\tau}=\theta+b\) and \(Z=1+b\).
They satisfy the first two equations in (20), and (19) satisfies the
third. Differentiation with respect to the initial activity shows
\(p=DV\); the possible difference has zero initial value and the
homogeneous linear characteristic equation. This proves (16), with
its integration constant fixed. In particular \(V(\tau,0)=0\).

The first correction in the exact map (7) is
\[
 \mathcal F_h(V)=\mathcal F(V)+h\mathcal F_1(V)+O(h^2),\qquad
 \mathcal F_1(V)=\frac WZ
       \left[-ct+\frac{c^2}{2}(\theta+t)D^2V\right].
 \tag{21}
\]
This is an analytic expansion on smaller disks, with fixed derivatives:
expand \(V(e^{-ch}t)\) and \(e^{-ch}t\) directly.
The transport equation for a subprincipal function \(A\) is
\[
 \partial_\tau A
 =-\frac{c(\theta+t)W}{Z}D A
       +\mathcal F_1(V)-\tfrac12\partial_\tau^2V,
                 \qquad A(0,t)=0.
 \tag{22}
\]
It has the explicit solution
\[
 \boxed{\quad A(\tau,t_\tau)=-\frac c2p_\tau-\frac12\Log\Delta_\tau.\quad}
 \tag{23}
\]
To check this without a transport assumption, differentiate (16):
\[
 V_{\tau\tau}
 =-\frac{c(\theta+t)W^2}{Z^2}
                  \{t-c(\theta+t)Dp\}.
\]
Along (17),
\[
 Dp=\frac1c\left\{\frac{t}{\theta+t}
                  -\frac{b}{\Delta_\tau(\theta+b)}\right\}.
\]
The displayed fractions have their removable meaning from (18).
Substituting into the right side of (22) along the characteristic
cancels the two mixed terms and leaves
\[
 -\frac12\omega(b)\frac{t_\tau}{\theta+t_\tau}
       -\frac12\frac{b\omega'(b)}{\Delta_\tau}
       =-\frac c2\dot p_\tau-\frac12\partial_\tau\Log\Delta_\tau.
\]
Analytic continuation across the removable denominators proves (23)
everywhere on the small chart, including \(\theta=0\).

## 4. Comparison with the actual finite kernel

We supply an analytic error argument for the discrete evolution.
Let \(W_j=V(jh,\cdot)+hA(jh,\cdot)\). Equations (16),(21),(22)
and Taylor's formula give
\[
 W_{j+1}-W_j-h\mathcal F_h(W_j)=\mathcal R_j,
                   \qquad \mathcal R_j=O(h^3),\quad \mathcal R_j(0)=0,
 \tag{24}
\]
uniformly on a fixed small disk, for \(j<N\). Uniform analyticity
on a larger disk gives a coefficient majorant
\(|\mathcal R_j|_{\rm coeff}\le C h^3t/(r-t)\).
All constants can be chosen uniformly in \(\theta\) on the original
compact set.

Here is the stability estimate needed for summing (24). The bounds
(14) and the analytic functions (19),(23), on slightly larger disks,
majorize the coefficients of \(V_j,W_j,\delta_hV_j,\delta_hW_j\)
by fixed convergent series with zero constant term. In the difference
\(\mathcal F_h(V_j)-\mathcal F_h(W_j)\), the term linear in their
difference is \(\theta\delta_h(V_j-W_j)\). Expanding the remaining
analytic difference, or integrating its derivative on the formal
line segment, gives a majorant
\[
 B(t)D e_j,\qquad B(t)=\frac{C t}{r-t},\qquad
 e_j=|V_j-W_j|_{\rm coeff}.
 \tag{25}
\]
The factor \(t\) occurs because the derivative of the nonlinear
remainder in (10) vanishes at \((t,p)=(0,0)\). The estimate for
\(\delta_h\) again uses \(|q_-^n-1|/h\le|c|n\).
Thus (9),(24) give
\[
 e_{j+1}\le e^{ChD}
       \left\{e_j+hB(t)D e_j+C h^3\frac{t}{r-t}\right\},
                         \qquad e_0=0.
 \tag{26}
\]

For completeness, a fixed analytic majorant for this recurrence is
obtained from the linear positive flow
\[
 \partial_\tau Z=C D Z+B(t)D Z+C\frac{t}{r-t},\qquad Z(0,t)=0.
 \tag{27}
\]
Its characteristic equation is \(\dot t=-t(C+B(t))\).
For a sufficiently small initial disk it and the integral of the
displayed analytic forcing are regular through time two; the inverse
characteristic map is regular as in (12). Hence \(Z\) is analytic
on a fixed smaller disk. Its coefficients are nonnegative. The same
two-step flow comparison used in (13) now gives
\[
                  e_j\le h^2 Z(2jh,t),\qquad j\le N.
 \tag{28}
\]
This proves the actual, uniform estimate
\[
              V_j=V(jh,t)+hA(jh,t)+O(h^2).
 \tag{29}
\]
Every fixed derivative follows on smaller disks by Cauchy estimates.
In particular no high-order formal expansion has been substituted
for an uncontrolled finite polynomial.

Use \(j=d=N-1\) in (29). Since \(V_\tau(1,t)=\log(1+b)\)
along (17), where now \(t=b e^{\omega(b)}\), the endpoint shift
\(d/N=1-h\) gives
\[
 \boxed{\quad
 G_d(\theta,t)=e^{N V(1,t)}
       \frac{e^{-cp/2}}{(1+b)\sqrt{\Delta}}
                         (1+O(N^{-1})),
 \quad}\tag{30}
\]
where
\[
 t=b\exp\!\left[\frac{c(\theta+b)}{1+b}\right],\qquad
 p=\frac1c\Log\!\left[\frac{\theta+t}{\theta+b}\right],\qquad
 \Delta=1+\frac{c(1-\theta)b}{(1+b)^2}.
 \tag{31}
\]
The ratio for \(p\) always means (18). The square root and all
logarithms are one or zero, respectively, at \(b=0\).
Every factor in the leading coefficient is nonzero on the small
chart. The relative error and its fixed derivatives are uniform.

As a check that the upper cap has not been erased, at \(\theta=1\)
the exact recurrence gives
\[
 G_d(1,t)=\prod_{k=1}^d(1+Q^{-k}t)
                  =\frac{1-(-t)^N}{1+t}.
 \tag{32}
\]
Here (31) gives \(b=t,p=0,\Delta=1\), and \(V(1,t)=0\) since
\(DV=p=0\) and \(V(1,0)=0\). Formula (30) therefore gives
the correct unit \((1+t)^{-1}\); the exact Fermat numerator in
(32) is exponentially close to one on the proved small disk.

## 5. The actual coherent chart and its limits

For any compact \(\mathcal K\Subset X\), the two functions
\(\theta\) and \(w_0z_1/I\) in (4) are bounded. Thus a fixed
small disk \(|\lambda|<\epsilon_{\mathcal K}\) puts the actual
kernel in (30). In homogeneous notation the theorem is
\[
 \boxed{\quad
 K_{U_N}(w,z)=I^d e^{N V(1,\theta,t)}
       \frac{e^{-cp/2}}{(1+b)\sqrt{\Delta}}
                        (1+O(N^{-1})).
 \quad}\tag{33}
\]
It is valid through projective coordinate infinities: all normalized
parameters used in the proof are regular on \(X\). The actual
normalized kernel is zero-free on this neighborhood for every \(N\)
by (15), and its displayed asymptotic coefficient is a unit.
At \(\lambda=0\) it is exactly the original identity kernel.

In a local trivialization its phase is \(\log I+V\), with the
additional amplitude factor \(I^{-1}\) from \(d=N-1\). At
\(\lambda=0\), the mixed phase derivative in affine coordinates
is \(\partial_w\partial_z\log(1+wz)=(1+wz)^{-2}\), nonzero.
Continuity and the proved derivative bounds keep this mixed derivative
nonzero on smaller compact charts for sufficiently small \(\lambda\).
Thus (33) is a regular local generating kernel near the identity,
including its computed nonzero amplitude.

The finite canonical rows are also explicit. With the original
\(K\), one has \(KE=QEK\), so
\[
 EU_N=U_NE,\qquad KU_N=(1-\lambda E)U_NK.
 \tag{34}
\]
For the second identity use the exact polynomial recurrence
\(E_N(QX)=(1-X)E_N(X)+X^N/N\) at \(X=\lambda E\);
the last term is zero as a matrix. Therefore the actual phase in
(33), when read in the original coherent canonical coordinates,
has \(e_{\rm out}=e_{\rm in}\) and
\(k_{\rm out}=(1-\lambda e_{\rm out})k_{\rm in}\).
These rows check the graph of an already proved analytic kernel.
They were not used to infer its amplitude or its zero-freeness.

The theorem is at fixed quantum root and complete meridian. It does
not differentiate the meridian-dependent lowering matrix, its vacuum
row, or a shifted denominator \((M^{-2}Q;Q)_n\). Those are additional
actual normal insertions. Likewise no quantum-parameter derivative is
obtained by differentiating \(E^N=0\) or the root products.

All occupations, including the original finite upper and lower arrows,
have been retained in (2)--(6). The theorem controls one actual Euler
factor on a small coherent neighborhood; it does not replace a
coproduct factorization, an inverse-factorial donor contraction, the
quotient \(q_F\), or the original pivotal first-jet closing row.
No assertion is made that a prescribed geometric source frame lies in
this neighborhood, or that a closed source period is nonzero.

## Complete proof direct

* S: notes/research_finite_trace_separator_and_opposite_characteristic.md,
  SHA256 1d5abd4e14df7aa32f17405e27543a35d815c130903ed379ab9c60bec2eef0f6.

The complete direct was freshly reread nontruncated in this author
sequence. The entire final was read back, every used implication
checked, and both hashes renewed before freezing. Only written
mathematics and text/hash operations were used. Frozen and public
files were unchanged.
