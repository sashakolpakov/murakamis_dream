# The boundary-color dependence of the filled-leaf upper bound

Private written proof, 16 November 2026.

The whole-interval leaf estimate can be sharpened at the actual
physical colors. Instead of spending its largest growth rate at
every color, stop the recurrence at the requested row. The resulting
upper exponent is a partial characteristic integral. It equals the
real part of the previously normalized stationary leaf action.
This statement includes the first derivatives that occur in the
original finite trace. It is not an interpolation theorem between
physical colors.

## 1. The original leaf and its color profile

Fix an integer \(n\), a nonnegative integer \(r\), and \(A<\infty\).
Use the original kernel, crossing polynomial, turn and quotient:
\[
 q=e^{\pi i/N},\qquad P_N(Z)=2T_N(Z/2)+2,\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N),
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 J_N=\lfloor(N-1)/2\rfloor,\qquad
 w_i=2\cosh(\alpha_i/N),\quad |\alpha_i|\le A.
\]
Here \(T_N\) is the Chebyshev polynomial, whereas \(T\) below
is the original tangle turn. Set
\[
 B_N=\operatorname{can}\prod_{i=1}^r K_N(w_i,Z),\qquad
 F_N=T(R^nB_N).
 \tag{1}
\]
The empty product is one. Equivalently, with \(\phi_N\) the
original trace in the variable \(W\),
\[
 F_N(Z)=\phi_{N,W}\left[
 K_N(Z,W)R^n(W)\prod_{i=1}^rK_N(w_i,W)\right].
 \tag{2}
\]
No factor in this expression is replaced by its absolute value.

Let \(L_n(u)\), for \(0<u<1/2\), be the largest logarithmic
modulus of the terminal physical shift roots, as in the literal
leaf theorem. It is nonnegative and integrable, satisfies
\(L_{-n}=L_n\), and vanishes for \(n=\pm1\).
Put \(L_0=0\), and define
\[
 \mathcal J_n(u)=\int_0^u L_n(v)\,dv,\qquad 0\le u\le1/2.
 \tag{3}
\]
Thus \(\mathcal J_n\) is continuous and nondecreasing,
\(\mathcal J_n(0)=0\), and
\(\mathcal J_n(1/2)=\mathcal I_n\).

Write
\[
 c_N(u)=2\cos(2\pi u+\pi/N),\qquad
 \dot F_{N,j}=
 \left.\frac{d}{du}F_N(c_N(u))\right|_{u=j/N}.
 \tag{4}
\]
This derivative is taken in the ordinary polynomial before
evaluation. At a double spectral node it retains the full first
normal. At the simple spectral node \(c_{J_N}=-2\), present
when \(N\) is odd, the angular derivative is zero.

