# Exact removal of the upper second-edge rows in the remaining outer trace

Private source theorem, 8 November 2026. No mathematical numerical
evaluation or frozen-source edit is used.

The remaining outer functional contains a factor which vanishes at
every physical spectral value. Multiplication by this factor
annihilates every second-edge Newton row of index at least
\(\lfloor N/2\rfloor\). At odd levels this includes the middle row,
even though that row itself is not in the radical of the physical
algebra. The resulting shorter kernel gives the same original trace.
Its contour formula and its endpoint bounds are derived below.

This removes the separate upper-row estimate for this particular
functional. The retained low rows, the full inner trace, and the
central outer contour still require estimates.

## 1. The annihilator of the outer factor

Let
\[
\begin{gathered}
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 M=\lceil N/2\rceil,\quad U=m-1=D-M,\\
 Q_N(x)=2T_N(x/2)+2,\qquad
 \mathcal A_N=\mathbb C[x]/(Q_N(x)),\\
 c_j=2\cos((2j+1)\pi/N),\quad
 s_k=2\sin(\pi k/N),\quad S_k=\prod_{\nu=1}^k s_\nu,\\
 e_b(x)=S_b^{-2}\prod_{j<b}(c_j-x),\qquad S_0=1 .
\end{gathered}
\tag{1}
\]
The trace and crossing element are the original ones:
\[
 \phi_N(f)=(-1)^D N^2[x^D]\operatorname{rem}_{Q_N}f,
 \qquad R_N(c_j)=\kappa(-1)^j q^{j(j+1)},
 \quad q=e^{\pi i/N},\quad \kappa=q^{D^2/2}.
\tag{2}
\]
Their full repeated-root data are retained. In particular a trace
in another variable is not replaced by evaluation.

Put
\[
                  r_N(x)=\prod_{j=0}^{m-1}(x-c_j).
\tag{3}
\]
These \(m\) roots are distinct. At even levels they are all the
distinct physical roots, each of multiplicity two. At odd levels
there is also the simple root \(c_m=-2\). Since \(Q_N\) is monic,
\[
 Q_N(x)=
 \begin{cases}
 r_N(x)^2,&N=2m,\\
 (x+2)r_N(x)^2,&N=2m+1.
 \end{cases}
\tag{4}
\]
The definition of \(e_M\) therefore gives
\[
 e_M(x)=\frac{(-1)^M}{S_M^2}
 \begin{cases}
 r_N(x),&N=2m,\\
 (x+2)r_N(x),&N=2m+1.
 \end{cases}
\tag{5}
\]

**Theorem 1.** For every polynomial \(f\),
\[
 e_M f=0\text{ in }\mathcal A_N
       \quad\Longleftrightarrow\quad r_N\mid f .
\tag{6}
\]
Consequently
\[
                 e_Me_b=0\text{ in }\mathcal A_N
                       \qquad(m\le b\le D).
\tag{7}
\]
More generally, if \(I_N f\) is the unique polynomial of degree
less than \(m\) with values \(f(c_j)\), \(0\le j<m\), then
\[
                         e_M f=e_M I_Nf
                              \text{ in }\mathcal A_N .
\tag{8}
\]

*Proof.* Dividing \(Q_N\) by the nonzero constant multiple \(e_M\)
in (5) leaves a nonzero constant multiple of \(r_N\). Polynomial
divisibility therefore proves (6). Every \(e_b\) in (7) contains
all the factors in \(r_N\). Finally \(f-I_Nf\) is divisible by
\(r_N\), proving (8). \(\square\)

Thus multiplication by \(e_M\) factors through the semisimple
quotient \(\mathbb C[x]/(r_N)\), of dimension \(m\). This statement
concerns that multiplication, not the original algebra, which
still has double roots.

For \(N=2m+1\), \(e_m(-2)\ne0\). Nevertheless \(e_{m+1}e_m\)
is a nonzero scalar multiple of \(Q_N\), so (7) includes \(b=m\).
Merely applying square-zero nilpotence to the radical would miss
this row.

For reference, the original surviving normal is explicitly
\[
 \phi_N(R_N^p e_M f)=
  \sum_{j=0}^{U}
  (-1)^{U+j}
   \frac{s_{2j+1}S_U^2}{S_{U-j}S_{U+j+1}}\,
                   R_N(c_j)^p f(c_j)
 \qquad(p\in\mathbb Z).
\tag{9}
\]
This is [the exact radical contraction, Theorem 1](research_high_newton_radical_contraction.md)
with \(D-U=M\). Equation (9) records how the original outer
normal is consumed; it does not discard it.

## 2. The shorter second edge gives the same functional

