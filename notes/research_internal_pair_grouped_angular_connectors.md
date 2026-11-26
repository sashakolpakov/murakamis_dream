# Grouped angular connectors for every positive internal pair

Research proof, updated 4 November 2026. Frozen manuscripts are unchanged.

The folded angular endpoint terms become uniformly smaller than the
geometric rate when paired with the whole other trace. This uses its
exact half-band source, not an independent asymptotic or a worst-case
bound for each horizontal trace piece. The result holds at complete
outside colors, through both level parities, with every original
physical first normal retained. Section 5 extends the grouped estimate
to free outside colors, using actual physical values and normals on the
whole contour. This supplies an upper bound throughout the real outside
period and a fixed complex neighborhood of completeness; it does not
assert decay as a real outside angle moves away from completeness.

## 1. Exact decomposition of one original trace

Fix a real wire interval \(I=[\alpha,\beta]\Subset(0,1/2)\)
containing the retained indices of the
[combined contour reduction](research_internal_pair_combined_contour_reduction.md).
Use a slightly larger compact interval for estimates, so that
all \(O(N^{-1})\) half-grid adjustments are included.
Put \(D=N-1\), \(\eta=(-1)^D\), and
\[
 C_{N,n}=e^{\pi i nD^2/(4N)},\qquad
 W_{n,N}(x)=\phi_N[R^n\mathbf B_N(x)K_N(\,\cdot\,,0)] .
 \tag{1}
\]
The function \(W_{n,N}\) is the actual half-band source with
frequencies \(-D/2,-D/2+1,\ldots,D/2\).
For a midpoint angular cut \(T_N=T+O(N^{-1})<\pi\),
\(e^{iNT_N}=-\eta\), let \(O_{n,N}\) be its original omitted
physical residues. Every first normal remains with its root.

