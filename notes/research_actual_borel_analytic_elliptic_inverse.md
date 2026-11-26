# An analytic elliptic inverse for the actual Borel shift equation

Private written proof, 18 November 2026.

The finite-shift Borel equation of the original source has a convergent
local inverse at a noncharacteristic tilted covector. The inverse is
proved here by a deficiency-sensitive coefficient estimate. Its actual
primitive histories are then retained to obtain holomorphic extension
of the canonical source across a supplied product wedge.

The product-domain hypotheses are stated explicitly below. A further
corollary constructs the required slab at a supplied smooth
noncharacteristic boundary. This note does not construct a global
exhaustion of the known Borel cluster by such boundaries, identify a
moving singular divisor, or identify an infinite Laplace sum with the
physical invariant.

## 1. The actual equation and the local assertion

Use the original logarithmic meridian \(u=\log Y\), \(h=\log Q\), and
canonical Borel transform of [B]:
\[
 b(u,\xi)=\sum_{j\ge0}W_j(e^u)\frac{\xi^j}{j!}.
 \tag{1}
\]
Let an actual annihilator, with its original state gauge retained, be
\[
 \mathcal P=\sum_{i\in\mathcal I}p_i(h,u)T^i,
 \qquad Tf(u)=f(u+h),\qquad
 P(u,L)=\sum_i p_i(0,u)L^i.                         \tag{2}
\]
Here \(\mathcal I\subset\mathbb Z\) is finite and all coefficients are
holomorphic on a product neighborhood in \((h,u)\). A common denominator
may already have been cleared in the whole actual equation. The
ellipticity assumption below is on this displayed operator, not on an
unjustified factor of it.

Write \(I\) for the continued primitive from the original Borel origin,
with its specified paths and histories. On the initial common germ,
and consequently on its joint continuations, [B] gives
\[
 c_s=\exp(sI\partial_u)b,\qquad
 \sum_i p_i(I,u)c_i=0.                             \tag{3}
\]
Both expressions use the actual left coefficient ordering. Negative
integer shifts are included. The parameter \(s\) is complex; on every
compact joint continuation strip these expressions and all histories
used below converge normally for \(s\) in compact sets.

Fix \(u_0,\xi_0,p_0\in\mathbb C\), and tilt the local coordinates by
\[
 \rho=\xi-\xi_0+p_0(u-u_0).
 \tag{4}
\]
Thus \(\partial_u\) at fixed original \(\xi\) becomes
\(\partial_u+p_0\partial_\rho\). Assume
\[
                         P(u_0,e^{p_0})\ne0.        \tag{5}
\]

Here are the precise domain hypotheses. There is a meridian disk \(U\)
about \(u_0\), a disk \(D=\{|\rho|<r\}\), and a simply connected open
set \(V\subset D\) on which the selected continuation of \(b\) is
holomorphic on \(U\times V\). The set \(V\) may be a one-sided wedge
with \(0\in\partial V\), or an interior product slab. Choose a base
\(\rho_b\in V\). Every point of \(V\) can be joined to \(\rho_b\)
inside \(V\) by a path of length at most \(C_Vr\), for one fixed
\(C_V<\infty\). These paths specify the same primitive because \(V\)
is simply connected. There is also a compact joint continuation strip
from the initial canonical germ to a neighborhood of
\(U\times\{\rho_b\}\), supplying the histories in (3). After shrinking
\(U\), the strip has a common positive meridian buffer and finite path
length. All its histories are holomorphic in \(u\).

**Extension theorem.** Fix nested meridian disks with closures in \(U\).
There is \(r_*>0\), depending on these buffers, the displayed operator,
and \(C_V\), such that if \(0<r<r_*\), the selected actual source on a
smaller meridian disk times \(V\) extends holomorphically to that disk
times all of \(D\).

There is no growth assumption on \(b\) as \(\rho\) approaches zero
inside \(V\). Uniform buffers in the meridian direction and short
local primitive paths are essential to the assertion. It is an actual
extension theorem on that domain, not merely a formal inverse statement.

## 2. The analytic symbol and its formal inverse

