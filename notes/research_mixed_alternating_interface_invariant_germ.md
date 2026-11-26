# An invariant phase germ for the original paired interface

Research deduction, 7 November 2026. The stable quadratic datum at the
original alternating interface extends to a holomorphic stationary
phase germ and a nonzero invariant leading amplitude. The proof is
an explicit analytic contraction. It concerns the local current
of the original paired kernel, not its entire input period, an
original finite-band eigenvector, or an ordinary-cap entrance.
No numerical evaluation is used.

## 1. The actual generating function and the twist

Use \(x_0,\Psi,q_3,q_4,a,b,c,p_*\) from
[the paired-interface theorem](research_mixed_alternating_interface_boundary_data.md).
Center coordinates at \(x_0\), writing
\(\psi(x,y)=\Psi(x_0+x,x_0+y)\). Its original two-jet is
\[
 \psi(0,0)=\psi_0,\qquad
 (\psi_x,\psi_y)(0,0)=(q_3,q_4),\qquad q_4=-q_3,
 \qquad
 -\psi''(0,0)=\begin{pmatrix}a&b\\b&c\end{pmatrix}.
 \tag{1}
\]
The unique accretive width obeys
\[
 p_*=c-\frac{b^2}{a+p_*},\qquad
 A=a+p_*,\qquad \lambda=-\frac bA,\qquad |\lambda|<1.
 \tag{2}
\]
Neither \(\psi_0\) nor the two momenta have been redefined.

For this actual interface \(b\ne0\). Here is an exact source check,
rather than a numerical genericity assumption. Equation (22) of
[the original interface calculation](research_three_four_source_interface.md)
expresses each reduced vertex's off-diagonal negative Hessian as
\[
 b_n=\frac{e_n^2}{f_n},\qquad
 e_n=-\frac{\sin\tau_n}
 {2\cos(\pi x_0-\tau_n/2)\cos(\pi x_0+\tau_n/2)},\qquad f_n\ne0.
 \tag{3}
\]
The original strip conditions keep both cosine factors nonzero.
The validated \(\tau_3,\tau_4\) have strictly negative imaginary
parts, so neither sine vanishes. Thus \(b_3b_4\ne0\), and the
paired Schur formula \(b=-b_3b_4/(d_3+d_4)\) proves the claim.

The generating relation
\[
 u=-\psi_x(x,y),\qquad v=\psi_y(x,y)
 \tag{4}
\]
therefore defines a local holomorphic canonical map from \((x,u)\)
to \((y,v)\), near the fixed point \((0,-q_3)\).
Indeed the implicit equation has derivative \(-\psi_{xy}=b\ne0\),
and \(d\psi=-u\,dx+v\,dy\) proves preservation of the symplectic
form. This interpretation will not replace the direct proof below.

## 2. A contraction on analytic nonlinear remainders

**Theorem 1.** On a sufficiently small complex disk there is a
unique holomorphic phase germ \(s\), normalized by \(s(0)=0\),
with
\[
 s'(0)=-q_3,\qquad s''(0)=-p_*,
 \tag{5}
\]
such that its critical input \(\chi(y)\) is holomorphic and
\[
 \chi(0)=0,\qquad \chi'(0)=\lambda,\qquad
 s(\chi(y))+\psi(\chi(y),y)=s(y)+\psi_0,
 \qquad s'(\chi(y))+\psi_x(\chi(y),y)=0.
 \tag{6}
\]
After shrinking the disk, \(|\chi(y)|\le r|y|\) for some fixed
\(r<1\), and \(-\Re s''>0\).

*Proof.* Write the exact holomorphic expansion
\[
 \psi_x(x,y)=q_3-a x-b y+R_x(x,y),\qquad
 R_x(x,y)=O((|x|+|y|)^2).
 \tag{7}
\]
For a prospective phase put
\[
 s_h'(z)=-q_3-p_*z+h(z),\qquad h(0)=h'(0)=0.
\]
On the open disk of radius \(R\), take the Banach norm
\[
 \|h\|_2=\sup_{0<|z|<R}\frac{|h(z)|}{|z|^2}.
 \tag{8}
\]
Equivalently \(h(z)=z^2k(z)\) with \(k\) bounded and
holomorphic on the disk. Fix \(|\lambda|<r<1\) and then
\(|\lambda|r^2<\Lambda<1\). First consider any finite ball
\(\|h\|_2\le M\); its radius \(M\) will be fixed below
before the final choice of \(R\).

