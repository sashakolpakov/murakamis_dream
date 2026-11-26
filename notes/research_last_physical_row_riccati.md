# Riccati transport through the last physical row

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The absolute normalization of the physical Newton rows extends to
their last row. At odd levels this last row is the complete color
\(-2\). Consequently the complete-end kernel itself has the geometric
exponential rate, with a nonzero holomorphic factor of polynomial
size, on every compact subset of the free-color half-plane
\(\Re w<2\).

This result estimates the coherent finite polynomial. An individual
Newton summand can have a larger exponential rate there. At even
levels the last physical color is different from \(-2\), and the
conclusion about the complete-end kernel requires a separate argument.

## 1. Original rows and the assertion

Use the original rows
\[
 F_{j,N}(w)=K_N(c_j,w),\qquad
 c_j=2\cos((2j+1)\theta),\qquad
 \theta=\pi/N,\qquad J_N=\lfloor(N-1)/2\rfloor .
 \tag{1}
\]
In particular \(F_{0,N}=1\). For \(0\le r<J_N\), their exact recurrence is
\[
 \rho_{r+1}=1+d_r+q_r(1-\rho_r^{-1}),\qquad
 \rho_r=F_{r,N}/F_{r-1,N},\qquad
 d_r=(c_0-w)/A_r,
 \tag{2}
\]
where the term involving \(\rho_0\) is absent, and
\[
 A_r=\frac{s_{r+1}^4}{s_{2r+1}s_{2r+2}},\qquad
 q_r=\frac{C_r}{A_r},\qquad
 s_r=2\sin(r\theta).
 \tag{3}
\]
The original positive Jacobi realization proves that every row is
nonzero for \(\Re w<c_0\), and
\(\Re\rho_r>1\) there. These facts and the bulk estimates are proved in
[the physical-row transport note](research_physical_row_riccati_transport.md).

Set
\[
 \lambda(x,w)=
 \exp\!\left(2\operatorname{asinh}
             \left(\frac{\sqrt{2-w}}2\cot(\pi x)\right)\right),
 \qquad 0<x<1/2 .
 \tag{4}
\]
The square root has positive real part. Thus \(\Re\lambda>1\), and the
logarithm in (4) is the one continued from real \(w<2\).

**Theorem 1.** Fix \(\gamma>0\) and \(R<\infty\). Uniformly for
\[
                 \Re w\le2-\gamma,\qquad |w|\le R,
 \tag{5}
\]
and all sufficiently large \(N\),
\[
 \boxed{\quad
 \sum_{r=1}^{J_N}\Log\rho_r(w)
     =N\int_0^{J_N/N}\Log\lambda(x,w)\,dx+O(\log N).
 \quad}
 \tag{6}
\]
Each ratio logarithm in (6) is its right-half-plane logarithm. This
specifies the logarithm of the row rather than taking the principal
logarithm of the final polynomial. Every fixed derivative in \(w\)
of the error is also \(O(\log N)\) on compact subsets of \(\Re w<2\).
The same estimate holds with any final row between
\(\lfloor N/4\rfloor\) and \(J_N\).

## 2. An exact lower barrier near the last row

Put \(r_0=\lfloor N/4\rfloor\), and define
\[
 Q_r=\frac{\cos(r\theta)}{\sin^3(r\theta)},\qquad
 h_r=N/2-r,\qquad u_r=\rho_r-1.
 \tag{7}
\]
All these \(Q_r\) are positive for \(r_0\le r\le J_N\). For the
recurrence indices \(r_0\le r<J_N\), the exact coefficient identities are
\[
 q_r=\frac{Q_{r+1}}{Q_r},\qquad
 \frac{1/A_r}{Q_rQ_{r+1}}
  =B_r:=\frac{\sin^3(r\theta)\sin((2r+1)\theta)}
                    {2\cos(r\theta)}.
 \tag{8}
\]
For all sufficiently large \(N\), \(r_0/N\ge1/5\). Since
\[
 \sin((2r+1)\theta)
  =\sin(r\theta)\cos((r+1)\theta)
       +\cos(r\theta)\sin((r+1)\theta),
 \]
one has uniform bounds
\[
 b_0:=\tfrac12\sin^4(\pi/5)\le B_r\le1,\qquad
 Q_r\asymp h_r/N,\qquad |Q_{r+1}-Q_r|\le C/N.
 \tag{9}
\]
The \(B_r\), \(q_r\), and \(d_r\) statements use \(r<J_N\);
the estimates for \(Q_r\) itself include \(r=J_N\).
Here and below all constants can depend on (5), but not on the row
or the level.

