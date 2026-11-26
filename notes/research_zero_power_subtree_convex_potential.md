# The convex Fourier bound for a subtree with zero crossing powers

Research note, 2 November 2026. This note determines the best imaginary-angle
bound supplied by the positive low-index part of the exact source. For a
selected subtree whose original vertices all have degree at least three,
the bound has a unique finite minimizer. The minimizer need not have all
edge indices in the interior of their ranges: two adjacent trivalent
vertices give an explicit example where one index reaches the endpoint.

The minimum below is an upper bound for the all-low contribution.
Identifying it with the complete source rate additionally requires
estimates for high indices and a nonzero contribution at the minimizer.
The convex calculation by itself makes neither that identification nor
a claim about hyperbolic volume.

The [full Newton-coordinate theorem](research_all_zero_subtree_newton_packet.md)
now evaluates the original boundary source for all the subtrees considered
here, using the strict Newton optimizer. On the regular region its action
agrees with the minimum in this note. At the trivalent fold it uses
different, nonsingular coordinates; the convex calculation below explains
why the edge-index Gaussian does not suffice there.

## 1. The source and the variational problem

Let \(T\) be a fixed finite tree, and let \(S\) be a nonempty connected
proper set of its vertices. All crossing powers at vertices in \(S\)
are zero. The degree \(d_v\) is the degree of \(v\) in the original
tree, including edges from \(S\) to its complement. Write \(E_S\)
for all edges with at least one endpoint in \(S\). Each such edge is
counted once. In a tree, an outside vertex cannot meet two vertices of
the connected set \(S\).

We use the original Newton polynomials, kernel, and closing functional
from [the full Fourier calculation](research_zero_power_subtree_fourier_bound.md):
\[
 e_a(z)=S_a^{-2}\prod_{j<a}
       \left(2\cos\frac{(2j+1)\pi}{N}-z\right),
 \qquad S_a=\prod_{j=1}^{a}2\sin\frac{\pi j}{N},
 \tag{1}
\]
\[
 K_N(t,u)=\sum_{a=0}^{N-1}e_a(-2\cos t)e_a(-2\cos u),
 \qquad
 \phi_N(f)=(-1)^{N-1}N^2[z^{N-1}]
                  \operatorname{rem}_{P_N}f,
 \tag{2}
\]
where
\[
 P_N(z)=\prod_{j=0}^{N-1}
              \left(z-2\cos\frac{(2j+1)\pi}{N}\right).
\]
The remainder is taken with the multiplicities of these roots retained.
In particular, the closing functional includes the derivative data at
double roots. The selected source is
\[
 Z_{S,N}(\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[
 \prod_{vw\subset S}K_N(t_v,t_w)
 \prod_{\substack{vw\in E_S\\v\in S,\ w\notin S}}
                         K_N(t_v,u_{vw})
 \right].
 \tag{3}
\]
An index \(a\) is called low when \(2a<N\). Denote the part of
(3) with every edge index low by \(Z^{\mathrm{low}}_{S,N}\).
The full source also has terms with high indices; they will be discussed
in Section 6.

Give each selected vertex a nonnegative height \(h_v\), representing
the imaginary angle \(t_v=-ih_v\), and set the outside heights to zero.
For \(0\le x\le 1/2\), define
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
 \qquad
 B(x,h)=\int_0^x\log(2\cos2\pi s+2\cosh h)\,ds-2J(x).
 \tag{4}
\]
The integrals have their continuous endpoint values. At \(h=0\),
the logarithmic zero at \(x=1/2\) is integrable. The edge potential is
\[
 V(h,g)=\max_{0\le x\le1/2}\{B(x,h)+B(x,g)\}.
 \tag{5}
\]
Finally, define
\[
 \mathcal L_S(\mathbf h)=
       \sum_{vw\in E_S}V(h_v,h_w)-\sum_{v\in S}h_v,
       \qquad h_w=0\quad(w\notin S).
 \tag{6}
\]
The linear term in (6) comes from the first nonzero Fourier charge
of each original closing functional. The exact estimate below also
retains all higher charges.

## 2. The edge maximum, including its endpoint

