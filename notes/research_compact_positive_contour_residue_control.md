# Complete physical residue packets on compact positive contours

Private written proof, 16 November 2026.

The physical-row Jacobi formula already supplies an exact replacement
for an independent first normal inside a subsequent original trace.
Here its determinant form removes all apparent resolvent poles, and
the all-row slit theorem bounds that replacement by the action of
the original physical row. This gives a uniform estimate for complete
physical residue packets of a fixed graph, including edges between
frozen vertices and all mixed first normals.

The result controls the local cost of crossing original grid poles
on compact positive-angle contours. It does not construct the
remaining joint contour, bound its untouched kernel factors, or
change an ordinary free-boundary polynomial.

## 1. Original rows and the pole-free normal representative

Let \(N\ge2\), and put
\[
 \theta=\pi/N,\quad D=N-1,\quad\eta=(-1)^D,\quad
 c(x)=2\cos((2x+1)\theta),\quad c_j=c(j),\quad
 s_x=2\sin(x\theta),
\]
\[
 P_N(z)=2T_N(z/2)+2,\qquad
 e_k(z)=\frac{\prod_{a<k}(c_a-z)}{\prod_{a=1}^k s_a^2},
 \qquad K_N(z,w)=\sum_{k=0}^{D}e_k(z)e_k(w).
 \tag{1}
\]
All algebra operations and traces are the original ones,
\(\phi_N(f)=\eta N^2[z^D]\operatorname{rem}_{P_N}f\).
The distinct physical rows are
\[
 0\le j\le J_N=\lfloor(N-1)/2\rfloor,\qquad
 F_j(w)=K_N(c_j,w).
 \tag{2}
\]
Only \(0\le j\le\lfloor(N-2)/2\rfloor\) have an independent
first spectral normal. For those rows set
\[
 G_j(w)=\partial_zK_N(c_j,w),\qquad Q_0(w)=G_0(w).
 \tag{3}
\]

Use the original Jacobi coefficients
\[
 A(x)=\frac{s_{x+1}^4}{s_{2x+1}s_{2x+2}},\qquad
 C(x)=\frac{s_x^4}{s_{2x}s_{2x+1}},\qquad C(0)=0.
 \tag{4}
\]
For \(j\ge1\), let \(\mathcal J_j(\varepsilon)\) be the
symmetric \(j\)-row matrix with diagonal
\(c_0+A(r+\varepsilon)+C(r+\varepsilon)\) and off-diagonal
\(-\sqrt{A(r+\varepsilon)C(r+1+\varepsilon)}\).
The branches are the positive ones at \(\varepsilon=0\).
Define the polynomials
\[
 F_j^{(\varepsilon)}(w)=
 \frac{\det(\mathcal J_j(\varepsilon)-wI)}
      {\prod_{r<j}A(r+\varepsilon)},\qquad
 R_j(w)=\left.\partial_\varepsilon
                     F_j^{(\varepsilon)}(w)\right|_{\varepsilon=0}.
 \tag{5}
\]
Set \(R_0=0\). The exact ordinary range in (5) is the range
in (2); no equation beyond the last ordinary row is imposed.
At zero, (5) is the original \(F_j\).

Write \(w(t)=-2\cos t\). The archived logarithmic-factorial
representative of \(Q_0\) is
\[
 \widetilde Q_N(t)=
 -\frac{g_N'(D/2-t/(2\theta))-g_N'(0)}
        {2\theta\sin\theta},\qquad
 g_N'(z)=\frac{\pi}{N^2}
             \sum_{a=0}^{D}(z-a)\cot\frac{\pi(z-a)}N .
 \tag{6}
\]
The removable terms in the finite sum have their continuous values.
This is even and holomorphic on \(|\Re t|<\pi+\theta\);
it has exactly the values and required first spectral normals
of \(Q_0(w(t))\). For each fixed height \(H\),
\[
 \sup_{|\Re t|\le\pi,\ |\Im t|\le H}
       |\widetilde Q_N(t)|
       \le C_H N^2(1+\log N).
 \tag{7}
\]
These are full-jet identities, not an off-grid approximation
to the canonical polynomial \(Q_0\).

