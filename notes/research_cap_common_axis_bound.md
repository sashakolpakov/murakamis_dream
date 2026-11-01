# Bounding a signed cap contribution by two derivatives of its pressure

The polynomial remaining after every other face has been summed contains
information about cancellations that is lost in an estimate of each local
factor. At odd levels it factors into linear forms with nonnegative
coefficients. Two derivatives of its logarithm then suffice for a useful
bound on its negative real axis. The finite inequality is proved first;
sections 2–5 show exactly how it applies to the prescribed coefficient of
the original source.

The application fixes the selected cap spectrum at \(+2\) and all other
spectra at \(-2\). The [uniform spectral extension](research_cap_uniform_spectral_gap.md)
allows the selected parameter to vary over \([-2,2]\). Both applications
retain the odd-level restriction. Neither bounds the entire filled-knot
remainder.

## 1. Finite polynomial theorem

Let \(d\ge1\), and suppose a nonzero homogeneous binary polynomial has the factorization
\[
 P(A,C)=P(1,1)\prod_{r=1}^{d}\bigl[(1-p_r)C+p_rA\bigr],
 \qquad P(1,1)>0,\quad 0\le p_r\le1.
 \tag{1}
\]
Factors with \(p_r=0\) or \(p_r=1\) are allowed. Define
\[
 \nu_d=\frac1d\sum_r p_r,\qquad
 \kappa_d=\frac1d\sum_r p_r(1-p_r),\qquad
 R_d=\max\{1-\nu_d-\kappa_d,\ \nu_d-\kappa_d,\ 1-4\kappa_d\}.
 \tag{2}
\]
Here \(\kappa_d\) is the average Bernoulli variance. It is not the variance of the root parameters \(p_r\). The latter is \(\nu_d-\kappa_d-\nu_d^2\). In particular
\[
 0\le\kappa_d\le\nu_d(1-\nu_d),\qquad \frac14\le R_d\le1.
 \tag{3}
\]
The lower bound on \(R_d\) follows because its first two entries sum to \(1-2\kappa_d\ge1/2\).

**Finite theorem.** Put
\[
 B^- =\sup_{0\le t\le1}|P(-t,1)|,\qquad
 B^+ =\sup_{0\le t\le1}|P(-1,t)|.
 \tag{4}
\]
Then
\[
 \boxed{\ \max(B^-,B^+)\le P(1,1)R_d^{d/2}.\ }
 \tag{5}
\]

For the proof, the arithmetic-geometric mean inequality on the nonnegative squared factors gives, for each fixed \(t\),
\[
 \begin{aligned}
 \frac{|P(-t,1)|^2}{P(1,1)^2}
 &\le \left(\frac1d\sum_r[1-(1+t)p_r]^2\right)^d,\\
 \frac{|P(-1,t)|^2}{P(1,1)^2}
 &\le \left(\frac1d\sum_r[t-(1+t)p_r]^2\right)^d.
 \end{aligned}
 \tag{6}
\]
No factor is divided out, so zeros cause no exception. Using \(d^{-1}\sum p_r^2=\nu_d-\kappa_d\), the two averages are
\[
 \begin{aligned}
 Q_-(t)&=1-2(1+t)\nu_d+(1+t)^2(\nu_d-\kappa_d),\\
 Q_+(t)&=t^2-2t(1+t)\nu_d+(1+t)^2(\nu_d-\kappa_d).
 \end{aligned}
 \tag{7}
\]
They are convex quadratics: their quadratic coefficients are respectively \(d^{-1}\sum p_r^2\) and \(d^{-1}\sum(1-p_r)^2\). A convex function on \([0,1]\) is bounded above by the larger endpoint value. The endpoint values here are
\[
 Q_-(0)=1-\nu_d-\kappa_d,\quad
 Q_+(0)=\nu_d-\kappa_d,\quad
 Q_-(1)=Q_+(1)=1-4\kappa_d.
 \tag{8}
\]
Equations (6)--(8) prove (5). The essential order is to average the squared factors at one common value of \(t\), and only then maximize. Maximizing every root factor separately loses this information.

