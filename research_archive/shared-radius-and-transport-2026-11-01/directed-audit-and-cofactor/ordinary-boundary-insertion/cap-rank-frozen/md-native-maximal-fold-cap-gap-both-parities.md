# The protected cap bound at the actual maximal folded nodes, at both parities

The odd-level restriction in the existing protected-cap application comes from placing every neighboring central spectrum at the fixed number \(-2\). At even levels that number is not a physical spectral node. This note instead keeps each neighbor at its actual maximal folded node. The resulting exterior is stable at both parities, and its common coefficient saddle has the same classical pressure, response and tilted upper bounds. Consequently the existing whole-real-interval cap estimate extends to all sufficiently large levels for this specified source slice.

This does not fill the neighboring regions or vary their spectra. In particular it does not control their first normals, the whole spectral cube, multiple noncentral regions, or the full knot invariant.

## 1. Exact original polynomial and parity

Fix the same simple matched-sphere Morse diagram, original MAIN mark, protected vertices, and protected left region with ordered quartet \((C,0,A,0)\). Put
\[
 d=N-1,\qquad J=\lfloor d/2\rfloor,\qquad e=d-2J\in\{0,1\},
 \qquad M=\lfloor N/2\rfloor-1,\qquad\theta=\pi/N.
 \tag{1}
\]
The indices \(J\) and \(M\) have different functions: \(J\) is the maximal folded channel and \(M\) is the literal protected-left cutoff. They agree at even levels; at odd levels \(M=J-1\).

The actual maximal spectral value is
\[
 c_N^*=2\cos((2J+1)\theta)
   =\begin{cases}-2,&N\text{ odd},\\-2\cos\theta,&N\text{ even}.
     \end{cases}\tag{2}
\]
At each other original region, the complete-node/full-resolvent identity gives, after removing only its fixed raw sign \((-1)^d\),
\[
 B_{N,*}(x,b,c,y)=N^2\beta_J^2
      \Delta_J(x,b,y)\Delta_J(x,c,y)P_e(x,y),
 \qquad P_0=1,\quad P_1=x+y.
 \tag{3}
\]
Here
\[
 \Delta_J(x,b,y)=\det\left(bI_J+\frac x2H_-^{[J]}+
                                      \frac y2H_+^{[J]}\right),
 \quad S_k=\prod_{r=1}^k2\sin(r\theta),\quad
 \beta_J=S_{2J}/S_J^2.\tag{4}
\]
The matrices are the original positive Hermitian matrices at level \(N\), not matrices at a smaller level. At odd levels \(\beta_J=1\). At even levels \(S_J^2=N/2\), \(S_{2J}=N/(2\sin\theta)\), and \(\beta_J=1/\sin\theta\). In particular every scalar in (3) is polynomial in \(N\).

One can check the even factor without a limiting argument. The exact even central cut is
\[
 s_{J+1}^2(x+y)R_J(b;u)R_J(c;u)
 +s_{J+1}s_Jxy(a_J+u)
       [R_J(b;u)R_{J-1}(c;u)+R_{J-1}(b;u)R_J(c;u)].\tag{5}
\]
At \(u=-a_J\), its second term is zero and \(s_{J+1}=2\). Since \(R_J(b;-a_J)=S_{2J}\Delta_J(x,b,y)\), (5) becomes exactly (3). The neighboring values, rather than neighboring first normals, are being used here.

Let \(I\) be the ordinary faces other than \(A,C\). The unchanged exterior is
\[
 P_N^*(A,C)=
 \left[\prod_{f\in I}L_f^d\right]
    \prod_{q\ne q_*}B_{N,*}(L_{x_q},L_{b_q},L_{c_q},L_{y_q})
   =\sum_{j=0}^{d}p_{N,j}^*A^jC^{d-j}.\tag{6}
\]
Protected variables are zero before extraction. Each factor has degree \(2J+e=d\), so the residual degree is exactly \(d\). No new target is introduced by \(P_1\), and no old target is decreased to absorb it.

Each determinant in (3) is stable with nonnegative coefficients; so is \(x+y\). Products, identifications of shared variables, coefficient extraction, and protected specializations preserve stability or give zero. Hence every nonzero \(P_N^*\) is a nonnegative stable homogeneous binary polynomial of degree \(d\).

There is no hidden vanishing parity factor for the intended simple-sphere MAIN mark. The two protected vertices are the endpoints of a nonmatching edge. If a matching edge had both protected endpoints, simplicity would identify it with that same edge, a contradiction. Therefore at least one outer argument in each spectator \(x+y\) is positive at a positive ordinary-weight assignment. If a more general source does have an identically zero factor, its exterior and the cap source are zero, and the upper bound is trivial; it cannot be used to assert a nonzero pressure packet.

## 2. The same common coefficient pressure at both parities

Assume the original exterior has a strict positive feasible half-load table at \(A=C=1\), with every \(I\)-load equal to one, and its supported ordinary pair graph is connected. These are the same assumptions used in the existing odd pressure theorem; they are verified for the recorded 54-region source.

