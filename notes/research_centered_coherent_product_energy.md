# The full output of two centered coherent inputs

Written research proof, 22 November 2026.

The product of two specified centered geometric-series packets has an
exact positive norm sum. On every compact complex input bidisk this sum
has one positive nondegenerate Laplace maximum. It gives a uniform norm
asymptotic, concentration of the entire output, and a complex Gaussian
approximation in the full Newton coefficient norm.

The proof uses the actual finite wall products, including both endpoint
rows. It is a forward estimate for this family of two inputs. It is not
a theorem for arbitrary packets or an arbitrary Conway component.

## 1. Inputs, wall products, and the exact output

Use the full original algebra and centered basis of the
[compiler](research_centered_fourier_conway_compiler.md):
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad\kappa=q^{d^2/2},\quad
 \mathcal H_N=\mathbb C[s]/(2T_N(s/2)+2).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind.
The positive norm makes both the original Newton basis \(e_j\) and
the centered basis \(f_a\) orthonormal. It is not the uniform physical
Hilbert--Schmidt metric. All spectral first normals remain in
\(\mathcal H_N\).

For \(t\in\mathbb D=\{|t|<1\}\), put
\[
 Z_N(t)=\sum_{a=0}^d|t|^{2a},\qquad
 u_N(t)=Z_N(t)^{-1/2}\sum_{a=0}^d t^af_a,\qquad
 w_N(y,z)=u_N(y)u_N(z).
 \tag{2}
\]
Thus the inputs have norm one. These are centered coefficient packets,
not the binomial coherent states of the physical head representation.
Write
\[
 C_{abc}=\phi(f_af_bf_c),\qquad
 \mathcal C_N(x,y,z)=\sum_{a,b,c=0}^dC_{abc}x^ay^bz^c,
 \quad D_N(t)=1-\eta t^N,\quad X_j=-qQ^j.
\]
The original Frobenius pairing is \(\phi(f_af_b)=\delta_{ab}\),
so these are the actual multiplication coefficients.

The complete [wall-source theorem](research_centered_tensor_wall_cauchy_source.md)
gives, at every level and \(0\le j<N\),
\[
 \mathcal C_N(X_j,y,z)
   =\frac{\kappa}{\sqrt N}D_N(y)D_N(z)H_{N,j}(y,z),
 \quad
 H_{N,j}=
 \frac{(Q;Q)_j(Qyz;Q)_j}
 {(-qy;Q)_{j+1}(-qz;Q)_{j+1}}.
 \tag{3}
\]
Every factor is nonzero for \(y,z\in\mathbb D\).
The points \(X_j\) are distinct Fourier sampling points, not a
replacement of the full Casimir algebra by distinct-root values.

Let \(w_{N,c}\) be the centered coefficients of \(w_N\).
Its generating polynomial is
\(\mathcal C_N(x,y,z)/\sqrt{Z_N(y)Z_N(z)}\).
Finite Fourier Parseval therefore gives the exact positive energy
\[
 \boxed{\quad
 \|w_N(y,z)\|^2
 =\frac{|D_N(y)D_N(z)|^2}{N^2Z_N(y)Z_N(z)}
                        \sum_{j=0}^d|H_{N,j}(y,z)|^2.
 \quad}
 \tag{4}
\]
Indeed its degree in \(x\) is less than \(N\), and multiplication of
the \(N\)-th-root grid by \(-q\) preserves Fourier orthogonality.

There is a stronger exact interpretation of the samples. If
\(\alpha_{N,j}\) are the Newton coefficients of the output, the
compiler matrix gives
\[
 \boxed{\quad
 \alpha_{N,j}
   =\frac{\kappa(-q)^j}{\sqrt{N Z_N(y)Z_N(z)}}
                            \mathcal C_N(X_j,y,z)
   =\frac{\kappa^2(-q)^jD_N(y)D_N(z)}
                  {N\sqrt{Z_N(y)Z_N(z)}}H_{N,j}.
 \quad}
 \tag{5}
\]
In fact \(U_{ja}=\kappa(-q)^jX_j^a/\sqrt N\). Thus the
concentration proved below concerns the full actual output vector,
up to an explicitly given unitary change of coordinates.

## 2. The rate has exactly one maximum

Put \(v=e^{2\pi iu}\), \(0<u<1\), and define
\[
 \mathcal R(v;y,z)=
       \frac{(1-v)(1-yzv)}{(1+yv)(1+zv)},\qquad
 E(u;y,z)=2\int_0^u\log|\mathcal R(e^{2\pi is};y,z)|\,ds .
 \tag{6}
\]
Its endpoint logarithms are integrable. In particular \(E\) extends
continuously to \([0,1]\). All assertions below are uniform on
\(|y|,|z|\le r<1\).