The numbers in (2) can be read from the polynomial itself without finding its roots:
\[
 \nu_d=\frac1d\left.\partial_z\log P(e^z,1)\right|_{z=0},\qquad
 \kappa_d=\frac1d\left.\partial_z^2\log P(e^z,1)\right|_{z=0}.
 \tag{9}
\]
The theorem is invariant under exchanging \(A,C\), which replaces \(\nu_d\) by \(1-\nu_d\) and leaves \(\kappa_d\) unchanged.

## 2. The exact original cap pairing

Fix a connected matched simple-sphere Morse source with \(R\) original crossing regions, its original cups, caps, and main mark. The two protected face variables are set to zero; all \(R\) ordinary targets remain \(d=N-1\). Fix one protected left coupon with the literal quartet
\[
                  (C,0,A,0).
 \tag{10}
\]
Use its actual spectrum \(+2\), and use the actual central polynomial at spectrum \(-2\) at every other original region. This is one fixed genuine sector, not an arbitrary mixture of local comparison branches.

Remove only the common raw unit sign from each central coupon. Let \(P_{e,\mathrm C}(-2;L)\) denote the resulting positive polynomial, including its original scalar normalization. Extract every other ordinary variable first:
\[
 P_N(A,C)=
 \left[\prod_{f\ne A,C\text{ ordinary}}L_f^d\right]
 \prod_{e\ne e_*}P_{e,\mathrm C}(-2;L)
 =\sum_{j=0}^{d}p_{N,j}A^jC^{d-j}.
 \tag{11}
\]
Every shared variable is still the original face variable. The total degree is exactly \(d\), since \((R-1)d-(R-2)d=d\). Positivity of the endpoint path coefficients gives \(p_{N,j}\ge0\).

Put \(\theta=\pi/N\), \(M=\lfloor N/2\rfloor-1\), and
\[
 s_r=2\sin(r\theta),\quad c_r=2\cos((2r+1)\theta),\quad
 U_{N,j}=\left(\prod_{r=1}^{j}s_r^2\right)
                       \prod_{r=j+1}^{d}(2-c_r).
 \tag{12}
\]
The literal protected left numerator is
\[
 H_{\mathrm L}(C,0,A,0;+2)
   =\sum_{j=0}^{M}(-1)^jU_{N,j}C^jA^{d-j}.
 \tag{13}
\]
Thus imposing the two remaining original targets gives exactly
\[
 S_N=[A^dC^d]\,H_{\mathrm L}(C,0,A,0;+2)P_N(A,C)
                  =\sum_{j=0}^{M}(-1)^jU_{N,j}p_{N,j}.
 \tag{14}
\]
The corresponding unadjusted raw sector differs by the product of the original central unit signs. There is no alteration of its magnitude. At odd levels \(d\) is even and these particular signs are already positive. Equation (14) is a source coefficient; no filling functional or physical framing normalization has yet been applied.

The exact all-index positive cap moment law provides a positive random variable \(X_N\) with
\[
 \mathbb E X_N^j=\frac{U_{N,j}}{U_{N,0}}\quad(0\le j\le d),\qquad
 U_{N,0}=\csc^2\frac\pi{2N}\le N^2,\qquad
 \mathbb E X_N^d=N^2\sin^2\frac\pi{2N}\le\frac{\pi^2}{4}.
 \tag{15}
\]
Its support is not assumed bounded. Define the actual omitted finite tail
\[
 T_N=\sum_{j=M+1}^{d}(-1)^jU_{N,j}p_{N,j}.
 \tag{16}
\]
Then, with no moment above degree \(d\),
\[
 S_N+T_N=U_{N,0}\mathbb E P_N(-X_N,1).
 \tag{17}
\]
For \(X_N\le1\) use the first supremum in (4). For \(X_N\ge1\), homogeneity gives \(P_N(-X_N,1)=X_N^dP_N(-1,X_N^{-1})\). Consequently
\[
 |S_N|\le U_{N,0}\left(B_N^-+\mathbb E X_N^d B_N^+\right)+|T_N|.
 \tag{18}
\]
This is the existing full-exterior negative-axis reduction, stated here with the exact left-cap coordinate order. It uses coherent extraction of the entire exterior, not an independent norm of each incident coupon.

