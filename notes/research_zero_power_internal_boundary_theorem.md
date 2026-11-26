# A zero crossing power with at least three neighboring tangles

Research proof, 2 November 2026. This note proves a whole-boundary
asymptotic at every original vertex of degree \(d\ge3\) whose
crossing power is zero. The degree is fixed before the quantum level
tends to infinity. The argument uses the full Fourier circle. Its
vertical endpoint currents vanish exactly at zero crossing power,
which removes the need for an endpoint estimate on a short angular
interval. The frozen manuscripts are unchanged.

## 1. The original polynomial and its selected action

Use the complete Newton polynomials and trace

\[
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}
       \{2\cos((2j+1)\pi/N)-z\},\qquad
 S_k=\prod_{j=1}^k2\sin(\pi j/N),
\]

\[
 K_N(t,u)=\sum_{k=0}^{N-1}e_k(-2\cos t)e_k(-2\cos u),
 \qquad \mathcal D_{0,N}f=\phi_N(f).
\]

The original boundary polynomial of a degree-\(d\) zero-power vertex
is

\[
 P_{d,0,N}(\mathbf u)
   =\mathcal D_{0,N}^{(t)}
         \left[\prod_{j=1}^d K_N(t,u_j)\right].           \tag{1}
\]

The trace includes every first normal derivative at a repeated root.
No boundary is closed after taking this trace. In particular, (1) is
a polynomial of degree at most \(N-1\) in each \(-2\cos u_j\).

Let \(\psi\) be the original edge phase, with

\[
 \psi(0,0)=M_\infty=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                         (\tan(t/2)\cos(u/2)).
\]

For \(d\ge3\), put

\[
 h_d=2\operatorname{arsinh}\tan\frac\pi d,
 \qquad t_d=-ih_d,
 \qquad x_d=\frac1\pi\arctan\cosh(h_d/2).
                                                               \tag{2}
\]

Then \(d\psi_t(t_d,0)=i\). Near \(\mathbf u=0\), define
\(t_d(\mathbf u)\) by

\[
 \sum_{j=1}^d\psi_t(t_d(\mathbf u),u_j)=i,
 \qquad t_d(0)=t_d,
\]

and set

\[
 G_d(\mathbf u)=\sum_{j=1}^d\psi(t_d(\mathbf u),u_j)
                                      -it_d(\mathbf u),
 \qquad M_d=G_d(0)=d\psi(-ih_d,0)-h_d.
                                                               \tag{3}
\]

The branch is continued from the original complete geometry. Its
existence and positive primitive cone deformation are proved in
[the isolated-vertex geometry](research_isolated_internal_vertex_geometry.md).

**Theorem.** For every fixed integer \(d\ge3\), there is a complex
polydisk about zero on which

\[
 P_{d,0,N}(\mathbf u)
 =N^{-3(d-1)/2}A_d(\mathbf u)e^{NG_d(\mathbf u)}
                       (1+O_d(N^{-1})),                  \tag{4}
\]

uniformly through all sufficiently large integer levels. The amplitude
is holomorphic and nonzero, and the normalized error is holomorphic,
with the same order for fixed derivatives on smaller polydisks.
There are positive constants \(c,B,b,C\) and a finite constant
\(A\) such that

\[
 |P_{d,0,N}(\mathbf x+i\mathbf y)|
   \le CN^A\exp N\left\{
       M_d-c\sum_{j=1}^d(1-\cos x_j)+B\sum_{j=1}^d y_j^2
                         \right\}                       \tag{5}
\]

for \(|x_j|\le\pi\), \(|y_j|\le b\). The phase in (4) is
exactly the marked geometric action (3), with no additional unit phase.
Its boundary Hessian is

\[
 (G_d)_{u_iu_j}(0)
       =-\delta_{ij}\frac{\cosh(h_d/2)}{2\pi}.            \tag{6}
\]

The theorem concerns the complete source, including its discarded
wire indices, and both parities of the level.

## 2. Positive Laurent coefficients and angular decrease

For every \(k\) with \(2k<N\), there is an exact Laurent identity

\[
 e_k(-2\cos t)
   =\frac{S_{2k}}{S_k^2}
        \sum_{r=-k}^{k}
          \frac{e^{irt}}{S_{k+r}S_{k-r}}.                 \tag{7}
\]

All its coefficients are positive. To prove it, put
\(q=e^{\pi i/N}\), \(Q=q^2\), \(w=e^{it}\). Factoring each
cosine numerator gives

\[
 e_k(-2\cos t)
 =\frac{w^{-k}}{S_k^2}
        \prod_{j=0}^{2k-1}(1+wq^{-2k+1}Q^j).
\]