Let \(Jf(u,\rho)=\int_{\rho_b}^{\rho}f(u,t)\,dt\). Initially work with
an independent formal variable \(h\). The local tilted operator is
\[
 \mathcal A_J=\sum_i e^{ip_0}p_i(J,u)\exp(iJ\partial_u).
 \tag{6}
\]
In this formula \(i\) is the integer shift index, not the imaginary
unit. For avoidance of ambiguity, \(e^{ip_0}\) means the exponential
of that integer times \(p_0\).

Use a second symbol variable \(\theta\), representing \(h\partial_u\),
and set
\[
 a(h,u,\theta)=\sum_i p_i(h,u)e^{ip_0+i\theta}
              =\sum_{a\ge0}h^a a_a(u,\theta).
 \tag{7}
\]
By (5), smaller disks in \(u,\theta\), with \(\theta\) centered at zero,
have \(a_0\) bounded away from zero. On their closures, for constants
\(M,H>0\), \(J_0=\max(1,\max_{i\in\mathcal I}|i|)\),
\[
 |\partial_\theta^r a_a(u,\theta)|
                      \le M H^{-a}J_0^r.           \tag{8}
\]
This is the finite-shift advantage: differentiating in \(\theta\)
costs a fixed integer power, rather than an additional factorial.

The left symbol product is
\[
 a\mathbin\# b
   =\sum_{r\ge0}\frac{h^r}{r!}
                      (\partial_\theta^r a)(\partial_u^r b).
 \tag{9}
\]
Indeed \(h^m\theta^k\) represents \(h^{m+k}\partial_u^k\), and the
ordinary Leibniz formula gives (9). The integer \(m\) is the deficiency
between total \(h\)-degree and differential order.

In Sections 2--4, \(b_m,b_{n,k}\) denote inverse-symbol coefficients,
distinct from the canonical source \(b(u,\xi)\). Construct the inverse
symbol \(b=\sum_{m\ge0}h^m b_m(u,\theta)\) with
\[
 \begin{split}
 b_0&=a_0^{-1},\\
 b_m&=-a_0^{-1}
  \sum_{\substack{a+q+r=m\\a+r>0}}
       \frac{(\partial_\theta^r a_a)(\partial_u^r b_q)}{r!}.
 \end{split}                                                   \tag{10}
\]
Every coefficient is holomorphic on the same open disks. We next
prove its quantitative bound; mere existence of (10) is insufficient.

## 3. A deficiency-sensitive Nagumo estimate

Translate \(u_0\) to zero for this paragraph and take a coefficient
disk \(|u|<R\), with \(R\le1\). Let \(d(u)=R-|u|\) and, uniformly on
a fixed closed \(\theta\)-disk, put
\[
 \|f\|_m=\sup |f(u,\theta)|d(u)^m.
 \tag{11}
\]
The elementary Cauchy estimate gives
\[
 \|\partial_u^r f\|_{m+r}
                \le e^r\frac{(m+r)!}{m!}\|f\|_m.
 \tag{12}
\]
For one derivative and \(m\ge1\), use the circle of radius
\(d(u)/(m+1)\); its remaining boundary distance is at least
\(d(u)m/(m+1)\), and \((1+1/m)^m\le e\). For \(m=0\), the circle
of radius \(d(u)/2\) gives \(2\le e\). Iteration proves (12).

Let \(M_0\ge\|a_0^{-1}\|_0\), and define
\(\beta_m=\|b_m\|_m/m!\). Multiplication by a bounded coefficient
does not increase its Nagumo index, and promotion of index \(q+r\)
to \(m=q+r+a\) costs at most \(R^a\). Equations (8), (10), and (12)
therefore imply
\[
 \beta_m\le M_0M
  \sum_{\substack{a+r>0\\a+r\le m}}
       (R/H)^a\frac{(eJ_0)^r}{r!}\,\beta_{m-a-r}.
 \tag{13}
\]
The discarded factorial ratio is exactly \((q+r)!/m!\le1\).
There is no estimate replacing it by an extra \(m!\).

