# Contracting the complete-end tail inside the inner three-trace

Private exact-algebra and source theorem, 8 November 2026.
No mathematical numerical evaluation or frozen-source edit is used.

The first edge can also be shortened inside the full inner trace,
with a uniformly exponentially smaller error on the actual positive
outer family. At even levels every removed row is radical. At odd
levels all rows above the middle vanish at the complete end, while
the middle row contracts through distinct physical values, including
the simple node \(-2\). Its coefficients are uniformly bounded.
This is a trace-level estimate, not pointwise equality of the two
first-edge kernels.

## 1. Original algebra and statement

Use the original full physical algebra, trace, and crossing:
\[
\begin{gathered}
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad U=m-1,
 \quad\theta=\pi/N,\quad q=e^{i\theta},\quad\eta=(-1)^D,\\
 P_N(x)=2T_N(x/2)+2,\qquad
 \mathcal A_N=\mathbb C[x]/(P_N),\\
 \phi_N(f)=\eta N^2[x^D]\operatorname{rem}_{P_N}f,\qquad
 \kappa=q^{D^2/2},\qquad C_{N,3}=q^{3D^2/4},\\
 s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\quad S_0=1,\\
 c_a=2\cos((2a+1)\theta),\qquad
 e_j(x)=S_j^{-2}\prod_{a<j}(c_a-x),\\
 R_N(c_a)=\kappa(-1)^a q^{a(a+1)},\qquad
                         \phi_N(e_i e_j)=\delta_{i+j,D}.
\end{gathered}                                                     \tag{1}
\]
All repeated-root data are retained. Set
\[
 \begin{split}
 \mathcal K_N(x,z)&=\sum_{j=0}^{D}e_j(x)e_j(z),&
 \mathcal K_N^<(x,z)&=\sum_{j=0}^{U}e_j(x)e_j(z),\\
 z_u&=-2\cos u,&
 Q_N(u)&=\phi_N^{(x)}
       [R_N(x)^3\mathcal K_N(x,-2)\mathcal K_N^<(x,z_u)],\\
 Q_N^{<<}(u)&=\phi_N^{(x)}
       [R_N(x)^3\mathcal K_N^<(x,-2)\mathcal K_N^<(x,z_u)],&
 E_N(u)&=Q_N(u)-Q_N^{<<}(u).
 \end{split}                                                       \tag{2}
\]
The quantity \(Q_N\) is exactly the shortened inner source of
[the outer low-edge reduction, equation (12)](research_mixed_next_outer_exact_low_edge_reduction.md).
The second shortening in \(Q_N^{<<}\) concerns the complete-end
first edge. Its trace is still the original full Hermite trace.

**Theorem.** There are constants \(C,A\) such that
\[
 \boxed{\quad
 |E_N(u)|\le C N^A
       \exp N\left(b_2+\frac23\right),
 \qquad |\Re u|\le\pi,\quad |\Im u|\le\frac12,
 \quad b_2<\frac{729}{1250}.
 \quad}                                                           \tag{3}
\]
The same bound holds for the sum of the absolute values of all
terms in the physical-value contraction in Sections 2--3.
In particular, on the actual family
\[
 \mathcal U_+=\{b-iK:0\le b\le\pi/2,\ 0\le K\le1/2\},
                                                                    \tag{4}
\]
with its original action \(S(u)=S_3(0,u)\),
\[
            Q_N(u)=Q_N^{<<}(u)
                       +O(e^{N(\Re S(u)-1/300)}).
                                                                    \tag{5}
\]
No bound for \(Q_N^{<<}\) follows from this theorem. Equation (5)
does not assert that applying another, unestimated outer trace
preserves its gap.

## 2. Every even tail row is radical

Suppose \(N=2m\). The removed indices in the first edge are
\(m\le b\le D\). Write \(b=D-r\), so \(0\le r<m\).
For these exact ranges,
[radical contraction, Theorems 1--2](research_high_newton_radical_contraction.md)
gives
\[
 \begin{split}
 \phi_N(R_N^3 e_{D-r}f)
   &=\sum_{a=0}^r b_{ra}R_N(c_a)^3 f(c_a),\\
 b_{ra}&=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},
       \qquad |b_{ra}|\le2 .
 \end{split}                                                       \tag{6}
