# A full boundary frame from charge-normal values and genuine turns

Written proof, 23 November 2026. Values of an actual boundary packet and
its genuine turn recover every Newton coefficient with polynomial inverse
cost. The observation weights come from the actual charge-normal trace.
An explicit odd-level completion retains the simple-node direction.
The resulting positive metric preserves the turn and both original
closing rows. This is a reconstruction and error estimate, not a lower
bound for the original knot scalar.

## 1. The full source and the completed observations

Fix \(N\ge2\), put \(d=N-1\), \(\gamma=\pi/N\), \(q=e^{i\gamma}\),
and use the complete original algebra and coefficient norm of [G]:
\[
 H_N=\mathbb C[z]/P_N,\qquad P_N(z)=2T_N(z/2)+2,\qquad
 e_k(z)=s_k^{-2}\prod_{h<k}(c_h-z),
\]
\[
 c_h=2\cos((2h+1)\gamma),\qquad
 s_k=\prod_{h=1}^k2\sin(h\gamma),\quad s_0=1,\qquad
 \left\|\sum_{k=0}^d\alpha_ke_k\right\|_{\rm N}^2
       =\sum_{k=0}^d|\alpha_k|^2.
 \tag{1}
\]
Here \(T_N\) is the first Chebyshev polynomial. All repeated-root first
normals belong to \(H_N\). The actual quarter-turn and original closings
satisfy
\[
 Je_k=e_{d-k},\qquad \lambda_0(f)=f(c_0)=\alpha_0,\qquad
 \phi_N(f)=(-1)^dN^2[z^d]\operatorname{rem}_{P_N}f=\alpha_d,
\]
\[
 \phi_N(fg)=\alpha^{\mathsf T}J\beta,\qquad
 \phi_N(f)=\lambda_0(Jf).
 \tag{2}
\]
Here \(g=\sum\beta_ke_k\), and the transpose has no conjugation.
These are the original
normalized source identities, including the actual turn cups and caps.

Put \(r=\lfloor N/2\rfloor\). The distinct double nodes are \(c_j\),
\(0\le j<r\), with positive angles and weights
\[
 \tau_j=\pi-(2j+1)\gamma,\qquad
 w_j=2N^2\tau_j\sin\tau_j.
 \tag{3}
\]
The actual entire charge family of [D] has normal
\(\mathfrak d_N=\partial_\chi\mathcal C_{N,\chi}|_0\), and its exact
full-algebra trace is
\[
 \phi_N(\mathfrak d_NE)=\sum_{j<r}w_jE(c_j).
 \tag{4}
\]
Thus, with \(f^\sharp(z)=\overline{f(\bar z)}\),
\[
 G_D(f):=\phi_N(\mathfrak d_N f^\sharp f)
               =\sum_{j<r}w_j|f(c_j)|^2.
 \tag{5}
\]
This positive form alone is degenerate. Define its full completion by
\[
 \|f\|_{\rm D}^2=G_D(f)+G_D(Jf)
   +\mathbf1_{N\ {\rm odd}}\bigl(|f(-2)|^2+|(Jf)(-2)|^2\bigr).
 \tag{6}
\]
The odd simple-node terms in (6) are specified additional metric rows.
They are not contributions of the charge-normal coupon itself.

**Theorem.** Equation (6) is positive definite on the full \(H_N\), and
\[
 \boxed{\qquad
 \|f\|_{\rm N}\le N^2\|f\|_{\rm D},\qquad
 \|Jf\|_{\rm D}=\|f\|_{\rm D}.
 \qquad}
 \tag{7}
\]
Moreover both original closing rows and their bilinear contraction obey
\[
 |\lambda_0(f)|,\ |\phi_N(f)|\le w_0^{-1/2}\|f\|_{\rm D}
                    \le(2\pi N)^{-1/2}\|f\|_{\rm D},
\]
\[
 \boxed{\qquad
 |\phi_N(fg)|\le N^4\|f\|_{\rm D}\|g\|_{\rm D}.
 \qquad}
 \tag{8}
\]
These estimates use the original normalization of \(\phi_N\). Any
separately recorded closing scalar multiplies the corresponding bound
by its absolute value.

## 2. An explicit polynomial inverse for half of the values

The double nodes are strictly decreasing. Direct factorization gives
\[
 A_{jk}:=e_k(c_j)=
 \begin{cases}
 s_{j+k}/(s_{j-k}s_k^2),&0\le k\le j<r,\\
 0,&k>j.
 \end{cases}
 \tag{9}
\]
Indeed \(c_h-c_j=4\sin((h+j+1)\gamma)\sin((j-h)\gamma)\).
All indices in (9) are less than \(N\). The square matrix \(A\) is
triangular with nonzero diagonal.