## 3. Why the actual odd polynomial meets the finite hypothesis

At \(N=2m+1\), the actual central endpoint numerator is exactly
\[
 P_{e,\mathrm C}(-2;x,b,c,y)
       =N^2D_m(x,b,y)D_m(x,c,y),\qquad
 D_m(x,b,y)=\det\left(bI+\frac x2H_-+\frac y2H_+\right),
 \tag{19}
\]
where the two physical Hermitian matrices \(H_-,H_+\) are positive definite. All normalizations in (19) are those of the original endpoint source. In particular the factor \(N^2\) is retained.

If all surviving arguments have positive imaginary parts, the matrix in (19) has positive-definite imaginary part and is invertible. Each determinant is therefore real stable. Products, identification of shared variables, coefficient extraction by differentiation followed by evaluation at zero, and specialization of the protected variables to zero preserve real stability or yield the zero polynomial. These are applied to the actual full exterior in (11). When \(P_N\ne0\), binary homogeneity and nonnegative coefficients give exactly (1), with \(d=N-1\).

Nonvanishing for all sufficiently large odd levels follows from the same original positive coefficient packet used below. For a level where \(P_N=0\), the sector itself is zero and every upper bound is automatic. Nothing here substitutes a positive comparator for an even-level numerator: that substitution would not preserve signed negative-axis values.

Combining (5), (15), and (18) gives the finite original-target estimate
\[
 |S_N|\le N^2\left(1+\frac{\pi^2}{4}\right)
                 P_N(1,1)R_{N-1}^{(N-1)/2}+|T_N|,
               \qquad N\text{ odd}.
 \tag{20}
\]

## 4. The pressure and the omitted tail use the same original demands

Assume the original exterior admits a strictly positive feasible half-load table with every other ordinary face load equal to one, and its supported ordinary pair graph is connected. Keep \(A=C=1\). Let \(I\) consist of the other ordinary faces, write \(L_i=e^{w_i}\), and define
\[
 \mathcal F(z,w)=\sum_{t\text{ exterior}}Q_t(L)-\sum_{i\in I}w_i,
 \qquad A=e^z, C=1.
 \tag{21}
\]
The triangles are precisely the original triangles outside the selected cap. For supported corner loads \(\alpha_f\ge0\), summing to \(1/2\), the triangle potential is
\[
 Q_t(L)=\max_{\sum\alpha_f=1/2}
       \sum_{f\in t}\bigl[f(\alpha_f)+\alpha_f\log L_f\bigr],\qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}{\pi},\qquad
 \Lambda(t)=-\int_0^t\log|2\sin u|\,du.
 \tag{22}
\]
Protected zero corners have forced load zero and are omitted from the supported maximization.

The strict table makes the recession function positive in every nonzero direction of the \(I\) coordinates: equality between a triangle maximum and its strictly positive weighted average would force the log-direction constant on that triangle. Connectedness, together with the fixed boundary values at \(A,C\), then forces the whole direction to be zero. Compactness of the unit sphere gives coercivity. The positive triangle Laplacians give a positive-definite Hessian after grounding \(C\). Thus the stationary \(w_*\) exists, is finite, and is unique; the implicit solution \(w(z)\) exists near zero. Define
\[
 F(z)=\mathcal F(z,w(z)),\qquad
 M_{\mathrm{cap}}=F(0),\quad \nu=F'(0),\quad
 \kappa=F''(0)>0.
 \tag{23}
\]
The second derivative is the Schur complement of the original triangle Hessian, not the curvature of an independently reweighted star.

