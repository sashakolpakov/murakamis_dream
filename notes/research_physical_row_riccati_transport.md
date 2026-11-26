# Riccati transport for the original physical edge rows

Research note, 3 November 2026. Frozen manuscripts are unchanged.

The original physical-row recurrence has a useful contraction that
survives complex free colors. It gives a uniform exponential
asymptotic for ratios of actual kernel values, with a bounded
nonzero transport factor. The phase is the original edge-phase
difference. Only the free-color endpoint is complex in this
statement; the other endpoint remains on the physical grid.

The argument uses the exact positive-real ratios from
[the Jacobi boundary problem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md).
It does not infer nonzero transport from a separation of two
formal characteristic roots.

## 1. The original recurrence and its contracting domain

For \(N\ge3\), put
\[
 \theta=\pi/N,\quad c_j=2\cos((2j+1)\theta),\quad
 J_N=\lfloor(N-1)/2\rfloor,\qquad
                  F_{j,N}(w)=K_N(c_j,w).
 \tag{1}
\]
Here \(K_N\) is the original finite Newton kernel. We keep
its normalization \(F_{0,N}=1\). For \(0\le r<J_N\),
\[
 \begin{split}
 A_{r,N}&=\frac{[2\sin((r+1)\theta)]^4}
                {4\sin((2r+1)\theta)\sin((2r+2)\theta)},\\
 C_{r,N}&=\frac{[2\sin(r\theta)]^4}
                {4\sin(2r\theta)\sin((2r+1)\theta)},
                       \qquad C_{0,N}=0 .
 \end{split}
 \tag{2}
\]
The value equation is exactly
\[
 A_{r,N}F_{r+1,N}
 =(c_0+A_{r,N}+C_{r,N}-w)F_{r,N}-C_{r,N}F_{r-1,N}.
 \tag{3}
\]
All coefficients used in (3) are finite. The coalescing
middle row at even levels is not treated as an ordinary
row beyond this range.

On \(\Re w<c_0\), the actual ratios
\(\rho_{r,N}=F_{r,N}/F_{r-1,N}\) satisfy
\[
 \Re\rho_{r+1,N}\ge1+\frac{c_0-\Re w}{A_{r,N}}>1.
 \tag{4}
\]
This follows inductively from
\[
 \rho_{r+1,N}=\mathscr R_{r,N,w}(\rho_{r,N}),\qquad
 \mathscr R_{r,N,w}(z)=1+d_{r,N}+q_{r,N}(1-z^{-1}),
 \quad
 d_{r,N}=\frac{c_0-w}{A_{r,N}},\quad
 q_{r,N}=\frac{C_{r,N}}{A_{r,N}},
 \tag{5}
\]
with \(\rho_{1,N}=1+(c_0-w)/A_{0,N}\).
Indeed \(\Re z\ge1\) implies \(\Re(z^{-1})\le1\).
In particular no physical value \(F_{r,N}\) vanishes in
this half-plane.

There is a stronger elementary coefficient fact:
\[
 q_{r,N}=
 \left(\frac{\sin(r\theta)}{\sin((r+1)\theta)}\right)^3
          \frac{\cos((r+1)\theta)}{\cos(r\theta)}
                         \in(0,1)\quad(r>0).
 \tag{6}
\]
Both factors are positive and less than one in the
ordinary range. Also \(q_{0,N}=0\). Therefore, on any
half-plane \(\Re z\ge1+\kappa\), \(\kappa>0\),
\[
 |\mathscr R_{r,N,w}(z)-\mathscr R_{r,N,w}(\zeta)|
       \le(1+\kappa)^{-2}|z-\zeta|
       \quad(\Re z,\Re\zeta\ge1+\kappa).
 \tag{7}
\]
This contraction is the reason a second solution cannot
cancel the growing component of the normalized physical
value solution in the result below.

## 2. Uniform attraction to the limiting root

