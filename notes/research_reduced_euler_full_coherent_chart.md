# A full finite Euler-star coherent chart through the lower row

Private written proof, 18 November 2026.

The actual all-factorial-gauge kernel of a reduced Euler star,
including the recipient sums, has a nonzero analytic amplitude
on a fixed open coherent chart through its lower donor row.
The proof sums integer occupations exactly. Its auxiliary
infinite exponential generating function has an explicitly
controlled connected-graph logarithm; count-marker integrals
then restore every finite capacity with exponentially small
relative error. The principal graph is the literal resolved
star correspondence.

The recipient products must lie in the finite-cap chart
specified below. This does not put an arbitrary geometric
point in that chart, and it does not establish a contribution
to a closed source period. Quantum-parameter normals are not
claimed. The complete proof directs are W, D, B and G, pinned
at the end.

## 1. Exact particles and exact finite capacities

Fix the number of heads \(r\ge2\). Put
\[
 d=N-1,\quad h=\mathfrak c/N,\quad \mathfrak c=2\pi i,\quad
 Q=e^h,\quad q=e^{h/2},\quad x=-M/q,\quad
 \mathcal G=G_F^{\otimes r},\quad
 G_Fw_a=(Q;Q)_a w_a .
 \tag{1}
\]
The common meridian \(M\) stays in a compact subset of
\(\mathbb C^*\), with a slightly larger compact neighborhood
when derivatives are used. Use B's exact scaled kernel
\[
 \mathcal K_N^\pm(z,w)
 =\sum_{a,b\in\{0,\ldots,d\}^r}
       z^a(\mathcal G^{-1}S_r^{\pm1}\mathcal G)_{ab}
                         \frac{(Nw)^b}{b!}.
 \tag{2}
\]
All interfaces are still the literal \(G_F\) interfaces.
There is no quadratic chirp in this formula.

Introduce donor types \(D_1,\ldots,D_r\) and recipient
types \(R_2,\ldots,R_r\). Their activities are
\[
 u_1=w_1z_1,\qquad
 u_j^\pm=(\pm1)x^{-(j-1)}w_1z_j\quad(j\ge2),\qquad
 v_i=z_iw_i\quad(i\ge2).
 \tag{3}
\]
Here the upper sign is positive and the lower sign negative;
\(u_1\) has the same sign for both kernels. For an ordered
pair of particle positions, the pair energy is
\[
 \begin{split}
 B_+(D_j,D_k)&=\mathbf1_{j>k},\\
 B_-(D_j,D_k)&=\mathbf1_{j>k}
                         +\mathbf1_{j\ge2,\ k\ge2},\\
 B_\pm(D_j,R_i)=B_\pm(R_i,D_j)&=\mathbf1_{2\le i<j},\\
 B_\pm(R_i,R_j)&=0 .
 \end{split}
 \tag{4}
\]
Donor--donor energies retain the order of their positions.
They have not been symmetrized.

For arbitrary activities \(\mathbf a=(u,v)\), define
\[
 Z_N^\pm(\mathbf a)=
 \sum_{s\ge0}\frac{N^s}{s!}
 \sum_{\ell_1,\ldots,\ell_s}
       \prod_{\nu=1}^s a_{\ell_\nu}
       \exp\left(h\sum_{\nu<\mu}B_\pm(\ell_\nu,\ell_\mu)\right).
 \tag{5}
\]
On the physical imaginary ray this is entire in all activities:
the absolute sum is at most
\(\exp(N\sum_\ell|a_\ell|)\).
This extension is an auxiliary generating function, not an
enlarged physical head.

In each word let \(a\) be its number of donor particles,
\(n_j\) its number of \(D_j\)'s for \(j\ge2\), and \(b_i\)
its number of \(R_i\)'s. Then the exact finite kernel (2)
is the part of (5) satisfying
\[
                   a<N,\qquad b_i+n_i<N\quad(2\le i\le r).
 \tag{6}
\]
To check this, fix the ordered donor subword and the recipient
counts. There are \(s!/(a!\prod b_i!)\) interleavings.
The donor energy is W's literal word energy. The other
energy is exactly \(\sum_jn_j\sum_{i<j}b_i\), giving the
original prefix Cartan factors. Thus (5) has coefficient
\(N^{a+\sum b_i}/(a!\prod b_i!)\), the dual in (2).
W's word identity recovers the finite Gaussian multinomial
when \(a<N\). Conditions (6) are precisely its donor and
recipient masks. Donor occupation decreases and recipient
occupations increase, so these also retain all intermediate
star masks.

