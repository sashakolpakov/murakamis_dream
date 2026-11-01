# A boundary-response criterion for a protected source term

Removing one crossing-region factor from the marked source leaves a
polynomial in two face variables. Its positive logarithmic growth records
how the remaining triangles distribute their loads between those faces.
The first derivative is the load at one boundary face; the second is an
effective conductance obtained from the triangle Hessians. This note shows
how those two quantities can pay for restoring the two removed triangles.

More precisely, let \(F(z)\) be the exterior pressure when the boundary
weights are \(A=e^z,C=1\), and put
\(\nu=F'(0)\), \(\kappa=F''(0)\). Under the strict feasibility and
connectivity hypotheses below, the condition
\(0<\nu\le1/2\), \(\nu+\kappa\ge1/2\) gives a strict exponential
bound for the original signed left contribution, uniformly over its
real spectral variable \(\sigma\in[-2,2]\), at odd levels. Every other
crossing region keeps its central numerator at spectrum \(-2\).
The comparison is with the unchanged diagram's complete action
\(\Phi=\operatorname{Vol}(Y)/(2\pi)\), where \(Y\) is its augmented
link exterior. The precise bound and proof appear in section 9.

The argument allows arbitrary fixed matched simple spheres satisfying
these hypotheses, with no restriction on their number of vertices or
cycles. It estimates one source contribution. It does not estimate
several noncentral regions, varying neighboring spectra, even levels,
or the full filling period. The recorded 54-region example does not
satisfy this response condition; its separate tilted certificate is
proved in [the uniform cap estimate](research_cap_uniform_spectral_gap.md).
No strict enlargement of a known knot-volume class is asserted here.

## 1. Original coordinates and the exact restoration problem

Start with a finite simple triangulation of the sphere, with its
triangular faces paired across shared edges. This pairing is the
matching. A distinguished nonmatching edge carries the original main
mark. Use the ordered source of its
[matched-sphere Morse diagram](research_matched_sphere_morse_source.md):
the matching pairs specify crossing regions, and the two endpoints of
the marked edge specify the protected face variables. All these
incidences and the mark remain fixed.

Use the source argument order \((x,b,c,y)\), for which the two central
triangle factors are \((x,b,y)\) and \((x,c,y)\). The selected protected
left contribution, also called the cap, has arguments

\[
                  (x,b,c,y)=(C,0,A,0).
\tag{1}
\]

Here \(A\) is the ordinary overloaded middle; \(C\) is the other
ordinary face. Thus the two omitted complete triangles have supports
\(\{C\}\) and \(\{A,C\}\). They are not two copies of a
two-supported triangle. In the 54-region source, \(A=L_{16}\) and
\(C=L_0\); the protected faces are \(50,29\).

At level \(N\), write \(d=N-1\). A protected face variable is set
to zero by the original main mark; every ordinary face retains the
coefficient target \(d\). Let \(I\) be the ordinary faces other than
\(A,C\). After extracting precisely those targets from the other
central factors, the remaining polynomial is

\[
P_N(A,C)=
\left[\prod_{i\in I}L_i^d\right]
\prod_{e\ne e_*}P_{e,\mathrm C}(-2;\boldsymbol L)
=\sum_{j=0}^{d}p_{N,j}A^jC^{d-j}.
\]

Here \(e_*\) is the selected crossing region. The notation
\(P_{e,\mathrm C}\) means its actual central source numerator, with
only its common unit sign removed. In particular its original
\(N^2\) normalization is retained. At odd levels the coefficients are
nonnegative and the nonzero binary polynomial is real stable, meaning
that it does not vanish when both variables have positive imaginary
part. These
facts follow from the original determinant factors, as explained in
[the common-axis estimate](research_cap_common_axis_bound.md), sections
2–3. The degree is \(d\), since removing one degree-\(d\) factor and
extracting all but the two remaining ordinary targets leaves that
homogeneous degree. We write \(S_N(\sigma)\) for the exact shared
coefficient when the selected region uses its left numerator at
spectrum \(\sigma\) and every other region uses this central numerator
at \(-2\). Restoring the removed unit signs multiplies this coefficient
by a unit scalar, leaving its absolute value unchanged. No filling
functional has been applied.

The complete triangle potential used below is

\[
Q(w_1,w_2,w_3)=
\max_{\substack{a_j\ge0,\ \sum_j a_j=1/2\\a_j=0\text{ if }w_j=0}}
\sum_{j:w_j>0}\bigl[f(a_j)+a_j\log w_j\bigr],
\qquad
f(a)=\frac{\Lambda(\pi a)+\Lambda(\pi/2-\pi a)}\pi,
\]

where \(\Lambda(t)=-\int_0^t\log|2\sin u|\,du\). The nonzero
weights are positive, and at least one weight is positive in each
triangle under consideration. Thus a supported triangle carries total load
\(1/2\), and a singleton of weight \(w\) has potential
\(\frac12\log w\). These are the absolute source conventions of
[the triangle entropy formula](actual_triangle_entropy_algebraic_balance.md).

Retain every other original triangle, every other ordinary target one,
and both protected zeros. Fix \(C=1\), put \(A=e^z\), and minimize over
the remaining ordinary log weights:

\[
F(z)=\min_{w_I}\left\{
\sum_{t\text{ exterior}}Q_t(e^z,1,e^{w_I})
-\sum_{i\in I}w_i\right\}.
\tag{2}
\]

Assume a strictly positive feasible exterior half-load table and a
connected supported ordinary pair graph. The row masses are \(1/2\),
and the extracted demands are precisely one at every \(i\in I\).
Strict positivity means that every unprotected corner of a retained
triangle has positive load. The graph has one vertex for each ordinary
face and joins two faces whenever they occur in the same retained
triangle.
These are the hypotheses of [the effective-response theorem](research_global_cap_effective_response_criterion.md).
It identifies the pressure below with the odd-level limit of
\(N^{-1}\log P_N(e^z,1)\), with locally uniform holomorphic derivatives.
Define

\[
M=F(0),\qquad \nu(z)=F'(z),\qquad
\kappa(z)=F''(z),\qquad \nu=\nu(0),\quad\kappa=\kappa(0).
\tag{3}
\]

The interesting interior-cap case has \(0<\nu<1/2\). The proofs below
also allow \(\nu=1/2\).

The two omitted complete triangles contribute
\(\frac12\log C+Q(C,A,0)\). With \(C=1\), set

\[
q(z)=Q(1,e^z,0)
=\frac2\pi\operatorname{Ti}_2(e^{z/2}),\qquad
\operatorname{Ti}_2(r)=\int_0^r\frac{\arctan t}{t}\,dt.
\tag{4}
\]

The original remaining target at \(A\) contributes \(-z\). Therefore
the complete action of the unchanged diagram is exactly

\[
\boxed{\quad \Phi=\min_{z\in\mathbb R}
             \{F(z)+q(z)-z\}.\quad}
\tag{5}
\]

This is the complete-capacity duality with the original targets. It is
not a filling equation or a geometric interpretation of a tilted
exterior. [The complete matched-sphere construction](actual_morse_geometric_contribution.md)
identifies \(2\pi\Phi\) with the volume of the original augmented exterior.

The useful identities for the restored triangle are

\[
q'(z)=\frac1\pi\arctan(e^{z/2}),\qquad
q''(z)=\frac1{4\pi\cosh(z/2)},\qquad
q(z)-\frac z2=q(-z)>0.
\tag{6}
\]

The last identity follows by differentiating both sides and evaluating
at zero. In particular \(q(0)=2G/\pi\), where
\(G=\operatorname{Ti}_2(1)\) is Catalan's constant.

## 2. The positive exterior exists for every finite real tilt

The strictly feasible table in (2) proves coercivity in the extracted
variables for every fixed finite \(z\). Indeed the recession function
is the sum of the triangle maxima minus the prescribed target pairing.
Equality with the strictly positive table forces a recession direction
to be constant on every supported triangle. Connectedness and the two
fixed boundary coordinates then make that direction zero. Compactness
of the unit sphere gives a positive recession margin. Changing finite
boundary values changes only bounded terms in this argument.

The triangle Hessians are graph Laplacians. After grounding \(C\),
their sum is positive definite. Thus the minimum exists uniquely for
every real \(z\), and the implicit function theorem gives a real
analytic interior solution \(w_I(z)\). This argument does not assume
that the tilted weights give a complete circle packing or a hyperbolic
link exterior.

For supported triangle weights \(a,b,c\), its conductance between two
distinct supported corners is

\[
g_{ab}=\frac{ab}{2\pi(a+b)\sqrt{ab+ac+bc}}.
\tag{7}
\]

The formula includes a protected third corner by setting \(c=0\).
A singleton triangle has zero Hessian. Parallel contributions from
distinct original triangles are all retained.

Differentiate the stationary interior equations with respect to \(z\).
The derivative vector has boundary values one at \(A\), zero at
\(C\), and is harmonic at every extracted face. The finite connected
network maximum principle gives

\[
0\le w_i'(z)\le1\qquad(i\in I).
\tag{8}
\]

Consequently, between \(z\) and \(z+s\), \(s\ge0\), every positive
weight is multiplied by a factor in \([1,e^s]\). The two positive
degree-one expressions
\(ab/(a+b)\) and \(\sqrt{ab+ac+bc}\) are coordinatewise increasing
and homogeneous. Each therefore increases by a factor in that same
interval. Their quotient in (7) yields

\[
e^{-s}g_{ab}(z)\le g_{ab}(z+s)\le e^s g_{ab}(z).
\tag{9}
\]

Minimizing the Dirichlet energy over the same boundary potentials
preserves both inequalities. Thus the actual Schur response satisfies

\[
\boxed{\quad e^{-s}\kappa(z)\le\kappa(z+s)
                         \le e^s\kappa(z),\quad s\ge0.\quad}
\tag{10}
\]

In particular,

\[
\begin{aligned}
\nu(z+s)&\ge\nu(z)+\kappa(z)(1-e^{-s}),\\
F(z+s)-F(z)&\ge\nu(z)s+\kappa(z)(s-1+e^{-s}),\\
\nu(z+s)+\kappa(z+s)&\ge\nu(z)+\kappa(z).
\end{aligned}
\tag{11}
\]

These are geometric-network inequalities for the original triangle
pressure. The root factorization of the odd polynomial gives the same
lower bound in the second line, but is not needed for its derivation.

## 3. A sufficient response region without a volume enclosure

Suppose

\[
                    0<\nu\le\frac12,\qquad
                    \nu+\kappa\ge\frac12.
\tag{12}
\]

The complete minimizer in (5) lies at positive \(z\): at zero the
derivative is \(\nu-3/4<0\), and the complete capacity has its strict
finite minimizer. For \(z\ge0\), (6) and (11) give

\[
\begin{aligned}
F(z)+q(z)-z
&\ge M-\kappa+
  (\nu+\kappa-1/2)z+\kappa e^{-z}+q(-z)\\
&\ge M-\kappa.
\end{aligned}
\tag{13}
\]

Hence

\[
                         M-\Phi\le\kappa.
\tag{14}
\]

The finite odd stable exterior supplies
\(0<\kappa\le\nu(1-\nu)\le1/4\). Its common-axis loss is

\[
\mathscr L(\nu,\kappa)=
-\frac12\log\max\{1-\nu-\kappa,
                         \nu-\kappa,1-4\kappa\}.
\tag{15}
\]

Under (12), the first two entries in the maximum are at most \(1/2\).
Since \(\kappa\le1/4\), they are strictly smaller than
\(e^{-2\kappa}\). The third entry is also strictly smaller than
\(e^{-2\kappa}\) for \(\kappa>0\). Therefore

\[
                \boxed{\quad M-\Phi\le\kappa
                                   <\mathscr L(\nu,\kappa).\quad}
\tag{16}
\]

Applying the existing common-axis theorem, including its original
omitted-tail estimate, proves a strict rate gap for the original
odd-level singleton at \((+2,-2,\ldots,-2)\). A limiting gap is at
least

\[
\min\{\mathscr L(\nu,\kappa)-\kappa,\ \gamma/2\},
\tag{17}
\]

where \(\gamma\) is the original complete omitted-tail gap. This
criterion uses only the exterior load and effective response; it does
not rephrase the desired inequality using an unknown \(\Phi\).
It is independent of the number of triangles and of graph cycles.

## 4. The weighted rate throughout the half-load interval

Put \(H(z)=F(z)-z/2\). Strict complete feasibility supplies an exterior
feasible load strictly greater than \(1/2\) at \(A\), so the positive
pressure derivative eventually exceeds \(1/2\). There is a unique
finite \(z_{1/2}\ge0\) with

\[
\nu(z_{1/2})=\frac12,\qquad
\min_{z\in\mathbb R}H(z)=H(z_{1/2}).
\tag{18}
\]

Let \(z_*\) be the finite attained complete minimizer in (5). Equation
(6) gives the strict comparison

\[
             \Phi=H(z_*)+q(-z_*)>H(z_{1/2}).
\tag{19}
\]

At any \(0\le z\le z_{1/2}\), write
\(a=1/2-\nu(z)\ge0\) and \(k=\kappa(z)>0\). By (11) and (12),
\(a\le k\). For \(0\le s\le z_{1/2}-z\),

\[
0\le\frac12-\nu(z+s)\le a-k(1-e^{-s}).
\tag{20}
\]

If \(a<k\), the right side vanishes at
\(T=-\log(1-a/k)\); the half-load point occurs no later than this
value. Integrating (20), and using its limiting value when \(a=k\),
gives the sharper action bound

\[
\begin{aligned}
H(z)-H(z_{1/2})
&\le J(a,k),\\
J(a,k)&=a+(k-a)\log(1-a/k)\le k,\qquad 0\le a\le k.
\end{aligned}
\tag{21}
\]

Here \(0\log0=0\). It follows that the weighted rate proposed for the
coupled spectral estimate satisfies

\[
\boxed{\quad
F(z)-\frac z2+\frac12\log(1-4\kappa(z))<\Phi,
\qquad 0\le z\le z_{1/2}.\quad}
\tag{22}
\]

Indeed \(-\frac12\log(1-4k)>2k\ge J(a,k)\) for \(0<k<1/4\).
At \(k=1/4\), the left side has value \(-\infty\). Compactness of
the interval gives a uniform strict margin. If

\[
                       b=\nu+\kappa-1/2>0,
\tag{23}
\]

then (20) at zero gives
\(z_{1/2}\le-\log(b/\kappa)\); hence (10) implies
\(\kappa(z)\ge b\) throughout the interval. In particular the margin
in (22) is greater than \(b\). The sharper expression in (21) may be
used instead.

This is a geometric comparison for the displayed rate. Section 9
applies the separate odd stable-section estimate to the actual cap
contraction. There is no asserted even-level analogue.

## 5. Comparison with complete-packing weak balance

Let \(z_*\) be the original complete minimizer in (5). At this cap the
complete-packing weak-balance test is exactly

\[
                             q(z_*)\ge z_*.
\tag{24}
\]

The other middle is protected and carries no surviving one-sided
condition. This is a test at the restored complete packing, whereas
(12) uses the exterior stationary point with \(A=C\).

For the present interior-cap problem, (24) implies (12). Here is a
quantitative proof. The function \(q(z)-z\) is strictly decreasing.
At \(z=\log(5/2)\),

\[
q(-z)<\frac2\pi\sqrt{\frac25}<\frac49<\frac z2.
\tag{25}
\]

For the last inequality,
\(\log(5/2)=2\operatorname{artanh}(3/7)
>6/7+18/343>8/9\). Thus (24) implies
\(1<t=e^{z_*}<5/2\). At the complete stationary point,

\[
\nu(z_*)=1-q'(z_*)>\frac58,
\tag{26}
\]

because \(\sqrt{5/2}<\tan(3\pi/8)=1+\sqrt2\).

For each root parameter \(p\in[0,1]\) of the original odd stable
polynomial, its positive-tilt value is
\(p_t=tp/(1-p+tp)\). Direct algebra gives

\[
p(2-p)\ge\min\{1,2/t\}\,p_t>\frac45p_t
\quad\text{when }p_t>0.
\tag{27}
\]

To see the nonstrict inequality, divide by \(p_t\) when it is nonzero.
The ratio \((2-p)(1+(t-1)p)/t\) is a concave quadratic in \(p\), so
its minimum occurs at an endpoint. Average, pass to the same positive
pressure, and use (26):

\[
\nu+\kappa=\int p(2-p)\,d\mu(p)
            >\frac45\nu(z_*)>\frac12.
\tag{28}
\]

Consequently, within the stated range \(0<\nu\le1/2\), every cap
satisfying complete weak balance belongs to the response region.
The ordinary coordinates are not exchanged: \(A\) remains the
overloaded middle in (1), as required by the restoration formula.
This proof does not require weak balance at the
other regions, whose source terms are central in this singleton.
However, this note does not prove that (12) gives a strict enlargement
within the realizable interior-cap matched-sphere class. A stable
binary polynomial by itself would not establish such a geometric
classification. In particular no new full knot-volume class is claimed.

## 6. Exact positive tilt of the original common-axis inequality

There is a separate, exact way to optimize the positive boundary ratio
without changing the cap moments. At a finite odd level let \(d=N-1\),
and set \(\rho=e^z>0\). Normalize the actual binary exterior by

\[
\frac{P_N(\rho A,C)}{P_N(\rho,1)}
=\prod_{r=1}^d[(1-p_r(z))C+p_r(z)A].
\tag{29}
\]

Let \(\nu_d(z),\kappa_d(z)\) be its mean and mean Bernoulli variance,
and write \(a=e^{-z}\). Applying the squared-factor arithmetic-geometric
mean inequality before maximizing the common negative-axis parameter
gives

\[
\begin{aligned}
\max\{B_N^-,B_N^+\}
&\le P_N(e^z,1)\,\mathcal R_d(z)^{d/2},\\
\mathcal R_d(z)=\max\bigl\{&1-\nu_d-\kappa_d,
 a^2(\nu_d-\kappa_d),\\
 &1-2(1+a)\nu_d+(1+a)^2(\nu_d-\kappa_d)\bigr\}.
\end{aligned}
\tag{30}
\]

Indeed the normalized factors on the two original intervals are
\((1-p)-atp\) and \(t(1-p)-ap\), \(0\le t\le1\). Their averaged
squares are convex quadratics in the same \(t\). Their three endpoint
values are exactly those in (30).

The original cap moment pairing and omitted finite tail are unchanged.
Thus, after the established pressure limit,

\[
\limsup_{N\text{ odd}}\frac1N\log|S_N|
\le\max\left\{
\inf_{z\in\mathbb R}\left[F(z)+\frac12\log\mathcal R(z)\right],
\Phi-\frac\gamma2\right\},
\tag{31}
\]

where \(\mathcal R\) uses the actual \(\nu(z),\kappa(z)\). It is
enough to use any certified finite collection or interval of real
tilts. The cap weights have not been rescaled independently, and the
polynomial value \(P_N(e^z,1)\) is retained. Dropping that factor would
give an incorrect free gain from changing radii.

Equation (30) is distinct from the weighted expression in (22). This
note does not identify the two bounds or attribute (22) to (30).

## 7. Why stability and two moments alone cannot settle every geometry

There is an elementary obstruction to deducing a universal result from
only an abstract stable binary exterior and the formal restoration
formula. For \(0<\varepsilon<1\), take the root measure with mass
\(2/5\) at \(7/10\) and mass \(3/5\) at \(\varepsilon\). Its
normalized pressure is

\[
F_\varepsilon(z)-M
=\frac25\log\left(\frac3{10}+\frac7{10}e^z\right)
 +\frac35\log(1-\varepsilon+\varepsilon e^z).
\tag{32}
\]

It is realized by genuine stable binary polynomials of degrees divisible
by five, has full coefficient support, and has positive response. As
\(\varepsilon\downarrow0\), its initial mean and response tend to
\(7/25\) and \(21/250\). Nevertheless, evaluating the formal
restoration at \(z=\log(1/\varepsilon)\) gives

\[
M-\inf_z[F_\varepsilon(z)+q(z)-z]
\ge\frac1{10}\log\frac1\varepsilon
-\frac35\log2-\frac{2\sqrt\varepsilon}{\pi}
\longrightarrow+\infty.
\tag{33}
\]

The actual negative-axis supremum has a finite lower rate from its
endpoint \(P_N(0,1)\):

\[
M+\frac25\log\frac3{10}
 +\frac35\log(1-\varepsilon).
\tag{34}
\]

Hence no correct positive-tilt upper bound for that entire supremum can
pay the restoration excess for all these abstract polynomials. This
does not construct a matched-sphere counterexample. In fact the
unbounded excess is incompatible with the existing positive
one-cap geometric pyramid budget in its stated strict range. The
example isolates the additional geometric restriction needed by any
universal argument; real stability, complete support and positive
response do not supply it alone.

## 8. Proof inputs and limits

The [common-axis theorem](research_cap_common_axis_bound.md) supplies the
original extraction, moment weights, odd stable factorization,
squared-factor estimate and omitted-tail bound. The exact restoration
of the two complete triangles is recorded in
[the cap-capacity comparison](research_cap_constrained_capacity_budget.md)
and [the algebraic boundary pressure](research_cap_algebraic_boundary_curve_and_volume_period.md).
The [effective-response theorem](research_global_cap_effective_response_criterion.md)
gives the original triangle conductance and positive coefficient packet.
The limitation discussed in section 7 is compared with
[the original one-cap geometric volume budget](research_one_cap_original_chain_volume_budget.md).

Sections 2–6 keep these original loads and the same complete action.
The Dirichlet estimate controls how the exterior changes with its
positive boundary ratio; the restoration formula compares that change
with the complete packing. The signed source is retained until the
whole exterior has been extracted. The tilted weights are not asserted
to describe another hyperbolic manifold.

## 9. Odd singleton consequence on the entire real cap interval

Use the finite sine-Cauchy metric and stable alternating-section lemma
from [the stable-section proof](research_cap_uniform_spectral_gap.md),
sections 1–2. Those are additional finite-source inputs, separate from
the geometric comparison above. Their hypotheses hold for the original
odd central exterior, with its actual determinant factors and all
extracted targets.

For clarity, put
\[
d=N-1,\qquad M_N=\lfloor N/2\rfloor-1,\qquad
Q_{N,M_N}(t)=\sum_{j=0}^{M_N}(-1)^jp_{N,j}t^j .
\tag{35}
\]

Here \(M_N\) is a cutoff degree, distinct from the pressure \(M=F(0)\).
The finite metric theorem bounds the full real cap spectrum by a
polynomial multiple of \(\|Q_{N,M_N}\|_C\), where
\[
\|Q_{N,M_N}\|_C^2
=\alpha_N\int_0^\infty
        \frac{|Q_{N,M_N}(t)|^2}{1+t^N}\,dt,
\qquad 0<\alpha_N\le1,\qquad
\|t^{M_N}\|_C\le1.
\tag{36}
\]

Take \(T=e^{z_{1/2}}\). The finite stable-section proof gives a
pointwise bound on \(0\le t\le T\) by
\(|P_N(-t,1)|+p_{N,M_N}t^{M_N}\). On \(t\ge T\), its log-concavity
and log-convex pressure argument gives the bound
\[
\left(\max\{P_N(T,1)/T^{M_N},(d+1)p_{N,M_N}\}
                          +p_{N,M_N}\right)t^{M_N}.
\tag{37}
\]

The proof covers support ending at or before \(M_N\), support starting
after it, and zero endpoint coefficients; no coefficient-ratio bound
is required. This is an estimate for the actual truncated alternating
polynomial, not for the full square integrated past its moment range.

For \(0\le t\le1\), the original common-axis bound gives rate at most
\(M-\mathscr L(\nu,\kappa)<\Phi\). For \(1\le t\le T\), put
\(z=\log t\). The same actual polynomial, normalized at this positive
tilt, satisfies
\[
|P_N(-e^z,1)|
\le P_N(e^z,1)(1-4\kappa_d(z))^{d/2}
\le P_N(e^z,1)e^{-2d\kappa_d(z)}.
\tag{38}
\]

The pressure and its first two normalized derivatives converge
uniformly on the compact interval \([0,z_{1/2}]\). To justify this
use of the derivative, apply the original positive coefficient packet
at each real tilt. Section 2 supplies the unique strict stationary
interior point at every tilt. These points form a compact set; the
grounded Hessians stay positive and the same connected, primitive
ordinary phase graph gives a strict complementary angular gap.
The determinant derivatives are uniformly bounded on small complex
neighborhoods. A finite subcover therefore gives relative holomorphic
packets with uniform error on the interval. Analytic logarithms and
Cauchy differentiation give the asserted convergence. This is not
differentiation of a pointwise rate or a continuation to the negative
axis.

After the factor \(t^{d/2}\) is removed in the integral (36), (38)
has limiting rate \(H(z)-2\kappa(z)\). Equation (21) shows this is at
most \(H(z_{1/2})-\kappa(z)\). The minimum of \(\kappa(z)\) on the
compact interval is positive. Thus the bounded part of the integral
is strictly below \(\Phi\), uniformly; the estimate also avoids a
logarithmic continuity issue if \(\kappa(z)=1/4\).

The first term of (37) has rate
\[
\lim_N\frac1N\log\frac{P_N(T,1)}{T^{M_N}}
=F(z_{1/2})-\frac{z_{1/2}}2
=H(z_{1/2})<\Phi .
\tag{39}
\]

The bounded difference between \(M_N\) and \(d/2\) changes no rate.
The original closed coefficient-capacity theorem bounds
\(p_{N,M_N}\) by rate at most \(\Phi-\gamma_D\), for some
\(\gamma_D>0\), because \(M_N/d\to1/2\). The finite norm
\(\|t^{M_N}\|_C\le1\) completes the unbounded-tail estimate.

Consequently, under (12), the original signed singleton satisfies
\[
\boxed{\quad
\limsup_{\substack{N\to\infty\\N\ \mathrm{odd}}}
\frac1N\log\sup_{\sigma\in[-2,2]}|S_N(\sigma)|
\le \Phi-\delta,\qquad
\delta=\min\{\mathscr L(\nu,\kappa)-\kappa,\,
             \Phi-H(z_{1/2}),\,\gamma_D\}>0 .
\quad}
\tag{40}
\]

Every other original region retains its central numerator at spectrum
\(-2\). The result concerns one original sector and one free spectral
variable. It supplies no estimate for varying neighboring spectra,
several noncentral regions, the even central exterior or the entire
filled invariant. In particular this corollary is not a new
knot-volume theorem.