Use the exact factorial representative \(B_N(x,t)\) in the
retained trace, and define
\[
 g_{n,N}(x,t)=
 \sin t\,B_N(x,t)K_N(t,0)e^{inNt^2/(4\pi)} .
 \tag{2}
\]
It is odd in \(t\). Choose a positive endpoint height
\(\epsilon_n\), and any permitted lower path
\(\Gamma_n(x)\) from \(-T_N-i\epsilon_n\) to
\(T_N-i\epsilon_n\). The exact folded trace identity gives
\[
 \begin{split}
 H_{n,N}(x)
  &=-\frac{N^2C_{N,n}}{\pi i}
    \int_{\Gamma_n(x)}
      \frac{g_{n,N}(x,t)e^{-iNt}}
                  {(1-\eta e^{-iNt})^2}\,dt,\\
 V_{n,N}(x)
  &=\frac{\eta N^2C_{N,n}}{\pi}
    \int_{-\epsilon_n}^{\epsilon_n}
       \frac{g_{n,N}(x,T_N+is)}
                         {4\cosh^2(Ns/2)}\,ds,\\
 W_{n,N}(x)&=H_{n,N}(x)+V_{n,N}(x)+O_{n,N}(x).
 \end{split}
 \tag{3}
\]
All scalars, charges, and folded endpoint signs in (3) are
those of the
[original exact trace](research_exact_complete_trace_contour.md#3-removing-outer-grid-points-before-contour-deformation).
In particular the double-pole denominator retains the first
normal; it has not been replaced by a single Fourier mode.
The odd simple node remains in the retained trace.

The exact identity holds pointwise in \(x\). The lower paths
and their endpoint heights may therefore taper with \(x\),
as proved in the
[endpoint-taper lemma](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_endpoint_taper.md).
The estimates below remain uniform if their positive endpoint
heights stay below the chosen \(\epsilon_n\).

## 2. The exact factorial exponent at the angular endpoint

Let \(\mathfrak b(x,t)\) be the original continuous factorial
upper exponent, with both terms of each reciprocal reflection
included. On every fixed compact wire strip,
\[
                     \mathfrak b(x,\pi)=\pi|\Im x|.
 \tag{4}
\]
Indeed \(J(1-x)=-J(x)\), so
\(b(x,\pi)=-J(-x)-J(x)\).
For \(\Im x>0\), the argument \(-x\) uses the lower
continuation \(J_-(-x)=-J(x)+i\pi x\), hence
\(b(x,\pi)=-i\pi x\). For \(\Im x<0\), the upper continuation
gives \(b(x,\pi)=i\pi x\). Their real boundary values agree
when \(\Im x=0\).

This normalization can also be seen directly, without dropping
an endpoint zero:
\[
 B_N(x,\pi)=\frac{2\cos(\pi Nx)}N
       \left(\frac{G_N(Nx-1/2)}{G_N(Nx)}\right)^2 .
 \tag{5}
\]
Use \(G_N(z)G_N(N-1-z)=N\) and the exact reciprocal reflection
to obtain (5). The cosine keeps both exponential terms.
Its absolute upper exponent is exactly that in (4).

Fix \(Y_0<\infty\). On
\(\Re x\in I\), \(|\Im x|\le Y_0\), the factorial arguments
at \(t=\pi\) stay away from their integer singularities,
except for crossing the negative real cut. The real upper
primitive is continuous across that cut and has bounded
one-sided derivatives on this compact set. Therefore
\[
 \mathfrak b(x,T+is)
 \le\pi|\Im x|+\omega_I(\pi-T+|s|),\qquad
                    \omega_I(\rho)\longrightarrow0 .
 \tag{6}
\]
One may take \(\omega_I(\rho)=C_I\rho\) for sufficiently
small \(\rho\). The exact uniform factorial bound then gives
\[
 |B_N(x,T_N+is)|\le CN^A
    e^{N\{\pi|\Im x|+\omega_I(\pi-T+|s|+O(N^{-1}))\}}.
 \tag{7}
\]
This remains valid on the real cut and at every reciprocal
factorial zero. It is an estimate of the actual interpolation
inside the original trace, not just of its lattice values.

## 3. The complete outside factor on a short vertical segment

Write \(\Psi(t)=\psi(t,0)\). For fixed \(T<\pi\), choose
\(\epsilon>0\) small enough that the vertical segment
\(T+i[-\epsilon,\epsilon]\) and a neighborhood of it satisfy
\(\Re(-2\cos t)<2\). For \(T>\pi/2\), it suffices to choose
\(2\epsilon<(\pi-T)/2\), with a strict margin for midpoint
rounding. Indeed
\(\cos(\pi-T)\cosh((\pi-T)/2)<1\).

The actual low complete-end kernel has
\(\exp\{N\Psi(t)+O(\log N)\}\) on this compact neighborhood,
by the last-row and even low-kernel theorems. The complete
radical obeys \(N^2e^{N|\Im t|}\). Thus the full kernel,
through both parities, satisfies
\[
 |K_N(T_N+is,0)|\le CN^A e^{N\kappa(T,\epsilon)},\qquad
 \kappa(T,\epsilon)=
 \max\left\{\sup_{|s|\le2\epsilon}\Re\Psi(T+is),\,2\epsilon\right\}
                         +o_{N\to\infty}(1).
 \tag{8}
\]
Here the slightly larger neighborhood absorbs rounding
and fixed selected-variable derivatives; decrease
\(\epsilon\) first if necessary.
Since \(J\) is continuous at the endpoint arguments,
\(\Psi(t)\to0\) as \(t\to\pi\) within this domain.
Consequently \(\kappa(T,\epsilon)\) can be made arbitrarily
small by first taking \(T\) close to \(\pi\), then choosing
\(\epsilon\) sufficiently small.
No bound on free outside-color derivatives is inferred
from this complete-end estimate.

**Lemma 1.** Given \(q>0\), choose \(T<\pi\) sufficiently
close to \(\pi\). For every fixed integer \(n\), its positive
endpoint height \(\epsilon_n\) can then be chosen so that
\[
 |V_{n,N}(x)|\le CN^A e^{N\{\pi|\Im x|+q\}},
                 \qquad \Re x\in I,\quad |\Im x|\le Y_0 .
 \tag{9}
\]

*Proof.* The vertical weight in (3) has modulus at most
\(1/4\). The sine and fixed curve length are bounded.
The original crossing Gaussian has modulus
\[
 \left|e^{inN(T_N+is)^2/(4\pi)}\right|
       \le \exp\{N|n|(T+o(1))|s|/(2\pi)\}.
 \tag{10}
\]
Combining (7)--(10), the exponent in excess of
\(\pi|\Im x|\) tends to zero as \(T\to\pi\) and then
\(\epsilon_n\to0\). The factor \(N^2C_{N,n}\) in (3)
costs only a polynomial because \(|C_{N,n}|=1\).
Choose these parameters with a strict margin below \(q\).
This proves the assertion for all sufficiently large levels;
the remaining finite levels are absorbed in the constant.
\(\square\)

## 4. Group with the whole other trace before taking absolute values

The
[physical-tail and half-band theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_angular_tail_transport.md)
gives, on the whole complex wire plane with bounded height,
\[
 \begin{split}
 |W_{n,N}(x)|&\le CN^A
              e^{N\{3M_\infty/2+\pi|\Im x|\}},\\
 |O_{n,N}(x)|&\le CN^A
              e^{N\{m(T_0)+\Psi(T_0)+\pi|\Im x|\}} .
 \end{split}
 \tag{11}
\]
Here \(T_0<T_N\) is a fixed nearby lower cut and
\(m(T_0)+\Psi(T_0)\to0\) as \(T_0\to\pi\).
These bounds reconstruct each half-band function separately
from its \(N\) original samples. They include high Newton
indices, every physical first normal, and both parities.

Choose \(T_0<T<\pi\) close enough to \(\pi\) and the endpoint
heights in Lemma 1 so that both small exponents are below
\(q<1/100\). Put \(D_n=V_n+O_n\). Then
\[
 |D_n(x)|\le CN^A e^{N\{\pi|\Im x|+q\}},\qquad
 |H_n(x)|\le CN^A
              e^{N\{3M_\infty/2+\pi|\Im x|\}},
 \tag{12}
\]
where the second inequality follows from the exact identity
\(H_n=W_n-D_n\).

**Theorem 2.** On the retained wire strip at the actual
geometric pair height \(Y=\Im x_*\),
\[
 |W_n(x)W_p(x)-H_n(x)H_p(x)|
 \le CN^A
       e^{N\{3M_\infty/2+2\pi|\Im x|+q\}}
 <CN^A e^{N(M_{n,p}-1/100)}
 \tag{13}
\]
for \(\Re x\in I\), \(|\Im x|\le Y\), after the choices above.

*Proof.* Use the exact grouping
\[
 W_nW_p-H_nH_p=D_nW_p+H_nD_p .
 \tag{14}
\]
Thus every folded angular connector and every omitted
physical-angle term is retained, including their intersections.
Equations (11)--(12) give the first bound in (13).
The actual wire-height theorem gives \(2\pi Y<3/4\).
Together with \(M_\infty<7/6\), \(q<1/100\), and
\(M_{n,p}\ge M_{3,3}>63/25\), this yields
\[
 \frac32M_\infty+2\pi Y+q
       <\frac74+\frac34+\frac1{100}
        =\frac{251}{100}<M_{n,p}-\frac1{100}.
 \tag{15}
\]
All these scalar and geometric inputs are proved in the
physical-tail and wire-height note. \(\square\)

For the retained-index Cauchy formula, the exact wire kernel
is \(1/(1-e^{2\pi iNx})\). It is bounded on a fixed positive
upper height, has the favorable factor
\(e^{-2\pi N|\Im x|}\) on a lower height, and has modulus at
most one on a half-index vertical side. Multiplication by
that kernel and integration therefore preserve the strict
gap (13), with only polynomial factors. The conclusion also
holds for the wire graphs and pointwise trace tapers of the
endpoint-collar construction, provided their heights stay
within \([-Y,Y]\) and the angular endpoint heights stay below
the chosen \(\epsilon_n,\epsilon_p\).

After combining this theorem with the real-tail and
endpoint-collar reductions, the unresolved contour consists
of the two joint lower-trace integrals over the middle wire
band, including its exact wire alias. The original first
normals and all higher trace charges are still present in
those integrals. No independent geometric asymptotic for
\(W_n\) or \(W_p\) was assumed.

The extension below replaces the complete-point inputs in (8) and
(11) by estimates of the actual finite polynomials. It does not
continue a relative error known only at the complete outside color.

## 5. Free outside colors, original normals, and coupled trace surfaces

Write the two ordinary outside colors as
\(\zeta=-2\cos u\) and \(\omega=-2\cos v\). All derivatives in
\(\zeta,\omega\) below are ordinary polynomial derivatives, including
at \(-2\); they are not angular derivatives divided by a vanishing
sine. Let \(L_N(w,\zeta)\) be the literal low Newton kernel and
let \(K_N-L_N\) be the full original radical. Replace \(K_N(t,0)\)
in (1)--(3) by \(K_N(t,u)\), and denote the resulting exact
functions by \(W_n(x;\zeta),H_n(x;\zeta),V_n(x;\zeta),O_n(x;\zeta)\).
They retain the identity \(W_n=H_n+V_n+O_n\). Indeed the new
factor remains even in the trace angle, so the original folding,
double-pole weights, and odd-level simple endpoint are unchanged.

**Lemma 3 (whole-contour upper bound).** Let \(\mathcal T\) be a
compact set of trace angles whose color image is contained in
\(\Re w<2\). Suppose, on a neighborhood of this compact set,
\[
             \Re\Psi(t)>|\Im t|+\delta,\qquad \delta>0.
 \tag{16}
\]
For every fixed ordinary outside derivative order \(k\), uniformly
for \(t\in\mathcal T\), \(-\pi\le\Re u\le\pi\), and bounded
\(|\Im u|\),
\[
 \left|\partial_\zeta^k K_N(-2\cos t,\zeta)
                           \big|_{\zeta=-2\cos u}\right|
 \le C_kN^{A_k}
            e^{N\{\Re\Psi(t)+|\Im u|\}}.
 \tag{17}
\]
All fixed ordinary selected-color derivatives satisfy the same
bound after shrinking the selected-color neighborhood and increasing
the polynomial power.

*Proof.* Equations (5) and (9) of the
[free-outside observation theorem](research_free_boundary_half_charge_observation.md#1-a-whole-contour-bound-from-the-actual-physical-rows)
give, respectively, the actual low-kernel and radical bounds
\[
 \begin{split}
 |\partial_\zeta^k L_N(-2\cos t,-2\cos u)|
       &\le C_kN^{A_k}e^{N\Re\Psi(t)+J_N|\Im u|},\\
 |\partial_\zeta^k(K_N-L_N)(-2\cos t,-2\cos u)|
       &\le C_kN^{A_k}e^{D(|\Im t|+|\Im u|)},
       \qquad J_N=\lfloor(N-1)/2\rfloor .
 \end{split}
 \tag{18}
\]
The first estimate follows from the original row recurrence,
ordinary Chebyshev interpolation, and the polynomial Bernstein
bound. The second is the original radical Fourier bound.
Since \(J_N,D\le N\), (16) proves (17). The estimates hold on a
fixed selected-color neighborhood inside \(\Re w<2\).
Cauchy's formula on color circles of radius \(1/N\) costs only
powers of \(N\); the change in \(\Re\Psi(w)\) on such circles
is \(O(1/N)\). This proves the derivative assertion even when
the angular coordinate is ramified at \(t=0\). \(\square\)

Every fixed angular cut \(T<\pi\) admits sufficiently small
positive heights for (16): \(\Psi(\tau)\ge\Psi(T)>0\) for
\(|\tau|\le T\), and the color image remains in \(\Re w<2\)
at small heights. The half-charge rectangle
\(|\Re t|\le\pi/2,\ |\Im t|\le2/5\) has the same property by
the proved complete-edge gap. Thus this lemma applies to whole
retained contours, not merely near their stationary points.
It is an upper bound; it does not assert a nonzero free-outside
packet on an enlarged selected-color domain.

**Theorem 4 (free-outside grouped connectors).** Fix the integer
powers \(n,p\ge3\), the compact wire interval \(I\), and the
actual pair height \(Y\). Given sufficiently small \(q>0\), choose
the cuts and positive endpoint heights as in Lemma 1. Then, for
each fixed \(k,\ell\ge0\),
\[
 \begin{split}
 &\left|\partial_\zeta^k\partial_\omega^\ell
       \{W_n(x;\zeta)W_p(x;\omega)
                  -H_n(x;\zeta)H_p(x;\omega)\}\right|\\
 &\qquad\le CN^A
   e^{N\{3M_\infty/2+2\pi|\Im x|+q+|\Im u|+|\Im v|\}},
 \quad \zeta=-2\cos u,\quad\omega=-2\cos v ,
 \end{split}
 \tag{19}
\]
uniformly for \(\Re x\in I,\ |\Im x|\le Y\), all real
outside angles, and a fixed bounded strip in those angles.
In particular there are fixed ordinary color disks about
\(\zeta=\omega=-2\), independent of \(N\), on which the
right side is at most
\[
                         CN^A e^{N(M_{n,p}-3/200)}.
 \tag{20}
\]
The same strict estimate holds throughout the real outside
period. Neither assertion includes a positive loss proportional
to \(1-\cos u\) or \(1-\cos v\).

*Proof of the endpoint estimate.* Fix \(T<\pi\) first, then
choose the endpoint height sufficiently small for (16) on
\(T+i[-2\epsilon_n,2\epsilon_n]\). The supremum of
\(\Re\Psi\) on this segment tends to zero as \(T\to\pi\) and
then \(\epsilon_n\to0\). Lemma 3, the exact factorial estimate
(7), and the crossing estimate (10) therefore prove
\[
 |\partial_\zeta^k V_n(x;\zeta)|
       \le CN^A e^{N\{\pi|\Im x|+q+|\Im u|\}}.
 \tag{21}
\]
The fixed ordinary outside derivatives were estimated in (18)
before the endpoint integral. No derivative estimate has been
inferred from its complete-point value.

*Proof for the whole source and omitted rows.* At a double
physical node \(c_a\), put
\(F_{a,N}(\zeta)=K_N(c_a,\zeta)\) and
\(G_{a,N}(\zeta)=\partial_wK_N(c_a,\zeta)\).
The exact physical-row bound (11) in the free-outside observation
note states
\[
 |\partial_\zeta^k F_{a,N}(-2\cos u)|
       +|\partial_\zeta^k G_{a,N}(-2\cos u)|
       \le C_kN^{A_k}F_{a,N}(-2)e^{D|\Im u|}.
 \tag{22}
\]
At the odd simple node only the value term is used. Formula
(22) includes the full kernel and its actual selected first
normal, not only its low part.

Apply the original Hermite trace to each literal sample
\(x=j/N\). The crossing values and first normals have polynomial
size for fixed \(n\). All-color Newton values and their required
ordinary first normals have rate at most
\(m(0)=M_\infty/2\), while \(F_{a,N}(-2)\) has rate at most
\(M_\infty\). Thus every sample of \(\partial_\zeta^kW_n\)
has rate at most \(3M_\infty/2+|\Im u|\).
For omitted angular nodes \(|t_a|\ge T_0\), the actual
[physical-tail theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_angular_tail_transport.md)
instead gives rates \(m(T_0)\) for the Newton value and normal,
and \(\Psi(T_0)\) for \(F_{a,N}(-2)\).
The normal estimate is on the corresponding real color interval
before restriction to nodes, so Markov differentiation preserves
the exponent. Hence omitted samples have rate
\(m(T_0)+\Psi(T_0)+|\Im u|\).

For every outside derivative these remain exact half-band functions
of \(x\). Reconstruct each function separately from its \(N\)
samples. The cardinal bound adds \(\pi|\Im x|\) to its rate
and only polynomial factors. Consequently
\[
 \begin{split}
 |\partial_\zeta^kW_n(x;\zeta)|
   &\le CN^A e^{N\{3M_\infty/2+\pi|\Im x|+|\Im u|\}},\\
 |\partial_\zeta^kO_n(x;\zeta)|
   &\le CN^A e^{N\{m(T_0)+\Psi(T_0)
                                      +\pi|\Im x|+|\Im u|\}} .
 \end{split}
 \tag{23}
\]
All original first normals and both level parities have been
retained in this construction.

Take \(T_0,T\) close enough to \(\pi\) that the small exponent
in (23) is below \(q\). Equations (21)--(23) give the analogues
of (12), with the added \(|\Im u|\). The exact grouping (14),
and Leibniz's rule for its fixed ordinary derivatives, prove
(19).

For (20), take \(q<1/400\) and choose the ordinary color disks
small enough that their small angular lifts satisfy
\(|\Im u|+|\Im v|<1/400\). Such disks exist because
\(-2\cos u+2=u^2+O(u^4)\); the two small lifts differ only by
sign and the actual functions are polynomials in the color.
Using \(2\pi Y<3/4,\ M_\infty<7/6,\ M_{n,p}>63/25\),
\[
 \frac32M_\infty+2\pi Y+q+|\Im u|+|\Im v|
       <\frac74+\frac34+\frac1{200}
       =\frac{501}{200}<M_{n,p}-\frac3{200}.
 \tag{24}
\]
For all real \(u,v\) the imaginary costs vanish, so the same
conclusion holds uniformly on the real outside period. The
wire kernel and its half-grid vertical sides are treated
exactly as after (15). \(\square\)

The theorem is also compatible with a coupled lower-trace
surface. For each fixed wire point, start with the product
of the two constant-height lower segments, with endpoint
heights \(\epsilon_n,\epsilon_p\). Replace it by a smooth
graph
\[
  (\tau,\rho)\longmapsto
       (\tau-ih_n(\tau,\rho),\rho-ih_p(\tau,\rho)),
       \qquad -T_N\le\tau,\rho\le T_N ,
 \tag{25}
\]
which agrees with that product on its entire boundary, has
strictly positive heights, and stays in the regular domain
of the finite factorial representatives. Suppose its homotopy
to the product has these properties as well.
The product of the two original lower-trace densities is a
closed holomorphic two-form below the physical poles.
Stokes' theorem relative to the fixed boundary therefore
identifies its integral on (25) with \(H_nH_p\), with the
literal scalar and pullback Jacobian retained. There is no
additional boundary term from the interior coupling of the
heights. Its existing folded endpoint curtains are exactly
the ones already included in (19).

This equality may be applied pointwise along the wire contour.
Height derivatives in the wire direction disappear after
wedging with \(dx\), or equivalently by the pointwise residue
identity and Fubini. Thus (19)--(20) also control the difference
between the original product and this coupled lower-trace
integral. The statement does not bound that integral itself
or prove a global pair coefficient. A whole-boundary decay
estimate for the remaining main integral, required for further
composition, remains separate from the upper bounds proved here.
