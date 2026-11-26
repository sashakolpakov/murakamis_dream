# The retained contour at the real Fourier seam

Research deduction, 7 November 2026. The two explicit left-taper
inequalities, if proved on their remaining compact rectangle, pay
the complete low retained source at the physical outgoing endpoint
\(q=0\). They also pay its short half-grid continuation
\(-1/(2N)\le q\le0\). All retained aliases and joins are included.
The assertion is conditional on the stated two scalar signs; no
numerical test is performed here.

The conclusion concerns this endpoint and its shrinking real
continuation. It does not bound the remaining central part of the
outgoing vertical current or discard the bent outgoing main path.

## 1. Original source and the sole additional premise

Keep the actual references, incoming targets and allocation from
[the complete bare inner source](research_mixed_fourier_right_cap_bare_inner_completion.md).
Thus
\[
 \eta\in\{0,1\},\quad a=x+i h_a,\quad
 x\in P=[11/50,9/20],\quad
 -.102\le h_s=\Im s_*,h_q=\Im q_*\le-.001.
 \tag{1}
\]
The incoming height is original, with \(|h_a|\le.108\);
for \(\eta=1\) it is negative and unselected. Write
\[
 B_\eta(x)=M_\eta+p_\eta(x-\Re a_*)
                   -\kappa(x-\Re a_*)^2,\qquad
 \kappa=1/2500000.
 \tag{2}
\]
Every action constant and marginal in (2) is unchanged.
Put \(c=11/50\) and \(\lambda=-h_q/c\le51/110\).

The functions \(H_\pm\) are exactly those defined in
[the left-taper reduction](research_mixed_fourier_left_taper_reduction.md),
equations (10)--(13), using the original output \(Y=e^{2\pi iy}\),
\(y=x_0\). The additional premise is
\[
 H_\pm(v,\lambda)\ge0
 \quad\text{on}\quad
 [1/100,11/50]\times[0,51/110].
 \tag{T}
\]
The near-zero Lemma 2 of that note is already proved:
both minimized derivatives exceed \(3/4\) on \(0<v\le1/100\).

Let
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad X=e^{-2\pi ia},
 \quad M_N=\lceil N/2\rceil-1.
 \tag{3}
\]
The exact low retained source and physical cardinal coefficient are
\[
 C_N^<(X,Z)=\sum_{j=0}^{M_N}\frac{X^{-j}p_j(X)p_j(Z)}{P_j^3},
 \qquad
 f_0(y)=\frac{e^{-\pi i(N-1)y}(1-Y^N)}{N(1-Y)}.
 \tag{4}
\]
In particular \(p_j(1)=P_j\), so the exact seam source is
\[
 f_0(y)C_N^<(X,1)
       =f_0(y)\sum_{j=0}^{M_N}\frac{X^{-j}p_j(X)}{P_j^2}.
 \tag{5}
\]
No outgoing halfweight or new crossing scalar is inserted.

## 2. A fixed loss at the seam, before taking any finite modulus

The allocated seam phase is the continuous \(q=0\) value of the
original two-index phase:
\[
 \Psi_\eta(s,a)=g(s+a)-2g(s)-(1+\eta/2)g(a)
                           +2\pi ias-\pi iy .
 \tag{6}
\]
Here \(g(0)=0\) and \(\ell_0(y)=-\pi iy\).
The finite product (5) has this rate with its original branches.

For any \(1/8\le u\le1/2\) and \(h_s\le v\le0\),
the retained radius \(e^{2\pi v}\) belongs to \([1/2,1]\).
The taper reduction therefore applies to the same \(s=u+iv\).
Integrating its directional derivative from \(0\) to \(c\),
using (T) and its proved first-hundredth bound, gives
\[
 \Re\Psi_\eta(u+iv,a)
 <
 \Re\mathscr F_\eta(u+iv,a,c+i h_q)-\frac3{400}.
 \tag{7}
\]
The primitive has its continuous value at \(q=0\), so no
endpoint logarithm is being differentiated there. The integral
of that logarithmic derivative is legitimate.