Fix
\[
 0<\varepsilon<1/4,\qquad \gamma>0,\qquad R<\infty,
 \qquad
 \mathcal W_{\gamma,R}
     =\{w\in\mathbb C:\Re w\le2-\gamma,\ |w|\le R\}.
 \tag{8}
\]
Empty free-color sets can simply be omitted.
For \(0<x<1/2\), define
\[
 p(x,w)=2+(2-w)\cot^2(\pi x),\qquad
 \lambda(x,w)=\frac{p(x,w)+\sqrt{p(x,w)^2-4}}2.
 \tag{9}
\]
The square root is positive for real \(p>2\), continued
through \(\Re p>2\). This is a single-valued analytic
branch: \(p^2-4\) does not meet the nonpositive real
axis there. The chosen root satisfies
\[
 |\lambda|>1,\qquad
 \Re\lambda\ge1+(2-\Re w)\cot^2(\pi x)>1.
 \tag{10}
\]
To see the first assertion, continue from real \(p>2\).
A root could cross the unit circle only if
\(p=\lambda+\lambda^{-1}\) belonged to \([-2,2]\).
Then
\(\Re p=\Re\lambda(1+|\lambda|^{-2})>2\)
gives \(\Re\lambda>1\). Finally
\(\lambda=2+(2-w)\cot^2(\pi x)-\lambda^{-1}\)
gives the displayed lower bound.
We use the principal logarithm of this right-half-plane
root.

**Theorem 1.** There are \(N_0\) and \(C\), depending only
on \(\varepsilon,\gamma,R\), such that for \(N\ge N_0\),
\(w\in\mathcal W_{\gamma,R}\), and every physical row
\(\varepsilon\le j/N\le1/2-\varepsilon\),
\[
                |\rho_{j,N}(w)-\lambda(j/N,w)|\le C/N.
 \tag{11}
\]
For each fixed nonnegative integer \(\ell\), the same
estimate holds after \(\ell\) derivatives in \(w\), with
a constant \(C_\ell\).

*Proof.* Work first on the larger real row interval
\[
 I_0=[\varepsilon/4,\ 1/2-\varepsilon/2].
 \tag{12}
\]
The sine denominators in (2), expressed in terms of
\(x=r/N\), are bounded away from zero there. Taylor's
formula, uniformly for \(w\in\mathcal W_{\gamma,R}\),
therefore gives
\[
 \begin{split}
 A_{r,N}&=\tan^2(\pi r/N)+O(N^{-1}),\\
 q_{r,N}&=1+O(N^{-1}),\\
 d_{r,N}&=(2-w)\cot^2(\pi r/N)+O(N^{-1}).
 \end{split}
 \tag{13}
\]
The limiting function \(\lambda(x,w)\) and its first
\(x\)-derivative are uniformly bounded on this compact
parameter set.

For large \(N\), \(c_0-\Re w\ge\gamma/2\).
Equations (4), (10), and the uniform upper bound on \(A\)
give a common \(\kappa>0\) such that
\[
 \Re\rho_{r,N}\ge1+\kappa,\qquad
                    \Re\lambda(r/N,w)\ge1+\kappa
 \tag{14}
\]
whenever \(r/N\in I_0\) and the preceding row also
lies in \(I_0\). Let \(a=(1+\kappa)^{-2}<1\).
The exact limiting fixed-point equation, (13), and the
bounded \(x\)-derivative imply
\[
 \left|\mathscr R_{r,N,w}(\lambda(r/N,w))
                 -\lambda((r+1)/N,w)\right|\le C_1/N.
 \tag{15}
\]
Thus, with \(e_r=|\rho_{r,N}-\lambda(r/N,w)|\),
\[
                         e_{r+1}\le a e_r+C_1/N.
 \tag{16}
\]

Start at \(r_0=\lceil\varepsilon N/2\rceil\).
The original initial solution gives a uniformly bounded
\(e_{r_0}\); it is not an assumed preparation condition.
In fact the preceding actual ratio has modulus at
least one, so (5) and (6) give
\[
 |\rho_{r_0,N}|\le3+|d_{r_0-1,N}|,
 \tag{17}
\]
and the right side is bounded on \(I_0\). Iterating
(16) gives
\[
 e_r\le C_2 a^{r-r_0}+\frac{C_1}{N(1-a)} .
 \tag{18}
\]
Every row in the stated interval has
\(r-r_0\ge\varepsilon N/2-1\). This proves (11).

