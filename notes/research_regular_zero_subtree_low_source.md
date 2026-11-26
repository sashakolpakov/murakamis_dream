# A nonzero asymptotic for the low-index part of a zero-power subtree

Research note, 2 November 2026. The convex bound for a zero-power subtree
becomes an asymptotic equality for its entire low-index part whenever
the minimizing heights give interior edge maxima. This includes every
selected subtree whose original vertex degrees are at least four. The
high-index part of the original source remains outside the theorem.

For the full source, including the nonregular edge configurations, see
[the Newton-coordinate theorem](research_all_zero_subtree_newton_packet.md).
The present calculation gives an independent contour derivation on the
regular region; the two holomorphic phases and amplitudes agree there.

## 1. Statement and notation

Use the finite tree \(T\), selected connected proper subtree \(S\),
original degrees \(d_v\), edge set \(E_S\), source \(Z_{S,N}\),
and low-index source \(Z^{\mathrm{low}}_{S,N}\) defined in
[Sections 1 and 5 of the convex-potential note](research_zero_power_subtree_convex_potential.md).
An index is low when \(2a<N\). All selected powers are zero, and all
original selected degrees are at least three. Write
\[
 k=|S|,\qquad m=|E_S|,\qquad b=|\partial S|.
\]
Since \(S\) is a subtree, \(m=k-1+b\). The \(b\) boundary
angles \(\mathbf u=(u_e)_{e\in\partial S}\) remain independent.

Let \(\mathbf h_*\) be the unique minimizer of
\[
 \mathcal L_S(\mathbf h)
 =\sum_{vw\in E_S}V(h_v,h_w)-\sum_{v\in S}h_v,
 \qquad h_w=0\quad(w\notin S),
 \tag{1}
\]
where \(V\) is the maximized real edge phase. Assume
\[
 \sinh(h_v/2)\sinh(h_w/2)<1
                       \qquad(vw\subset S)
 \tag{2}
\]
at this minimizer. Every edge then has a unique maximizing index
\(x_e\in(0,1/2)\). A sufficient condition for (2) is
\[
 \tan(\pi/d_v)\tan(\pi/d_w)\le1
                        \qquad(vw\subset S).
 \tag{3}
\]
In particular, all selected degrees at least four suffice. For a
singleton, (2) has no internal edges to check and holds automatically.

Continue the original edge phase \(\psi(t,u)\) along
\((t,u)=(-i\lambda h_v,-i\lambda h_w)\), \(0\le\lambda\le1\),
using the positive real critical value of its real index integral.
Condition (2) stays strict along this segment. For an edge leaving
\(S\), the outside angle is zero during this continuation. Near
\((\mathbf t,\mathbf u)=(-i\mathbf h_*,\mathbf0)\), set
\[
 F(\mathbf t,\mathbf u)
 =\sum_{vw\subset S}\psi(t_v,t_w)
  +\sum_{\substack{e=vw\in\partial S\\v\in S}}
                                     \psi(t_v,u_e)
  -i\sum_{v\in S}t_v.
 \tag{4}
\]
The selected stationary point \(\mathbf t(\mathbf u)\) is the
holomorphic solution of \(F_{\mathbf t}=0\) with
\(\mathbf t(\mathbf0)=-i\mathbf h_*\). Define
\[
 W(\mathbf u)=F(\mathbf t(\mathbf u),\mathbf u),
 \qquad M=W(\mathbf0)=\mathcal L_S(\mathbf h_*).
 \tag{5}
\]

