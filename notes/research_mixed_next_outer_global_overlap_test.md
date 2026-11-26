# A global radical test from the central analytic and interior inverses

Private exact-source proof, 8 November 2026. The central analytic test
can be matched to the actual interior Dirichlet solution on an
overlap. The resulting global polynomial test satisfies the three
original endpoint conditions exactly. Its error consists of the
central analytic residual, six exponentially small interface rows,
and the original far-side terms. There is no unestimated matching
matrix or replacement of full Hermite data by shortened normals.

The exponential rate obtained here is positive, but is not sufficient
for the required outer action budget. All residuals remain in the
original coherent observation. No mathematical numerical evaluation
or frozen-source edit is used.

## 1. Original full source and the central analytic test

Use the notation and complete source of
[the complete-color layer reduction](research_mixed_next_outer_complete_color_layer_reduction.md):
\[
\begin{gathered}
m=\lfloor N/2\rfloor,\quad U=m-1,\quad M=\lceil N/2\rceil,\quad
q=e^{\pi i/N},\quad \kappa_N=q^{(N-1)^2/2},\\
u_j=\pi-(2j+1)\pi/N,\quad c_j=-2\cos u_j,\quad 0\le j\le U,\\
q_j=Q_N^{\rm full}(c_j),\qquad
\mathcal L_N(F)=\phi_N(R^3e_MFQ_N^{\rm full})
                  =\sum_{j=0}^{U}\mu_jF(c_j)q_j,\\
\mu_j=(-1)^U\kappa_N^3\omega_N(u_j)q^{3j(j+1)},\qquad
\omega_N(u)=
\begin{cases}
\sin u,&N\ {\rm even},\\
\sin u\sin(u/2)/\cos^2(\pi/(2N)),&N\ {\rm odd}.
\end{cases}
\end{gathered}                                                     \tag{1}
\]
Here \(F\) is an arbitrary ordinary polynomial until the actual
insertion is specified. Its coefficients may depend on \(N\).
That application retains the actual complete reference of an original
word in powers three and four beginning \(343\), of length at least
five, with \(w=-2\) and \(Z=Z_*\).
The original full equation is
\[
\mathcal D_{3,N}Q_N^{\rm full}=\mathfrak f_N1,\qquad
\mathfrak f_N=
\begin{cases}
4\kappa_N^3/N^2,&N\ {\rm even},\\
0,&N\ {\rm odd}.
\end{cases}                                                       \tag{2}
\]
The scalar \(q\) in (1) is distinct from the full source values \(q_j\).

Keep the ordinary operator and reversed three-node factor of
[central regularization](research_mixed_next_outer_central_regularized_operator.md):
\[
\begin{split}
\mathcal B_N
 &=q^{-2}\mathcal L_2(\mathcal L_3^2-I)
       +q^{-3}Z\mathcal L_3-8q^{-2}\mathcal L_3+(8q^{-1}+2)I,\\
Q_N^{\rm rev}(z)&=\prod_{\nu=0}^{2}(z-c_{U-\nu}),\qquad
E_N(u)=e_M(-2\cos u),\\
\mathcal C_Ng
 &=E_N^{-1}\mathcal B_N\!
       \left(E_NQ_N^{\rm rev}(-2\cos u)g(u)\right).
\end{split}                                                       \tag{3}
\]
Its grouped even-analytic continuation, not its separate pole-bearing
coefficients, is used throughout.

Choose fixed \(0<r<R<R_0\), with \(R<1/2\), in the domain of
the central regularization theorem. For
\[
F_N^{\rm ang}(u)=F(-2\cos u),\qquad
\mathcal M_N=\|F_N^{\rm ang}\|_{D_R},\qquad
G_N=\max_{0\le j\le U}|F(c_j)|,\qquad
K_N=\max\{\mathcal M_N,G_N\},
                                                                    \tag{4}
\]
that theorem constructs an even analytic \(g_N\) and \(\rho_N\),
with a remaining layer for all finite shifts, such that on \(D_r\)
\[
\begin{gathered}
h_c(u)=Q_N^{\rm rev}(-2\cos u)g_N(u),\\
\mathcal B_N(E_Nh_c)=E_N(F_N^{\rm ang}-\rho_N),\\
\|h_c\|_{D_r}\le C\mathcal M_N,\qquad
\|\rho_N\|_{D_r}\le e^{-cN}\mathcal M_N,\qquad c>0.
\end{gathered}                                                     \tag{5}
\]
The constant bounding \(Q_N^{\rm rev}\) on this fixed disk is
uniform in \(N\) and both parities. In particular
\[
h_c(u_U)=h_c(u_{U-1})=h_c(u_{U-2})=0
                                                                    \tag{6}
\]
for all sufficiently large \(N\). No zeros of the target \(F\)
are assumed.