\]
The complete-end coefficients themselves satisfy
\[
                       |e_{D-r}(-2)|\le\sqrt{N-1}
                                                                    \tag{7}
\]
by the real-period Fourier estimate in Section 7 of that source.
This bound concerns the radical basis and is used only at
the eligible \(r<m\).

Consequently the exact even-level error is
\[
 \boxed{\quad
 E_N(u)=\sum_{r=0}^{m-1} e_{D-r}(-2)
           \sum_{a=0}^r b_{ra}R_N(c_a)^3
                             \mathcal K_N^<(c_a,z_u).
 \quad}                                                           \tag{8}
\]
Every crossing value in (8) has modulus one. Equation (6)
consumes the original first normal at each double node; it
does not replace the original trace by a distinct-node trace
on an arbitrary source.

## 3. The odd middle row and its simple endpoint

Now let \(N=2m+1\), so \(D=2m\). There are \(m\) double
nodes \(c_0,\ldots,c_{m-1}\) and one simple node \(c_m=-2\).
Every \(e_b(-2)\) with \(b>m\) vanishes, since its defining
product contains \(c_m+2=0\). Thus only \(b=m\) survives
from the first-edge tail.

We first record its exact complete-end value:
\[
                              e_m(-2)=1.
                                                                    \tag{9}
\]
One direct proof uses
\(S_m^2=S_{N-1}=N\) and
\(\prod_{a<m}(c_a+2)=N\), as in
[the original last distinct-node calculation, Section 3](research_original_low_color_bound.md).
For the second product without a trigonometric limit, put
\(r_m(x)=\prod_{a<m}(x-c_a)\). Then
\[
 P_N(x)=(x+2)r_m(x)^2,\qquad
 P_N'(-2)=N U_{N-1}(-1)=N^2.
 \tag{10}
\]
The product \(\prod_{a<m}(c_a+2)\) is positive, and (10)
shows its square is \(N^2\). This proves (9).

**Lemma.** At odd levels, for every \(f\in\mathcal A_N\),
\[
 \boxed{\quad
 \phi_N(e_m f)=
  \sum_{a=0}^{m-1}(-1)^{m+a}
          2\cos((m-a)\theta)\,f(c_a)+f(-2).
 \quad}                                                           \tag{11}
\]
All displayed coefficients have modulus at most two; the
coefficient of the simple-node value is exactly one.

*Proof.* Expand the full canonical representative as
\(f=\sum_{j=0}^{D}f_j e_j\). The unchanged Frobenius pairing
in (1) gives \(\phi_N(e_m f)=f_m\).
The first \(m+1\) nodes are distinct, and every \(e_j\) with
\(j>m\) vanishes at all of them. Ordinary Newton interpolation
therefore gives exactly
\[
 f_m=(-1)^mS_m^2\sum_{a=0}^m
       \frac{f(c_a)}
        {\prod_{\substack{0\le h\le m\\h\ne a}}(c_a-c_h)}.
                                                                    \tag{12}
\]
The denominator has sign \((-1)^a\).
The removable sine cancellation in
[original low-color bound, equation (13)](research_original_low_color_bound.md)
is
\[
 \frac{S_m^2}
  {\left|\prod_{h\ne a}(c_a-c_h)\right|}
 =\begin{cases}
       2\cos((m-a)\theta),&a<m,\\
       1,&a=m .
   \end{cases}                                                     \tag{13}
\]
For \(a<m\), it follows by pairing equal sine factors about
\((m+1/2)\theta=\pi/2\); equivalently the quotient is
\(s_{2a+1}/s_{m+a+1}=2\cos((m-a)\theta)\).
For \(a=m\), it is precisely \(1/e_m(-2)=1\).
Thus no \(0/0\) factorial expression is evaluated at the
last node. Equations (12)--(13) prove (11). \(\square\)