For \(A=e^z,C=1,L_f=e^{w_f}\), let
\[
 \mathcal F(z,w)=\sum_{t\text{ exterior}}Q_t(L)-\sum_{f\in I}w_f,
 \qquad F(z)=\mathcal F(z,w(z)),\quad
 \partial_w\mathcal F(z,w(z))=0.\tag{7}
\]
The triangles and targets are the original ones. The half-triangle potential is
\[
 Q_t(L)=\max_{\substack{\alpha_f\ge0\\\sum_f\alpha_f=1/2}}
       \sum_f\{f(\alpha_f)+\alpha_f\log L_f\},\qquad
 f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}\pi,
 \quad \Lambda(t)=-\int_0^t\log|2\sin v|\,dv.\tag{8}
\]
Protected-zero loads are zero. The strict table and connected pair graph give coercivity in \(w\) and a positive-definite grounded Hessian. Thus the finite stationary point at zero is unique, and \(w(z)\) is holomorphic for small \(z\).

Define the exact finite potential using (3), not an even comparator:
\[
 \mathcal F_N(z,w)=\frac1N\log\prod_{q\ne q_*}B_{N,*}(L)
                         -\frac dN\sum_{f\in I}w_f.\tag{9}
\]
On a fixed complex neighborhood of the positive stationary weights, the normalized logarithms and all fixed derivatives converge to (7), along the full sequence of levels. Here are the inputs and the parity bookkeeping.

1. The determinant angle-force and absolute positive triangle normalization apply to every actual channel approaching the fold, including \(J=(N-1)/2\) and \(J=N/2-1\). The normalized determinant log therefore has limit \(Q_t\). The finite positive curvature theorem gives a common complex neighborhood with every fixed positive-order log derivative bounded by \(O(N)\). Cauchy estimates applied to the normalized holomorphic logs upgrade their locally uniform limit to convergence of all fixed derivatives. There is no differentiation of a merely pointwise coefficient rate.
2. The number of factors \(P_e\) is fixed by the diagram. Each even factor has a nonzero positive value and a holomorphic logarithm on that neighborhood; its fixed log derivatives are \(O(1)\). Thus its contribution to (9) and all normalized derivatives is \(O(N^{-1})\). The original degree change it compensates remains in (6).
3. The factors \(N^2\beta_J^2\) are independent of the faces, contribute \(O(\log N/N)\) in (9), and no log derivative. The target difference \(d/N-1\) contributes only a linear \(O(N^{-1})\) term.

The preconditioned implicit-function theorem consequently supplies finite stationary points \(w_N(z)\) on one common smaller complex disk, tending to \(w(z)\), with a uniformly invertible normalized Hessian.

The original \(|I|\)-torus coefficient integral has only one angular maximum. Indeed determinant contraction controls the primitive phase differences on the connected supported pair graph, with a lower bound proportional to \(N\). Both \(A,C\) are fixed at zero phase. Hence every extracted phase is forced to zero, with no additional lattice coset. The nonnegative even factors \(x+y\) have modulus ratio at most one and cannot weaken this bound. On compact weights the same bulk pair traces work through both maximal parities.

The local contour can therefore be shifted to \(w_N(z)\) for fixed small complex \(z\); the old angular complement and connectors retain a fixed gap. Taylor expansion with the uniform higher derivative bounds gives the actual relative coefficient estimate
\[
 P_N^*(e^z,1)=
 \frac{\exp(NF_N(z))}
 {(2\pi N)^{|I|/2}\sqrt{\det H_{N,II}(z)}}
       (1+O(N^{-1})),\quad
 F_N(z)=\mathcal F_N(z,w_N(z)).\tag{10}
\]
Here \(H_{N,II}=\partial_w^2\mathcal F_N\), and the square root continues from its positive real value. The zero-dimensional case uses the empty determinant one. Equation (10) is uniform and relative on a fixed complex disk; its leading factor is nonzero. Consequently
\[
 \frac1N\log P_N^*(e^z,1)\longrightarrow F(z),\qquad
 \nu_N:=\frac{\partial_z\log P_N^*(e^z,1)|_0}{d}\to\nu=F'(0),
 \quad
 \kappa_N:=\frac{\partial_z^2\log P_N^*(e^z,1)|_0}{d}\to\kappa=F''(0).
 \tag{11}
\]
This proves the required same-pressure statement, including nonvanishing at all sufficiently large levels. It does not compare even and odd coefficients term by term or infer equality of asymptotics from a finite sample.

## 3. Tilted and cutoff bounds retain the original targets

For every fixed positive trial vector with \(A=T,C=1\), positivity gives
\[
 \limsup_N\frac1N\log\frac{P_N^*(T,1)}{T^{d/2}}
 \le \sum_{t\text{ exterior}}Q_t(L)-\sum_{f\in I}\log L_f
                                  -\tfrac12\log T.\tag{12}
\]
The right side is exactly the earlier classical trial-pressure expression. This upper bound needs no remote stationary point at \(T\), and the parity factor and source scalar have zero normalized logarithmic cost.