## 2. Why matching nodal tests preserves the full Hermite data

For a global polynomial \(h\), the original radical test is
\(R^3e_Mh\). Its values vanish at every distinct physical node,
including the odd simple node. At each double node its only
nonzero required jet is
\[
\left.\partial_u\bigl[(R^3e_Mh)(-2\cos u)\bigr]\right|_{u=u_j}
       =2\sin u_j\,R(c_j)^3e_M'(c_j)h(c_j).
                                                                    \tag{7}
\]
Thus all full input jets depend only on the nodal values of \(h\).
The exact grouped formulas (7), (9), (12)--(14) of
[the endpoint theorem](research_mixed_next_outer_adjoint_radical_endpoint_conditions.md)
propagate those full jets. Each ordinary \(\mathcal L_n\) has
nearest-neighbor dependence; the ordered operator in (3) therefore
has width three. At a coalescing node the grouped formulas cancel
all apparent higher derivatives. The same statement applies to
local even analytic inputs on every neighborhood containing the
required shifted nodes.

Consequently two tests with identical nodal values on a
three-neighbor stencil have identical relevant output jets there.
If one is the local test \(h_c\), its output is exactly that in
(5), including at the central coalescing nodes. This is a statement
about the full grouped maps, not a conclusion from agreeing
ordinary values of two shortened kernels.

For a global \(h\) satisfying (6), the endpoint theorem gives
\[
\mathcal D_{3,N}^{\rm t}(R^3e_Mh)
     =R^3e_M\widetilde h\quad\hbox{in }\mathcal A_N,
\qquad
\mathcal B_N(e_Mh)/e_M\in\mathbb C[z].
                                                                    \tag{8}
\]
The ordinary quotient in the second expression supplies a
representative for \(\widetilde h\). In the regular interior,
its nodal action is the exact weighted sequence adjoint:
\[
\widetilde h_i=\sum_{|j-i|\le3}A_{ij,N}h(c_j),\qquad
A_{ij,N}=\frac{\mu_j}{\mu_i}d_{j,i-j,N}.
                                                                    \tag{9}
\]
Here \(d_{j,s,N}\) are the original seven-term coefficients;
all crossing phases and scalar factors in (9) are retained.
Only regular interior indices are used for this displayed
coefficient formula. At the center, (7)--(8) and the grouped
maps supply its endpoint completion.

Finally every choice of the \(m\) double-node test values has a
unique interpolating polynomial \(h\) of degree less than \(m\).
If its last three values are zero, this polynomial is divisible
by \(Q_N^{\rm rev}\). Its value at the odd simple node need
not be separately prescribed: multiplication by \(e_M\), and
then the endpoint theorem, supplies exactly the required full
simple-node behavior. No bound on coefficients of this
interpolating polynomial will be needed.

## 3. Interior solution with prescribed central exterior data

Fix
\[
0<\delta_0<\delta_s<\delta_1<r,\qquad
a=\lfloor N/24\rfloor,\qquad
b(\delta)=\left\lfloor\frac{N(\pi-\delta)}{2\pi}-\frac12\right\rfloor.
                                                                    \tag{10}
\]
Write
\[
b_0=b(\delta_0),\qquad s=b(\delta_s),\qquad c_1=b(\delta_1),
\qquad I=[a,b_0],\quad J=[c_1,b_0].
                                                                    \tag{11}
\]
All intervals here and below consist of integers. For sufficiently
large \(N\), they are nonempty, lie in one fixed regular interior
chart, and have all required neighboring indices. In particular
\(a<c_1<s<b_0<U-3\). The local stencil at \(c_1\) lies
inside \(D_r\).

The actual zero-extended matrices on both \(I\) and \(J\) obey
the interior Dirichlet theorem and the banded inverse estimate
of the complete-color layer reduction. With constants common to
these intervals and both parities,
\[
|A_{I}^{-1}(i,\ell)|,\ |A_J^{-1}(i,\ell)|
       \le\tfrac12 e^{-\gamma|i-\ell|},\qquad
\|A_I^{-1}\|_{\infty\to\infty},
\|A_J^{-1}\|_{\infty\to\infty}\le C_\infty.
                                                                    \tag{12}
\]
The corresponding matrix is meant in each term of (12).
For example one may choose
\(\gamma=\frac13\log(1+1/(7C_A))\), where \(C_A\ge1\)
bounds every entry in (9) on the fixed chart.