Expand by the finite Gaussian-binomial identity. The coefficient of
\(w^a\) in the product is
\(q^{a(a-2k)}{2k\brack a}_Q\). The equality
\({2k\brack a}_Q=q^{a(2k-a)}S_{2k}/(S_aS_{2k-a})\)
cancels this phase and proves (7). All indices of the denominators
are less than \(N\), so this specialization has no zero denominator.
The finite Gaussian-binomial identity itself follows by induction on
the number of factors, or by its usual two-term coefficient recurrence.

Fix a compact interval \(I=[\alpha,\beta]\subset(0,1/2)\) and
a positive height \(h\). For real \(|\tau|\le\pi\), the root
product gives the sharper angular estimate

\[
 |e_k(-2\cos(\tau-ih))|
  \le C_{I,h}e_k(-2\cosh h)
    \exp\left[-N\frac{\sin(2\pi k/N)}
                         {2\pi(\cosh h+1)}(1-\cos\tau)\right]
               \qquad(k/N\in I).                        \tag{8}
\]

Here is the real-variable proof, including the uniformity in the wire
index. Define

\[
 f_h(s)=\log|1+e^{h+is}|,
 \qquad L_{x,h}(\tau)=\frac1{2\pi}
             \int_{-2\pi x}^{2\pi x}f_h(\tau+s)\,ds.
\]

The roots in the product above are precisely the midpoints of this
interval with mesh \(2\pi/N\). Since \(h>0\), the periodic
function \(f_h\) is smooth, with bounded second derivative.
The midpoint rule therefore gives, uniformly in \(k/N\in I\)
and real \(\tau\),

\[
 \log\frac{|e_k(-2\cos(\tau-ih))|}{e_k(-2\cosh h)}
      =N\{L_{k/N,h}(\tau)-L_{k/N,h}(0)\}+O_{I,h}(N^{-1}).
                                                               \tag{9}
\]

Let \(a=2\pi x\in(0,\pi)\). For \(0\le\tau\le\pi\),

\[
 L_{x,h}'(\tau)
 =\frac1{4\pi}\log
    \frac{\cosh h+\cos(\tau+a)}{\cosh h+\cos(\tau-a)}
 \le-\frac{\sin a\sin\tau}{2\pi(\cosh h+1)}.
                                                               \tag{10}
\]

Indeed the denominator minus the numerator is
\(2\sin a\sin\tau\), and \(\log(A/B)\le-(B-A)/B\)
for \(0<A\le B\); also \(B\le\cosh h+1\).
Integrating (10), and using evenness for negative \(\tau\),
proves (8).

We also need the real-parent estimate

\[
 |e_k(-2\cos u)|
    \le CN^{A_0}e_k(-2)
       \exp\left[-N\frac{\sin(2\pi k/N)}{4\pi}
                                        (1-\cos u)\right]
                  \quad(k/N\in I,\ |u|\le\pi).          \tag{11}
\]

This is the height-zero version of the same potential inequality.
The logarithmic zeros of \(f_0\) prevent a uniform smooth midpoint
error, but its upper error is \(O(\log N)\): remove the at most two
mesh intervals touching a zero, bound the variation on the remaining
intervals, and integrate the removed logarithms. A product vanishing
at a root already satisfies the upper bound. At \(u=0\), the compact
wire interval stays away from those zeros and has the ordinary uniform
bulk estimate. Equivalently, (11) follows directly from the real-wire
case of the proved
[Newton boundary-decrease lemma](research_uniform_factorial_and_boundary_decay.md).
In (10) with \(h=0\), the logarithmic singularity is integrable and
the derivative inequality holds off its isolated singular point.
It therefore integrates to the same loss, with coefficient
\(\sin a/(4\pi)\).

## 3. A strict gap for the omitted wire indices

First suppose \(d\ge4\), and put \(\Delta_d=dM_\infty-M_d\). The
[action-gap lemma](research_isolated_vertex_action_gap.md)
proves

\[
 0<\Delta_d<M_\infty\qquad(d\ge4).
\]

For clarity, this uses the explicit zero-power branch
\(h_d(\lambda)=2\operatorname{arsinh}\tan(\pi\lambda/d)\).
Its integrated action loss decreases strictly with \(d\), and the
exact degree-three loss is \(M_\infty\). Thus

\[
 \eta_d:=M_d-(d-1)M_\infty=M_\infty-\Delta_d>0.          \tag{12}
\]

