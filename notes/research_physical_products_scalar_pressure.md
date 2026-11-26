# The scalar pressure of any fixed physical-row product

Private written proof, 17 November 2026.

For an arbitrary fixed number of physical value rows, the original
positive trace has a logarithmic rate determined by one real height.
The rate includes the original normalization: no additive constant
is left to be identified. Its height equation is the sum of the
individual row returns, and has one solution on the entire strict
support. This gives an explicit continuation of the three-row
pressure to any fixed number of incoming rows.

The theorem concerns the product followed by the original trace,
with no filling crossing inserted. It does not estimate independent
boundary derivatives or prove a volume identity for a partially
filled knot.

## 1. Original rows and the scalar coefficient saddle

Use \(N\ge3\), \(D=N-1\), \(J=\lfloor D/2\rfloor\),
\[
 c_j=2\cos((2j+1)\pi/N),\quad
 P_N(C)=2T_N(C/2)+2,\quad
 \phi_N(f)=(-1)^D N^2[C^D]\operatorname{rem}_{P_N}f,
\]
and \(F_{j,N}(C)=K_N(c_j,C)\), \(0\le j\le J\).
Fix \(m\ge3\) and put
\[
 \Gamma_{\mathbf j,N}=\phi_N\!\left(\prod_{i=1}^mF_{j_i,N}\right),
 \qquad k=\sum_i j_i-D.
 \tag{1}
\]
The positive coefficient theorem supplies a generating function
\(H_N\), a positive constant \(a_N\), and a unique radius \(\rho_N\)
with
\[
 \rho_N H_N'(\rho_N)/H_N(\rho_N)=k.
 \tag{2}
\]
It defines the variance \(V_N\) by differentiating this mean with
respect to \(\log\rho\). Uniformly for \(k\ge\varepsilon N\),
\[
 0<a\le\rho_N\le b<1/4,\qquad cN\le V_N\le CN,
\]
\[
 \Gamma_{\mathbf j,N}
  =\frac{N^2a_NH_N(\rho_N)\rho_N^{-k}}{\sqrt{2\pi V_N}}
                                             (1+O(N^{-1})).
 \tag{3}
\]
All constants depend only on \(m,\varepsilon\). In particular
the midpoint rows are included.

Set
\[
 \zeta_N=c_0-\rho_N^{-1}<-2,\qquad
 h_N=\operatorname{arcosh}(-\zeta_N/2)>0.
 \tag{4}
\]
The inequality holds for all sufficiently large \(N\), uniformly
in the stated range. The compact bounds on \(\rho_N\) put \(h_N\)
in a fixed compact subinterval of \((0,\infty)\).

The exact product definitions in the coefficient theorem give
\[
 a_NH_N(\rho)\rho^{-k}
   =\frac{\prod_iF_{j_i,N}(c_0-\rho^{-1})}
           {\rho\,|P_N(c_0-\rho^{-1})|}
 \quad\text{if }c_0-\rho^{-1}<-2.
 \tag{5}
\]
Indeed its denominator lists all \(N\) roots of \(P_N\) with
multiplicity; its numerator is the positive Jacobi factorization.
At \(C=-2\cosh h\),
\[
 |P_N(C)|=e^{Nh}\bigl(1+(-1)^Ne^{-Nh}\bigr)^2.
 \tag{6}
\]
Equations (3)--(6) keep the trace normalization at both parities.

## 2. The normalized row action

The full physical-row profile is
\[
 \Psi_x(w)=\int_0^x
    2\operatorname{arsinh}\!\left(
            \frac{\sqrt{2-w}}{2}\cot(\pi s)\right)\,ds,
 \qquad 0\le x\le1/2.
 \tag{7}
\]
The branches are positive on \(w<-2\). The integrable logarithmic
singularity at \(s=0\) fixes the normalization. The complete row
profile source proves, on each compact subset of \(\Re w<2\),
\[
 \log F_{j,N}(w)=N\Psi_{j/N}(w)+O(\log N)
 \tag{8}
\]
uniformly over all physical indices, including both ends.
The logarithm is the one positive on the real half-line.
The same bound holds after every fixed number of \(w\)-derivatives
on smaller compact sets: apply Cauchy's formula to the holomorphic
difference in (8).

For real \(h\ge0\), direct differentiation of (7) gives
\[
 \partial_h\Psi_x(-2\cosh h)
   =\frac1\pi\arcsin\!\left(\tanh(h/2)\sin(\pi x)\right).
 \tag{9}
\]
For example the differentiated integrand is
\[
 \frac{\tanh(h/2)\cos(\pi s)}
      {\sqrt{1-\tanh^2(h/2)\sin^2(\pi s)}},
\]
whose integral is (9). All inverse sines in this note take values
in \([0,\pi/2]\).

