# An exact heat reduction of the entire charged original source

Private written proof, 16 November 2026.

The canonical real-power crossing and the full-Hermite charge coupon
give a scalar heat equation for the original source. Its initial datum
is the entire zero-power charged source, with every original kernel,
trace and outside polynomial retained. A convergent Gaussian integral
implements every fixed signed real power, and its charge contours can
be translated through any prescribed finite point without crossing a
pole. These are exact finite-source statements. They do not replace
the initial datum by one of its asymptotic branches.

The real-power semigroup and the analytic charge coupons were already
proved separately. The Gaussian-window Newton frame also already gives
exact crossing integrals. The reduction here acts on the prescribed
charged scalar itself, uses its faithful finite exponential-polynomial
space, and retains the nilpotent normal through the heat operator.
It does not use a positive norm in place of the original closing.

## 1. Original data and the entire charged observation

Let
\[
 N\ge2,\qquad D=N-1,\qquad \eta=(-1)^D,\qquad
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 P_N(z)=2T_N(z/2)+2,
\]
\[
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{1}
\]
The double nodes and their positive angular lifts are
\[
 c_a=2\cos((2a+1)\pi/N)=-2\cos\tau_a,\qquad
 \tau_a=\pi(D-2a)/N,\qquad 0\le a<\lfloor N/2\rfloor.
 \tag{2}
\]
At odd \(N\), the remaining simple node is \(-2\), with angle zero.
The exact trace is
\[
 \phi_N(f)=
 \eta\sum_{a<\lfloor N/2\rfloor}
       \{4\sin^2\tau_a\,f'(c_a)-c_a f(c_a)\}
       +\mathbf1_{N\ {\rm odd}}f(-2).
 \tag{3}
\]
In particular the factor \(\eta N^2\) in (1) is not changed below.

Let \(\mathscr T_N\in\mathcal A_N\) have the full physical data
\[
 \mathscr T_N(c_a)=\tau_a^2,\qquad
 \mathscr T_N'(c_a)=\frac{\tau_a}{\sin\tau_a},
 \qquad \mathscr T_N(-2)=0\quad(N\ {\rm odd}).
 \tag{4}
\]
Define the canonical crossing family and its known carrier by
\[
 C_{N,n}=\exp\!\left(\frac{\pi i nD^2}{4N}\right),\qquad
 R_n=C_{N,n}
       \exp_{\mathcal A_N}\!\left(\frac{i nN}{4\pi}\mathscr T_N\right),
 \qquad n\in\mathbb C.
 \tag{5}
\]
This is the entire family in the real-power source theorem. At every
signed integer \(n\), it equals the actual physical \(R^n\), including
the first normals. Its angular jet representative on the specified
physical lifts is
\[
                  C_{N,n}\exp(i nNt^2/(4\pi)).
 \tag{6}
\]
No periodic resetting of this representative is made. Although the
prior real-power note states \(N\ge3\), its direct local-algebra proof
also proves (4)--(6) for \(N=2\): there is one double node with
\(c_0=0,\tau_0=\pi/2\) and no simple-node term.

The original entire charge coupon \(\mathcal C_{N,\chi}\) has data
\[
 \begin{split}
 \mathcal C_{N,\chi}(c_a)
     &=\cos\!\bigl(N(1-\chi)\tau_a\bigr),\\
 \mathcal C_{N,\chi}'(c_a)
     &=-\frac{N(1-\chi)\sin\!\bigl(N(1-\chi)\tau_a\bigr)}
                    {2\sin\tau_a},
 \end{split}
 \qquad
 \mathcal C_{N,\chi}(-2)=1\quad(N\ {\rm odd}).
 \tag{7}
\]
Full Hermite interpolation defines it for every complex \(\chi\).
The exact endpoints are
\[
                 \mathcal C_{N,1}=1,\qquad
                 \mathcal C_{N,0}=\eta\,1.
 \tag{8}
\]
At \(\chi=j/N\), \(0\le j\le N\), it is the original Chebyshev coupon
\(T_{N-j}(-z/2)\), reduced only in a traced variable.

Fix an original compiled numerator \(F_N(z_1,\ldots,z_m;\mathbf u)\),
independent of the parameters below. The \(z_v\) are distinct contracted
algebra copies. Every original identity/turn kernel, other coupon and
fixed scalar remains in \(F_N\); the variables \(\mathbf u\) remain
ordinary free-boundary variables. For the circle-tree source one can
take the original product of same-index kernels. Define
\[
 Z_N(\mathbf n,\boldsymbol\chi;\mathbf u)=
 \phi_N^{\otimes m}\!
   \left[F_N\prod_{v=1}^m R_{n_v}(z_v)
                         \mathcal C_{N,\chi_v}(z_v)\right],
 \qquad
 \widetilde Z_N=
       \left(\prod_v C_{N,n_v}^{-1}\right)Z_N.
 \tag{9}
\]
If two variable crossing insertions occur at different positions of a
compiled word, they are kept in their separate algebra copies; they
are not commuted through a physical turn. Formula (9) covers them by
the original finite kernel compiler.
At integral \(\mathbf n\) and \(\boldsymbol\chi=\mathbf1\), (9) is
the original prescribed source. At other parameters it is a specified
analytic family, not a new topological filling operation.

## 2. The charge space is faithful, and the heat equation is exact

Write \(y=1-\chi\), and let \(\mathcal E_N\) be the span of
\[
 \cos(N\tau_a y),\qquad y\sin(N\tau_a y)
       \quad(0\le a<\lfloor N/2\rfloor),
 \qquad
 1\quad(N\ {\rm odd}).
 \tag{10}
\]
These are functions of \(\chi\), with the indicated \(y=1-\chi\).

**Theorem 1.** The map
\[
 \mathcal O_N:\mathcal A_N\longrightarrow\mathcal E_N,\qquad
              f\longmapsto\phi_N(f\mathcal C_{N,\chi})
 \tag{11}
\]
is an isomorphism. In particular \(\dim\mathcal E_N=N\).
It intertwines multiplication by \(\mathscr T_N\) with
\(-N^{-2}\partial_\chi^2\). Consequently (9) is entire in all its
parameters and satisfies
\[
 \boxed{\qquad
 \partial_{n_v}\widetilde Z_N
       =-\frac{i}{4\pi N}\partial_{\chi_v}^2\widetilde Z_N
                  \qquad(1\le v\le m).
 \qquad}
 \tag{12}
\]
Its initial datum is exactly
\(\widetilde Z_N(\mathbf0,\boldsymbol\chi;\mathbf u)\).
The equations uniquely determine it in
\(\mathcal E_N^{\otimes m}\), coefficientwise in the free variables.

*Proof.* From (3) and (7), the observation (11) is
\[
 \mathcal O_N(f)=\sum_a\{A_a(f)\cos(N\tau_a y)
                            +B_a(f)y\sin(N\tau_a y)\}
                    +\mathbf1_{N\ {\rm odd}}f(-2),
 \tag{13}
\]
where
\[
 A_a(f)=\eta\{4\sin^2\tau_a\,f'(c_a)-c_af(c_a)\},\qquad
 B_a(f)=-2\eta N\sin\tau_a\,f(c_a).
 \tag{14}
\]
The positive \(\tau_a\) are distinct, and none has zero sine.
Exponential polynomials at distinct frequencies are independent;
expanding the sine and cosine in their two frequencies also proves
independence of the two functions at each \(a\). The optional constant
has a different frequency. Thus (10) has dimension \(N\).
Equations (14) recover each value first and then each derivative,
while the constant recovers the odd simple-node value. This proves
the isomorphism, including the nilpotent coordinates.

The equality
\[
           \partial_\chi^2\mathcal C_{N,\chi}
                     =-N^2\mathscr T_N\mathcal C_{N,\chi}
                 \quad\hbox{in }\mathcal A_N
 \tag{15}
\]
can be checked on the angular representatives
\(\partial_\chi^2\cos(N(1-\chi)t)=-N^2t^2\cos(N(1-\chi)t)\).
Taking their spectral first derivatives gives exactly the product
rule in the double local factors. The odd simple value is zero on
both sides. This is a full-Hermite identity, not just a nodal one.
It proves the intertwining assertion. Differentiating (5) and using
(15) inside (9) proves (12).

The space \(\mathcal E_N\) is invariant under \(\partial_\chi^2\).
For example, if \(\lambda=N\tau_a\), then
\[
 \partial_\chi^2\cos(\lambda y)=-\lambda^2\cos(\lambda y),\qquad
 \partial_\chi^2(y\sin(\lambda y))
    =-\lambda^2y\sin(\lambda y)+2\lambda\cos(\lambda y).
 \tag{16}
\]
These are the actual size-two normal blocks; the odd constant is the
remaining simple block. Thus (12) is an ordinary finite-dimensional
constant-matrix evolution, independently in each coordinate:
\[
 \widetilde Z_N(\mathbf n,\boldsymbol\chi)
  =\exp\!\left[-\frac{i}{4\pi N}
                   \sum_v n_v\partial_{\chi_v}^2\right]
            \widetilde Z_N(\mathbf0,\boldsymbol\chi).
 \tag{17}
\]
The operators commute, proving uniqueness and tensorization. All
statements commute with ordinary free-boundary differentiation.
\(\square\)

Faithfulness here concerns the whole function of the charges. A
single value of that function, in particular its value at
\(\boldsymbol\chi=\mathbf1\), is still one prescribed observation.
The \(N\)-dimensional initial datum has not been compressed to a
geometric line.

This theorem also retains coherent low Newton coefficients. With the
original basis and pairing
\(\phi_N(e_i e_j)=\mathbf1_{i+j=D}\), set
\(\alpha_r(f)=[e_r]\operatorname{rem}_{P_N}f=\phi_N(e_{D-r}f)\).
Putting \(e_{D-r}f\) in (11) gives (12)--(17) for the entire charged
extension of \(\alpha_r(R_n f)\). Finite sums such as
\[
                    \sum_{r<\lfloor N/2\rfloor}
                      \alpha_r(R_n f)\alpha_r(R_p g)
 \tag{18}
\]
therefore have the same tensorized exact reduction, with their
original signs and common index retained. No termwise absolute value
or semisimple projection enters this step.

## 3. Convergent Gaussian contours and arbitrary translations

For one real \(n\ne0\), put
\[
 \sigma=\operatorname{sgn}n,\qquad v_n=e^{-i\sigma\pi/4},
 \qquad
 \mathfrak G_n[f](\chi)
   =\sqrt{\frac{N}{|n|}}
       \int_{\mathbb R}e^{-\pi Nr^2/|n|}
                                  f(\chi+v_n r)\,dr.
 \tag{19}
\]
This integral is absolutely convergent for every \(f\in\mathcal E_N\),
including its derivatives in any of the finite parameters.

**Theorem 2.** For all \(f\in\mathcal E_N\),
\[
       \mathfrak G_n[f]
        =\exp[-i n\partial_\chi^2/(4\pi N)]f.
 \tag{20}
\]
Equivalently, with the line oriented by increasing real \(r\),
\[
 \mathfrak G_n[f](\chi)
   =e^{i\sigma\pi/4}\sqrt{\frac{N}{|n|}}
      \int_{\chi+v_n\mathbb R}
          e^{-i\pi N(y-\chi)^2/n}f(y)\,dy.
 \tag{21}
\]
The line in (21) may be replaced by
\(\chi+b+v_n\mathbb R\) for any finite \(b\in\mathbb C\).
For \(J=\{v:n_v\ne0\}\), applying these formulas in every coordinate
of (17), and leaving the others fixed, gives an exact absolutely
convergent integral for the whole original source:
\[
 \boxed{\quad
 Z_N(\mathbf n,\boldsymbol\chi;\mathbf u)
   =\left(\prod_v C_{N,n_v}\right)
       \left(\prod_{v\in J}\mathfrak G_{n_v}^{(\chi_v)}\right)
                   Z_N(\mathbf0,\boldsymbol\chi;\mathbf u).
 \quad}
 \tag{22}
\]
Each of its charge lines can be independently translated through a
specified target charge. All attached spectators, mixed normals and
ordinary free-boundary derivatives remain in the initial function.

*Proof.* For \(f(\chi)=e^{\lambda\chi}\), elementary completion of
the square in the real Gaussian gives
\[
 \mathfrak G_n[f](\chi)
   =e^{\lambda\chi}
        \exp\!\left(\frac{|n|v_n^2\lambda^2}{4\pi N}\right)
   =e^{\lambda\chi-i n\lambda^2/(4\pi N)}.
 \tag{23}
\]
The identity holds for every complex \(\lambda\) by absolute
convergence and the entire Gaussian identity. Differentiating in
\(\lambda\) also proves it for \(\chi e^{\lambda\chi}\).
Every function in (10) is a linear combination of these functions,
so (20) follows, with the normal blocks included.
Changing variable \(y=\chi+v_n r\) proves the prefactor and
orientation in (21).

For a compact set of free-boundary parameters, every initial function
in \(\mathcal E_N^{\otimes m}\) has a bound of the form
\[
 |Z_N(\mathbf0,\mathbf y;\mathbf u)|
   \le A_N\prod_v(1+|y_v|)
                    \exp\!\left(\pi D\sum_v|\Im y_v|\right).
 \tag{24}
\]
The finite number \(A_N\) retains the actual full source and can grow
exponentially with \(N\); no uniform estimate for it is asserted.
The same form of bound holds for fixed derivatives, with their
actual constants. Formula (24) follows directly from (10)--(14).

On the two connectors
\(y=\chi\pm v_n R+s b\), \(0\le s\le1\), the real Gaussian exponent
is at most
\[
                         -\frac{\pi N}{|n|}R^2+O_N(R+1).
 \tag{25}
\]
The source in (24) contributes only another exponential linear in
\(R\), times a polynomial. The connector integrals tend to zero as
\(R\to\infty\). The integrand is entire, so Cauchy's theorem proves
the translated-line identity. This argument is at each fixed \(N\);
it does not replace (24) by a subexponential estimate.

In several coordinates the Gaussian quadratic dominates the sum of
the linear growth bounds. Fubini's theorem and successive one-variable
translations are therefore legitimate, proving (22). Coefficientwise
polynomial dependence, or uniformity on a compact set of ordinary
boundary variables, proves the derivative statements. \(\square\)

In particular the new charge contours have no factorial poles or
physical grid poles. Those finite-source contributions have already
been combined into the entire initial function. Passing through a
target point by translation is an exact contour statement; it is not
yet a descent estimate for the full integrand.

## 4. The original primitive action and the two Schur complements

Here specialize to an original circle-tree component on a regular
canonical positive edge chart. Keep every outside complex angle fixed.
Write
\[
 W(\mathbf t)=\sum_{e=vw}\psi(t_v,t_w),\qquad
 P_0(\mathbf t)=\left(\sum_{e\ni v}r_{v,e}\right)_v,\qquad
 J_0=\partial_{\mathbf t}P_0,\qquad W_{\mathbf t}=-P_0/\pi.
 \tag{26}
\]
The phases and meridian increments have their original normalization.
Let \(D_{\mathbf n}=\operatorname{diag}(n_v)\). The filled primitive
phase, excluding only the explicit carrier in (5), is
\[
 \Phi_{\mathbf n,\boldsymbol\chi}(\mathbf t)
      =W(\mathbf t)+\frac{i}{4\pi}\mathbf t^{\mathsf T}
                         D_{\mathbf n}\mathbf t
                       -i\boldsymbol\chi^{\mathsf T}\mathbf t.
 \tag{27}
\]
Its critical equation and Hessian are
\[
 P_{\mathbf n}:=P_0-\frac i2D_{\mathbf n}\mathbf t
                          =-\pi i\boldsymbol\chi,\qquad
 \Phi_{\mathbf t\mathbf t}=-J_{\mathbf n}/\pi,\qquad
 J_{\mathbf n}=J_0-\frac i2D_{\mathbf n}.
 \tag{28}
\]

Let \(J=\{v:n_v\ne0\}\), let \(E:\mathbb C^J\to\mathbb C^m\)
be the coordinate inclusion, and set
\(D_J=\operatorname{diag}(n_v)_{v\in J}\).
The charge variables outside \(J\) are kept equal to \(\chi_v\).
Before any stationary elimination the corresponding joint phase is
\[
 \mathcal Q(\mathbf t,\mathbf y_J)
   =W(\mathbf t)-i\mathbf y^{\mathsf T}\mathbf t
     -i\pi(\mathbf y_J-\boldsymbol\chi_J)^{\mathsf T}
                    D_J^{-1}(\mathbf y_J-\boldsymbol\chi_J).
 \tag{29}
\]
Its charge stationarity is exactly
\[
       \mathbf y_J=\boldsymbol\chi_J-\frac{D_J\mathbf t_J}{2\pi}.
 \tag{30}
\]
Substitution in (29) gives (27) with no additive constant.
Thus the charge Gaussian supplies the actual signed quadratic
crossing action.

At any original positive critical point \(\mathbf t_*\), (30) is
a finite charge point. Theorem 2 permits the actual charge lines
to pass through it. The positive period theorem gives
\(\Re J_0>0\); adding the purely imaginary diagonal in (28)
preserves this property for real signed \(\mathbf n\).
Hence both \(J_0\) and \(J_{\mathbf n}\) are invertible there.

Locally solve \(P_0(\mathbf t)=-\pi i\mathbf y\), with the outside
angles fixed, and define the zero-power critical action
\[
 S_0(\mathbf y)=W(\mathbf t(\mathbf y))
                         -i\mathbf y^{\mathsf T}\mathbf t(\mathbf y).
 \tag{31}
\]
This is a local classical generating function. We have not asserted
that the entire zero-power source has a single asymptotic with phase
\(S_0\) on the translated charge lines. Differentiation gives
\[
 (S_0)_{\mathbf y}=-i\mathbf t,\qquad
 (S_0)_{\mathbf y\mathbf y}=-\pi J_0^{-1}.
 \tag{32}
\]
The charge phase obtained by eliminating \(\mathbf t\) is
\[
 \Psi(\mathbf y_J)=S_0(\mathbf y)
    -i\pi(\mathbf y_J-\boldsymbol\chi_J)^{\mathsf T}
                      D_J^{-1}(\mathbf y_J-\boldsymbol\chi_J).
 \tag{33}
\]
At (30), its Hessian and determinant are
\[
 H_{\rm ch}=-\pi E^{\mathsf T}J_0^{-1}E-2\pi iD_J^{-1},
 \qquad
 \boxed{\quad
 \det H_{\rm ch}=(-2\pi i)^{|J|}
                     \frac{\det J_{\mathbf n}}
                          {\det J_0\det D_J}.
 \quad}
 \tag{34}
\]
In particular this charge critical point is nondegenerate.

For a direct verification, the joint Hessian of (29), in the order
\((\mathbf t,\mathbf y_J)\), is
\[
 \begin{pmatrix}
       -J_0/\pi&-iE\\
       -iE^{\mathsf T}&-2\pi iD_J^{-1}
 \end{pmatrix}.
 \tag{35}
\]
Its \(\mathbf t\)-Schur complement is \(H_{\rm ch}\), while its
\(\mathbf y_J\)-Schur complement is \(-J_{\mathbf n}/\pi\).
Equating the two determinant factorizations proves (34), including
mixed signs and zero powers omitted from \(J\).

If a separately justified local term of the zero-power charged source
has amplitude \(A_0\), the square of its formal Gaussian density after
(21) is multiplied by
\[
                         \frac{\det J_0}{\det J_{\mathbf n}}.
 \tag{36}
\]
Indeed the square of the exact prefactor in (21), multiplied by
\((2\pi/N)^{|J|}/\det(-H_{\rm ch})\), is precisely that ratio.
This is a local density identity. A contributing cycle and its
orientation are still needed to infer any actual leading coefficient.
At \(J=\varnothing\) the Gaussian transformation is the identity.

Finally the carrier has not been suppressed from the original answer:
\[
 \prod_v C_{N,n_v}
 =\exp\!\left(N\frac{i\pi}{4}\sum_vn_v\right)
   \exp\!\left(-\frac{i\pi}{2}\sum_vn_v
                       +\frac{i\pi}{4N}\sum_vn_v\right).
 \tag{37}
\]
Thus (27)--(36) compare the carrier-normalized actions; (22) and (37)
restore their original phase and finite subscalar exactly.

## 5. What the reduction leaves to estimate

The initial datum in (22) is the full function
\(Z_N(\mathbf0,\boldsymbol\chi;\mathbf u)\), not its value at
\(\boldsymbol\chi=\mathbf1\), and not a local formal geometric unit.
For example, (8) gives the exact identity
\[
 Z_N(\mathbf0,\mathbf0;\mathbf u)
                       =\eta^m Z_N(\mathbf0,\mathbf1;\mathbf u).
 \tag{38}
\]
The known small-charge initializer is on a box separated from zero;
the original coupon source at zero is not a fresh complete-edge
initial value. Its companion phases and full Hermite aliases cannot
be replaced by one chosen primitive branch inside the Gaussian
integral.

The new entire contours remove pole avoidance as a condition on charge
translations. They do not remove the initial source's exponential
growth, its competing actions, or cancellation among its branches.
To use (33) for the complete integral still requires a controlled
expansion of that actual initial function on the chosen charge
contours and a bound on their complement. Formula (34) proves local
nondegeneracy, not that the straight translated contour is a descent
contour or that its geometric contribution survives the rest.

The earlier Gaussian Newton frame resolves coefficient vectors by a
positive family and expresses the crossing of a frame vector by a
Gaussian integral of a finite Pochhammer product. It retains separate
cup and closing observations. Here the heat operator acts directly on
the original entire charged observation, its initial datum is the
actual zero-power compiled source, and the size-two charge blocks in
(16) preserve the normal data. Neither representation by itself
proves a filled-action upper bound or noncancellation for arbitrary
short components.

## Pinned direct sources

* notes/research_real_power_source_transport.md, SHA256
  7dac43d1a5fac6b4602a3aab12bfe977cb42a61b36d40a2fb8517e29566df8ea:
  the canonical entire crossing group, its angular logarithm and
  exact carrier, all physical normals, and prior finite-generator scope.
* notes/research_dominant_saddle_transport.md, SHA256
  413940497a23e884d726b91f9c0ebc01994fef8216811ed2c6fb0838fc80bb04:
  the original entire full-Hermite coupon in Section 9, its exact
  endpoints, and the distinction between an integrand coefficient
  and the original cycle coefficient.
* notes/research_actual_source_dualizing_residue.md, SHA256
  806f8e4530736632830a15cff19f4c0f72e659fa6280d48005c4184a6ffc9afb:
  original trace normalization, perfect Newton pairing, kernels and
  arbitrary compiled contractions with unreduced free boundaries.
* notes/research_positive_period_inverse_descent.md, SHA256
  b9b5c3d61c704700e9431315cf50591c921ebeb95becdf6a52877606bdbc4565:
  original phase derivatives, canonical period normalization and
  accretive Jacobian on the positive circle-tree domain.
* notes/research_gaussian_frame_newton_transport.md, SHA256
  b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9:
  prior exact positive Gaussian frame and crossing integral, cited
  for coverage and the different role of its boundary observations.

Only written proofs, source-text reads and file hashes enter this note.
No mathematical code, numerical evaluation, test or compilation was
run. Frozen manuscripts and other authors' notes were not edited.