At \(v=h_s\), the old stationary-sheet inequality yields
\[
 \Re\Psi_\eta(u+i h_s,a)
 \le B_\eta(x)-\frac3{400}
       -\kappa\{(u-\Re s_*)^2+(c-\Re q_*)^2\}.
 \tag{8}
\]
At either real retained cut \(b=1/8,1/2\), the completed
individual row comparison gives
\[
 \Re\Psi_\eta(b,a)
       <B_\eta(x)-\frac3{400}-\frac1{35000}.
 \tag{9}
\]
These are comparisons of the original source phases, not
consequences of an upper bound on a canceled finite sum.

For the unpenalized joins \(h_s\le v\le0\) at either cut,
the original bare Hessian gives vertical convexity at
\(q=c+i h_q\). The two endpoint bounds there, followed by
(7), pay every such joining point by \(B_\eta-3/400\).
Equivalently one may use the seam curvature proved below.
No assertion about convexity of the logarithm of (5) is used.

## 3. All retained aliases and joins at \(q=0\)

The seam derivative has the useful all-height strip
\[
 -\frac{53\pi}{50}
       <\Im\Psi_{\eta,s}(u+iv,a)<\frac{9\pi}{10},
 \qquad \frac18\le u\le\frac12,\quad v\in\mathbb R.
 \tag{10}
\]
Boundary equalities in elementary argument estimates can be
replaced by nonstrict inequalities without changing any reserve
below. To prove the strip, use
\[
 \Psi_{\eta,s}=g'(s+a)-2g'(s)+2\pi ia .
 \tag{11}
\]
For \(u\le1/2\), the original regular-strip argument of
\(1-e^{-2\pi is}\) is between \(0\) and
\(\pi(1-2u)\), at every finite height.
If \(u+x\le1/2\), the argument of the first term in (11)
lies between \(0\) and \(\pi(1-2u-2x)\). This gives the
lower bound \(-2\pi(1-2u)+2\pi x\ge-53\pi/50\) and
upper bound \(\pi(1-2u)\le3\pi/4\).
If \(u+x\ge1/2\), its argument lies between
\(\pi(1-2u-2x)\) and zero. The lower bound becomes
\(-\pi(1-2u)\ge-3\pi/4\), and the upper bound is
\(2\pi x\le9\pi/10\). All arguments remain in their
original \(0<\Re(s+a)<1\) and \(0<\Re s<1\) strips.

Choose the original retained heights
\[
 h_-=-1/5,\qquad h_+=5/4.
 \tag{12}
\]
Integration of (10) proves
\[
 \begin{split}
 \Re\Psi_\eta(u+i h_-,a)-2\pi/5
     &<\Re\Psi_\eta(u+i h_s,a)-11\pi/50,\\
 \Re\Psi_\eta(u+i h_+,a)-5\pi/2
     &<\Re\Psi_\eta(u+i h_s,a)-\pi.
 \end{split}
 \tag{13}
\]
For the second inequality, the unreduced upper bound is
\(-47\pi/40-(53\pi/50)h_s<-\pi\), using \(h_s\ge-.102\).
Thus both complete horizontal aliases have strict reserves.

At a fixed real cut, the paid height functions obey
\[
 \begin{split}
 \frac d{dv}\{\Re\Psi_\eta(b+iv,a)+2\pi v\}
       &>11\pi/10 &&(v<0),\\
 \frac d{dv}\{\Re\Psi_\eta(b+iv,a)-2\pi v\}
       &<-47\pi/50 &&(v>0).
 \end{split}
 \tag{14}
\]
Consequently all penalized vertical pieces are bounded by
their real-cut values (9). The unpenalized pieces were
retained and paid following (9).

For completeness, the seam itself is horizontally strictly
concave for \(|v|\le.108\):
\[
 -\Re\Psi_{\eta,ss}
       =\pi\{2\Re\cot\pi s-\Re\cot\pi(s+a)\}>0.
 \tag{15}
\]
When \(u+x\ge1/2\), the second cotangent is nonpositive,
and the first is positive unless \(u=1/2\), where the
second is strictly negative. Otherwise \(u<.28\).
Then \(\sin(2\pi u)>7/10\),
\(\cos(2\pi u)>-1/4\), and
\(\cosh(.216\pi)<5/4\), giving
\(\Re\cot\pi s>7/15\).
Also \(u+x\ge.345>1/3\), so
\(\Re\cot\pi(s+a)<\cot(\pi/3)<3/5\).
The expression in braces exceeds \(1/3\).
The elementary hyperbolic bound uses
\(.216\pi<17/25\), \((17/25)^2<7/15\), and
\[
 \cosh t\le1+\frac{t^2}{2}
              +\frac{t^4}{24(1-t^2/30)}
 <1+\frac7{30}+\frac{49}{5316}<\frac54 .
 \tag{16}
\]
This supplies a direct alternative justification for vertical
convexity of the seam joins.