## 3. A unique height on the entire strict support

For
\[
 \mathcal X_m=\{\mathbf x\in[0,1/2]^m:\ \sum_i x_i>1\},
\]
define
\[
 A_{\mathbf x}(h)=\sum_i\Psi_{x_i}(-2\cosh h)-h,\qquad h\ge0.
 \tag{10}
\]
There is exactly one minimum, at a finite positive height
\(h=h(\mathbf x)\). It is determined by
\[
 \boxed{\qquad
 \sum_{i=1}^m
   \arcsin\!\left(\tanh(h/2)\sin(\pi x_i)\right)=\pi .
 \qquad}
 \tag{11}
\]
To see this, use (9):
\[
 A'_{\mathbf x}(0)=-1,\qquad
 \lim_{h\to\infty}A'_{\mathbf x}(h)=\sum_i x_i-1>0,
\]
\[
 A''_{\mathbf x}(h)=
 \frac{\operatorname{sech}^2(h/2)}{2\pi}
 \sum_i\frac{\sin(\pi x_i)}
 {\sqrt{1-\tanh^2(h/2)\sin^2(\pi x_i)}}>0.
 \tag{12}
\]
Thus the derivative crosses zero once. It stays positive thereafter,
which also proves that this is the global minimum.

For every fixed support margin \(\sum_i x_i\ge1+\delta\),
the height lies in a compact subinterval of \((0,\infty)\),
uniformly up to the midpoint faces and coordinates equal to zero.
The lower bound follows from
\[
 \pi\le m\arcsin(\tanh(h/2)),
 \quad\text{hence}\quad
 h\ge2\operatorname{artanh}(\sin(\pi/m)).
 \tag{13}
\]
For an upper bound, the functions
\(\arcsin(t\sin(\pi x))\) tend uniformly to \(\pi x\) on
\([0,1/2]\) as \(t\uparrow1\), by uniform continuity of
\(\arcsin\) on \([0,1]\). Their sum is therefore greater than
\(\pi\) at one fixed sufficiently large height.

Write
\[
                 \mathcal G_m(\mathbf x)=A_{\mathbf x}(h(\mathbf x)).
 \tag{14}
\]
This definition is continuous on \(\mathcal X_m\).
It is real analytic wherever every \(x_i>0\), including
one-sided neighborhoods of midpoint faces. This follows from
(12), the implicit function theorem and (7).

## 4. The original trace has this pressure

**Theorem.** Fix \(m\ge3\) and \(\varepsilon>0\). Uniformly over
physical tuples with \(k\ge\varepsilon N\), at both parities,
\[
 \boxed{\qquad
 \log\Gamma_{\mathbf j,N}
       =N\mathcal G_m(\mathbf j/N)+O_{m,\varepsilon}(\log N).
 \qquad}
 \tag{15}
\]
Their coefficient saddle obeys
\[
 h_N=h(\mathbf j/N)+O_{m,\varepsilon}(\log N/N).
 \tag{16}
\]
Its variance has the geometric expression
\[
 \frac{V_N}{N}
   =\frac{A''_{\mathbf j/N}(h(\mathbf j/N))}
           {\tanh^2(h(\mathbf j/N)/2)}
                  +O_{m,\varepsilon}(\log N/N).
 \tag{16a}
\]