For derivatives, repeat the argument on the larger
free-color set
\(\mathcal W_{\gamma/2,R+1}\). A fixed small complex
disk around every point of \(\mathcal W_{\gamma,R}\)
lies in that set. Both the actual ratios and the
chosen root are holomorphic there. Cauchy's formula
applied to (11) proves every fixed derivative estimate.
\(\square\)

## 3. The logarithmic error and the nonzero transport factor

On \(\Re w<c_0\), define the logarithm of the actual
normalized ratio by
\[
 L_{i,j,N}(w)=
       \sum_{r=i+1}^{j}\operatorname{Log}\rho_{r,N}(w),
       \qquad \exp L_{i,j,N}=F_{j,N}/F_{i,N}.
 \tag{19}
\]
This is the holomorphic branch that is real on the real
free-color interval. It need not equal the principal
logarithm of the final quotient after its argument has
wound around zero.

**Corollary 2.** Under the hypotheses of Theorem 1,
uniformly for
\(\varepsilon\le i/N\le j/N\le1/2-\varepsilon\),
\[
 \left|L_{i,j,N}(w)
       -N\int_{i/N}^{j/N}\operatorname{Log}\lambda(x,w)\,dx\right|
                                  \le C\frac{j-i}{N}.
 \tag{20}
\]
The error is holomorphic and obeys the same bound, with
a new constant, after every fixed number of
free-color derivatives.
Consequently the actual ratio has the form
\[
 \frac{F_{j,N}(w)}{F_{i,N}(w)}
   =B_{i,j,N}(w)
      \exp\left(N\int_{i/N}^{j/N}
                       \operatorname{Log}\lambda(x,w)\,dx\right),
 \qquad e^{-C}\le|B_{i,j,N}(w)|\le e^C .
 \tag{21}
\]
The factor \(B_{i,j,N}\) is holomorphic and nonzero.

*Proof.* On the common half-plane in (14), the logarithm
is Lipschitz with constant \((1+\kappa)^{-1}\).
Summing (11) therefore changes (19) by at most
\(C(j-i)/N\) when each ratio is replaced by
\(\lambda(r/N,w)\).
The bounded \(x\)-derivative of \(\operatorname{Log}\lambda\)
gives the same bound for the error of the right-endpoint
Riemann sum. This proves (20). The derivative assertion
again follows by applying the argument on a larger
free-color set and using Cauchy's formula. Exponentiating
the actual holomorphic error gives (21). \(\square\)

This is a bounded-factor asymptotic. It does not assert
that \(B_{i,j,N}\) converges, or that it equals
\(1+O(N^{-1})\). The nonzero factor in (21) has been
obtained from the normalized original solution, rather
than inserted as an unspecified branch coefficient.

## 4. Agreement with the original edge phase

The relation to the geometric return is explicit. For
\(\Re w<2\), take the square root of \(2-w\) with positive
real part. Then
\[
 \operatorname{Log}\lambda(x,w)
   =2\operatorname{arsinh}
          \left(\frac{\sqrt{2-w}}2\cot(\pi x)\right).
 \tag{22}
\]
The argument of the square root has absolute value less
than \(\pi/4\). The indicated inverse hyperbolic sine
has imaginary part in \((-\pi/4,\pi/4)\), so the
logarithm in (22) is the same one used in (19)--(21).
Squaring
\(\sqrt{1+z^2}+z\), where
\(z=\sqrt{2-w}\cot(\pi x)/2\), verifies its characteristic
equation and proves (22).

