# The original contracted phase for arbitrary three/four cycles

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The exact Fourier contraction removes every shared wire before an
estimate is made. Its remaining index phase has a strictly negative
real Hessian on one common chamber for every word in three and four.
This note records the complete finite summand, its holomorphic symbol,
and the absolutely calibrated alternating stationary point. The full
finite-index complement is not estimated here.

## 1. An exact all-level cyclic source

Let \(n_1,\ldots,n_m\in\{3,4\}\), \(m\ge1\), and set
\(\epsilon_v=1_{n_v=4}\), \(k=\sum_v\epsilon_v\).
Use the original matrices \(A_n=JM^n\), scalar \(\kappa\), and
positive sine factorials
\(S_j=\prod_{a=1}^j2\sin(\pi a/N)\), \(S_0=1\).
Indices are cyclic, so \(i_{m+1}=i_1\). The exact support is
\[
 \mathcal P_N=\{(i_v,j_v):i_v,j_v\ge0,\quad
                  i_v+j_v<N,\quad j_v+i_{v+1}<N\ \text{for all }v\}.
 \tag{1}
\]
Put \(s_v=i_v/N\), \(t_v=j_v/N\), and define
\[
 \begin{split}
 \varphi(z)&=\frac\pi2(z-z^2),\\
 \Theta(\mathbf s,\mathbf t)
   &=\pi\sum_vt_v(s_{v+1}-s_v)
                    -\sum_v\epsilon_v\{\varphi(s_v)+\varphi(t_v)\},\\
 W_N&=\frac{\prod_v S_{i_v+j_v}S_{j_v+i_{v+1}}}
                {\prod_v(S_{i_v}S_{j_v})^{2+\epsilon_v}}.
 \end{split}
 \tag{2}
\]
Then the literal original trace is
\[
 \boxed{\quad
 \operatorname{tr}(A_{n_1}\cdots A_{n_m})
 =\kappa^{m+k}N^k
 \sum_{\mathcal P_N}W_N
  \exp\!\left(iN\Theta+\frac{i\pi}{2}
                                  \sum_v\epsilon_v(s_v+t_v)\right).
 \quad}
 \tag{3}
\]
This holds at every integer level \(N\ge2\), with both parity
conventions and every original crossing normal retained.

Indeed, expand the exact product
\(\operatorname{tr}(B_{n_1}\Gamma\cdots B_{n_m}\Gamma)\)
from the [Fourier contraction theorem](research_mixed_wire_exact_contraction.md).
Its vertex factors are \(\kappa P_{i+j}\) or
\(\kappa^2N P_{i+j}/(P_iP_j)\); each shared boundary contributes
\(Q^{jk}P_{j+k}/(P_j^2P_k^2)\). Their exact supports give (1).
Writing
\[
 P_j=(r;r)_j=S_j\exp i\vartheta_N(j),\qquad
 \vartheta_N(j)=\frac{\pi j}{2}-\frac{\pi j(j+1)}{2N},
 \tag{4}
\]
and using \(\vartheta_N(i+j)=\vartheta_N(i)+\vartheta_N(j)-\pi ij/N\)
gives (2)--(3). In particular the order-one exponential in (3)
is part of the coefficient and cannot be dropped. The weights
\(W_N\) are positive on the physical support; the phase is not
constant and no positivity of the trace is inferred.

## 2. Exact interpolation and its full symbol

