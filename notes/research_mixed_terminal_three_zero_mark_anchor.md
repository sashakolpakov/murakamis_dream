# The zero-mark anchor and its singular small-mark branch

Research deduction, 5 November 2026. The marked terminal source has a
well-defined original-log critical branch for small positive marking.
It emerges from the Newton boundary at fourth-root scale. Its exact
zero-mark source satisfies a forced second-order equation; the
homogeneous third-order equation has annihilated that forcing.
These facts identify an analytic starting point and its limitations.
They do not provide a nonzero whole-source asymptotic or a continuation
of a contributing cycle to marking one.

## 1. The finite anchor retains a forced sector

Use \(F_N(\omega;X,Y)\), \(K,W,Z\), \(r=q^{-2}\), and \(\rho_i\)
from [the marked difference system](research_mixed_terminal_three_marked_difference_system.md).
Its zero-mark value is independent of the ordinary color:
\[
 G_N(X):=F_N(\omega;X,0)
       =\sum_{i=0}^{N-1}\frac{\rho_i(X)}{P_i^2}
       =C_{1,N}(X,1).
\tag{1}
\]
This is a whole finite sum, not a single constant term in the
remaining index. The old conditional packets require a nonzero
second logarithmic argument in their admitted domains and do not
supply a packet at this seam. The
[boundary-strip theorem](research_mixed_boundary_strip_bounds.md)
provides upper estimates there, not its nonzero saddle coefficient.

The exact Gram transform, with constant input and exponent two,
gives
\[
 Q_NG_N=-\frac{\rho_N(X)}{N^2},\qquad
 Q_N=(K-1)^2-r^{-2}ZK^2+r^{-1}K,\qquad
 \rho_N=X^{-N}-1.
\tag{2}
\]
This is [Gram-shift equation (6)](research_mixed_terminal_gram_shift.md),
including its nonphysical boundary term.
At \(Y=0\), the marked operator in the \(t\)-direction satisfies
the exact ordered factorization
\[
 L_t\big|_{W=1}=r^3(K-1)Q_N .
\tag{3}
\]
Indeed \(KZ=r^{-1}ZK+(r-1)\) expands both sides to
\[
 r^3(K-1)^3-ZK^3+rZK^2+rK^2-r^2K .
\tag{4}
\]
Since \(K\rho_N=\rho_N\), equation (3) kills the right side
of (2). Dividing out \(K-1\), or silently replacing (2) by a
homogeneous equation, would lose the original source normalization.
No such inverse is used.

## 2. The regular critical point of the anchor phase

Let \(a\) lie in the vertical strip \(0<\Re a<1/2\), put
\(A=e^{-2\pi ia}\), and retain the original primitive \(g\).
At \(u=0\), the terminal reduced phase has the limit
\[
 \psi_0(a;t)=g(a+t)-g(a)-2g(t)+2\pi iat .
\tag{5}
\]
The original stationary equation is
\(\psi_{0,t}=g'(a+t)-2g'(t)+2\pi ia=0\).
With \(z=e^{-2\pi it}\), its regular exponential equation is
\[
                         z^2-z+1-A^{-1}=0 .
\tag{6}
\]
The extra factor \(1-z\) in the full zero-mark cubic is the
classical counterpart of (3), and is not a regular solution of (5).

**Lemma 1.** The anchor equation has exactly one original-log
stationary point with \(0<\Re t<1/2\). It is
\[
 z_0=\frac{1-\sqrt{4A^{-1}-3}}2,\qquad
 t_0=-\frac{\Log z_0}{2\pi i},
\tag{7}
\]
where the square root has positive real and imaginary parts and
\(-\pi<\arg z_0<0\).

*Proof.* Since \(A^{-1}=e^{2\pi ia}\) has positive imaginary
part, \(4A^{-1}-3\) lies in the upper half-plane. The root in
(7) lies strictly in the lower half-plane and the other quadratic
root lies in the upper half-plane. Thus exactly one root has the
required sine-strip logarithm. Neither \(z_0=0\) nor \(z_0=1\)
is possible: either would require \(A=1\).
Also \(0<\Re(a+t_0)<1\), so both original sine arguments are
regular.

The logarithmic residual has exponential one and is continuous
on the connected \(a\)-strip. Along real \(a\downarrow0\),
\(z_0=-2\pi ia+O(a^2)\), hence \(\Im t_0\to-\infty\).
Both \(g'(t_0)\) and \(g'(a+t_0)\) tend to zero, as does
\(2\pi ia\). The integral logarithmic residual is therefore
zero, proving the original equation rather than only (6).
Its derivative is
\[
 \psi_{0,tt}(a;t_0)
       =\frac{2\pi iz_0(2z_0-1)}{(1-z_0)^2}\ne0 .
\tag{8}
\]
The discriminant lies off zero and \(z_0\ne0,1\), proving
simplicity. \(\square\)