**Theorem.** Under (2), there is a fixed complex polydisk about
\(\mathbf u=0\) on which
\[
 Z^{\mathrm{low}}_{S,N}(\mathbf u)
 =N^{-3(b-1)/2}A(\mathbf u)e^{NW(\mathbf u)}
                  (1+O(N^{-1})),
 \tag{6}
\]
uniformly and holomorphically, along both parities of \(N\).
The function \(A\) is holomorphic and nonzero after shrinking the
polydisk. At zero it is strictly positive. The stationary boundary
Hessian is diagonal:
\[
 W_{u_eu_f}(\mathbf0)=
 -\delta_{ef}\frac{\cosh(h_{v(e)}/2)}{2\pi},
 \tag{7}
\]
where \(v(e)\) is the selected endpoint of the boundary edge.
There are constants \(c,C,\varepsilon>0\) and \(a\), depending
on the fixed subtree, such that
\[
 |Z^{\mathrm{low}}_{S,N}(\mathbf u)|
 \le C N^a
 \exp N\left[M-c\sum_{e\in\partial S}
                (1-\cos\operatorname{Re}u_e)
            +C\sum_{e\in\partial S}
                (\operatorname{Im}u_e)^2\right]
 \tag{8}
\]
for \(|\operatorname{Im}u_e|<\varepsilon\).

The theorem concerns the original trace of the low-index part, not a
trace with only its first Fourier charge retained by definition. The
proof estimates all the other charges. It does not assert (6) for
the full source \(Z_{S,N}\).

## 2. Removing low indices away from their real maxima

Choose a closed interval \(I_e\subset(0,1/2)\) containing
\(x_e\) in its interior for each edge. Retain the corresponding
finite kernels
\[
 K_{N,I_e}(t,u)=\sum_{a/N\in I_e}
                      e_a(-2\cos t)e_a(-2\cos u).
 \tag{9}
\]
Their product followed by the original selected traces will be denoted
by \(Z^I_{S,N}\).

The exact positive Fourier bound in
[Sections 3–4 of the Fourier note](research_zero_power_subtree_fourier_bound.md)
applies to any subset of low-index assignments. At the fixed heights
\(\mathbf h_*\), its real index phase is a sum of independent
strictly concave edge phases. The complement of
\(\prod_e\operatorname{int}I_e\) is compact and avoids the unique
maximizing vector. Therefore some \(\delta>0\) satisfies
\[
 \sup_{\mathbf u\text{ real}}
 |Z^{\mathrm{low}}_{S,N}(\mathbf u)-Z^I_{S,N}(\mathbf u)|
 \le C N^a e^{N(M-\delta)}.
 \tag{10}
\]
This is an estimate after all the original traces, including their
double-root derivatives and every Fourier charge. It does not use a
coarse bound before tracing. Each boundary spectral degree is at most
\(N-1\). Polynomial continuation therefore preserves a strict gap
in (10) on a sufficiently small complex boundary polydisk.

## 3. The local edge expansion at two imaginary angles

For one edge, let \(h,g\) be its minimizing heights, one of which
is zero on a boundary edge. The base point is
\((t_0,u_0)=(-ih,-ig)\). The retained real index phase is
\[
 Q(x;t,u)=b(x,t)+b(x,u),\qquad
 b(x,t)=\int_0^x\log(2\cos2\pi s+2\cos t)\,ds-2J(x).
 \tag{11}
\]
At the base point the logarithms are real, its maximum is the interior
point \(x_e\), and \(Q_{xx}(x_e;t_0,u_0)<0\).
The logarithms and their derivatives are holomorphic on a fixed small
complex neighborhood of the retained real index interval. In the
factorial interpolation the real parts of the midpoint arguments are
\(1/2-x>0\), and the unshifted index arguments have real parts
\(x>0\). They stay separated from their poles on this neighborhood.

The uniform factorial expansion gives the local summand
\[
 e_a(-2\cos t)e_a(-2\cos u)
 =\frac{e^{NQ(x;t,u)}}{4N^2\sin^2\pi x}
                       (1+O(N^{-1})),\qquad x=a/N.
 \tag{12}
\]
The complete finite sum has the corresponding holomorphic saddle
expansion
\[
 K_{N,I_e}(t,u)
 =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),
 \tag{13}
\]
\[
 a_e(t,u)=
 \frac{\sqrt{2\pi}}
      {4\sin^2(\pi x_e(t,u))
             \sqrt{-Q_{xx}(x_e(t,u);t,u)}}.
 \tag{14}
\]
The square root is positive at the imaginary base point, and
\(a_e(t_0,u_0)>0\).

