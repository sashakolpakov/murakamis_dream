# The original trace on a path with large signed powers

Research note, 3 November 2026.

For every fixed finite positive path with crossing powers at least
twenty, all the mixed vertical terms of a central trace rectangle
have a strict gap below the selected geometric action. The gap
comes from one inequality at each vertex where a vertical term
occurs. Its constants do not depend on the length of the path.

Sections 4--6 compare every complementary original row and every
mixed current with the selected action when the signed powers have
absolute value at least sixty-four. The
[full thin-box kernel theorem](research_bare_kernel_thin_rectangle.md)
supplies the required uniform bound and nonzero expansion.
Section 7 retains one outside angle and proves its whole-period and
complex-strip estimates. Sections 8--9 give the stronger local
comparisons used for powers seven and eight in the
[full path-source theorem](research_uniform_path_trace_assembly.md#7-the-source-theorem-at-powers-seven-and-eight).
The proved wide-kernel bound now supplies their finite-source input.

## 1. The phase and the selected point

Let \(I\) be the selected vertices of an original finite circle
path. Complete outside endpoints, when present, have angle zero.
Write \(d_v\in\{1,2\}\) for each selected vertex's original degree,
including incidences to those outside endpoints. Put
\[
 \Psi(\mathbf t)=\sum_{\{v,w\}\in E}\psi(t_v,t_w),\qquad
 \Phi(\mathbf t)=\Psi(\mathbf t)+
       \sum_{v\in I}\left(\frac{i n_vt_v^2}{4\pi}-it_v\right),
 \tag{1}
\]
where \(\psi\) is the original complete edge phase. Every
\(n_v\) is an integer at least twenty. The selected geometric
critical point is denoted by
\[
 t_v^*=\theta_v-iH_v,\qquad
 \mathcal M=\Re\Phi(\mathbf t^*).
 \tag{2}
\]
The [edge-response theorem](research_edge_hessian_and_phase_response.md),
Section 7, proves
\[
 0<\theta_v<\frac{7\pi}{3n_v},\qquad
 0<H_v<\frac{21d_v}{16n_v}<\frac13 .
 \tag{3}
\]
It also proves, throughout
\(\mathcal B=\{t:|\Re t|\le1,\ |\Im t|\le1/3\}\),
\[
 K(t,u)=-2\pi\psi''(t,u),\qquad
                  \Re K(t,u)\succeq\frac15 I .
 \tag{4}
\]
Here and below real parts of complex symmetric matrices mean
their entrywise real parts, which are their Hermitian parts.

There is a useful upper bound on the same box:
\[
                         \|K(t,u)\|_2<2.
 \tag{5}
\]
Indeed, with \(w=\tan(t/2)\), \(z=\tan(u/2)\), and
\(s=\sqrt{1+w^2+z^2}\), the exact matrix is
\[
 K=\frac1s
       \begin{pmatrix}1+w^2&-wz\\-wz&1+z^2\end{pmatrix}.
 \]
The bounds already proved on \(\mathcal B\) give
\(|w|,|z|<3/5\) and \(\Re(s^2)>7/8\).
Its absolute row and column sums are less than
\((43/25)/\sqrt{7/8}<2\), proving (5).

## 2. Every mixed face is below the same critical value

Fix \(T=19/20\). For a nonempty subset \(S\subseteq I\),
consider the following product of segments:
\[
 \begin{cases}
 t_v=x_v-iH_v,\quad -T\le x_v\le T,&v\notin S,\\
 t_v=T+ih_v,\quad -H_v\le h_v\le H_v,&v\in S.
 \end{cases}
 \tag{6}
\]
The vertices in \(S\) are those at which the vertical term
of the exact trace identity is used. Its exponential modulus,
including its trace kernels, is
\[
 \mathcal E_S(\mathbf t)=
 \Re\!\left(\Psi(\mathbf t)+
                   \sum_v\frac{i n_vt_v^2}{4\pi}\right)
       -\sum_{v\notin S}H_v-\sum_{v\in S}|h_v|.
 \tag{7}
\]

**Theorem 1.** For every subset \(S\) and every point of (6),
\[
                    \mathcal E_S(\mathbf t)
                       \le\mathcal M-\frac{|S|}{400}.
 \tag{8}
\]
In particular this estimate applies simultaneously to all
nonempty mixed-current subsets of an arbitrarily long fixed
path. The powers may have unrelated magnitudes.

**Proof.** First, \(\mathcal E_S\le\Re\Phi\). At a horizontal
vertex the charge term \(\Re(-it_v)=-H_v\) is precisely the
term in (7). At a vertical vertex it is \(h_v\), which is
at least \(-|h_v|\).

Write
\[
 \mathbf t-\mathbf t^*=\mathbf a+i\mathbf b.
 \]
Then \(b_v=0\) outside \(S\), while on \(S\)
\[
 a_v=T-\theta_v>\frac7{12},\qquad
 0\le b_v=h_v+H_v\le2H_v.
 \tag{9}
\]
The first inequality follows from (3), \(n_v\ge20\),
and \(\pi<22/7\).
The segment from \(\mathbf t^*\) to \(\mathbf t\)
stays in the convex box \(\mathcal B^I\).

Let \(K_G\) be the sum of the edge matrices embedded
in the selected vertex coordinates. Define its weighted
average along that segment by
\[
 \overline K_G=
   2\int_0^1(1-s)K_G(\mathbf t^*+
                           s(\mathbf a+i\mathbf b))\,ds
       =A+iB .
 \tag{10}
\]
Extend all vectors by zero at complete outside endpoints.
Equations (4)--(5) imply, with
\(A_2=\sum_vd_va_v^2\) and \(B_2=\sum_vd_vb_v^2\),
\[
 a^TAa\ge A_2/5,\qquad
 |b^TAb|\le2B_2,\qquad
 |a^TBb|\le2\sqrt{A_2B_2}.
 \tag{11}
\]
The last bound follows first on each edge and then
from Cauchy--Schwarz over edges. These inequalities
therefore have no factor depending on path length.

Taylor's formula at the full complex critical point,
with the quadratic filling term kept exactly, gives
\[
 \Re\Phi(\mathbf t)-\mathcal M
 =-\frac1{4\pi}
      \bigl(a^TAa-b^TAb-2a^TBb\bigr)
       -\frac1{2\pi}\sum_vn_va_vb_v.
 \tag{12}
\]
The elementary inequality
\(4\sqrt{A_2B_2}\le A_2/10+40B_2\)
now yields
\[
 \Re\Phi(\mathbf t)-\mathcal M
 \le-\frac{A_2}{40\pi}
       +\frac{42B_2}{4\pi}
       -\frac1{2\pi}\sum_{v\in S}n_va_vb_v.
 \tag{13}
\]
The last term has the favorable sign because the vertical
side in (6) is the positive real side of the rectangle.

For \(v\in S\), (3) and \(d_v\le2\) give
\[
 n_va_v\ge\frac{19n_v}{20}-\frac{7\pi}{3},
 \qquad 42b_v<\frac{441}{2n_v}.
 \]
For every \(n\ge20\),
\[
 \frac{19n^2}{20}-\frac{7\pi n}{3}-\frac{441}{2}>0.
 \tag{14}
\]
For a rational verification, replace \(7\pi/3\) by
\(22/3\). The resulting expression equals \(77/6>0\)
at \(n=20\) and increases thereafter. Thus
\(n_va_v\ge42b_v\ge21d_vb_v\).
The last two terms of (13) consequently have nonpositive
sum. Using (9),
\[
 \Re\Phi(\mathbf t)
 \le\mathcal M-\frac1{40\pi}
                  \sum_{v\in S}d_v(T-\theta_v)^2
 <\mathcal M-\frac{|S|}{400}.
 \]
Indeed \(49/(5760\pi)>1/400\), for example by
\(\pi<22/7\). This proves (8). \(\square\)

The same argument works with midpoint cutoffs
\(T_N\le T\) and \(T_N=T+O(N^{-1})\), giving a gap \( |S|/401\) for all
sufficiently large levels. This weakened constant is
only to absorb the finite-grid rounding.

## 3. Why these are the actual Hermite currents

Put \(\eta=(-1)^{N-1}\) and retain the original crossing
unit \(C_{N,n}\) from the
[exact complete trace formula](research_exact_complete_trace_contour.md).
Choose \(T_N\) to be the largest midpoint between consecutive
physical angles that is no greater than \(T\).
Then \(T_N\le T\), \(0\le T-T_N<2\pi/N\), and
\(e^{iNT_N}=-\eta\).
For an even polynomial spectator \(f(t)\), the retained
trace is exactly
\[
 \begin{split}
 \mathcal D_{n,N}^{T_N}[f]
 ={}&-\frac{N^2C_{N,n}}{\pi i}
  \int_{-T_N-iH}^{T_N-iH}
     \sin t\,f(t)e^{inNt^2/(4\pi)}
       \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
  \int_{-H}^{H}
     \frac{\sin(T_N+ih)\,f(T_N+ih)
                  e^{inN(T_N+ih)^2/(4\pi)}}
          {4\cosh^2(Nh/2)}\,dh .
 \end{split}
 \tag{15}
\]
The original value and first derivative at every retained
double root, and the simple odd-level root, are all included.
The two vertical sides have already been combined into the
positive real side in the second line. This uses the
spectator's evenness, not a change of the source.

Apply (15) at every selected vertex to the exact product
of original edge kernels
\[
                         \prod_{\{v,w\}\in E}K_N(t_v,t_w).
 \tag{16}
\]
Each kernel is even in each angle, so the identity remains
applicable when other variables have already been moved.
The expansion has one term for every subset \(S\subseteq I\),
with exactly the domains (6). It introduces no independent
edge variables and no missing derivatives at shared edges.

The horizontal rational kernel has modulus bounded by
a fixed multiple of \(e^{-NH_v}\), and its leading term
is \(e^{-iNt_v}\). The vertical factor obeys exactly
\[
                   \frac1{4\cosh^2(Nh_v/2)}
                           \le e^{-N|h_v|}.
 \tag{17}
\]
Thus (7) is precisely the exponential upper functional
for these terms, provided the edge kernels obey
\[
 |K_N(t,u)|\le C N^A e^{N\Re\psi(t,u)}
                  \quad\text{uniformly on }\mathcal B^2.
 \tag{18}
\]
Under (18), Theorem 1 makes every nonempty mixed term
exponentially smaller than the selected contribution,
at all level parities. Their number \(2^{|I|}-1\) is
fixed before \(N\to\infty\).

For the empty subset, (4) gives strict horizontal
concavity on the entire retained rectangle and its
unique maximum at \(\mathbf t^*\). The summed higher
Fourier charges are smaller by
\(\exp(-N\min_v H_v)\). A uniform nonzero kernel
asymptotic near that saddle, together with (18), then
gives a nonzero Gaussian coefficient for the retained
trace. No separate charge-by-charge certificate is
needed.

## 4. A centered bound for the original complementary rows

Write \(e_j(t)=e_j(-2\cos t)\) in this section, and keep
all \(0\le j<N\) in the original kernel
\(K_N(t,u)=\sum_j e_j(t)e_j(u)\).
Set \(\gamma=1/200\) and
\[
 \Omega=\{z:|\Re z|\le19/20,\ |\Im z|\le1/200\}.
 \tag{19}
\]

**Lemma 2.** Uniformly for \(z\in\Omega\) and real
\(9/10\le|u|\le\pi\),
\[
 |K_N(u,z)|
       \le C N^A
          e^{N[\Re\psi(0,z)-\gamma(1-\cos u)]}.
 \tag{20}
\]
For two real angles one also has
\[
 |K_N(u,v)|\le C N^A
       e^{N[M_\infty-\gamma(1-\cos u)-\gamma(1-\cos v)]},
 \qquad M_\infty=\psi(0,0).
 \tag{21}
\]
The first derivative in either removed spectral variable,
or the mixed first derivative in both, obeys the same
bounds at polynomial cost if each angular loss is
replaced by the constant \(\gamma(1-\cos(9/10))\)
and the removed angles satisfy \(|u|,|v|\ge9/10\).

**Proof of (20).** We separate the original wire indices
into \(j/N\in[1/8,1/3]\), the rest of the lower half,
and the upper half. This separation is only an estimate
of the exact kernel.

For a central index and \(|r|\le19/20\), every factor
of \(e_j(r)\) is positive. Its exact logarithmic second
derivative is
\[
 -\partial_z^2\log e_j(z)
 =\frac14\sum_{\nu<j}
  \left[
   \sec^2\!\left(\frac{(2\nu+1)\pi/N+z}{2}\right)
  +\sec^2\!\left(\frac{(2\nu+1)\pi/N-z}{2}\right)
  \right].
 \tag{22}
\]
On a vertical line the modulus of each squared secant
is no larger than its value at real part \(r\).
The sum at real part \(r\) is a midpoint sum of a convex
function. Hence its value is at most
\[
 \frac N{4\pi}
   \left[\tan\!\left(\frac{\pi j}{N}+\frac r2\right)
        +\tan\!\left(\frac{\pi j}{N}-\frac r2\right)\right].
 \]
The bracket increases with \(j/N\) and \(|r|\).
At \(j/N=1/3,\ |r|=19/20\), its first tangent is
\(\cot(\pi/6-19/40)<21\) and its second is less than
one. Integrating (22) twice vertically, with zero
initial real derivative, proves the finite inequality
\[
                |e_j(r+ih)|\le e_j(r)e^{Nh^2}.
 \tag{23}
\]
For example \(\pi>157/50\) proves the cotangent bound;
the resulting coefficient \(22/(8\pi)\) is less than one.

The [real Newton estimate](research_three_crossing_real_period_newton_bound.md)
gives, uniformly on this central wire,
\[
 |e_j(u)|\le C N^A e_j(0)
                 e^{-N(1-\cos u)/20}.
 \tag{24}
\]
Indeed the coefficient there is at least
\(\sin(\pi/4)/(4\pi)>1/20\).
Put \(A_r(y)=V_0(y)+V_r(y)\), with the real Newton
entropy \(V_r\) defined in that note.
Its maximum on the lower half is attained uniquely at
\[
 y_*(r)=\frac1{2\pi}
          \arccos\!\frac{1-\cos r}{3+\cos r},
 \qquad \frac15<y_*(r)\le\frac14,
 \tag{25}
\]
and equals the original edge phase \(\psi(0,r)\).
The latter identity is the real stationary formula in
the original edge calculation; its value at \(r=0\)
is \(M_\infty\), fixing the additive constant.
Uniform logarithmic factorial errors therefore bound
the positive central sum \(\sum e_j(0)e_j(r)\) by
\(C N^A e^{N\psi(0,r)}\).

The phase is real on the real square. From (4),
its real part increases vertically from \(r\):
\(\Re\psi(0,r+ih)\ge\psi(0,r)\).
Equations (23)--(24) thus bound the central contribution
by
\[
 C N^A e^{N[\Re\psi(0,z)+h^2-(1-\cos u)/20]}.
 \]
Since \(h^2\le1/40000\) and
\(1-\cos u\ge1-\cos(9/10)>1/3\), this is smaller
than the bound (20).

Here are uniform bounds for the other wire indices.
The same midpoint argument used for real logarithmic
zeros gives
\[
 |e_j(r+ih)|\le C N^A e^{N V_{r,h}(j/N)},\qquad
                  V_{r,h}(y)\le V_r(y)+|h|.
 \tag{26}
\]
To verify the second inequality directly, factor the
numerator integrand as
\[
 2\cos(2\pi x)+2\cos(r+ih)
 =4\cos(\pi x+(r+ih)/2)\cos(\pi x-(r+ih)/2).
 \]
In each cosine, introducing the imaginary part increases
its modulus. The increase in the logarithmic integral
over a full period in \(x\) is \(|h|/2\) for each
factor, by the elementary logarithmic mean of
\(a+be^{2\pi ix}\). The increase over a partial interval
is nonnegative and no larger than the sum \(|h|\).
For the first inequality, omit the bounded number of
mesh cells meeting a real cosine zero. On the remaining
cells the logarithmic derivative has the same harmonic
sum bound as for a real zero. In a removed cell,
\(\log|\cos(a+ih/2)|\) has upper sampling error \(O(1)\),
uniformly down to \(h=0\); an exact sampled zero only
improves an upper bound. The total numerator error is
uniform because, when \(|h|\le N^{-1}\), the sampled
logarithm on such a cell is at most \(\log(C/N)\),
while its integral average is at least \(-\log N-C\).
When \(|h|>N^{-1}\), the variation across that cell is
at most \(C/(N|h|)\le C\).
The total numerator error is
therefore \(O(\log N)\), uniformly in all the parameters
in (19). The sine denominator has the established
uniform error of the same order. This proves (26).

On \(0<y<1/2-|r|/(2\pi)\), one has
\(A_r''(y)\le V_0''(y)\le-4\pi\).
The interval from (25) to either \(1/8\) or \(1/3\)
lies in this range, because \(19/20<\pi/3\).
Also \(A_r\) decreases on \([1/4,1/2]\), including
across its logarithmic derivative singularity.
Consequently
\[
 \sup_{y\in[0,1/2]\setminus(1/8,1/3)}
           A_r(y)
       \le\psi(0,r)-\delta,\qquad
                         \delta=\frac{9\pi}{800}.
 \tag{27}
\]
At the lower endpoint the distance to the saddle
exceeds \(3/40\); at the upper endpoint it is at least
\(1/12\). These distances and the second-derivative
bound give (27).
For any real \(u\), \(V_u(y)\le V_0(y)\) on the
lower half. Thus (26)--(27) bound its omitted part
by \(C N^A e^{N[\psi(0,r)-\delta+|h|]}\).
Since \(\delta-|h|>1/100\), this proves (20) for
that part as well.

On the upper half, both \(V_u\) and \(V_r\) are
nonpositive, so (26) bounds the entire contribution
by \(C N^A e^{N|h|}\).
On the other hand \(\psi(0,r)>5/6\): use
\(M_\infty>1\), \(|K|<2\), and integrate twice
along the real interval of length less than one.
This makes the upper half exponentially smaller
than (20), finishing its proof.

For (21), first retain the original wire
\([1/5,3/10]\). The same real angular inequality
used in (24), applied to both factors, bounds this
part by
\(C N^A e^{N[M_\infty-((1-\cos u)+(1-\cos v))/20]}\).
The established full omitted-wire estimate has rate
at most \(M_\infty-\pi/100\), uniformly on the real
square. Since
\(\gamma[(1-\cos u)+(1-\cos v)]\le4\gamma=1/50\),
it satisfies (21) too.

Finally apply the polynomial Markov inequality in
each removed variable \(z=-2\cos u\) on the fixed
interval \([-2\cos(9/10),2]\).
The supremum bounds just proved are uniform in the
remaining complex variable. Each derivative costs
only \(C N^2\); applying it in both variables gives
the mixed bound. Complex coefficients are allowed
by rotating the derivative at the evaluation point
and applying the real inequality to its real part.
No endpoint or original first normal is excluded.
\(\square\)

## 5. Every complementary-row subset has a local action budget

Assume now \(n_v\ge64\). For \(S\subseteq I\), let
\(\lambda_v=0\) on \(S\), and \(\lambda_v=1\) elsewhere.
The [partial-charge theorem](research_positive_path_partial_charge_bounds.md)
gives its stationary point with \(t_v=0\) exactly on
\(S\), and
\[
 |t_v^*(\lambda)|\le
       \frac{2\pi}{n_v-2d_v/5}<\frac1{10},\qquad
 H_v(\lambda)\le C_v<\frac1{200},
 \quad
 C_v=\frac{14\pi d_v/5}
       {(n_v-2d_v/5)^2+(7d_v/5)^2}.
 \tag{28}
\]
The same theorem bounds its real stationary action by
\[
 0\le\mathcal M(\lambda)-\mathcal M(\mathbf1)
       \le\frac12\sum_{v\in S}C_v
       <\frac1{800}\sum_{v\in S}d_v .
 \tag{29}
\]
For the last rational inequality drop the positive
\((7d_v/5)^2\) term in the denominator, use \(n_v\ge64\),
\(d_v\le2\), and
\(C_v/(2d_v)\le35\pi/99856<1/800\).

Expand the original finite trace according to the
vertices whose physical angles lie outside
\((-T_N,T_N)\). Fix a nonempty such set \(S\).
Keep those original grid rows and their first normals.
At every other vertex use (15), with the selected
height from the partial-charge solution (28).
Every remaining angle lies in \(\Omega\).

On an edge between \(S\) and its complement, (20)
replaces the edge's modulus by the phase
\(\Re\psi(0,t_w)\) and an angular loss at its removed
endpoint. On an edge inside \(S\), (21) gives
\(\psi(0,0)\) and a loss at both endpoints.
The last assertion of Lemma 2 preserves these
estimates for every derivative contributed by the
original removed rows. Crossing values have modulus
one at those rows; their first normals and the
finite trace factors cost only fixed powers of \(N\).

Thus, after these bounds, the remaining phase is
exactly the original phase with the vertices in
\(S\) fixed at zero. The surviving components are
paths with the same degrees, now including their
zero-angle boundary incidences. Theorem 1 applies
component by component to every retained mixed
current. In particular their integrals have upper
rate at most \(\mathcal M(\lambda)\).

The total loss from the removed endpoints is at least
\[
 \gamma(1-\cos(9/10))\sum_{v\in S}d_v
                    >\frac1{600}\sum_{v\in S}d_v .
 \tag{30}
\]
Combining (29)--(30) proves a gap greater than
\[
                         \frac1{2400}\sum_{v\in S}d_v
 \tag{31}
\]
below the full selected action. This is independent
of the number of other selected vertices.
The finitely many grid sums and contour subsets have
only polynomial costs for each fixed path.

The full thin-box kernel theorem proves the required
uniform upper bound on the surviving thin contours,
\[
 |K_N(t,u)|\le C N^A e^{N\Re\psi(t,u)},\qquad
 |\Re t|,|\Re u|\le1,\quad
 |\Im t|,|\Im u|\le1/200.
 \tag{32}
\]
It does not require (18) on the larger-height box.
Thus (31) controls every complementary-row subset of
the original whole trace. The same kernel theorem gives
its uniform nonzero local expansion at the selected
saddle, so Section 3 supplies the surviving nonzero
Gaussian term. This uses a single uniform kernel theorem
and the local action budgets above for every fixed
path length.

## 6. Signed retained currents, including a scalar closure

Corollary 3 of
[the partial-charge theorem](research_positive_path_partial_charge_bounds.md)
constructs the original positive geometric solution for
any selected set of a nontrivial circle path, including
all auxiliary vertices, when \(|n_v|\ge8\). It retains
every original carrier and primitive filling coefficient.
For the current estimate we use the more conservative
threshold \(|n_v|\ge64\).

Put \(\sigma_v=\operatorname{sgn}(n_v)\). At the selected
unit-charge point,
\[
 \operatorname{sgn}(\theta_v)=\sigma_v,\qquad
                |\theta_v|<1/10,\qquad 0<H_v<1/200.
 \tag{33}
\]
For a current subset \(S\), use the unchanged lower
horizontal segment at every vertex outside \(S\), and
the vertical segment
\[
               t_v=\sigma_vT+ih_v,\qquad
               -H_v\le h_v\le H_v,\qquad T=19/20
 \tag{34}
\]
at every vertex in \(S\).

**Corollary 3.** For these domains the exponential upper
functional (7) satisfies
\[
                  \mathcal E_S\le\mathcal M-|S|/400
 \tag{35}
\]
for every nonempty subset \(S\), with no restriction on
the signs or relative magnitudes of the powers.
No complete outside endpoint is required.
The exact term for this domain retains the additional
scalar
\[
                           \prod_{v\in S}\sigma_v
 \tag{36}
\]
from the choice of vertical sides. The proved thin-box
kernel estimate (32) and its nonzero local expansion
give the stated quantum comparison for the original
retained trace.

**Proof.** First check the exact change of side. With the
odd function \(g(t)\) used in (15), and the even function
\(c(h)=1/(4\cosh^2(Nh/2))\), one has
\[
 \int_{-H}^{H}g(-T+ih)c(h)\,dh
 =-\int_{-H}^{H}g(T-ih)c(h)\,dh
 =-\int_{-H}^{H}g(T+ih)c(h)\,dh .
 \tag{37}
\]
The last equality changes \(h\) to \(-h\), including
its integration limits. Thus replacing the positive
vertical side by the negative one contributes exactly
the factor \(-1\). Applying this independently at the
vertices proves (36). The spectator remains even in
each variable after other integrations, because each
original edge kernel has that property. All shared
normal data therefore remain those of the exact
Hermite identity.

The horizontal segment is still below the real axis,
and its principal Fourier charge is still \(+1\).
In particular the charge term remains \(-it_v\) for
both signs of \(n_v\); it is not changed when a
vertical side is reflected. The reflected vertical
domain still contains the full symmetric height
interval, so \(-|h_v|\le h_v\) proves
\(\mathcal E_S\le\Re\Phi\) exactly as before.

Write \(t-t^*=a+ib\). On a vertical coordinate,
\[
 a_v=\sigma_v(T-|\theta_v|),\qquad
 b_v=h_v+H_v\in[0,2H_v],
\]
and consequently
\[
 |a_v|>17/20,\qquad
 n_va_v=|n_v||a_v|>64(17/20),\qquad
                    0\le b_v<1/100.
 \tag{38}
\]
All segments from \(t^*\) to the current domain remain
in \(\mathcal B^I\). The weighted Taylor calculation
(10)--(13) uses absolute norms for its mixed term
and so does not require \(a_v>0\). Its last term is
still favorable, since \(n_va_v>0\).
In particular \(n_va_v>21d_vb_v\), and therefore
the \(B_2\) term in (13) is absorbed. We obtain
\[
 \Re\Phi(t)-\mathcal M
 <-\frac1{40\pi}\sum_{v\in S}d_v(17/20)^2
 <-|S|/400.
 \tag{39}
\]
This proves (35). The strict reserve also absorbs
midpoint replacements \(T_N=T+O(N^{-1})\) for all
sufficiently large levels, with the same constant
\(1/400\).

The partial-charge theorem and marked completion identify
this critical point and its absolute volume even when
all auxiliary vertices are selected. Its principal
horizontal Gaussian determinant is nonzero by the
same Hessian bound. Every height in the current domain
is less than \(1/200\) in modulus, so (32) is the
kernel bound needed for the retained finite trace;
the larger-height assumption (18) is unnecessary here.
The proved local kernel expansion supplies its nonzero
Gaussian coefficient.
\(\square\)

The signs in (36) do not affect the upper bound, but
they are part of the exact finite formula. This
corollary concerns the retained trace currents.
The complementary real grid rows obey the separate
comparison in Sections 4--5, also in the all-selected
scalar case. Those bounds use only the moduli of crossing
values and their polynomially bounded first normals.
The signed partial-charge theorem gives the same height
and action budgets with \(|n_v|\) in their denominators.
Hence that outer-row comparison applies unchanged
to these independently signed powers.

## 7. The retained external angle has a whole-period bound

Suppose one original outside endpoint is left free, with
angle \(u\), while the other outside endpoints remain
complete. Let \(F_N(u)\) be the corresponding original
path source, with every selected power satisfying \(|n_v|\ge64\),
and let \(\mathcal M\) denote its selected action at
\(u=0\). Use the proved thin-box kernel bound (32)
and the signed current domains of Section 6.
Then
\[
 |F_N(u)|\le C N^A
       e^{N[\mathcal M-(1-\cos u)/200]},
                       \qquad -\pi\le u\le\pi .
 \tag{40}
\]
The constants and polynomial powers may depend on the
fixed path and its fixed crossing powers.

For \(|u|\le19/20\), evenness at the free endpoint and
(4) give, for every retained neighboring angle \(t\),
\[
       \Re\psi(t,u)\le
          \Re\psi(t,0)-\frac{u^2}{20\pi}.
 \tag{41}
\]
This follows by integrating the \(uu\) entry of the
negative real Hessian twice along the real \(u\)-segment.
Its first derivative at zero is exactly zero, also for
complex \(t\). Thus the principal phase and every mixed
current acquire the same external loss. If the neighboring
vertex is one of the removed real rows, Lemma 2 first
replaces the edge by \(\psi(0,u)\); (41), with \(t=0\),
then gives that same loss. The estimates of Sections 5
and 6 therefore retain it term by term.

For \(9/10\le|u|\le\pi\), use (20) when its neighboring
vertex is retained. The centered phase is precisely
the phase of the edge with its outside endpoint complete,
and the extra loss is \((1-\cos u)/200\).
If the neighboring vertex is also removed, (21) retains
both angular losses, so the internal-row budget (30)
is unchanged. This proves the same estimate in the
outer range. The ranges overlap, and
\(u^2/(20\pi)\ge(1-\cos u)/200\), proving (40).

The uniform holomorphic kernel expansion has nonzero
amplitude on the thin box. Therefore the full source
has a nonzero holomorphic packet on a neighborhood
of \(u=0\). The stationary point persists by the
invertible complex Hessian; its amplitude is the product
of the original edge amplitudes and the nonzero
\(\sin t_v^*\) factors, divided by the continued Gaussian
determinant. The strict current and complementary-row
gaps persist on a smaller complex neighborhood, by
polynomial continuation and the uniform kernel estimates.

Finally the canonical source has degree at most \(N-1\)
in \(-2\cos u\). The exact Laurent-polynomial maximum
principle applied to (40), together with its local
holomorphic packet, gives a quadratic thin-strip bound
\[
 |F_N(x+iy)|\le C_1N^{A_1}
       e^{N[\mathcal M-c(1-\cos x)+B y^2]}
                 \quad(|x|\le\pi,\ |y|\le h),
 \tag{42}
\]
for some \(c,B,h>0\).
The proof is the harmonic-majorant and local Taylor
argument in
[the Newton note, Lemma 8](research_three_crossing_real_period_newton_bound.md).
No new observation or positive replacement state is used.
These are proved analytic estimates for the original
source. Its marking and geometric volume identification
are the separate inputs used when assembling a knot
volume theorem.

## 8. A stronger centered loss for a removed incidence

The next estimate concerns one full original edge. Its selected angle
may range across the full width \(\pi/2\) at height \(3/10\).
It requires the other real angle to be at least \(\pi/2\).
It supplies a source estimate for a complementary-row argument;
it does not extend the retained path contour theorem to powers seven.

Write \(\mathcal K_N(w,v)=\sum_{j=0}^{N-1}e_j(w)e_j(v)\), so that
\(K_N(u,z)=\mathcal K_N(-2\cos u,-2\cos z)\), and keep the
original normalization \(\Psi(z)=\psi(0,z)\).

**Lemma 4.** For every fixed pair of nonnegative integers \(k,\ell\),
there are constants \(C,A\) such that, at both level parities,
\[
 \left|
  \partial_w^k\partial_v^\ell\mathcal K_N(w,v)
       \big|_{w=-2\cos u,\ v=-2\cos z}
 \right|
 \le CN^A\exp N\left\{\Re\Psi(z)-\frac{21}{200}\right\},
 \quad
 \frac{\pi}{2}\le |u|\le\pi,\quad
 |\Re z|\le\frac{\pi}{2},\quad |\Im z|\le\frac3{10}.
 \tag{43}
\]
The derivatives are ordinary spectral derivatives, including
at \(w=2\) and \(v=-2\).

*The exact low-index entropy.* Put \(J_N=\lfloor(N-1)/2\rfloor\).
Evenness and conjugation allow writing \(z=r+iH\), with
\(0\le r\le\pi/2\) and \(0\le H\le3/10\).
Keep the selected angle in its modulus entropy:
\[
 \begin{split}
 B_z(x)&=\int_0^x\log|2\cos(2\pi s)+2\cos z|\,ds-2J(x),\\
 F_{r,H}(x)&=V_{\pi/2}(x)+B_z(x),\\
 |e_j(-2\cos u)e_j(-2\cos z)|
       &\le CN^A e^{NF_{r,H}(j/N)},\qquad 0\le j\le J_N.
 \end{split}
 \tag{44}
\]
The real-angle monotonicity of
[the original Newton entropy](research_three_crossing_real_period_newton_bound.md)
gives the removed-angle comparison. Its midpoint proof applies
also to the two complex shifted cosine factors of the selected
polynomial. Away from the bounded number of cells closest to a
real zero, the logarithmic derivative is bounded by a constant
over that real distance, uniformly in the imaginary shift.
On those cells, rescaling the modulus of a complex linear factor
bounds the upper midpoint error uniformly, including a zero
sample. Summation costs \(O(\log N)\).
This proves (44) uniformly through both low-index endpoints
and all shifted zeros. In particular it uses the literal
polynomials, without division by a vanishing value.

Set \(c=\cos(r+iH)\), \(C=\cosh H<21/20\), and
\(q=\cos(2\pi x)\). Since \(\Re c\ge0\), for \(q>0\)
the ratio \(q|q+c|/(1-q)^2\) is strictly increasing in \(q\).
Its logarithm is \(F'_{r,H}\). It has a unique critical
value \(q_*\), and
\[
 \begin{split}
 F'_{r,H}(x)&=\log\frac{|q|\,|q+c|}{(1-q)^2},\\
 1=\frac{q_*|q_*+c|}{(1-q_*)^2}
      &\le\frac{q_*(q_*+C)}{(1-q_*)^2},
 \qquad
 q_*\ge\frac1{C+2}>\frac{20}{61}>
        \cos\frac{2\pi}{5}.
 \end{split}
 \tag{45}
\]
For \(q=-v<0\), \(0<v<1\), the ratio is at most
\(v(C+v)/(1+v)^2<1\). Thus the reflected half has
no competing maximum. The logarithmic zeros are integrable.
The unique global maximum of (44) lies at \(0<x_*<1/5\).

On \(0\le x\le1/5\) all selected factorial arguments are in
their regular strips. Therefore \(B_z(x)=\Re b(x,z)\), with
the original branch. Since \(q>0\) on this interval,
\[
 \begin{split}
 \partial_H^2 B_{r+iH}(x)
 &=\frac{\sin(2\pi x)}{2\pi}
              \Re\frac1{q+\cos(r+iH)}
 \le\frac{\tan(2\pi x)}{2\pi}<\frac12,\\
 B_{r+iH}(x)&\le V_r(x)+\frac{H^2}{4},\\
 E(r,H):=\max_{0\le x\le1/2}F_{r,H}(x)
       &\le E(r,0)+\frac9{400}.
 \end{split}
 \tag{46}
\]
Here \(\partial_H B_{r+iH}|_{H=0}=0\).
The final numerical inequality follows from
\(\tan^2(2\pi/5)=5+2\sqrt5<19/2<(31/10)^2<\pi^2\).
No factorial estimate near the reflected zero was used in
this second-derivative argument: (45) first located the maximum
in the regular interval.

*Centering at the actual complete-edge action.*
At \(H=0\), the critical coordinate is
\(q_*=1/(2+\cos r)\). The
[calibrated stationary edge identity](research_unsummed_network_phase_coercivity.md#5-what-positive-geometry-does-imply-locally)
gives, with its original complete constant,
\[
 \begin{split}
 E(r,0)&=\psi(\pi/2,r),\\
 \Psi(r)-\psi(\pi/2,r)
 &=\frac1\pi\int_0^{\pi/2}
       \operatorname{asinh}\{\tan(a/2)\cos(r/2)\}\,da\\
 &\ge d_*:=
       \frac1\pi\int_0^{\pi/2}
                    \operatorname{asinh}\{\tan(a/2)/\sqrt2\}\,da.
 \end{split}
 \tag{47}
\]
This is a phase identity, not an assumed kernel asymptotic.
The bound \(\operatorname{asinh}s\ge s-s^3/6\) gives an
elementary exact lower bound:
\[
 d_*\ge\frac{13\log2-1}{12\pi\sqrt2}
                 >\frac{1127}{7920}.
 \tag{48}
\]
For the integral use
\(\int_0^{\pi/4}\tan a\,da=(\log2)/2\) and
\(\int_0^{\pi/4}\tan^3a\,da=(1-\log2)/2\).
For the strict rational inequality use
\(\log2=2\operatorname{atanh}(1/3)>2/3\),
\(\pi<22/7\), and \(\sqrt2<10/7\).

The selected color box lies in \(\Re(-2\cos z)<2\).
Since \(\Psi''(z)=-\sec(z/2)/(2\pi)\) and
\(\Re\sec(z/2)>0\) there, imaginary convexity gives
\(\Re\Psi(r+iH)\ge\Psi(r)\). Combining (46)--(48),
\[
 \Re\Psi(z)-E(r,H)>
       \frac{1127}{7920}-\frac9{400}
       =\frac{593}{4950}
       =\frac{21}{200}+\frac{293}{19800}.
 \tag{49}
\]

*Restoring the full radical.* Each original radical
\(e_j\), \(j>J_N\), has real interval norm at most
\(\sqrt{N-1}\), by the
[full original radical bound](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials).
Bernstein continuation in the selected angle costs
\(e^{(N-1)H}\); the removed angle stays real.
Hence their sum is at most \(CN^Ae^{NH}\).
For a coarse uniform lower bound on the selected phase,
\(\operatorname{asinh}\tan(a/2)\le a/\sqrt2\) on
\(0\le a\le\pi/2\), by differentiation. Consequently
\[
 \begin{split}
 \Re\Psi(z)&\ge\Psi(\pi/2)
      \ge M_\infty-\frac{\pi}{8\sqrt2}
       >\frac{29}{25}-\frac{55}{196}
        =\frac{4309}{4900}
        >\frac3{10}+\frac{21}{200}.
 \end{split}
 \tag{50}
\]
The lower bound \(M_\infty>29/25\) follows from the first
six alternating terms of the Catalan series and \(\pi<22/7\).
Thus every original index is retained in (43), at both parities.

*Ordinary derivatives.* The low-index and radical estimates
hold on the entire real removed-color interval \(0\le w\le2\),
for every selected angle in the displayed box. Ordinary Markov
inequalities retain all \(w\)-derivatives at polynomial cost,
including both endpoints. The modulus entropy and its compact
maximum are continuous in the selected angle, also when its
factorial zeros move through the real integration interval.
The strict reserve in (49)--(50) therefore persists on a
slightly enlarged selected-angle neighborhood. Cauchy's formula
on ordinary selected-color circles of radius \(O(N^{-2})\)
then costs only powers of \(N\). Their angular lifts move by
\(O(N^{-1})\), including the quadratic ramification at \(-2\).
This proves all the stated mixed ordinary derivatives. \(\square\)

**Corollary (two removed endpoints).** At both parities and for
all fixed ordinary derivatives,
\[
 \left|
 \partial_w^k\partial_v^\ell\mathcal K_N(w,v)
       \big|_{w=-2\cos u,\ v=-2\cos z}
 \right|
 \le CN^A e^{N(M_\infty-2(21/200))},
             \qquad \pi/2\le|u|,|z|\le\pi.
 \tag{51}
\]
Indeed the original real Newton bounds give low-index exponent
at most \(2m(\pi/2)=\psi(\pi/2,\pi/2)\).
Integrating the two real edge derivatives along the sides
\((0,0)\to(\pi/2,0)\to(\pi/2,\pi/2)\) gives
\(M_\infty-\psi(\pi/2,\pi/2)\ge2d_*>2(21/200)\).
The full radical has polynomial norm on both real intervals.
Markov's inequality in each ordinary color proves the derivative
statement, including the endpoints. This establishes an actual
loss per removed incidence even when both ends of an edge are
removed.

These are cancellation-free upper bounds for the original edge.
No corresponding lower bound, nonzero distant-color coefficient,
or whole-path contour theorem is inferred.

The focused exact checker
[check_path_large_angle_incidence.py](../experiments/check_path_large_angle_incidence.py)
verifies the rational comparisons and the entropy-maximizer
and integral identities in this section. Its
[saved record](../repro/results/research-path-large-angle-incidence.json)
records the proof and dependency hashes. It contains no finite-level
pattern extrapolation and no test of an unproved path assembly.

## 9. Vertical-current monotonicity at powers of at least seven

The threshold twenty in Section 2 comes from its Taylor estimate,
not from a change in the actual trace currents. A direct height
derivative gives a stronger phase comparison. The full finite-kernel
input is identified separately at the end of this section.

Use the positive path charge family with a stipulated complete
outside endpoint. At unit charges, the
[path geometry bound](research_unsummed_network_phase_coercivity.md#6-a-common-central-domain-for-positive-paths-of-power-at-least-seven)
gives, for every integer power \(n_v\ge7\),
\[
             0<a_v<19/20,\qquad 0<H_v<3/10.
 \tag{52}
\]
Write \(t_v^*=a_v-iH_v\), and retain the original phase
\(\Phi\) and action \(\mathcal M\) from (1)--(2).
For any common cutoff \(99/100\le T\le\pi/2\), define
the mixed rectangle and its exponent exactly by (6)--(7).

**Lemma 5 (the wider phase rectangle).** On
\[
       |\Re t|,|\Re u|\le\pi/2,
          \qquad |\Im t|,|\Im u|\le3/10,
 \tag{53}
\]
the original continued edge phase is holomorphic on a
neighborhood of the rectangle, and
\[
                         \Re K(t,u)\succeq\frac1{10}I.
 \tag{54}
\]

*Proof.* Set \(w=\tan(t/2)\), \(v=\tan(u/2)\).
On (53), \(|w|,|v|\le1\) and
\(|\Im w|,|\Im v|<3/10\). The latter follows directly
from \(\cos(\Re t)\ge0\) and
\[
 |\Im\tan(t/2)|
 =\frac{\sinh|\Im t|}{\cos(\Re t)+\cosh(\Im t)}
 \le\tanh|\Im t|.
\]
Consequently the branch \(s=\sqrt{1+w^2+v^2}\) has
positive real part throughout the rectangle. None of the
factors \(s\pm w,s\pm v\) vanish, since their paired
products are \(1+v^2,1+w^2\), respectively. Continuing
the logarithms from the complete point gives the original
edge branch on this simply connected domain.

Put \(X=(\Re w,\Re v)\), \(Y=(\Im w,\Im v)\) and
\(\alpha=\Re s\). The
[exact edge criterion](research_edge_hessian_and_phase_response.md#2-an-exact-positivity-criterion)
gives
\[
 \begin{split}
 \alpha^2-\{\Im(w\overline v)\}^2
   &\ge(1-|Y|^2)(1+|X|^2)+(X\cdot Y)^2>41/50,\\
 \alpha(|s|^2+1)&\le4\sqrt3<7.
 \end{split}
 \tag{55}
\]
Its determinant-over-trace estimate therefore bounds the
smaller eigenvalue of \(\Re K\) below by
\(41/350>1/10\). This proves (54). \(\square\)

**Theorem 6 (all mixed-current subsets).** For every nonempty
\(S\subseteq I\), every cutoff in the stated interval and
every point of (6),
\[
 \mathcal E_S(\mathbf t)
 \le\mathcal M-\frac{|S|}{80000}
                -\frac1{40}\sum_{v\in S}(h_v+H_v).
 \tag{56}
\]
The estimate is uniform in path length and in the individual
powers \(n_v\ge7\).

*Proof.* Hold all coordinates except a vertical one fixed,
and write \(t_v=T+ih\). Its exact exponent derivative,
away from the harmless cusp at \(h=0\), is
\[
 \partial_h\mathcal E_S
   =\frac1\pi\sum_{w\sim v}\Im r_{vw}
                     -\frac{n_vT}{2\pi}-\operatorname{sign}h,
 \qquad
 r_{vw}=\operatorname{asinh}
       \{\tan((T+ih)/2)\cos(t_w/2)\}.
 \tag{57}
\]
This uses the original derivative \(\psi_t=-r/\pi\),
and retains the folded vertical trace penalty \(-|h|\).
Other coordinates may themselves lie anywhere on their
vertical segments; their heights need not have the same sign.

We record the branch and numerical bounds in (57). If
\(C=\cos(t_w/2)\), then
\[
 \Re C>7/10,\qquad |\Im C|<4/35,\qquad
 \Re\tan((T+ih)/2)>16/41,\qquad
 |\Im\tan((T+ih)/2)|<3/10.
 \tag{58}
\]
For the first two inequalities use \(\cos(\pi/4)>7/10\),
\(\sin(\pi/4)<5/7\), and \(\sinh(3/20)<4/25\).
For the third use \(\sin T\ge\sin(99/100)>4/5\)
and \(\cos T+\cosh h<41/20\).
Thus the argument of asinh in (57) has strictly positive
real part. Its original branch has \(\Re r>0\) and
\(-\pi/2<\Im r<\pi/2\) on all these segments.

When \(h\le0\), the imaginary part of the tangent is
nonpositive, and its real part is at most one. Hence a
positive imaginary return \(g=\Im r\) satisfies
\[
 \sin g=\frac{\Im\{\tan((T+ih)/2)C\}}{\cosh(\Re r)}
       <\frac4{35},\qquad
          g<\frac{25}{24}\frac4{35}=\frac5{42}.
 \tag{59}
\]
The same upper bound holds if \(g\le0\). There are at
most two incidences. Using \(\pi<22/7\), (57) gives
\[
 \partial_h\mathcal E_S
 <1-\frac{693/100-10/21}{2\pi}
 <-\frac{353}{13200}<-\frac1{40},\qquad h<0.
 \tag{60}
\]
For \(h>0\), the simpler bound \(g<\pi/2\) gives
\(\partial_h\mathcal E_S<-n_vT/(2\pi)<-1/40\).
Both one-sided bounds hold at zero. Integrating each
vertical height from \(-H_v\) to its actual value proves
that its exponent is no larger than its bottom horizontal
value minus \((h_v+H_v)/40\).

At the resulting bottom point all imaginary coordinates
equal those of the geometric saddle. Lemma 5, summed over
the actual edges, and Taylor's formula at that saddle give
\[
 \Re\Phi(\mathbf r-i\mathbf H)
 \le\mathcal M-\frac1{40\pi}
                 \sum_v d_v(r_v-a_v)^2.
 \tag{61}
\]
For each \(v\in S\), \(r_v=T\) and
\(T-a_v>1/25\). Therefore its contribution to the loss
is greater than \(1/(25000\pi)>1/80000\). Combining
these losses with (60) proves (56). \(\square\)

These are precisely the phases of the original mixed
Hermite currents in (15), at both level parities. Choose the
largest midpoint cut \(T_N\le T\), where
\(T\in(99/100,\pi/2]\) is fixed. Then \(T_N\to T\)
and the cut lies in the theorem's interval for all sufficiently
large levels. Thus no rounding limit changes its positive gap.

The full [wide-kernel theorem](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two)
now gives the uniform finite-kernel bound on all of (53),
including its original normal directions. Consequently (56)
bounds the actual mixed quantum currents with cutoff \(T=\pi/2\).
Lemma 4 covers every retained complex endpoint on that same
rectangle and gives the matching removed-row loss. The
[full path assembly](research_uniform_path_trace_assembly.md#7-the-source-theorem-at-powers-seven-and-eight)
combines these source bounds with the local action budget and
the original nonzero Gaussian coefficient. The phase estimate
(56) alone is not being substituted for those finite-source steps.

The exact scalar checks for (55), (58)--(61) are included in
[check_positive_path_seven_geometry.py](../experiments/check_positive_path_seven_geometry.py),
with their current proof dependencies in its
[saved record](../repro/results/research-positive-path-seven-geometry.json).
