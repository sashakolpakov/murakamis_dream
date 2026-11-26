# Exact contraction of the full high Newton radical

Research note, 3 November 2026. The entire nilpotent high-index sector
of the original edge kernel contracts to physical values with uniformly
bounded coefficients. At both ends of an edge these coefficients give
an explicit real positive-definite Gram matrix. Original crossing
phases remain in the physical color sum, so this is an exact grouping
and an upper bound, not a positivity assertion for the filled source.

The coefficient identity below is the signed form of the divided
differences already used in the
[original low-color bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_original_low_color_bound.md),
equations (5)--(6). Square-zero nilpotence is also recorded in the
[arbitrary-power compiler](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_arbitrary_power_source_compilation.md),
Proposition 2. The purpose here is their full high-index edge
contraction, including a uniform bound through the last double node.
This differs from the first-normal product-rule expansion in
[the grouped Ward-current note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_grouped_endpoint_current_matchings.md):
a radical insertion consumes the local normal and leaves only the
spectator's value.

## 1. The physical radical and its exact value functional

Let
\[
 N\ge3,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 \theta=\pi/N,\quad q=e^{i\theta},\quad \eta=(-1)^D,
 \tag{1}
\]
and use the full physical algebra and its original closing functional
\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\quad
 P_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
The original Newton data are
\[
 s_j=2\sin(j\theta),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,
 \qquad c_a=2\cos((2a+1)\theta),\quad
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z).
 \tag{3}
\]
The double nodes are \(c_a\), \(0\le a<m\). When \(N=2m+1\)
there is also the simple node \(c_m=-2\).