There is \(c>0\) such that
\[
                     \Re u_r\ge cQ_r
                 \quad(r_0\le r\le J_N).
 \tag{10}
\]
To prove this, the bulk theorem initializes (10) at \(r_0\), after
choosing \(c\) small enough. Indeed the limiting ratio at \(x=1/4\)
has real part strictly greater than one, uniformly on (5).
Decrease \(c\) further so that \(c^2\le\gamma b_0/2\).
For large \(N\), \(c_0-\Re w\ge\gamma/2\), so
\[
                  \Re d_r\ge(\gamma b_0/2)Q_rQ_{r+1}.
 \tag{11}
\]
For \(\Re u\ge0\),
\[
              \Re\frac{u}{1+u}
                      \ge\frac{\Re u}{1+\Re u}.
 \tag{12}
\]
Applying (12) to the form \(u_{r+1}=d_r+q_ru_r/(1+u_r)\) of (2),
and using (8), proves the induction:
\[
 \Re u_{r+1}
 \ge \Re d_r+\frac{cQ_{r+1}}{1+cQ_r}
 \ge cQ_{r+1}.
 \tag{13}
\]
Thus the needed lower bound comes from the original row solution.
No dominant mode is prescribed as a boundary condition.

## 3. Transport down to a square-root distance from the endpoint

Write \(\lambda_r=\lambda(r/N,w)\). On this closed tail, including
the limit \(x=1/2\), the explicit formula (4) gives
\[
 |\lambda_r-1|\le C Q_r,\qquad
 \Re\lambda_r\ge1+c_1Q_r,\qquad
 |\lambda_{r+1}-\lambda_r|\le C/N.
 \tag{14}
\]
For example,
\((\lambda(x,w)-1)/(\cos(\pi x)/\sin^3(\pi x))\)
extends continuously at \(x=1/2\) with value \(\sqrt{2-w}\).
Its real part stays strictly positive on the compact domain.

The local recurrence defect is uniformly bounded by
\[
 \left|1+d_r+q_r(1-\lambda_r^{-1})-\lambda_{r+1}\right|
                                                       \le C/N.
 \tag{15}
\]
There is no endpoint singularity hidden in this assertion.
The identity
\[
 \frac1{A_r}=
 \frac{\sin((2r+1)\theta)\cos((r+1)\theta)}
                     {2\sin^3((r+1)\theta)}
 \tag{16}
\]
shows that \(d_r-(2-w)\cot^2(r\theta)=O(N^{-1})\), uniformly
to the last row. Moreover
\[
 |q_r-1|\,|1-\lambda_r^{-1}|
   =\frac{|Q_{r+1}-Q_r|}{Q_r}|1-\lambda_r^{-1}|
                                                        \le C/N.
 \]
Together with (14) and
\(\lambda_r=1+(2-w)\cot^2(r\theta)+(1-\lambda_r^{-1})\),
this proves (15).

Let \(e_r=|\rho_r-\lambda_r|\). Subtracting the exact and approximate
recurrences, then using (10) and (14), yields
\[
 e_{r+1}\le
     \frac{q_r}{|\rho_r\lambda_r|}e_r+C/N
       \le (1-c_2h_r/N)e_r+C/N .
 \tag{17}
\]
Choose the positive constant \(c_2\) small enough that the displayed
factor is nonnegative. At \(r_0\), the bulk theorem gives
\(e_{r_0}=O(N^{-1})\). An induction with the barrier \(C_2/h_r\),
where \(C_2\ge C/c_2\), proves
\[
                       e_r\le C_2/h_r.
 \tag{18}
\]
For the induction, \(h_{r+1}=h_r-1\), and the right side of (17)
at the proposed barrier is at most \(C_2/h_r\), hence at most
\(C_2/h_{r+1}\). We use (18) only while \(h_r\ge\sqrt N\).
Because both ratios lie in \(\Re z\ge1\), the line segment between
them stays in that half-plane, and
\[
                  |\Log\rho_r-\Log\lambda_r|\le e_r.
 \tag{19}
\]
Summing (18)--(19) over these rows costs \(O(\log N)\).

## 4. The final square-root layer

