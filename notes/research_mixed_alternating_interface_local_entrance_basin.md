# An open local entrance basin at the alternating interface

Research deduction, 7 November 2026. The invariant phase germ has an
open basin of nearby bounded holomorphic phase gradients. The class
allows the critical input, momentum and width to move; it preserves
the exact stationary action increment. A corresponding class of
nonzero normalized leading amplitudes is also invariant. These are
local statements about the original paired current. They do not
establish that an actual cap enters this basin, or bound the
complementary input period or a propagated finite-source remainder.
No numerical evaluation is used.

## 1. Frozen local data and the open class

Use the original centered generating function \(\psi\), invariant
phase \(s\), width \(p_*\), and paired amplitude \(a_{34}\) from
[the invariant-germ theorem](research_mixed_alternating_interface_invariant_germ.md)
and [the paired-interface theorem](research_mixed_alternating_interface_boundary_data.md).
In particular,
\[
 s(0)=0,\quad s'(0)=-q_3,\quad s''(0)=-p_*,\quad
 A=a+p_*,\quad \lambda=-b/A,\quad |\lambda|<1,
 \qquad \Re A>0,
 \tag{1}
\]
and the unperturbed critical input satisfies
\[
 s'(\chi_0(y))+\psi_x(\chi_0(y),y)=0,\qquad
 s(\chi_0(y))+\psi(\chi_0(y),y)=s(y)+\psi_0,
 \quad \chi_0(0)=0.
 \tag{2}
\]
All functions retain their original lifts and normalizations.