Use the ordinary full kernel and its truncation
\[
 K_N(x,t)=\sum_{b=0}^{D}e_b(x)e_b(t),\qquad
 K_N^{<}(x,t)=\sum_{b=0}^{U}e_b(x)e_b(t).
\tag{10}
\]
The truncated kernel has degree at most \(U\) in each variable.
Theorem 1 gives an identity with arbitrary polynomial coefficients
in the other variable:
\[
                    e_M(x)\{K_N(x,t)-K_N^{<}(x,t)\}=0
                  \quad\text{in }\mathcal A_N^{(x)}[t].
\tag{11}
\]
Define
\[
\begin{split}
 \mathcal K_{3,N}(-2,x)
   &=\phi_N^{(t)}
       [R_N(t)^3K_N(-2,t)K_N(x,t)],\\
 \mathcal K_{3,N}^{<}(-2,x)
   &=\phi_N^{(t)}
       [R_N(t)^3K_N(-2,t)K_N^{<}(x,t)] .
\end{split}
\tag{12}
\]
The inner crossing, complete-end edge, and complete inner trace
are identical in these two formulas.

**Corollary 2.** For every ordinary polynomial \(P_N\),
\[
\begin{split}
 \mathcal L_N(P_N)
  &:=\phi_N^{(x)}
     [R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P_N(x)]\\
  &=\phi_N^{(x)}
     [R_N(x)^3e_M(x)\mathcal K_{3,N}^{<}(-2,x)P_N(x)] .
\end{split}
\tag{13}
\]
This equality is exact at every level. It remains valid with
arbitrary polynomial boundary variables, their fixed derivatives,
and any signed power in place of the outer power three.

*Proof.* The finite inner trace commutes with (11), as does
multiplication by every spectator. Apply the outer trace.
Boundary differentiation commutes with the same finite identity.
The crossing is an element of the original finite algebra, so
multiplication by any of its signed powers preserves zero.
\(\square\)

For each double node \(c_j\), \(0\le j<m\), one also has the
ordinary equality
\[
                 \mathcal K_{3,N}^{<}(-2,c_j)
                       =\mathcal K_{3,N}(-2,c_j).
\tag{14}
\]
Indeed \(e_b(c_j)=0\) for \(b\ge m>j\). No corresponding equality
is needed at the odd simple node.

## 3. A fresh outer contour, with its full endpoint contribution

Let
\[
\begin{gathered}
 \eta_N=(-1)^D,\quad C_{N,3}=q^{3D^2/4},\quad
 \tau_j=\frac{2\pi}{N}(D/2-j),\\
 a=\frac{11\pi}{12},\quad
 a_N=\pi-\frac{2\pi\lfloor N/24\rfloor}{N},\\
 \mathfrak B_N=
  \sup_{\substack{\theta\in[-\pi,\pi]\\|\sigma|\le1/2}}
       |P_N(-2\cos(\theta+i\sigma))|.
\end{gathered}
\tag{15}
\]
For the new ordinary polynomial in (13) set
\[
\begin{split}
 g_N^{<}(u)&=\sin u\,e_M(-2\cos u)
     \mathcal K_{3,N}^{<}(-2,-2\cos u)P_N(-2\cos u)
                                      e^{3iNu^2/(4\pi)},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2}.
\end{split}
\tag{16}
\]
The first function is entire and odd.