Choose rational cutoffs \(0<\alpha<\beta<1/2\), sufficiently
close to zero and one half, that \(x_d\in(\alpha,\beta)\) and

\[
 \sup_{x\in[0,\alpha]\cup[\beta,1/2]}2g(x)<\eta_d/2,
 \qquad g(x)=J(2x)-4J(x).
\]

Such cutoffs exist because \(g\) is continuous and zero at both
endpoints. Retain exactly the wire indices \(k/N\in I=[\alpha,\beta]\)
in every edge kernel. The complete Hermite norm estimate applies before
the trace and gives, for all omitted assignments together,

\[
 |\text{omitted contribution}|
    \le CN^A\exp N(M_d-\eta_d/2),                       \tag{13}
\]

uniformly for all real parent angles. One omitted low wire has rate
at most \(\eta_d/2\); a high wire has rate zero; and every other
wire has rate at most \(M_\infty\). There are polynomially many
assignments for fixed \(d\). This includes the first normal
derivatives and does not presume positivity of multiplication in the
quotient algebra.

At \(d=3\), the coarse gap in (12) is zero, so a different argument
is necessary. The
[degree-three discarded-wire proof](research_degree_three_zero_wire_tails.md)
establishes the following stronger statement: for every fixed interval
\(I\subset(0,1/2)\) containing
\(x_3=\arctan(2)/\pi\) in its interior, all omitted assignments
together have a uniform real-boundary bound

\[
 |\text{omitted contribution}|\le CN^A e^{N(M_3-\delta_I)}
                 \qquad\text{for some }\delta_I>0,
 \qquad M_3=2M_\infty.                                  \tag{13a}
\]

Its two ingredients are exact finite identities. Two high indices
give zero in the full quotient algebra. For a term with one high
index, the positive Newton multiplication law couples its coefficient
to the two low parent factors; their continuous joint rate is strictly
below \(2M_\infty\) on its entire compact support. For an all-low
triple, write the product of its three Newton polynomials as
\(\sum_m a_me^{imt}\). All \(a_m\) are nonnegative, and the
full trace is exactly
\(N^2(a_{N-1}-a_{N+1})\). Positivity of the Newton multiplication
then gives the upper bound
\(N^2e^{-(N-1)h_3}\sum_ma_me^{mh_3}\). Strict concavity of
the three resulting real wire phases supplies the gap whenever one
index is outside \(I\). This retains the first normal derivatives
and all real parent angles. The cited proof includes the uniform
endpoint estimates and the compactness argument.

Thus for every fixed \(d\ge3\) we have an interval \(I\) with
\(x_d\) in its interior and a strict whole-source omitted-wire gap.
These are the only properties of the discarded terms used below.

## 4. The local edge expansion at the deeper imaginary angle

Let \(h=h_d\) and \(t_0=-ih\). The retained kernel is

\[
 K_{N,I}(t,u)=\sum_{k/N\in I}e_k(-2\cos t)e_k(-2\cos u).
\]

At \((t,u)=(t_0,0)\), both Newton factors are positive. Its
canonical interpolating phase is

\[
 A(x;t,u)=b(x,t)+b(x,u),
 \qquad
 b(x,t)=\int_0^x\log(2\cos(2\pi v)+2\cos t)\,dv-2J(x).
\]

At \((t_0,0)\) the logarithms are real and the phase is strictly
concave for \(0<x<1/2\), since

\[
 A_{xx}(x;t_0,0)
 =\sum_{v\in\{t_0,0\}}
  \left[-\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+\cos v}
                                      -2\pi\cot(\pi x)\right]<0.
                                                               \tag{14}
\]

Its derivative tends to positive infinity at zero and negative
infinity at one half. Its unique maximum is \(x=x_d\). The
critical equation is the original one,

\[
 \cos(2\pi x)=\frac{1-\cos t\cos u}{2+\cos t+\cos u},
\]

and therefore its holomorphic critical branch agrees with the original
edge phase \(\psi(t,u)\), continued along \(t=-iy\),
\(0\le y\le h\).

The canonical factorial interpolation has no singularity near the
real wire interval at this point. Its midpoint arguments have real
parts \(1/2-x>0\), the unshifted wire arguments have real parts
\(x>0\), and all of them stay in compact subsets of their regular
strips after a sufficiently small complex perturbation of \(x,t,u\).
Thus the same factorial expansion as in the exact edge theorem applies.