Equivalently introduce count markers \(\xi_0,\xi_2,\ldots,\xi_r\):
\[
 u_1\mapsto\xi_0u_1,\qquad
 u_j\mapsto\xi_0\xi_ju_j,\qquad
 v_j\mapsto\xi_jv_j .
 \tag{7}
\]
Apply the coefficient projections of degrees \(0,\ldots,d\)
in each marker, then evaluate every marker at one.
This is an exact formula for (2), including all \(E_d\)
caps of B. No upper projector has yet been approximated.

## 2. Connected graphs with bounded recipient activity

Write \(t=|\mathfrak c|=2\pi\),
\[
                  U=\sum_j|u_j|,\qquad V=\sum_i|v_i|.
 \tag{8}
\]
For each fixed bound \(V\le V_*\), there is \(U_*>0\)
such that all estimates below hold for \(U<U_*\).
In particular recipient activities need not have a small sum.

Here are the combinatorial estimates used to prove this.
For a fixed type word expand each pair as
\(e^{hB}=1+(e^{hB}-1)\), and group the resulting graphs
by connected components. Increasing relabeling of a component
preserves its ordered pair energies. Consequently the weight
of a component depends only on its size after its types have
been summed. The exponential formula follows directly by
partitioning the labelled vertex set into its components.

We use D's elementary breadth-first interval partition.
Root a connected graph at vertex \(1\), take its distance
levels, and choose the smallest-labelled preceding neighbor
as parent. For the resulting tree \(T\), its permitted
additional edges \(R(T)\setminus T\) are the same-level
edges and the adjacent-level edges whose preceding endpoint
is no smaller than the chosen parent. The graphs with this
tree are exactly the interval \([T,R(T)]\): adding these
edges changes neither distances nor the selected parents,
and every connected graph lies in its own such interval.
It follows exactly that its connected sum is
\[
 \sum_T\prod_{e\in T}(e^{hB_e}-1)
                  \prod_{e\in R(T)\setminus T}e^{hB_e}.
 \tag{9}
\]
This proof uses ordered \(B_e\)'s throughout.

Put \(e^{hB}-1=hB\int_0^1e^{hB\theta}\,d\theta\).
The connected \(s\)-vertex weight is therefore
\[
 h^{s-1}\sum_{\ell,T}\prod_\nu a_{\ell_\nu}
       \prod_{e\in T}B_e
       \int_{[0,1]^{s-1}}e^{h E_T(\theta)}\,d\theta,
 \quad
 E_T=\sum_{e\in T}B_e\theta_e+
                   \sum_{e\in R(T)\setminus T}B_e .
 \tag{10}
\]
The real energy satisfies \(0\le E_T\le s(s-1)\).
Thus on the physical ray the integral has modulus at most
one, and
\[
 |e^{hE_T}-1-hE_T|\le \tfrac12|h|^2s^4.
 \tag{11}
\]
No factor \(e^{Cs^2/N}\) occurs.

For completeness the needed tree-series convergence has
a direct majorant. Replace donor--donor edge weights by
two, donor--recipient weights by one, and recipient--recipient
weights by zero. Let \(T_D,T_R\) be the sums of rooted
labelled trees whose root has the indicated type, with
edge parameter \(t\), donor activity \(U\) and recipient
activity \(V\). Deleting the root leaves an unordered set
of rooted branches. Expanding its exponential, including
the branch factorials, proves the coefficient identities
\[
       T_D=Ue^{t(2T_D+T_R)},\qquad T_R=Ve^{tT_D}.
 \tag{12}
\]
One may first restrict tree height; iteration from the
single-vertex trees proves these equations coefficientwise
and monotonically, without assuming convergence.

Use the inflated activities \(2U,2V\). Set
\(\eta=1/(4t)\). If
\[
            2Ue^{\,1/2+3tV_*}\le\eta,
 \tag{13}
\]
the iteration stays in
\(T_D\le\eta,\ T_R\le3V_*\):
indeed \(2V_*e^{1/4}<3V_*\), and the donor equation
gives the other bound. It therefore converges there.
The sum of unrooted trees is at most the rooted sum.
Inflation by two additionally controls every fixed
polynomial in the vertex number, since
\(\sup_{s\ge1}s^k2^{-s}<\infty\).

Every tree with at least two vertices contains a donor.
More quantitatively (12) and the above bounds give
\(T_D\le C_{V_*}U\) and
\(T_R-V\le C_{V_*}U\) at uninflated activities.
Hence the entire connected series, after subtracting
the isolated recipients, has an \(O_{V_*}(U)\)
majorant. These bounds persist on smaller complex
activity polydiscs and after any fixed number of
activity derivatives by Cauchy's formula.