For a double physical row define
\[
 \boxed{\quad
 \widehat G_j(t)=
 \frac{c'(0)F_j(w(t))\widetilde Q_N(t)+R_j(w(t))}
      {c'(j)},\qquad
 c'(j)=-4\theta\sin((2j+1)\theta).
 \quad}
 \tag{8}
\]
For \(j=0\), this gives \(\widehat G_0=\widetilde Q_N\).

**Proposition 1.** Formula (8) is even and holomorphic on the
whole strip \(|\Re t|<\pi+\theta\). It has no Jacobi resolvent
poles. On the original window \(|\Re t|<\pi\), it descends
to a holomorphic function \(\widehat G_j(w)\) on
\(\Omega=\mathbb C\setminus[2,\infty)\), including \(w=-2\).
At every physical second endpoint it has exactly the value
and required first \(w\)-normal of \(G_j(w)\).

Consequently \(G_j\) can be replaced by \(\widehat G_j\)
inside every subsequent original trace in that endpoint,
with arbitrary original spectators. Products preserve all
mixed first normals under further original traces.
No equality at an untraced complex endpoint is asserted.

**Proof.** For \(j\ge1\), the exact Jacobi normal formula in
the pinned source is
\[
 \begin{split}
 c'(j)G_j(w)={}&c'(0)F_j(w)Q_0(w)+R_j(w)\\
 &+\frac{c'(0)P_N(w)}{N^2s_1^2}
                 F_j(w)[(\mathcal J_j-wI)^{-1}]_{00}.
 \end{split}
 \tag{9}
\]
The last term is \(P_N\) times a polynomial cofactor. It has
zero required jets at every second-endpoint double node, since \(P_N=P_N'=0\);
at the odd simple node only its value is required and \(P_N=0\).
The remaining endpoint term can be replaced by (6), with all
its physical jets. At \(j=0\) the assertion is directly (6);
this also covers the only double row when \(N=2\).
This proves the exact jet assertion.

Equation (5) makes \(R_j\) a polynomial without division by
\(\det(\mathcal J_j-wI)\). Thus (8) is holomorphic on the
asserted strip, even where the resolvent expression for
\(R_j/F_j\) would have a pole. Evenness supplies holomorphic
descent through \(t=0\), because \(w+2=t^2+O(t^4)\).
The map \(t\mapsto-2\cos t\) from \(|\Re t|<\pi\), modulo
\(t\mapsto-t\), parametrizes \(\Omega\); this proves the
spectral assertion. The ordinary product rule proves every
subsequent trace and mixed-normal statement. \(\square\)

## 2. Uniform slit bounds with the row's own action

**Theorem 2.** Fix a compact \(\mathcal K\Subset\Omega\) and
an integer \(k\ge0\). For all sufficiently large \(N\), uniformly
in every eligible row and \(w\in\mathcal K\),
\[
 |\partial_w^k F_j(w)|\le C_k N^k|F_j(w)|,\qquad
 |\partial_w^k\widehat G_j(w)|
       \le C_k N^{6+k}(1+\log N)|F_j(w)|.
 \tag{10}
\]
The second inequality concerns the double-row range only.
Every fixed derivative is an ordinary spectral derivative;
in particular it remains meaningful at \(w=-2\).

Define, on its original branch,
\[
 \Psi_x(w)=\int_0^x
    2\operatorname{arsinh}
          \left(\frac{\sqrt{2-w}}2\cot(\pi s)\right)\,ds,
 \qquad 0\le x\le\tfrac12,
 \tag{11}
\]
where the square root has positive real part. For every
\(\epsilon>0\), the right sides of (10) are bounded by
\[
 C_{\epsilon,k}N^{6+k}(1+\log N)
            \exp N\{\Re\Psi_{j/N}(w)+\epsilon\}.
 \tag{12}
\]
On compact subsets of \(\Re w<2\), the fixed exponential
tolerance can instead be replaced by a fixed power of \(N\).

**Proof.** The spectrum of \(\mathcal J_j\) lies in
\((c_0,\infty)\), and \(c_0\to2\). On a slightly larger
compact slit neighborhood of \(\mathcal K\), its distance
from this ray is bounded below independently of \(N,j\).
Hence the resolvent and every fixed \(w\)-derivative of it
are uniformly bounded there. The source bounds
\[
 \|\mathcal J_j'\|\le6\pi N^3,\qquad
 |A'(r)/A(r)|\le4\pi,\qquad
 |c'(j)|\ge8\pi/N^2,\qquad
 |c'(0)/c'(j)|\le1
 \tag{13}
\]
hold throughout the stated double-row range. Differentiating
the determinant in (5) gives exactly
\[
 \frac{R_j(w)}{F_j(w)}
 =\operatorname{Tr}((\mathcal J_j-wI)^{-1}\mathcal J_j')
                           -\sum_{r<j}A'(r)/A(r).
 \tag{14}
\]
This and every fixed spectral derivative are \(O_k(N^4)\).
The spectral form of (7), with Cauchy on a larger compact
slit neighborhood, bounds all fixed derivatives of
\(\widetilde Q_N\) by \(O_k(N^2(1+\log N))\).
Thus (8) divided by \(F_j\) has all these derivatives bounded
by \(C_kN^6(1+\log N)\).

The logarithmic determinant formula also gives
\[
 |\partial_w^\ell\log F_j(w)|
       \le(\ell-1)!\,j\,\operatorname{dist}
                  (w,[c_0,\infty))^{-\ell}\quad(\ell\ge1).
 \tag{15}
\]
Differentiating the exponential of this logarithm proves the
first inequality of (10), and the product rule proves the second.
The zero row is handled directly by (7).

The complete all-row slit theorem gives, uniformly in \(j\),
\[
 N^{-1}\log F_j(w)=\Psi_{j/N}(w)+o(1),
 \tag{16}
\]
with the logarithm positive-real normalized at \(w=-2\).
Its stronger half-plane statement has error \(O(\log N)/N\).
Combining these with (10) proves the remaining assertions.
\(\square\)

The original angular edge phase with one real angle can be
calibrated directly from (11):
\[
 \psi(t,s)=\Psi_{(\pi-|s|)/(2\pi)}(-2\cos t),
       \qquad -\pi<s<\pi,\quad |\Re t|<\pi.
 \tag{17}
\]
It has \(\psi(t,\pi)=0\) by the limiting value \(x=0\).
For \(s>0\),
\[
 \partial_s\psi(t,s)=
 -\pi^{-1}\operatorname{arsinh}
                  \{\cos(t/2)\tan(s/2)\}.
 \tag{18}
\]
This is the original positive edge return, with its complete
constant fixed by \(\Psi_{1/2}\). The expression extends evenly
and analytically through \(s=0\).
For two real arguments it is symmetric: apply the exact symmetry
of \(K_N\), (16), and approximation by physical nodes on real
compact sets. In an incident-edge expression with only one real
endpoint, put that endpoint second in (17).

At the positive physical angle
\(\tau_j=\pi-(2j+1)\pi/N\), the exact relation is
\[
 \Psi_{j/N}(-2\cos t)=\psi(t,\tau_j+\pi/N).
 \tag{19}
\]
On any compact \(|\tau_j|\le\pi-\delta\), the difference
between (19) and \(\psi(t,\tau_j)\) is \(O(N^{-1})\),
uniformly on compact first-angle sets. At the odd simple
node \(\tau_{J_N}=0\), the same statement holds for its value.
Even without such a row buffer, the upper comparison
\(\Re\Psi_{j/N}\le
\Re\Psi_{(j+1/2)/N}\) follows because the integrand in (11)
has positive real part. Thus using the actual physical
angle introduces no larger upper action.

Every compact family of original positive angles lies in the
slit charts used here. Indeed positivity includes
\(|\Re t|<\pi\). If \(-2\cos(s+ih)\) is real, then
\(\sin s\,\sinh h=0\). When \(h=0\), its value is less than
2; otherwise \(s=0\), and its value is at most \(-2\).
The value can therefore never belong to \([2,\infty)\).
Compactness supplies a uniform slit distance. This argument
does not impose a half-plane restriction on the positive family.

For an edge with both endpoints physical, the separate all-color
estimate from the pinned physical-pressure source is stronger
than a fixed-slit continuation. Uniformly over the entire physical
grids, including colors approaching \(2\),
\[
 \begin{split}
 K_N(c_j,c_k)&\le C N^a e^{N\psi(\tau_j,\tau_k)},\\
 |\partial_zK_N(c_j,c_k)|&\le N^{11}K_N(c_j,c_k),\\
 |\partial_z\partial_wK_N(c_j,c_k)|
                   &\le (N^{16}+N^{22})K_N(c_j,c_k).
 \end{split}
 \tag{19a}
\]
Each derivative is asserted only at endpoints having that
original first normal. The first-derivative bound also covers
an odd simple node at the other endpoint.
The value estimate follows from the zero-inclusive uniform real
Newton entropy and the literal terminating support; its maximum
is the original \(\psi\). Thus it has a polynomial prefactor
even when both indices are \(o(N)\). The normal estimates are
for the original full polynomials, including high Newton terms.
They do not come from differentiating the terminating values.

## 3. Complete frozen-vertex residue packets

Let \(\Gamma\) be a fixed finite loopless graph, with the
original same-index edge \(K_N\) on every edge and a fixed
signed integer crossing power at each traced vertex.
Repeated edges cause no change. Choose a set \(S\) of traced
vertices to freeze at one of the distinct physical spectral
nodes for each vertex; different vertices may use the
same node. No condition on the signs or nonvanishing of
the powers is needed.

For a double node define the original local trace functional
\[
 \mathcal R_{j,N}f
       =\eta\{(4-c_j^2)f'(c_j)-c_jf(c_j)\}.
 \tag{20}
\]
At the odd simple node define
\(\mathcal R_{J_N,N}f=f(-2)\).
Their sum is the original \(\phi_N\). In particular the
simple node has one value and no independently prescribed
spectral normal. Formula (20) includes the complete node,
with its original normalization; when angular pole pairs
are treated separately their original orientations and
multiplicities are retained.

Apply the product of (20) over \(S\) to the original source.
Edges disjoint from \(S\), and every other factor independent
of the frozen variables, remain outside this local operation.
Let \(E_S\) denote the edges incident to \(S\). The resulting
incident-edge packet is exactly
\[
 A_{S,N}(\mathbf w)=
 \left(\prod_{v\in S}\mathcal R_{j_v,N}^{(z_v)}\right)
 \left[\prod_{v\in S}R(z_v)^{n_v}
                  \prod_{vw\in E_S}K_N(z_v,z_w)\right],
 \qquad z_v=w_v\quad(v\notin S).
 \tag{20a}
\]
The crossing powers in this formula retain their original
value and first-normal data. Expanding (20a) is a finite
sum of products of:

* values and first or mixed first normals of \(K_N\) on
  edges with both endpoints in \(S\);
* \(F_{j_v}(w)\) or \(G_{j_v}(w)\) on edges from \(v\in S\)
  to a remaining endpoint;
* the original physical crossing values and first normals,
  and the coefficients in (20).

This expansion is literal: each frozen variable is differentiated
at most once, and an internal frozen edge can receive one
derivative at each endpoint.

**Theorem 3.** Allow every frozen vertex to use any physical
node, with no angle buffer or index restriction. Suppose the
remaining traced angles range over a fixed compact
positive-angle family.
On every edge from \(S\) to a remaining traced endpoint,
replace \(G_j\) by (8), leaving \(F_j\) unchanged. Denote the
resulting incident packet by \(\widehat A_{S,N}\).

This packet has exactly the original full mixed physical data
in every remaining traced variable. Its product with the
untouched remainder has the same value under all remaining
original traces, coefficientwise in any retained free
boundary polynomial.

Let \(t_v\) be the actual real physical angle at \(v\in S\)
and the retained complex angle otherwise. For every
\(\epsilon>0\) and every fixed multi-index \(\beta\) in the
remaining spectral variables, there are \(C,M\) such that
\[
 |\partial_{\mathbf w}^{\beta}\widehat A_{S,N}|
 \le C N^M
       \exp N\left\{
          \sum_{vw\in E_S}\Re\psi(t_v,t_w)+\epsilon
                         \right\}.
 \tag{21}
\]
Only the incident-edge packet is bounded in (21).
Untouched edge kernels and their original remaining currents
are not included in this estimate. If their own bounds are
available, (21) can be multiplied with them without altering
the incident-edge action.
If all remaining spectral arguments lie in a compact subset
of \(\Re w<2\), the fixed tolerance in (21) can instead be
replaced by an additional polynomial factor.

If an incident endpoint is genuinely free and untraced,
its \(G_j\) is not replaced. Keep that exact ordinary
free-boundary factor in the packet. The corresponding
bound contains its actual norm and derivatives as an
additional supplied factor instead of an asserted
\(\psi\)-bound. The same convention applies to additional
spectators whose source-specific norms have not been proved.

**Proof.** Proposition 1 applies at every remaining traced
endpoint before it is contracted. Its product assertion
retains all mixed normals, including when several frozen
vertices meet the same remaining vertex. It is immaterial
that the physical colors at different vertices coincide.
The product rule gives the exact statement with all
untouched spectators and free boundary parameters.

For a frozen internal edge, use (19a) for its value and
each possible first or mixed first normal. This retains
the original ordinary derivatives at both endpoints
uniformly even when either spectral argument tends to
\(2\); no fixed slit distance is claimed there.
Equivalently, Proposition 1 identifies a first normal with
\(\widehat G_j(c_k)\) and a mixed normal with
\(\partial_w\widehat G_j(c_k)\), but the uniform bound
at these moving real arguments is supplied by (19a).
If an endpoint is the odd simple node it is never
differentiated, and (19a) includes its value contribution.

Theorem 2 also applies to every edge going to a remaining
traced endpoint and to its fixed derivatives, uniformly
over every frozen row. Use the monotone upper comparison
after (19) to replace its row profile by the action at the
actual physical angle, without an endpoint error.
Allocate a fixed small part of
\(\epsilon\) to each edge in the finite graph. All crossing
values have modulus one at physical nodes; their first
normals are bounded by a fixed power of \(N\), for every
fixed signed power, including zero. The factors in (20)
are bounded. There are only finitely many product-rule
terms, independently of \(N\). Multiplication proves (21).
The stronger half-plane alternative follows from the
last assertion of Theorem 2 and the polynomial bound (19a).

The proof never replaces a factor at an untraced endpoint,
which gives the last assertion. It also proves the
corresponding estimate for fixed spectral derivatives
near the odd simple endpoint by holomorphic spectral
descent, rather than division by \(\sin t\). \(\square\)

For a polynomially sized collection of crossed physical-node
assignments, (21) bounds their sum by the supremum of the
displayed action, with an additional polynomial factor.
For example all assignments on a fixed frozen set have
at most \(N^{|S|}\) members. Actual contour orientations,
any different crossing multiplicities, and the untouched
remaining integrals still belong to the original source.

## 4. Scope for contour transport

This theorem removes a specific local obstacle: crossing an
original physical pole does not force an additional exponential
cost from the independent first normal once the other endpoint
is subsequently traced on a compact positive contour.
The bound keeps the physical angle of that pole rather than
replacing it by the complete-end maximum.

It is a relative-source assertion. The omitted term of (9)
and the change \(Q_0\mapsto\widetilde Q_N\) are not discarded
as separate functions on an arbitrary open current. Their
full physical jets agree before the remaining original
traces are represented by contours. Any later open contour
decomposition must retain its own endpoints and seams.
The logarithmic-factorial representative has poles outside
the original angular window; this argument does not shift
that window across them.

No global deformation, rate for the untouched remaining
kernel product, bound on its joint wire connectors, or
nonzero scalar coefficient follows. In particular a
geometric action decrease along a proposed flow and (21)
still require a source-preserving construction of that
flow and control of its complete remaining boundary.

## Direct sources

The complete texts and their directly used implications were
read at these versions:

* [Physical Jacobi boundary](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_jacobi_charge_boundary.md),
  SHA256 530425b0c4504f2512954438465deb6d9a6e322fa58c641b6c678161baae6583:
  the exact row and normal formulas, determinant normalization,
  source-preserving logarithmic-factorial replacement and its bounds.
* [All-row slit theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_next_first_short_edge_slit_plane_bound.md),
  SHA256 efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b:
  uniform own-row logarithmic asymptotics, stronger half-plane
  error, normalization of the original edge phase and its slit branch.
* [Physical normal lift](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_physical_normal_lift.md),
  SHA256 115c38aa6ce5e683f49f1f9be3a4cc6b2362e451307fe50e5f35c60db10a272d:
  the complete original residue trace, crossing normals and
  odd simple-node convention.
* [Physical charge pressure](research_charged_source_physical_pressure.md),
  SHA256 1e127c0842c0d6d5727a517cc66c39e73baa2846848c284d257c1ebe49679091:
  equations (12) and (20), the uniform real two-row own-action
  upper estimate and complete first/mixed-normal bounds,
  including every physical endpoint regime.

Only written proofs, source-text reads and file hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Frozen notes, manuscripts and public files were unchanged.