The stationary equation is exactly
\[
 x=\lambda y+\frac{h(x)+R_x(x,y)}A.
 \tag{9}
\]
Uniformly over this ball, it has a unique solution
\(|x|\le r|y|\), \(|y|<R\), once \(R\) is small enough.
For completeness, on \(|x|\le r|y|\) the correction to
\(\lambda y\) is at most
\[
 \frac{Mr^2+C(r+1)^2}{|A|}|y|^2,
\]
where \(C\) is a fixed local bound from (7). This is less than
\((r-|\lambda|)|y|\) for small \(R\). Also Cauchy's estimate
on \(|x|\le rR\) gives \(|h'(x)|\le C_rMR\), while
\(|\partial_xR_x(x,y)|=O(R)\). The right side of (9)
is therefore a contraction in \(x\), with a common constant
less than one. Its iterates, or the implicit function theorem,
give a holomorphic solution \(\chi_h(y)\) with
\(\chi_h(0)=0,\chi_h'(0)=\lambda\). All evaluations of
\(h\) stay strictly inside its domain.

Define the output remainder by
\[
 (\mathcal Gh)(y)=\psi_y(\chi_h(y),y)-q_4+p_*y.
 \tag{10}
\]
It has zero value and first derivative at zero: for the derivative,
\(-b\lambda-c+p_*=0\) is precisely (2). It therefore belongs
to the same remainder space.

Here is the quantitative contraction estimate. For \(h_1,h_2\)
in the ball, interpolate \(h_\theta=(1-\theta)h_2+\theta h_1\),
\(0\le\theta\le1\). Implicit differentiation of (9) gives
\[
 \partial_\theta\chi_{h_\theta}(y)=
 \frac{(h_1-h_2)(\chi_{h_\theta}(y))}
 {A-h_\theta'(\chi_{h_\theta}(y))
       -\partial_xR_x(\chi_{h_\theta}(y),y)}.
 \tag{11}
\]
Multiplication by \(\psi_{yx}\) gives the derivative of (10).
Its coefficient converges uniformly to \(-b/A=\lambda\)
as \(R\downarrow0\). Choose \(\varepsilon>0\) with
\((|\lambda|+\varepsilon)r^2\le\Lambda\). A sufficiently
small \(R\), depending on \(M\), then gives
\[
 \|\mathcal Gh_1-\mathcal Gh_2\|_2
 \le (|\lambda|+\varepsilon)r^2\|h_1-h_2\|_2
 \le\Lambda\|h_1-h_2\|_2.
 \tag{12}
\]
The factor \(r^2\) retains evaluation at the contracting input;
replacing it by an uncontrolled derivative norm is unnecessary.

For \(h=0\), the solution and output are analytic on a fixed
neighborhood before \(R\) is chosen. Since their two lower
jets vanish, \(\|\mathcal G0\|_2\le C_0\) for all small \(R\),
with a fixed \(C_0\). Choose
\(M>C_0/(1-\Lambda)\), and then shrink \(R\) to obtain all
preceding uniform bounds for this \(M\).
Equations (12) and this choice show that \(\mathcal G\)
maps its closed ball into itself and contracts. Its fixed point
\(h_*\) is therefore unique in that ball.

Integrate \(s'(z)=-q_3-p_*z+h_*(z)\), with \(s(0)=0\).
Equation (10) says that the derivative of the stationary output
equals \(s'(y)\). At zero the output value is \(\psi_0\);
hence the first identity in (6) follows. Accretivity of \(p_*\)
gives \(-\Re s''>0\) on a smaller disk.

Finally any two analytic germs satisfying (5)--(6) have finite
norms (8) on a common smaller disk. Choose \(M\) to include
both and shrink again; the same contraction proves equality.
This is uniqueness of the germ, not merely of a preselected ball.
\(\square\)

The contraction proof itself does not require \(b\ne0\):
\(\lambda=0\) is allowed. Nonzero twist is used only for
the following canonical-map interpretation. The exact Lagrangian
graph \(u=s'(x)\) is invariant under (4).
Its forward coordinate map expands with derivative
\(\lambda^{-1}\), while its inverse on the graph is
\(y\mapsto\chi(y)\), with derivative \(\lambda\).
Thus it is the unstable graph for the forward canonical map and
the stable graph for the inverse. The critical-input direction
in the attachment is the contracting one.

## 3. A nonzero invariant leading amplitude

The original paired local packet has amplitude \(a_{34}\) from
equation (7) of the paired-interface theorem. In centered coordinates
put
\[
 m(y)=
 \frac{\sqrt{2\pi}\,a_{34}(x_0+\chi(y),x_0+y)}
 {\sqrt{-s''(\chi(y))-\psi_{xx}(\chi(y),y)}},
 \qquad m_0=m(0)\ne0.
 \tag{13}
\]
All roots are the continued accretive roots from the original
local Gaussian currents. This function is holomorphic and nonzero
on a smaller disk.

**Corollary 2.** There is a unique normalized nonzero holomorphic
germ \(f\), \(f(0)=1\), with
\[
                 m(y)f(\chi(y))=m_0f(y).
 \tag{14}
\]
It is given by the convergent expression
\[
 f(y)=\exp\left(\sum_{j=0}^{\infty}
                  \log\frac{m(\chi^{\circ j}(y))}{m_0}\right).
 \tag{15}
\]

*Proof.* Choose the logarithm equal to zero at the center. Its
value at \(y\) is \(O(|y|)\). Since
\(|\chi^{\circ j}(y)|\le r^j|y|\), the series converges
normally on a fixed smaller disk, and its exponential never
vanishes. Splitting off the first term gives (14). If two
normalized solutions existed, their quotient would be invariant
under \(\chi\); iteration to zero makes that quotient one.
\(\square\)

For example, let \(G_N(x_0+x)=N^\nu f(x)e^{Ns(x)}\) on this
local disk. Attach the actual paired local kernel, integrating
the remaining input on a sufficiently short fixed segment through
zero. The same local contour argument as before gives
\[
 \mathcal L_N^{\mathrm{loc}}G_N(x_0+y)
 =\kappa^3m_0e^{N\psi_0}G_N(x_0+y)(1+O(N^{-1})).
 \tag{16}
\]
The factors \(N\), \(N^{-1/2}\) from the paired kernel and
\(N^{-1/2}\) from the final Gaussian preserve \(N^\nu\).
This constructed germ is not asserted to extend to an original
finite-band function or an eigenvector of the full finite matrix.

## 4. What is and is not closed

Equations (6) and (14) are an operation-preserving local phase and
leading-amplitude class at the actual mixed interface. They retain
the constant \(\psi_0=\Phi_3(x_0,x_0)+\Phi_4(x_0,x_0)\),
the original momenta, \(\kappa^3\), the original contour orientation,
and both parities. No phase is transported from the separate
homogeneous-three disk.

To turn this local construction into a whole-source induction
requires an actual ordinary-cap entrance with a nonzero coefficient
in this class, a bound for the full complementary input period,
and control of the propagated finite-source remainder and envelope
relative to the actual action. Equations (6), (12) and (16) do
not supply those estimates. In particular they do not justify
discarding the complement of either local wire integration.

The [coherent suffix identity](research_mixed_coherent_suffix_reversal.md)
and [exact Fourier bridge](research_mixed_conditional_fourier_message_bridge.md)
specify the full source and observation to be controlled. The
invariant germ does not identify their whole contraction with
the local current. No new whole-source, knot-family or cofinite
filling conclusion follows from this note alone.