## 3. The analytic phase and its nonzero amplitude

Define the homogeneous polynomials
\[
 \begin{split}
 T_s(\mathbf a)
   &=\sum_{\ell,T}\prod_\nu a_{\ell_\nu}\prod_{e\in T}B_e,\\
 J_s(\mathbf a)
   &=\sum_{\ell,T}\prod_\nu a_{\ell_\nu}\prod_{e\in T}B_e
       \left(\tfrac12\sum_{e\in T}B_e+
                        \sum_{e\in R(T)\setminus T}B_e\right).
 \end{split}
 \tag{14}
\]
For \(s=1\), put \(T_1=\sum a_\ell,\ J_1=0\).
The sign choice in (4) is understood. The convergent
analytic functions
\[
 \mathcal F_\pm(\mathbf a)=
       \sum_{s\ge1}\frac{\mathfrak c^{\,s-1}}{s!}T_s(\mathbf a),
 \qquad
 \mathcal A_\pm(\mathbf a)=
       \sum_{s\ge1}\frac{\mathfrak c^{\,s}}{s!}J_s(\mathbf a)
 \tag{15}
\]
are explicitly determined by the actual word kernel.
They satisfy
\[
 \mathcal F_\pm=\sum_i v_i+O(U),\qquad
 \mathcal A_\pm=O(U).
 \tag{16}
\]

The component identity and (10) show that (5) has the
exact logarithm given by its connected series on this
domain. To justify the identity analytically, first use
small common activities, where its formal exponential
identity converges absolutely. The tree majorant extends
the connected series and its exponential throughout the
stated domain. Equality follows there by analytic
continuation, or by scaling all activities from zero.
In particular \(Z_N^\pm\) never vanishes there.
Its logarithm is fixed by its value
\(N\sum_i v_i\) at \(u=0\).

Multiplying (11) by \(N^s|h|^{s-1}/s!\) and summing
with the inflated tree majorant proves
\[
 \log Z_N^\pm
       =N\mathcal F_\pm(\mathbf a)
                         +\mathcal A_\pm(\mathbf a)+O(N^{-1}).
 \tag{17}
\]
All fixed activity derivatives of the remainder satisfy
the same estimate on smaller compact domains. This is
a physical-ray estimate, not a complex-\(h\) assertion.
The same majorant without Taylor expansion also gives
\[
 \left|\log Z_N^\pm-N\sum_i v_i\right|
                                      \le C_{V_*}NU .
 \tag{18}
\]

The activities in (3) include the actual half shift
\(x=-Me^{-h/2}\). One may retain them in (17) exactly.
Alternatively put \(x_{\rm cl}=-M\) and let
\(\mathbf a_{\rm cl}\) be (3) with this value. Then
\[
 \mathcal K_N^\pm
   =e^{N F_\pm(z,w;M)}\,a_\pm(z,w;M)(1+O(N^{-1}))
 \tag{19}
\]
once the capacities are restored as below, where
\[
 \begin{split}
 F_\pm&=\mathcal F_\pm(\mathbf a_{\rm cl}),\\
 a_\pm&=\exp\left(
     \mathcal A_\pm(\mathbf a_{\rm cl})
       +\frac{\mathfrak c}{2}
          \sum_{j=2}^r(j-1)u_{j,\rm cl}
                        \partial_{u_j}\mathcal F_\pm(\mathbf a_{\rm cl})
                       \right).
 \end{split}
 \tag{20}
\]
The amplitude is holomorphic and nonzero. At \(w_1=0\)
it is exactly one and \(F_\pm=\sum_{i\ge2}z_iw_i\).
The half shift has not been absorbed into an unspecified
constant.

## 4. Restoring every finite cap relatively

Fix a compact chart with
\[
                       |v_i|\le\rho=1/8 .
 \tag{21}
\]
The donor activity \(U\) is now chosen sufficiently small
depending on \(r\), the compact meridian/coherent domain,
and a slightly larger version of (21). No smallness
condition on \(\sum_i|v_i|\) beyond its fixed bound
is needed.

For a function of one count marker analytic on
\(|\xi|\le R\), the tail at one has the exact expression
\[
       \sum_{k\ge N}[\xi^k]f(\xi)
        =\frac1{2\pi i}\oint_{|\xi|=R}
                  f(\xi)\frac{\xi^{-N}}{\xi-1}\,d\xi .
 \tag{22}
\]
Use radius two for the donor marker and radius eight
for each recipient marker. All marked activities (7)
then have recipient sum bounded by a constant depending
on \(r\), while their donor sum is at most \(16U\).
Choose \(U\) so that the preceding connected estimates
hold on all these marker polydiscs.

