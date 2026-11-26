# An exponentially accurate slow graph for the actual filled-leaf state

Private written proof, 16 November 2026.

For every fixed integer filling power of absolute value at least two,
the normalized actual leaf companion has one unit spectral cluster
and a strictly stable complement on each fixed bulk interval.
The entire unit cluster, including its independent normal copy,
admits a bounded holomorphic graph with exponentially small
invariance defect. The actual state is exponentially close to this
graph after a fixed left buffer. Its slow rank is independent of
the magnitude of the filling power.

The retained slow transfer and its inverse have subexponential
cost. This transports a suitable already established lower norm;
it neither supplies that lower norm nor estimates a scalar closing.
No first normal is identified with a derivative of an interpolated
value amplitude.

## 1. Actual companion and its principal unit cluster

Use the original source
\[
 F_N=T(R^nB_N),\qquad
 B_N=\operatorname{can}\prod_{i=1}^{r}
                     K_N(2\cosh(\alpha_i/N),Z),
 \qquad |n|\ge2,\quad |\alpha_i|\le A.
 \tag{1}
\]
Here \(n\) and \(r\) are fixed integers, \(r\ge1\). An empty
endpoint product can be padded by the exact constant
\(K_N(c_0,Z)=1\), with \(\alpha=i\pi\); in all dimension
counts below use the padded number of factors.
The quotient, carriers, turns and full physical jets are the
original ones. Exterior parameters are not quotiented.

Put \(h=N^{-1}\), \(u_j=jh\). On a fixed buffered interval
inside \(0<u<1/2\), take the complete normalized state of the
jet-adjoint theorem:
\[
 X_{j+1}=Q_h(u_j,\boldsymbol\alpha)X_j,\qquad
 \sup_{\boldsymbol\alpha,j}\|X_j\|\le {\cal B}_N,\qquad
 \log(1+{\cal B}_N)=o(N).
 \tag{2}
\]
It contains the gauged source channels, their shifted values,
the forced recovered product, and both actual first-normal
blocks divided by \(N\). Every component is multiplied by
the same base-row phase
\[
 \exp[-N{\cal S}_h(u_j)],\qquad
 {\cal S}_h(u)=S_n(\pi-2\pi u-\pi h).
 \tag{3}
\]
The original phase branch and its additive constant are
unchanged. The cited source proves (2) simultaneously for
every channel on a fixed bulk buffer, uniformly on larger
bounded complex parameter sets. It also proves that \(Q_h\)
is holomorphic and bounded on a fixed complex \(u\)-neighborhood,
with a bounded analytic expansion at \(h=0\).
No off-grid holomorphic estimate for \(X_j\) is asserted.

**Lemma 1.** The unit eigenvalue of \(Q_0(u)\) has algebraic
multiplicity
\[
                            d_{\rm s}=4\,6^r.
 \tag{4}
\]
On its generalized eigenspace the restriction \(A_0(u)\)
satisfies
\[
                           (A_0-I)^2=0.
 \tag{5}
\]
On any fixed closed bulk interval all remaining eigenvalues
have modulus at most some \(\rho<1\). These assertions hold
uniformly in the stated parameters; \(Q_0\) is independent
of the microscopic parameters.