There are exactly two solutions of \(|\mathcal R(v)|=1\) on the
unit circle. Their parameters satisfy
\[
 0<u_-<u_*<1,\qquad
 E'<0\text{ on }(0,u_-),\quad
 E'>0\text{ on }(u_-,u_*),\quad
 E'<0\text{ on }(u_*,1).
 \tag{7}
\]
Both crossings are simple. Moreover
\[
 E(0)=E(1)=0,\qquad E_*:=E(u_*)>0,\qquad
                     a_*:=-E''(u_*)>0.
 \tag{8}
\]

Here is an elementary proof valid for complex \(y,z\).
Set \(a=(1+y)(1+z)\), \(D(v)=(1+yv)(1+zv)\), and
\[
 K=|a|^2-2\Re\{a(\bar y+\bar z)\},\qquad
 L=a+\bar a\,yz.
\]
Since \((1-v)(1-yzv)=D(v)-av\), on \(|v|=1\) one has
\[
 |D(v)|^2\bigl(|\mathcal R(v)|^2-1\bigr)
                            =K-2\Re(Lv).
 \tag{9}
\]
At \(v=1\) this is \(-|a|^2<0\).
On the other hand,
\[
 \int_0^1\log|\mathcal R(e^{2\pi iu})|\,du=0.
 \tag{10}
\]
For the three regular factors this follows by integrating their
convergent logarithm series; the same identity for \(1-v\) follows
by an integrable boundary limit, or the elementary log-sine integral.
The logarithm is negative on a nonempty interval near \(v=1\),
so it must be positive somewhere else. Thus the single cosine in
(9) has negative and positive values. It has precisely two simple
zeros, with one positive arc which does not contain \(v=1\).
This proves (7), and (10) proves the two endpoint values in (8).
The last decreasing interval forces \(E(u_*)>E(1)=0\);
the downward simple crossing gives \(E''(u_*)<0\).

The roots, \(E_*\), and \(a_*\) depend continuously on the complex
parameters viewed as real coordinates. Compactness then gives uniform
separation of the two roots from each other and from \(0,1\), a positive
lower bound for \(E_*,a_*\), and uniform derivative bounds near \(u_*\).
For every fixed \(\epsilon>0\), uniqueness also gives a uniform gap
between \(E_*\) and \(E(u)\) on \(|u-u_*|\ge\epsilon\).

## 3. Bulk amplitude and the full norm asymptotic

Use midpoint labels \(u_j=(j+1/2)/N\), and put
\[
 B(u;y,z)=[(1-yz)(1+ye^{2\pi iu})(1+ze^{2\pi iu})]^{-1/2},
 \qquad b(u;y,z)=|B(u;y,z)|^2.
 \tag{11}
\]
Branches are one at \(y=z=0\). In particular \(B\) is nonzero
and all its required bulk derivatives are uniformly bounded.
The wall-source theorem, including its original complex phase,
implies on each fixed bulk interval
\[
 |H_{N,j}|^2
       =N\,b(u_j;y,z)e^{NE(u_j;y,z)}(1+O(N^{-1})).
 \tag{12}
\]
One can also read the rate directly from (3). If
\(J(u)=\int_0^u\log(2\sin\pi s)\,ds\), it is
\[
 \frac{E(u)}2=J(u)+
  \int_0^u\log\left|
       \frac{1-yze^{2\pi is}}
            {(1+ye^{2\pi is})(1+ze^{2\pi is})}\right|ds .
 \tag{13}
\]
This proves agreement with (6), with no adjustable additive constant.

We need global control before applying a local Laplace estimate.
The exact same products give
\[
 \bigl|\log|H_{N,j}|-\tfrac N2E(u_j)\bigr|
                                      \le C_r\log N
                    \quad(0\le j<N).
 \tag{14}
\]
For a direct endpoint-uniform justification,
\(\log(2\sin\pi s)-\log s-\log(1-s)\) has a continuously
differentiable extension to \([0,1]\). Integral comparison for the two
logarithms and the bounded Riemann-sum error for the remainder show
\(\log|(Q;Q)_j|=NJ(j/N)+O(\log N)\), uniformly even at \(j=0,d\).
Moving \(j/N\) to \(u_j\) costs another \(O(\log N)\).
All other logarithms in (3) have uniformly bounded first derivatives
on the entire interval for \(|y|,|z|\le r\); their sum errors are
bounded. This proves (14), retaining both finite endpoints.