Here are the estimates needed to justify (13) for the discrete sum.
Use the exact cotangent rectangle enclosing the retained integer
indices, with half-grid vertical sides and fixed small horizontal
index heights \(\pm\epsilon\). Strict real concavity gives a
positive gap at the two real endpoints. Choose \(\epsilon\) small
enough that their vertical sides retain that gap. On the horizontal
sides the real phase can exceed its real stationary value by only
\(O(\epsilon^2)\); take this smaller than \(\pi\epsilon\).
The nonconstant cotangent modes have decay
\(e^{-2\pi N\epsilon}\), so they remain exponentially smaller.
The constant modes give \(N\) times the index integral. Deform that
integral through its unique holomorphic critical point, keeping the
endpoint connectors in their fixed gap, and use the strict negative
real second derivative for its Gaussian expansion. All these gaps
persist after a sufficiently small complex perturbation of \((t,u)\).
The half-grid endpoints differ from the fixed endpoints by
\(O(N^{-1})\), within the same larger regular rectangle. This proves
the uniform relative error and the holomorphic assertion in (13).
The argument is the two-height version of
[Section 4 of the isolated zero-power proof](research_zero_power_internal_boundary_theorem.md#4-the-local-edge-expansion-at-the-deeper-imaginary-angle).

## 4. The full product contour and its unique maximum

For any separately even polynomial \(f(\mathbf t)\), the exact
zero-power trace is the product of the one-variable identities
\[
 \phi_N^{(v)}f=
 -\frac{N^2}{\pi i}
 \int_{-\pi-ih_v}^{\pi-ih_v}
 \sin t_v\,f\,
 \frac{e^{-iNt_v}}{(1-\eta e^{-iNt_v})^2}\,dt_v,
 \qquad \eta=(-1)^{N-1}.
 \tag{15}
\]
The opposite vertical sides cancel by \(2\pi\)-periodicity.
Equivalently, the original vertical current is odd in its height
coordinate. This holds with all other variables fixed at arbitrary
complex values. Applying (15) successively therefore gives exactly
the product of lower-circle integrals, with no remaining boundary
faces. There is no degree restriction on \(f\) in this identity.

Positive Laurent coefficients give a strict angular estimate on these
lower circles. For \(a/N=x\in I_e\) and fixed \(h>0\),
\[
 |e_a(-2\cos(\tau-ih))|
 \le C N^a e_a(-2\cosh h)
 \exp\left[-N\frac{\sin2\pi x}{2\pi(\cosh h+1)}
                             (1-\cos\tau)\right].
 \tag{16}
\]
For a real boundary angle the corresponding bound is
\[
 |e_a(-2\cos u)|
 \le C N^a e_a(-2)
 \exp\left[-N\frac{\sin2\pi x}{4\pi}(1-\cos u)\right].
 \tag{17}
\]
Both follow by comparing the midpoint product with its logarithmic
potential; their endpoint-uniform derivation is in
[Section 2 of the isolated zero-power proof](research_zero_power_internal_boundary_theorem.md).
The constants in (16) and (17) have a positive minimum on every
\(I_e\). Since the base summands are positive, these inequalities
may be summed in each retained kernel and then multiplied over the
edges. Every selected angle occurs in at least one edge, and every
boundary angle occurs in its boundary edge. Thus the full retained
integrand has the upper rate
\[
 M-c\sum_{v\in S}(1-\cos\tau_v)
       -c\sum_{e\in\partial S}(1-\cos u_e)
 \tag{18}
\]
for some \(c>0\), uniformly on all real circles.

In (15), on the chosen lower circle,
\[
 \frac{e^{-iNt_v}}{(1-\eta e^{-iNt_v})^2}
 =e^{-iNt_v}(1+O(e^{-Nh_v})).
 \tag{19}
\]
All selected heights are positive. The error in replacing the product
of these exact factors by its unit-charge term has a fixed exponential
gap, by (18). At zero boundary angles, (18) also shows that
\(\boldsymbol\tau=0\) is the only possible contributing maximum;
all other closed regions have a strict gap.

The selected Hessian of (4) at that point is
\[
 F_{\mathbf t\mathbf t}(-i\mathbf h_*,\mathbf0)
                =-H,\qquad
 H=\nabla^2\mathcal L_S(\mathbf h_*)>0.
 \tag{20}
\]
The full positive definite matrix in (20), including its off-diagonal
entries from shared edges, was computed in Section 3 of the convex
note. Thus the implicit function theorem gives \(\mathbf t(\mathbf u)\),
and the multidimensional Gaussian expansion applies at zero. For small
complex boundary angles, deform the local contour through this
holomorphic stationary point. The remaining faces retain the strict
gap in (18), and all selected depths stay positive, so no pole of the
exact rational trace is crossed. The relative expansion is therefore
uniform and holomorphic.

## 5. The coefficient, boundary estimate, and limitation

Combining (13), (15), and the \(k\)-dimensional Gaussian gives
\[
 A(\mathbf u)=
 \left(i\sqrt{\frac2\pi}\right)^k
 \frac{\prod_{v\in S}\sin t_v(\mathbf u)
       \prod_{e\in E_S}a_e}
      {\sqrt{\det(-F_{\mathbf t\mathbf t})}},
 \tag{21}
\]
with each edge amplitude evaluated at its selected or boundary angles.
The square root continues its positive real value at zero. In
particular,
\[
 A(\mathbf0)=
 \left(\frac2\pi\right)^{k/2}
 \frac{\prod_{v\in S}\sinh h_v
       \prod_{e\in E_S}a_e(-ih_v,-ih_w)}{\sqrt{\det H}}>0.
 \tag{22}
\]
The powers of \(N\) are \(N^{2k}\) from the exact traces,
\(N^{-3m/2}\) from the edge sums, and \(N^{-k/2}\) from the
selected Gaussian. Their product is
\[
 N^{3k/2-3m/2}=N^{-3(b-1)/2}.
 \tag{23}
\]
The omitted low-index part in (10) is exponentially smaller, so it
does not change (6) or (22).

Separate evenness in every outside angle gives
\(\partial\mathbf t/\partial u_e(\mathbf0)=0\).
The original edge identity
\(\psi_{uu}(t,0)=-\cos(t/2)/(2\pi)\) then gives exactly (7).
For real boundary angles, (18) gives the claimed angular loss for the
retained contribution. Decrease its constant so that the uniform gap
in (10) absorbs the omitted terms as well; the total angular sum is
bounded by \(2b\). This proves (8) on the real torus.

Near a complete real boundary point, (6) and the negative real Hessian
(7) give (8) on a small complex neighborhood, with quadratic dependence
on the imaginary angles. On the compact real complement of these
neighborhoods there is a fixed angular gap. A polynomial continuation
estimate on finitely many products of real spectral intervals preserves
half of that gap on a sufficiently thin complex strip, since each
boundary degree is at most \(N-1\). Decreasing the angular constant
again gives (8) on that complement. Periodicity joins the neighborhoods
into the stated strip. This completes the theorem.

At complete outside angles every full-source index assignment is
nonnegative: the Newton quotient structure constants and the selected
traces are nonnegative, and \(e_a(-2)\ge0\) for all indices. At odd
levels some of the high-index values vanish. Hence
\[
 Z_{S,N}(\mathbf0)\ge Z^{\mathrm{low}}_{S,N}(\mathbf0),
 \qquad
 \liminf_{N\to\infty}\frac1N\log Z_{S,N}(\mathbf0)\ge M.
 \tag{24}
\]
This lower bound does not determine the full-source exponential rate.
The high-index matching terms might be larger, and the present proof
does not compare them with \(M\). Nor does it identify \(2\pi M\)
with an absolute hyperbolic volume for the coupled subtree. Those two
questions must be settled before the theorem can replace the whole-source
input in the further-filling argument.
