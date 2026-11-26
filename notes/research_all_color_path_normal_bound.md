# A bound for all physical first normals

Research note, 3 November 2026.

This note proves a one-sided bound for the mixed logarithmic
derivative of the full original edge kernel at every pair of double
physical roots. The bound makes the entire first-normal matrix of
a same-sign filled path sectorial at each color assignment. Its
determinant is nonzero and loses at most a polynomial factor at
fixed path length. The same conclusion holds for a tree when
\(\operatorname{diag}(|n_v|)-\operatorname{Adj}(G)\) is positive
definite and all powers have one common sign. The argument retains the high Newton indices,
the endpoint source, and the coalescing middle nodes.

The coherent sum over color assignments is still oscillatory.
No lower bound for that sum, or a new volume-conjecture statement,
follows from the per-color result.

## 1. Definitions and statement

Use the original kernel and notation of
[the finite difference equation](research_edge_kernel_difference_and_endpoint_bound.md):
\[
 \begin{gathered}
 \theta=\pi/N,\quad D=N-1,\quad \eta=(-1)^D,\quad
 s_x=2\sin(x\theta),\quad c(x)=2\cos((2x+1)\theta),\\
 e_i(z)=\frac{\prod_{r=0}^{i-1}(c(r)-z)}
                  {\prod_{r=1}^{i}s_r^2},\qquad
 K_N(z,w)=\sum_{i=0}^{D}e_i(z)e_i(w),\\
 P_N(z)=2T_N(z/2)+2,\qquad c_j=c(j).
 \end{gathered}
 \tag{1}
\]
Here \(N\ge2\), and \(T_N\) has the standard Chebyshev
normalization. The double roots are indexed by
\[
             0\le j\le\left\lfloor\frac{N-2}{2}\right\rfloor.
 \tag{2}
\]
For these indices put
\[
 m_j=N-2j-1>0,\qquad
 \gamma_j=\frac{m_j}{4\sin((2j+1)\theta)},\qquad
 H_{jk}=\left.\partial_z\partial_w\log K_N(z,w)
                                            \right|_{(c_j,c_k)}.
 \tag{3}
\]
The logarithmic derivative is well defined since
\(K_N(c_j,c_k)\ge1\). In the original crossing normalization,
\((R^n)'(c_j)/R^n(c_j)=in\gamma_j\).

**Theorem 1.** For every level and every pair in (2),
\[
                             H_{jk}\le\gamma_j\gamma_k.
 \tag{4}
\]
The inequality is strict when \(N>2\). At \(N=2\) its
only entry is an equality. No assertion that the entire
matrix \(H\) is positive semidefinite is needed.

The proof has two parts. First, the full normal in the first
kernel variable is expressed by a parameter derivative of
a finite Jacobi determinant, together with the original
endpoint source. Second, that parameter derivative is
positive as a quadratic form.

## 2. An exact normal decomposition

Set
\[
 A(x)=\frac{s_{x+1}^4}{s_{2x+1}s_{2x+2}},\qquad
 C(x)=\frac{s_x^4}{s_{2x}s_{2x+1}},
 \qquad c'(x)=-4\theta\sin((2x+1)\theta).
 \tag{5}
\]
The value \(C(0)=0\) is removable, and \(C'(0)=0\).
Write
\[
 F_j(w)=K_N(c_j,w),\quad
 G_j(w)=\partial_zK_N(c_j,w),\quad Q(w)=G_0(w).
 \tag{6}
\]
Let \(F_j^{(\varepsilon)}\) be the polynomial solution of
\[
 \begin{split}
 F_{-1}^{(\varepsilon)}&=0,\qquad F_0^{(\varepsilon)}=1,\\
 A(r+\varepsilon)F_{r+1}^{(\varepsilon)}
   &=(c_0+A(r+\varepsilon)+C(r+\varepsilon)-w)
                  F_r^{(\varepsilon)}
       -C(r+\varepsilon)F_{r-1}^{(\varepsilon)}.
 \end{split}
 \tag{7}
\]
Only \(0\le r<j\) is used in defining \(F_j^{(\varepsilon)}\).
For \(j\le\lfloor D/2\rfloor\) all these coefficients are
analytic near \(\varepsilon=0\), after removing the zero
in \(C\). At zero, (7) gives the original row \(F_j\).
Define
\[
                 R_j(w)=
                  \left.\partial_\varepsilon
                            F_j^{(\varepsilon)}(w)\right|_0.
 \tag{8}
\]

**Lemma 2.** There are polynomials \(D_j(w)\) such that
\[
 \boxed{\displaystyle
 c'(j)G_j(w)=c'(0)F_j(w)Q(w)+R_j(w)+P_N(w)D_j(w).}
 \tag{9}
\]
Their exact normalization is \(D_0=0\). When \(j\ge1\)
(so \(N\ge3\)), the required remaining polynomials are
given by
\[
 \begin{gathered}
 D_0=0,\qquad
 D_1=\frac{c'(0)}{N^2s_1^2A(0)},\\
 A(r)D_{r+1}
    =(c_0+A(r)+C(r)-w)D_r-C(r)D_{r-1}\quad(r\ge1).
 \end{gathered}
 \tag{10}
\]

*Proof.* The full difference equation, before any spectral
specialization, is
\[
 \begin{split}
 A(x)K_N(c(x+1),w)
   ={}&(c_0+A(x)+C(x)-w)K_N(c(x),w)\\
     &-C(x)K_N(c(x-1),w)
       +\frac{\eta}{N^2}P_N(w)e_D(c(x)).
 \end{split}
 \tag{11}
\]
It is an ordinary polynomial identity, proved from the
Newton recurrence in the cited note.
Differentiate it at \(x=r\). For \(r\ge1\) in the range
needed here, \(e_D(c_r)=e_D'(c_r)=0\).
At \(r=0\), its source derivative is
\[
  \frac{\eta}{N^2}P_N(w)e_D'(c_0)c'(0)
                 =\frac{c'(0)}{N^2s_1^2}P_N(w).
 \tag{12}
\]
The term containing \(K_N(c(x-1),w)\) causes no initial
ambiguity: \(C(0)=C'(0)=0\).
The differentiated recurrence is linear. Its initial
value is \(c'(0)G_0=c'(0)Q\); varying its coefficients
produces \(R_j\); propagating (12) produces exactly (10).
This proves (9), including its sign and all polynomial
terms. \(\square\)

At a double physical root \(w=c_k\), both \(P_N(w)\) and
its first derivative vanish. Dividing (9) by \(F_j\) and
differentiating in \(w\) therefore gives the exact identity
\[
 H_{jk}=\frac{c'(0)}{c'(j)}H_{0k}
              +\frac1{c'(j)}
                       \left(\frac{R_j}{F_j}\right)'(c_k).
 \tag{13}
\]
This is an identity for the full mixed first normal.
It was not obtained by differentiating just the terminating
values of the kernel.

## 3. The shifted Jacobi matrix

Let \(\mathcal J_j(\varepsilon)\) be the real symmetric
\(j\)-by-\(j\) matrix with diagonal
\[
 d(r+\varepsilon)=c_0+A(r+\varepsilon)+C(r+\varepsilon)
    =\frac{2}{\cos((r+\varepsilon)\theta)
               \cos((r+\varepsilon+1)\theta)}
 \tag{14}
\]
and off-diagonal entries
\[
 -B(r+\varepsilon),\qquad
 B(x)=\sqrt{A(x)C(x+1)}
  =\frac{2\sin^3((x+1)\theta)}
   {\cos((x+1)\theta)
    \sqrt{\sin((2x+1)\theta)\sin((2x+3)\theta)}}.
 \tag{15}
\]
The positive square roots are used near \(\varepsilon=0\).
The determinant recurrence gives
\[
 F_j^{(\varepsilon)}(w)=
     \frac{\det(\mathcal J_j(\varepsilon)-wI)}
                         {\prod_{r=0}^{j-1}A(r+\varepsilon)}.
 \tag{16}
\]
The positive finite Jacobi form in the preceding note
shows that \(\mathcal J_j(0)>c_0I\).
Consequently, for every \(w\le c_0\),
\[
 \left(\frac{R_j}{F_j}\right)'(w)
   =\operatorname{Tr}\!\left[
       (\mathcal J_j-wI)^{-1}\mathcal J_j'
                         (\mathcal J_j-wI)^{-1}\right].
 \tag{17}
\]
The normalization in the denominator of (16) has no
\(w\)-dependence. In (17), the matrices and the prime on
\(\mathcal J_j\) are evaluated at \(\varepsilon=0\).

**Lemma 3.** For \(1\le j\le\lfloor D/2\rfloor\),
\[
                             \mathcal J_j'(0)>0.
 \tag{18}
\]

*Proof.* The diagonal entries of the derivative are
\[
 d'(r)=\frac{2\theta\sin((2r+1)\theta)}
               {\cos^2(r\theta)\cos^2((r+1)\theta)}>0.
 \tag{19}
\]
For the edge between rows \(m-1,m\), define its normalized
off-diagonal magnitude
\[
             \rho_m=\frac{B'(m-1)}
                         {\sqrt{d'(m-1)d'(m)}}.
 \tag{20}
\]
Here \(1\le m<j\), so \(N\ge2m+3\).
Put
\[
       u=\sin^2(m\theta),\quad v=1-u,\quad
       a=\sin^2\theta,\quad h=\frac{a}{4uv},\quad
       h_0=\frac1{4m^2}.
 \tag{21}
\]
Direct differentiation of (15) simplifies to
\[
 \begin{split}
 \rho_m
 &=\frac{u(v-a)[8uv-a(1+2v)]}{(4uv-a)^2}\\
 &=\frac{(1-4uh)(2-h(3-2u))}{4(1-h)^2}.
 \end{split}
 \tag{22}
\]
All factors in the first numerator are positive.
For example \(m\theta+\theta<\pi/2\) gives \(v>a\).
Also \(h<1/2\): the condition \(N\ge2m+3\) implies
\(\theta\le\pi/5\) and
\[
 2\theta\le2m\theta\le\pi-3\theta,\qquad
 \sin(2m\theta)\ge\sin(2\theta).
 \tag{23}
\]
The last inequality follows because
\(\sin3\theta\ge\sin2\theta\) in this range.
Thus \(h\le1/(4\cos^2\theta)<1/2\), and
\(8uv-a(1+2v)=4uv[2-h(1+2v)]>0\).

We claim
\[
 0<\rho_m\le
 r_0(h_0):=\frac{2-3h_0}{4(1-h_0)^2}
       =\frac{m^2(8m^2-3)}{(4m^2-1)^2}.
 \tag{24}
\]
For \(u\ge1/6\), subtracting \(1/2\) in (22) gives
the numerator
\[
        h\{(1-6u)-2h(1-6u+4u^2)\}.
 \tag{25}
\]
It is nonpositive. If the second bracket is nonnegative
this is immediate; otherwise \(h<1/2\) bounds the
braced expression above by \(-4u^2\).
Thus \(\rho_m\le1/2<r_0(h_0)\) in this case.

If \(0<u\le1/6\), then \(a\le u\), so \(h\le3/10\).
Since \(\sin\theta\le\theta\) and
\(m\theta\le\tan(m\theta)\),
\[
                         \frac{h_0}{h}\ge(1-u)^2.
 \tag{26}
\]
Also \(0\le r_0'(h)\le1/4\) for \(0\le h\le3/10\).
Equation (22) can be written as
\[
 \rho_m=r_0(h)
       -\frac{uh(3-6h+4uh)}{2(1-h)^2}.
 \tag{27}
\]
By (26), the positive part of \(h-h_0\) is at most
\(2uh\). Therefore
\(r_0(h)-r_0(h_0)\le uh/2\).
The term subtracted in (27) is at least \(3uh/5\).
This proves (24).

Finally
\[
       \frac{m^2(8m^2-3)}{(4m^2-1)^2}
                  <\frac{m}{\sqrt{4m^2-1}}.
 \tag{28}
\]
After squaring the positive sides and clearing factors,
the difference is \(3m^2-1>0\).
Normalize \(\mathcal J_j'\) by its positive diagonal
square root. Its diagonal becomes one and its
off-diagonal entries become \(-\rho_m\).
The positive vector \(v_r=\sqrt{2r+1}\) is a strict
diagonal-dominance vector: for an interior row \(r\),
the larger bounds in (28) give
\[
 \frac{r}{\sqrt{(2r-1)(2r+1)}}v_{r-1}
 +\frac{r+1}{\sqrt{(2r+1)(2r+3)}}v_{r+1}=v_r.
 \tag{29}
\]
The actual coefficients are strictly smaller. At the
first and last rows the missing term only improves the
inequality. Positive diagonal scaling therefore gives a
strictly diagonally dominant real symmetric matrix with
positive diagonal, which is positive definite.
For \(j=1\), (19) proves the result directly.
\(\square\)

This is a finite matrix inequality. It uses the
Askey--Wilson coefficients already identified in the
previous note, but does not import an orthogonality
measure at the colliding root-of-unity parameters.

## 4. Proof of the general mixed-normal bound

For \(j\ge1\), Lemma 3 makes the trace in (17) strictly
positive. Since \(c'(j)<0\), equation (13) gives
\[
 H_{jk}<\frac{c'(0)}{c'(j)}H_{0k}
   =\frac{\displaystyle\sum_{r=k+1}^{N-1-k}\csc^2(r\theta)}
          {16\sin((2j+1)\theta)\sin((2k+1)\theta)}.
 \tag{30}
\]
For \(j=0\), the corresponding equality is the exact
endpoint formula.
By symmetry assume \(j\le k\), hence \(m_j\ge m_k\).
For fixed positive \(m=m_k\), the central sum can be
written as
\[
 \sum_{\ell=0}^{m-1}
   \sec^2\!\left(\frac{\pi}{N}
                   \left(\ell-\frac{m-1}{2}\right)\right).
 \tag{31}
\]
It decreases as \(N\) increases. The smallest possible
level is \(N=m+1\); there the standard full cosecant sum
gives \(m(m+2)/3\). Thus
\[
       \sum_{r=k+1}^{N-1-k}\csc^2(r\theta)
                  \le\frac{m_k(m_k+2)}3
                  \le m_k^2\le m_jm_k.
 \tag{32}
\]
Substitution in (30) proves (4).
When \(j\ge1\), the first inequality in (30) is strict.
When \(j=0\) and \(N>2\), either \(k=0\), where the
endpoint ratio is \((N+1)/(3(N-1))<1\), or
\(m_j=N-1>m_k\), which makes the last comparison strict.
The \(N=2\) endpoint formula gives equality. This proves
Theorem 1.

Only prefixes of length at most \(\lfloor D/2\rfloor\)
were used. Every coefficient in those finite matrices is
regular. No step replaces the singular middle-node
equation by an equation for coincident values.
The full difference identity (11), including its source,
is what justified the differentiated equations.

## 5. The complete normal determinant at every color assignment

Consider a fixed finite path of filled original vertices,
with every signed power satisfying \(n_v\ge2\), or every
power satisfying \(n_v\le-2\). Assign any physical spectral
root at each vertex. Odd simple roots are evaluated first;
their crossing values have modulus one and their removal
leaves a disjoint union of double-root subpaths.
The other factors here are the original edge kernels
between those assigned roots, together with any original
boundary kernels evaluated at the complete value \(-2\).
Their values and spectral derivatives are real, and their
values are at least one. The following scalar lower bound
does not include arbitrary complex uncontracted boundary
amplitudes.

The exact colored determinant formula in
[the grouped-current note](research_grouped_endpoint_current_matchings.md),
Section 5, factors at each double root as follows. Remove
the row factor
\(\eta(4-c_j^2)R^{n_v}(c_j)\).
The diagonal that remains is a real number plus
\(in_v\gamma_j\).
An edge has dimer weight \(H_{jk}\).
Choose its symmetric off-diagonal entries to be
\(i\sqrt{H_{jk}}\) if \(H_{jk}\ge0\), and
\(\sqrt{-H_{jk}}\) if \(H_{jk}<0\).
In both cases the determinant transposition contributes
the required \(+H_{jk}\).

After the common sign is chosen, the imaginary part is
positive definite. Indeed Theorem 1 bounds every
normalized imaginary off-diagonal by one, while the
normalized diagonal has magnitude at least two.
For \(m\ge1\) double-root vertices, let
\[
                        \lambda_m=2-2\cos\frac{\pi}{m+1}.
 \tag{33}
\]
The elementary finite-path comparison gives
\[
                 B\ge\lambda_m\operatorname{diag}(\gamma_j).
 \tag{34}
\]
Negative dimer weights add only real symmetric entries
and cause no difficulty in this inequality.
For any real symmetric \(A\) and positive definite \(B\),
\[
       |\det(A+iB)|\ge\det B.
 \tag{35}
\]
To prove it, conjugate by \(B^{-1/2}\); the resulting
real symmetric matrix has real eigenvalues \(x_\nu\),
and \(\prod_\nu|x_\nu+i|\ge1\).

Since \(\gamma_j\ge N/(4\pi)\) and
\(4-c_j^2\ge16/N^2\), restoring the original row factors
and the positive edge kernel values yields
\[
 \boxed{\displaystyle
 |\text{contribution of any physical color assignment}|
 \ \ge\
 \left(\frac{4\lambda_m}{\pi N}\right)^m
                    \prod_{e=vw}K_N(c_v,c_w).}
 \tag{36}
\]
For \(m=0\), the contribution is its positive kernel
product times a unit, so the same assertion is read
without derivative rows.
Thus the complete first-normal calculation at each
assignment has no exponential cancellation. Both
parities and every original crossing normal are retained.

**Corollary 4 (a positive definite tree).** Let \(G\) be any
fixed finite filled tree with powers of one common sign.
Retain the same real original kernel factors as above.
If
\[
          Q_G=\operatorname{diag}(|n_v|)-\operatorname{Adj}(G)>0,
                  \qquad \lambda_G=\lambda_{\min}(Q_G),
 \tag{36a}
\]
then every physical color assignment with \(m\) double-root
vertices satisfies
\[
 |\text{its full contribution}|
       \ge\left(\frac{4\lambda_G}{\pi N}\right)^m
                          \prod_{e=vw}K_N(c_v,c_w).
 \tag{36b}
\]
No lower bound of two on each individual power is required
in this corollary. Positive definiteness already forces
every \(|n_v|>0\).

To prove it, remove the simple-root vertices. The remaining
graph is a forest and its comparison matrix is a principal
submatrix of \(Q_G\). For any vector \(x\), the normalized
imaginary part has diagonal \(|n_v|\) and off-diagonal
absolute values at most one. Its quadratic form is
therefore at least
\[
  \sum_v |n_v||x_v|^2-2\sum_{vw}|x_v||x_w|
            =|x|^TQ_G|x|
            \ge\lambda_G\|x\|^2,
 \tag{36c}
\]
with zeros inserted at the deleted vertices. The exact
tree determinant has only matching transpositions, so the
same symmetric realization is valid. Equations (35) and
the original row-factor bounds prove (36b).

A simple sufficient condition is
\(|n_v|\ge\deg_G(v)\), with strict inequality somewhere in
each connected component. Indeed the quadratic form of
\(Q_G\) is the sum of \(|x_v-x_w|^2\) over edges and
\((|n_v|-\deg_G(v))|x_v|^2\) over vertices; its only
possible constant zero mode is removed by the strict
inequality. This criterion concerns the filled tree and
does not change any original crossing power or carrier.

**Lemma 5 (relative upper bounds).** Uniformly over the
physical double roots,
\[
 |H_{jk}|\le N^{16},\qquad
 \left|\frac{G_j(w)}{F_j(w)}\right|\le N^{11}
                         \quad(-2\le w\le c_0).
 \tag{36d}
\]
These deliberately coarse powers are independent of
the color indices. For a fixed tree and fixed crossing
powers, they give a polynomial upper bound for the
absolute value of its complete normal determinant
relative to the positive kernel product. Together with
(36b), this bounds that factor both above and below
by powers of \(N\), for each color assignment separately.

Here is a proof retaining the free-variable source.
For \(j\ge1\), write
\(\mathcal R_j(w)=(\mathcal J_j-wI)^{-1}\).
Cramer's rule in (10),(16) gives the exact expression
\[
 \begin{split}
 c'(j)\frac{G_j(w)}{F_j(w)}
  ={}&c'(0)Q(w)+
       \operatorname{Tr}(\mathcal R_j(w)\mathcal J_j')
                -\sum_{r=0}^{j-1}\frac{A'(r)}{A(r)}\\
     &+\frac{c'(0)P_N(w)}{N^2s_1^2}
                                 (\mathcal R_j(w))_{00}.
 \end{split}
 \tag{36e}
\]
In particular \(D_j/F_j=
c'(0)(\mathcal R_j)_{00}/(N^2s_1^2)\).
This identity is holomorphic throughout \(\Re w\le c_0\)
and retains the polynomial source away from the physical
roots.

For explicit bounds, the Jacobi form has mass
\(s_{2r+1}\le2\) and edge conductance
\[
 \frac{s_{r+1}^4}{s_{2r+2}}
       =\frac{s_{r+1}^3}{2\cos((r+1)\theta)}
                         \ge\frac{32}{N^3}.
 \tag{36f}
\]
The elementary one-ended path inequality
\(\sum|v_r|^2\le j^2\sum|v_r-v_{r+1}|^2\), with
\(v_j=0\), yields
\[
 \mathcal J_j-c_0I\ge\frac{16}{N^5}I,\quad
 \|\mathcal R_j(w)\|\le\frac{N^5}{16}
                             \quad(\Re w\le c_0).
 \tag{36g}
\]
Equations (19),(24) imply
\(\|\mathcal J_j'\|\le6\pi N^3\).
Indeed \(\cos(j\theta)\ge\sin(\theta/2)\ge1/N\),
so each diagonal derivative is at most \(2\pi N^3\),
and each off-diagonal is bounded by the geometric mean
of its two diagonal entries.
Also \(|c'(j)|\ge8\pi/N^2\).
Applying these bounds to (13),(17), and using
\(|c'(0)/c'(j)|\le1\), gives
\[
 |H_{jk}|\le\frac{N^4}{64}+\frac{3N^{16}}{1024}
                                                   \le N^{16}.
 \tag{36h}
\]
The case \(j=0\) follows directly from the endpoint bound.

For the other estimate, the full-real-boundary bound
in [the Ward packet theorem](research_signed_gaussian_ward_endpoint_packet.md),
equation (30), implies
\(\|T\Pi_0\|_{[-2,2]}\le3N^2\).
Thus \(|Q(w)|\le N^4/4\) on that interval.
For the regular coefficients used here,
\[
 \left|\frac{A'(r)}{A(r)}\right|\le4\pi,\qquad
 \left|\frac{c'(0)}{N^2s_1^2}\right|
                              \le\frac{\pi}{2N^2}.
 \tag{36i}
\]
Use (36g),(36i), \(|P_N(w)|\le4\), and
\(|c'(0)|\le4\pi/N\) in (36e). After division by
\(|c'(j)|\ge8\pi/N^2\), the resulting bound is at most
\[
                 \frac{3N^{11}}{64}
                      +\frac{9N^5}{64}+\frac{N^3}{2}
                                                   \le N^{11}.
 \tag{36j}
\]
For \(j=0\), it is just the bound for \(Q\).

Finally each diagonal of the normalized determinant is
bounded by a fixed multiple of \(N^{11}\): its real part
is \(-c_j/(4-c_j^2)\) plus the incident logarithmic
kernel derivatives, and its imaginary part is
\(n_v\gamma_j\).
Its symmetric off-diagonal entries have modulus
\(\sqrt{|H_{jk}|}\le N^8\).
Hadamard's inequality therefore supplies the asserted
polynomial upper bound for each fixed tree.
All removed row factors have modulus at most four.
This proves the lemma. \(\square\)

## 6. The remaining coherent sum and complex contours

The exact original scalar source is the sum of the
contributions in (36), with their original crossing
phases and determinant phases. A lower bound for each
summand is not a lower bound for their sum. In particular,
(36) does not identify the coefficient of a geometric
integration cycle.

There is already exponential cancellation in the simplest
eligible negative path. At odd levels, \(z=-2\) is a simple
physical root, and its exact contribution to
\(H_{-2,N}(0)=\phi_N(R^{-2}K_N(z,-2))\) is
\[
                         R^{-2}(-2)K_N(-2,-2).
 \tag{37}
\]
The crossing value has modulus one. The complete
[edge theorem](../papers/circle-tree-volume/edge-packet.tex)
gives its modulus as
\[
             \tfrac14 N^{-3/2}e^{NM_\infty}(1+O(N^{-1})),
             \qquad M_\infty=\frac{4G}{\pi},
 \tag{38}
\]
where \(G\) is Catalan's constant.
The full [two-crossing terminal theorem](research_two_crossing_terminal_filling.md)
instead gives rate \(M_\infty/2\) for \(H_{-2,N}(0)\).
Thus other physical colors cancel the larger exponential
contribution (37), even for a single original power
\(-2\). The bound (36) cannot justify taking absolute
values before summing colors.

The proof also does not give a fixed complex strip on
which \(\partial_z\partial_w\log K_N\) is bounded by
the same expression. There is a source-specific reason
to retain this distinction: the literal diagonal
\(K_N(z,z)\) has complex zeros at distance
\(O(N^{-3/2})\) from the endpoint \(c_0\), as proved in
[the turn-trace density note](research_turn_trace_residue_density.md).
Division by \(K_N\) can therefore introduce poles in
any fixed complex neighborhood of the full physical
interval as \(N\) grows. The unfactored original
polynomial source has no such artificial poles.
An application on a complex contour must either avoid
and control these zeros or use the denominator-free
source identity. The real physical matrix bound above
does not discard the corresponding contour terms.

## 7. Reproduction

Run
~~~sh
python3 experiments/check_all_color_path_normal_bound.py \
  --precision 100 \
  --output repro/results/research-all-color-path-normal-bound.json
~~~
The [standalone script](../experiments/check_all_color_path_normal_bound.py)
checks the rational algebra used in (25), (27), and (28)
symbolically. It then computes the original full Newton
basis through degree \(D\), independently of the shifted
Jacobi recurrence. The saved finite comparisons comprise
128 complex tests of (9), including its polynomial source
term, 2,736 ordered double-root pairs in (4), and 22
positive Jacobi-derivative matrices.
The [100-digit record](../repro/results/research-all-color-path-normal-bound.json)
passed with largest relative discrepancy
\(1.28\cdot10^{-99}\) in the source identity.
The separate [150-digit replay](../repro/results/research-all-color-path-normal-bound-root.json)
repeats all 128 source identities, 2,736 physical pairs and 22
Jacobi matrices; its largest source discrepancy is
\(1.32\cdot10^{-148}\).
The finite tests check normalization and implementation;
the uniform all-level bounds are proved above.