**Theorem 1.** The original physical values and angular first
normals obey
\[
 \limsup_{N\to\infty}\max_{0\le j\le J_N}
 \left\{
 \frac1N\log\left(
 1+\sup_{|\boldsymbol\alpha|\le A}
       \bigl[|F_N(c_j)|+|\dot F_{N,j}|\bigr]\right)
 -\mathcal J_n(j/N)
 \right\}\le0.
 \tag{5}
\]
The same bound holds after any fixed derivatives in the exterior
parameters \(\alpha_i\), or in \(w_i\). At the double physical
nodes, \(\dot F_{N,j}\) can be replaced by the first spectral
derivative \(F_N'(c_j)\). No first spectral derivative is needed
at the odd simple node.

The theorem is an upper estimate. It does not assert that every
row achieves this exponent.

## 2. Proof by stopping the actual recurrence

For \(n=0,\pm1\), the whole-interval leaf theorem gives a
subexponential real norm, uniformly on larger parameter disks.
Markov's inequality gives the same rate for the first derivative.
This proves (5), since \(\mathcal J_n=0\).

Suppose \(|n|\ge2\). We can assume \(r\ge1\). Indeed, if the
product is empty, insert the exact constant factor
\[
 K_N(c_0,Z)=1,\qquad c_0=2\cosh(i\pi/N).
 \tag{6}
\]
This is one fixed microscopic parameter \(\alpha=i\pi\).
It does not change the source or its derivatives in any of the
original exterior parameters.

Use the actual value-and-normal recurrence of the literal leaf
theorem, including the gauged source channels and their forced
recovery. Its initial fixed rows have polynomial bounds. Let
\(0<\epsilon<1/8\) be fixed.

For rows below \(\epsilon N\), that theorem's left-end estimate,
applied to every prefix of the left strip, gives
\[
 \frac1N\log\left(1+\sup_{\boldsymbol\alpha}
       [|F_N(c_j)|+|\dot F_{N,j}|]\right)
 \le C\epsilon\log(e/\epsilon)+o_\epsilon(1).
 \tag{7}
\]
The constant \(C\) is independent of \(\epsilon\).
Finitely many initial rows are included by their polynomial
source bounds. Since \(\mathcal J_n\ge0\), subtracting
\(\mathcal J_n(j/N)\) preserves this upper bound.

On \(\epsilon N\le j\le(1/2-\epsilon)N\), stop the compact
propagation at the row that generates \(F_N(c_j)\) and its
first normal. The source and recovery windows have fixed
length, so their centers differ from \(j\) by a fixed number
of rows. The compact-prefix bound of the literal leaf theorem
therefore gives, uniformly in these rows,
\[
 \begin{split}
 \frac1N\log\left(1+\sup_{\boldsymbol\alpha}
       [|F_N(c_j)|+|\dot F_{N,j}|]\right)
 \le{}&C\epsilon\log(e/\epsilon)
       +\int_\epsilon^{j/N}L_n(v)\,dv
       +o_\epsilon(1).
 \end{split}
 \tag{8}
\]
For fixed \(\epsilon\), changing either integration endpoint
by a fixed number of rows changes the exponent by \(O_\epsilon(1)\)
before division by \(N\). The recurrence's multiple-root error
is \(O_\epsilon(N^{-1/(66r)})\) after that division.
Again (8) minus \(\mathcal J_n(j/N)\) is at most
\(C\epsilon\log(e/\epsilon)+o_\epsilon(1)\).

For \(j>(1/2-\epsilon)N\), use the whole-interval estimate
and Markov's inequality. They give
\[
 \frac1N\log\left(1+\sup_{\boldsymbol\alpha}
       [|F_N(c_j)|+|\dot F_{N,j}|]\right)
 \le\mathcal I_n+o(1).
 \tag{9}
\]
On this last set of rows,
\[
 0\le\mathcal I_n-\mathcal J_n(j/N)
 \le\int_{1/2-\epsilon}^{1/2}L_n(v)\,dv.
 \tag{10}
\]
This argument also includes the final recovery rows and the
odd simple node. Combining the three ranges, taking the
upper limit in \(N\), and then letting \(\epsilon\) decrease
to zero proves (5).

For a double spectral node,
\[
 |c_N'(j/N)|=4\pi|\sin((2j+1)\pi/N)|\ge c/N
 \tag{11}
\]
for an absolute \(c>0\). Dividing the angular derivative
by this number costs only a polynomial factor, proving the
first-spectral-normal assertion.

All estimates are uniform on larger fixed complex parameter
disks, so Cauchy's formula proves the assertion for fixed
\(\alpha_i\) derivatives. For derivatives in \(w_i\), the
source is even in \(\alpha_i\). Set \(\beta_i=\alpha_i^2\).
The map
\[
 \beta_i\longmapsto
 N^2\bigl(2\cosh(\sqrt{\beta_i}/N)-2\bigr)
 =\beta_i+O(N^{-2})
 \tag{12}
\]
has a uniformly regular analytic inverse on any fixed smaller
bounded domain, for large \(N\). Cauchy estimates in \(\beta_i\)
then show that each fixed \(w_i\) derivative costs only a
factor of order \(N^2\). This leaves the exponential rate
unchanged. \(\square\)

## 3. Equality with the previously normalized phase action

For \(m=|n|\ge2\), use exactly the stationary action of the
action-calibration theorem:
\[
 S_m(s)=\psi(t_m(s),s)+\frac{im}{4\pi}t_m(s)^2-it_m(s),
 \qquad 0\le s<\pi.
 \tag{13}
\]
Here \(\psi\) is its specified original edge phase,
\(t_m(s)=2\arccos\zeta_m(\cos(s/2))\), and \(\zeta_m(h)\)
is the dominant first-quadrant branch of
\(\zeta U_{m-1}(\zeta)=ih\).
For \(m\ge3\) it starts at \(\cos(\pi/m)\) as \(h\) decreases
to zero; for \(m=2\) it is \(e^{i\pi/4}\sqrt{h/2}\).
The calibration theorem fixes all logarithmic branches and
the endpoint constant:
\[
 \frac{d}{du}\operatorname{Re}S_m(\pi-2\pi u)=L_m(u),
 \qquad S_m(\pi)=-i\pi/m.
 \tag{14}
\]
Integration gives the identity at every boundary angle,
\[
 \boxed{\ \mathcal J_n(u)
       =\operatorname{Re}S_{|n|}(\pi-2\pi u).\ }
 \tag{15}
\]
For negative powers the reflected phase has the same real part.

At the actual physical color put
\[
 s_{N,j}=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos s_{N,j}.
 \tag{16}
\]
Then (15) evaluates at \(u=(j+1/2)/N\), whereas (5) uses
\(j/N\). The difference is uniformly \(o(1)\), because
\(\mathcal J_n\) is continuous on the closed interval.
Consequently the upper exponent in (5) may equivalently be
written \(\operatorname{Re}S_{|n|}(s_{N,j})\).

This is an exact phase normalization attached to a proved
physical-color upper estimate. It does not prove that the
stationary phase is realized by positive cells for every
boundary angle, or that its coefficient in the closed knot
evaluation is nonzero.

## 4. Scope and direct sources

The refined exponent is attached to physical values and their
first normals. Global Hermite reconstruction uses data from all
rows, so it need not preserve this smaller exponent at points
between rows. Nor does a global Markov bound establish the
same exponent for higher spectral derivatives. An estimate
on a fixed complex boundary contour requires a further argument.

In a geometric comparison, the boundary incidence variable
conjugate to its imaginary angle must also be retained.
Setting that incidence to zero is not the same as requiring
a real external color. No convex-minimization identity for
that boundary variable is asserted here.

Complete direct sources were read at these unchanged versions:

* [Literal filled-leaf theorem](research_filled_leaf_endpoint_product_upper_bound.md),
  SHA256 5a5f9be510823289b97c1c4df6104d95156b43a881fe148adf592ed5b5adc844.
  Its actual initial traces, full value-and-normal recurrence,
  compact prefix estimate, endpoint estimates and whole norm
  bound are used.
* [Terminal action calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd.
  Its normalized phase, branch choices, integrability, derivative
  identity and endpoint constant are used.

The proof uses written mathematics only. Public manuscripts and
documentation are unchanged.