**Proof.** Write \(\rho(h)=(c_0+2\cosh h)^{-1}\).
The logarithm of the right side of (5) is
\[
 B_N(h)=\sum_i\log F_{j_i,N}(-2\cosh h)
            -\log|P_N(-2\cosh h)|-\log\rho(h).
 \tag{17}
\]
By (2), \(B_N'(h_N)=0\): the logarithmic derivative of
\(a_NH_N(\rho)\rho^{-k}\) with respect to \(\log\rho\)
is its mean minus \(k\), and \(\rho'(h_N)\ne0\).

On the compact height interval containing \(h_N\), equations
(6), (8), and their differentiated forms give
\[
 B_N(h)=N A_{\mathbf j/N}(h)+O(\log N),\qquad
 B_N'(h)=N A'_{\mathbf j/N}(h)+O(\log N).
 \tag{18}
\]
The constants are uniform. For large \(N\), the support hypothesis
implies \(\sum_i j_i/N\ge1+\varepsilon/2\); hence section 3
also bounds \(h(\mathbf j/N)\) in a fixed compact height interval.
On the interval containing both heights, (12) has a uniform positive
lower bound. Indeed \(\sin(\pi x_i)\ge2x_i\), their sum is bounded
below, and the hyperbolic factor is bounded away from zero.
The mean-value theorem applied to (18) proves (16).

The first equation of (18), stationarity at \(h(\mathbf j/N)\),
and bounded second derivatives then imply
\[
 B_N(h_N)=N\mathcal G_m(\mathbf j/N)+O(\log N).
 \tag{19}
\]
Finally (3) and (5) add only
\(2\log N-\tfrac12\log(2\pi V_N)+O(N^{-1})=O(\log N)\).
This proves (15). At the exact saddle, differentiating with
respect to \(h\) twice gives
\[
 B_N''(h_N)=V_N\left(\frac{d}{dh}\log\rho(h_N)\right)^2.
\]
The extra chain-rule term vanishes because the mean equals \(k\).
More explicitly, the second
chain-rule term is \((\mu_N-k)(\log\rho)''=0\).
The twice-differentiated version of (18) and
\[
 \frac{d}{dh}\log\rho(h)
       =-\frac{2\sinh h}{c_0+2\cosh h}
       =-\tanh(h/2)+O(N^{-2})
\]
now prove (16a), using (16). \(\square\)

Thus the leading coefficient in the positive coefficient theorem
and the explicit pressure in (15) concern the same original trace.
The normalization of \(\Psi\) in (7) and the exact denominator
in (6) determine the additive constant directly.

## 5. Concavity and the algebraic branch

For \(0<x_i\le1/2\), the gradient is
\[
 \partial_{x_i}\mathcal G_m
   =2\operatorname{arsinh}\!\left(\cosh(h/2)\cot(\pi x_i)\right).
 \tag{20}
\]
Its Hessian is strictly negative definite on the interior in the
external variables. Indeed, before minimizing over \(h\),
the external Hessian of \(A_{\mathbf x}\) is diagonal with entries
\[
 \partial_{x_i}^2 A_{\mathbf x}
   =-\frac{2\pi\cosh(h/2)}
     {\sin^2(\pi x_i)
       \sqrt{1+\cosh^2(h/2)\cot^2(\pi x_i)}}<0.
 \tag{21}
\]
The Hessian of the minimum is this negative definite diagonal
matrix minus
\(A_{\mathbf x h}(A_{hh})^{-1}A_{h\mathbf x}\), which is
positive semidefinite. It is therefore negative definite.
The argument also gives continuity and concavity on portions
including zero coordinates, by taking limits.

Set \(L=\operatorname{sech}^2(h/2)\). Equation (11) becomes
\[
 \sum_i\arcsin\!\left(\sqrt{1-L}\sin(\pi x_i)\right)=\pi,
 \qquad 0<L\le\cos^2(\pi/m)<1.
 \tag{22}
\]
For \(x_i=1/2\) for all \(i\), equality holds in the upper bound.
In complex variables, exponentiating (22) gives an algebraic
relation with the square roots retained:
\[
 \prod_i\left(
   \sqrt{1-(1-L)\sin^2(\pi x_i)}
       +i\sqrt{1-L}\sin(\pi x_i)\right)=-1.
 \tag{23}
\]
The positive roots and the sum of principal angles in (22)
select its real branch. Equation (23) alone does not select
that branch; for larger \(m\) it can also encode other odd
multiples of \(\pi\). In terms of the boundary exponentials
\(e^{i\pi x_i}\), the sine coefficients are Laurent algebraic.
No identification of (23) with a knot's A-polynomial is asserted.

For \(m=3\), this pressure equals the previously proved
triple-row pressure on strict support: both are uniform logarithmic
limits of the same original positive traces, and approximation by
physical grids together with continuity identifies the functions.
The common characteristic is consequently
\[
                    \zeta=-2\cosh h=2-\frac4L.
 \tag{24}
\]
The sum of row returns in (11) and the term \(-h\) in (10)
are the explicit central closing condition and action. To use
this point in a larger tangle calculation, one must still estimate
the original boundary derivatives and the signed filling factors.

## Complete direct sources

The complete direct texts were read at the following pins:

* [Positive coefficient and scalar saddle](research_physical_products_positive_coefficient_saddle.md),
  SHA256 e82fea1f786383a1cfe4529573805adf5fc75a77e433e38ea609024bdeed7824:
  exact positive coefficient, compact radius, variance, and the
  uniform nonzero leading factor at all physical midpoint rows.
* [The calibrated physical-row profile](research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b:
  the original logarithm, its normalized profile and uniform
  \(O(\log N)\) estimate throughout the physical row range.
* [Triple-row pressure](research_physical_triple_row_pressure.md),
  SHA256 df556243507231e0edb2ea5234163b29623b6d5751b9be987d8f4d967170db4e:
  used only for the comparison with the earlier three-row function.

Only written mathematics, source reads, and metadata hashes were used.
No mathematical programs, numerical evaluations, tests, builds or
compilations were run. Frozen manuscripts and public documents remain
unchanged.
