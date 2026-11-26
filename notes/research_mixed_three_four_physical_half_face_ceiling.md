# Analytic reduction and a universal ceiling for the physical half face

Research deduction, 7 November 2026. The exact finite-source reduction
in [the physical middle-sector theorem](research_mixed_three_four_physical_middle_reduction.md)
leaves a sufficient half-face comparison. Here its transform maximum
is restricted analytically to \([1/10,1/3]\). For one allowed private
main height, all five private profiles have a common explicit ceiling.
That ceiling does not establish the comparison with the original
ordinary three/four action. No new source, root, or phase evaluation
is used.

## 1. Every private profile decreases above transform index one third

Retain exactly \(J,S,\Psi_1,\Phi,A(t;h_e),\overline Q\) and
\(M\) from the middle-sector theorem. In particular
\[
 E_c=[.27,.49]+i[-.055,.04],\qquad
 \mathcal E(1/2;h_e)=\overline Q(1/2)+
 \max_{1/10\le t\le1/2}
 \{A(t;h_e)-J(1/2-t)-2J(t)\}.                         \tag{1}
\]
The private main height is fixed in \((-.055,.04)\); both real
cuts and both horizontal aliases are retained in \(A\).

For incoming \(a=1/2\), real \(0<t<1/2\), and every \(e\in E_c\),
the original logarithmic derivative is
\[
 \exp\{\partial_t\Re\Phi(1/2;t,e)\}
 =\frac{2\cos\pi t\,|1-e^{-2\pi i(e+t)}|}
             {(2\sin\pi t)^3}.                       \tag{2}
\]
On \(1/3\le t<1/2\), the numerator's first factor is at most one,
and the denominator is at least \(3\sqrt3>24/5\).
Also
\[
 e^{.08\pi}<\frac75,\qquad
             |1-e^{-2\pi i(e+t)}|<\frac{12}{5}.        \tag{3}
\]
Indeed \(.08\pi<2/7\) follows from \(\pi<22/7\), and
\(e^u\le(1-u)^{-1}\) for \(0\le u<1\) proves (3).
Thus (2) is strictly less than \(1/2\).

Every private alias penalty is independent of \(t\). Integrating
this inequality pointwise before taking the appropriate private
maximum proves, for every allowed \(h_e\),
\[
 \boxed{\quad
 \mathcal E(1/2;h_e)=\overline Q(1/2)+
 \max_{1/10\le t\le1/3}
 \{A(t;h_e)-J(1/2-t)-2J(t)\}.
 \quad}                                                \tag{4}
\]
The primitive is continuous at \(t=1/2\), so that endpoint is
included in the comparison. No physical support has been enlarged
in an equality of finite sums: (4) is an identity of the already
defined upper envelopes.

## 2. At private main height zero, both weighted aliases lie below the real profile

Choose the allowed height \(h_e=0\). The original endpoint branch
on \(E_c\) obeys
\[
 S'(e)=-J'(e-u_c(e))+i\pi u_c(e),\qquad
 0<\Re u_c(e)<1/2,\quad 0<\Re(e-u_c(e))<1/2,           \tag{5}
\]
by [the complete endpoint rectangle](research_mixed_endpoint_cap_rectangle.md)
and [the original endpoint equations](research_mixed_open_word_critical_localization.md),
equation (2). The original logarithm of \(2\sin\pi z\) has
imaginary part in \((-\pi/2,\pi/2)\) on \(0<\Re z<1\).
It follows directly that
\[
                       -\pi/2<\Im S'(e)<\pi.           \tag{6}
\]
The argument estimate in
[the complex-private curvature proof](research_mixed_cap_early_taper_complex_profiles.md),
Lemma 1, gives \(|\arg\sin\pi e|<\pi/4\) on \(E_c\).
Since \(g'(e)=J'(e)+i\pi(1/2-e)\), this implies
\[
                       -\pi/4<\Im g'(e)<\pi/2.         \tag{7}
\]
For real \(t\in[1/10,1/3]\), the real part of \(e+t\) lies
strictly between zero and one. Therefore, retaining the exact chirp,
\[
 \Psi_{1,e}=S'(e)+J'(e+t)-i\pi t-g'(e),\qquad
 -\frac{11\pi}{6}<\Im\Psi_{1,e}<\frac{33\pi}{20}.      \tag{8}
\]
These are original-log estimates at every height in \(E_c\), not
estimates only at the physical real line.

