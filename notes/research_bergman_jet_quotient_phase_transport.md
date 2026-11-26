# Holomorphic phase transport on the original Hermite jet quotient

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 \chi_N=q^{d^2/4},\qquad \eta=(-1)^d .
 \tag{1}
\]
Fractional powers of \(q\) always mean their displayed exponential,
not a newly chosen root of its numerical value. The finite algebra,
Newton normalization, original trace, and signed crossing data are
those of [C]. We construct norms on this same full algebra, retaining
its repeated-root derivatives.

## 1. The domain and the full jet map

Choose \(R>2\) and the fixed slit disk
\[
 D=\{z:|z|<R\}\setminus[2,R).
 \tag{2}
\]
Its physical double nodes are
\(c_a=2\cos((2a+1)\pi/N)\), \(0\le a<\lfloor N/2\rfloor\).
For odd \(N\), there is also the simple node \(-2\).
Let \(J_N f\) list \(f(c_a),f'(c_a)\) at every double node
and the odd simple value. Its target is the \(N\)-dimensional algebra
\[
 \mathcal Q_N=\prod_a\mathbb C[\epsilon_a]/(\epsilon_a^2)
       \quad\text{with an additional \(\mathbb C\) if \(N\) is odd}.
 \tag{3}
\]
This is precisely \(\mathbb C[z]/(P_N)\), by Hermite interpolation.
In particular, the product on (3) retains the derivative product rule.

All nodes lie in \(D\), and their distances to its boundary satisfy
\[
 \operatorname{dist}(c_a,\partial D)
 \ge \min\{R-2,\,4\sin^2(\pi/(2N))\}\ge c_R N^{-2}.
 \tag{4}
\]
The same bound holds for the odd simple node. An arbitrary bounded
domain containing the nodes need not satisfy (4); the explicit choice
(2) is used for the polynomial estimates below.

For \(s\) traced variables use \(D^s\) and the full tensor jet map
\(J_N^{(s)}\). At a product of double nodes it retains every mixed
derivative \(\partial^\alpha\), \(\alpha_v\in\{0,1\}\);
a simple-node slot has only \(\alpha_v=0\). The target has dimension
\(N^s\). Tensor products of the one-variable Hermite polynomials
prove surjectivity on holomorphic functions.

## 2. Minimal weighted representatives

Let \(\Phi\) be any holomorphic function on \(D^s\). Define
\[
 \mathcal H_{\Phi,N}
 =\left\{f\in\mathcal O(D^s):
       \|f\|_{\Phi,N}^2
       :=\int_{D^s}|f|^2e^{-2N\operatorname{Re}\Phi}\,dV<\infty
       \right\}.
 \tag{5}
\]
Multiplication by \(e^{-N\Phi}\) is an onto isometry from this space
to the unweighted Bergman space \(\mathcal H_0=A^2(D^s)\).
Indeed its inverse is multiplication by \(e^{N\Phi}\).
The latter assertion does not require the weight to be bounded.
The unweighted space is complete: local mean-value bounds turn
an \(L^2\)-Cauchy sequence of holomorphic functions into a locally
uniformly convergent sequence with the same \(L^2\) limit.

The holomorphic functions with zero full jets form a holomorphic
ideal \(\mathcal I_N\subset\mathcal O(D^s)\): the mixed Leibniz rule
proves this assertion. Its intersection
\[
 I_{\Phi,N}=\mathcal I_N\cap\mathcal H_{\Phi,N}
             =\ker J_N^{(s)}
 \tag{6}
\]
is a closed Hilbert subspace. We do not treat \(\mathcal H_{\Phi,N}\)
as an algebra or assert that an unbounded product stays in it.
Evaluations and the indicated derivatives are continuous by local
mean-value and Cauchy estimates after the gauge in (5).

The restricted jet map in (6) is onto. Given a target jet \(u\),
multiply it in the finite jet algebra by \(J(e^{-N\Phi})\), choose
its Hermite polynomial \(p\), and take \(e^{N\Phi}p\).
This belongs to (5), since \(D^s\) is bounded and \(p\in A^2(D^s)\).
It has jets \(u\). Consequently the quotient norm
\[
 |u|_{\Phi,N}
   =\inf\{\|f\|_{\Phi,N}:Jf=u\}
 \tag{7}
\]
is a positive Hilbert norm on the entire original algebra
\(\mathcal Q_N^{\otimes s}\).

Here and below \(J=J_N^{(s)}\). Let
\[
 G_0=JJ^*,\qquad S_0=J^*G_0^{-1},\qquad P_0=S_0J
 \tag{8}
\]
in the unweighted space. Surjectivity makes \(G_0\) positive definite.
Orthogonal decomposition by \(\ker J\) proves that \(S_0u\) is the
unique least-norm lift and that \(P_0\) is its orthogonal projection.
Put \(\Gamma_\Phi=M_{J(e^{N\Phi})}\), multiplication in the jet algebra.
It is invertible, including all mixed normal entries. The weighted
section and projection are exactly
\[
 \begin{split}
 S_\Phi u&=e^{N\Phi}S_0\Gamma_\Phi^{-1}u,\\
 P_\Phi f&=e^{N\Phi}P_0(e^{-N\Phi}f),\\
 G_\Phi&=\Gamma_\Phi G_0\Gamma_\Phi^*,\qquad
 |u|_{\Phi,N}^2=u^*G_\Phi^{-1}u .
 \end{split}
 \tag{9}
\]
These formulas prove existence, uniqueness, jet preservation, and
projection norm one, rather than selecting a new polynomial source.

If \(\Phi(z,\lambda)\) and \(u(\lambda)\) depend holomorphically on
ordinary exterior parameters, the first formula (9) is holomorphic
in \((z,\lambda)\). It uses the fixed finite section \(S_0\) and
the holomorphic matrix \(\Gamma_\Phi^{-1}\). Thus exterior derivatives
are retained without differentiating a varying orthogonal basis.
The exterior variables are not themselves quotiented.

## 3. Exact crossing transport

The function
\[
 \tau(z)=\arccos(-z/2)^2
        =4\arcsin\!\left(\sqrt{(z+2)/4}\right)^2
 \tag{10}
\]
is the single holomorphic continuation on
\(\mathbb C\setminus[2,\infty)\) that is real nonnegative on
\([-2,2)\). The square removes the apparent branch at \(-2\):
the last expression has a power series in \(z+2\) there.
Away from that point, if \(t=\arccos(-z/2)\) in its local branch,
\(\tau'=t/\sin t\); this also extends at \(-2\).

For any signed integer \(n\), set
\[
 \theta_n(z)=\frac{in}{4\pi}\tau(z),\qquad
 m_{n,N}(z)=\chi_N^n e^{N\theta_n(z)} .
 \tag{11}
\]
This is a nowhere-zero holomorphic function. It represents the
original \(R^n\) in the full algebra. To check that claim directly,
at the listed double nodes let
\(t_a=\pi(d-2a)/N\). Then
\[
 \begin{split}
 m_{n,N}(c_a)
   &=\kappa^n(-1)^{na}q^{na(a+1)},\qquad
       \kappa=q^{d^2/2},\\
 \frac{m_{n,N}'(c_a)}{m_{n,N}(c_a)}
   &=\frac{in(d-2a)}{4\sin((2a+1)\pi/N)} .
 \end{split}
 \tag{12}
\]
For the first equality, use
\([d^2+(d-2a)^2]/4=d^2/2+a(a+1)-Na\).
For the second use \(dt/dz=1/(2\sin t)\).
These are exactly [C, (5), (21)]. For odd \(N\), \(t=0\) at
the simple node and (12)'s value formula is \(\chi_N^n\);
there is no derivative condition at that node.

It follows pointwise from (5) that multiplication by \(m_{n,N}\)
is an onto isometry
\[
 \mathcal H_{\Phi,N}\longrightarrow
 \mathcal H_{\Phi+\theta_n,N},\qquad
 \|m_{n,N}f\|_{\Phi+\theta_n,N}=\|f\|_{\Phi,N}.
 \tag{13}
\]
It maps the zero-jet subspaces onto each other, with inverse
\(m_{-n,N}\). Hence the actual finite operator \(M_{R^n}\) is an
exact isometry between the quotient norms in (7), and
\[
 P_{\Phi+\theta_n}(m_{n,N}f)=m_{n,N}P_\Phi f .
 \tag{14}
\]
For \(s\) variables this holds with any signed powers \(n_v\),
the multiplier \(\prod_v m_{n_v,N}(z_v)\), and phase increment
\(\sum_v\theta_{n_v}(z_v)\), even when \(\Phi\) is not separable.
The original Jordan blocks have been retained. Equation (13) changes
the norm and does not make them unitary in one fixed positive metric.
Nor does (11) claim equality to the canonical polynomial off its jets.

More generally, if \(b=e^{N\Theta}a\) is holomorphic and
\(\|a\|_\infty\le B\), multiplication gives
\[
 |J(b)u|_{\Phi+\Theta,N}\le B|u|_{\Phi,N}.
 \tag{15}
\]
Apply the ambient bound to the least-norm representative.
An inverse bound follows when \(a^{-1}\) is holomorphic and bounded.
This states the needed product hypothesis; arbitrary holomorphic
spectators need not be bounded multipliers.

## 4. Evaluation bounds and the original closing

For \(g=e^{-N\Phi}f\), product disks of radius comparable to
\(N^{-2}\) at the nodes, the mean-value inequality and Cauchy's
formula give, for each fixed multi-index \(\alpha\),
\[
 |\partial^\alpha g(c)|\le
       C_{\alpha,s,R}N^{2|\alpha|+2s}\|f\|_{\Phi,N}.
 \tag{16}
\]
Thus the gauge-covariant evaluations have polynomial cost, including
the first mixed normals and the endpoint nodes. Ordinary evaluations
extract \(e^{N\Phi(c)}\); ordinary derivative bounds also contain the
explicit derivatives of that gauge. For arbitrary holomorphic
\(\Phi\) those derivatives are not asserted polynomial. For (11)
they are polynomial at the nodes for fixed derivative order and
fixed \(n\): near \(2\), \(\tau^{(k)}=O(|2-z|^{1/2-k})\), and
away from \(2\) they are bounded. In particular
\(N\theta_n^{(k)}(c)=O_n(N^{2k})\) for \(k\ge1\).

Here is the actual original trace, not an arbitrary evaluation.
For a holomorphic germ \(f\) at all nodes, its full Hermite class has
\[
 \phi_N(f)=\eta\sum_a\{(4-c_a^2)f'(c_a)-c_af(c_a)\}
                 +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{17}
\]
Indeed [C, (1)--(2)] imply that \(\phi_N\) extracts the \(e_d\)
coefficient. The polynomial \(e_d\) has leading coefficient
\(\eta/N^2\), since
\(\prod_{j=1}^{N-1}2\sin(\pi j/N)=N\).
The leading coefficient of the Hermite interpolant is the sum of
residues of \(f/P_N\). The Chebyshev differential equation gives,
at a double node,
\[
 P_N''(c_a)/2=N^2/(4-c_a^2),\qquad
 P_N'''(c_a)/(3P_N''(c_a))=c_a/(4-c_a^2).
 \]
At the odd simple node \(P_N'(-2)=N^2\). These identities give
(17), and also the exact Cauchy expression
\[
 \phi_N(f)=\frac{\eta N^2}{2\pi i}
                     \int_{\Gamma_N}\frac{f(z)}{P_N(z)}\,dz,
 \tag{18}
\]
where \(\Gamma_N\subset D\) is the positive union of small circles
around every distinct physical node. Products with attachments and
the Gaussian (11) retain their full derivatives in this formula.
Tensor products give the corresponding original multi-trace.

Write any specified original closing, with its attachment and powers,
as a row \(\ell\) on these full jets. The exact norm of that row is
\[
 \boxed{\ \|\ell\|_{\Phi,N,*}^2=\ell G_\Phi\ell^*
       =\ell\Gamma_\Phi G_0\Gamma_\Phi^*\ell^*.\ }
 \tag{19}
\]
The entries of \(G_0\) are the appropriate holomorphic and
antiholomorphic derivatives of the unweighted Bergman kernel at
the physical nodes. Formula (19) follows either from (9) or by
applying the weighted adjoint of \(J\) to \(\ell^*\). It retains cross terms between
all physical rows and all their normal components.
Under (13), the inverse-dual row
\(\ell_{\rm new}=\ell M_{R^n}^{-1}\) has exactly the old dual norm
and pairs with the transported source to give the same scalar.
This is bilinear source/co-source transport, not replacement of the
original closing by a Hermitian positive expectation.

The finite source compiler [C] can therefore be represented exactly
on these least-norm ranges: an original finite operation \(A\) becomes
\(S_\Psi A J\), and a closing remains \(\ell J\).
Composition is exact because \(JS_\Phi=I\) at each intermediate
stage; no estimate for that composition is being assumed.
At a fully traced variable any replacement with the same full jets
preserves the scalar, including arbitrary original attachment
products and all mixed normals. A free exterior variable remains
ordinary. Bounds for turns or general compositions do not follow
from the crossing isometry alone.

In particular, (19) does not estimate the fixed original row in a
geometric phase norm, prove nonzero overlap, or assemble independently
repaired spectral windows into a global holomorphic representative
with controlled norm. The original exterior and seam terms in (18)
must still be transported or estimated. All statements here concern
an exact phase-adapted representation of the same finite invariant.

## Direct source

[C] [Exact source compilation with arbitrary crossing powers](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md),
SHA256 55e2de84870cfd20dac5922791dbc2bed54909439dfbf4663f17c70a1089445f.
The Gaussian jet calculation, Hilbert-space quotient, and residue
derivation used here are given explicitly above.