If \(w=-2\cos u\) and
\(\cos(u/2)=\sqrt{2-w}/2\), the
[original edge return](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_powers_three_and_above.md#1-the-phase-and-its-selected-leaf-solution)
satisfies
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                       (\tan(t/2)\cos(u/2)).
 \tag{23}
\]
It follows from (22)--(23) that
\[
 \int_a^b\operatorname{Log}\lambda(x,w)\,dx
             =\psi(\pi-2\pi b,u)-\psi(\pi-2\pi a,u).
 \tag{24}
\]
An additive normalization of \(\psi\) cancels here.
The branches are continued from the complete real
edge; no exponentiated characteristic is used to
choose a new logarithmic lift.

The actual physical angle is
\(\tau_j=\pi-(2j+1)\pi/N\).
Replacing \(j/N\) by \((j+1/2)/N\) at both endpoints
of the integral changes the error in (20) by at most
\(C(j-i)/N\). Thus
\[
 \frac{K_N(c_j,w)}{K_N(c_i,w)}
  =\widetilde B_{i,j,N}(w)
     e^{\,N\{\psi(\tau_j,u)-\psi(\tau_i,u)\}},
       \qquad e^{-C}\le|\widetilde B_{i,j,N}(w)|\le e^C.
 \tag{25}
\]
Indeed the change of integral is the integral, over a
shift of size \(1/(2N)\), of the difference of its two
endpoint integrands. Their Lipschitz bound gives the
stated estimate.

For the positive path charge cube, the
[geometric half-plane theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_geometric_spectral_half_plane.md)
gives \(\Re w<7/4\) and \(|w|<7/2\). Hence a single
choice \(\gamma=1/4,\ R=7/2\) covers every geometric
free color, independently of the fixed path and its
powers. The other endpoint in (25) remains an actual
physical row. This result neither continues that
row to a complex angle nor estimates the original
signed Fourier sum over rows.

## 5. Why the determinant formula does not replace the contraction

The existing Jacobi representation gives the exact
Stieltjes formula
\[
 F_{j,N}(w)=
   \frac{\det(\mathcal J_j-wI)}{\prod_{r<j}A_{r,N}},
 \qquad
 -\partial_w\log F_{j,N}(w)
                  =\operatorname{Tr}(\mathcal J_j-wI)^{-1}.
 \tag{26}
\]
It proves zero-freeness and bounds free-color derivatives.
By itself it does not compare neighboring row sizes at
the required precision. The Riccati map is the exact
Schur-complement recursion for these determinants.
Its contraction (7) supplies the quantitative attraction
and the bounded logarithmic error, without a separate
assumption about spectral-measure convergence.

## 6. Absolute normalization from the original first row

The normalization \(F_{0,N}=1\) also determines the
exponential rate without a reference row in the interior.
Fix \(0<\alpha<1/2\) and the same free-color set (8).
Write \(\lambda_r=\lambda(r/N,w)\).

**Theorem 3.** Uniformly for \(1\le j\le\alpha N\) and
\(w\in\mathcal W_{\gamma,R}\), for all sufficiently
large \(N\),
\[
 \left|\log F_{j,N}(w)
       -N\int_0^{j/N}\operatorname{Log}\lambda(x,w)\,dx\right|
                                      \le C\log(j+1).
 \tag{27}
\]
Here \(\log F_{j,N}=\sum_{r=1}^j\operatorname{Log}\rho_{r,N}\)
is the actual normalized holomorphic logarithm.
The integral converges at zero. Every fixed free-color
derivative of the error has the same logarithmic bound.
In particular
\[
 (j+1)^{-C}\le
 \left|F_{j,N}(w)
       \exp\left(-N\int_0^{j/N}\operatorname{Log}\lambda(x,w)\,dx\right)
 \right|\le(j+1)^C .
 \tag{28}
\]