Define \(h_I\) by the exact nonzero-exterior Dirichlet problem
\[
\sum_{j\in I}A_{ij,N}(h_I)_j
 =F(c_i)-\sum_{\substack{b_0<j\le b_0+3\\|j-i|\le3}}
                A_{ij,N}h_c(u_j),\qquad i\in I.
                                                                    \tag{13}
\]
At the left exterior nodes prescribe zero; at the right exterior
nodes prescribe \(h_c(u_j)\). Equation (12) solves (13) uniquely,
and the fixed coefficient bounds and (5) give
\[
                       \|h_I\|_\infty\le C K_N.
                                                                    \tag{14}
\]
This is the original adjoint matrix with its actual phases.
The exterior values have not been absorbed into a changed source.

On \(J\), put \(e_i=(h_I)_i-h_c(u_i)\). Its three right
exterior values are zero. Its left exterior values, at
\(c_1-3,c_1-2,c_1-1\), have modulus at most \(C K_N\).
By (5), (9), and (13), it satisfies
\[
A_J e=\rho_J-f_L,\qquad
(f_L)_i=
\sum_{\substack{c_1-3\le j<c_1\\|j-i|\le3}}A_{ij,N}e_j .
                                                                    \tag{15}
\]
The vector \(f_L\) is supported on the first three rows of \(J\)
and has norm at most \(C K_N\). Thus (12) proves, for \(i\in J\),
\[
|e_i|
 \le C\mathcal M_Ne^{-cN}
       +C K_N e^{-\gamma(i-c_1-2)} .
                                                                    \tag{16}
\]
A negative exponent distance in this formula only enlarges its
right side; we use it a fixed positive distance into the overlap.

Set
\[
\kappa=\frac{\gamma(\delta_1-\delta_s)}{4\pi}>0,\qquad
\epsilon_N=\mathcal M_Ne^{-cN}+K_Ne^{-\kappa N}.
                                                                    \tag{17}
\]
The exact floor convention gives
\(s-c_1\ge N(\delta_1-\delta_s)/(2\pi)-1\).
After absorbing the fixed offsets in (16), for all large \(N\)
\[
                    |e_i|\le C\epsilon_N
                    \quad(s-2\le i\le s+3).
                                                                    \tag{18}
\]
No three-dimensional interface inverse is invoked.

## 4. The global polynomial test and all of its residual rows

Prescribe the following nodal values, and interpolate by the
unique polynomial \(\bar h_N\) of degree less than \(m\):
\[
\bar h_N(c_j)=
\begin{cases}
0,&0\le j<a,\\
(h_I)_j,&a\le j\le s,\\
h_c(u_j),&s<j\le U.
\end{cases}                                                       \tag{19}
\]
Its last three values vanish by (6), so
\(\bar h_N\in Q_N^{\rm rev}\mathbb C[z]\).
Equations (7)--(8) therefore produce a global radical output
\[
\mathcal D_{3,N}^{\rm t}(R^3e_M\bar h_N)
          =R^3e_M\widetilde h_N .
                                                                    \tag{20}
\]
Define the exact nodal residual
\[
                         r_j=F(c_j)-\widetilde h_N(c_j).
                                                                    \tag{21}
\]
Width-three dependence gives the complete inventory:
\[
\begin{array}{c|c}
\text{indices}&r_i\\ \hline
0\le i<a&F(c_i)-\widetilde h_N(c_i)\\
a\le i\le s-3&0\\
s-2\le i\le s&
 \displaystyle\sum_{\substack{j>s\\|j-i|\le3}}A_{ij,N}e_j\\
s+1\le i\le s+3&
 \displaystyle\rho_N(u_i)
      -\sum_{\substack{j\le s\\|j-i|\le3}}A_{ij,N}e_j\\
s+4\le i\le U&\rho_N(u_i).
\end{array}                                                       \tag{22}
\]
For the first line, \(\widetilde h_N(c_i)=0\) if \(i<a-3\);
its remaining three entries are regular and bounded by \(C K_N\).
The last line uses the full grouped endpoint argument of Section 2,
not an ungrouped difference formula at a coalescing pole.
In particular
\[
|r_i|\le
\begin{cases}
C K_N,&i<a,\\
C\epsilon_N,&s-2\le i\le s+3,\\
\mathcal M_Ne^{-cN},&i\ge s+4.
\end{cases}                                                       \tag{23}
\]
There are six interface rows because both sides of a width-three
splice have changed. All six signs are displayed in (22).
Every test value obeys \(|\bar h_N(c_j)|\le C K_N\).

Apply the original full Frobenius transpose to (20), then use (2).
The endpoint theorem removes every newly exposed first normal
and the odd simple-node term exactly, because the test satisfies
the three zero conditions. The resulting global identity is
\[
\boxed{\quad
\mathcal L_N(F)
  =\mathfrak f_N\sum_{j=0}^{U}\mu_j\bar h_N(c_j)
       +\sum_{j=0}^{U}\mu_jr_jq_j .
\quad}                                                            \tag{24}
\]
This is an exact identity of the original full finite source.
At odd levels the forcing vanishes. At even levels it has the
same \(4\kappa_N^3/N^2\) factor as before. No shortened first
normal, arbitrary odd simple value, or replacement trace is used.