There is also a direct Hermite interpretation. At a double
node, \(e_m(c_a)=0\), so the local trace
\[
       \eta\{(4-c_a^2)h'(c_a)-c_a h(c_a)\},
                         \qquad h=e_m f,
                                                                    \tag{14}
\]
reduces to the normal of \(e_m\) times \(f(c_a)\).
The derivative of \(f\) and the value term vanish there.
At the simple node the original trace is \(h(-2)\), which
is exactly \(f(-2)\) by (9). The final term of (11) is
therefore essential.

Apply (11) to \(R_N^3 f\). Evaluation remains an algebra
homomorphism, and every original \(R_N(c_a)\) has modulus
one. At the simple endpoint,
\[
 R_N(-2)=\kappa(-1)^m q^{m(m+1)}=q^{m^2},
 \qquad R_N(-2)^3=q^{3m^2}=C_{N,3}.
                                                                    \tag{15}
\]
The equality follows since \(N=2m+1\) and \(q^N=-1\).
Thus the exact odd-level error, retaining the simple node,
is
\[
 \boxed{\quad
 E_N(u)=\sum_{a=0}^{m-1}(-1)^{m+a}
      2\cos((m-a)\theta)R_N(c_a)^3
                           \mathcal K_N^<(c_a,z_u)
           +C_{N,3}\mathcal K_N^<(-2,z_u).
 \quad}                                                           \tag{16}
\]
This proves a polynomial coefficient bound for the middle
row without treating that row as radical.

## 4. A uniform finite bound for the surviving values

The all-index real Newton estimate and its complex-strip
extension in
[the complete outer boundary proof, Sections 2--3](research_mixed_next_outer_far_angles_and_verticals.md),
also recorded in
[the complete inner boundary proof, equation (20)](research_mixed_next_inner_three_far_samples_and_verticals.md),
give
\[
 \begin{split}
 \sup_{-2\le x\le2}|e_k(x)|
                     &\le C N^A e^{Nb_2},\\
 \sup_{\substack{|\Re u|\le\pi\\|\Im u|\le2/3}}
       |e_k(-2\cos u)|
                     &\le C N^A e^{2N/3},
                  \qquad 0\le k\le D .
 \end{split}                                                       \tag{17}
\]
These are upper bounds for each literal finite polynomial,
including its zeros and both level parities. In particular
they apply to every retained \(k\le U\) and all the real
nodes in (8) and (16). The direct finite sum therefore yields
\[
 \sup_{-2\le x\le2}|\mathcal K_N^<(x,z_u)|
       \le C N^A e^{N(b_2+2/3)}
       \quad(|\Re u|\le\pi,\ |\Im u|\le1/2).
                                                                    \tag{18}
\]
At double physical nodes the literal terms with \(k>a\)
vanish; this only improves (18). At the odd simple node
all retained \(k\le m-1\) remain, and are bounded by (17).
In particular no claim that a complete-end kernel value is
polynomially bounded has been made.

Equations (7)--(8), (13), (15)--(16), and (18) prove (3):
the number of physical terms, every contraction coefficient,
and every complete-end tail coefficient contribute only
fixed powers of \(N\). Their absolute sum has the same
upper rate. The unit crossing phases are retained in the
exact identities even though only their moduli are used
for this upper estimate.

Finally [the actual inner action floor](research_mixed_next_inner_three_far_samples_and_verticals.md),
equation (19), gives
\[
 \Re S(u)>\frac{79}{63},\qquad
 \frac{79}{63}-\left(\frac{729}{1250}+\frac23\right)
                       =\frac{323}{78750}.
                                                                    \tag{19}
\]
The reserve after a final gap \(1/300\) is
\[
                  \frac{323}{78750}-\frac1{300}
                              =\frac{121}{157500}>0.
                                                                    \tag{20}
\]
Absorbing the polynomial prefactor in (3) proves (5).

The exact source remaining in \(Q_N^{<<}\) still contains
the full original inner Hermite trace, crossing, and all
its physical values and first normals. Both incident edge
sums now terminate at \(U\), and their product has ordinary
degree at most \(2U<N\). This last degree observation is
not an estimate of the remaining coherent trace or its
subsequent outer observation.