We first calculate (5) without assuming that its maximum is interior.
For \(h>0\) and \(0<x<1/2\), differentiation of (4) gives
\[
 B_h(x,h)=\frac1\pi\arctan\left(\tanh(h/2)\tan\pi x\right),
 \tag{7}
\]
\[
 B_{hh}(x,h)=
 \frac{\tan\pi x\,\operatorname{sech}^2(h/2)}
      {2\pi\{1+\tanh^2(h/2)\tan^2\pi x\}}>0.
 \tag{8}
\]
For example, (7) follows by substituting \(y=2\pi s\) in
\(\int_0^x\sinh h/(\cos2\pi s+\cosh h)\,ds\), and then
using \(\tan(y/2)\). At the two endpoints,
\[
 B(0,h)=0,\qquad B(1/2,h)=h/2.
 \tag{9}
\]
For the second identity, \(B(1/2,0)=0\) follows from the elementary
sine and cosine integrals, and (7) tends to \(1/2\) as
\(x\uparrow1/2\) for every \(h>0\). Thus \(B(x,h)\) is
convex in \(h\) for each fixed \(x\), including the two endpoints.
Equation (7) also bounds its height derivative between zero and \(1/2\).
Consequently \(B\) is uniformly \(1/2\)-Lipschitz in its height
variable; this gives continuity at \(h=0\) uniformly in the index.

Put
\[
 r=\sinh(h/2),\qquad s=\sinh(g/2),\qquad p=rs.
\]
The function \(A(x)=B(x,h)+B(x,g)\) is strictly concave in
\(0<x<1/2\), because
\[
 A''(x)=\sum_{a\in\{h,g\}}
 \left[-\frac{2\pi\sin2\pi x}{\cos2\pi x+\cosh a}
             -2\pi\cot\pi x\right]<0.
 \tag{10}
\]
Its derivative tends to positive infinity at zero. If both heights are
positive, its derivative at the other endpoint is
\[
 A'(1/2)=2\log p.
 \tag{11}
\]
If one height is zero, that derivative tends instead to negative
infinity. It follows that the maximum in (5) is unique and has the
following two forms:

* If \(p<1\), the maximum is at an interior point \(x_*(h,g)\),
  given by
  \[
   \tan(\pi x_*)=
   \frac{\sqrt{1+r^2}\sqrt{1+s^2}}{\sqrt{1-r^2s^2}}.
   \tag{12}
  \]
* If \(p\ge1\), the maximum is at \(x_*=1/2\), and
  \[
   V(h,g)=(h+g)/2.
   \tag{13}
  \]