Write \(a_u=2\sin(u\gamma)\). Its inverse is exactly
\[
 (A^{-1})_{kj}
   =(-1)^{k-j}
       \frac{a_{2j+1}s_k^2}{s_{k+j+1}s_{k-j}},
       \qquad 0\le j\le k<r.
 \tag{10}
\]
To prove (10), interpolate a polynomial of degree at most \(k\) at
\(c_0,\ldots,c_k\). Its \(e_k\)-coefficient is \((-1)^ks_k^2\) times
the leading interpolation coefficient. The node products have sign
\((-1)^j\) and magnitude
\[
 \left|\prod_{\substack{0\le h\le k\\h\ne j}}(c_j-c_h)\right|
                  =\frac{s_{k+j+1}s_{k-j}}{a_{2j+1}}.
 \tag{11}
\]
This follows by multiplying the two sine factors of every node gap.
It proves every entry in (10), including the boundary \(k=j=0\).

The inverse is polynomially bounded despite the size of some forward
entries. Factoring its magnitude gives
\[
 |(A^{-1})_{kj}|=
 \frac{a_{2j+1}}{a_{k+j+1}}
       \prod_{h=0}^{j-1}\frac{a_{k-h}}{a_{k+h+1}}
       \le\frac N2.
 \tag{12}
\]
For each factor in the product, the two sine indices have sum
\(2k+1<N\), so the numerator is at most the denominator. The remaining
numerator is at most two, and its denominator is at least \(4/N\).
Empty products are one. Consequently
\[
                  \|A^{-1}\|_2\le rN/2\le N^2/4.
 \tag{13}
\]

The weights satisfy
\[
       \min_{j<r}w_j\ge4\pi,\qquad w_0\ge2\pi N.
 \tag{14}
\]
For the first bound use \(\pi/N\le\tau_j\le\pi-\pi/N\). If
\(\tau_j\le\pi/2\), then \(\sin\tau_j\ge2\tau_j/\pi\); otherwise
\(\sin\tau_j\ge2(\pi-\tau_j)/\pi\). The second bound uses
\(\tau_0\ge\pi/2\) and \(\sin(\pi/N)\ge2/N\).

## 3. Reconstruction at both parities

Let \(f=\sum\alpha_ke_k\). Values at the double nodes only see
\(\alpha_0,\ldots,\alpha_{r-1}\), because all later \(e_k(c_j)\)
vanish. Their vector is \(A(\alpha_0,\ldots,\alpha_{r-1})^{\mathsf T}\).
Values of \(Jf\) similarly recover
\(\alpha_d,\ldots,\alpha_{d-r+1}\). Equations (13)--(14) give
\[
 \sum_{k<r}|\alpha_k|^2+
       \sum_{k>d-r}|\alpha_k|^2
       \le\frac{N^4}{64\pi}\{G_D(f)+G_D(Jf)\}.
 \tag{15}
\]
At even \(N=2r\), these are all the coefficients. This proves (7)
in that case.

Suppose \(N=2r+1\). Only the middle coefficient \(\alpha_r\) is missing.
Its recovery from the simple value must retain cancellations. Put
\[
 Q(z)=\prod_{j<r}(z-c_j)
             =U_r(z/2)-U_{r-1}(z/2),
 \tag{16}
\]
where \(U_k(\cos t)=\sin((k+1)t)/\sin t\). The second polynomial is
monic and has the stated roots, since its value at \(z=2\cos t\) is
\(\cos(Nt/2)/\cos(t/2)\). Also \(Q(-2)=(-1)^rN\).

Let \(\ell_j\) be its Lagrange cardinal polynomial at \(c_j\). Direct
differentiation of the last trigonometric expression yields
\[
 \ell_j(-2)=(-1)^{r-j+1}2\sin((2j+1)\gamma/2),
                  \qquad |\ell_j(-2)|\le2.
 \tag{17}
\]
In particular this endpoint extrapolation has no exponential cost.
The root identity \(\prod_{h=1}^{N-1}(1-e^{2\pi ih/N})=N\), paired
into conjugates at odd \(N\), gives \(s_r^2=N\). Since
\(\prod_{j<r}(c_j+2)=N\), one has \(e_r(-2)=1\), while
\(e_k(-2)=0\) for \(k>r\).