The actual positive determinant packet gives locally uniform convergence of the holomorphic logarithms
\[
 \frac1N\log P_N(e^z,1)\longrightarrow F(z)
 \quad\text{on a fixed complex disk around }0,\qquad N\text{ odd}.
 \tag{24}
\]
Here the finite coefficient integral extracts exactly the \(I\) targets \(d\). Its real radius is the actual finite stationary radius. The determinant contraction has a strict global angular gap because the supported pair graph is connected and each edge character is the primitive difference of two face phases. The finite Hessian is uniformly positive after division by \(N\); the positive determinant pencils have all fixed logarithmic derivatives \(O(N)\) on a uniform complex neighborhood. The local Gaussian and the complementary angular gap therefore give a relative, locally uniform packet. Its analytic logarithm and Cauchy differentiation yield
\[
 \frac1N\log P_N(1,1)\to M_{\mathrm{cap}},\qquad
 \nu_{N-1}\to\nu,\qquad \kappa_{N-1}\to\kappa.
 \tag{25}
\]
The factors \(N^2\) in (19) remain present and contribute only \(O(\log N/N)\) to the normalized logarithm. No differentiation of a merely pointwise rate is used. This local proof is the effective-response theorem; its input is the exact Morse source and connected determinant graph, not a flat-plat layout.

Let \(\Phi\) be the original complete augmented source action, normalized so that \(2\pi\Phi\) is the actual augmented complement volume. Let \(R(s)\) be the residual complete triangle capacity with exterior loads \(A:s,C:1-s\), all other ordinary loads one, and the same protected zeros. The original complete positive action gives
\[
 \Phi=\max_{1/2\le s\le1}\{R(s)+2f(s-1/2)\},\qquad
 \max_{1/2\le s\le1}R(s)\le\Phi-\gamma
 \tag{26}
\]
for some \(\gamma>0\). The second statement uses the unique strict complete optimizer: interior splits have a strictly positive restored cap entropy, while the two endpoint splits make its half-triangle a pure vertex and cannot be the strict optimizer. Compactness supplies a uniform loss.

The uniform closed coefficient upper for the actual endpoint central polynomials gives \(\limsup N^{-1}\log p_{N,j_N}\le R(s)\) whenever \(j_N/d\to s\). Also \(U_{N,j}\le N^2\) for every \(0\le j\le d\). The omitted tail in (16) consequently satisfies, for all sufficiently large levels,
\[
                         |T_N|\le e^{N(\Phi-\gamma/2)}.
 \tag{27}
\]
At odd levels the first omitted index is exactly \(j=m=d/2\); this endpoint is included in (26). No endpoint current or low-degree cutoff has been dropped.

## 5. A two-derivative sufficient criterion

Define
\[
 \mathscr L(\nu,\kappa)
 =-\frac12\log\max\{1-\nu-\kappa,\ \nu-\kappa,\ 1-4\kappa\}.
 \tag{28}
\]
Equations (20), (25), and (27) prove
\[
 \boxed{\quad
 \limsup_{\substack{N\to\infty\\N\text{ odd}}}\frac1N\log|S_N|
 \le\max\left\{M_{\mathrm{cap}}-\mathscr L(\nu,\kappa),\
                         \Phi-\frac\gamma2\right\}.\quad}
 \tag{29}
\]
Thus \(\mathscr L(\nu,\kappa)>M_{\mathrm{cap}}-\Phi\) proves a strict absolute rate gap for this original sector, at the fixed spectra under consideration. If the difference is \(\delta>0\), the limiting gap is at least \(\min(\delta,\gamma/2)\). A bound with any smaller positive gap holds for all sufficiently large odd levels. A nonstrict inequality gives the weak absolute rate bound.