## 4. The exact retained contour and the physical low tail

Let \(L_N=\lceil N/8\rceil\) and
\[
 \sigma_-=(L_N-\tfrac12)/N,\qquad
 \sigma_+=(M_N+\tfrac12)/N.
 \tag{17}
\]
Use the original exact factorial interpolation \(\Pi_N\),
with reciprocal \(E_N=1/\Pi_N\), and set
\[
 F_N(s;a,y)=
 f_0(y)e^{2\pi iNas}
             \Pi_N(s+a)E_N(a)E_N(s)^2 .
 \tag{18}
\]
At \(s=j/N\), (18) is exactly the \(j\)-th summand of
(5). It is holomorphic on a neighborhood of the complete
retained rectangle with heights (12).
The exact one-index regrouping gives
\[
 f_0\sum_{j=L_N}^{M_N}\frac{X^{-j}p_j(X)}{P_j^2}
          =Z_N+L_N^{\rm al}+U_N^{\rm al}+B_N^{\rm ver},
 \tag{19}
\]
where
\[
 \begin{split}
 Z_N&=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_s)\,du,\\
 L_N^{\rm al}
 &=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_-)
       \frac{e^{-2\pi iN(u+i h_-)}}{1-e^{-2\pi iN(u+i h_-)}}\,du,\\
 U_N^{\rm al}
 &=N\int_{\sigma_-}^{\sigma_+}F_N(u+i h_+)
       \frac{e^{2\pi iN(u+i h_+)}}{1-e^{2\pi iN(u+i h_+)}}\,du,\\
 B_N^{\rm ver}
 &=iN\int_{h_-}^{h_+}
 \left\{\frac1{1+e^{2\pi Nv}}-\boldsymbol1_{\{v<h_s\}}\right\}
       [F_N(\sigma_++iv)-F_N(\sigma_-+iv)]\,dv .
 \end{split}
 \tag{20}
\]
In particular the zero-mode coefficient is \(+N\);
the signed vertical difference and both full alias
denominators are retained. The cardinal \(1/N\) is already
inside \(F_N\), and is not canceled or inserted again.
Both parity choices in (17) enclose exactly the displayed rows.

The original compact factorial symbols bound all terms
in (20) by their phases with uniform polynomial factors.
Their \(O(1/N)\) cut shifts cost only a uniform constant,
because every retained factorial argument stays in a
fixed regular real strip. Equations (8)--(14) therefore pay
the four groups in (19) by \(B_\eta-3/400\), before
one aggregate finite tolerance and polynomial absorption.

The omitted physical rows \(0\le j<L_N\) are also paid.
Their rate is the exact real-seam rate \(E_\eta^0(u;a)\)
from [the high-row seam theorem](research_mixed_fourier_right_cap_real_seam_high_rows.md).
For \(0<u\le1/8\),
\[
 (E_\eta^0)'(u)
       =\log\frac{|X^{-1}-e^{-2\pi iu}|}
                        {|1-e^{-2\pi iu}|^2}>\log(3/2)>0.
 \tag{21}
\]
Indeed the angle between \(X^{-1}\) and \(e^{-2\pi iu}\)
is \(2\pi(x+u)\in[.44\pi,1.15\pi]\), whose cosine is
less than \(1/5\). Minimizing distance over every
nonnegative radius gives a numerator greater than \(9/10\).
The denominator is at most \(2-\sqrt2<3/5\).
The continuous \(u=0\) rate is included by integration.
Thus this whole low physical tail is bounded by its cut
value (9), with the original uniform finite-product upper
bounds and all zeros retained.

## 5. The half-grid endpoint segment