For fixed \(u=\Re e\), put \(f(h)=\Re\Psi_1(u+ih,t)\).
Then \(f'(h)=-\Im\Psi_{1,e}\). Equation (8) gives
\[
\begin{split}
 f(H)-2\pi H&<f(0)-\frac\pi6H &&(0<H\le.04),\\
 f(-H)-2\pi H&<f(0)-\frac{7\pi}{20}H
                                      &&(0<H\le.055).
\end{split}                                             \tag{9}
\]
Thus both complete horizontal aliases are below their corresponding
real profiles. The main segment at height zero contains both real
cuts. All five profiles consequently satisfy the exact maximum identity
\[
 A(t;0)=\max_{.27\le e\le.49}
       \{\lambda(e)+J(e+t)-J(t)-J(e)\},
       \qquad 1/10\le t\le1/3,\quad \lambda=\Re S.       \tag{10}
\]
The vertical sides and joins are still controlled by the five-profile
source theorem; (10) does not remove any finite current separately.

## 3. One explicit universal ceiling

The original coherent seam theorem gives
\(\lambda(e)<433/500\) for \(0<e<1/2\). This is the
concave tangent bound (6)--(7) of
[the cap seam source proof](research_mixed_cap_seam_source_bounds.md),
using its already established scalar constants. Also
\[
 \max_{0\le e\le1-t}\{J(e+t)-J(e)\}
       =L(t):=-2J((1-t)/2).                             \tag{11}
\]
Indeed the derivative has the sign of
\(\sin\pi(e+t)-\sin\pi e\), so its unique maximum is at
\(e=(1-t)/2\). This is the same complete physical quotient
comparison used in the far-half source proof.

Define
\[
 D(t)=L(t)-J(1/2-t)-3J(t),\qquad 0<t<1/2.             \tag{12}
\]
The established \(\overline Q(1/2)<41/40\) and equations (4),
(10)--(11) give
\[
 \mathcal E(1/2;0)
 <\frac{41}{40}+\frac{433}{500}+\max_{0<t<1/2}D(t).     \tag{13}
\]
This use of the full interval only enlarges a scalar upper bound.
Direct differentiation gives
\[
\begin{split}
 D'(1/4)&=\log\cos(\pi/8),\\
 D''(t)&=-\frac\pi2\tan(\pi t/2)
          -\pi\tan\pi t-3\pi\cot\pi t
            \le-2\pi\sqrt3.
\end{split}                                             \tag{14}
\]
The quadratic support at \(1/4\) therefore yields
\[
 \max D\le D(1/4)
           +\frac{\log^2\cos(\pi/8)}{4\pi\sqrt3}.       \tag{15}
\]
All endpoint values are covered by continuous limits of this support.

The elementary inequality \(\log\cos z\le-z^2/2\) gives
\[
\begin{split}
 L(t)&=2\int_0^{t/2}\log(2\cos\pi u)\,du
                   \le t\log2-\frac{\pi^2t^3}{24},\\
 D(1/4)&\le\frac14\log2-\frac{\pi^2}{1536}-4J(1/4)
             <\frac7{40}-\frac3{512}+\frac{73}{125}.
\end{split}                                             \tag{16}
\]
Here \(\log2<7/10\), \(\pi>3\), and the unchanged
\(-4J(1/4)<73/125\) from
[the endpoint seam majorants](research_mixed_endpoint_seam_majorants.md)
are sufficient. Finally \(\cos(\pi/8)>10/11\), since
\(\cos^2(\pi/8)=(2+\sqrt2)/4>17/20>100/121\).
Consequently
\[
 -\log\cos(\pi/8)<\log(11/10)<1/10,\qquad
 \frac{\log^2\cos(\pi/8)}{4\pi\sqrt3}<\frac1{2000},   \tag{17}
\]
where \(\pi\sqrt3>5\).
Combining these exact inequalities proves
\[
 \boxed{\quad
 \mathcal E(1/2;0)
 <\frac{53}{20}-\frac3{512}+\frac1{2000}
 <\frac{529}{200}.
 \quad}                                                 \tag{18}
\]
For the last rational comparison, \(3/512>11/2000\).
Thus (18) is a uniform ceiling for an allowed complete private
envelope, with all five profiles included.

## 4. The calibration and a mandatory-cut test remain separate

The proved original action floor \(M>22269/10000\) does not
turn (18) into a strict gap. No sharper action floor, or sign of
\(\mathcal E(1/2;h_e)-M\), is asserted here. In particular a
nonzero coherent terminal value at the half point is not substituted
for this real-transform upper envelope.

There are also exact lower witnesses for the envelope, independent
of the choice of private main height. Every real cut
\(e\in\{.27,.49\}\) and every \(t\in[1/10,1/3]\) give
\[
\begin{split}
 \mathcal E(1/2;h_e)\ge{}&-7J(1/4)+\lambda(e)+J(e+t)-J(e)\\
                       &-J(1/2-t)-3J(t).
\end{split}                                             \tag{19}
\]
This uses only \(\overline Q(1/2)\ge Q(1/2,1/4)=-7J(1/4)\)
and the inclusion of both real-cut profiles in \(A\). At
\((e,t)=(.27,1/4)\), it reads
\[
 \mathcal E(1/2;h_e)
 \ge\lambda(.27)+J(.52)-J(.27)-11J(1/4).               \tag{20}
\]
Neither (19) nor (20) has been compared with an upper bound on the
actual action. They therefore establish no failure of the criterion.
If a future rigorous comparison does show such an excess, it will
concern the real-transform majorant and require retaining additional
transform cancellation; it will not be a lower bound or a failure
statement for the original signed finite source.