*Proof.* The endpoint coefficient has the exact form
\[
 A_{r-1,N}
 =\tan^2(r\theta)
                \frac{\sin(2r\theta)}{\sin((2r-1)\theta)}.
 \tag{29}
\]
For \(1\le r\le\alpha N\), the sine ratio is bounded
above and below by positive constants depending only
on \(\alpha\). For example, putting
\(m_\alpha=\sin(2\pi\alpha)/(2\pi\alpha)>0\),
these bounds can be taken as \(m_\alpha\) and \(2\).
Use that \(\sin x/x\) decreases on \((0,\pi)\) for the
upper bound and \(\sin x\ge m_\alpha x\) for the lower.
Moreover
\[
 \left|\frac{\sin((2r-1)\theta)}{\sin(2r\theta)}-1\right|
                    \le\frac{1}{2m_\alpha r}.
 \tag{30}
\]
These estimates and (4) give uniform comparability
\[
 c(1+\cot^2(r\theta))
       \le|\rho_{r,N}|,\ |\lambda_r|
       \le C(1+\cot^2(r\theta)).
 \tag{31}
\]
For the upper bound on \(\rho\), use
\(|\rho_{r,N}|\le3+|(c_0-w)/A_{r-1,N}|\).
For its lower bound use (4) and
\(c_0-\Re w\ge\gamma/2\).
For \(\lambda\), use (10) and
\(|\lambda|\le|p|+1\).
Both real parts also lie in one common half-plane
\(\Re z\ge1+\kappa\), with \(\kappa>0\), throughout
this range.

We next bound the local relative defect down to the
first row. Equations (6) and (29)--(30) give, for \(r\ge1\),
\[
 \begin{split}
 |q_{r,N}-1|&\le C/(r+1),\\
 \left|d_{r,N}-(2-w)\cot^2((r+1)\theta)\right|
       &\le \frac{C}{r+1}|(2-w)\cot^2((r+1)\theta)|.
 \end{split}
 \tag{32}
\]
For the first estimate, the difference of two
consecutive sines is at most \(\theta\), their
denominator is at least a fixed multiple of
\((r+1)\theta\), and \(\cos(r\theta)\) is bounded
away from zero. Apply these facts to the two ratios
in (6). For the second estimate use (30) with \(r+1\)
in place of \(r\), and
\((c_0-w)/(2-w)=1+O(N^{-2})\).

The limiting root has a controlled logarithmic
variation at the endpoint:
\[
 |\partial_x\operatorname{Log}\lambda(x,w)|
 \le\left|\frac{\partial_x[(2-w)\cot^2(\pi x)]}
                  {(2-w)\cot^2(\pi x)}\right|
 =\frac{2\pi}{\sin(\pi x)\cos(\pi x)}
 \le\frac{C_\alpha}{x}.
 \tag{33}
\]
Indeed its exact derivative has denominator
\(\sqrt{d(d+4)}\), with \(d=(2-w)\cot^2(\pi x)\);
\(\Re d>0\) implies \(|d+4|\ge|d|\).
Thus \(|\lambda_r/\lambda_{r+1}-1|\le C/r\).
Combining this with (32) and the fixed-point equation
for \(\lambda_{r+1}\) yields
\[
 \frac{|\mathscr R_{r,N,w}(\lambda_r)-\lambda_{r+1}|}
                           {|\lambda_{r+1}|}\le C/r.
 \tag{34}
\]
For completeness, split the numerator by inserting
\(\mathscr R_{r,N,w}(\lambda_{r+1})\). The first
difference is
\(q_{r,N}(\lambda_r-\lambda_{r+1})/
(\lambda_r\lambda_{r+1})\), up to sign.
The second is the difference in \(d\) from (32)
plus \((q_{r,N}-1)(1-\lambda_{r+1}^{-1})\).
Also \(|d|\le4|\lambda_{r+1}|\), since
\(d=\lambda_{r+1}+\lambda_{r+1}^{-1}-2\).
This proves (34) without an unbounded absolute
coefficient estimate.