This criterion can be combined with the existing Mahler or higher-derivative criteria by taking their maximum. It is not claimed to dominate each of them for every root distribution. It instead controls the common negative-axis parameter directly. In the limiting root-measure notation of the existing pressure theorem, the conclusion is the additional explicit lower bound \(\chi_D\ge\mathscr L(\nu,\kappa)\).

## 6. Exact scope of the 54-region application

For the recorded original 54-region source, the selected region is \(32\), its quartet is \((0,50,16,29)\), and the protected faces are \(29,50\). Thus (10) uses
\[
                         A=L_{16},\qquad C=L_0.
 \tag{30}
\]
The response calculation must use the load of face \(16\) for \(\nu\). This is precisely the cap index paired in (14). Its complementary boundary coordinate would give \(1-\nu\), which leaves (28) unchanged. The recorded positive spectator table gives the strict feasible table required in section 4; its ordinary support graph is connected. No changed matching, mark, or knot is introduced.

The following are sufficient **certified classical enclosures**, stated separately from a numerical locating calculation:
\[
 \frac{27}{100}\le\nu\le\frac{28}{100},\qquad
 \kappa\ge\frac{11}{125},\qquad
 M_{\mathrm{cap}}\le\frac{33947}{500},\qquad
 \Phi\ge\frac{67687}{1000}.
 \tag{31}
\]
The three entries of (28) are at most \(.642,.192,.648\), respectively, so their maximum is at most \(81/125\). The elementary exact inequality
\[
                  -\frac12\log(81/125)>\frac{27}{125}=0.216
 \tag{32}
\]
then gives \(M_{\mathrm{cap}}-\mathscr L<67.678\le\Phi-.009\). Hence (29) gives a positive limiting gap at least \(\min(.009,\gamma/2)\). The constant \(\gamma\) is the original omitted-tail gap; this argument does not claim an explicit lower bound for it.

For a rational proof of (32), put \(x=22/103\). Since \(125/81=(1+x)/(1-x)\), the positive series \(\tfrac12\log((1+x)/(1-x))=x+x^3/3+x^5/5+\cdots\) gives a rational lower bound. Already \(x+x^3/3>27/125\), as an exact cross-multiplication check shows.

Both parts of (31) are supplied by exact rational interval certificates. The complete feasible-flow entropy certificate gives the last inequality without an approximate stationary equation. The response certificate gives the first three by the local argument in the next section. Consequently this particular fixed-spectrum odd singleton satisfies (29) with a positive gap. This conclusion does not depend on a floating-point saddle or on a sample of quantum levels.

## 7. The response certificate localizes the actual stationary point

The source certificate fixes all 54 ordered quartets and the two protected faces. At the selected cap, the two remaining ordinary faces are exactly (30). The response certificate gives positive rational trial weights \(L^0_f\), with \(L^0_A=L^0_C=1\), and rational electrical trial potentials \(h_f\), with \(h_A=1,h_C=0\). There are \(n=52\) free log weights and 106 exterior triangle rows. The proof uses a Euclidean ball of radius \(r=1/1000\) about the exact log vector \(w^0_f=\log L^0_f\). The log vector need not itself be rational; interval evaluation at rational positive weights encloses all required quantities.

For each original supported triangle and each pair of distinct supported corners, its Hessian conductance is
\[
 g_{ab}=\frac{ab}{2\pi(a+b)\sqrt{ab+ac+bc}},\qquad
                    0<g_{ab}\le\frac1{4\pi}.
 \tag{33}
\]
With exactly two supported corners, put the third weight equal to zero. A singleton row has zero Hessian and its exact value is one half of the logarithm of its weight. In (33), the inequality follows from \(\sqrt{ab+ac+bc}\ge\sqrt{ab}\) and \(a+b\ge2\sqrt{ab}\).