Choose \(C>R/H\) so large that
\[
 M_0M\left\{\frac{\exp(eJ_0/C)}{1-R/(HC)}-1\right\}<1.
 \tag{14}
\]
Induction in (13), with \(\beta_0\le M_0\), proves
\[
                          \|b_m\|_m\le M_0 C^m m!.
 \tag{15}
\]
On any smaller meridian disk whose distance from the coefficient
boundary is at least \(d_0>0\), (15) becomes
\(|b_m|\le M_0(C/d_0)^m m!\). Expand in \(\theta\):
\[
 b_m(u,\theta)=\sum_{k\ge0}b_{m+k,k}(u)\theta^k.
\]
Cauchy's estimate on a fixed positive \(\theta\)-radius now gives,
with one finite \(D_0\ge1\),
\[
 \boxed{\quad |b_{n,k}(u)|\le M_0D_0^n(n-k)!,
                     \qquad 0\le k\le n.\quad}    \tag{16}
\]
This is the required refined bound. A bound \(D_0^n n!\) independent
of \(k\) would not suffice for the next step.

## 4. Convergence and the two-sided analytic inverse

Define the actual local operator
\[
 \mathcal B_J f
      =\sum_{n\ge0}\sum_{k=0}^n
                    b_{n,k}(u)J^n\partial_u^k f.
 \tag{17}
\]
Suppose the input is bounded by \(M_f\) on a meridian disk with buffer
\(d_1>0\) beyond the output disk and on the primitive paths in use.
If every such path has length at most \(L\), then
\[
 |J^n\partial_u^k f|
                 \le M_f\frac{k!}{d_1^k}\frac{L^n}{n!}.
 \tag{18}
\]
The repeated-primitive formula used here is
\(J^nf=(n-1)!^{-1}\int(\rho-t)^{n-1}f(t)\,dt\); the corresponding
length estimate is valid for any of the specified finite paths.
Combining (16)--(18) and
\((n-k)!k!/n!=\binom nk^{-1}\le1\) gives the normally convergent bound
\[
 |\mathcal B_J f|
 \le M_fM_0\sum_{n\ge0}(n+1)
          [D_0L\max(1,d_1^{-1})]^n.               \tag{19}
\]
In particular the bracket can be required to be less than \(1/2\).
The same estimates prove joint holomorphy of (17).

The operator (6) also converges normally on buffered disks. For
example its terms of degrees \(a,k\), acting on \(f\), are bounded
by a constant times
\[
 M_f H^{-a}|i|^k d_1^{-k}
                       \frac{L^{a+k}}{(a+k)!}.
 \tag{20}
\]
The factorial \(k!\) from the Cauchy derivative has canceled the
shift exponential's \(1/k!\). This double sum converges normally.

Choose four nested meridian disks before choosing \(r_*\). Apply
(19)--(20) successively across their positive buffers, taking
\(L\le\max(C_V,2)r\). For sufficiently small \(r\), both compositions
\(\mathcal A_J\mathcal B_J\) and
\(\mathcal B_J\mathcal A_J\) converge normally on the innermost disk.
These compositions may be collected by total primitive degree.
To justify collection directly, estimate each inner series absolutely
on the next larger disk and then use Cauchy for the outer derivatives;
the same bounds (19)--(20) give an absolutely summable double series.
The facts that \(J\) commutes with \(u\)-derivatives and multipliers
and that \(J^nJ^m=J^{n+m}\) then give exactly (9).

Equation (10) proves \(\mathcal A_J\mathcal B_J=1\). The inverse is
two-sided: in the formal algebra filtered by total primitive degree,
the constant coefficient \(a_0(u,0)\) is an invertible multiplier,
so a left inverse also exists by the elementary degree recursion.
Associativity identifies it with the right inverse just constructed.
Normal convergence consequently gives
\[
             \mathcal A_J\mathcal B_J f=f,
             \mathcal B_J\mathcal A_J f=f.          \tag{21}
\]
These are identities of analytic functions, with the stated buffers.

For a function holomorphic on \(U\times V\) which is not uniformly
bounded toward \(\partial V\), apply this argument on each compact
family of the prescribed paths and on closed smaller meridian disks.
Its bound \(M_f\) is finite there. The convergence threshold in (19)
does not depend on \(M_f\). Thus (21) holds throughout the smaller
product with \(V\), without a boundary growth hypothesis.