**Theorem 3.** There is a fixed \(h_c^{<}\in(0,1/2000]\) such that,
for either level parity, the exact identity is
\[
 \mathcal L_N(P_N)=
 -\frac{N^2C_{N,3}}{\pi i}
       \int_{\Gamma_N}g_N^{<}(u)W_N(u)\,du
       +\mathcal V_N^{<}+\mathcal R_N^{\rm far},
\tag{17}
\]
where \(\Gamma_N\) is any piecewise smooth lower-half-plane path
from \(-a_N-ih_c^{<}\) to \(a_N-ih_c^{<}\), and
\[
 \mathcal V_N^{<}
   =\frac{\eta_N N^2C_{N,3}}{\pi}
       \int_{-h_c^{<}}^{h_c^{<}}
          \frac{g_N^{<}(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
\tag{18}
\]
The removed real samples \(\mathcal R_N^{\rm far}\) agree
term by term with those of
[the full-kernel outer contour](research_mixed_next_outer_far_angles_and_verticals.md).
Both their absolute sum and the absolute integral in (18) satisfy
\[
 |\mathcal R_N^{\rm far}|+|\mathcal V_N^{<}|
       \le C N^A\mathfrak B_N e^{N(8/5+1/1000)}.
\tag{19}
\]

*Proof.* The exact derivative sampling and contour formulas in
[the complete-trace identity, Corollary 3](research_exact_complete_trace_contour.md)
apply to every ordinary polynomial, hence to the second expression
in (13). They give (17)--(18), initially for the horizontal path.
All poles of \(W_N\) lie on the real axis. Cauchy's theorem therefore
gives the stated freedom of the interior path.

We give the boundary estimates for the new kernel. The all-index
Newton bounds in Sections 2--3 of the full-kernel boundary proof are
\[
 \sup_{|\Im t|\le2/3}|e_b(-2\cos t)|
     \le C N^A e^{2N/3},\qquad
 |e_b(-2\cos\theta)|\le C N^A e^{N/12}
       \quad(a\le|\theta|\le\pi).
\tag{20}
\]
The first supremum has real period \([-\pi,\pi]\). Both bounds
hold for every \(0\le b\le D\), so summing only \(b\le U\) gives
\[
 \|K_N^{<}(-2\cos\theta,-2\cos t)\|_{|\Im t|\le2/3}
                \le C N^A e^{3N/4}.
\tag{21}
\]
This is a termwise absolute bound; it uses no cancellation from
the discarded rows. Apply the original full terminal insertion
operator, whose rate is strictly below \(17/20\), to (21).
Its degree condition holds because \(U<N\). This proves
\[
 |\mathcal K_{3,N}^{<}(-2,-2\cos\theta)|
             \le C N^A e^{8N/5}\qquad(a\le|\theta|\le\pi).
\tag{22}
\]
The inner trace and all its normals are included in that operator.

The new kernel has degree at most \(U<N\) in \(x\). The same
Chebyshev continuation argument on
\(I=[2\cos(\pi/12),2]\) therefore gives some fixed
\(\delta>0\) such that
\[
 |\mathcal K_{3,N}^{<}(-2,x)|
       \le C N^A e^{N(8/5+1/2000)}
                 \quad(\operatorname{dist}(x,I)\le\delta).
\tag{23}
\]
Choose \(h_c^{<}\le1/2000\) so that
\(2(e^{h_c^{<}}-1)<\delta\). Every point
\(-2\cos(a_N+iv)\), \(|v|\le h_c^{<}\), lies in this neighborhood.

At every physical angular point, \(e_M(-2\cos\tau_j)=0\).
At a double node only its derivative can survive in
\((g_N^{<})'(\tau_j)\). Equation (14) makes this derivative
sample identical to the full-kernel sample. At the odd simple
node \(\tau_j=0\), the derivative sample is zero in both cases,
because it is the value of \(e_M(-2)\) times the spectator.
This proves the asserted termwise equality. The bounded real
derivative of the radical, from formula (28) of the boundary
proof, together with (22), gives
\[
 \sum_{|\tau_j|\ge a_N}|(g_N^{<})'(\tau_j)|
                         \le C N^A\mathfrak B_N e^{8N/5}.
\tag{24}
\]

On the vertical segments, that same exact radical formula gives
\[
 |e_M(-2\cos(a_N+iv))|\le C N^{-1}e^{N|v|/2}.
\]
The denominator in (18) is bounded by \(e^{-N|v|}\), and the
crossing exponential by \(e^{3N|v|/2}\). The sine factor is
uniformly bounded. Hence the combined height cost is at most
\(e^{N|v|}\). Equation (23) and \(h_c^{<}\le1/2000\) prove
the absolute integral bound in (19). No cancellation between
the two vertical halves is used. \(\square\)

For the actual outgoing polynomial \(P_N=H_N(\,\cdot\,,Z_*)\),
[the fixed ellipse theorem](research_mixed_next_middle_fixed_spectral_ellipse.md)
gives
\[
 \mathfrak B_N\le C_\tau N^{A_\tau}e^{N(E_*+\tau)},\quad
 E_*=\Lambda-\frac{2383}{1500}-\frac1{50},\quad
 \Lambda=\Re\mathcal P_* .
\tag{25}
\]
Choose \(\tau=1/2000\). The exponent on the right of (19) is
then \(\Lambda-43/6000<\Lambda-1/200\).
After the outside factor \((-q)^M/(\kappa^2N)\) from
[the original outer reduction](research_mixed_next_three_outer_casimir_observation.md),
the complete boundary term is \(O(e^{N(\Lambda-1/200)})\).
The strict margin absorbs all fixed polynomial factors.

## 4. The analytic obligation that remains

The second edge in (12) now terminates at \(U=\lfloor N/2\rfloor-1\).
Its upper block is absent from the exact outer functional, at
both parities. In particular the exponential ceiling for the
full second-edge radical on a complex contour need not be paid
in (17).

The ordinary functions \(\mathcal K_{3,N}\) and
\(\mathcal K_{3,N}^{<}\) need not agree at complex spectral values.
Their central contour integrals and vertical contributions need
not agree separately. Equations (17)--(19) were proved afresh
precisely for that reason.

The retained second-edge rows near \(U\), the complete inner
trace in (12), and the remaining integral in (17) have not been
shown to lie below the required rate. No full transfer asymptotic,
noncancellation theorem, arbitrary-short filling theorem, or
finite-exceptions conclusion follows from the algebraic deletion
alone.

