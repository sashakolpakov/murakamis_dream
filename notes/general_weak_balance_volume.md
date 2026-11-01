# Volume limits from weak balance in a circle packing

A complete circle packing determines a useful bound for each local part of the quantum invariant. Earlier balance criteria required every one-sided bound to be strictly smaller than the complete local rate. Here equality is allowed. A small common power change of the positive face weights makes all the required comparisons strict, with an explicit bound on the cost of changing those weights.

The proof controls the whole complementary polynomial, applies the finite filling functional, and compares it with the nonzero geometric contribution. It therefore gives a volume limit for the original knot invariant under the stated geometric condition. The knot diagram and its peripheral curves remain fixed. A second criterion permits a quantified failure of weak balance. Neither condition is asserted for every matched sphere.

## 1. Statement with the actual diagram fixed

Let \(D\) be a fixed connected augmented diagram in \(S^3\) with the following recorded data: a simple triangulated white sphere, a perfect matching of its cubic dual, the original cyclic four-face orders and crossing-disk framings, and one marked nonmatching strand edge. Equivalently, use the literal inverse-cut construction of [actual morse geometric contribution](actual_morse_geometric_contribution.md), §§1–2. Write \(u,v\) for the two protected faces meeting that mark and \(V\) for all other white vertices. There are \(R=|V|\) matched crossing regions and \(2R\) triangles. The original complete marked packing has curvatures
\[
 w_u^*=w_v^*=0,\qquad w_f^*>0\quad(f\in V),
 \qquad q_f=\log w_f^* .                         \tag{1}
\]
The simple-sphere geometry supplies the actual positive cut certificate before any terminal decoration. Alternatively that certificate can be specified as input. Its complete augmented exterior is \(Y_D\), and
\[
 \Phi=\frac{\operatorname{Vol}(Y_D)}{2\pi}.       \tag{2}
\]

At each ordered crossing region \(e=(x,b,c,y)\), the outer pair \(xy\) is the matched diagonal. Define the source-normalized complete triangle potential \(Q\) in §2 and put
\[
 X_e=Q(w_x^*,w_b^*,w_y^*)+Q(w_x^*,w_c^*,w_y^*).
                                                        \tag{3}
\]
A logarithm below is only taken when its middle curvature is positive.

**Theorem.** If at every crossing region
\[
 X_e\ge\log w_b^*\quad(w_b^*>0),\qquad
 X_e\ge\log w_c^*\quad(w_c^*>0),                 \tag{4}
\]
then the full original spectral numerator minus its all-CROSS part has a strict uniform exponential gap below \(\Phi\) on \([-2,2]^R\), at both parities of the level. An explicit single shared Cauchy vector and gap are given in (23)–(24).

Fix any retained half-twist pattern \(\epsilon_e\in\{-1,0,1\}\) whose original terminal graph gives a knot with no additional closed main component. There is a threshold depending on this fixed diagram and pattern such that every independently chosen fixed signed filling vector \(p_e\), sufficiently large in absolute value, with actual crossing powers
\[
 n_e=\epsilon_e-2p_e,
\]
gives a hyperbolic knot \(K_{\boldsymbol p}\) and
\[
 \lim_{N\to\infty}\frac{2\pi}{N}
   \log|\langle K_{\boldsymbol p}\rangle_N|
       =\operatorname{Vol}(S^3\setminus K_{\boldsymbol p}).
                                                        \tag{5}
\]
The invariant is the original reduced, zero-framed complete-color invariant with unknot value one; the stated full one-cut modified convention has the same rate after its single prescribed factor is retained. Neither the diagram nor the powers grow with \(N\). There is no uniform filling threshold over a growing family.

The quantitative sufficient hypothesis (22) permits positive defects in (4). The theorem does not assert that all simple matched spheres satisfy either hypothesis.

## 2. The exact triangle potential and protected corners