Write \(J'(z)=\Log(2\sin\pi z)\) on the original strip
\(0<\Re z<1\). On any compact subset of
\[
 0<\Re s_v,\Re t_v,\Re(s_v+t_v),\Re(t_v+s_{v+1})<1,
 \tag{5}
\]
use the exact sine-factorial interpolant \(G_N(Nz)\) from
[the original interpolation proof](exact_factorial_interpolation_and_complex_contours.md).
Replace each factorial in (3) by this interpolant, before taking its
expansion. On the compact set it is nonzero for all sufficiently
large \(N\), and this gives a holomorphic function \(\mathcal T_N\)
which agrees exactly with every enclosed lattice summand, including
the prefactor in (3).

Define
\[
 \begin{split}
 H&=\sum_v\{J(s_v+t_v)+J(t_v+s_{v+1})\}
              -\sum_v(2+\epsilon_v)\{J(s_v)+J(t_v)\},\\
 \mathcal F&=H+i\Theta,\qquad L(z)=\sqrt{2\sin\pi z},\\
 a(\mathbf s,\mathbf t)
   &=e^{(i\pi/2)\sum_v\epsilon_v(s_v+t_v)}
       \frac{\prod_vL(s_v+t_v)L(t_v+s_{v+1})}
            {\prod_v\{L(s_v)L(t_v)\}^{2+\epsilon_v}}.
 \end{split}
 \tag{6}
\]
The roots are the original sine-symbol branches, positive for real
arguments in \((0,1)\).

**Theorem 1.** For each fixed word, uniformly on every compact set
in (5), the exact interpolant satisfies
\[
 \mathcal T_N=\kappa^{m+k}N^{-m}
                  a(\mathbf s,\mathbf t)e^{N\mathcal F}
                                      \{1+O(N^{-1})\}.
 \tag{7}
\]
The coefficient is holomorphic and nonzero. There is a full
holomorphic expansion in inverse powers of \(N\), with every fixed
index derivative uniform on a smaller compact set.

*Proof.* Every numerator factorial contributes \(N^{1/2}L(z)e^{NJ(z)}\).
There are \(2m\) numerator factors and total denominator exponent
\(4m+2k\). Thus their net power is \(N^{-m-k}\), which combines
with the original \(N^k\) to give \(N^{-m}\). The exact phase
(3) gives precisely (6). The all-order expansion and its derivatives
are the original uniform factorial expansion and Cauchy estimates.
\(\square\)

## 3. A length-independent Hessian bound

For any fixed \(B<\infty\), let all leg indices satisfy
\[
          \frac14\le\Re s_v,\Re t_v\le\frac9{20},\qquad
                   |\Im s_v|,|\Im t_v|\le B.
 \tag{8}
\]
Set
\[
 c_B=\frac{\pi\sin(9\pi/10)}{\cosh(2\pi B)-\cos(9\pi/10)}>0.
 \tag{9}
\]

**Theorem 2.** For every cyclic word and every point of (8),
\[
        -\Re\mathcal F''\succeq
          c_B\operatorname{diag}(2+\epsilon_1,2+\epsilon_1,
                                  \ldots,2+\epsilon_m,2+\epsilon_m)
                       \succeq2c_B I_{2m}.
 \tag{10}
\]
In particular at \(B=11/200\) the last lower bound is strictly
greater than \((4/5)I_{2m}\). The bound does not depend on the word
length or the arrangement of its letters.

*Proof.* The Hessian of \(i\Theta\) is purely imaginary, even at
complex indices, because \(\Theta\) is a quadratic polynomial
with real coefficients. The real Hessian of \(H\) is exactly
\[
 \begin{split}
 -\Re d^2\mathcal F={}&
 \sum_v[-\Re J''(s_v+t_v)](ds_v+dt_v)^2\\
 &+\sum_v[-\Re J''(t_v+s_{v+1})](dt_v+ds_{v+1})^2\\
 &+\sum_v(2+\epsilon_v)
           \{\Re J''(s_v)ds_v^2+\Re J''(t_v)dt_v^2\}.
 \end{split}
 \tag{11}
\]
Here \(J''(z)=\pi\cot\pi z\). The two sums have real parts
in \([1/2,9/10]\), so their displayed coefficients are
nonnegative. A single-leg real part is in \([1/4,9/20]\), and
\[
 \Re J''(a+ib)=\frac{\pi\sin(2\pi a)}
                              {\cosh(2\pi b)-\cos(2\pi a)}\ge c_B.
 \tag{12}
\]
The minimum is at \(|b|=B,a=9/20\): the expression decreases
in \(|b|\), and its angular derivative has sign
\(\cosh(2\pi b)\cos(2\pi a)-1<0\) on this interval.
Discarding the first two nonnegative sums proves (10). This also
handles \(m=1\), where the two summed arguments coincide, and
\(m=2\), where the two cyclic incidences must both be counted.
\(\square\)

The chamber is convex. Integrating the complex symmetric Hessian
along a line segment and pairing with the conjugate difference shows
that the full holomorphic gradient has at most one zero there.
On a horizontal plane through any such zero, (10) gives a strict
quadratic maximum and a nonzero accretive Gaussian determinant.
This does not locate a critical point for an arbitrary word.

There is a short-range algebraic form of the equations. Writing
\(U_v=e^{-2\pi is_v}\), \(V_v=e^{-2\pi it_v}\),
every critical point satisfies
\[
 \begin{split}
 (1-U_vV_v)(1-U_vV_{v-1})
       &=V_{v-1}(1-U_v)^{2+\epsilon_v},\\
 (1-U_vV_v)(1-V_vU_{v+1})
       &=U_{v+1}(1-V_v)^{2+\epsilon_v}.
 \end{split}
\]
These follow by exponentiating the actual logarithmic derivatives;
the converse still requires their zero lifts. With its two opposite
legs fixed, each equation is quadratic for a three-vertex and cubic
for a four-vertex. For example the homogeneous exponentiated four-vertex
equations admit \(U_v=V_v=(-1-i\sqrt7)/4\); this algebraic observation alone
asserts no source dominance or continuation for a general word.

## 4. Exact alternating stationarity

At the validated alternating reference let
\[
 p(a)=4a^4-6a^3+4a^2-2a+1=0,\quad
 K=(1+2a-4a^2)^{-1},\quad
 U=1-2a,\quad V=(1-K)/(2K),
 \quad z_3=-\frac{\Log U}{2\pi i},\quad z_4=-\frac{\Log V}{2\pi i}.
 \tag{13}
\]
These are the original reference branches in the full
[V3 packet](research_three_vertex_mixed_reference_packet.md) and
[V4 packet](research_power_four_source_packet.md). In particular
\(z_3\simeq.353583333-.016783825i\) and
\(z_4\simeq.284527778-.042367208i\), strictly inside (8) with
\(B=11/200\).

For an alternating cycle of even length \(m\), set
\(s_v=t_v=z_{n_v}\). Both leg gradients at a three-vertex equal
\[
 d_3=J'(2z_3)+J'(z_3+z_4)-2J'(z_3)+i\pi(z_4-z_3),
 \tag{14}
\]
and both gradients at a four-vertex equal
\[
 d_4=J'(2z_4)+J'(z_3+z_4)-3J'(z_4)+i\pi z_3-i\pi/2.
 \tag{15}
\]
Their exponentials are exactly one, since modulo \(p(a)\),
\[
 \begin{split}
 &(1-U^2)(1-UV)=V(1-U)^2,\\
 &(1-V^2)(1-UV)=U(1-V)^3.
 \end{split}
 \tag{16}
\]
The focused outward checker evaluates the actual sine-log
derivatives and encloses \(|\Im d_3|,|\Im d_4|<\pi\).
Consequently \(d_3=d_4=0\) with their original lifts. Theorem 2
now proves uniqueness in the whole chamber, not just infinitesimal
nondegeneracy at the reference.

## 5. Absolute action under the exact wire contraction

The leading phase of a boundary basis function is
\[
 \ell_s(x)=2\pi i sx-I_X(s)-\pi i x,
 \qquad X=e^{2\pi ix},\quad U=e^{-2\pi is}.
 \tag{17}
\]
For two legs \((s,t)\), put \(V=e^{-2\pi it}\) and
\[
 X_c=\frac{1-UV}{U+V-2UV},\qquad
 G(s,t)=J(s+t)-2J(s)-2J(t)-i\varphi(s+t).
 \tag{18}
\]
On the connected original branch described below,
\[
 \boxed{\qquad G(s,t)=\ell_s(x_c)+\ell_t(x_c),\qquad
                \partial_x(\ell_s+\ell_t)(x_c)=0.\qquad}
 \tag{19}
\]
This is an equality with its absolute constant, not merely an
exponentiated stationary equation.

To prove it, first observe the rational identities
\[
 (1-X_cU)(1-X_cV)=UV(1-X_c)^2,\qquad
 \frac{X_c}{1-X_cU}=\frac{1-UV}{V(1-U)^2},
 \tag{20}
\]
and their transposes. Thus the wire equation is exponentiated
stationarity, and the derivatives of the two sides of (19) have
the same exponentials. At \(s=t=1/3\) their actual logarithmic
lifts agree; the checker verifies the zero strips directly.

One connected branch joins this point to \((z_3,z_4)\): take
straight paths in \((U,V)\) from
\((e^{-2\pi i/3},e^{-2\pi i/3})\) to \((U,V)\) in (13),
and use (18). An exact interval cover proves that \(U,V\) stay
in the lower-left quadrant, \(X_c\) stays in the first-quadrant
disk, \(|X_cU|,|X_cV|<1\), and all original index and logarithm
arguments stay in their regular strips. These strict conditions
give a connected open neighborhood of the path. The lifts therefore
remain equal and the difference in (19) is constant there.

To fix it without a numerical dilogarithm comparison, continue on
the real diagonal \(s=t\in[1/3,1/2)\). Then
\(X_c=(1+U)/(2U)\) is in the first-quadrant disk and tends to
zero as \(s\uparrow1/2\). Both denominator primitives tend to
zero, while \((2s-1)\Log X_c\to0\). Thus the right side of
(19) tends to zero. The left side tends to
\(J(1)-4J(1/2)-i\varphi(1)=0\). The constant is zero.

At the alternating point one also has
\(K(U+V-2UV)=1-UV\) exactly modulo \(p(a)\), so this critical
wire is precisely the original \(x_0=\Log K/(2\pi i)\).
Since the original unsummed vertex phase is
\[
 \mathcal F_n^{\rm original}
   =g(s+t)-\epsilon_n\{g(s)+g(t)\}
                       +\ell_s(x)+\ell_t(y),\qquad
 g(z)=J(z)+i\varphi(z),
 \tag{21}
\]
summing (19) proves that the contracted critical action equals the
original unsummed critical action, with no new constant. In particular
for an alternating cycle of length \(m=2r\),
\[
 \mathcal F_c=r\{\Phi_3(x_0,x_0)+\Phi_4(x_0,x_0)\}
             =r\{\Xi_3(x_0,x_0)+\Xi_4(x_0,x_0)+i\gamma\}.
 \tag{22}
\]
Here \(i\gamma\) is exactly the previously calibrated three-vertex
carrier. The selected angular branches and their absolute real
constants are those of the full original packets. Thus the real
action is the sum of their original marked geometric actions. This
does not identify an arbitrary cyclic diagram with a knot.

## 6. The central integral and the remaining global obligation

For each fixed alternating even word take the horizontal central
chain in which each real leg ranges over \([1/4,9/20]\), with
its height fixed at \(\Im z_{n_v}\). It lies strictly inside the
exact support strips. Its zero Fourier integral, with the actual
lattice measure, is
\[
 N^{2m}\int_{\mathcal C}\mathcal T_N(\mathbf s,\mathbf t)
                          \,d\mathbf s\,d\mathbf t
 =\kappa^{m+k}\frac{(2\pi)^m a(\mathbf z_c)}
                  {\sqrt{\det(-\mathcal F''(\mathbf z_c))}}
                    e^{N\mathcal F_c}\{1+O(N^{-1})\}.
 \tag{23}
\]
The determinant uses its accretive Gaussian branch. The coefficient
is nonzero and the power of \(N\) is exactly zero: \(N^{2m}\)
from the lattice measure, \(N^{-m}\) from (7), and \(N^{-m}\)
from the \(2m\)-dimensional Gaussian. Theorem 2 controls the whole
horizontal chain and gives strict face gaps, so (23) follows directly
by holomorphic stationary phase for this specified integral.

Equation (23) is not the asymptotic of the full trace (3) without
an additional argument. Its real-index complement, the currents
joining the original real lattice to \(\mathcal C\), and all
lattice aliases still require a grouped estimate in the contracted
variables. No such estimate is asserted by the positive Hessian or
by the exact Fourier contraction alone. For nonalternating words,
the location/existence of a critical point in this chamber is an
additional obligation.

Reproduce the exact algebra, normalization, and original branch
checks with `python3 experiments/check_mixed_contracted_phase.py`.
The checker does not certify a whole-sum lower bound.
