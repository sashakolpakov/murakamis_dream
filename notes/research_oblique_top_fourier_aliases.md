# A convergent Fourier expansion on the translated state domains

Private written proof, 18 November 2026.

The exact oblique contour decomposition can be written as a sum
over the integer Fourier charges, each occurring once with coefficient
one, together with its retained relative boundary currents. On each
translated top domain the factorial amplitude is uniformly
nonzero on the entire domain. Charges sufficiently far out in
their respective orthants have an arbitrarily small absolute
exponential bound.

The Fourier integrals are complex and can cancel.
The result supplies neither a nonzero geometric integral nor
cancellation bounds for the relative boundary currents.

The complete proof sources are R, the exact oblique decomposition,
and A, the literal factorial amplitude. Their pins appear below.

## 1. Keep the exact domains and boundary terms

Use R's primitive cut-and-transfer coordinates in dimension
\(m=c+1\), original literal interpolant \(I_N(z)\), and bulk
real chain \(\Omega_N\). Let \(x^*\) be its geometric point,
\(x^0\) its strict real interior point, and
\(\epsilon_j=\operatorname{sgn}\operatorname{Im}x^*_j\).
The positive vector \(a\) is R's generic height vector.

For \(\sigma\in\{\pm1\}^m\), denote the translated top by
\[
 T_{\sigma,N}=
 \begin{cases}
   \Omega_N+N(x^*-x^0),&\sigma=\epsilon,\\
   \Omega_N+iN\sigma a,&\sigma\ne\epsilon .
 \end{cases}
 \tag{1}
\]
Every top has the coordinate orientation inherited from
\(\Omega_N\), before multiplication by
\(c_\sigma=\prod_j(-\sigma_j)\).
Fix the geometric correcting charge \(q\in\mathbb Z^m\), and put
\[
 J_N(z)=e^{-2\pi i q\cdot z}I_N(z),\qquad
 K_{\epsilon_j}(z_j)=\pi\cot(\pi z_j)-i\pi\epsilon_j .
\]
Write \(\mathcal B_N\) for the sum of the three retained
boundary contributions in R's equation (24):
the original boundary-band tori, the initial mixed rectangle
current, and the signed translated side currents.
This is their actual sum of integrals, not an estimated error.
The exact identity is
\[
 K_N=\sum_\sigma\int_{T_{\sigma,N}}
   c_\sigma(2\pi i)^{-m}J_N(z)
                 \prod_jK_{\epsilon_j}(z_j)\,dz+\mathcal B_N .
 \tag{2}
\]
All fixed framing, pivotal and external normalization lines
in R remain unchanged.

## 2. Exact Fourier charges of the polarized kernels

Set
\[
 d_\sigma=\frac{\epsilon-\sigma}{2}\in\mathbb Z^m,
 \qquad q_\sigma=q+d_\sigma .
 \tag{3}
\]
The elementary formula for cotangent proves the meromorphic identity
\[
 c_\sigma(2\pi i)^{-m}\prod_jK_{\epsilon_j}(z_j)
  =\frac{\exp(-2\pi i d_\sigma\cdot z)}
          {\prod_j(1-\exp(2\pi i\sigma_jz_j))}.
 \tag{4}
\]
For one coordinate, when \(\sigma=\epsilon\) its normalized
factor is \(1/(1-e^{2\pi i\epsilon z})\).
When \(\sigma=-\epsilon\), it is
\(e^{-2\pi i\epsilon z}/(1-e^{-2\pi i\epsilon z})\).
These are the four possible sign cases and prove (4),
including the rectangle orientations.

On each top, \(\sigma_j\operatorname{Im}z_j>0\) with a
fixed lower bound proportional to \(N\).
The denominator of (4) therefore has its absolutely
and uniformly convergent geometric expansion. Consequently
(2) becomes
\[
 K_N=
 \sum_{\sigma\in\{\pm1\}^m}\ \sum_{r\in\mathbb Z_{\ge0}^m}
   \int_{T_{\sigma,N}}
       I_N(z)\exp\{-2\pi i(q_\sigma-\sigma r)\cdot z\}\,dz
       +\mathcal B_N .
 \tag{5}
\]
Products such as \(\sigma r\) are coordinatewise.
Uniform absolute convergence on the compact chain at
each fixed \(N\) justifies termwise integration.

The charges in (5) form a disjoint partition of \(\mathbb Z^m\).
In one coordinate, the two sets are
\[
 \{q_j-\epsilon_jr:r\ge0\},
 \qquad
 \{q_j+\epsilon_j(1+r):r\ge0\}.
 \tag{6}
\]
They partition the integers. Taking products proves the
claim. Thus (5) is a genuine complete integer Fourier
expansion, with a specified translated integration domain
for each charge. It is not a collection of independent
unknown lattice-period coefficients.

The geometric charge \(q\) occurs at
\(\sigma=\epsilon,\ r=0\), with coefficient exactly one.
This statement concerns its explicit Fourier integral.
It does not say that a local geometric steepest-descent
cycle occurs in that integral with coefficient one.

## 3. Uniform amplitudes on the whole translated tops