For any nonempty subset of the capacity tails, apply
(22) to its markers. Estimate the generating function
there using (18). Unmarked recipient phases remain
exactly \(N v_i\), not \(N|v_i|\). A marked recipient
contributes, relative to the unmarked function, at most
\[
       \exp N\{8|v_i|-\operatorname{Re}v_i-\log8\}
          \le \exp[-N(\log8-1-\rho)] .
 \tag{23}
\]
A marked donor contributes \(2^{-N}\). The remaining
logarithmic error is at most \(C_rNU\), uniformly for
every subset. Shrink \(U\) until this is smaller than
one quarter of
\(\min(\log2,\log8-1-\rho)N\).
The factors \(R/(R-1)\) in (22) are fixed.

Finally expand the product of all projections as a
finite inclusion--exclusion of these tail operators.
Equations (6)--(7) and (22)--(23) prove
\[
                 \mathcal K_N^\pm/Z_N^\pm
                                  =1+O(e^{-\delta N})
 \tag{24}
\]
for some \(\delta>0\), uniformly on smaller compact
charts, with all fixed coherent and fixed-\(q\)
meridian derivatives. Derivatives follow from the
same estimates on a slightly larger complex parameter
domain. This proves (19), including nonvanishing of
the actual finite kernel for sufficiently large \(N\).
It retains, rather than identifies, every original
capacity and its complementary tail.

## 5. Identifying the principal graph

This identification uses exact coherent contiguities,
not a complex occupation interpolation. In (5) select
the first donor letter. For the positive kernel,
\[
 \frac1N\partial_{w_1}Z_N^+
 =z_1Z_N^+
  +\sum_{j=2}^r x^{-(j-1)}z_j
       Z_N^+(Qz_1,Qz_2,\ldots,Qz_{j-1},
                         z_j,\ldots,z_r;w).
 \tag{25}
\]
For the negative kernel the corresponding \(j\)-term
has a minus sign and makes the replacements
\[
 z_1\mapsto Qz_1,\quad
 z_k\mapsto Q^{\,1+\mathbf1_{k<j}}z_k\ (k\ge2),\quad
 w_k\mapsto Q^{-1}w_k\ (k\ge2).
 \tag{26}
\]
The donor variable \(w_1\) is not shifted. Indeed the
extra inverse pair energy shifts every later nonzero
donor letter once; the compensating recipient \(w\)
shifts in (26) leave exactly the original recipient
prefix factors. This proves (25)--(26) directly from
the finite-word energies and then the convergent sum.

The analytic asymptotic (17), including derivatives,
allows these \(O(N^{-1})\) coherent shifts. Set
\[
 f_j^{\rm in}=\partial_{w_j}F,\quad
 \widehat w_j^{\rm out}=\partial_{z_j}F,\quad
 A_j^{\rm in}=e^{\mathfrak c w_j f_j^{\rm in}},\quad
 A_j^{\rm out}=e^{\mathfrak c z_j\widehat w_j^{\rm out}},
 \qquad f_j^{\rm out}=z_j .
 \tag{27}
\]
Exact homogeneity under \((z,w)\mapsto(tz,t^{-1}w)\)
gives \(\sum z_jF_{z_j}=\sum w_jF_{w_j}\).
Consequently (25)--(26) imply, respectively,
\[
 \begin{split}
 F_{+,w_1}
    &=z_1+A_1^{\rm out}F_{\rm tail}^{\rm out}/x_{\rm cl},\\
 F_{-,w_1}
    &=z_1-A_1^{\rm in}F_{\rm tail}^{\rm out}/x_{\rm cl},
 \end{split}
 \quad
 F_{\rm tail}^{\rm out}
    =\sum_{j=2}^r x_{\rm cl}^{-(j-2)}
             \left(\prod_{2\le i<j}A_i^{\rm out}\right)z_j .
 \tag{28}
\]
Before homogeneity is used, the negative exponent is
\(\mathfrak c(z_1F_{z_1}+\sum_{k\ge2}z_kF_{z_k}
 +\sum_{2\le k<j}z_kF_{z_k}-\sum_{k\ge2}w_kF_{w_k})\).
Thus both equations are analytic first-order evolution
equations in \(w_1\), involving only derivatives in
the other coordinates on their right sides.
Their initial value is exactly
\[
                         F|_{w_1=0}=\sum_{i\ge2}z_iw_i .
 \tag{29}
\]