Let \(B_*=B(u_*;y,z)\). The full output norm is
\[
 \boxed{\quad
 \|w_N(y,z)\|^2=
 \frac{|D_N(y)D_N(z)|^2}{Z_N(y)Z_N(z)}
 |B_*|^2\sqrt{\frac{2\pi}{a_*N}}\,
                         e^{NE_*}(1+O_r(N^{-1})).
 \quad}
 \tag{15}
\]
In particular \(N^{-1}\log\|w_N\|\to E_*/2>0\), uniformly
on compact input bidisks.

For proof, the global gap and (14) make all rows outside one fixed
bulk neighborhood exponentially small compared to \(e^{NE_*}\),
with at most a polynomial factor. Inside, substitute (12).
Uniform real Laplace expansion gives
\[
 \int b(u)e^{NE(u)}\,du
   =b_*\sqrt{\frac{2\pi}{Na_*}}e^{NE_*}(1+O_r(N^{-1})).
 \tag{16}
\]
The usual error estimate follows by Taylor expansion on a symmetric
fixed neighborhood of \(u_*\): the terms of odd Gaussian degree
integrate to zero and the next even terms have relative order \(N^{-1}\).
All derivatives and Gaussian bounds are uniform by Section 2.

The midpoint sum has the same relative error. Insert a smooth cutoff
equal to one near every possible \(u_*\). For
\(f_N=b e^{NE}\) times this cutoff, midpoint quadrature gives
\[
 \left|\frac1N\sum_j f_N(u_j)-\int f_N(u)\,du\right|
        \le C N^{-2}\int|f_N''(u)|\,du
        \le C_rN^{-3/2}e^{NE_*}.
 \tag{17}
\]
The first inequality follows by integrating the second-order Taylor
remainder on each mesh cell. The second follows from
\(|E'|\le C|u-u_*|\), \(E\le E_*-c|u-u_*|^2\) near
the maximum; the cutoff derivatives lie in a fixed gapped region.
Comparison with (16) proves a relative \(O(N^{-1})\) error.
Finally combine the extra factor \(N\) in (12), the factor \(N\)
from summation, and \(N^{-2}\) in (4). This proves (15).

## 4. Concentration and an actual complex Gaussian output

The entire output probability in Newton coordinates is exactly
\[
 \mu_{N,j}=\frac{|\alpha_{N,j}|^2}{\|w_N\|^2}
         =\frac{|H_{N,j}|^2}{\sum_h|H_{N,h}|^2}.
 \tag{18}
\]
For each fixed \(\epsilon>0\), (7), (14), and (15) give
\[
 \sum_{|u_j-u_*|\ge\epsilon}\mu_{N,j}
                         \le C_{r,\epsilon}e^{-c_{r,\epsilon}N}.
 \tag{19}
\]
Polynomial factors have been absorbed by decreasing the positive
exponential gap. In the scale
\(s_j=(j+1/2-Nu_*)/\sqrt N\), the limiting density is
\[
                 \sqrt{\frac{a_*}{2\pi}}e^{-a_*s^2/2}.
 \tag{20}
\]
For example, the discrete local probabilities are this density times
\(N^{-1/2}(1+o(1))\), uniformly for bounded \(s_j\).

The original complex phase also gives a full-vector approximation.
Define its fixed branch on \(0<u<1\) by
\[
 \begin{split}
 \mathcal F(u;y,z)={}&J(u)+\frac{i\pi}{2}(u^2-u)\\
 &+\int_0^u\{\log(1-yze^{2\pi is})
       -\log(1+ye^{2\pi is})-\log(1+ze^{2\pi is})\}\,ds .
 \end{split}
 \tag{21}
\]
The regular logarithms use their power-series branches. Thus
\(2\Re\mathcal F=E\), with the exact factorial phase retained.
The complex wall theorem is, equivalently,
\[
 H_{N,j}=\sqrt N\,\xi_N B(u_j;y,z)e^{N\mathcal F(u_j;y,z)}
                           (1+O_r(N^{-1})),\qquad
             \xi_N=e^{i\pi/4-\pi i/(8N)}
 \tag{22}
\]
on fixed bulk intervals. This is the already calibrated midpoint
phase, not an inference from the absolute-value formula.

Put \(\delta_j=j+1/2-Nu_*\), \(\vartheta_*=\Im\mathcal F'(u_*)\),
and \(F_{2,*}=\mathcal F''(u_*)\), so that
\(\Re F_{2,*}=-a_*/2<0\). The explicit unit vector
\[
 g_{N,j}=\mathcal Z_N^{-1/2}(-q)^j
       \exp\left\{i\vartheta_*\delta_j+
                         \frac{F_{2,*}\delta_j^2}{2N}\right\},
 \qquad
 \mathcal Z_N=\sum_{j=0}^d e^{-a_*\delta_j^2/(2N)}
 \tag{23}
\]
satisfies
\[
 \boxed{\qquad
 \left\|\frac{(\alpha_{N,j})_j}{\|w_N\|}
                      -\lambda_N(g_{N,j})_j\right\|_{\ell^2}
                         =O_r(N^{-1/2}),\qquad}
 \tag{24}
\]
where the known unit phase is
\[
 \lambda_N=
 \frac{\kappa^2D_N(y)D_N(z)\xi_N B_*}
      {|\kappa^2D_N(y)D_N(z)\xi_N B_*|}
                            e^{iN\Im\mathcal F(u_*)}.
 \tag{25}
\]

To prove (24), use (5) and (22) in a bulk neighborhood.
The real part of \(\mathcal F'(u_*)\) is zero. Taylor expansion
therefore gives the linear and quadratic terms in (23), with error
\(O(|\delta_j|^3/N^2)\) in the exponent and
\(O(|\delta_j|/N)\) in \(B/B_*\).
On \(|\delta_j|\le N^{1/2+\gamma}\), \(0<\gamma<1/6\),
the squared error is bounded by \(C/N\) times a fixed polynomial
in \(|s_j|\) against a uniform Gaussian.
Summing these Gaussian moments gives the \(O(N^{-1/2})\) norm
error. The intervening bulk tails are \(e^{-cN^{2\gamma}}\),
and (14) controls the remaining full interval with a fixed gap.
The same Gaussian sum shows
\(\mathcal Z_N=\sqrt{2\pi N/a_*}(1+o(1))\).
Normalizing the approximating vector and the actual output changes
the estimate by at most the same norm error, and fixes its phase
as (25). This proves the assertion with all finite rows retained.

## 5. Exact endpoints, scope, and coverage

Both original closing functionals are explicit. The compiler gives
\(m(e_j)=\delta_{j0}\) and \(\phi(e_j)=\delta_{jd}\).
Using the two exact wall endpoints in (3) yields
\[
 \boxed{\begin{aligned}
 m(w_N)&=\frac{\kappa^2D_N(y)D_N(z)}
 {N\sqrt{Z_N(y)Z_N(z)}(1+qy)(1+qz)},\\
 \phi(w_N)&=\frac{\sum_{a=0}^d(yz)^a}
                         {\sqrt{Z_N(y)Z_N(z)}}.
 \end{aligned}}
 \tag{26}
\]
The second identity also follows directly from
\(\phi(f_af_b)=\delta_{ab}\). These closings remain bounded on
compact bidisks while the internal output norm has the positive
exponential rate in (15). Consequently the norm and Gaussian
approximation do not supply a scalar closing lower bound.

The result estimates the actual forward product of the two packets
(2) in the original centered/Newton coefficient metric. It does not
put an arbitrary incoming packet, a geometric short component, or
every physical binomial coherent input into this family. No uniform
positive conditioning of the full multiplication map or its
\(MM^*\) factor is proved. Composition through arbitrary further
turns and branching, or a filled-knot geometric action, remains
outside the theorem.

The complete proof directs are:

| Source | SHA-256 |
|---|---|
| [Exact wall source and complex bulk amplitude, 366 lines](research_centered_tensor_wall_cauchy_source.md) | 3cda6a170c46abf27a1c8c15b110780ebcb6017a5aa18758a4e51ba0a271892c |
| [Centered compiler and original closures, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

Both complete matching texts were read. The full crossing-covariance
note and the centered prism-transport notes were also checked for
coverage; they concern different inputs or scalar source evaluations,
not this whole-output norm and its single-cosine Laplace maximum.
General bilinear and Poisson kernels for Al-Salam--Chihara polynomials
are standard; see Ismail--Stanton,
[Classical Orthogonal Polynomials as Moments, Section 4](https://www-users.cse.umn.edu/~stant001/PAPERS/opmom.pdf),
Theorem 4.2 and equation (4.7), for primary coverage. No generic
orthogonality theorem or root-of-unity specialization from that paper
is a premise. Parseval, Laplace asymptotics, and Gaussian concentration
are standard methods. The source-specific assertion here is the
compact-complex full-output estimate for the original finite tensor,
with its phases, endpoints and full Hermite algebra retained.

Only written mathematics and text operations were used. Earlier finals
and public manuscripts remain unchanged.