For each actual triangle \(t\), let \(I_t\subset V\) be its ordinary corners. It is nonempty because the sphere is simple and has only two protected vertices. Protected coordinates are deleted from the supported simplex; no small positive approximation to their zero weight is used. The exact source normalization is
\[
 \begin{split}
 Q_t(q)&=\max_{a_i\ge0,\ \sum_{i\in I_t}a_i=1/2}
          \sum_{i\in I_t}\bigl(f(a_i)+a_iq_i\bigr),\\
 f(a)&=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},
 \qquad \Lambda(s)=-\int_0^s\log|2\sin z|\,dz .
 \end{split}                                            \tag{6}
\]
This is the Legendre identity in [actual triangle entropy algebraic balance](actual_triangle_entropy_algebraic_balance.md), §1, obtained from the normalized local coefficient theorem and the actual cofactor action. Its identification can use the even-level positive coefficient limit; once it identifies the fixed function \(Q\), the later both-parity source bounds use that same function. No odd-level coefficient entropy theorem is silently inferred from an even-level one.

Direct differentiation gives
\[
 f(0)=f(1/2)=0,\quad f'(a)=\log\cot(\pi a),\quad
 f''(a)=-\frac{2\pi}{\sin(2\pi a)}<0
                       \quad(0<a<1/2).                 \tag{7}
\]
Thus \(f>0\) on the open interval. On a singleton row, \(Q_t=q_i/2\), with zero entropy and zero Hessian.