Let \(R(s)\) be the original residual complete-triangle capacity for boundary loads \(A:s,C:1-s\) and all \(I\)-loads one. The complete strict optimizer gives
\[
 \max_{1/2\le s\le1}R(s)\le\Phi-\gamma_D,
 \qquad \gamma_D>0,\tag{13}
\]
where \(2\pi\Phi\) is the original augmented volume. This is the same closed entropy problem; it has no level parity. The coefficient upper follows at either parity directly from positive Cauchy bounds and compact entropy duality:
\[
 \limsup_N\frac1N\log p_{N,j_N}^*\le R(s)
                    \quad\text{if }j_N/d\to s.\tag{14}
\]
One may first use any finite positive trial vector, then take the infimum. The compact supported triangle entropy supplies its closed concave dual, including boundary loads; no coefficient lower asymptotic is needed. In particular \(M/d\to1/2\), so
\[
 \limsup_N N^{-1}\log p_{N,M}^*\le\Phi-\gamma_D.\tag{15}
\]
The exact one-step difference between the two parity cutoffs is retained before this limit.

## 4. All-level protected spectral bound and the recorded example

The original protected functional is
\[
 S_N^*(\sigma)=\sum_{j=0}^{M}v_{N,j}(\sigma)p_{N,j}^*,\qquad
 v_{N,j}(\sigma)=(-1)^jS_j^2\prod_{r=j+1}^{d}(\sigma-c_r),
 \quad c_r=2\cos((2r+1)\theta).\tag{16}
\]
It retains every original unused-row factor and both remaining degree targets. The common raw signs removed in (3) multiply (16) by one unit scalar and do not alter its modulus.

The finite sine-Cauchy and alternating-section theorem already applies to both parities. Its cutoff has \(2M=N-2\) at even levels and \(2M=N-3\) at odd levels, and its last Gram diagonal is respectively \(1\) and \((2\cos\theta)^{-1}\le1\). Thus no missing full-square moment is used. For the stable factorization of (6), put
\[
 a=1-\nu-\kappa,\qquad b=\nu-\kappa,\qquad
 R_T=\max\{a,b,1-4\kappa,a/T+bT-2\kappa\}.\tag{17}
\]
Combining its exact finite estimate with (11), (12), and (15) gives
\[
 \limsup_{N\to\infty}\frac1N\log
       \sup_{\sigma\in[-2,2]}|S_N^*(\sigma)|
 \le\max\{F(0)+\tfrac12\log R_T,\ F_T,\ \Phi-\gamma_D\},\tag{18}
\]
where \(F_T\) is any certified upper bound in (12). All level parities now enter the limsup. The finite spectral theorem is unchanged; the new input is the actual even maximal-fold exterior and its pressure proof above.

For the unchanged 54-region source, the selected region is 32, its quartet is \((0,50,16,29)\), the protected faces are 29 and 50, and \(A=L_{16},C=L_0\). The existing rational response and trial-vector certificates give
\[
 F(0)\le67.894,\quad .27\le\nu\le.275,\quad
 \kappa\ge.088,\quad\Phi\ge67.687,\quad
 T=17/5,\quad F_T<67.684.\tag{19}
\]
These are classical finite certificates, unchanged by parity. Exact rational arithmetic gives \(a-Tb\ge3/2500\) and \(R_T\le81/125\). The already certified logarithmic inequality \(-\tfrac12\log(81/125)>.216\) gives
\[
 \boxed{\quad
 \limsup_{N\to\infty}\frac1N\log
     \sup_{\sigma\in[-2,2]}|S_N^*(\sigma)|
       \le\Phi-\min\{.003,\gamma_D\}<\Phi.
 \quad}\tag{20}
\]
Every smaller fixed gap holds eventually. No explicit numerical value for \(\gamma_D\) is asserted. The theorem concerns the same original singleton sector and actual common extraction. Its neighboring spectral values are \(c_N^*\), not \(-2\) at even levels.

Since (16) has spectral degree at most \(d\), its first cap derivative has the same exponential rate by the elementary polynomial derivative bound. The original one-variable full-Hermite insertion of any fixed signed power also preserves this gap by its finite norm. These statements apply only to the selected cap variable; neighboring spectral derivatives and neighboring filling operations are not covered.

## 5. Dependencies and remaining application

The source scalar and central/full equality at physical nodes are in `actual_cross_cofactor_factorization.md` section 3 and `actual_complete_circle_positive_face_polynomial.md`. The local finite curvature, zero-free log neighborhoods and bulk pair traces include both maximal parities in `actual_q_hahn_boundary_model_curvature.md`. The action and angle-force normalization are in `actual_original_boundary_stationary_character.md`; the original coefficient contour and primitive angular gap are in `actual_positive_face_coefficient_saddle.md`. The exterior variant repeats their finite connected-graph argument as in `research_global_cap_effective_response_criterion.md`, now with the retained even factor. The existing exact finite cap theorem is `research_cap_uniform_spectral_gap.md`. Its old odd-only application is extended here only along the specified physical-node slice.

The result does not show that positive stable atom masses at neighboring first normals have sufficiently small rank. The separate nodal stable-jet theorem has polynomial total mass but includes ranks of order \(N\). A quantitative comparison for that rank distribution after the same face extraction remains necessary before applying any neighboring-spectrum or full-period conclusion.
