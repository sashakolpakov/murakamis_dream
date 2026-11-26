# Trace-norm limit of the actual crossing density

20 November 2026. The Gaussian covariance theorem determines the full
normalized density of one actual Newton crossing in trace norm. The
limit is a positive Gaussian integral operator of trace one. It is
mixed: its purity is \(\sqrt{3/7}<1\). Thus an orthonormal change of
basis cannot make this default crossing marginal approach a pure
boundary vector. A compatible change of metric would have to do more.

## 1. The actual density and its scaling

Use the exact full crossing \(T\), covariance \(\mathcal C=TT^*\),
and explicit diagonal unitary \(U\) from
[the Gaussian covariance theorem](research_actual_newton_crossing_gaussian_covariance.md).
That theorem retains the original Cartan scalar, complete Newton
algebra, and the original two closing rows. Write
\[
 K=U^*\mathcal CU,\quad
 B(x)=J(x)-2J(x/2),\quad
 J(x)=\int_0^x\log(2\sin\pi t)\,dt.
\]
Let \(v_3=3\Lambda(\pi/3)\), where
\(\Lambda(\theta)=-\int_0^\theta\log(2\sin t)dt\).
The full trace has the asymptotic
\[
 \boxed{\quad Z_N:=\operatorname{tr}\mathcal C
       =\frac1{\sqrt3}e^{2Nv_3/\pi}(1+o(1)).\quad}     \tag{1}
\]

For \(0\leq i<N\), put
\[
 u_{N,i}=\frac{i-2N/3}{\sqrt N},\qquad h_N=N^{-1/2},
 \qquad I_{N,i}=[u_{N,i}-h_N/2,u_{N,i}+h_N/2).
\]
The map
\[
 V_Ne_i=N^{1/4}\mathbf1_{I_{N,i}}
\]
is an isometry from \(\mathbb C^N\) into \(L^2(\mathbb R)\).
Define the positive trace-one operator
\[
 \rho_N=V_N\frac{K}{Z_N}V_N^*.                       \tag{2}
\]
Its integral kernel on \(I_{N,i}\times I_{N,j}\) is
\(\sqrt N K_{ij}/Z_N\), and is zero off the union of these cells.

**Theorem.** In trace norm on \(L^2(\mathbb R)\),
\[
 \boxed{\quad\rho_N\longrightarrow\rho_\infty,\quad}  \tag{3}
\]
where \(\rho_\infty\) has kernel
\[
 \rho_\infty(u,v)=\frac{3^{1/4}}{\sqrt2}
   \exp\!\left[-\frac{5\pi}{4\sqrt3}(u^2+v^2)
                          +\frac\pi{\sqrt3}uv\right]. \tag{4}
\]
This is a limit of the complete crossing density, not a selected
matrix entry or a truncated covariance block.

## 2. Trace and concentration

The elementary derivatives
\[
 B'(x)=\log(2\cos(\pi x/2)),\qquad
 B''(x)=-\frac\pi2\tan(\pi x/2)
\]
show that \(B\) has its unique maximum at \(x_*=2/3\), with
\[
 B(x_*)=v_3/\pi,\qquad B''(x_*)=-\pi\sqrt3/2.
\]
The direct source proves, uniformly on compact subintervals of
\((0,1)\),
\[
 \mathcal C_{ii}
 =\sqrt{\frac{\cot(\pi x/2)}{2N}}e^{2NB(x)}(1+o(1)),
 \qquad x=i/N.                                      \tag{5}
\]
Its endpoint-uniform factorial bound also gives
\(\mathcal C_{ii}\leq N^C e^{2NB(i/N)}\) for a fixed \(C\),
at all indices. Indeed the row contains at most \(N\) terms and
its positive factorial action is maximized at its middle index.

Outside any fixed neighborhood of \(x_*\), uniqueness of the
maximum and this last bound make the summed contribution
exponentially smaller than \(e^{2NB(x_*)}\). In a fixed interior
neighborhood, (5) and strict negative curvature give a uniform
Gaussian bound in \(u_{N,i}\). Ordinary lattice Laplace summation
therefore gives
\[
\begin{split}
 Z_Ne^{-2NB(x_*)}
 &\longrightarrow
 \frac1{\sqrt{2\sqrt3}}
       \int_{\mathbb R}e^{-\pi\sqrt3 u^2/2}du
 =\frac1{\sqrt3}.
\end{split}
\]
This proves (1). The same argument gives tightness of the diagonal
density \(d_N(u)=\rho_N(u,u)\):
\[
 \lim_{R\to\infty}\limsup_{N\to\infty}
           \int_{|u|>R}d_N(u)du=0.                  \tag{6}
\]
The cell displacement is at most \(h_N/2\) and changes none of
these bounds.