All normalized real domains \(\Omega_N/N\) lie in one fixed
bounded set. On any chosen top, every normalized factorial
length has a fixed nonzero imaginary part, independent of
the real point of that domain. The same holds for the cut
coordinate. Hence the union, over all sufficiently large
\(N\), of the normalized tops has a compact neighborhood
on which every such length lies in
\[
 \mathcal D=\mathbb C\setminus((-\infty,0]\cup[1,\infty)).
 \tag{7}
\]
There are only finitely many tops and factor forms.
This gives simultaneous compact sets, with a separate
neighborhood component when necessary.

A supplies its uniform shifted factorial expansion on
these compact sets. Its chosen branches are fixed on
\(\mathcal D\). The cut binomial has the same global
compact-domain expansion
\[
 \frac{\Gamma(N)\theta^{Ny}(1-\theta)^{N-1-Ny}}
      {\Gamma(Ny+1)\Gamma(N-Ny)}
 =
 N^{-1/2}
 \frac{1-y}{(1-\theta)\sqrt{2\pi y(1-y)}}
 e^{N b_\theta(y)}(1+O(N^{-1})).
 \tag{8}
\]
Here logarithms and square roots are continued from
\(0<y<1\) on (7), and
\[
 b_\theta(y)=-y\log y-(1-y)\log(1-y)
                  +y\log\theta+(1-y)\log(1-\theta).
\]
To prove (8) beyond the small midpoint neighborhood,
apply ordinary Gamma Stirling to \(Ny\) and \(N(1-y)\).
On every compact subset of (7), both arguments remain
in fixed closed sectors away from the negative real axis.
The remainder is uniform. The identity
\(\binom{N-1}{Ny}=(1-y)\binom N{Ny}\) gives the displayed
finite correction. None of its amplitude factors vanish
on the compact sets under consideration.

Multiplying (8), the \(c\) actual crossing expansions,
and their retained monomial and pivotal factors proves
\[
 I_N(Nx)=N^{-(c+1)/2}A_0(x)e^{N\phi(x)}
                              (1+O(N^{-1})),
 \qquad A_0(x)\ne0 .
 \tag{9}
\]
It holds uniformly on the entire normalized top domains
and on fixed neighborhoods of them, with every fixed
holomorphic derivative on smaller neighborhoods.
The phase and units use the original marked factorial
sections. As in R, any explicitly supplied alternative
whole external normalization keeps its prescribed
phase and polynomial power.

In particular each signed top in (2) has uniform density
\[
 N^{m-(c+1)/2}A_0(x)
 e^{N(\phi(x)-2\pi i q_\sigma\cdot x)}
                         (1+O(N^{-1}))\,dx .
 \tag{10}
\]
The remaining denominator in (4) is exponentially close
to one there. Every signed top has leading normalized
kernel coefficient \(+1\); its differing exponential
penalty is part of the explicit integer-alias phase.

## 4. A uniform tail bound for the Fourier charges

Choose \(v_*>0\) such that
\(\sigma_j\operatorname{Im}z_j\ge Nv_*\)
on every top and every coordinate. Put
\[
 C_{\sigma,N}=
 \int_{T_{\sigma,N}}
       |I_N(z)e^{-2\pi iq_\sigma\cdot z}|\,|dz|.
\]
Compactness and (9) give constants \(C,p,C_*>0\),
depending on the fixed braid and selected frame, with
\[
                  C_{\sigma,N}\le C N^p e^{C_*N}.
 \tag{11}
\]
All domains have only polynomial geometric volume.
For \(\gamma=2\pi v_*\), a term of index \(r\) in (5)
has absolute integral at most
\(C_{\sigma,N}e^{-\gamma N|r|_1}\).
Therefore
\[
 \sum_{|r|_1\ge R}
 \left|\int_{T_{\sigma,N}}
 I_N(z)e^{-2\pi i(q_\sigma-\sigma r)\cdot z}\,dz\right|
 \le
 C_{\sigma,N}
 \frac{e^{-\gamma NR/2}}{(1-e^{-\gamma N/2})^m}.
 \tag{12}
\]
For any fixed \(\Lambda>0\), choose a fixed integer \(R\)
with \(\gamma R/2>C_*+\Lambda\). Summing (12) over the
finitely many tops then gives \(O(e^{-\Lambda N})\),
after absorbing the polynomial factor using the strict
inequality. Thus only finitely many Fourier integrals
are needed at any prescribed exponential accuracy.
This is a finite-charge reduction, not a theorem of
finitely many exceptional Dehn fillings.

The finitely many remaining integrals still require
their genuine contour analysis. Their coefficients
being one does not make the integrals nonnegative.
The geometric charge retains its centralizer direction.
Nor has (12) estimated any term in \(\mathcal B_N\).
Those distinctions are essential to the outstanding
volume-conjecture lower bound.

## Complete proof-source pins

* R: notes/research_actual_oblique_geometric_contour_decomposition.md,
  SHA256 9180de472bafb38c479d3e1aafac6c75c388d668371892f54219de658728034c.
* A: notes/research_literal_crossing_slit_chart_amplitude.md,
  SHA256 c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.

The entire matching R was freshly read; the complete unchanged
A read was explicitly retained from the active author sequence.
Every used implication was checked and both matching hashes
renewed. The Fourier partition, global binomial extension
and tail bound are proved here by written calculations.
No mathematical program, numerical test, build, or edit
to frozen or public files was used.