For completeness, to obtain (12), set \(c=\cos\pi x\).
The equation \(A'(x)=0\) is
\((c^2+r^2)(c^2+s^2)=(1-c^2)^2\), hence
\(c^2=(1-r^2s^2)/(2+r^2+s^2)\). At \(p=1\), (10)
and (11) show that \(A'\) is positive throughout the open interval;
the endpoint is still the unique maximum.

We call an edge regular at a height vector if \(p<1\). Every edge
joining \(S\) to its complement is regular, because one height is
zero. This use of “regular” refers specifically to the position of the
real index maximum; it is not a claim about the topology of a filled
manifold.

## 3. Convexity and the full two-variable Hessian

For each fixed \(x\), the function
\(B(x,h)+B(x,g)\) is convex in \((h,g)\). Taking its supremum
over the fixed compact interval proves that \(V\) is convex on
the entire nonnegative quadrant. This proof includes the region where
the index maximum is at the endpoint.

The unique maximizing index varies continuously with \((h,g)\).
Indeed, every convergent subsequence of maximizing indices maximizes
the limiting continuous function, and uniqueness identifies its limit.
For positive heights, the derivatives in (7) are continuous uniformly
for \(0\le x\le1/2\). Comparing the values at the old and new
maximizing indices therefore proves differentiability of \(V\), with
derivative obtained by evaluating (7) at the maximizer. On a regular
edge,
\[
 V_h(h,g)=\frac{\alpha_h}{\pi},\qquad
 \alpha_h=
 \arcsin\left(\frac{r\sqrt{1+s^2}}{\sqrt{1+r^2}}\right)
 =\arctan\left(\frac{r\sqrt{1+s^2}}{\sqrt{1-r^2s^2}}\right).
 \tag{14}
\]
The inverse sine and inverse tangent take their real values between
zero and \(\pi/2\). At \(p\ge1\), both derivatives of \(V\)
are \(1/2\). These formulas agree continuously at \(p=1\).
When \(h=0\) and \(g\) is finite, the maximizing index is interior,
and the one-sided derivative \(V_h(0,g)\) is zero.

The complete Hessian on a regular edge with positive heights is
\[
 \nabla^2V(h,g)=
 \frac1{2\pi\sqrt{1-p^2}}
 \begin{pmatrix}
   \dfrac{\sqrt{1+s^2}}{\sqrt{1+r^2}}&p\\[6pt]
   p&\dfrac{\sqrt{1+r^2}}{\sqrt{1+s^2}}
 \end{pmatrix}.
 \tag{15}
\]
For instance, differentiating the inverse sine in (14) uses
\[
 1-\frac{r^2(1+s^2)}{1+r^2}
       =\frac{1-r^2s^2}{1+r^2}.
\]
The first diagonal entry in (15) is positive, and
\[
 \det\nabla^2V(h,g)=\frac1{4\pi^2}>0.
 \tag{16}
\]
Thus the two-variable Hessian is positive definite; positivity of its
diagonal entries alone is not the assertion being used. On a boundary
edge, whose other height is fixed at zero, the relevant scalar second
derivative is
\[
 \frac{d^2}{dh^2}V(h,0)=\frac1{2\pi\cosh(h/2)}>0.
 \tag{17}
\]
There need not be a finite second derivative across \(p=1\).
Global convexity and the continuous first derivatives suffice there.

## 4. Existence and uniqueness of the optimal height vector

**Proposition.** Suppose \(d_v\ge3\) for every selected vertex.
Then \(\mathcal L_S\) has exactly one minimizer in
\([0,\infty)^S\). All its coordinates are finite and strictly
positive. Every selected vertex meets at least one regular edge at
the minimizer. The function is locally strongly convex there, even if
some other edges attain their index maximum at \(1/2\).

**Proof.** The convexity in Section 3 makes \(\mathcal L_S\)
convex. Choosing \(x=1/2\) in (5) and using (9) gives
\[
 \mathcal L_S(\mathbf h)
 \ge\sum_{v\in S}(d_v/2-1)h_v
 \ge\frac12\sum_{v\in S}h_v.
 \tag{18}
\]
Consequently its sublevel sets are bounded. Continuity makes them
closed, so a finite minimum exists.

If \(h_v=0\), all incident edge derivatives with respect to that
coordinate are zero, by Section 3. The one-sided partial derivative
of \(\mathcal L_S\) in the positive \(h_v\) direction is
therefore \(-1\). A minimizer cannot have such a coordinate.
It lies in the positive orthant and satisfies the ordinary stationary
equations.

Suppose a selected vertex had no regular incident edge at a minimizer.
All \(d_v\) contributions to its derivative would then be \(1/2\),
giving
\(\partial_{h_v}\mathcal L_S=d_v/2-1>0\), a contradiction.
Thus the regular edges at a minimizer cover every selected vertex.

Take the sum of the edge potentials over just these regular edges.
Their Hessians are the positive definite two-variable forms (15),
or the positive scalar forms (17) for edges leaving \(S\).
Their sum is positive definite on \(\mathbb R^S\). To see this
without an assumption about the connectivity of the regular edges,
take any nonzero vector and choose a coordinate at which it is nonzero.
A regular edge incident to that vertex contributes a strictly positive
local quadratic form; every other chosen edge contributes a
nonnegative one. Since there are finitely many edges, continuity gives
a positive lower bound for this Hessian on a sufficiently small
neighborhood of the minimizer. The other edge potentials remain convex.
Hence their addition preserves local strong convexity. Two distinct
global minimizers would give a segment of minima by convexity, contrary
to local strong convexity at either endpoint. This proves uniqueness.
\(\square\)

Writing \(\alpha_{v,e}=\pi V_{h_v}\) for each incident edge,
the stationary equations at the minimizer are
\[
 \sum_{e\ni v}\alpha_{v,e}=\pi
                         \qquad(v\in S).
 \tag{19}
\]
For a regular internal edge, \(\alpha_{v,e}\) is given by (14).
For an internal edge with its maximum at \(1/2\), it is \(\pi/2\).
For an edge leaving \(S\), it is
\(\arctan(\sinh(h_v/2))\). The proposition does not assert that
every term in (19) comes from a regular edge.

There is a useful degree condition under which they all do.

**Corollary.** Suppose \(|S|\ge2\), every selected degree is at least
three, and each internal edge \(vw\) satisfies
\[
 \tan(\pi/d_v)\tan(\pi/d_w)\le1.
 \tag{19a}
\]
Then every edge is regular at the unique minimizer. In particular,
this holds for any selected subtree all of whose original degrees are
at least four, without a bound on the number of selected vertices.
It also permits a selected degree-three vertex when each of its
selected neighbors has degree at least six.

**Proof.** Put \(r_v=\sinh(h_v/2)\) at the minimizer. Every incident
angle in (19) is at least \(\arctan r_v\). On a regular internal edge
this follows from (14), since the other height is positive; the
inequality is strict. On an internal edge whose maximum is at the
endpoint, it follows from \(\pi/2>\arctan r_v\), and is again
strict. Since \(S\) is connected and has at least two vertices, every
selected vertex has an internal neighbor. Thus (19) implies
\[
 d_v\arctan r_v<\pi,
 \qquad r_v<\tan(\pi/d_v).
 \tag{19b}
\]
For any internal edge, (19a) now gives \(r_vr_w<1\), which is
exactly regularity. Boundary edges are regular automatically.
\(\square\)

For a singleton the corresponding index is also interior: its height
is \(2\operatorname{arsinh}(\tan(\pi/d_v))\), and all its edges
have outside height zero. The corollary supplies existence and
nondegeneracy of an interior imaginary-angle saddle for many connected
zero-power subtrees. It does not estimate their high-index terms.

## 5. What the minimum bounds in the finite source

The exact Fourier estimate connects (6) to the original trace, without
removing its higher charges. Let \(k=|S|\), and let
\(F_N(\mathbf t)\) be the all-low product in (3) before tracing,
with every outside angle set to zero. For a low index,
\[
 e_a(-2\cos t)=\frac{S_{2a}}{S_a^2}
       \sum_{r=-a}^{a}\frac{e^{irt}}{S_{a+r}S_{a-r}}
 \tag{20}
\]
has positive Laurent coefficients. The separately even Laurent
polynomial \(F_N\) therefore has nonnegative coefficients.
[Section 3 of the Fourier note](research_zero_power_subtree_fourier_bound.md#3-every-fourier-charge-in-the-iterated-trace)
derives the complete derivative-sampling formula and proves, for every
positive height vector,
\[
 \sup_{\mathbf u\in\mathbb R^{\partial S}}
        |Z^{\mathrm{low}}_{S,N}(\mathbf u)|
 \le N^{2k}F_N(-i\mathbf h)
       \prod_{v\in S}
       \frac{2\cosh h_v\,e^{-Nh_v}}
            {(1-e^{-Nh_v})^2}.
 \tag{21}
\]
The inequality uses positivity of the full quotient trace for each
fixed low-index assignment and
\(|e_a(-2\cos u)|\le e_a(-2)\) for real \(u\).
The geometric-series factors in (21) include every nonzero Fourier
charge, at both parities of \(N\).

Uniform sum-to-integral estimates, including the endpoint indices,
give
\[
 \log\{e_a(-2\cosh h)e_a(-2\cosh g)\}
 =N\{B(a/N,h)+B(a/N,g)\}+O_{h,g}(\log N)
 \tag{22}
\]
for \(2a<N\). The number of edge indices is fixed. The edge sums
are positive, so their exponential rates are their maxima in (5).
The low lattice approaches \(x=1/2\), including when that endpoint
is the maximizer. It follows from (21) that
\[
 \limsup_{N\to\infty}\frac1N
 \log\sup_{\mathbf u\in\mathbb R^{\partial S}}
           |Z^{\mathrm{low}}_{S,N}(\mathbf u)|
 \le \mathcal L_S(\mathbf h).
 \tag{23}
\]
Applying (23) at the unique positive minimizer \(\mathbf h_*\)
proves the precise bound
\[
 \limsup_{N\to\infty}\frac1N
 \log\sup_{\mathbf u\in\mathbb R^{\partial S}}
           |Z^{\mathrm{low}}_{S,N}(\mathbf u)|
 \le \min_{\mathbf h\ge0}\mathcal L_S(\mathbf h).
 \tag{24}
\]

There is also a strict bound for low-index assignments separated from
the unique edge-maximizing vector at \(\mathbf h_*\). If a closed
subset of \([0,1/2]^{E_S}\) does not contain that vector, continuity
and the uniqueness of each edge maximum give \(\delta>0\) such that
its partial source is at most
\[
 C N^A\exp\{N(\mathcal L_S(\mathbf h_*)-\delta)\}
 \tag{25}
\]
uniformly for real boundary angles. This remains true when a maximizing
index is \(1/2\); its neighborhood must then include the endpoint.
If every edge is regular at \(\mathbf h_*\), all such neighborhoods
may instead be chosen as closed intervals strictly inside \((0,1/2)\).
This is the interior-index tail estimate proved in the Fourier note.

Neither (24) nor (25) is a lower bound. In particular, they do not
show that the charge-one contribution survives the exact trace, or that
its leading coefficient is nonzero.

## 6. Two adjacent trivalent vertices and the remaining problem

Let \(S\) consist of two adjacent vertices, each of original degree
three. Each selected vertex has two edges to free vertices. Put
\(r=\sinh(h_1/2)\) and \(s=\sinh(h_2/2)\).
If the shared edge were regular, (19) would read
\[
 2\arctan r+
 \arcsin\frac{r\sqrt{1+s^2}}{\sqrt{1+r^2}}=\pi,
 \qquad
 2\arctan s+
 \arcsin\frac{s\sqrt{1+r^2}}{\sqrt{1+s^2}}=\pi.
 \tag{26}
\]
Each inverse sine would be strictly smaller than \(\pi/2\).
The first equation would require \(r>1\), the second \(s>1\),
contradicting regularity \(rs<1\).

The unique minimizer supplied by Section 4 is explicitly
\[
 h_1=h_2=2\operatorname{arsinh}1.
 \tag{27}
\]
Indeed, then \(r=s=1\), the shared edge contributes \(\pi/2\)
to each equation (19), and each of the two outside edges contributes
\(\pi/4\). Thus the gradient is zero, and convexity and uniqueness
prove (27). At this minimizer the shared edge has
\[
 x_{\mathrm{shared}}=1/2,
 \qquad
 x_{\mathrm{outside}}=\frac1\pi\arctan\sqrt2.
 \tag{28}
\]
The failure of an interior shared index is therefore not caused by
choosing poor contour constants. It occurs at the unique optimal height
vector for the positive low-index estimate.

The full source also retains high-index terms. The exact positive Newton
multiplication rule shows that a nonzero assignment has at most one high
edge at each selected vertex. Internal high edges consequently form a
matching. A high shared edge affects both endpoint traces, so estimates
for a high boundary index at a single isolated vertex do not settle it.
[Section 6 of the Fourier note](research_zero_power_subtree_fourier_bound.md#6-what-the-high-indices-still-require)
gives a coefficient bound for these terms, but no comparison of an
arbitrary high matching with (24).

The edge-coordinate argument alone does not compare high-index matchings
with the optimized bound or provide a nonzero asymptotic when an edge
maximum is \(1/2\). The example (27) requires the latter analysis even
for the smallest adjacent trivalent subtree. It does not prove
nonhyperbolicity of the corresponding filling, or disprove a volume
limit. The Newton-coordinate theorem linked above handles both analytic
questions by retaining all internal indices from the outset. The
original geometric periods and the volume identification are separate
from that theorem.
