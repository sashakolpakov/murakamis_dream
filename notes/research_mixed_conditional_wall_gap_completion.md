# Conditional asymptotics from the boundary action comparison

Research deduction, 7 November 2026. On the displaced incoming
rectangle, one remaining inequality suffices for a complete
asymptotic of the original conditional polynomial. This note states
that implication with all finite summands and contour segments
included. It also proves the inequality whenever the selected
critical point has nonpositive imaginary part.

The comparison for positive critical heights is not assumed. The
result does not give a new knot-family theorem or a complete
estimate for the product with the cap. No numerical evaluation is
used.

## 1. The finite polynomial and the comparison

Use the compact parameter set
\[
\begin{gathered}
 a=x-i\eta,\qquad \frac12\le x\le\frac7{10},\qquad
                         0\le\eta\le\frac9{125},\\
 y=z+iH,\qquad \frac{11}{50}\le z\le\frac9{20},\qquad
                         0\le H\le\frac1{100}.
\end{gathered}                                                     \tag{1}
\]
Write this set as \(\mathcal D\). Retain the original definitions
\[
\begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad
 p_j(X)=(rX;r)_j,\qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\\
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                    \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,
 \qquad g'(q)=\Log(1-e^{-2\pi iq}).
\end{gathered}                                                     \tag{2}
\]
The logarithms and primitives have their original branches on
\(0<\Re q<1\). The
[critical-branch theorem](research_mixed_conditional_negative_height_branch.md)
provides the unique selected upper root \(V=e^{2\pi it_*}\),
with the original equation \(Q_t(t_*;a,y)=0\). Put
\[
 u_*=\Re t_*,\qquad h_*=\Im t_*,\qquad
 \Theta(a,y)=Q(t_*;a,y),\qquad M=\Re\Theta,\qquad w=1-x.
                                                               \tag{3}
\]
The same theorem proves
\[
 \frac1{16}<u_*<w,\qquad \frac25<|V|<2,
 \qquad \Re Q_{tt}(t+i\sigma;a,y)<0
       \quad\left(\frac1{16}\le t<w,\ \sigma\in\mathbb R\right).
                                                               \tag{4}
\]
The critical-point distances are uniform and positive on
\(\mathcal D\).

Let \(\mathcal R(t;a,y)\) be the continuous physical row rate
defined with all incoming factors and the carrier retained:
\[
\begin{split}
 \mathcal R(t;a,y)
  ={}&\int_0^t\log|e^{2\pi\eta}-e^{-2\pi i(x+s)}|\,ds\\
     &+\int_0^t\log|1-e^{2\pi H-2\pi i(z+s)}|\,ds-3J(t).
\end{split}                                                       \tag{5}
\]
Integrated logarithmic zeros are interpreted continuously. Define
\[
              W(a,y)=\mathcal R(w;a,y),\qquad G(a,y)=M(a,y)-W(a,y).
                                                               \tag{6}
\]
Both functions in (6) are continuous on \(\mathcal D\).
The [wall reduction](research_mixed_conditional_negative_height_wall_reduction.md)
proves that \(\mathcal R(t)\) decreases on \(w\le t\le1/2\).
It also proves that \(G(x-i\eta,y)\) decreases strictly with
\(\eta\). Thus the sign of \(G\) throughout the full parameter
rectangle would follow from its sign on \(\eta=9/125\).
That deepest-face sign is not an input asserted by this note.

## 2. A comparison from the height of the critical point

The boundary phase below is the limit from \(\Re t<w\):
\[
                 F_b(\sigma)=\Re Q(w+i\sigma;a,y).
                                                               \tag{7}
\]
It is continuous at the possible incoming zero \(\sigma=\eta\).
The primitive \(g\) has a finite continuous limit there: its
derivative has only a logarithmic singularity. Also
\(F_b(0)=W\), by the original integrated physical rate.

**Lemma 1.** There exists a constant \(d_0>0\), uniform on
\(\mathcal D\), such that
\[
\begin{array}{ll}
 G(a,y)\ge d_0+\dfrac{\pi}{10}|h_*|,&h_*\le0,\\[2mm]
 G(a,y)\ge d_0-\pi h_*,&h_*\ge0.
\end{array}                                                       \tag{8}
\]
No numerical value for \(d_0\) is needed.