Here are the contour details needed to extend that theorem beyond its
previous small angle disk. Enclose the retained integers by the exact
cotangent rectangle with half-grid vertical sides near \(\alpha\)
and \(\beta\), and horizontal wire heights \(\pm\varepsilon\).
At the real base point, (14) gives a fixed gap at both endpoints.
Choose \(\varepsilon>0\) so small that these vertical sides and
their connectors retain the gap. Along the horizontal sides, the
excess above the stationary real phase is at most
\(C\varepsilon^2\), because the base phase is real on its real
interval. Take \(C\varepsilon^2<\pi\varepsilon\). The
nonconstant cotangent modes then retain a gap, since their exact
decay is \(e^{-2\pi N\varepsilon}\).

Next choose the \((t,u)\) neighborhood sufficiently small. The
strict endpoint gaps and the cotangent gap persist uniformly there,
and the imaginary part of the critical wire coordinate is less than
\(\varepsilon/10\). The constant cotangent terms give \(N\)
times the real integral; translate it to the horizontal tangent
through the critical wire point. The endpoint connectors still have
the fixed gap. Strict negative real wire Hessian gives the uniform
Gaussian expansion. The half-grid endpoints differ from
\(\alpha,\beta\) by \(O(N^{-1})\), and the estimates hold on
a fixed larger regular rectangle, so this change is included.

Consequently, near \((t_0,0)\),

\[
 K_{N,I}(t,u)
   =N^{-3/2}a_e(t,u)e^{N\psi(t,u)}(1+O(N^{-1})),          \tag{15}
\]

with a holomorphic relative error. The original amplitude remains

\[
 a_e(t,u)=\frac{\sqrt{2\pi}}
        {4\sin^2(\pi x(t,u))\sqrt{-A_{xx}(x(t,u);t,u)}}.
                                                               \tag{16}
\]

The square root is positive at \((t_0,0)\). No factor in (16)
vanishes there. This proves the local expansion for the actual finite
wire sum, including its lattice corrections.

## 5. The endpoint current is identically zero

For any even periodic polynomial \(f(t)=f^\sharp(-2\cos t)\),
the exact complete trace at zero crossing power is

\[
 \mathcal D_{0,N}f
 =-\frac{N^2}{\pi i}\int_{-\pi-ih}^{\pi-ih}
       \sin t\,f(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt,
 \qquad \eta=(-1)^{N-1}.                                \tag{17}
\]

This is the full-circle form of the
[exact rational trace](research_exact_complete_trace_contour.md).
Its displayed vertical current vanishes exactly here: at
\(t=\pi+iv\),

\[
 \sin(\pi+iv)f(\pi+iv)
          =-i\sinh v\,f^\sharp(2\cosh v)
\]

is odd in \(v\), while \(1/(4\cosh^2(Nv/2))\) is even.
Their integral on \([-h,h]\) is zero. Equivalently, the opposite
vertical sides cancel by \(2\pi\)-periodicity. This argument is
valid for any polynomial degree and retains the original normal
derivatives. It applies to the entire retained product in (1), not
just to its leading phase.

## 6. The full lower circle and its unique contribution

Let

\[
 c_t=\min_{x\in I}\frac{\sin(2\pi x)}{2\pi(\cosh h+1)}>0,
 \qquad c_u=\min_{x\in I}\frac{\sin(2\pi x)}{4\pi}>0.
\]

Equations (8) and (11), summed over the positive base terms, give

\[
 |K_{N,I}(\tau-ih,u)|
  \le CN^A K_{N,I}(-ih,0)
       e^{-N\{c_t(1-\cos\tau)+c_u(1-\cos u)\}}
                                                               \tag{18}
\]

for the whole real circles in \(\tau\) and \(u\). This bound
is possible because the base wire summands at \((-ih,0)\) are
positive. It does not assert positivity at general real parent angles.

Apply (17) to \(f(t)=\prod_jK_{N,I}(t,u_j)\). On its lower
circle,

\[
 \frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}
          =e^{-iNt}(1+O(e^{-Nh})).
\]

The modulus of the first factor is \(e^{-Nh}\). By (15),
\(K_{N,I}(-ih,0)^d\) has rate \(d\psi(-ih,0)\).
Consequently (18) bounds the full trace integrand by a polynomial
times

\[
 \exp N\left\{M_d-dc_t(1-\cos\tau)
                          -c_u\sum_j(1-\cos u_j)\right\}.
                                                               \tag{19}
\]

At complete parents the lower-circle parameter \(\tau=0\) is
therefore the only possible maximum, with a strict gap on every
closed region excluding it. The exact rational denominator places
all higher Fourier charges below that same contribution by at least
\(h\). No other contour piece remains to be estimated.

Near \(\tau=0\), insert (15) for each kernel. The phase is
\(\sum_j\psi(t,u_j)-it\), whose selected critical point is
(3). At complete parents its second derivative is