The actual outgoing endpoint is
\(\alpha_N=-1/(2N)\), not zero. Keep the global factorial
cardinal \(\widehat f_N(q;y)\) from
[the global continuation](research_mixed_fourier_global_factorial_cardinal.md),
and define the literal low source
\[
 S_N^<(q)=C_N^<(X,e^{-2\pi iq})\widehat f_N(q;y).
 \tag{22}
\]
For \(\alpha_N\le q\le0\), its central retained-row
interpolation is exactly
\[
 F_N^{(q)}(s)=
 \widehat f_N(q;y)e^{2\pi iNas}
 \Pi_N(s+a)E_N(a)\Pi_N(s+q)E_N(q)E_N(s)^3 .
 \tag{23}
\]
At a physical retained \(j\), (23) is exactly the summand
in (22); it uses neither an asymptotic interpolation
identity nor a modulus of the central physical sum.

On each fixed retained contour in (20),
\(\Pi_N(s+q)/\Pi_N(s)\) is uniformly bounded for this
\(O(1/N)\) real displacement, by the proved uniform
regular-strip symbols. Likewise
\(\widehat f_N(q;y)\) has the same bounded-relative
endpoint normalization as \(f_0(y)\); its arguments stay
in a fixed zero-free neighborhood of \(q=0\), and the
original phase displacement is \(O(1/N)\).

There is also a direct zero-safe bound
\[
                         |E_N(q)|\le C
                 \qquad(-1/(2N)\le q\le0).
 \tag{24}
\]
To see it, choose an integer \(m_N\) with
\(m_N/N\) in a fixed small neighborhood of \(1/8\).
The exact continuation formula is
\[
 E_N(q)=
 \frac{\prod_{k=1}^{m_N}(1-e^{-2\pi i(q+k/N)})}
                         {\Pi_N(q+m_N/N)} .
 \tag{25}
\]
For the real \(q\) under consideration, each numerator
modulus is at most \(|1-r^k|\), since its sine angle
decreases within \((0,\pi/2)\). Their product is at most
\(|P_{m_N}|=|\Pi_N(m_N/N)|\).
The remaining ratio of the two regular-strip factorials
is bounded for displacement \(O(1/N)\). No recurrence
factor is divided out at a zero.

Apply the exact contour (19)--(20) to (23).
The bounds just established preserve every contour group,
including all vertical joins, with only a uniform finite
prefactor. For the already paid physical low tail,
\[
 |p_j(e^{-2\pi iq})|\le|P_j|,
     \qquad \alpha_N\le q\le0,\quad 0\le j\le M_N,
 \tag{26}
\]
by the same sine-factor comparison. Use (26) only on that
physical low tail; the central sum continues to use (23).
Thus no unproved termwise bound on the central coherent
source is introduced.

## 6. Conditional finite conclusion and remaining scope

**Theorem.** Assume (T). Uniformly on the actual references
and incoming targets (1), for all sufficiently large \(N\)
of either parity,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}
       \sup_{\alpha_N\le q\le0}|S_N^<(q)|
                \le e^{N(B_\eta(x)-1/1000)} .
 \quad}
 \tag{27}
\]
In particular this includes the exact low seam
\(S_N^<(0)=f_0C_N^<(X,1)\), and
\[
 |d_N(X)|^{\eta/2}
       \left|N\int_{\alpha_N}^{0}S_N^<(q)\,dq\right|
               \le\frac12 e^{N(B_\eta(x)-1/1000)} .
 \tag{28}
\]
For example, the raw reserve \(3/400\) above allows one
fixed aggregate source tolerance \(1/1000\); the remaining
polynomial factors are absorbed before weakening to (27).

The separately proved absolute high-row seam estimate has
finite gap \(1/70000\). Adding it to (27) gives, eventually,
\[
 |d_N(X)|^{\eta/2}|f_0(y)C_{1,N}(X,1)|
                  \le e^{N(B_\eta(x)-1/140000)}.
 \tag{29}
\]
This uses the exact high/low difference at the physical
endpoint. Neither a finite incoming weight nor a cardinal
zero is divided out.

Assertions (27)--(29) remain conditional on the explicit
two-function premise (T). They do not bound
\(C_N^<(X,e^{-2\pi i(\alpha_N+iv)})\) at fixed nonzero
height, or replace its compact vertical integral by its
endpoint value. If the outgoing main path is bent to have
real endpoints, its exact integral and the real-endpoint
vertical current remain as in
[the vertical envelope](research_mixed_fourier_real_endpoint_vertical_envelope.md).
The short real segment (28) is now included; the central
retained part of the remaining compact current still needs
its own coherent estimate or regrouping.