Let \(e_r=|\rho_{r,N}-\lambda_r|/|\lambda_r|\).
The exact difference of two Riccati maps now gives
\[
 e_{r+1}
 \le\frac{q_{r,N}}{|\rho_{r,N}\lambda_{r+1}|}e_r+C/r
 \le a e_r+C/r,\qquad a=(1+\kappa)^{-2}<1.
 \tag{35}
\]
The factor \(\lambda_r\) cancels in this relative
estimate. Equation (31) bounds \(e_1\) uniformly for
the original first row.
Iteration gives \(e_r\le C/r\): in the convolution
\(\sum_{k<r}a^{r-1-k}/k\), terms with \(k\ge r/2\)
are bounded by \(2/[r(1-a)]\), and the remaining
terms by \(a^{r/2-1}(1+\log r)\).
The initial term is exponentially smaller.

For large \(r\), \(e_r\le1/2\) implies
\(|\operatorname{Log}\rho_{r,N}-\operatorname{Log}\lambda_r|
\le2e_r\). The finitely many smaller rows have the
same bound \(C/r\), after enlarging \(C\), by (31)
and the right-half-plane arguments of both factors.
Therefore their total logarithmic difference is
\(O(\log(j+1))\).

Finally the elementary root expansion at \(x=0\) is
\[
 \operatorname{Log}\lambda(x,w)
       =\operatorname{Log}(2-w)-2\log(\pi x)+O(x^2),
 \tag{36}
\]
uniformly with every fixed free-color derivative;
the \(x\)-derivative of the remainder is \(O(x)\).
After adding \(2\log x\),
the remaining function has a bounded first derivative
on \([0,\alpha]\), so its Riemann-sum error is bounded.
For the singular part, the error is
\(2(j\log j-j-\log(j!))=O(\log(j+1))\);
the elementary integral bounds for \(\log x\) suffice.
This proves (27). Cauchy's formula on the enlarged
free-color set used in Theorem 1 gives the derivative
claim, and exponentiation gives (28). \(\square\)

The integral in (27) is the absolute original edge
phase. The normalization at its degenerate boundary
is \(\psi(\pi,u)=0\). One can check this directly:
the [symmetric return formula](research_edge_hessian_and_phase_response.md#1-branches-and-the-exact-edge-matrix)
\(\psi_u(t,u)=-\pi^{-1}\operatorname{arsinh}
(\tan(u/2)\cos(t/2))\) tends to zero at \(t=\pi\),
so that boundary value is independent of \(u\).
At \(u=0\),
\(\int_0^\pi\operatorname{arsinh}(\tan(t/2))\,dt=4G\),
where \(G=-\int_0^{\pi/4}\log(\tan s)\,ds\)
is Catalan's constant. This cancels
\(\psi(0,0)=4G/\pi\). The branch continues from the
complete edge with this normalization.

Thus, on each compact physical-row interval from
Theorem 1, (27) also gives
\[
             \log K_N(c_j,w)
                 =N\psi(\tau_j,u)+O(\log N),
                 \qquad w=-2\cos u.
 \tag{37}
\]
The half-offset changes the exponent by \(O(1)\)
on this interior interval. In particular the
polynomial lower factor in (28) is anchored at
the exact value \(F_{0,N}=1\); it contains no
unknown reference-row amplitude. This remains
a theorem about physical rows with complex
free color, not a complex-row interpolation
or a lower bound for their signed trace.

## 7. Finite reproduction

Run

~~~sh
python3 experiments/check_physical_row_riccati_transport.py \
  --precision 140 \
  --output repro/results/research-physical-row-riccati-transport.json
~~~

The [checker](../experiments/check_physical_row_riccati_transport.py)
evaluates the original rows by the terminating Newton sum,
independently of the recurrence used in the proof. The
[saved record](../repro/results/research-physical-row-riccati-transport.json)
covers 16 complete or complex free-color cases at levels
\(32,64,128,256\). It checks 720 exact row recurrences,
600 bulk contraction inequalities, and 704 endpoint
relative-contraction inequalities. It also checks the
continued-log product and the return-phase identity with
the physical half-offset.

The scaled ratio and logarithmic errors in that record
are reported as diagnostics. They are not used as a
proof of a uniform asymptotic estimate; that estimate
follows from the contraction and endpoint arguments above.