Write \(D_R=\{z:|z|<R\}\). For a bounded holomorphic function
\(h\in H^\infty(D_R)\), set
\[
 S_h(z)=s(z)+\int_0^z h(w)\,dw.
 \tag{3}
\]
There is no condition on \(h(0)\) or \(h'(0)\).
Thus this class does not fix the original center jets. An arbitrary
additive phase constant can be carried separately from the
normalization \(S_h(0)=0\).

**Theorem 1.** There exist \(R,\delta>0\), \(|\lambda|<r<1\)
and \(|\lambda|<k<1\) such that the following assertions hold on
the closed ball \(\|h\|_\infty\le\delta R\).

The stationary equation
\[
 S_h'(x)+\psi_x(x,y)=0
 \tag{4}
\]
has a unique solution in \(D_{rR}\), denoted \(\chi_h(y)\),
for every \(y\in D_R\). It is holomorphic, and
\[
 \chi_h(D_R)\subset D_{rR},\qquad
 \sup_{D_R}|\chi_h'|\le k.
 \tag{5}
\]
Define the exact action increment and normalized output by
\[
 C(h)=S_h(\chi_h(0))+\psi(\chi_h(0),0),
 \qquad
 S_h^+(y)=S_h(\chi_h(y))+\psi(\chi_h(y),y)-C(h).
 \tag{6}
\]
Then \(S_h^+=S_{\mathcal Gh}\), where
\[
 (\mathcal Gh)(y)=\psi_y(\chi_h(y),y)-s'(y),\qquad
 \mathcal G0=0,\qquad
 \|\mathcal Gh_1-\mathcal Gh_2\|_\infty
 \le k\|h_1-h_2\|_\infty.
 \tag{7}
\]
Consequently both the open and closed balls are invariant, and
\(\|\mathcal G^n h\|_\infty\le k^n\|h\|_\infty\).

*Proof.* Put \(\eta(x)=s'(x)+q_3+p_*x=O(x^2)\) and use
the original expansion
\(\psi_x(x,y)=q_3-a x-b y+R_x(x,y)\), with
\(R_x=O((|x|+|y|)^2)\). Equation (4) is exactly
\[
 x=\lambda y+\frac{\eta(x)+R_x(x,y)+h(x)}A.
 \tag{8}
\]
Fix \(r\) and \(k\) strictly between \(|\lambda|\) and one.
First choose \(\delta\) small, and then choose \(R\) small.
Uniformly over the stated ball, the right side of (8) maps
\(|x|\le rR\) strictly inside that disk: its modulus is at most
\(|\lambda|R+O(R^2)/|A|+\delta R/|A|\).
Cauchy's estimate gives \(|h'(x)|\le C_r\delta\) there;
the other nonlinear derivatives are \(O(R)\).
The same right side is therefore a strict contraction in \(x\).
Its unique fixed point depends holomorphically on \(y\).

For later use set
\[
 F_h(x,y)=S_h'(x)+\psi_x(x,y).
 \tag{9}
\]
On the indicated product, \((F_h)_x\) is uniformly close
to \(-A\). It stays nonzero, and implicit differentiation gives
\[
 \chi_h'(y)=-\frac{\psi_{xy}(\chi_h(y),y)}
 {(F_h)_x(\chi_h(y),y)}.
 \tag{10}
\]
The right side is uniformly as close to \(\lambda\) as desired
by the preceding order of choices. This proves (5).

Interpolate \(h_\theta=(1-\theta)h_2+\theta h_1\).
Differentiating (4) and then (7) shows exactly that
\[
 \partial_\theta(\mathcal Gh_\theta)(y)
 =\chi_{h_\theta}'(y)
       (h_1-h_2)(\chi_{h_\theta}(y)).
 \tag{11}
\]
Equations (5) and (11) prove the contraction. Differentiating
the stationary value in (6) gives \(\psi_y\), and its normalized
value at zero is zero. Thus (6) is exactly \(S_{\mathcal Gh}\).
Equation (2) proves \(\mathcal G0=0\), so (7) also proves
invariance of the balls. \(\square\)

The distinction in (5) is essential: generally
\(\chi_h(0)\ne0\), so no bound
\(|\chi_h(y)|\le r|y|\) is asserted for the perturbed input.
Cauchy's estimates imply convergence of every fixed gradient jet
on smaller disks. On such disks, shrinking \(\delta,R\) also
retains \(-\Re S_h''>0\). No derivative bound on the boundary
of \(D_R\) is assumed for an arbitrary \(H^\infty\) input.

## 2. Exact action increments and moving centers

There is a uniform finite \(D\) such that
\[
 \|\chi_h-\chi_0\|_\infty\le D\|h\|_\infty,
 \qquad |\chi_h(0)|\le D\|h\|_\infty.
 \tag{12}
\]
Indeed apply the fundamental theorem of calculus to \(F_0\)
on the segment between the two roots. The averaged \(x\)
derivative differs from \(-A\) by at most a fixed
\(\varepsilon<|A|\), while
\(F_0(\chi_h,y)=-h(\chi_h)\). One may take
\(D=(|A|-\varepsilon)^{-1}\).

Stationarity also removes the first-order action drift. Along
the segment \(\theta h\), (6) gives
\[
 \frac{d}{d\theta}C(\theta h)
   =\int_0^{\chi_{\theta h}(0)}h(z)\,dz,
 \qquad C(0)=\psi_0,
 \qquad |C(h)-\psi_0|\le\frac D2\|h\|_\infty^2.
 \tag{13}
\]
For \(h_n=\mathcal G^n h_0\), the accumulated action is
exactly \(A_n=\sum_{j=0}^{n-1}C(h_j)\), and
\[
 \sum_{j=0}^{\infty}|C(h_j)-\psi_0|
 \le\frac{D\|h_0\|_\infty^2}{2(1-k^2)}.
 \tag{14}
\]
Thus the action correction converges, as do the center and jet
perturbations. The exact \(A_n\), not \(n\psi_0\), is the
action in the iterated local exponential. This is not an estimate
for a simultaneous limit in the number of attachments and \(N\).

## 3. A normalized nonzero leading-amplitude class

The continued original Gaussian root defines
\[
 m_h(y)=\frac{\sqrt{2\pi}\,
   a_{34}(x_0+\chi_h(y),x_0+y)}
 {\sqrt{-S_h''(\chi_h(y))-\psi_{xx}(\chi_h(y),y)}}.
 \tag{15}
\]
The quantity under the square root remains in a small neighborhood
of the accretive number \(A\). After the same domain restrictions, \(m_h\) is
holomorphic and nonzero, uniformly over the phase ball.
Furthermore
\[
 M_0:=\sup_{\|h\|_\infty\le\delta R}
       \|m_h'/m_h\|_\infty<\infty.
 \tag{16}
\]
To see this directly, every occurrence of \(h'\) and \(h''\)
in (15) and its derivative is evaluated in \(D_{rR}\).
Cauchy's estimates bound them uniformly for this fixed \(R\);
(5) bounds \(\chi_h'\), and all other functions extend to a
larger fixed product. The numerator and denominator are bounded
away from zero on that product after shrinking it.

Represent a normalized amplitude as \(f=e^\ell\), where
\(\ell(0)=0\) and \(\|\ell'\|_\infty\le M\).
For any \(M>M_0/(1-k)\), the exact leading-amplitude map is
\[
 \begin{split}
 \mu(h,\ell)&=m_h(0)e^{\ell(\chi_h(0))}\ne0,\\
 \ell^+(y)&=\log\frac{m_h(y)}{m_h(0)}
       +\ell(\chi_h(y))-\ell(\chi_h(0)).
 \end{split}
 \tag{17}
\]
The logarithm is the one vanishing at zero. Its existence follows
from nonvanishing on the disk. Equations (5) and (16) imply
\[
 \| (\ell^+)'\|_\infty\le M_0+kM<M.
 \tag{18}
\]
For the same phase \(h\), two amplitude logarithms contract in
the derivative norm by at most \(k\). These statements prove
an invariant class of normalized nonzero leading amplitudes with
the nonzero scalar \(\mu(h,\ell)\) retained separately.

They also give convergence along the phase iteration. Let
\(\ell_*\) be the logarithm of the invariant normalized amplitude
from the frozen theorem. Its equation and (16) imply
\(\|\ell_*'\|_\infty\le M_0/(1-k)\), on the chosen disk.
Cauchy's estimates on the strict interior disk and implicit
differentiation show that \(\chi_{h_n},\chi_{h_n}'\) and
\(m_{h_n}'/m_{h_n}\) converge uniformly to their values at
\(h=0\). Therefore, for \(d_n=\|\ell_n'-\ell_*'\|_\infty\),
\[
 d_{n+1}\le k d_n+\epsilon_n,\qquad \epsilon_n\longrightarrow0.
 \tag{19}
\]
Here the remaining comparison evaluates the fixed analytic
\(\ell_*'\) only inside \(D_{rR}\). Equation (19) and boundedness
give \(d_n\to0\). This is contraction in the amplitude fiber
and convergence in the coupled iteration, not a claim that the
unweighted product norm has contraction constant \(k\).

## 4. Scope for the original local current

At the stationary leading level a paired attachment sends
\(N^\nu f\,e^{N S_h}\) to
\[
 \kappa^3\mu(h,\ell)e^{N C(h)}
       N^\nu e^{\ell^+}e^{N S_{\mathcal Gh}}.
 \tag{20}
\]
The powers of \(N\), continued root, original phase lifts and
parities are those of the paired-interface theorem. Equation
(20) retains every action and amplitude scalar. It describes the
local stationary phase and leading coefficient; it does not
propagate a full finite-source asymptotic error by itself.

The basin is a genuine open analytic class, rather than only the
single invariant germ or its fixed two-jet. Membership of the
original cap or an exact Fourier message is still unproved.
The [exact Fourier bridge](research_mixed_conditional_fourier_message_bridge.md)
and [coherent suffix identity](research_mixed_coherent_suffix_reversal.md)
continue to determine the whole source, including its observation
and complementary input period. No bound for those discarded
parts, no full matrix eigenfunction, and no whole-source or
knot-family conclusion follows from this local basin alone.