For two or three ordinary corners, put \(w_i=e^{q_i}\) and
\[
 D_t^2=\sum_{\{i,j\}\subset I_t}w_iw_j,
 \qquad a_{ti}=\frac1\pi\arctan\frac{w_i}{D_t}.   \tag{8}
\]
The angles sum to \(\pi/2\). For two weights this follows from their reciprocal tangent ratios. For three weights,
\(D_t^2-w_iw_j=w_k(w_i+w_j)\), so the sum of the first two arctangents is \(\arctan(D_t/w_k)\), which is complementary to the third. Equation (7) then gives
\(f'(a_{ti})+q_i=\log D_t\). Strict concavity proves that (8) is the unique maximizer of (6), with every allowed load in \((0,1/2)\).

Consequently \(\partial_{q_i}Q_t=a_{ti}\), and its entropy is
\[
 E_t(q)=Q_t(q)-q\cdot\nabla Q_t(q)
              =\sum_{i\in I_t} f(a_{ti}).                \tag{9}
\]
This is strictly positive on every nonsingleton row.

The outer edge of a crossing region is matched, whereas the protected edge \(uv\) is nonmatching. Simplicity excludes a second edge with the same endpoints. Hence the outer pair cannot be the two protected vertices. In particular \(w_x^*+w_y^*>0\). A triangle containing a positive middle and this outer pair therefore has at least two ordinary corners. Its entropy is strictly positive, even if its opposite triangle is a protected singleton.

## 3. Exact Hessian and the full shared action

For distinct ordinary corners \(i,j\) of one triangle, differentiation of (8) gives
\[
 \partial_{q_iq_j}Q_t
       =-\frac{w_iw_j}{2\pi D_t(w_i+w_j)}
       =-\kappa^t_{ij}.                                 \tag{10}
\]
For three corners the cancellation uses
\(D_t^2+w_i^2=(w_i+w_j)(w_i+w_k)\); for two corners it uses \(D_t^2=w_iw_j\). Since \(D_t\ge\sqrt{w_iw_j}\) and \(w_i+w_j\ge2\sqrt{w_iw_j}\),
\[
 0<\kappa^t_{ij}\le\frac1{4\pi}.                        \tag{11}
\]
Each row has degree \(1/2\), so its Hessian rows sum to zero. Thus, for any real vector \(h\),
\[
 h^{\mathsf T}\nabla^2Q_t h
       =\sum_{\{i,j\}\subset I_t}\kappa^t_{ij}(h_i-h_j)^2.
                                                        \tag{12}
\]
There is no missing factor of two: this is the quadratic form of the Laplacian with off-diagonal entries \(-\kappa_{ij}\).

Set
\[
 P(q')=\sum_t Q_t(q')-\sum_{f\in V}q'_f .                \tag{13}
\]
At the actual complete vector \(q\), the normalized circle angles give the face-star equations
\[
 \sum_{t\ni f}a_{tf}=1,\qquad
 \nabla P(q)=0,\qquad P(q)=\Phi.                         \tag{14}
\]
These are the complete geometric action and stationarity used in [actual morse cross filling period](actual_morse_cross_filling_period.md), §§2–4, and [actual morse geometric contribution](actual_morse_geometric_contribution.md), §§2,4–6. Their normalization is the determinant/beta/half-forced-product action in (6). They do not require a bound on the full endpoint coefficient. In particular no middle-forest full-source theorem is used here.

Define
\[
 \mathcal E=
 \frac1{4\pi}\sum_t\sum_{\{i,j\}\subset I_t}(q_i-q_j)^2
 =\frac1{2\pi}\sum_{\substack{ij\text{ a white edge}\\i,j\in V}}
                         (q_i-q_j)^2.                  \tag{15}
\]
Each ordinary white edge is incident to exactly two original triangles, proving the second expression. Equation (11) holds at every positive weight vector, not only at completeness. Applying Taylor's formula with integral remainder along \(q-tq\), and using (14), proves
\[
 0\le P((1-t)q)-\Phi
   =\int_0^t(t-s)q^{\mathsf T}\nabla^2P((1-s)q)q\,ds
   \le\tfrac12t^2\mathcal E,
                    \qquad 0\le t<1.                  \tag{16}
\]
The lower bound is convexity at a stationary point. This is the cost for the entire shared face action, not a sum of independently optimized crossing budgets.

The action \(P\), the energy \(\mathcal E\), the row entropies, and the balance losses are invariant under a common curvature scaling \(q\mapsto q+c\mathbf1\). Indeed, there are \(2R\) rows of degree \(1/2\) and \(R\) targets, so the added terms in \(P\) cancel. The individual coordinates \(q_i\) and triangle potentials \(Q_t\) do change under this scaling.

## 4. Entropy monotonicity and the one-sided gain

For \(0<\beta\le1\), use the single shared ordinary-weight vector \(w_f(\beta)=e^{\beta q_f}\), keeping the protected weights exactly zero. This need not be a circle packing. It is simply a permissible coefficient torus.

Let \(E_t(\beta)=Q_t(\beta q)-\beta q\cdot\nabla Q_t(\beta q)\). Differentiating and using (12) gives
\[
 E_t'(\beta)=-\beta q^{\mathsf T}\nabla^2Q_t(\beta q)q\le0.
                                                        \tag{17}
\]
Singleton rows satisfy the identity with both sides zero. Integrating the derivative of \(Q_t(\beta q)/\beta\) yields
\[
 Q_t(\beta q)
 =\beta Q_t(q)+\beta\int_\beta^1\frac{E_t(s)}{s^2}\,ds
 \ge\beta Q_t(q)+(1-\beta)E_t(q).                       \tag{18}
\]
This uses the actual absolute constant in (6).

At an original crossing region write \(Q_b=Q(x,b,y)\), \(Q_c=Q(x,c,y)\). The actual real-spectral, phase-uniform local rates are
\[
 A_C=X=Q_b+Q_c,\qquad
 A_L=\max(q_c,Q_b+q_c/2),\qquad
 A_R=\max(q_b,Q_c+q_b/2).                               \tag{19}
\]
A one-sided label is omitted when its overloaded middle is protected. The exact loss for LEFT is \(X-A_L=\min(X-q_c,Q_c-q_c/2)\). At completeness, \(Q_c>q_c/2\) whenever LEFT survives: a simplex vertex with all load at \(c\) gives \(q_c/2\), while the unique maximizer has all allowed loads positive. RIGHT is identical with the two middle roles exchanged.

For a surviving side \((e,s)\), denote its overloaded middle by \(z\) and its triangle by \(t(e,s)\). Put
\[
 \epsilon_{e,s}=\max(0,q_z-X_e(q)),\qquad
 h_{e,s}=E_{t(e,s)}(q)>0.                               \tag{20}
\]
Apply (18) to the two triangles in \(X-q_z\) and to the overloaded triangle in \(Q_z-q_z/2\). With \(t=1-\beta\), this proves
\[
 (X_e-A_s)((1-t)q)
        \ge t h_{e,s}-(1-t)\epsilon_{e,s}.              \tag{21}
\]
In the first branch the entropy gain is the sum of both triangle entropies, at least \(h_{e,s}\); in the second it is \(h_{e,s}\), and its original nonnegative loss is retained. Thus taking the smaller branch is legitimate. Protected singleton entropy is never substituted for \(h_{e,s}\).

## 5. Quantitative criterion, weak equality, and local ratio bounds

Suppose there is \(0<t<1\) such that
\[
 \gamma_0=
 \min_{(e,s)\ \mathrm{surviving}}
       \{t h_{e,s}-(1-t)\epsilon_{e,s}\}
                         -\tfrac12t^2\mathcal E>0.      \tag{22}
\]
If there are no surviving one-sided labels, the complementary polynomial is zero and no criterion is necessary. Otherwise let \(h_*=\min h_{e,s}>0\).

Under weak balance (4), every defect is zero. Choose
\[
 t_0=\begin{cases}
 \min(1/2,h_*/\mathcal E),&\mathcal E>0,\\
 1/2,&\mathcal E=0.
 \end{cases}                                           \tag{23}
\]
Then (22) holds with
\[
 \gamma_0\ge t_0h_*/2>0\quad(\mathcal E>0),\qquad
 \gamma_0=h_*/2>0\quad(\mathcal E=0).                    \tag{24}
\]
Indeed \(t_0\mathcal E\le h_*\). Equality in any or all instances of (4) therefore causes no exceptional sector.

For positive defects let \(\epsilon_*\) be their maximum. The scalar sufficient test is
\[
 t(h_*+\epsilon_*)-\epsilon_*-\tfrac12t^2\mathcal E>0.
                                                        \tag{25}
\]
In particular, \(\epsilon_*<t_0h_*/2\) suffices, with gap at least \(t_0h_*/2-\epsilon_*\). This statement also uses the explicit \(\mathcal E=0\) convention in (23).

There is also a useful bound in terms of local curvature ratios. If every pair of ordinary weights in a triangle has ratio at most \(K\ge1\), normalize the smallest to one. Then \(D_t^2\le K^2+2K\), so every allowed load on a nonsingleton row lies in
\[
 [a_0,1/2-a_0],\qquad
 a_0=\pi^{-1}\arctan((K^2+2K)^{-1/2}).                  \tag{26}
\]
The two-corner case has a stronger lower bound. Symmetry and concavity of \(f\) imply \(f(a)\ge f(a_0)\) throughout this interval. Thus \(E_t\ge2f(a_0)>0\). Likewise an upper bound of \(E\) on the number of ordinary edges gives \(\mathcal E\le E(\log K)^2/(2\pi)\). A degree bound alone does not make this independent of diagram size. A family satisfying uniform bounds on \(\mathcal E,h_*,\epsilon_*\) and a common strict (25) has a uniform source gap, but its geometric filling thresholds can still depend on the individual diagram.

## 6. Why these rates bound the actual finite polynomial

Set \(d=N-1\) and \(q_N=e^{\pi i/N}\). The original polynomial resolvent is
\[
 V_N(\sigma;\Omega)=
 \frac{\chi_N(\sigma)-\chi_N(\Omega)}{\sigma-\Omega},
 \qquad \chi_N(z)=2T_N(z/2)+2.                           \tag{27}
\]
This is a degree-\(d\) matrix polynomial; division is polynomial division. It retains the derivative directions at double Casimir roots. The exact Morse source is
\[
 S_{N,\mathrm{full}}(\boldsymbol\sigma)=
 [\prod_{f\in V}L_f^d]\,
       \left.\prod_e H_{V_N}(L_{x_e},L_{b_e},L_{c_e},L_{y_e};\sigma_e)
                         \right|_{L_u=L_v=0}.           \tag{28}
\]
The unrestricted physical mark, cups/caps, face measure and even-level coset have already been included in this identity. One must not insert an additional \(N^R\) or a new normal operation. Its source derivation is [research matched sphere morse source](research_matched_sphere_morse_source.md), §§4–6, and the finite-source part of [actual morse geometric contribution](actual_morse_geometric_contribution.md), §3.

The decomposition into CROSS, LEFT and RIGHT is a literal path partition of each \(H_{V_N}\), with the odd central row included in CROSS once. These pieces are not separately declared covariant coupons. For even \(N=2m\), the lower piece has \(0\le i\le j\le m-1\); for odd \(N=2m+1\) the same lower range holds and the central row \(m\) belongs to CROSS. The upper piece is the physical row reflection. At a protected overloaded middle the one-sided polynomial vanishes exactly, since that middle exponent is at least \(\lfloor N/2\rfloor\).

The all-level local inputs are precisely:

- [actual cross cofactor factorization](actual_cross_cofactor_factorization.md), §8: the global real-spectral coefficient comparison for CROSS, giving its weighted rate \(X\).
- [actual global left weighted spectral envelope](actual_global_left_weighted_spectral_envelope.md), §§1–4: the weighted rate \(A_L\) for every real spectral value and every original face-phase tuple, including zero outer weights; RIGHT follows by the physical reflection.

The latter does not replace the signed recurrence by absolute coefficients at arbitrary spectra. It proves coefficient positivity of the normalized tail recurrence on \([-2,2\cos(\pi/N)]\), retaining both unused products and the omitted-half factor, and then treats the remaining \(O(N^{-2})\) cap by polynomial extrapolation at only bounded cost. The denominator recurrence starts at its second step, so no \(s_0\) is divided out. The odd omitted-half factor is polynomially bounded and its endpoint is removable. These facts give (19) at both parities and at every fixed positive ordinary weight vector, uniformly in face phases and spectra. No independently optimized local capacity is used.

For a genuine string \(\sigma\) containing at least one one-sided label, let \(J_\sigma\) record its one-sided positions. Apply Cauchy's inequality to (28) on the one common torus with moduli \(L_f=e^{(1-t)q_f}\). Equations (16),(21) give
\[
 \begin{split}
 G_\sigma&=\sum_e A_{e,\sigma_e}((1-t)q)
                            -\sum_{f\in V}(1-t)q_f\\
 &\le\Phi+\tfrac12t^2\mathcal E
       -\sum_{(e,s)\in J_\sigma}
                       \{t h_{e,s}-(1-t)\epsilon_{e,s}\}
 \le\Phi-\gamma_0.                                    \tag{29}
 \end{split}
\]
The last inequality uses the positivity of every individual loss ensured by (22). It therefore covers all spectators, not just one isolated anchor. Equivalently unrestricted spectator maxima are \(X_e\) at this common vector.

The actual targets are \(d=N-1\). Replacing \(d/N\) by one changes the logarithmic bound by the fixed quantity \(N^{-1}\sum_f\log L_f\). Local polynomial prefactors and uniform \(o(N)\) errors remain \(o(N)\) for this fixed diagram. There are at most \(3^R-1\) strings, independent of the level. Summing them therefore proves
\[
 \limsup_{N\to\infty}\frac1N
  \log\|\mathcal D_N\|_{[-2,2]^R}\le\Phi-\gamma_0,
 \qquad \mathcal D_N=S_{N,\mathrm{full}}-S_{N,\mathrm C}.
                                                        \tag{30}
\]
Every \(\sigma_e\) degree remains at most \(d\). The limit superior includes both parities. Equivalently any smaller fixed gap can be used in an eventual exponential bound. No claim uniform in diagrams growing with \(N\) has been made.

## 7. Exact finite filling transfer, with all normal data

For the actual power \(R^n\), let \(\mathcal L_N^n\) denote its physical full-Hermite functional on degree-at-most-\(d\) spectral polynomials. Write \(\phi_k=(2k+1)\pi/N\), \(P(\phi)=H(2\cos\phi)\), and
\[
 f_n(2\cos\phi)=q_N^{nd^2/4}
       \exp\!\left(\frac{i nN(\phi-\pi)^2}{4\pi}\right).
                                                        \tag{31}
\]
For either sign of the fixed integer \(n\), this retains the actual crossing phase and its derivatives. The exact formula is
\[
 \mathcal L_N^nH=-\frac1{N^2}\sum_{k=0}^{N-1}
   \bigl(\cos\phi_k f_kP_k+
          \sin\phi_k f_k'P_k+\sin\phi_k f_kP_k'\bigr).
                                                        \tag{32}
\]
Here \(f_k=f_n(2\cos\phi_k)\) and \(P_k=P(\phi_k)\); the primes mean derivatives of these functions with respect to \(\phi\), evaluated at \(\phi_k\). The double nodes occur twice in this grid and the odd simple node occurs once. Its weight is exactly the derivative of the sine factor, not an omitted or doubled normal. On the real circle \(|f_n|=1\), \(|f_n'|\le |n|N/2\); the exact trigonometric Bernstein inequality gives \(\|P'\|\le d\|P\|\). Hence
\[
 |\mathcal L_N^nH|
 \le\left(\frac1N+\frac{|n|}{2}+\frac dN\right)\|H\|_{[-2,2]}
 =\left(1+\frac{|n|}{2}\right)\|H\|_{[-2,2]}.           \tag{33}
\]
These are the finite identities and all-level inequality proved in [actual uniform filling supremum bound](actual_uniform_filling_supremum_bound.md), §§1–3. Its exact Riesz interpolation proof applies to complex polynomials; no sign of \(H\) is assumed.

The original filled source is exactly the tensor application of these functionals to (28). Other variables retain degree at most \(d\) after each application. Applying (33) successively therefore gives
\[
 |Z_{N,\mathrm{full}}(\boldsymbol n)-Z_{N,\mathrm C}(\boldsymbol n)|
 \le\prod_e\left(1+\frac{|n_e|}{2}\right)
                      \|\mathcal D_N\|_{[-2,2]^R}.      \tag{34}
\]
All powers and the diagram are fixed, so this prefactor has zero exponential rate. Joint node vanishing could improve it but is unnecessary here. No Fourier-tail argument, complex spectral strip or discarded-normal estimate is added at this step. The exterior framing/component character has modulus one at complete color. The prescribed full one-cut modified convention additionally has the one factor \(i^{N+3}/N\); either convention has the same logarithmic rate.

## 8. Nonzero geometric contribution and the actual filled volume

The separate input is the **general-Morse all-CROSS** theorem, not the older theorem stated only for marked flat plats. For the present fixed simple-sphere diagram, [actual morse cross filling period](actual_morse_cross_filling_period.md), §§1–8, proves the nonzero relative asymptotic of the whole CROSS period, with all charges, finite phases, both parities, and the original side currents. Its leading factors include
\[
 q_N^{d^2\sum_e n_e/4}(-2i)^R\sqrt{2\pi}\,N^{R+1/2}
 \frac{\prod_e\sin(2\pi\delta_{N,\mathbf1,e})}
 {\sqrt{\det H_N(\boldsymbol\delta_{N,\mathbf1})}
  \sqrt{\det Q_{N,\mathbf1}}}\,
                   e^{NS_{N,\mathbf1}}.                \tag{35}
\]
The determinant roots are its prescribed face and spectral Gaussian branches; the finite critical point is its original unit-charge point. The sine/determinant coefficient tends to a nonzero number for every sufficiently long fixed independently signed vector. The paired charge signs and level-parity factors have already been combined exactly in that theorem; no positivity or further noncancellation is assumed here.

Let \(F_{\boldsymbol n}=\operatorname{Re}S_{0,\mathbf1}\). The theorem gives
\[
 \frac1N\log|Z_{N,\mathrm C}(\boldsymbol n)|\longrightarrow F_{\boldsymbol n},
 \qquad F_{\boldsymbol n}\longrightarrow\Phi
                      \quad\text{as }\min_e|n_e|\to\infty.
                                                        \tag{36}
\]
The source neighborhood and reciprocal-slope argument are valid for independent signs and without bounds on slope ratios.

The geometric identification is [actual morse geometric contribution](actual_morse_geometric_contribution.md), §§4–7. It follows the original face maps and the original primitive disk words. The selected critical point satisfies \(U_e+p_eV_e=-2\pi i\), with the small logarithms identified before multiplication by \(p_e\). The framed representation is near the complete positive cut for all sufficiently long powers. The equivariant compact-core and cusp construction gives a complete smooth hyperbolic metric on the specified filling, keeping the main cusp complete. Calibration on the same oriented boundary triangulation yields
\[
 2\pi F_{\boldsymbol n}=\operatorname{Vol}(S^3\setminus K_{\boldsymbol p}).
                                                        \tag{37}
\]
This is the actual original filled knot, not the hypothetical complement associated to the auxiliary Cauchy weights \(w_f(1-t)\). Those weights are never used as geometric shapes.

Increase the common filling threshold until these analytic and geometric conclusions hold and \(F_{\boldsymbol n}>\Phi-\gamma_0/4\). Combining (30),(34),(36) gives
\[
 \limsup_{N\to\infty}\frac1N
 \log\left|\frac{Z_{N,\mathrm{full}}-Z_{N,\mathrm C}}
                  {Z_{N,\mathrm C}}\right|
                  \le-3\gamma_0/4<0.                  \tag{38}
\]
Thus the ratio of full to CROSS is \(1+O_{\boldsymbol n}(e^{-cN})\) for some \(c>0\), the full invariant is nonzero eventually at both parities, and (5) follows from (37). This finishes the proof.

## 9. Dependency and scope record

The new argument is the exact entropy integration (17)–(18), the linear one-sided loss (21), and its comparison with the whole quadratic cost (16). The local source bounds and the nonzero geometric CROSS asymptotic are explicit inherited theorems, not numerical assumptions.

- [actual triangle entropy algebraic balance](actual_triangle_entropy_algebraic_balance.md), §1, fixes the absolute triangle Legendre normalization, including zero weights. [actual fejer half block entropy](actual_fejer_half_block_entropy.md), §5, supplies its local closed entropy input; only this local normalization, not a full endpoint limit, is used.
- [actual morse cross filling period](actual_morse_cross_filling_period.md), §§2–4, supplies the actual face-star stationarity and calibrated CROSS action on the connected ordinary graph. [actual morse geometric contribution](actual_morse_geometric_contribution.md), §§1–2, supplies the actual simple-sphere topology and complete geometry.
- [actual cross cofactor factorization](actual_cross_cofactor_factorization.md), §8, and [actual global left weighted spectral envelope](actual_global_left_weighted_spectral_envelope.md), §§1–4, supply the both-parity real-spectral and face-phase uniform local rate bounds.
- [research matched sphere morse source](research_matched_sphere_morse_source.md), §§4–6, supplies the original coefficient, mark, parity coset and full-Hermite functional identity.
- [actual uniform filling supremum bound](actual_uniform_filling_supremum_bound.md), §§1–3, supplies the level-independent finite functional estimate, here rederived from its midpoint identity.
- [actual morse cross filling period](actual_morse_cross_filling_period.md), §§1–8, and [actual morse geometric contribution](actual_morse_geometric_contribution.md), §§4–9, supply the nonzero whole CROSS period and primitive smooth filling identification.

No flat-plat presentation, middle forest, global full-positive-source endpoint theorem, coefficientwise one-sided positivity on the whole spectral interval, or universal success of radius optimization is used. No short-filling, growing-level diagram, moving-main-meridian, shifted-chart or operator assertion follows from this note.

All calculations above are analytic. No code was run to test the inequalities or sample diagrams. Static native-math validation, if recorded alongside this file, checks notation only.