## 5. Source estimates and the remaining action deficit

Every far node \(j<a\) lies in the adopted whole-kernel region
\(u_j\ge11\pi/12\), so
\[
|q_j|\le C N^A e^{8N/5}\qquad(j<a).
                                                                    \tag{25}
\]
Since \(|\mu_j|\le2\), (23)--(25) and the exact forcing yield
\[
\boxed{\quad
\left|\mathcal L_N(F)\right|
 \le C N^A K_Ne^{8N/5}
       +C\epsilon_N
                   \sum_{j=s-2}^{U}|\mu_jq_j| .
\quad}                                                            \tag{26}
\]
This positive inequality is only a bound for the retained
residual in (24); the exact identity keeps its correlated signs.

For the actual insertion \(F=H_N(\cdot,Z_*)\), the
[fixed spectral ellipse theorem, equation (9)](research_mixed_next_middle_fixed_spectral_ellipse.md)
applies both to the real spectral interval and to
\(-2\cos(D_R)\), since \(R<1/2\). Therefore, for every \(\tau>0\),
\[
K_N\le C_\tau N^{A_\tau}e^{N(E_*+\tau)},\qquad
E_*=\Lambda-\frac{2383}{1500}-\frac1{50}.
                                                                    \tag{27}
\]
This uses the actual outgoing polynomial after its full summation
and its original small-index subtraction. No generic coefficient
degree penalty is substituted for that source theorem.
Taking \(\tau=1/3000\) pays the first term in (26) at the same
eventual \(\Lambda-1/200\) rate as the original layer reduction.

One can also choose \(\delta_1\) inside the fixed complete-color
packet neighborhood of
[the degree-two theorem](research_all_nonzero_degree_two_fillings.md).
Writing \(\mathfrak M_3=\Re S_3(0,0)\), continuity and that full
holomorphic packet give a number \(\omega(\delta_1)\to0\) as
\(\delta_1\downarrow0\) such that
\[
\sum_{j=s-2}^{U}|\mu_jq_j|
 \le C N^A e^{N(\mathfrak M_3+\omega(\delta_1))}
                                                                    \tag{28}
\]
for all sufficiently large \(N\). This is an upper bound for
the full values; no relative packet error is deleted inside
the exact residual sum.

Let \(c_{\rm match}=\min\{c,\kappa\}>0\).
Equations (26)--(28) give the explicit available residual rate
\[
E_*+\tau+\mathfrak M_3+\omega(\delta_1)-c_{\rm match}.
                                                                    \tag{29}
\]
The matching theorem does not assert that (29) is below
\(\Lambda\). Indeed the displayed construction in central
regularization has
\[
c=\frac{(R-r)\log4}{8M_{r,R}},\qquad
M_{r,R}\ge12\pi,\qquad R-r<1,
\]
and hence \(c<1/192\), using \(\log4<3/2\) and \(\pi>3\).
On the other hand the adopted complete action satisfies
\(\mathfrak M_3>9/5\), so
\[
\mathfrak M_3-\frac{2383}{1500}-\frac1{50}
                         >\frac{287}{1500}>\frac1{192}.
                                                                    \tag{30}
\]
Thus this particular generic-norm residual estimate is
insufficient for the desired exponent. This comparison
does not lower-bound the residual or the signed observation.

The original transfer still contains
\((-q)^M\mathcal L_N(H_N)/(\kappa_N^2N)\), with its original
two Fourier sectors, geometric term, and separately paid errors.
Equation (24) may be inserted into that identity without any
change of normalization. It supplies a genuine global radical
test and controlled matching residuals; it does not establish
surjectivity of the constrained adjoint, an exact zero-residual
completion, or suppression of the remaining outer correction.

## Source versions

- Central regularized operator:
  244a089f0046f1a8b81f55941c17c32304eb3fd679aa933361ebacbfa416f9a8.
- Full adjoint endpoint conditions:
  9cde443d65bfdc41104ffe9e78ce4e4540ec998b53681923f99fd42a5d436d71.
- Interior Dirichlet inverse:
  e1b713461bacdf263c07c3baa21de67960fae5e5e2735e5c400c009c987afddf.
- Complete-color layer reduction:
  0a5a1f9c970edca8be9268b966aef6add07a18d08af884629fd8258c7a7e7108.
- Fixed spectral ellipse:
  dc656300238775a26ac4af0309b7be66405334b93e0ca60b12d4c895dfdfd1b6.
- All nonzero degree-two fillings:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