*Proof.* Write \(A(q)=\Arg(1-e^{-2\pi iq})\), taking the original
strip argument and its left boundary limits. For \(t=w+i\sigma\),
\[
              \Im Q_t=A(a+t)+A(y+t)-3A(t)+2\pi x.
                                                               \tag{9}
\]
First suppose \(\sigma\le0\). Since
\(a+t=1+i(\sigma-\eta)\), the incoming argument is zero
when \(\sigma-\eta<0\). At a possible endpoint zero use this
one-sided vertical limit. Moreover
\[
 A(y+t)\ge\pi-2\pi(z+w),\qquad
                  0\le A(t)\le\frac{\pi}{2}-\pi w.
                                                               \tag{10}
\]
The first inequality uses \(1/2<z+w\le19/20\) and is valid
at every outgoing height. The second uses \(w\le1/2\) and
an own radius at most one. Since \(x=1-w\), (9)--(10) give
\[
             \Im Q_t\ge\frac{3\pi}{2}-2\pi z-\pi w
                           \ge\frac{\pi}{10}.
                                                               \tag{11}
\]
Consequently \(F_b'(\sigma)\le-\pi/10\) for \(\sigma<0\),
and integration gives
\[
              F_b(h_*)\ge W+\frac{\pi}{10}|h_*|
                                      \quad(h_*\le0).
                                                               \tag{12}
\]
The equality case \(h_*=0\) uses continuity.

For \(\sigma\ge0\), the incoming boundary argument is either
zero or \(-\pi\). The outgoing argument is nonpositive, and
the own argument satisfies
\[
                      A(t)\ge\frac{\pi}{2}-\pi w .
\]
Thus (9) instead gives
\[
             \Im Q_t\le\frac{\pi}{2}+\pi w\le\pi.
                                                               \tag{13}
\]
Its boundary value can jump at \(\sigma=\eta\), but is bounded
on both sides and the primitive is continuous there. Integration
therefore remains valid across that point:
\[
                         F_b(h_*)\ge W-\pi h_*
                                         \quad(h_*\ge0).
                                                               \tag{14}
\]

It remains to make the horizontal strict inequality uniform.
Put \(d=w-u_*>0\), and let \(d_{\min}>0\) be its minimum
on \(\mathcal D\). On the compact collection of segments
\[
       t_*+s,\qquad 0\le s\le d/2,
\]
the real part stays a uniform distance below the incoming wall.
Equation (4) and compactness give a constant \(\kappa>0\)
such that \(-\Re Q_{tt}\ge\kappa\) on these segments.
Horizontal concavity holds on the rest of the segment up to
the wall as well. Since \(Q_t(t_*)=0\), twice integration,
followed by the continuous wall limit, gives
\[
\begin{split}
 M-F_b(h_*)
 &=\int_0^d(d-s)\{-\Re Q_{tt}(t_*+s)\}\,ds\\
 &\ge\kappa\int_0^{d/2}(d-s)\,ds
   =\frac{3\kappa d^2}{8}\ge\frac{3\kappa d_{\min}^2}{8}.
\end{split}                                                       \tag{15}
\]
If the wall itself is a logarithmic zero, first integrate to
a point strictly before it and then take the continuous limit.
The lower bound uses only the nonsingular first half of the
segment. Set \(d_0=3\kappa d_{\min}^2/8\).
Combining (12), (14), and (15) proves (8). \(\square\)

In particular every parameter with \(h_*\le0\) satisfies the
needed wall inequality, with a uniform positive reserve.
This is an automatic domain for the theorem below. The second
line also gives a uniform small positive-height extension; it
does not give a quantified bound large enough to contain every
positive critical height in (1).

## 3. Completion of the original finite conditional sum

**Theorem 2.** Let \(\mathcal K\) be any compact subset of
\(\mathcal D\) on which \(G>0\). On a fixed complex neighborhood
of \(\mathcal K\), the complete original polynomial has
\[
 C_{1,N}(e^{-2\pi ia},e^{-2\pi iy})
   =N^{-1}\mathcal B(a,y)e^{N\Theta(a,y)}
                       \bigl(1+O_{\mathrm{hol}}(N^{-1})\bigr),
 \qquad \mathcal B(a,y)\ne0.
                                                               \tag{16}
\]
Both integer parities and all fixed mixed derivatives of the
normalized error are included. In particular this applies to
the whole compact subset
\[
             \mathcal D_-=\{(a,y)\in\mathcal D:h_*(a,y)\le0\}.
                                                               \tag{17}
\]

*Proof.* Compactness gives \(\gamma=\min_{\mathcal K}G>0\).
The wall reduction pays every physical row between \(w\) and
\(1/2\) below \(M-\gamma\). The
[upper-half theorem](research_mixed_conditional_negative_height_upper_half.md)
pays every physical row at and above \(1/2\). By the zero-safe
continuity of (5), a fixed sufficiently small collar before
the wall has rate below \(M-\gamma/2\). Choose its width
smaller than the uniform critical-point distance in (4).

Keep the exact cuts
\[
\begin{gathered}
 L_N=\lfloor N/16\rfloor+1,\qquad
 K_N(x)=\lceil N(1-x-\varepsilon)\rceil,\\
 \ell_N=(L_N-1/2)/N,\qquad u_N=(K_N(x)-1/2)/N .
\end{gathered}                                                     \tag{18}
\]
For all large \(N\), the real upper cut is in the paid collar
and stays strictly to the right of \(u_*\). The complete
physical complement \(j\ge K_N(x)\) is paid by that collar,
the wall comparison, and the upper-half theorem. The
[lower-current theorem](research_mixed_conditional_negative_height_lower_currents.md)
already pays \(0\le j<L_N\) and the real lower cut.

The canonical interpolation is unchanged:
\[
 T_N(t)=e^{2\pi iNat}\Pi_N(a+t)\Pi_N(y+t)
                     E_N(a)E_N(y)E_N(t)^3,\qquad E_N=1/\Pi_N.
                                                               \tag{19}
\]
It agrees exactly with the physical summand at \(t=j/N\).
Every factorial argument is regular on
\(\ell_N\le\Re t\le u_N,\ |\Im t|\le2\). The original
split residue formula therefore gives the real integral
\(N\int_{\ell_N}^{u_N}T_N(t)\,dt\), with density \(+N\),
and both horizontal and all four vertical half-side
remainders.

The lower-current theorem pays both horizontal remainders
and the lower vertical sides. Its argument bounds on the
upper vertical sides reduce their rates to the real upper
cut, with additional losses
\[
 -(\pi/5)\sigma\quad(\sigma\ge0),\qquad
 -(7\pi/20)|\sigma|\quad(\sigma\le0).
\]
The newly paid real upper cut therefore pays these complete
sides too.

Move the real main segment to height \(h_*\), keeping both
unweighted vertical connectors. On that height line,
horizontal concavity and the fixed distances of the cuts
from the critical point give a strict gap at both ends.
Their real values have already been paid. Since
\(\partial_{\sigma\sigma}\Re Q=-\Re Q_{tt}>0\), the entire
vertical connectors are bounded by their endpoint values.
This includes the upper connector, which was not paid in
the lower-current theorem alone.

Every omitted physical group and every added contour
remainder is consequently bounded by
\[
                   C N^B e^{N(M-\gamma_1)}
                                                               \tag{20}
\]
for some uniform \(\gamma_1>0\), after choosing all factorial
error tolerances within the strict reserves. No off-grid
termination or dropped numerator factor is used.

On the retained main segment the original regular factorial
symbol is
\[
\begin{gathered}
 T_N(t)=N^{-3/2}b(t;a,y)e^{NQ(t;a,y)}
                                  (1+O_{\mathrm{hol}}(N^{-1})),\\
 a_0(q)=\sqrt{2\sin\pi q}\,e^{-i\pi q/2},\qquad
 b(t;a,y)=\frac{a_0(a+t)a_0(y+t)}
                       {a_0(t)^3a_0(a)a_0(y)},\\
 \mathcal B(a,y)=
          \frac{\sqrt{2\pi}\,b(t_*;a,y)}
                            {\sqrt{-Q_{tt}(t_*;a,y)}} .
\end{gathered}                                                     \tag{21}
\]
These are the original symbols from the
[real-arc complete theorem, equations (35)--(36)](research_mixed_real_arc_complete_conditional_packet.md).
All branches remain in the same primitive strips.
The Gaussian square root has positive real part because
\(-\Re Q_{tt}>0\). Every factor in \(\mathcal B\) is
nonzero. The unique horizontal maximum gives (16):
the row power \(N^{-3/2}\), residue density \(N\), and
Gaussian width \(N^{-1/2}\) multiply to \(N^{-1}\).
The remainders (20) are exponentially smaller.

For complex continuation, fix the integer cuts and all
paths at each base point before moving the parameters.
The strict physical and contour gaps persist in a fixed
neighborhood; so does the local nondegenerate saddle
expansion. Compactness supplies finitely many such charts.
They describe the same entire finite polynomial and the
same continued critical branch. Cauchy's formula on smaller
neighborhoods gives all stated derivatives. No moving
integer cutoff is differentiated.

Finally Lemma 1 supplies \(G\ge d_0>0\) on the closed
compact set (17), so that set meets the hypotheses.
\(\square\)

## 4. A nonempty domain at the full incoming depth

The automatic domain (17) includes a whole incoming-depth
segment at the half face. More precisely,
\[
 x=\frac12,\qquad 0\le\eta\le\frac9{125},\qquad
                  \frac38\le z\le\frac9{20},\qquad H=0
                                                               \tag{22}
\]
has \(h_*<0\). This can be checked algebraically without
evaluating the critical root.

Write \(X=-\rho\), where \(5/8<\rho\le1\); the lower-current
theorem proves this radius bound. Suppose a selected root
were on the unit circle, \(V=e^{i\phi}\), \(0<\phi<\pi\).
Solving the critical equation for \(Y\) gives
\[
          Y=V+\frac{\rho(V-1)^3}{V(V+\rho)} .
                                                               \tag{23}
\]
With \(c=\cos\phi\), multiplication by \(|V+\rho|^2\) yields
the exact factorization
\[
 |V+\rho|^2(|Y|^2-1)
       =4\rho(c-1)^2\{(\rho-1)-2(1+\rho)c\}.
                                                               \tag{24}
\]
Here \(|Y|=1\), so
\[
                    c=\frac{\rho-1}{2(1+\rho)}>-\frac3{26}.
                                                               \tag{25}
\]
In particular
\(\Re(V+\rho)>5/8-3/26=53/104>1/2\), while
\(\Im(V+\rho)\le1\). It follows that
\[
                 \Arg(V+\rho)<\arctan2<\frac{3\pi}{8},
                                                               \tag{26}
\]
using \(\tan(3\pi/8)=1+\sqrt2>2\).

At a unit root the original logarithmic equation has
\[
                    \Im Q_t=\Arg(V+\rho)-\pi z.
                                                               \tag{27}
\]
To verify the lift, the incoming argument is
\(\Arg(V+\rho)-\phi\); the outgoing and own arguments
on their real strips are respectively
\(\pi/2-\pi(z+\phi/(2\pi))\) and \(\pi/2-\phi/2\).
Adding the carrier \(\pi\) gives exactly (27).
Equations (26)--(27) contradict \(z\ge3/8\).
Thus no selected root reaches the unit circle on (22).

For the side of that circle, use the endpoint
\(\rho=1,z=1/2\), temporarily allowing this outgoing
boundary value. Its polynomial is
\[
                         2V^3-V^2+4V-1.
                                                               \tag{28}
\]
Its derivative is strictly positive on the real line, and
its unique real root \(\alpha\) lies in \((0,1/2)\).
The conjugate nonreal roots consequently have squared
modulus \(1/(2\alpha)>1\). The upper root is simple and
continues to \(z<1/2\), where it is the unique selected
upper root of the original equation.

The same unit-circle exclusion works on the connected
domain \(5/8<\rho\le1,\ 3/8\le z<1/2\).
The root cannot change its side of the unit circle there.
Thus \(|V|>1\) on (22), or \(h_*=-\log|V|/(2\pi)<0\).
Compactness gives a uniform strict margin on (22);
Theorem 2 therefore applies on a fixed complex neighborhood
of this entire set, including its deepest incoming values.

This example is a conditional-factor statement. The still
unresolved positive-height part of (1), the required cap
source bounds, and the comparison with the following
geometric action remain necessary for the next full
composition theorem.