\[
 d\psi_{tt}(-ih,0)=-\frac{d}{2\pi}\operatorname{sech}(h/2)<0.
\]

Uniform one-dimensional Gaussian expansion proves (4), with

\[
 A_d(\mathbf u)
   =i\sqrt{\frac2\pi}\,
      \frac{\sin t_d(\mathbf u)
                 \prod_j a_e(t_d(\mathbf u),u_j)}
           {\sqrt{-\sum_j\psi_{tt}(t_d(\mathbf u),u_j)}}.
                                                               \tag{20}
\]

At zero its value is explicitly positive:

\[
 A_d(0)=
       \frac{2\sinh h}{\sqrt{d\operatorname{sech}(h/2)}}
                          a_e(-ih,0)^d>0.
\]

There is also a closed expression. Put \(k=\cosh(h/2)=\sec(\pi/d)\).
At the real wire saddle, direct substitution in (14) gives
\(A_{xx}=-2\pi(1+k^2)^2/k^3\), so (16) simplifies to
\(a_e(-ih,0)=1/(4\sqrt k)\). Hence

\[
 A_d(0)=\frac{4^{1-d}}{\sqrt d}\tan\frac\pi d
                   \left(\sec\frac\pi d\right)^{(3-d)/2}.
                                                               \tag{21}
\]

The powers of \(N\) are \(N^2\) from the trace,
\(N^{-3d/2}\) from the kernels, and \(N^{-1/2}\) from the
last Gaussian. The resulting exponent is \(-3(d-1)/2\).
The local expansion and exterior gaps continue on a sufficiently
small complex parent polydisk. The omitted-wire bounds of Section 3
also retain their gap there by polynomial continuation. This completes
the proof of the uniform holomorphic asymptotic for the whole source.

## 7. Global boundary bounds and geometric normalization

Equation (19) proves a real-parent angular loss for the retained
trace. The omitted contribution from Section 3 has a fixed gap independently
of the real parents. Since \(\sum_j(1-\cos u_j)\le2d\),
decreasing the angular constant absorbs that contribution as well.
This proves (5) first for real parents.

Separate evenness gives \(\partial t_d/\partial u_j(0)=0\).
The stationary boundary Hessian is consequently the explicit parent
Hessian of the edge phase, which is (6). The local holomorphic
expansion therefore gives a quadratic bound on a small complex
parent neighborhood. Away from that neighborhood, the real angular
gap persists on a sufficiently thin complex strip by the polynomial
Bernstein–Walsh estimate on a finite cover by products of real
spectral intervals. Each boundary degree is at most \(N-1\).
Combining those two estimates proves (5).

The selected action is exactly (3): the physical trace has no
crossing chirp and \(C_{N,0}=1\), and the unit-charge factor in (17)
is \(e^{-iNt}\). The isolated-vertex geometric proof identifies
this same stationary action along the original positive primitive
cone path, starting with \(2d\) regular ideal octahedra. Its
Schläfli derivative is \(2\pi\) times the real action derivative.
Thus the complete partially filled star contributes volume
\(2\pi M_d\), with its original peripheral curves and absolute
normalization. No additional phase or additive volume constant occurs.

Accordingly these degree-\(d\ge3\) zero-power vertices may be used
as singleton selected components in the further-filling theorem of
[the connected-cluster note](research_connected_short_filling_clusters.md#10-a-volume-theorem-after-further-long-fillings).
The resulting statement still requires all remaining powers to be
independently sufficiently long, unless their own joint boundary
polynomials have also been established.

## 8. The degree-three value and the remaining scope

The additional omitted-wire argument is essential at degree three;
the elementary Hermite estimate alone has no strict gap there. With
(13a), however, the same full-circle proof applies. The explicit
normalization (21) and the action-gap identity give

\[
 M_3=2M_\infty,\qquad A_3(0)=\frac1{16},\qquad
 P_{3,0,N}(0,0,0)
   =\frac{e^{2NM_\infty}}{16N^3}(1+O(N^{-1})).
\]

The theorem proves the entire three-boundary polynomial near zero
and its global boundary bound, not only this value at complete
parents. It makes no assertion that the finite polynomial is exactly
the square of an edge kernel.

At degree two and zero power, the selected cone branch degenerates
at unit charge; its exact algebraic and marked tangle reduction is
a separate result. Connected sets of adjacent low-degree short
fillings also require their joint boundary estimates. The present
theorem supplies one zero-power vertex of any degree at least three,
with every neighboring boundary left free.