Choose \(k_N\) so that \(\sqrt N\le h_{k_N}<\sqrt N+1\).
Equations (14) and (18) imply
\[
                 |u_{k_N}|\le C/\sqrt N,\qquad
                 |u_{k_N}|/Q_{k_N}\le C.
 \tag{20}
\]
Since \(\Re u_r\ge0\), the exact recurrence and (8) imply
\[
 \frac{|u_{r+1}|}{Q_{r+1}}
 \le\frac{|u_r|}{Q_r}+\frac{|d_r|}{Q_{r+1}}
 \le\frac{|u_r|}{Q_r}+C Q_r .
 \tag{21}
\]
There are \(O(\sqrt N)\) remaining rows, and
\(\sum_{r=k_N}^{J_N}Q_r=O(1)\) by (9). Thus
\[
 |u_r|\le C Q_r,\qquad
 \sum_{r=k_N}^{J_N}
       (|\Log\rho_r|+|\Log\lambda_r|)=O(1).
 \tag{22}
\]
For the logarithms use the integral from \(1\) to \(1+u_r\),
which lies in \(\Re z\ge1\). The same argument applies to
\(\lambda_r\).

The absolute theorem in the linked note already supplies the
normalization through \(r_0\), with error \(O(\log N)\). The
function \(\Log\lambda(x,w)\) has bounded first derivative on
\([1/5,1/2]\), uniformly on (5). Its remaining Riemann-sum error
is \(O(1)\). Combining this fact with (19)--(22) proves (6).
The proof also permits every earlier stopping row. Finally apply
the same proof on a slightly larger compact free-color set and
use Cauchy's formula for the holomorphic logarithmic error.
This proves the derivative assertion.

## 5. The actual complete-end kernel at odd levels

Define the holomorphic function
\[
                 \Psi(w)=\int_0^{1/2}\Log\lambda(x,w)\,dx .
 \tag{23}
\]
The integrable logarithmic singularity at \(x=0\) is the one handled
by the absolute normalization theorem. The integral is holomorphic
on \(\Re w<2\). On the original geometric branch
\[
            w=-2\cos t,\qquad \Psi(w)=\psi(t,0).
 \tag{24}
\]
This is the normalized phase identity in the physical-row note:
the opposite endpoint of its integral is \(\psi(\pi,t)=0\).

**Corollary 2.** If \(N\) is odd, then on every fixed compact subset
of \(\Re w<2\),
\[
 K_N(w,-2)=\exp\{N\Psi(w)+E_N(w)\},\qquad
              |\partial_w^\ell E_N(w)|\le C_\ell\log N
 \tag{25}
\]
for every fixed \(\ell\ge0\) and all sufficiently large odd \(N\).
In particular the factor \(e^{E_N}\) is holomorphic and nonzero,
and its modulus is bounded above and below by fixed powers of \(N\).

Indeed \(c_{J_N}=-2\) at odd levels, so symmetry of the original kernel
gives \(K_N(w,-2)=F_{J_N,N}(w)\) exactly. The difference between the
integral in (6) and (23), multiplied by \(N\), is \(O(N^{-1})\):
the omitted interval has length \(1/(2N)\) and
\(\Log\lambda(x,w)=O(1/2-x)\) there. This proves (25).

At even levels Theorem 1 applies to the actual last row
\(c_{J_N}=-2\cos(\pi/N)\). It is not an estimate of
\(K_N(w,-2)\). An extrapolation in the physical-row label or a
claim about its first-normal correction is not used.

The logarithmic derivative bounds in (25) have a useful local
consequence. On a fixed complex neighborhood, the nonzero factor
changes by \(1+O((\log N)/\sqrt N)\) over a bounded Gaussian window
of radius \(N^{-1/2}\). Thus it can be kept as an \(N\)-dependent
nonzero amplitude in a local saddle calculation. A full-source
lower bound still needs an original contributing cycle and a
bound on its complement; neither follows merely from (25).

## 6. Reproducing the finite checks

The checker below evaluates the defining finite Newton rows, rather
than generating them from the recurrence it tests. It checks both
parities, the exact coefficient identities, the propagated lower
barrier, and the odd-level equality with the original complete-end
kernel. Its reported scaled asymptotic errors are diagnostics; the
uniform estimates are proved above.

~~~sh
python3 experiments/check_last_physical_row_riccati.py
~~~

The [saved record](../repro/results/research-last-physical-row-riccati.json)
includes the checker and proof dependencies.
