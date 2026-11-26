# An exact two-boundary formula for two crossings

Research calculation, 2 November 2026. This note sums the central
trace before deforming any contour. For a degree-two vertex with
crossing power two, it gives a factorial formula with two free
boundary angles. Its selected point lies in the interior of this
factorial chart, although it lies on the boundary of the earlier
chart that retained the central angle. The global estimates for this
new sum are a separate step.

## 1. The finite identity

Fix \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Use the original Newton basis \(e_i\), trace \(\phi\), and crossing
\(R\). Write
\[
F_j=(Q;Q)_j=\prod_{r=1}^j(1-Q^r),\qquad F_0=1.
\]
The symbol \(\mathrm i\) in a complex scalar denotes the square root
of minus one; the subscript \(i\) is an integer index.
In particular \(F_j\ne0\) for \(0\le j<N\). Set \(F_j=0\) for
\(N\le j\le2D\), consistently with the finite product.

**Proposition.** At every integer level,
\[
\boxed{\displaystyle
\phi(R^2e_i e_j)=
 Nq^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2}
 \qquad(0\le i,j<N).}
\tag{1}
\]
Thus the full boundary polynomial is exactly
\[
P_{2,2,N}(u,v)
 =N\sum_{\substack{i,j\ge0\\i+j<N}}
 q^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2}
 e_i(-2\cos u)e_j(-2\cos v).
\tag{2}
\]
There are no omitted indices, denominator zeros, or evaluations
only at distinct spectral roots. Negative crossing power is
obtained by conjugating the coefficients.

Here is a proof from the finite crossing matrix. In the notation of
[the crossing-power calculation](research_terminal_powers_qbinomial.md),
let \(M\) be multiplication by \(R\), let \(J\) reverse the Newton
basis, and put
\[
\kappa=q^{D^2/2},\qquad
\mathsf D_{kk}=(-q)^kF_k,\qquad
B_{kj}=Q^{j(j+1)}{k\brack j}_Q\quad(j\le k).
\]
That calculation proves
\[
M^2=\kappa^2\mathsf D B\mathsf D^{-1}.
\tag{3}
\]
The coefficient matrix of the left side of (1) is \(JM^2\).
It vanishes when \(i+j>D\), since \(M^2\) is lower triangular.
Otherwise the root-of-unity reflection gives
\[
F_{D-i}=\frac{N(-1)^i q^{i(i+1)}}{F_i},
\qquad
{D-i\brack j}_Q
 =(-1)^j q^{-2ij-j(j+1)}\frac{F_{i+j}}{F_iF_j}.
\tag{4}
\]
Substitution into the \((D-i,j)\) entry of (3) gives (1), because
\(\kappa^2(-1)^Dq^D=1\).
All equalities are in the original quotient algebra, so they retain
first normal derivatives at every repeated root.

## 2. The new interior critical point

For \(0<\Re z<1\), let
\[
J(z)=\int_0^z\log(2\sin\pi w)\,dw
\]
on the branch continued from the real interval. In this section
\(J(z)\) is the logarithmic integral, rather than the reversal
matrix of Section 1. Let \(b(x,u)\) be the canonical Newton phase,
normalized by \(b(x,0)=g(x)=J(2x)-4J(x)\); its exact definition is
in [the factorial interpolation](research_terminal_three_central_phase.md).

The relation
\[
F_j=i^{-j}q^{j(j+1)/2}S_j,\qquad
S_j=\prod_{r=1}^j2\sin(\pi r/N),
\]
puts the coefficient in (1) into the form
\[
N\mathrm i^{\,i+j}q^{((i-j)^2-i-j)/2}
     \frac{S_{i+j}}{S_i^2S_j^2}.
\]
With \(x=i/N\), \(y=j/N\), the resulting phase is
\[
\begin{split}
\mathcal W(x,y;u,v)
={}&J(x+y)-2J(x)-2J(y)+b(x,u)+b(y,v)\\
 &+\frac{i\pi}{2}\bigl((x-y)^2+x+y\bigr).
\end{split}
\tag{5}
\]
On compact subsets where these factorial arguments remain regular,
the summand in (2) has the uniform expansion
\[
N^{-5/2}a(x,y)e^{N\mathcal W(x,y;u,v)}(1+O(N^{-1})),
\tag{6}
\]
where
\[
a(x,y)=\frac{\sqrt2}{16}
 e^{-i\pi(x+y)/2}
 \frac{\sqrt{\sin\pi(x+y)}}{\sin^2(\pi x)\sin^2(\pi y)}.
\tag{7}
\]
The branches continue from the real interior. The midpoint shifts
in the Newton factors are included in (7).

At \(u=v=0\), put
\[
z=\frac14+\frac{i\log3}{4\pi},
\qquad \tan(\pi z)=e^{i\pi/6}.
\]
Then \((x,y)=(z,z)\) is an exact critical point. Indeed each first
derivative of (5) there is
\[
3\log\cot(\pi z)+\frac{i\pi}{2}=0.
\]
The Hessian is
\[
\mathcal W''(z,z)=
\begin{pmatrix}
-3\sqrt3\,\pi+3i\pi/2&-3i\pi/2\\
-3i\pi/2&-3\sqrt3\,\pi+3i\pi/2
\end{pmatrix}.
\tag{8}
\]
Its real part is negative definite. Its arguments \(z,2z\) lie
strictly inside their original factorial strips. The implicit
function theorem gives a nearby holomorphic critical point for
small \(u,v\).

If the full discrete contour is shown to pass through this point
with all complementary contributions exponentially smaller, (6)
would yield a leading power \(N^{-3/2}\), with coefficient
\[
\frac{2\pi\,a(z,z)}{\sqrt{\det[-\mathcal W''(z,z)]}}\ne0
\]
at complete boundary. This conditional calculation does not replace
that global comparison.

## 3. Why this is a different factorial chart

The central-angle formulation has selected
\[
t_*=\frac{\pi}{2}-2i\operatorname{arsinh}(1/\sqrt2),
\qquad x_*=y_*=z.
\]
In that formulation one denominator has real normalized argument
\[
\frac12-\Re z-\frac{\Re t_*}{2\pi}=0.
\]
The new exact formula has already summed that angle. Its factorial
arguments at the selected point are \(z\) and \(2z\), with real
parts \(1/4\) and \(1/2\). Thus the old boundary difficulty does not
justify treating this source as singular; the finite identity gives
a regular alternative.

The phase (5) includes the full crossing normalization. It must not
be identified with the geometric action merely because their
critical equations exponentiate to the same equations. The geometric
comparison must retain its additive unit phase. This is now proved
in [the marked phase calculation](research_degree_two_power_two_geometric_phase.md):
the selected phase is the original geometric action plus \(i\pi/2\).
The [whole two-boundary theorem](research_degree_two_power_two_boundary_theorem.md)
also supplies the global contour estimates. The all-level identity
(1) is independent of these subsequent arguments.

## 4. Reproduction

Run

    python3 experiments/audit_degree_two_power_two_formula.py

The calculation compares every coefficient in (1) with the independently
squared crossing multiplication matrix, using exact cyclotomic
arithmetic. The written argument proves the identity at every level.
The finite checks detect normalization errors and do not prove
global asymptotic estimates.