## 5. The exact tilted histories are holomorphic error terms

It remains to relate (6) to the original equation (3); simply replacing
the original primitive by \(J\) would be incorrect.

All quantities at the local base below are evaluated on the retained
joint continuation strip. They are holomorphic in \(u\), with a
positive buffer. Their finite-\(s\) bounds follow directly from Cauchy
and the primitive factorial. If the strip length is \(L_0\) and its
meridian buffer is \(d_2\), for example,
\[
 \left|\frac{s^k}{k!}I^k\partial_u^k b\right|
               \le M_b\frac{(|s|L_0/d_2)^k}{k!}.
 \tag{22}
\]
This also constructs \(c_s\) jointly for every compact \(s\)-set on
that strip. Short overlapping continuation strips give the same
functions by analytic uniqueness.

In the tilted coordinates, differentiate with respect to \(\rho\).
The difference
\(I\partial_{u,\mathrm{old}}c_s-(p_0+J\partial_u)c_s\)
has derivative zero. Therefore the exact evolution is
\[
 \partial_s c_s=(p_0+J\partial_u)c_s+q_s(u),\qquad
 q_s(u)=
  (I\partial_{u,\mathrm{old}}c_s)(u,\rho_b)
                          -p_0c_s(u,\rho_b).       \tag{23}
\]
The forcing is independent of \(\rho\); it is not discarded.
Variation of constants gives, for each integer shift \(i\),
\[
 c_i=e^{ip_0}\exp(iJ\partial_u)b+H_i,
\quad
 H_i=\int_0^i e^{(i-s)p_0}
              \exp((i-s)J\partial_u)q_s\,ds.       \tag{24}
\]
The integral can use the straight complex \(s\)-segment, including
negative \(i\). Since \(q_s\) is independent of \(\rho\), its local
semigroup series converges normally on all of the small disk \(D\),
using a meridian buffer and the two factorials as in (22).
Consequently \(H_i\) is holomorphic through \(\rho=0\).
Equation (24) also constructs the continued \(c_s\) on the product
wedge from its base histories. It agrees with its original definition
on their overlap and hence throughout the chosen continuation.

For every \(a\ge1\), the exact primitive-history identity is
\[
 I^a c_i-J^a c_i
   =\sum_{l=0}^{a-1}\frac{(\rho-\rho_b)^l}{l!}
                         (I^{a-l}c_i)(u,\rho_b).
 \tag{25}
\]
It follows either by repeated integration or by matching the \(a\)th
derivative and the first \(a\) initial data. These polynomials retain
all earlier paths, including any earlier loops.

The correction in replacing \(p_i(I,u)c_i\) by \(p_i(J,u)c_i\) is
holomorphic on the full local disk, and its series is normal there.
Indeed the analytic coefficient bound \(|p_{i,a}|\le M H^{-a}\)
and the history bound
\[
 |(I^j c_i)(u,\rho_b)|\le M_iL_0^j/j!
\]
bound its absolute sum by a constant times
\[
 \sum_{j\ge1,\ l\ge0}
       H^{-(j+l)}\frac{L_0^j(2r)^l}{j!l!}<\infty.
 \tag{26}
\]
Here \(M_i,L_0\) may be enlarged for the fixed finite set of shifts.
There is no assertion that they remain bounded on an unconstructed
global continuation.

Combining (24)--(26) with the actual equation (3) proves the exact
local identity
\[
                         \mathcal A_J b=F,
 \tag{27}
\]
where \(F\) is holomorphic on a buffered meridian disk times all of
\(D\). Its sign is the negative of the sum of the retained corrections
when (3) is written with zero right side. The value of \(F\) is fixed
by the original source histories; it is not freely prescribed.

Apply (21) on the wedge. It gives \(b=\mathcal B_JF\) there. The right
side is holomorphic through the full local disk by (19), proving the
extension theorem. This also proves that primitive-history terms,
although essential for the actual value of the extension, cannot
create a local obstruction at an elliptic tilted covector.

## 6. Holomorphic graph coordinates and retained companions