This identifies a critical point of the anchor phase. It does not
identify its coefficient in the entire finite sum (1).

## 3. A small positive marking is a fourth-root boundary problem

For real \(Y>0\), the marked complete-color phase is
\[
                \mathcal T_Y(a;t,u)
                        =\mathcal T(a;t,u)+u\log Y.
\tag{9}
\]
Its exponential equations are
\[
 (1-Az)(1-wz)=A(1-z)^3,\qquad
 (1-w)^4=Y(1+w)^2(1-wz),
 \quad w=e^{-2\pi iu}.
\tag{10}
\]
At a regular anchor (7), these equations have a fourth-root
collision at \(w=1\). Set \(\tau=Y^{1/4}>0\), and choose
\[
 v_0(a)^4=\frac{1-z_0(a)}{4\pi^4},\qquad
                      0<\arg v_0<\pi/4 .
\tag{11}
\]
The choice is holomorphic in the \(a\)-strip because \(1-z_0\)
lies in the upper half-plane.

**Theorem 2.** Uniformly for \(a\) in a compact subset of that strip,
there is a sufficiently small positive \(\tau_0\) and a branch of
the original zero-log equations for \(0<\tau<\tau_0\) with
\[
 t(a,\tau)=t_0(a)+O(\tau),\qquad
 u(a,\tau)=\tau v_0(a)+O(\tau^2).
\tag{12}
\]
The functions \(t(a,\tau)\) and \(u(a,\tau)/\tau\) extend
holomorphically to \(\tau=0\). The selected critical value obeys
\[
 \mathcal T_Y(a;t(a,\tau),u(a,\tau))
       =\psi_0(a;t_0(a))+4\tau v_0(a)+O(\tau^2).
\tag{13}
\]

*Proof.* Substitute \(u=\tau v\) in the original equations.
In the second equation the \(4\log\tau\) from \(\log Y\)
cancels the singularity in \(4\Log(2\sin\pi u)\).
The remaining holomorphic equation uses
\(\sin(\pi\tau v)/(\pi\tau v)\), which equals one at zero.
At \(\tau=0\) the equations become
\[
 \psi_{0,t}(a;t)=0,\qquad
       2\log2+g'(t)-4\Log(2\pi v)=0 .
\tag{14}
\]
The branch (11) has exactly the zero lift in the second equation.
The \((t,v)\) Jacobian is triangular with diagonal
\(\psi_{0,tt}(a;t_0)\) and \(-4/v_0\), both nonzero.
The holomorphic implicit-function theorem, compactness and
uniqueness on overlaps prove (12), uniformly on each compact
input family. For positive small \(\tau\), \(u\) lies in the
first quadrant and the actual original sine strips remain regular.

The local primitive expansion is
\[
 \mathcal T(a;t,u)=\psi_0(a;t)
 +u\{g'(t)+2\log2-4\Log(2\pi u)+4\}+O(u^2).
\tag{15}
\]
Adding \(u\log Y\), using the stationary equation, and using
\(\psi_{0,t}(t_0)=0\) proves (13).
\(\square\)

There are four algebraic fourth-root branches, but they are not
four zero-lift stationary points on the original Newton sheet.
The root \(v_0\) is its first-quadrant branch. The other branch
with positive real part has limiting argument
\(\arg v_0-\pi/2\); its original \(u\)-residual tends to
\(2\pi i\), and is exactly that nonzero integral lift for
small positive \(\tau\). The two remaining roots have negative
real part and leave the local original sine strip. Thus exponent
equations alone cannot assign their source currents.

## 4. The remaining source issue

The new small-mark branch is uniform on the actual compact input
disks, but has \(u\to0\). It therefore leaves every currently
proved compact central Newton contour as \(Y\downarrow0\).
This is a boundary-saddle degeneration, not an ordinary Gaussian
deformation through \(Y=0\).

Two distinct steps would be needed for a noncancellation route
based on this anchor. First, the actual finite source (1), with
its forcing (2), needs a nonzero asymptotic and a compatible
small-mark transition through the Newton boundary. Second, its
selected cycle must be transported to \(Y=1\) with all joining
currents and aliases retained. Neither the local implicit-function
argument nor finite-band kernel uniqueness supplies that transport.
The theorem does not assert that the small-\(Y\) branch reaches the
already identified geometric branch at \(Y=1\) without a critical
or Stokes transition.

No counterexample to such a continuation is claimed. The exact
forced anchor and the fourth-root scaling identify why the present
system cannot start from a presumed trivial or already controlled
source at \(Y=0\). The original one-index anchor problem and the
subsequent complete-cycle comparison are concrete additional
analytic obligations.