The radical, meaning the kernel of evaluation at every distinct
physical node, is exactly
\[
 \mathfrak r_N=\operatorname{span}
                  \{e_{D-r}:0\le r<m\},\qquad
                        \mathfrak r_N^2=0.
 \tag{4}
\]
Indeed each displayed polynomial contains every distinct root among
its factors. They are independent and their number is
\(N-\#\{\text{distinct roots}\}=m\). A product of two polynomials
vanishing at every root is divisible by \(P_N\), whose root
multiplicities are at most two. At odd levels \(e_m\) is deliberately
excluded: it does not vanish at the simple node \(-2\).

For \(0\le a\le r<m\) define
\[
 b_{ra}=(-1)^{r+a}
       \frac{s_{2a+1}S_r^2}{S_{r-a}S_{r+a+1}},
 \qquad b_{ra}=0\quad(a>r).
 \tag{5}
\]
All denominators are nonzero: \(r+a+1\le2m-1<N\).

**Theorem 1.** For every \(f\in\mathcal A_N\),
\[
                  \phi_N(e_{D-r}f)
                      =\sum_{a=0}^r b_{ra}f(c_a).
 \tag{6}
\]
For the original crossing \(R\), every signed integer \(n\), and
\(\kappa=\exp(\pi iD^2/(2N))\), this gives
\[
 \phi_N(R^n e_{D-r}f)
   =\sum_{a=0}^r b_{ra}\,\kappa^n(-1)^{na}q^{na(a+1)}f(c_a).
 \tag{7}
\]
These are coefficientwise identities with arbitrary ordinary
free-boundary polynomials as coefficients.

*Proof.* Write the canonical representative
\(f=\sum_{j=0}^D f_j e_j\). The original Frobenius pairing is
\(\phi_N(e_i e_j)=\delta_{i+j,D}\), so the left side of (6) is
\(f_r\). The first \(r+1\) nodes are distinct; ordinary Newton
interpolation gives
\[
 f_r=(-1)^rS_r^2\sum_{a=0}^r
                \frac{f(c_a)}{\prod_{0\le h\le r,\ h\ne a}(c_a-c_h)}.
 \tag{8}
\]
They decrease with \(a\), so the denominator has sign \((-1)^a\).
The difference-of-cosines product has absolute value
\(S_{r+a+1}S_{r-a}/s_{2a+1}\), proving (5)--(6).
Finally the actual crossing values are
\[
                  R(c_a)=\kappa(-1)^a q^{a(a+1)}.
 \tag{9}
\]
Evaluation is an algebra homomorphism and these values are nonzero,
so (9) applies to all signed powers, proving (7). \(\square\)

Formula (6) does not discard the original first normals. The local
physical residue at a double node is
\[
     \eta\{(4-c_a^2)h'(c_a)-c_a h(c_a)\}.
 \tag{10}
\]
For \(h=e_{D-r}f\), the value term and the derivative of \(f\)
vanish, and
\[
      \eta s_{2a+1}^2 e_{D-r}'(c_a)=b_{ra}
                \quad(a\le r),
 \tag{11}
\]
with zero derivative for \(a>r\). The odd simple-node value is zero.
Thus (6) is exactly the original surviving normal, expressed as an
evaluation functional. Ordinary derivatives in every uncontracted
free-boundary variable commute with this finite identity.

## 2. A uniform bound on the exact coefficients

**Theorem 2.** At every integer level and every \(0\le a\le r<m\),
\[
                    |b_{ra}|\le2,\qquad
                 \sum_{a=0}^{m-1}b_{ra}=\delta_{r0}.
 \tag{12}
\]
In particular, uniformly in the signed crossing power,
\[
 |\phi_N(R^n e_{D-r}f)|
       \le2\sum_{a=0}^r|f(c_a)|
       \le2(r+1)\max_{a\le r}|f(c_a)|.
 \tag{13}
\]

*Proof.* Factor the factorial quotient as
\[
 \frac{S_r^2}{S_{r-a}S_{r+a+1}}
   =\frac1{s_{r+a+1}}
                    \prod_{j=1}^a\frac{s_{r-j+1}}{s_{r+j}}
   \le\frac1{s_{r+a+1}}.
 \tag{14}
\]
Each factor is at most one, since
\[
 \sin((r+j)\theta)-\sin((r-j+1)\theta)
   =2\cos((r+\tfrac12)\theta)\sin((j-\tfrac12)\theta)>0.
 \tag{15}
\]
The restriction \(r<m\) is exactly what keeps the cosine positive.
Set \(x=(a+1/2)\theta\), \(y=(r+1/2)\theta\). Then
\(0<x\le y<\pi/2\), and
\[
 \frac{s_{2a+1}}{s_{r+a+1}}
    =\frac{\sin(2x)}{\sin(x+y)}\le2,
 \tag{16}
\]
because \(\sin(x+y)\ge\cos x\sin y\ge\cos x\sin x\).
Equations (14)--(16) prove the first bound in (12).
Putting \(f=1\) in (6) gives its row sum, since
\(\phi_N(e_{D-r})=\delta_{r0}\). Equation (9) has unit modulus,
even if the integer \(n\) depends on \(N\); this proves (13).
\(\square\)

## 3. The whole radical edge becomes a physical Gram matrix

Separate the exact ordinary kernel as
\[
 \begin{split}
 K_N(z,w)&=K_N^{\rm low}(z,w)+H_N^{\rm rad}(z,w),\\
 H_N^{\rm rad}(z,w)&=\sum_{r=0}^{m-1}e_{D-r}(z)e_{D-r}(w),\\
 K_N^{\rm low}(z,w)&=\sum_{j=0}^{D-m}e_j(z)e_j(w).
 \end{split}
 \tag{17}
\]
At even levels the radical sector is every index \(j\ge N/2\).
At odd levels it is \(j\ge(N+1)/2\); the middle polynomial stays
in the low sector.

Let \(\mathsf B=(b_{ra})_{0\le r,a<m}\), and set
\[
 W=\mathsf B^T\mathsf B,\qquad
 W_{ab}=\sum_{r=\max(a,b)}^{m-1}b_{ra}b_{rb}.
 \tag{18}
\]
Then for arbitrary original spectators \(f,g\) and signed powers
\(n,p\),
\[
 \boxed{\quad
 (\phi_N\otimes\phi_N)
   \bigl[R^n(z)R^p(w)H_N^{\rm rad}(z,w)f(z)g(w)\bigr]
   =\sum_{a,b=0}^{m-1}W_{ab}R(c_a)^nR(c_b)^p f(c_a)g(c_b).
 \quad}
 \tag{19}
\]
The same identity holds with \(f(z)g(w)\) replaced by any joint
spectator \(F(z,w;\mathbf u)\), by replacing its final product of
values with \(F(c_a,c_b;\mathbf u)\). No independence assumption
on outside variables is required.

**Theorem 3.** The matrix \(W\) is real symmetric positive definite,
and
\[
 \begin{split}
 |W_{ab}|&\le4m,\qquad
        \sum_{a,b}|W_{ab}|\le4m^3,\\
 \operatorname{sign}(W_{ab})&=(-1)^{a+b},\qquad
                         W\mathbf1=\mathbf e_0.
 \end{split}
 \tag{20}
\]
Consequently (19) is bounded in absolute value by
\(4m^3\max_{a,b}|F(c_a,c_b;\mathbf u)|\), uniformly over all
signed integer powers.

*Proof.* Apply (6) in each variable to prove (19).
The real triangular matrix \(\mathsf B\) has strictly positive
diagonal
\(b_{rr}=S_r^2/S_{2r}\), so it is invertible and its Gram matrix
is positive definite. The bounds follow from \(|b_{ra}|\le2\).
Every summand in (18) has sign \((-1)^{a+b}\), and at least one
is nonzero. Finally (12) says
\(\mathsf B\mathbf1=\mathbf e_0\), while the first row of
\(\mathsf B\) is \(\mathbf e_0^T\). Hence
\(W\mathbf1=\mathsf B^T\mathbf e_0=\mathbf e_0\).
\(\square\)

Conjugating \(W\) by \(\operatorname{diag}((-1)^a)\) makes every
entry positive. This does not make (19) positive: after that sign
change the original crossing still supplies the chirp
\(q^{na(a+1)}\), as well as \((-1)^{(n+1)a}\) and its fixed unit
\(\kappa^n\). Even when odd powers cancel the checkerboard signs,
the chirp generally remains. The formula preserves that coherent
sum exactly.

**Proposition 4.** This actual positive Gram matrix is exponentially
ill-conditioned as \(N\to\infty\):
\[
 \lambda_{\min}(W)\le
       \exp\{-2GN/\pi+O(\log N)\},\qquad
 \lambda_{\max}(W)\ge1,
 \tag{21}
\]
where \(G\) is Catalan's constant. In particular its condition
number is at least \(\exp\{2GN/\pi-O(\log N)\}\).

*Proof.* Choose \(r=\lfloor N/4\rfloor<m\). The diagonal entry
of \(\mathsf B^{-1}\) at \(r\) is \(1/b_{rr}\), so
\[
 \lambda_{\min}(W)=\sigma_{\min}(\mathsf B)^2
       =\|\mathsf B^{-1}\|_2^{-2}\le b_{rr}^2
       =\left(\frac{S_r^2}{S_{2r}}\right)^2.
 \tag{22}
\]
The uniform sine-factorial estimate
\(\log S_j=N\mathcal J(j/N)+O(\log N)\), together with
\(\mathcal J(1/4)=-G/(2\pi)\) and \(\mathcal J(1/2)=0\),
evaluates the last expression as
\(\exp\{-2GN/\pi+O(\log N)\}\). The values of these integrals
follow directly from the Fourier series for
\(\log(2\sin\pi x)\); see the
[original sine-factorial profile](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_three_crossing_full_coefficient_profile.md).
Finally \(W_{00}\ge b_{00}^2=1\), so the largest eigenvalue is
at least one. \(\square\)

Thus positive definiteness here supplies no uniform lower frame bound
in the ordinary physical-value Euclidean norm. It cannot be used as
an identity metric or as a spectral-gap lower bound for a specified
source coefficient.

All nilpotence assertions here concern the physical relation
\(P_N\). They are not assertions about a scalar-smoothed algebra
\(P_\sigma\ne P_N\). Likewise, two radical factors multiply to zero
at a contracted or canonically reduced vertex, but their ordinary
product need not vanish in an unreduced free-boundary variable.
The free-variable identities and their derivatives in (19) remain
literal polynomial identities without imposing such a reduction.

## 4. Grouping all radical edges in a coupled source

Let \(\Gamma=(V,E)\) be a fixed finite simple graph, and let
\(I\subseteq V\) be the vertices at which the original trace is
taken. Each such vertex has a signed crossing power \(n_v\).
The variables at the other vertices remain ordinary boundary
variables. Put
\[
 E_I=\{\{v,w\}\in E:v,w\in I\},\qquad
 Z_K=\left(\prod_{v\in I}\phi_N^{(z_v)}\right)
       \left[\prod_{v\in I}R(z_v)^{n_v}
                    \prod_{\{v,w\}\in E}K_N(z_v,z_w)\right].
 \tag{23}
\]
Define \(Z_{\rm low}\) by replacing \(K_N\) with
\(K_N^{\rm low}\) only on the edges in \(E_I\). Every edge
incident to an uncontracted boundary keeps its original full
kernel. Thus the nilpotence in (4) will only be used at a vertex
where the original algebra relation is imposed.

A matching \(M\subseteq E_I\) is a set of edges with no shared
endpoint. Write \(S=V(M)\) for its set of endpoints. For a choice
of physical colors \(\mathbf a=(a_v)_{v\in S}\), with
\(0\le a_v<m\), set
\[
 C_S(\mathbf a)=
 \left(\prod_{v\in I\setminus S}\phi_N^{(z_v)}\right)
 \left[
   \prod_{v\in I\setminus S}R(z_v)^{n_v}
   \left.\prod_{\{v,w\}\in E}K_N(z_v,z_w)
                           \right|_{z_v=c_{a_v}\ (v\in S)}
 \right].
 \tag{24}
\]
In particular \(C_\varnothing=Z_K\). This is the original source
with the vertices in \(S\) evaluated at physical colors, and with
their crossing scalars kept outside the definition. All edges are
still present. An edge crossing from \(S\) to its complement has
factor \(K_N(c_{a_v},z_w)\); an edge within \(S\) has factor
\(K_N(c_{a_v},c_{a_w})\).

**Theorem 5.** The exact difference between the full and low sources is
\[
 \begin{split}
 Z_K-Z_{\rm low}
   =\sum_{\substack{M\subseteq E_I\ {\rm matching}\\M\ne\varnothing}}
        (-1)^{|M|+1}\sum_{\mathbf a}
       \left[\prod_{\{v,w\}\in M}
          \frac{W_{a_va_w}}{K_N(c_{a_v},c_{a_w})}\right]
       \left[\prod_{v\in V(M)}R(c_{a_v})^{n_v}\right]
                          C_{V(M)}(\mathbf a).
 \end{split}
 \tag{25}
\]
Each matching contribution has the bound
\[
 \left|\sum_{\mathbf a}
       \left[\prod_{\{v,w\}\in M}
          \frac{W_{a_va_w}}{K_N(c_{a_v},c_{a_w})}\right]
       \left[\prod_{v\in V(M)}R(c_{a_v})^{n_v}\right]
                          C_{V(M)}(\mathbf a)\right|
 \le (4m^3)^{|M|}
                       \max_{\mathbf a}|C_{V(M)}(\mathbf a)|.
 \tag{26}
\]
These statements hold at both level parities, with arbitrary
boundary variables and all their fixed ordinary derivatives retained.

*Proof.* Expand \(K_N^{\rm low}=K_N-H_N^{\rm rad}\) on the
edges in \(E_I\). If two chosen radical edges meet at a vertex,
every resulting term contains a product of two elements of
\(\mathfrak r_N\) there. Its original trace is zero by (4).
The only surviving subsets are therefore matchings.

For a matching, apply (19) at its disjoint pairs of endpoints.
The joint-spectator version of that identity is needed here:
edges not in the matching may connect different pairs or meet
the same remaining vertex. They all become their literal
physical evaluations. In particular they are not removed.
The factors on the matching edges themselves have been replaced
by \(W\). Restoring their original \(K_N\) factors in order to
use (24) accounts for the divisions in (25).

These divisions are harmless. At a physical node \(c_a\),
\[
 e_j(c_a)>0\quad(0\le j\le a),\qquad
 e_j(c_a)=0\quad(j>a),
 \qquad K_N(c_a,c_b)\ge1.
 \tag{27}
\]
The first statement follows because the first \(a+1\) distinct
nodes decrease; the second follows from the factor \(c_a-z\)
in every later Newton polynomial. The constant term \(e_0=1\)
then proves the last inequality. Finally use
\(|R(c_a)^{n_v}|=1\), \(|W_{ab}|\le4m\), and the
\(m^{2|M|}\) possible color assignments to prove (26).
All operations are finite and in selected variables, so boundary
derivatives commute with the identity. \(\square\)

For a fixed graph, the prefactors and the number of matchings in
(26) have no exponential growth in \(N\). Consequently, if one
independently proves
\[
 \max_{\mathbf a}|C_{V(M)}(\mathbf a)|
           \le \exp\{N\mu_M+o(N)\}
 \tag{28}
\]
for every nonempty matching, then
\[
 |Z_K-Z_{\rm low}|
      \le \exp\{N\max_{M\ne\varnothing}\mu_M+o(N)\}.
 \tag{29}
\]
If the low source has a nonzero leading term of rate \(\mu\),
and all these \(\mu_M\) are strictly smaller than \(\mu\),
the full source has that same leading term. This implication
is just the reverse triangle inequality after (29).
Neither the needed bound (28) nor the required strict comparison
is supplied by the matching formula.

This is the relevance to the
[power-three kernel obstruction](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_bare_kernel_power_three_obstruction.md).
The high sector can be exponentially large at an off-grid complex
geometric point before contraction. Its exact contribution after
contraction is instead bounded by physical-color sources at
polynomial cost. The next analytic estimate therefore concerns
those sources, with their remaining traces and edge couplings.
The [all-color normal bound](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_all_color_path_normal_bound.md)
controls the first-normal determinant at each color, but explicitly
leaves the coherent color sum unestimated. A positive local Gram
matrix cannot replace that missing estimate.

For odd powers on the matched vertices, the signs
\((-1)^{a_v+a_w}\) in \(W\) cancel the crossing signs.
Their matching weights become positive magnitudes times
\[
       \kappa^{\sum_{v\in V(M)}n_v}
           q^{\sum_{v\in V(M)}n_v a_v(a_v+1)}.
 \tag{30}
\]
The displayed quadratic phases and the phases of \(C_S\) remain.
For reflected conjugate data a Gram pairing can give a squared
norm, but a general matching contribution is a bilinear sum,
not a Hermitian quadratic form.

## 5. The single top mode and why removing it is insufficient

The special term \(e_D(z)e_D(w)\) has an especially simple
interpretation. Equations (6) and (9) at \(r=0\) give
\[
 \phi_N(R^n e_D f)=\kappa^n f(c_0),\qquad
                         K_N(c_0,w)=1.
 \tag{31}
\]
The first identity already appears in
[the free-boundary crossing identity](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_current_free_aw_crossing_transport.md).
Let \(Z^\circ_\Gamma\) use
\(K_N-e_D\otimes e_D\) on its selected--selected edges
and the original kernel elsewhere. Expansion as above now gives
\[
 Z_\Gamma=
   \sum_{M\subseteq E_I\ {\rm matching}}
      \kappa^{\sum_{v\in V(M)}n_v}
                         Z^\circ_{\Gamma\setminus V(M)}.
 \tag{32}
\]
Here the graph on the right loses the matched vertices and
every edge incident to them, since all those edges evaluate
to one. An isolated surviving selected vertex still carries
its original factor \(\phi_N(R^{n_v})\). The deletion in
(32) is an algebraic contraction, not an asserted topological
move on the knot complement.

This deletion rule is special to the single top mode.
For the full radical, the physical evaluations in (24)
must remain. Moreover, at the power-three point in the linked
obstruction theorem, the next term
\(e_{D-1}(z)e_{D-1}(w)\) differs from the top by a factor
of order \(N^{-4}\), and has the same exponential rate.
Removing any fixed number of top terms therefore does not
restore the bare geometric expansion. The full radical
contraction in (25) addresses the entire sector instead.

## 6. Finite-level checks

The proofs above are for all integer levels. The separate script
[check_high_newton_radical_contraction.py](../experiments/check_high_newton_radical_contraction.py)
also checks the normalization by direct polynomial division:

    python3 experiments/check_high_newton_radical_contraction.py

It checks the trace on every monomial basis element at levels
3 through 14, the square-zero products, and the coefficient
bound. Direct Laurent expansion also checks the Fourier bound
in Section 7 on every radical basis element at those levels.
At levels 3 through 8 it compares a four-vertex path
contraction with the physical-evaluation matching expansion,
using complex polynomial vertex weights and retaining the edge
between two disjoint matched pairs. The
[saved numerical diagnostics](../repro/results/research-high-newton-radical.json)
record 100-digit arithmetic and the residuals. These finite checks
test the formulas; they do not replace the uniform arguments.

## 7. Fourier bounds for the original radical polynomials

There is also a direct Fourier estimate before contraction.
It uses the same exact physical normals as (11), rather than
a replacement interpolant or a general polynomial derivative
inequality. For \(0\le r<m\), write
\[
 h_r(t)=e_{D-r}(-2\cos t)
            =\sum_{j=-D}^{D}\widehat h_r(j)e^{-ijt},
 \qquad
 \|\widehat h_r\|_1=\sum_j|\widehat h_r(j)|.
 \tag{33}
\]

**Theorem 6.** Uniformly over the whole radical basis,
\[
 \|\widehat h_r\|_1
       \le\frac{2\sqrt{N-1}}{N\sin(\pi/N)}
       \le\sqrt{N-1}.
 \tag{34}
\]
Consequently, for every integer \(k\ge0\),
\[
 \sup_{t\in\mathbb R}|\partial_t^k h_r(t)|
                       \le D^k\sqrt{N-1}.
 \tag{35}
\]
In angular variables set
\(\widehat H_N^{\rm rad}(t,u)
 =H_N^{\rm rad}(-2\cos t,-2\cos u)\).
For all integers \(k,\ell\ge0\) and all complex \(t,u\),
\[
 |\partial_t^k\partial_u^\ell\widehat H_N^{\rm rad}(t,u)|
 \le m(N-1)D^{k+\ell}
                      e^{D(|\Im t|+|\Im u|)}.
 \tag{36}
\]
In particular its real-period derivatives have polynomial bounds.

**Proof.** Put \(z=e^{-it}\) and
\[
 P_r(z)=z^Dh_r(t).
\]
This is an ordinary polynomial of degree at most \(2D\).
At the physical angles
\(t_j=\pi(N-1-2j)/N\), the numbers \(z_j=e^{-it_j}\)
are the \(N\) distinct roots of \(z^N=\eta\).
Every radical polynomial vanishes at every physical spectral
node, including the odd simple node. Hence
\[
                  P_r(z)=(z^N-\eta)g_r(z),\qquad
                           \deg g_r\le N-2.
 \tag{37}
\]
Differentiating along the angular variable at a grid point gives
\[
 z_j^D h_r'(t_j)=-iN\eta\,g_r(z_j),\qquad
                     |g_r(z_j)|=\frac{|h_r'(t_j)|}{N}.
 \tag{38}
\]

For a double node \(c_a\), set \(\vartheta_a=(2a+1)\theta\).
At its two angular preimages, the chain rule and (11) give
\[
 |h_r'(t_j)|
     =\frac{|b_{ra}|}{2\sin\vartheta_a}
     \le\frac1{\sin\theta}.
 \tag{39}
\]
Here \(b_{ra}=0\) for \(a>r\). All double-node angles lie
between \(\theta\) and \(\pi-\theta\), so their sines are
at least \(\sin\theta\). At the odd simple node the angular
point is \(t=0\), and \(h_r'(0)=0\) by the chain rule.
Thus (39) bounds every value in (38).

Write \(g_r(z)=\sum_{a=0}^{N-2}d_a z^a\).
The orthogonality of the \(N\) equally spaced physical points
gives the exact discrete Parseval identity
\[
 \sum_{a=0}^{N-2}|d_a|^2
       =\frac1N\sum_{j=0}^{N-1}|g_r(z_j)|^2
       \le\frac1{N^2\sin^2\theta}.
 \tag{40}
\]
For completeness, a cross term with distinct frequencies
\(a,b\) contains \(N^{-1}\sum_jz_j^{a-b}=0\), because
\(0<|a-b|<N\); diagonal terms have average one.
Cauchy--Schwarz therefore bounds
\(\sum_a|d_a|\le\sqrt{N-1}/(N\sin\theta)\).
Multiplication by \(z^N-\eta\) in (37) at most doubles
the coefficient norm, and multiplication by \(z^{-D}\)
only shifts its frequencies. This proves the first bound
in (34). Concavity of sine on \([0,\pi/2]\) gives
\(\sin(\pi/N)\ge2/N\), proving the second.

Each differentiation of (33) multiplies its coefficients by
a frequency of magnitude at most \(D\). On a complex line,
each exponential has modulus at most \(e^{D|\Im t|}\).
This proves (35) and its corresponding complex-line bound.
Finally
\(\widehat H_N^{\rm rad}(t,u)=\sum_{r=0}^{m-1}h_r(t)h_r(u)\).
Apply the single-factor bounds to this finite sum to obtain
(36). \(\square\)

The normalization in (39) uses the actual surviving spectral
normal. Thus the Fourier estimate includes both parities and
does not discard derivative data. It explains the distinction
between the real physical estimates and the complex obstruction:
the radical is polynomially bounded on the entire real period,
but (36) allows exponential growth at a fixed nonzero height.
No polynomial bound on a fixed complex strip, or lower bound
for a coherent traced source, follows from (34).