The same extension theorem holds for a nonlinear holomorphic tilt
\[
 \rho=\xi-\xi_0+\psi(u),\qquad \psi(u_0)=0,\qquad
                  P(u_0,e^{\psi'(u_0)})\ne0,        \tag{28}
\]
provided the same product-domain and joint-history hypotheses hold
in these coordinates. This adds no assumed coordinate invariance.
Here is the explicit adapter.

The local generator in (23) is now \(\psi'(u)+J\partial_u\).
For bounded complex \(s\), the function
\[
 g_s(h,u)=\exp\!\left(\frac{\psi(u+sh)-\psi(u)}{h}\right),
 \qquad g_s(0,u)=e^{s\psi'(u)},                     \tag{29}
\]
is holomorphic also at \(h=0\) on fixed buffered disks. The identity
\[
 \exp\bigl(s(\psi'+h\partial_u)\bigr)
                    =g_s(h,u)\exp(sh\partial_u)    \tag{30}
\]
follows by differentiating in \(s\) and checking its initial value.
Equivalently it is the conjugation
\(e^{-\psi/h}e^{sh\partial_u}e^{\psi/h}\).
The right side with \(h=J\) converges normally by (20), since the
Taylor coefficients of \(g_s\) have a uniform geometric bound.
It defines the local analytic flow on smaller disks and obeys the
same evolution and semigroup identities.

Replace the coefficients in (7) by
\[
                   p_i^\psi(h,u)=p_i(h,u)g_i(h,u).  \tag{31}
\]
Use these coefficients in (6)--(7) with the external constant tilt
set to zero: the new local operator is
\(\sum_i p_i^\psi(J,u)\exp(iJ\partial_u)\). The tilt is already
included in \(g_i\), so it is not counted twice.
These are still analytic finite-shift coefficients. Their deficiency-zero
symbol is \(\sum_i p_i(0,u)e^{i\psi'(u)+i\theta}\), and its
\(\theta\)-derivatives still cost only a fixed integer power.
Thus (8)--(21) apply after changing constants.

Differentiating with respect to \(\rho\) gives the exact history formula
\[
 I\partial_{u,\mathrm{old}}c_s
   =(\psi'+J\partial_u)c_s+q_s(u),\qquad
 q_s=(I\partial_{u,\mathrm{old}}c_s)(\rho_b)
                                      -\psi'c_s(\rho_b).
 \tag{32}
\]
Use (30) in the Duhamel formula (24). Its forcing is independent of
\(\rho\), so its correction is holomorphic on the full small disk.
The primitive identity (25) is unchanged. The original equation
again has the form (27), with the coefficient replacement (31), and
the convergent inverse proves extension.

Moreover all the companions extend with \(b\), rather than merely
their sum in (27). For each bounded set of \(s\), (24), or its version
using (30), extends \(c_s\) holomorphically and normally on smaller
disks. Equation (25) then extends every continued primitive from its
original base values. For each fixed \(H>0\) the sums of these
histories with coefficients bounded by \(H^{-a}\) converge normally
by (26) and the corresponding local primitive factorial bound.
Their \(u\)-derivatives extend on smaller disks as well. They agree
with the old companions on the overlap, so the original equation,
all base histories, and the selected branches persist on the new
patch. This statement is local; no uniform global history norm is
asserted.

## 7. Extension through a smooth noncharacteristic boundary

A supplied fixed product wedge is not necessary at a twice
continuously differentiable boundary. The following consequence
states precisely the extra domain information used.

Suppose the actual source and its continued companions from Section 6
are jointly holomorphic on one side of a real \(C^2\) boundary near
\((u_0,\xi_0)\), with one fixed continuation branch there. The complex
normal has nonzero \(\xi\)-component. In suitable local normalization
write its defining function as
\[
 \operatorname{Re}\bigl(c_\xi[
       \xi-\xi_0+p_0(u-u_0)]\bigr)
       +O(|u-u_0|^2+|\xi-\xi_0|^2)>0,\qquad c_\xi\ne0,
 \tag{33}
\]
on the known side, and suppose \(P(u_0,e^{p_0})\ne0\).
The continuation companions here include \(c_s\) for \(s\) on
bounded sets and their primitive histories, with the local normal
convergence just described. They need not have bounded norms at
the boundary.

Then \(b\), these companions, and the original equation extend to a
neighborhood of the boundary point. To prove this, use the constant
tilt (4) and rotate only the description of the \(\rho\)-disks so
that the inward normal points along \(c_\xi^{-1}\mathbb R_+\).
For every sufficiently small positive \(\varepsilon\), the known
side contains a product slab centered at
\(\rho_b=\varepsilon/c_\xi\), with meridian radius
\[
              d_\varepsilon=c_0\sqrt{\varepsilon}
 \tag{34}
\]
and \(\rho\)-radius \(c_1\varepsilon\). The fixed positive constants
\(c_0,c_1\) can be chosen small: the quadratic error in (33) is
bounded by a constant times
\(d_\varepsilon^2+\varepsilon^2\), while the real linear term is
bounded below by a positive constant times \(\varepsilon\).
Use several nested meridian disks of radii fixed fractions of
\(d_\varepsilon\).

The coefficients of the inverse are estimated on one fixed
coefficient neighborhood of \(u_0\). Hence the constants \(M_0,D_0\)
in (16) are independent of \(\varepsilon\). Only the Cauchy buffer
for the input and for its known base histories shrinks like
\(d_\varepsilon\). Apply the local construction to a \(\rho\)-disk
centered at zero of radius \(C_2\varepsilon\), containing the base
and a neighborhood of zero. Its primitive paths have length
\(O(\varepsilon)\). The bracket in (19) is therefore
\[
             O(\varepsilon/d_\varepsilon)
                         =O(\sqrt{\varepsilon}),   \tag{35}
\]
which is less than \(1/2\) for sufficiently small \(\varepsilon\).
In particular there is no second inverse power of
\(d_\varepsilon\) from re-estimating the operator coefficients on a
shrinking coefficient disk.

All base values in (23)--(26) are holomorphic on the meridian slab
by the stated known-side companion hypothesis. Their norms may
grow as \(\varepsilon\) decreases, but do not enter (35). The exact
history correction \(F\) consequently extends over the target
\(\rho\)-disk. The inverse extends \(b\) from the interior slab to
the target disk, including \(\rho=0\); Section 6 extends its
companions there as well. Fixing any one sufficiently small
\(\varepsilon\) gives an open neighborhood of the boundary point
and proves the assertion.

This argument makes no claim at a boundary with vanishing
\(\xi\)-normal component, a characteristic normal, or without the
specified one-sided joint branch and its continued histories. It
does not by itself provide a global exhaustion by such boundaries.

## 8. Scope and proof source

The symbol tested by this theorem is precisely
\(P(u,e^{p_0})\), the finite-shift symbol in the tilted direction.
No modulus ordering among its roots, conormal expansion of the input,
Laplace inversion, or estimate of a selected scalar period is used.
The theorem allows arbitrary finite earlier paths whose joint
histories satisfy the stated continuation-strip hypothesis.

A product slab with sufficient meridian buffer is the quantitative
input to the inverse. Section 7 constructs it at a supplied \(C^2\)
noncharacteristic boundary, retaining the known-side histories. This
result alone does not show that all remaining singularities form the
predicted characteristic graph. A suitable global boundary
construction and its branch control remain separate questions. It also
does not remove a cofactor which is characteristic at the selected
partner branch in an inserted moment system.

The analytic inverse construction is elementary here, rather than an
imported analytic-microfunction or resurgence theorem. No novelty is
claimed for the general principle of noncharacteristic extension.
The point is the refined convergent inverse and exact history adapter
for the same canonical source and finite-shift equation.

| Label | Complete proof direct | SHA256 |
|---|---|---|
| B | notes/research_canonical_borel_finite_laplace_current.md | b3b1e4246e2b5ed1b364585b8504edf8e0f1f1e15797f62f276fc4b89dca586f |

B supplies the original canonical Borel source, finite-shift equation,
ordering, continued primitives and their source normalization. All
inverse estimates, local histories and extension steps used here are
proved above. Only written mathematics and source-text reads were
used. No mathematical programs, tests or builds were run. Frozen
notes and public manuscripts are unchanged.
