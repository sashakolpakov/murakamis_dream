# Localized entropy and Dirichlet capacity for genuine source sectors

This note gives a sufficient shared-weight criterion for a fixed genuine CROSS/LEFT/RIGHT string on the original matched simple sphere. It improves the total-energy cost of uniform power flattening: only the quadrilaterals carrying a one-sided label are required to flatten, and their extension through all other faces is optimized. The original coefficient targets and protected zeros are never changed.

There are two complementary forms. A quadratic Dirichlet capacity gives an explicit computable sufficient inequality along a partial flattening of selected quadrilaterals. At full flattening, only each overloaded triangle needs to be flattened. There is then an exact formula involving the Bregman cost of all triangle rows that remain in the selected envelope. This supplies a nonlinear current-conservation problem and a rigorous dual obstruction to this particular family of weight choices.

Neither criterion is proved to succeed on every matched sphere. In particular, the estimates below do not replace a long connected cluster of one-sided ports by independently optimized local pieces. They give a size-independent theorem under stated cluster or curvature-spread hypotheses, not an automatic graph-gluing theorem.

## 1. Original source and complete triangle data

Fix the original simple triangulated white sphere, a matching of its cubic dual, and the original adjacent protected MAIN pair. Let \(V\) be its ordinary white vertices. The coefficient target at every \(f\in V\) is \(d=N-1\); both protected targets and weights are zero. A common scale of all positive ordinary weights is immaterial.

Let \(q_f=\log w_f^*\) be the complete marked curvature vector. Each original triangle \(t\) has a nonempty ordinary support \(I_t\subset V\). Define
\[
 Q_t(q)=
 \max_{\substack{a_f\ge0,\ f\in I_t\\ \sum_fa_f=1/2}}
 \left\{\mathcal E_t(a)+\sum_fa_fq_f\right\},
 \qquad
 \mathcal E_t(a)=\sum_{f\in I_t}
 \frac{\Lambda(\pi a_f)+\Lambda(\pi/2-\pi a_f)}{\pi}.
 \tag{1}
\]
Here \(\Lambda(\theta)=-\int_0^\theta\log|2\sin u|\,du\). A singleton row is \(Q_t(q)=q_f/2\). On a row with at least two ordinary corners the maximizer \(a_t^*=\nabla Q_t(q)\) is interior, with
\[
 a_{tf}^*=\frac1\pi\arctan\frac{w_f^*}{D_t},
 \qquad D_t^2=\sum_{\{i,j\}\subset I_t}w_i^*w_j^*.
 \tag{2}
\]
Write
\[
 E_t=Q_t(q)-a_t^*\cdot q=\mathcal E_t(a_t^*).
 \tag{3}
\]
This entropy is positive for every nonsingleton row and zero for a singleton row.

The original complete equations, with their absolute normalization, are
\[
 P(z)=\sum_tQ_t(z)-\sum_{f\in V}z_f,\qquad
 \nabla P(q)=0,\qquad P(q)=\Phi=\sum_tE_t .
 \tag{4}
\]
Thus \(\sum_{t\ni f}a_{tf}^*=1\). The number \(2\pi\Phi\) is the actual complete augmented volume. These are the calibrated Morse-source equations; no full positive-endpoint coefficient theorem is assumed.

At an original port \(e=(x,b,c,y)\), put
\[
 X_e=Q(x,b,y)+Q(x,c,y),\quad
 A_{e,C}=X_e,\quad
 A_{e,L}=\max\{q_c,Q(x,b,y)+q_c/2\},\quad
 A_{e,R}=\max\{q_b,Q(x,c,y)+q_b/2\}.
 \tag{5}
\]
The arguments in (5) are logarithmic coordinates of the same shared weights. A one-sided label overloading a protected middle is absent. The protected MAIN pair is not a matching edge, so the outer pair \(x,y\) cannot both be protected.