We now check that these equations identify G's actual
principal correspondence. Work near a point of (29)
with every \(z_j\ne0\), and also
\[
        z_1+F_{\rm tail}^{\rm out}/x_{\rm cl}\ne0
       \quad\hbox{or}\quad
        z_1-F_{\rm tail}^{\rm out}/x_{\rm cl}\ne0
 \tag{30}
\]
for the corresponding sign. These are open conditions.
For the positive map of G put
\(C=1-p_1F_{\rm tail}/x_{\rm cl}\).
Its equations imply
\[
 f_1^{\rm in}=C f_1^{\rm out}+F_{\rm tail}/x_{\rm cl}
             =f_1^{\rm out}
                         +A_1^{\rm out}F_{\rm tail}/x_{\rm cl}.
 \tag{31}
\]
The tail \(F\) is preserved. Reversing this map gives
\(f_1^{\rm in}=f_1^{\rm out}
-A_1^{\rm in}F_{\rm tail}/x_{\rm cl}\) for the inverse.
These are exactly (28).

The mixed projection of this rational canonical map
is nonsingular at \(p_1=0\). Indeed the recipients
are unchanged there, while
\[
 w_1=\frac{\log A_1^{\rm in}}
                   {\mathfrak c f_1^{\rm in}}
                    =-p_1/\mathfrak c+O(p_1^2).
 \tag{32}
\]
At fixed nonzero recipient \(z_i\), their coordinate
changes \(A_i\mapsto\log A_i/(\mathfrak c z_i)\)
are invertible. All \(C,T_j\) of G equal one at
this row, so no denominator is lost. The holomorphic
inverse-function theorem therefore gives its graph
in the mixed coordinates \((z,w)\) on a neighborhood.

G's symplectic identity becomes the standard
\(\mathfrak c\,dz\wedge dw\) identity in these
coordinates. Its mixed one-form
\(\sum\widehat w_j^{\rm out}dz_j+
 \sum f_j^{\rm in}dw_j\) is closed. Integrating on
a small polydisc gives its generating function,
normalized by (29). It satisfies (28), before
homogeneity in the inverse case, by (31): total
Cartan conservation gives equality of the sums
of the input and output logarithms on the
branches agreeing at (29).
Analytic solutions of (25)'s principal equation
or (26)'s principal equation with (29) are unique:
their successive Taylor coefficients in \(w_1\)
are recursively determined by the preceding ones.
Hence this classical generating function is
exactly \(F_\pm\). This proves equality of the full
principal graphs, including the selected lower flag.

In particular the old resolved coordinate
\((A_1-1)/p_1=-f_1\) remains finite at this row;
it is not replaced by the singular quotient \(0/0\).
The coherent amplitude (20) extends across that row
and is one there. This is a whole-star statement,
not an inference from nonvanishing of its separate
columns.

## 6. Source scope

The theorem applies to the literal finite kernel (2),
with its exact gauge interfaces and all capacity
projectors. It is uniform on smaller compact open
charts satisfying (21), sufficiently small donor
activity, and (30) when the graph is identified.
Such charts are nonempty and have fixed size
independent of \(N\). They contain resolved lower
row points with the indicated recipient logarithms.

For a geometric point, the retained assignment is
\(z=f,\ w=\log A/(\mathfrak c f)\); membership in
this chart must still be checked. An upper
logarithmic lift is not reset to the lower one.
The result gives no interpolation of integer
recipient occupations and no complex-\(h\)
zero-free neighborhood. Fixed-\(q\) meridian
derivatives are those of the actual finite
matrices and their actual half shifts.

The estimate may be inserted into B's exact paired
period only on a domain where its hypotheses hold;
the complementary kernels and interfaces remain.
It proves neither such a domain for the whole
original cycle nor a nonzero closed pairing.

## Complete proof-source pins

* W: notes/research_reduced_euler_star_complex_word_kernel.md,
  SHA256 6baac1f8303d21be4a5c3f6c809795272dd51d3e0060e13843e0f25958902fdb.
* D: notes/research_reduced_euler_donor_coherent_sum.md,
  SHA256 ff35583f203ae7686de4ff7fb91fcb4d4d0190e4f8995bd89a871849bc91d7f4.
* B: notes/research_reduced_word_bargmann_source_period.md,
  SHA256 abbe118e89f2d80f82f4bcd591a71dc193fda852cd488262461d07b262696655.
* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.

All four complete sources were read nontruncated in the active
author/formal sequence and retained unchanged. Every used
implication was checked. All new calculations are written
proofs; no mathematical programs were run and no frozen or
public files were edited.