The polynomial \(p=\sum_{k<r}\alpha_ke_k\) has the same double-node
values as \(f\). Thus the middle coefficient is explicitly
\[
 \alpha_r=f(-2)-p(-2)
          =f(-2)-\sum_{j<r}\ell_j(-2)f(c_j).
 \tag{18}
\]
Weighted Cauchy--Schwarz and (14),(17) show
\[
 |\alpha_r|^2
 \le\left(1+\sum_{j<r}\frac{|\ell_j(-2)|^2}{w_j}\right)
                          \bigl(|f(-2)|^2+G_D(f)\bigr)
 \le(1+r/\pi)\|f\|_{\rm D}^2.
 \tag{19}
\]
Combining (15),(19), and
\(N^4/(64\pi)+1+r/\pi\le N^4\) for odd \(N\ge3\), proves (7).
The isometry in (7) follows directly from (6) and \(J^2=I\).
Both parities retain every independent coefficient, hence every
physical first normal at the repeated nodes.

## 4. Positive resolution and original-source error bounds

Let \(S_Nf\) be the observation vector in (6), including its square-root
weights and both odd simple rows. Then
\[
 H_N^{\rm obs}=S_N^*S_N\succeq N^{-4}I,\qquad
 \mathcal R_N=(S_N^*S_N)^{-1}S_N^*,\qquad
 \mathcal R_NS_N=I,\qquad \|\mathcal R_N\|_{2\to{\rm N}}\le N^2.
 \tag{20}
\]
The last assertion follows because \(S_N\mathcal R_N\) is the ordinary
orthogonal projection onto the observation range, and (7) bounds its
inverse there. Thus redundant observation data cause no ambiguity.
Equivalently, if \(s_\ell\) are the observation rows and
\(\psi_\ell=(H_N^{\rm obs})^{-1}s_\ell^*\), then
\[
 f=\sum_\ell\psi_\ell(s_\ell f),\qquad
 \|f\|_{\rm D}^2=\sum_\ell|s_\ell f|^2.
 \tag{21}
\]
This is an exact positive frame in the completed metric.
Indeed \(\langle\psi_\ell,f\rangle_{\rm D}=s_\ell f\), so its
rank-one resolution operators are positive for that inner product.

Equation (6) contains \(w_0|f(c_0)|^2\) and
\(w_0|(Jf)(c_0)|^2\). Identities (2) and (14) therefore prove the
closing bounds in (8). Its bilinear bound follows from
\(|\alpha^{\mathsf T}J\beta|\le\|\alpha\|_2\|\beta\|_2\) and (7).
It concerns two separate inputs; no unit bound on a full tensor-product
row is asserted.

In particular the entire boundary error is controlled by
\[
              \|f-\widetilde f\|_{\rm N}
                       \le N^2\|f-\widetilde f\|_{\rm D}.
 \tag{22}
\]
The right side requires both actual value observations and those of
the genuine turned error. It is not supplied by one coherent input,
one physical row, or a positive scalar sum alone.

No upper polynomial bound for \(S_N\), its Gram condition number, or
the full multiplication operator in this metric is claimed. Every
original gate and closing must use the same chosen metric when its
budget is estimated. The theorem does not transfer an earlier budget
or source lower bound from a different metric.

These are auxiliary pair-Casimir samples. They have not been identified
with ordinary main-meridian colors of an assembled knot. Nor does the
charge-normal initializer of [D] provide both sets of observations or a
lower bound for their particular original closing coordinate. Reversed
edges and the simple completion remain explicit. No unit-coupon
continuation, geometric rate, or finite-exception theorem follows.

## Complete proof sources and coverage

Both complete proof inputs were read at matching pins:

- [D] [Actual charge-normal source](research_actual_charge_normal_initializer.md), SHA256 a36b691f41231aee6440a198196d72708b4ce02e6a1f1c248c6aaf40ec032e85.
- [G] [Original endpoint and turn identities](research_conway_global_closing_curvature.md), SHA256 863f170da9a9017aa8b83b1ace44ee3e2c851f57c806c77678b3699e3f2f305f.

D supplies the actual trace (4) and Newton source; G supplies the genuine
turn, both original closings and the Frobenius pairing. The inverse,
odd extrapolation and quantitative completed-frame bounds are proved
above. No off-root quantum-normal differentiation is used.

The complete closest comparisons are
[the uniform physical metric](research_conway_uniform_physical_quartic.md),
SHA256 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8,
and [complete Casimir--Hermite frames](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_complete_casimir_hermite_packet.md),
SHA256 a4e96738a3a093d963fe13cc03585085951fa8699a506ade4e2e7a47c17b3f4c.
They control different physical or spectral coordinate systems. Neither
supplies the joint value-and-genuine-turn reconstruction bound (7).
The interpolation method is elementary; the quantitative conclusion
concerns this specified full source and its original closing.