*Proof.* Write \(k=33r\), \(m=|n|\). The unnormalized gauged
companion has \(6^r\) scalar principal copies with symbol
\[
                         (y-2)^k(x_{-n}-2).
 \tag{6}
\]
Each of the \(m\) distinct selected terminal roots has
multiplicity two. The recovery companion has only the
unit root, with multiplicity \(2r\). The exact signed
identity proved in the jet-adjoint note is
\[
                    e^{{\cal S}_0'(u)}
                              =\tau_{\max,-n}(u).
 \tag{7}
\]
This root is uniquely largest in modulus and has modulus
strictly greater than one. Dividing the entire matrix by
it makes its terminal root one and places every other
root strictly inside the unit disk.

There are two copies of the gauged principal companion,
one for values and one for normals. More explicitly the
scaled finite matrix before phase normalization is
\[
 \begin{pmatrix}
 A_{\cal F}&0&0&0\\
 hA_{\cal F}'&A_{\cal F}&0&0\\
 B&0&A_F&0\\
 hB'&B&hA_F'&A_F
 \end{pmatrix}.
 \tag{8}
\]
The derivative couplings vanish at \(h=0\). After reordering,
the principal matrix consists of two copies of a lower
triangular gauged/recovery system. Recovery has spectrum
disjoint from the maximal terminal root. Its coupling
therefore does not increase that root's multiplicity or
Jordan length: on this generalized eigenspace its
recovery coordinate is solved by an invertible finite
Sylvester equation, or directly by the resolvent of the
recovery block. A scalar companion at a double, separated
root has one Jordan block of length two. Hence each of the
two copies contributes \(2\,6^r\), proving (4)--(5).

The limiting gauged coefficients come from
\(d(Z)\to(Z-2)^k\); the \(s^2E\) correction vanishes,
and recovery is the fixed equation \((J-2)^rF={\cal F}_*\).
Thus these principal coefficients and their selected-component
recovery map have no microscopic parameter dependence.
Strict modulus ordering and compactness give \(\rho<1\).
All multiplicities, including the independent normal copy,
have been counted. \(\square\)

## 2. A holomorphic fixed splitting of the principal state

Fix a closed interval \(J=[a_0,b_0]\Subset(0,1/2)\), with
a slightly larger real buffer on which (2) holds. For
\(R>0\) write
\[
                U_R=\{u\in\mathbb C:\operatorname{dist}(u,J)<R\}.
 \tag{9}
\]
All constants below may depend on this fixed interval,
\(n,r,A\), and chosen smaller buffers, but not on \(N\).

Choose a sufficiently small circle around \(1\), separating
it from the other eigenvalues for every real \(u\) in the
buffer. By continuity the same circle separates the spectra
on a sufficiently thin fixed tube \(U_R\).
The Riesz projection
\[
 P_0(u)=\frac1{2\pi i}
             \int_{\gamma}(zI-Q_0(u))^{-1}\,dz
 \tag{10}
\]
is bounded and holomorphic there, with rank \(d_{\rm s}\).
It commutes with \(Q_0\).

Here is an explicit way to use one splitting on the whole
interval, rather than unrelated pointwise bases. Set
\[
 K(u)=[P_0'(u),P_0(u)],\qquad
 T'(u)=K(u)T(u),\qquad T(u_*)=I
 \tag{11}
\]
at one real \(u_*\in J\).
The tube is simply connected. The holomorphic linear ODE
has an invertible holomorphic solution there; on a smaller
closed tube both it and its inverse are bounded. This also
follows from the usual integral iteration on finite disks
and continuation along paths of bounded length.
Differentiating \(P_0^2=P_0\) gives
\([K,P_0]=P_0'\), so \(T^{-1}P_0T=P_0(u_*)\).
Compose \(T\) with a fixed basis for the range and kernel
of \(P_0(u_*)\). Denote the resulting bounded frame by
\(\mathcal T(u)\).

Use this moving frame at the two ends of the actual step:
\[
 Z_j=\mathcal T(u_j)^{-1}X_j,\qquad
 \widetilde Q_h(u)=\mathcal T(u+h)^{-1}
                         Q_h(u)\mathcal T(u)
             =\begin{pmatrix}A_h&B_h\\C_h&D_h\end{pmatrix}.
 \tag{12}
\]
Its principal matrix is \(\operatorname{diag}(A_0,D_0)\).
On fixed complex buffers, uniformly in the parameters,
\[
 A_h=A_0+O(h),\quad D_h=D_0+O(h),\quad
                         B_h=O(h),\quad C_h=O(h).
 \tag{13}
\]
All these statements include fixed holomorphic derivatives.
The eigenvalues of \(D_0\) have modulus at most \(\rho<1\)
on the real interval. No claim that \(\|D_0\|<1\) in the
chosen matrix norm is needed.

Put \(J_0=A_0-I\), so \(J_0^2=0\). The Sylvester operator
on rectangular matrices,
\[
                   {\cal L}_u(R)=RA_0-D_0R,
 \tag{14}
\]
has the explicit holomorphic inverse
\[
 {\cal L}_u^{-1}(F)
      =(I-D_0)^{-1}F-(I-D_0)^{-2}FJ_0 .
 \tag{15}
\]
Multiplying out proves this formula. The inverse is uniformly
bounded on a smaller fixed tube, since \(1\) is outside
the stable spectrum. Thus no separation within the unit
cluster or within the stable cluster is imposed.

## 3. A nonlinear graph with exponentially small defect

For a matrix function \(R\), write \(R_+(u)=R(u+h)\).
An invariant graph \(y=R(u)x\) for (12) would satisfy
\[
                    R_+(A_h+B_hR)=C_h+D_hR.
 \tag{16}
\]
We construct a finite analytic approximation to this equation.
Define
\[
 {\cal F}_h(R)={\cal L}^{-1}\!
 \left[
 C_h+(D_h-D_0)R-R(A_h-A_0)
       -(R_+-R)A_h-R_+B_hR
 \right].
 \tag{17}
\]
All multiplications in (17) occur at \(u\), except the
explicit \(R_+\). Direct expansion gives the exact identity
\[
 R_+(A_h+B_hR)-C_h-D_hR
                         ={\cal L}\bigl(R-{\cal F}_h(R)\bigr).
 \tag{18}
\]
Thus this construction keeps the nonlinear term; it is not
the triangular switching equation from the earlier note.

**Theorem 2.** On a fixed smaller tube, there are holomorphic
matrices \(R_h\), uniform on the fixed parameter polydisk, with
\[
 \|R_h\|\le C h,\qquad
 E_h:=R_{h,+}(A_h+B_hR_h)-C_h-D_hR_h,\qquad
                       \|E_h\|\le C e^{-\kappa/h}
 \tag{19}
\]
for some \(\kappa>0\) and all sufficiently small
physical \(h=1/N\). Every fixed derivative in \(u\) or
the exterior parameters has the same bound on smaller
fixed domains.

*Proof.* We give the domain-loss estimate explicitly.
On tubes of widths \(s,s+\delta\), with \(\delta\ge2h\),
Cauchy's inequality gives
\[
 \|R_+-R\|_s\le C\frac h\delta\|R\|_{s+\delta}.
 \tag{20}
\]
Equations (13), (15), and (17) then give constants \(C_1,C_2\)
such that
\[
 \|{\cal F}_h(R)\|_s
 \le C_1h+C_2(h+h/\delta)\|R\|_{s+\delta}
                              +C_2h\|R\|_{s+\delta}^2.
 \tag{21}
\]
On a ball \(\|R\|,\|S\|\le Lh\), they also give
\[
 \|{\cal F}_h(R)-{\cal F}_h(S)\|_s
 \le C_2(h+h/\delta+2Lh^2)\|R-S\|_{s+\delta}.
 \tag{22}
\]
The constants may be enlarged to account for the bounded
shift in the quadratic term and the bounded Sylvester inverse.
They are independent of the tube widths in a fixed closed
outer tube.

Take \(L\ge2C_1+1\). Choose a fixed \(M\ge2\) sufficiently
large that \(C_2/M<1/8\), and then take \(h\) small enough
that the remaining terms in (21)--(22) give a contraction
factor at most \(1/2\) and preserve the ball of radius \(Lh\).
Reserve a fixed total tube loss \(\Delta>0\). Put
\[
 k_h=\left\lfloor\frac{\Delta}{2Mh}\right\rfloor,\qquad
                  \delta_h=\frac{\Delta}{k_h+1}.
 \tag{23}
\]
For sufficiently small \(h\), \(\delta_h\ge Mh\ge2h\).
Starting with \(R^{(0)}=0\), define the literal finite iterates
\[
                         R^{(j+1)}={\cal F}_h(R^{(j)}).
 \tag{24}
\]
Use one successive tube loss \(\delta_h\) for each
application, including the final residual application.
Induction using (21) proves \(\|R^{(j)}\|\le Lh\) on
its domain. Applying (22) to successive iterates gives
\[
 \|R^{(j+1)}-R^{(j)}\|
                     \le C_1h\,2^{-j}
 \tag{25}
\]
on the correspondingly smaller domains.
Set \(R_h=R^{(k_h)}\), and evaluate
\({\cal F}_h(R_h)\) on the final additional layer.
Equation (18) and (25) imply
\(\|E_h\|\le Ch\,2^{-k_h}\), proving (19), after
decreasing a fixed positive \(\kappa\).

The construction uses only finitely many literal shifts
and holomorphic matrix operations. It therefore preserves
holomorphic parameter dependence. The estimates were made
on larger fixed parameter domains and with additional
fixed \(u\)-buffers. Cauchy's estimates give the derivative
assertions on smaller sets. No convergence of an infinite
formal series is invoked. \(\square\)

## 4. Stable attraction of the actual source

Write \(Z_j=(x_j,y_j)\) in (12), and set
\[
 \eta_j=y_j-R_h(u_j)x_j,\qquad
 {\cal A}_h=A_h+B_hR_h,\qquad
                    {\cal D}_h=D_h-R_{h,+}B_h.
 \tag{26}
\]
Exact block multiplication, using the defect in (19), gives
\[
 \begin{split}
 x_{j+1}&={\cal A}_h(u_j)x_j+B_h(u_j)\eta_j,\\
 \eta_{j+1}&={\cal D}_h(u_j)\eta_j-E_h(u_j)x_j .
 \end{split}
 \tag{27}
\]
The error is an actual forcing term in this equation.
It is not discarded by defining an exactly invariant subspace.

**Lemma 3.** For real grid rows in the fixed interval,
\[
 \|{\cal D}_h(u_{j-1})\cdots{\cal D}_h(u_l)\|
                          \le C e^{-c(j-l)}
                         \qquad (j\ge l),
 \tag{28}
\]
uniformly in the fixed complex microscopic parameters.

*Proof.* Choose \(\rho<\rho_1<1\). The resolvent of \(D_0(u)\)
is bounded on \(|z|=\rho_1\), uniformly for real \(u\) in
the buffered interval. The finite matrix Cauchy formula gives
\(\|D_0(u)^p\|\le C\rho_1^p\).
Choose a fixed integer \(p\) making this at most \(1/4\).
Because \({\cal D}_h=D_0+O(h)\), with bounded first
derivatives, a product of \(p\) consecutive actual matrices
differs from \(D_0(u)^p\) by \(O_p(h)\), uniformly.
For small \(h\) its norm is at most \(1/2\).
The at most \(p-1\) remaining factors have bounded norms.
Splitting any product into these fixed blocks proves (28).
This argument allows nonnormal \(D_0\) and all stable
Jordan multiplicities. \(\square\)

Fix a starting row \(j_*\) with its physical coordinate
in the left part of the buffered interval. For every later
row in the interval, equations (2), (19), (27), and (28) give
\[
 \|\eta_j\|
 \le C\left(e^{-c(j-j_*)}+e^{-\kappa/h}\right){\cal B}_N .
 \tag{29}
\]
Indeed iterate the second equation of (27); the stable
geometric sum is uniformly bounded. The bounded frame and
the \(O(h)\) graph allow the same \({\cal B}_N\) up to a
constant for \(x_j,y_j,\eta_j\).

In particular, for any fixed \(\beta>0\), on the rows with
\((j-j_*)h\ge\beta\),
\[
 \boxed{\quad
 X_j=\mathcal T(u_j)
              \begin{pmatrix}x_j\\R_h(u_j)x_j\end{pmatrix}
                      +O\!\left(e^{-c_\beta/h+o(1/h)}\right),
 \quad c_\beta=\min(c\beta,\kappa)>0 .
 \quad}
 \tag{30}
\]
The bound is uniform in the stated parameters.
The left packet in (29) has not been set to zero;
it is the actual source packet and decays only after
the indicated positive-length buffer.

The same conclusion applies to every selected full-normal
component, since all component selectors and the frame
are bounded. For example the normalized combination
\(b_j/N-2\pi i\xi a_j\), for bounded real \(\xi\),
equals its original selector on the slow graph plus the
error in (30). This does not say that this selector vanishes
on the slow graph. Its independent normal coordinate is
still present.

## 5. The slow transfer costs subexponentially in both directions

The retained slow matrix satisfies
\[
                     {\cal A}_h(u)=A_0(u)+O(h)
                                   =I+J_0(u)+O(h),
                       \qquad J_0(u)^2=0 .
 \tag{31}
\]
It is invertible for small \(h\), with
\({\cal A}_h^{-1}=I-J_0+O(h)\), uniformly.
For a slow vector \(v\), use the varying norm
\[
               |v|_{u,h}=\|v\|+h^{-1/2}\|J_0(u)v\|.
 \tag{32}
\]
It obeys
\(\|v\|\le |v|_{u,h}\le Ch^{-1/2}\|v\|\).
Since \(J_0(u+h)-J_0(u)=O(h)\), equations (31)--(32) give
\[
 |{\cal A}_h(u)v|_{u+h,h}\le(1+C\sqrt h)|v|_{u,h}.
 \tag{33}
\]
To check this without a Jordan-frame assumption, first use
\((I+J_0)v=v+J_0v\) and \(J_0(I+J_0)v=J_0v\).
The extra \(\|J_0v\|\) costs at most \(\sqrt h|v|_{u,h}\).
The changes in \(J_0\) and the \(O(h)\) matrix remainder
cost \(O(\sqrt h)\|v\|\) in the weighted term.
The same argument for \(I-J_0+O(h)\), with the two
coordinates reversed, gives
\[
 |{\cal A}_h(u)^{-1}v|_{u,h}
                         \le(1+C\sqrt h)|v|_{u+h,h}.
 \tag{34}
\]

Let \({\cal U}_{j,l}\) be the product of the slow matrices
from \(l\) to \(j-1\), and use the inverse for reversed
indices. On every fixed bulk interval,
\[
 \boxed{\qquad
 \|{\cal U}_{j,l}\|+\|{\cal U}_{j,l}^{-1}\|
       \le C h^{-1/2}
                 \exp(C|j-l|\sqrt h)
                              =e^{o(1/h)} .
 \qquad}
 \tag{35}
\]
The equal-rate statement is uniform for
\(|j-l|h\) bounded. It concerns the slow matrix, not a
general turn on arbitrary polynomial inputs.

There is also an approximation by an exact slow trajectory.
Choose a row \(l\) after the buffer in (30), and define
\(\bar x_j={\cal U}_{j,l}x_l\) for subsequent rows.
The first equation of (27), the \(O(h)\) bound for \(B_h\),
and (30), (35) give
\[
 \|x_j-\bar x_j\|
                       \le e^{-c_\beta/h+o(1/h)} .
 \tag{36}
\]
There are only \(O(1/h)\) forcing terms in this comparison;
the slow products cost \(e^{o(1/h)}\). Thus the exact
original source is approximated, on a fixed inner interval,
by this specified rank-\(4\,6^r\) slow evolution and the graph.

If one separately establishes
\(\|x_l\|\ge e^{-o(1/h)}\), (35)--(36) transport the same
lower exponential rate to all later rows in that fixed
inner interval. The upper bound is already available
from (2). This conditional implication does not establish
the initial lower norm: the actual source may have an
exponentially small or zero slow projection. Moreover a
lower vector norm does not imply a lower bound for its
specified scalar observation or original shared closing.

## 6. Fixed shared products and scope

The same construction applies to a fixed tensor of actual
leaf states at a common physical color, provided every
participating power has absolute value at least two.
Use their exact tensor recurrence and total normalizing
phase, as in the jet-adjoint source. Shared microscopic
parameters are allowed. All individual normalized roots
have modulus at most one, so the unit cluster of the tensor
is exactly the tensor of the individual unit clusters.
For \(q\) factors its rank is
\[
                              \prod_{i=1}^q 4\,6^{r_i}.
 \tag{37}
\]
This again does not depend on the magnitudes of the powers.

On that cluster the principal operator is
\(\bigotimes_i(I+J_{0,i})=I+J_0^{\rm joint}\).
The matrices acting in the different tensor factors
commute and each squares to zero. Every monomial of
degree greater than \(q\) therefore vanishes, proving
\[
                       (J_0^{\rm joint})^{q+1}=0 .
 \tag{38}
\]
The Sylvester inverse (15) is replaced by the finite sum
\[
 {\cal L}^{-1}(F)=
       \sum_{k=0}^{q}(-1)^k(I-D_0)^{-k-1}
                                  F(J_0^{\rm joint})^k .
 \tag{39}
\]
All the graph and attraction estimates follow with new
fixed constants. The slow two-sided estimate follows
by replacing (32) with
\[
 \sum_{k=0}^{q}h^{-k/(q+1)}
                            \|(J_0^{\rm joint}(u))^k v\|.
 \tag{40}
\]
Its one-step cost is \(1+Ch^{1/(q+1)}\), in both directions.
To see this, multiplication by \(I+J_0^{\rm joint}\)
shifts each weighted power to the next, at cost
\(h^{1/(q+1)}\); the \(O(h)\) coefficient and base-point
changes cost at most
\(h\,h^{-q/(q+1)}=h^{1/(q+1)}\).
The inverse is the finite nilpotent geometric sum plus
\(O(h)\), with the same estimate. Hence its product
cost remains \(e^{o(1/h)}\).
The original joint first normal is selected by the exact
product rule inside this tensor, not by independent scalar
mode selection.

The estimates are uniform on larger bounded complex
parameter domains. Fixed exterior derivatives follow by
Cauchy's formula on smaller domains; the actual first
physical normals were retained from the start.
Microscopic spectral derivatives can also be treated by
the even parameter \(\alpha_i^2\), with the usual polynomial
\(N^2\) conversion cost per derivative.
This does not extend the theorem to arbitrary ordinary
free colors outside the microscopic domains.

No endpoint of the full physical interval is included
in the fixed spectral gap. The theorem neither erases
the exterior currents of the weighted trace construction
nor proves a parent-action bound. It controls the actual
state on a fixed interior interval and retains the full
unit generalized eigenspace. In particular it does not
deduce \(b_j\approx a_j'\), a scalar holomorphic amplitude,
or noncancellation from phase centering alone.

## 7. Coverage and direct sources

The archived analytic switching theorem treats a triangular
transfer and a linear Sylvester equation. Its literal-shift
nested-domain argument is the relevant prior method.
The two-way \(O(h)\) coupling, nonlinear graph iteration,
actual-source attraction, normal-cluster rank, and
two-sided slow norm estimate are proved here.

Complete direct sources were read at these unchanged pins:

* [Actual normalized leaf jet companion](research_filled_leaf_normalized_jet_adjoint.md),
  SHA256 49e6f5494df6de3b1fa0f6ad05d17ef0712fc89377cb3695ac737094bf5f9a70:
  full holomorphic companion, simultaneous normalized state
  budget, exact signed phase centering, and shared tensors.
* [Literal filled-leaf source](research_filled_leaf_endpoint_product_upper_bound.md),
  SHA256 5a5f9be510823289b97c1c4df6104d95156b43a881fe148adf592ed5b5adc844:
  original gauged/recovery block sizes, double terminal
  multiplicities, full normals, and actual source placement.
* [Analytic triangular switching suppression](research_analytic_switching_suppression.md),
  SHA256 c086980caa870e6198f77acb29680df971e6afecccb25d22b7781e3878512a84:
  prior finite nested-domain construction and the need to
  retain actual endpoint contributions.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts are unchanged.