On every fixed compact set of \((u,v)\), the direct source's
uniform mixed-kernel theorem applies with
\(a=(i+j)/(2N)\to2/3\) and
\((i-j)/\sqrt N\to u-v\). Its normalized correlation is
\(\exp[-\pi(u-v)^2/(2\sqrt3)]\). Multiplying by the square
root of the two diagonal limits and using (1) gives (4), uniformly
on compact sets. In particular the coefficient and both quadratic
terms in (4) come from the actual mixed phase, not only the absolute
factorial envelope.

## 3. Positivity, Hilbert--Schmidt convergence, and trace norm

First the proposed limit is positive and trace class. Put
\(a=5\pi/(4\sqrt3)\), \(b=\pi/\sqrt3\), and
\(c=3^{1/4}/\sqrt2\). Expanding
\[
 c e^{-a(u^2+v^2)}e^{buv}
 =c\sum_{n=0}^\infty\frac{b^n}{n!}
          (u^ne^{-au^2})(v^ne^{-av^2})
\]
expresses the kernel as a sum of positive rank-one operators.
Their trace sum is the integral of the diagonal, by monotone
convergence, and equals
\[
 c\int_{\mathbb R}e^{-(2a-b)u^2}du=1.
\]
The series therefore converges in trace norm to a positive trace-one
operator with kernel (4).

Positivity of each finite covariance gives the kernel inequality
\[
 |\rho_N(u,v)|^2\leq d_N(u)d_N(v)
\]
almost everywhere. Hence its squared Hilbert--Schmidt mass outside
\([-R,R]^2\) is at most \(2\int_{|u|>R}d_N(u)du\).
The corresponding limit has Gaussian tails. Compact uniform kernel
convergence, (6), and this inequality give
\[
                 \|\rho_N-\rho_\infty\|_2\to0.        \tag{7}
\]

Here is the stronger trace-norm argument. Given \(\epsilon>0\),
choose a finite-rank orthogonal projection \(P\) with
\(\operatorname{tr}((I-P)\rho_\infty)<\epsilon\); positivity
and trace class provide such a projection. Put \(Q=I-P\).
By (7), \(P\rho_NP\to P\rho_\infty P\) in trace norm on this
fixed finite-dimensional range. Since all total traces are one,
\(\operatorname{tr}(Q\rho_N)<2\epsilon\) for sufficiently
large \(N\). For every positive trace-one operator \(A\),
\[
 \|PAQ\|_1\leq\|PA^{1/2}\|_2\|A^{1/2}Q\|_2
 =\sqrt{\operatorname{tr}(PA)\operatorname{tr}(QA)},
\]
and consequently
\[
 \|A-PAP\|_1\leq2\sqrt{\operatorname{tr}(QA)}
                                  +\operatorname{tr}(QA).
\]
Apply this to \(A=\rho_N,\rho_\infty\), and use convergence
of their finite-rank blocks. Letting \(\epsilon\downarrow0\)
proves (3).

## 4. A fixed amount of mixing survives every unitary basis change

A direct two-variable Gaussian integral gives
\[
 \operatorname{tr}(\rho_\infty^2)
 =c^2\frac\pi{\sqrt{(2a)^2-b^2}}
 =\sqrt{\frac37}.                                    \tag{8}
\]
Trace-norm convergence and operator norms at most one imply
\(\operatorname{tr}(\rho_N^2)\to\sqrt{3/7}\). In particular
\[
 \lambda_{\max}(\rho_N)\leq(3/7)^{1/4}+o(1).
\]
For every unit vector \(f_N\), the trace-zero Hermitian difference
\(\rho_N-|f_N\rangle\langle f_N|\), tested on the projection
\(|f_N\rangle\langle f_N|\), yields
\[
 \boxed{\quad
 \|\rho_N-|f_N\rangle\langle f_N|\|_1
 \geq2[1-(3/7)^{1/4}]+o(1)>0.
 \quad}                                                   \tag{9}
\]
The \(o(1)\) is uniform in the unit vector. The same bound holds
after any unitary conjugation of the density, since its eigenvalues
and purity are unchanged.

This is a statement about the default complete-Newton crossing
marginal. It does not rule out nonunitary matrix gauges. In a
bilinear gluing, an edge change of orthonormal coordinates acts by
\(W\) at one end and \(\overline W\) at the other. It preserves
the trace distance between one density and the transpose of the
other. One cannot apply the same independent chirp at both ends
and infer improved balance from their separate Gaussian limits.

The actual main-color energy includes a different root tensor and
all its main-color representations. No identity with that energy,
or with the original scalar after a fixed short tangle, is asserted
here. The new result provides full trace-norm data for one actual
crossing; compatible gluing metrics and the original boundary
projection still require a further argument.

## Direct source and written proof check

The author read the complete matching-final source
[Gaussian and endpoint kernels](research_actual_newton_crossing_gaussian_covariance.md),
SHA-256 `ce2b1b8efbbcffa8bafe0d0de4f7ce12febf193e433d8e3291f7d2a8c826fa3f`.
The trace concentration, positive-series construction, finite-rank
upgrade and mixing estimate are proved explicitly above. No
mathematical program, test, build or numerical sample was used.