The original supported pair graph has distance at most four from the grounded set \(\{A,C\}\). Let \(g_0\) be the smallest certified lower bound for an individual conductance at the trial weights. For every free vector \(v\), extend it by zero at \(A,C\), choose one path of length at most four from each free vertex to a ground, and use Cauchy's inequality along each path. Even allowing every edge to be counted in all \(n\) paths gives
\[
 v^TH_{II}(w^0)v\ge\lambda\|v\|_2^2,
                      \qquad \lambda=\frac{g_0}{4n}.
 \tag{34}
\]
Parallel conductance contributions only strengthen this inequality.

On the radius-\(r\) ball, each log coordinate changes by at most \(r\). Each numerator and denominator factor in (33) then gives
\[
 e^{-4r}g_{ab}(w^0)\le g_{ab}(w)\le e^{4r}g_{ab}(w^0),\qquad
 H_{II}(w)\succeq(1-4r)\lambda I.
 \tag{35}
\]
Let \(g_{\max}\) be a certified bound for the largest absolute component of \(\partial_I\mathcal F(0,w^0)\). The exact certificate verifies
\[
                  8g_{\max}<(1-4r)\lambda r.
 \tag{36}
\]
Since \(\sqrt{52}<8\), at every point of the boundary sphere the radial derivative is positive: the integrated Hessian contribution is at least \((1-4r)\lambda r^2\), while the initial gradient contributes no less than \(-8rg_{\max}\). A minimum on the closed ball therefore lies in its interior. Strict convexity makes this the unique positive stationary exterior. In particular the certified point is the same \(w_*\) used in (23), rather than an unrelated nearby solution.

For the response, let \(E_0=\sum g_{ab}(w^0)(h_a-h_b)^2\) be the trial Dirichlet energy, with original triangle contributions counted once each. Let \(r_I\) be the free electrical residual, namely the free part of the weighted Laplacian applied to \(h\). Orthogonal quadratic minimization with the two boundary potentials fixed gives
\[
 \kappa(w^0)=E_0-r_I^TH_{II}(w^0)^{-1}r_I
       \ge E_0-\frac{\|r_I\|_2^2}{\lambda}.
 \tag{37}
\]
This is a lower bound; a trial Dirichlet energy by itself would be an upper bound and would not suffice. By (35), minimization over the same boundary potentials gives
\[
 \kappa(w_*)\ge(1-4r)\kappa(w^0)
 \ge(1-4r)\left(E_0-\frac{n r_{\max}^2}{\lambda}\right),
 \tag{38}
\]
where \(r_{\max}\) bounds the largest absolute residual entry. The verifier proves that the last expression exceeds \(11/125\).

The load \(\nu\) is \(\partial_A\mathcal F\). If \(D_A\) counts the original supported pair incidences at \(A\), including multiplicities, (33) and the coordinate bound give
\[
 |\nu(w_*)-\nu(w^0)|\le\frac{rD_A}{4\pi}.
 \tag{39}
\]
The resulting interval lies strictly inside \((27/100,28/100)\). Finally convex minimization gives \(M_{\mathrm{cap}}\le\mathcal F(0,w^0)\), and the certified upper endpoint of that trial value is below \(33947/500\).

All these tests are evaluated with outward integer fixed-point intervals at scale \(10^{40}\). Square roots use integer square-root bounds. Arctangents first use the exact half-angle identity until the argument is at most \(1/2\), then use 80 alternating terms with an explicit next-term remainder. Logarithms use the positive artanh series after power-of-two scaling. For \(0<t<1/2\), the triangle entropy is evaluated through
\[
 J(t)=t\log(2\pi t)-t
       -\sum_{k=1}^{20}\frac{\zeta(2k)t^{2k+1}}{k(2k+1)}
       +\mathcal R(t),\qquad
 -\frac{2t^{43}}{21\cdot43(1-t^2)}\le\mathcal R(t)\le0,
 \tag{40}
\]
and \(f(t)=-J(t)-J(1/2-t)\). The positive Euler sine-product series proves this remainder. The stored \(\zeta(2k)\) intervals use positive partial sums and an integral tail; \(\pi\) uses the exact Machin identity with alternating arctangent tails. These are finite elementary enclosures, not floating-point tolerances.