Fix a genuine label string \(\sigma\), not the all-CROSS string. Let \(S\) be its nonempty set of one-sided ports. At \(e\in S\), write \(z_e\) for the overloaded middle, \(t_e\) for its triangle, and \(t'_e\) for the other triangle. Define
\[
 M_\sigma=\sum_{e\in S}E_{t_e}>0,\qquad
 \epsilon_\sigma=\sum_{e\in S}
       \max\{0,q_{z_e}-X_e(q)\}.
 \tag{6}
\]
Every \(t_e\) is nonsingleton. The rows \(t_e,t'_e\) are distinct original triangles, and pairs belonging to distinct ports are disjoint as triangle rows, even when they share face coordinates.

The genuine shared envelope is
\[
 G_\sigma(z)=\sum_eA_{e,\sigma_e}(z)-\sum_{f\in V}z_f.
 \tag{7}
\]
Both comparison atoms of a one-sided maximum remain present. They will not be interpreted as separate quantum sectors.

## 2. Removed entropy and the exact local current

At each one-sided port, call its two comparison atoms the half-load atom and the collapsed atom:
\[
 A_{e,h}=Q_{t'_e}+\frac12q_{z_e},
 \qquad A_{e,c}=q_{z_e}.
 \tag{8}
\]
Relative to \(X_e\), the half-load atom removes precisely \(t_e\), while the collapsed atom removes both rows. The word “removes” here describes the algebraic envelope only, not a diagram operation.

Choose one of these atoms at every one-sided port. Let \(F_{\mathfrak a}\) be the resulting smooth cost, including the original target subtraction and the CROSS rows at all other ports. Its removed entropy and current at completeness satisfy
\[
 F_{\mathfrak a}(q)-\Phi
        =q\cdot p_{\mathfrak a}-E_{\mathfrak a}^{\rm rem},
 \qquad
 p_{\mathfrak a}=\nabla F_{\mathfrak a}(q),\qquad
 E_{\mathfrak a}^{\rm rem}\ge M_\sigma .
 \tag{9}
\]
Indeed, each removed row contributes \(Q_t(q)=E_t+a_t^*\cdot q\); the replacement half- or full-face load contributes no entropy. The complete face equation (4) cancels the gradients of all untouched rows and the target. Each local current is supported on that port's ordinary quadrilateral and has total sum zero.

One useful consequence is exact. If an average of these atom currents is zero, its averaged value defect is minus its averaged removed entropy, hence strictly negative. Thus a nonnegative zero-current obstruction at the *complete tangent* cannot be obtained for a fixed genuine non-CROSS string. This does not exclude an obstruction to its nonlinear capacity at another allocation. It also does not contradict failure of a coarse anchored branch, which allows many different genuine strings at its spectators.

## 3. Flatten only the selected quadrilaterals

Let \(W_e\subset V\) be the ordinary face set of \(e\). Require a displacement \(v\in\mathbb R^V\) to satisfy
\[
                   v_f+q_f=k_e\qquad(f\in W_e,\ e\in S),
 \tag{10}
\]
where the constants \(k_e\) are free. If selected quadrilaterals overlap in an ordinary face, their constants agree. Let \(\mathcal F_\sigma\) be this nonempty affine space; \(v=-q\) is always feasible. One may fix a global additive gauge.

For every smooth atom choice, (10) and the zero total of its local current give
\[
 p_{\mathfrak a}\cdot v=-p_{\mathfrak a}\cdot q.
 \tag{11}
\]
The same displacement applies to every occurrence of a face, including all spectator ports. It does not create independently weighted copies of a shared face.

For a row \(t\), define the fixed quadratic form
\[
 \overline L_t[v]
       =\frac1{4\pi}\sum_{\{i,j\}\subset I_t}(v_i-v_j)^2.
 \tag{12}
\]
The exact Hessian has conductances
\[
 \kappa^t_{ij}(z)=
 \frac{w_iw_j}{2\pi D_t(w_i+w_j)}\le\frac1{4\pi},
 \qquad
 v^{\mathsf T}\nabla^2Q_t(z)v
        =\sum_{\{i,j\}\subset I_t}\kappa^t_{ij}(z)(v_i-v_j)^2.
 \tag{13}
\]
The formulas hold also for two ordinary corners; a singleton has zero Hessian.

Crucially, the overloaded row \(t_e\) is absent from *both* atoms at every \(e\in S\). Define the surviving-row Laplacian
\[
 L_\sigma=\sum_{t\notin\{t_e:e\in S\}}\overline L_t.
 \tag{14}
\]
It is positive semidefinite and may have a larger kernel than the constants. Every \(F_{\mathfrak a}\) has Hessian bounded above by \(L_\sigma\) at every finite ordinary weight vector.

Taylor's formula, (9) and (11) now imply, for \(0<t\le1\),
\[
 \begin{aligned}
 F_{\mathfrak a}(q+tv)-\Phi
 &\le (1-t)[F_{\mathfrak a}(q)-\Phi]
           -t E_{\mathfrak a}^{\rm rem}
           +\frac{t^2}{2}v^{\mathsf T}L_\sigma v\\
 &\le (1-t)\epsilon_\sigma-tM_\sigma
           +\frac{t^2}{2}v^{\mathsf T}L_\sigma v .
 \end{aligned}
 \tag{15}
\]
For the last inequality, a half-load atom has negative complete defect because \(Q_{t_e}(q)>q_{z_e}/2\). A collapsed atom has defect at most the corresponding summand of \(\epsilon_\sigma\). Taking the maximum over the entire finite atom set proves
\[
 \boxed{\quad
 G_\sigma(q+tv)-\Phi
 \le (1-t)\epsilon_\sigma-tM_\sigma
                  +\frac{t^2}{2}v^{\mathsf T}L_\sigma v .
 \quad}
 \tag{16}
\]
This is the actual one-sided maximum, not a bound for only its convenient branch. It also retains the cost of every spectator triangle touched by \(v\).

## 4. A string-dependent Dirichlet capacity

Define
\[
 \mathcal C_\sigma=
       \min_{v\in\mathcal F_\sigma}v^{\mathsf T}L_\sigma v.
 \tag{17}
\]
This is a finite constrained nonnegative quadratic problem. A minimizer exists: after quotienting the null directions of the quadratic form restricted to the affine tangent space, it is a coercive quadratic on a finite-dimensional space. The minimizing potential need not be unique.

For an explicit linear description, choose difference rows \(B\) imposing equality of \(v+q\) on each connected component of overlapping selected quadrilaterals. Then
\[
 Bv=-Bq,\qquad
 L_\sigma v+B^{\mathsf T}\lambda=0
 \tag{18}
\]
are the constraint and stationarity equations. They retain ordinary face coordinates, rather than replacing them by independent incidence variables.

When \(L_\sigma\) has only the constant kernel, its Green inverse on the zero-sum space gives
\[
 \mathcal C_\sigma
   =(Bq)^{\mathsf T}
       (B L_\sigma^+B^{\mathsf T})^+(Bq).
 \tag{19}
\]
The outer pseudoinverse permits redundant difference rows. Equation (19) must not be used without modification when surviving rows disconnect the graph. In that case (17)–(18) remain the definition and exact finite system.

For completeness, the general quadratic dual is
\[
 \mathcal C_\sigma
   =\max_{\substack{\lambda\\B^{\mathsf T}\lambda\perp\ker L_\sigma}}
       \left\{-2\lambda\cdot Bq
          -\lambda^{\mathsf T}B L_\sigma^+B^{\mathsf T}\lambda\right\}.
 \tag{20}
\]
Minimizing \(v^{\mathsf T}L_\sigma v-2\lambda\cdot(Bv+Bq)\) first gives this expression up to replacing \(\lambda\) by its negative. Equality follows from a minimizer in (18), or directly by completing the square on the range of \(L_\sigma\). The orthogonality condition is essential: free constant values on disconnected surviving components may satisfy part of the flattening constraints at no energy cost.

Consequently the sufficient test is
\[
 \gamma_\sigma(t):=
 tM_\sigma-(1-t)\epsilon_\sigma
                    -\frac12t^2\mathcal C_\sigma>0
 \quad\text{for some }0<t\le1.
 \tag{21}
\]
It provides the single genuine-string witness \(e^{q+tv}\). No nonlinear minimizer needs to be found. Notably,
\[
                   \mathcal C_\sigma<2M_\sigma
 \tag{22}
\]
is sufficient at \(t=1\), regardless of the complete balance defect. If \(\epsilon_\sigma=0\), some sufficiently small positive \(t\) always works.

The old total-energy number is an upper bound for \(\mathcal C_\sigma\): use \(v=-q\), and then restore all the deleted rows. Thus this criterion can never lose a string already certified by the corresponding total-energy estimate. It can gain substantially when one-sided ports occupy a small region, when much of the original logarithmic variation lies elsewhere, or when the compulsory row deletions disconnect the energy graph.

## 5. Full flattening needs only the overloaded triangles

The quadratic estimate is not the only available budget. For every original triangle define its nonnegative Bregman cost
\[
 D_t(v)=Q_t(q+v)-Q_t(q)-a_t^*\cdot v.
 \tag{23}
\]
There is a strictly weaker sufficient constraint than (10). Require only
\[
 v_f+q_f=k_e\qquad(f\in I_{t_e},\ e\in S).
 \tag{24}
\]
Call this larger affine space \(\widehat{\mathcal F}_\sigma\). The overloaded middle is one of these corners, so its new logarithmic weight is \(k_e\). At least one outer corner is ordinary and belongs to both triangles. Its new logarithmic weight is also \(k_e\). The pure allocation on that corner in the variational formula (1) therefore gives
\[
                   Q_{t'_e}(q+v)\ge k_e/2 .
 \tag{24a}
\]
Thus the half-load atom is at least \(k_e\), which is exactly the collapsed atom. The half-load atom really is maximal at every vector satisfying (24). The other middle weight need not be flattened. This conclusion uses an allowed vertex allocation of the original triangle, not a subdivision of the LEFT/RIGHT source.

For the resulting smooth cost, the removed rows are exactly the \(t_e\). Its local current is \(\tfrac12e_{z_e}-a_{t_e}^*\), supported on \(I_{t_e}\), with total zero. Consequently (24) gives the required current cancellation even though the collapsed-atom current need not cancel. Equation (9) and the exact Taylor remainder (23) give
\[
 \boxed{\quad
 G_\sigma(q+v)-\Phi
       =\sum_{t\notin\{t_e:e\in S\}}D_t(v)-M_\sigma,
       \qquad v\in\widehat{\mathcal F}_\sigma .
 \quad}
 \tag{25}
\]
This formula is an exact entropy/current budget at fixed real weights. In particular, it yields a certificate whenever
\[
 \sum_{t\notin\{t_e:e\in S\}}D_t(v)<M_\sigma .
 \tag{26}
\]
Define the weaker-constraint capacity
\[
 \widehat{\mathcal C}_\sigma
     =\min_{v\in\widehat{\mathcal F}_\sigma}
                         v^{\mathsf T}L_\sigma v
     \le\mathcal C_\sigma.
 \tag{26a}
\]
Since \(\sum_{t\notin\{t_e\}}D_t(v)\le v^{\mathsf T}L_\sigma v/2\), a sufficient condition with no balance-defect restriction is
\[
                  \widehat{\mathcal C}_\sigma<2M_\sigma.
 \tag{26b}
\]
The exact finite systems (18)–(20) apply with \(B\) replaced by the difference constraints of (24). The intermediate-\(t\) estimate (16) still uses the stronger quadrilateral constraints: it is not asserted for arbitrary partial triangle flattening.

A finite minimizer of the left side of (26), when it exists, has a direct current interpretation. On each ordinary face outside the union of overloaded triangle supports, its first derivative is zero:
\[
 \sum_{\substack{t\ni f\\t\notin\{t_e\}}}
          \left(a_{tf}(q+v)-a_{tf}^*\right)=0.
 \tag{27}
\]
On a connected component of overlapping overloaded triangles, only its common flattening value is free, so the sum of these derivatives over that component is zero. Thus the extension conserves the retained angle current at every free face and across each constrained component. It accounts for all the original exterior triangles; it is not a local Cauchy estimate with independently chosen boundary data.

There is also a rigorous lower certificate for this restricted nonlinear problem. Choose any simplex load \(\widetilde a_t\) on each surviving row, with its original support and total \(1/2\). Set
\[
 \begin{aligned}
 I_t(\widetilde a_t)
   &=Q_t(q)-\mathcal E_t(\widetilde a_t)
                       -q\cdot\widetilde a_t\ge0,\\
 J&=\sum_{t\notin\{t_e\}}(\widetilde a_t-a_t^*).
 \end{aligned}
 \tag{28}
\]
The variational definition implies
\[
 \sum_{t\notin\{t_e\}}D_t(v)
       \ge J\cdot v-\sum_{t\notin\{t_e\}}I_t(\widetilde a_t).
 \tag{29}
\]
Use the difference matrix \(B\) for (24). If \(J=B^{\mathsf T}\lambda\), this lower bound is constant throughout the triangle-flattening affine space:
\[
 \sum_{t\notin\{t_e\}}D_t(v)
       \ge-\lambda\cdot Bq-\sum_{t\notin\{t_e\}}I_t(\widetilde a_t).
 \tag{30}
\]
If the right side is at least \(M_\sigma\), no fully flattened witness can prove a gap for this string. This is an obstruction to (26), not to an arbitrary shared vector and not to the quantum invariant. Only weak duality is used; no unproved interior optimizer or minimax exchange is needed.

## 6. A local cluster bound, independent of unrelated faces

Let \(\Delta\) be the maximum degree of the ordinary white graph. Form a graph whose vertices are the ports in \(S\), joining two when their quadrilaterals share an ordinary face. For each of its components \(C\), put
\[
 W_C=\bigcup_{e\in C}W_e,\qquad
 k_C=|C|,\qquad
 K_C=\max_{f\in W_C}q_f-\min_{f\in W_C}q_f.
 \tag{31}
\]
The sets \(W_C\) are disjoint. Define a trial displacement on each \(W_C\) by
\[
 v_f=-q_f+\frac12
       \left(\max_{g\in W_C}q_g+\min_{g\in W_C}q_g\right),
 \qquad v_f=0\text{ off }\bigcup_CW_C .
 \tag{32}
\]
It is feasible, and \(|v_f|\le K_C/2\). Because a quadrilateral has at most four ordinary vertices, \(|W_C|\le4k_C\).

Every ordinary white edge belongs to two original triangles. Restoring all deleted rows and using \((a-b)^2\le2a^2+2b^2\) gives
\[
 \begin{aligned}
 \mathcal C_\sigma
 &\le\frac1{2\pi}\sum_{\{f,g\}\text{ ordinary edge}}(v_f-v_g)^2\\
 &\le\frac{\Delta}{\pi}\sum_fv_f^2
 \le\boxed{\ \frac{\Delta}{\pi}\sum_Ck_CK_C^2\ }.
 \end{aligned}
 \tag{33}
\]
Edges between two selected components or from a component to its exterior are included. No independence of their energies is assumed.

If each selected quadrilateral has logarithmic curvature oscillation at most \(K_0\), a chain of \(k_C\) overlapping quadrilaterals gives \(K_C\le k_CK_0\). Therefore
\[
 \mathcal C_\sigma\le\frac{\Delta K_0^2}{\pi}\sum_Ck_C^3 .
 \tag{34}
\]
In particular, strings whose one-sided clusters all have size at most \(B\) satisfy
\[
             \mathcal C_\sigma\le
             \frac{\Delta B^2K_0^2}{\pi}|S|.
 \tag{35}
\]
This estimate remains valid when the total diagram and the number of separate clusters are arbitrarily large. It requires no bound on the total logarithmic energy elsewhere in the sphere.

For full triangle flattening, form the analogous components using intersections of the sets \(I_{t_e}\), and denote their sizes and logarithmic oscillations by \(\widehat k_C,\widehat K_C\). Each overloaded triangle has at most three ordinary corners. The same trial potential and the same edge inequality therefore prove the sharper estimate
\[
 \boxed{\quad
 \widehat{\mathcal C}_\sigma
       \le\frac{3\Delta}{4\pi}
                    \sum_C\widehat k_C\widehat K_C^2 .
 \quad}
 \tag{35a}
\]
Every white edge remains counted, including edges joining two different selected components. In particular, if these components have size at most \(B\) and each overloaded triangle has logarithmic oscillation at most \(K_0\), then
\[
 \widehat{\mathcal C}_\sigma
             \le\frac{3\Delta B^2K_0^2}{4\pi}|S|.
 \tag{35b}
\]

## 7. Uniform consequences and the remaining large-cluster problem

Suppose a collection of genuine strings, possibly on many unchanged marked spheres, has
\[
 \mathcal C_\sigma\le C_0|S|,\qquad
 E_{t_e}\ge m_0>0,\qquad
 \max(0,q_{z_e}-X_e(q))\le\epsilon_0 .
 \tag{36}
\]
For a fixed \(0<t\le1\), define
\[
       \delta=t m_0-(1-t)\epsilon_0-\frac12t^2C_0.
 \tag{37}
\]
If \(\delta>0\), each string has a shared witness with
\[
                 G_\sigma\le\Phi-\delta|S|.
 \tag{38}
\]
Unlike the total-energy criterion, the allowed positive defect does not shrink merely because many unrelated faces are added to the fixed diagram. A convenient sufficient choice is
\[
 t_0=\min(1/2,m_0/C_0),\qquad
 \epsilon_0<t_0m_0/2
 \tag{39}
\]
when \(C_0>0\). If \(C_0=0\), full flattening gives gap \(m_0|S|\) without a defect restriction.

Equation (35) proves (36) for bounded one-sided clusters under local degree and curvature-ratio bounds. Alternatively, if the *entire* ordinary curvature vector has oscillation at most \(K\) and ordinary degree at most \(\Delta\), (33) proves (36) for every string with
\[
                         C_0=\Delta K^2/\pi .
 \tag{40}
\]
This is a size-independent sufficient class stated entirely in original geometric data. It does not assert that arbitrary bounded-degree sphere packings have a uniform global curvature spread.

A row-entropy lower bound can also be made explicit. If the ratio of positive corner weights in every original triangle is at most \(K_{\rm rat}\), put
\[
 a_0=\frac1\pi\arctan\frac1{\sqrt{K_{\rm rat}^2+2K_{\rm rat}}},
 \qquad m_0=2\,
 \frac{\Lambda(\pi a_0)+\Lambda(\pi/2-\pi a_0)}{\pi}>0.
 \tag{41}
\]
Equation (2) bounds each nonsingleton load between \(a_0\) and \(1/2-a_0\); concavity and symmetry of the entropy summand give (41). No packing ratio theorem is inferred solely from the graph degree.

There is a separate uniform criterion that permits arbitrary complete balance defects. Suppose the strings under consideration satisfy
\[
 \widehat{\mathcal C}_\sigma\le\widehat C_0|S|,
 \qquad E_{t_e}\ge m_0>0,\qquad
                         \widehat C_0<2m_0 .
 \tag{41a}
\]
Equations (25)–(26b) give a gap of at least
\((m_0-\widehat C_0/2)|S|\). One explicit sufficient hypothesis for bounded overloaded-triangle clusters is
\[
                     \frac{3\Delta B^2K_0^2}{4\pi}<2m_0.
 \tag{41b}
\]
For arbitrary cluster sizes, a uniform global ordinary curvature oscillation \(K\) instead gives the sufficient condition \(3\Delta K^2/(4\pi)<2m_0\). These are conditions on the unchanged diagram and complete packing. They do not infer that any specified combinatorial class satisfies the inequalities without a geometric argument.

For any one fixed diagram there are finitely many genuine strings. If (21), (26), or another independently proved shared-vector test supplies a strict witness for each non-CROSS string, these singleton branches constitute a genuine finite-sector cover. Their weights can differ between strings. The local phase-uniform bounds, the degree-\(d\) full-Hermite filling norm, and the nonzero general-Morse CROSS theorem then give the usual long-filling full-source comparison, with its original knot-pairing and metric hypotheses. This is the already established cover-to-volume interface, not a new charge or scalar normalization.

What has not been proved is that every string on an arbitrary sphere satisfies (21) or (26). The cluster bound (34) can become large for a long connected chain of one-sided ports; bounded local ratios and ordinary degree alone do not remove that term. Nor do favorable independent port energies imply a bound for their union: their flattening constants must agree whenever the ports share a face. The nonlinear current problem (25)–(30) retains precisely this possible obstruction.

## 8. Dependency and interpretation

The new calculations use the exact triangle potential and complete face equations; the original CROSS/LEFT/RIGHT envelopes; and the elementary Hessian bound (13). Their immediate output is a shared coefficient certificate or a lower obstruction to a specified restricted certificate. They require no sampled quantum values, guessed phase cancellation, independent per-incidence weights, or new change of the diagram.

For source transfer, the relevant existing results are the exact general Morse coefficient identity, the real-spectral phase-uniform local envelope theorem, the finite full-Hermite norm on polynomials of degree at most \(N-1\) in each variable, and the nonzero all-CROSS long-filling contribution with actual metric completion. The protected zeros, original marked cut, signed fixed powers, both level parities, and original framing factors remain in those theorems.

This note does not claim a short-filling theorem, a moving-meridian expansion, or a universal volume theorem. Its advance over the global power criterion is the deleted-row localized capacity, the reduction from quadrilateral to overloaded-triangle flattening at a full step, the exact retained-row Bregman identity, and uniform bounds for controlled clusters or global curvature spread.