The separate complete-flow certificate checks 108 original triangle rows, each with mass \(1/2\), all 54 ordinary column demands equal to one, and the two original protected loads zero. Its entropy interval is
\[
 67.688246275129\ \le E_{\mathrm{complete\ flow}}
                 \le\ 67.688246636527.
 \tag{41}
\]
This is a lower bound for the original complete maximum \(\Phi\); the upper endpoint in (41) is an upper bound for this feasible flow's entropy, not an upper bound for \(\Phi\). In particular \(\Phi>67.687\), which is all that (31) uses.

## 8. Coverage and limitations

The existing negative-axis note proves the exact exterior extraction, finite moment reduction, omitted-tail estimate, odd real stability, and factorwise Mahler loss. The effective-response note proves the local complex pressure packet and its Schur-complement response. The root-pressure note proves that this germ determines the full root measure and the exact common-variable negative-axis loss; its explicit low-order bounds use the Mahler loss, including the conductance and fourth-derivative improvements. The finite squared-factor estimate (5) adds a direct two-derivative lower bound on that common-variable loss. It does not require continuing a classical saddle through the negative axis or reconstructing the limiting density.

The full original-source coefficient has been grouped before taking modulus in (17). Thus this estimate is compatible with the separate exponential lower bound for the sum of absolute original-array terms: cancellation is retained here, whereas that termwise sum discards it. That particular array lower bound was established on even levels; the present signed estimate is on odd levels. No same-level conclusion is inferred by comparing those two parity-restricted statements.

The conclusion concerns one genuine singleton sector and one mixed spectral tuple. It gives no bound for multiple noncentral coupons, all real spectra, a complex filling contour, odd endpoint derivatives, or the even source. In particular the actual even central cofactor is not generally real stable. Its coefficientwise positive comparison with a stable reference does not control signed negative-axis values. The strict fixed-spectrum odd result therefore is not a full remainder theorem and does not prove a new knot-volume equality.

## Sources used in the proof

- [The original one-cap coefficient reduces to two negative-axis suprema](research_global_cap_negative_axis_and_mahler_bound.md), sections 1--4 and 6: the exact original extraction, finite cap completion, odd factorization, and strict omitted tail.
- [Effective boundary response and the original global cap variance](research_global_cap_effective_response_criterion.md), sections 1--3: strict exterior pressure, connected determinant packet, and the actual Schur response.
- [The classical boundary-pressure germ determines the cap root loss](research_cap_root_measure_from_classical_pressure.md), sections 2--7: prior root-measure, Mahler, and common-variable criteria; the present bound does not require its logarithmic-potential convergence theorem.
- [An exact positive moment form for the original flat-cap coefficients](research_flat_cap_positive_moment_form.md): the original finite moments through degree \(d\), with unbounded support retained.
- [The full numerator after localization: exact cross cofactors and the packet interface](actual_cross_cofactor_factorization.md), section 3, and [Finite local curvature of the original boundary models](actual_q_hahn_boundary_model_curvature.md): actual odd endpoint determinants and their finite curvature/holomorphic estimates.
- [The positive face coefficient has one global saddle](actual_positive_face_coefficient_saddle.md), sections 2--4: determinant angular contraction and the primitive finite coefficient Gaussian.
- [The geometric contribution and all Fourier charges](actual_morse_cross_filling_period.md) and [The original complement and its geometric contribution](actual_morse_geometric_contribution.md): original Morse source marking and complete action normalization; only the exact source and complete geometric action are used here.
- [The exact even CROSS endpoint is not real stable, and the remaining parity adapter](research_even_cross_stability_obstruction.md): the even-parity limitation.
- [A fixed source sector beyond the shared-radius envelope criterion](actual_singleton_sector_envelope_obstruction.md): the fixed 54-region incidence data and strict spectator table.
